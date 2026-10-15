#!/usr/bin/env python3
"""Human-sounding line synthesis, engine-agnostic (DL-033 VieNeu, DL-035 F5-TTS). Run with the TTS venv:
  /workspace/tts-venv/bin/python pipeline/scripts/voice-prosody.py job.json      (job = {"jobs":[...]} )
  /workspace/tts-venv/bin/python pipeline/scripts/voice-prosody.py --metrics a.wav b.wav ...   (F0/pause stats only)

Why: synthesizing a whole sentence and then time-stretching it (old path: atempo ×1.3) flattens
pitch, removes pauses and smears consonants. Instead, per LINE:
  1. split into PHRASES (breath groups, 2-8 syllables), each keeps its own punctuation so the model
     closes it with a phrase-final contour ("…" trails off, "?" rises, "," continues);
  2. crafted GAPS between phrases (150-400 ms; comma ≈180, colon ≈260, ellipsis ≈380), filled with
     room tone, never digital silence;
  3. per-phrase delivery: tempo (0.88-1.12), pitch (±1.5 st), gain (dB). Emphasis phrase = slower
     tempo + +0.6..1 st + +1.5 dB (rubberband, formant-preserving);
  4. N TAKES per phrase (temperature/top-k grid, seeded) → pick by objective score:
     STT similarity (faster-whisper, asr venv) ≥0.8 gate, then 0.55·STT + 0.3·F0 range + 0.15·(1-artifact);
  5. line mastering: HPF 70 Hz, de-ess, gentle compression (2.5:1), −16 LUFS, room tone bed.
Engines (job["engine"]): "vieneu-tts" (preset by name, in-process) or "f5-tts" (default since DL-035:
  hynt/F5-TTS-Vietnamese-ViVoice via pipeline/tts/f5tts_gen.py in /workspace/f5-venv, job needs "ref"+"ref_text").
  F5 takes = seed/speed grid; every raw take is auto-trimmed for REFERENCE LEAKAGE (words of the reference
  sentence bleeding in before the target text) using faster-whisper word timestamps, then the same
  STT/F0/artifact pick, gaps, emphasis and mastering apply.
Cached by content hash (phrases+voice+settings); outputs <out>.wav and <out>.json
{duration, envelope, engine, phrases:[{text,start,end,take,score}], metrics}.

Phrase spec per job:  {"voice":"Đức Trí","out":"…/key","phrases":[{"t":"…","gap":0.3,"tempo":1,"semi":0,"gain":0,"emph":false,"tag":""}]}
or {"text": "a / b {300} / *c*"} DSL: "/" splits phrases, {ms} sets the gap after, *…* marks emphasis.
"""
import json, os, re, sys, subprocess, tempfile, hashlib, wave, struct, math, unicodedata
import numpy as np

ASR_PY = os.environ.get("ASR_PYTHON", "/workspace/asr-venv/bin/python")
FPS = 30
SR = 48000
TAKES = [(0.7, 30), (0.85, 40), (1.0, 50)]
F5_TAKES = [(11, 1.0), (23, 0.96), (37, 1.04)]   # (seed, speed)
F5_PY = os.environ.get("F5_PYTHON", "/workspace/f5-venv/bin/python")
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BASE_TEMPO = {"Đức Trí": 1.12, "Kim Thanh": 1.04}   # gentle; pacing comes from gaps, not stretching
PUNCT_GAP = {",": 0.18, ":": 0.26, "…": 0.38, "...": 0.38, ".": 0.32, "?": 0.34, "!": 0.3}
ALIAS = {"toeic": "tô ích", "tô ít": "tô ích", "ok": "ô kê", "okay": "ô kê",
         # L-025: Whisper writes respelled English/brand words back in Latin; same word, not a misread
         "pov": "pi ô vi", "omi": "ô mi", "tiktok": "tíc tóc", "tích tóc": "tíc tóc", "code": "cốt",
         "ôm mì": "ô mi", "âu mì": "ô mi"}  # Whisper heard-forms of the brand Omi (no Vietnamese word); human ear confirms (L-025)
DIGITS = {"0": "không", "1": "một", "2": "hai", "3": "ba", "4": "bốn", "5": "năm", "6": "sáu", "7": "bảy", "8": "tám", "9": "chín", "10": "mười"}

def parse_dsl(text):
    out = []
    for raw in [p.strip() for p in text.split("/") if p.strip()]:
        m = re.search(r"\{(\d+)\}\s*$", raw); gap = None
        if m: gap = int(m.group(1)) / 1000; raw = raw[:m.start()].strip()
        emph = raw.startswith("*") and raw.rstrip(".,!?…:").endswith("*")
        t = raw.replace("*", "")
        if gap is None:
            end = "..." if t.endswith("...") else t[-1]
            gap = PUNCT_GAP.get(end, 0.16)
        out.append({"t": t, "gap": gap, "emph": emph})
    out[-1]["gap"] = 0
    return out

def norm(s):
    s = unicodedata.normalize("NFC", s.lower())
    s = re.sub(r"\b(\w)\.(\w)\.(\w)\b\.?", r"\1\2\3", s)          # P.O.V. → pov (STT acronym form)
    s = re.sub(r"\b(pi|ô)-", r"\1 ", s).replace("ô-mi", "ô mi")         # hyphenated respellings
    s = re.sub(r"\b(\d{1,2})\b", lambda m: DIGITS.get(m.group(1), m.group(1)), s)
    for k, v in ALIAS.items(): s = re.sub(rf"\b{k}\b", v, s)
    return re.sub(r"[^\w\s]", " ", s).split()

def sim(a, b, toneless=False):
    import difflib
    f = (lambda w: "".join(c for c in unicodedata.normalize("NFD", w) if not unicodedata.combining(c)).replace("đ", "d")) if toneless else (lambda w: w)
    return difflib.SequenceMatcher(None, [f(x) for x in norm(a)], [f(x) for x in norm(b)]).ratio()

def read(path):
    with wave.open(path) as w:
        sr, n, ch = w.getframerate(), w.getnframes(), w.getnchannels()
        x = np.frombuffer(w.readframes(n), dtype=np.int16)[::ch].astype(np.float32) / 32768
    return x, sr

def write(path, x, sr=SR):
    y = (np.clip(x, -1, 1) * 32767).astype(np.int16)
    with wave.open(path, "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(y.tobytes())

def ff(inp, out, af):
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", inp, "-af", af, "-ac", "1", "-ar", str(SR), "-c:a", "pcm_s16le", out], check=True)

def f0_stats(x, sr):
    import librosa
    y = librosa.resample(x, orig_sr=sr, target_sr=16000) if sr != 16000 else x
    f0, vflag, _ = librosa.pyin(y, fmin=60, fmax=450, sr=16000, frame_length=1024)
    f = f0[vflag & ~np.isnan(f0)]
    if len(f) < 5: return {"f0_std_st": 0.0, "f0_range_st": 0.0, "f0_med_hz": 0.0}
    st = 12 * np.log2(f / np.median(f))
    return {"f0_std_st": round(float(np.std(st)), 2), "f0_range_st": round(float(np.percentile(st, 95) - np.percentile(st, 5)), 2), "f0_med_hz": round(float(np.median(f)), 1)}

def pauses(x, sr, thr_db=-38, min_s=0.12):
    hop = int(sr * 0.01); fr = np.array([np.sqrt(np.mean(x[i:i + hop] ** 2) + 1e-12) for i in range(0, len(x) - hop, hop)])
    db = 20 * np.log10(fr / (fr.max() + 1e-9) + 1e-9); sil = db < thr_db
    nz = np.where(~sil)[0]
    if len(nz) == 0: return {"pauses": 0, "pause_mean_ms": 0, "pause_total_ms": 0}
    sil = sil[nz[0]:nz[-1] + 1]; runs = []; c = 0
    for s in sil:
        if s: c += 1
        else:
            if c * 0.01 >= min_s: runs.append(c * 10)
            c = 0
    return {"pauses": len(runs), "pause_mean_ms": int(np.mean(runs)) if runs else 0, "pause_total_ms": int(sum(runs))}

def metrics(path):
    x, sr = read(path)
    return {"dur": round(len(x) / sr, 2), **f0_stats(x, sr), **pauses(x, sr)}

def artifact(x, sr, text):
    clip = float(np.mean(np.abs(x) > 0.985))
    p = pauses(x, sr, min_s=0.5)["pauses"]
    syl = max(1, len(norm(text))); spd = (len(x) / sr) / syl
    bad = (clip > 0.001) + (p > 0) + (spd < 0.11 or spd > 0.42)
    return min(1.0, bad / 2)

def stt(paths):
    code = ("import sys,json,subprocess,numpy as np\nfrom faster_whisper import WhisperModel\nm=WhisperModel('small',device='cpu',compute_type='int8')\nr={}\n"
            "for f in sys.argv[1:]:\n pcm=subprocess.run(['ffmpeg','-loglevel','error','-i',f,'-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout\n"
            " a=np.frombuffer(pcm,dtype=np.int16).astype('float32')/32768\n s,_=m.transcribe(a,language='vi',beam_size=5,temperature=0,condition_on_previous_text=False)\n r[f]=' '.join(x.text.strip() for x in s)\nprint(json.dumps(r,ensure_ascii=False))")
    out = subprocess.run([ASR_PY, "-c", code, *paths], capture_output=True, text=True, check=True).stdout
    return json.loads(out.strip().splitlines()[-1])

def stt_words(paths):
    code = ("import sys,json,subprocess,numpy as np\nfrom faster_whisper import WhisperModel\nm=WhisperModel('small',device='cpu',compute_type='int8')\nr={}\n"
            "for f in sys.argv[1:]:\n pcm=subprocess.run(['ffmpeg','-loglevel','error','-i',f,'-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout\n"
            " a=np.frombuffer(pcm,dtype=np.int16).astype('float32')/32768\n s,_=m.transcribe(a,language='vi',beam_size=5,temperature=0,condition_on_previous_text=False,word_timestamps=True)\n"
            " r[f]=[[w.word.strip(),w.start,w.end] for x in s for w in (x.words or [])]\nprint(json.dumps(r,ensure_ascii=False))")
    out = subprocess.run([ASR_PY, "-c", code, *paths], capture_output=True, text=True, check=True).stdout
    return json.loads(out.strip().splitlines()[-1])

def tl(w):
    return "".join(c for c in unicodedata.normalize("NFD", w) if not unicodedata.combining(c)).replace("đ", "d")

def leak_cut(words, target, ref_text):
    """Seconds to cut from the start of an F5 take: leading words that belong to the reference sentence
    and not to the target start. Returns 0 when the take starts cleanly."""
    tg = [tl(x) for x in norm(target)]; rf = {tl(x) for x in norm(ref_text)}
    ws = [(tl(" ".join(norm(w))), a) for w, a, _ in words if norm(w)]
    if not ws or not tg or ws[0][0] == tg[0]: return 0.0
    for i, (w, a) in enumerate(ws[:6]):
        if w == tg[0] or (len(tg) > 1 and w == tg[1] and i > 0):
            lead = [x for x, _ in ws[:i]]
            if lead and all(x in rf for x in lead): return max(0.0, a - 0.04)
            return 0.0
    return 0.0

def room_tone(n, seed=7, db=-62):
    rng = np.random.default_rng(seed); w = rng.standard_normal(n).astype(np.float32)
    b = np.cumsum(w); b -= np.convolve(b, np.ones(2400) / 2400, mode="same")  # brown-ish, DC removed
    b /= (np.std(b) + 1e-9); return b * (10 ** (db / 20))

def envelope(x, sr):
    hop = sr / FPS; env = [float(np.sqrt(np.mean(x[int(i * hop):int((i + 1) * hop)] ** 2))) for i in range(int(len(x) / hop) + 1)]
    env = [e for e in env]; peak = sorted(env)[int(len(env) * 0.95)] if env else 1
    return [round(min(1.0, e / max(peak, 1e-4)), 3) for e in env]

def assemble(j, rank, pick):
    segs = [np.zeros(int(0.06 * SR), np.float32)]; meta = []; t = 0.06
    for pi, ph in enumerate(j["phrases"]):
        best = rank[pi][pick[pi]]; x, _ = read(best["path"]); x = x.copy()
        fade = int(0.012 * SR); x[:fade] *= np.linspace(0, 1, fade); x[-fade:] *= np.linspace(1, 0, fade)
        segs.append(x); meta.append({"text": ph["t"], "start": round(t, 3), "end": round(t + len(x) / SR, 3), "emph": ph.get("emph", False), "take": best["take"], "sim": best["sim"], "score": best["score"],
                                     "alts": [{k: r[k] for k in ("take", "sim", "score", "f0_range_st")} for r in rank[pi]]})
        t += len(x) / SR + ph.get("gap", 0); segs.append(np.zeros(int(ph.get("gap", 0) * SR), np.float32))
    segs.append(np.zeros(int(0.08 * SR), np.float32)); y = np.concatenate(segs)
    return y + room_tone(len(y)), meta

def job_key(j):
    eng = j.get("engine", "vieneu-tts")
    return hashlib.sha1(json.dumps([j["voice"], j["phrases"], TAKES, BASE_TEMPO.get(j["voice"]), "vp1"] + ([eng, j.get("ref"), F5_TAKES] if eng == "f5-tts" else []), ensure_ascii=False).encode()).hexdigest()[:12]

def align_bounds(words, phrases):
    """Map phrase boundaries onto STT word timestamps (difflib on toneless syllables, proportional inside
    non-equal blocks). Returns [t_cut_1, …] (len = phrases-1) or None if not monotonic/plausible."""
    import difflib
    tg = []; cuts = []
    for ph in phrases:
        tg += [tl(x) for x in norm(re.sub(r"\[[^\]]*\]", "", ph["t"]))]; cuts.append(len(tg))
    ws = [(tl(" ".join(norm(w))), a, e) for w, a, e in words if norm(w)]
    if len(ws) < max(2, len(tg) // 2): return None
    m = {}
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, tg, [w for w, _, _ in ws], autojunk=False).get_opcodes():
        for i in range(i1, i2): m[i] = min(j2 - 1, j1 + int((i - i1) * max(1, j2 - j1) / max(1, i2 - i1))) if j2 > j1 else j1
    out = []; prev = 0
    for c in cuts[:-1]:
        k = m.get(c, len(ws)); k = max(k, prev + 1)
        if k >= len(ws): return None
        out.append((ws[k - 1][2] + ws[k][1]) / 2); prev = k
    return out if all(b2 > b1 + 0.15 for b1, b2 in zip([0] + out, out)) else None

def f5_raw(j, d):
    """F5 line mode (DL-035): F5 is unstable on tiny inputs (short phrases → hallucinated/empty takes), so each
    TAKE synthesizes the WHOLE line once (seed/speed grid), reference leakage is trimmed, and the take is cut into
    the spec's phrases at word-timestamp boundaries. Gaps/emphasis/tempo/pitch are then applied per phrase exactly
    like the VieNeu path. Takes whose phrases can't be aligned are dropped. Returns {(pi,ti): path}."""
    txt = re.sub(r"\s+", " ", " ".join(re.sub(r"\[[^\]]*\]\s*", "", ph["t"]) for ph in j["phrases"])).strip()
    items = [{"t": txt, "seed": seed, "speed": spd, "out": os.path.join(d, f"t{ti}-f5.wav"), "_t": ti} for ti, (seed, spd) in enumerate(F5_TAKES)]
    ref = j["ref"] if os.path.isabs(j["ref"]) else os.path.join(REPO, j["ref"])
    bf = os.path.join(d, "f5-batch.json"); json.dump({"ref": ref, "ref_text": j["ref_text"], "items": [{k: v for k, v in it.items() if k != "_t"} for it in items]}, open(bf, "w"), ensure_ascii=False)
    subprocess.run([F5_PY, os.path.join(REPO, "pipeline/tts/f5tts_gen.py"), bf], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    wd = stt_words([it["out"] for it in items]); res = {}; j.setdefault("_leak", {}); j.setdefault("_take_stt", {})
    for it in items:
        ti = it["_t"]; ws = wd[it["out"]]; cut = leak_cut(ws, txt, j["ref_text"])
        if cut > 0: j["_leak"][f"t{ti}"] = round(cut, 2)
        ws = [[w, a - cut, e - cut] for w, a, e in ws if a >= cut - 0.02]
        j["_take_stt"][f"t{ti}"] = " ".join(w for w, _, _ in ws)
        x, sr = read(it["out"]); x = x[int(cut * sr):]; dur = len(x) / sr
        b = [0.0] + (align_bounds(ws, j["phrases"]) or []) + [dur] if len(j["phrases"]) > 1 else [0.0, dur]
        if len(b) != len(j["phrases"]) + 1: continue
        for pi in range(len(j["phrases"])):
            p = os.path.join(d, f"p{pi}t{ti}-raw.wav"); write(p, x[int(b[pi] * sr):int(b[pi + 1] * sr)], sr); res[(pi, ti)] = p
    return res

def _rms_db(x, sr, hop_s=0.005, win_s=0.02):
    hop, win = int(sr * hop_s), int(sr * win_s); pk = np.abs(x).max() + 1e-9
    n = max(1, (len(x) - win) // hop)
    return np.array([20 * np.log10(np.sqrt(np.mean(x[i * hop:i * hop + win] ** 2)) / pk + 1e-9) for i in range(n)]), hop

def _zc(x, i, r=240):
    lo, hi = max(1, i - r), min(len(x) - 1, i + r)
    z = np.where(np.signbit(x[lo - 1:hi - 1]) != np.signbit(x[lo:hi]))[0]
    return lo + int(z[np.argmin(np.abs(z + lo - i))]) if len(z) else i

def _rep_penalty(hyp, ref):
    h, r = [tl(w) for w in norm(hyp)], [tl(w) for w in norm(ref)]
    extra = max(0, len(h) - len(r)) / max(1, len(r))
    rb = set(zip(r, r[1:]))
    dup = sum(1 for k in range(1, len(h)) if h[k] == h[k - 1] and (h[k], h[k]) not in rb)
    return extra + 0.25 * dup

def f5_line(j, d, sil_db=-32.0, search=0.25, fade=0.012):
    """F5 v3 (DL-036, fixes 'vấp'): ONE natural take per line, never a cross-take collage. Whole-line takes
    (seed/speed grid, NFE 32) → STT (word timestamps) → leakage trim → score = toneless STT + STT − repeat/drop
    penalty → best take. Phrase boundaries are only CUT where the take is really silent (energy minimum
    < sil_db re peak within ±search s of the word-timestamp boundary); the silence is replaced by the spec gap,
    cut points snapped to zero crossings with 12 ms fades. Boundaries without a real pause stay continuous
    (F5's own phrasing). No silenceremove, no rubberband on F5 audio (they caused smeared onsets/glitches);
    emphasis = +1.5 dB gain ramp only. Returns (wav, meta, stt, sim, sim_toneless)."""
    txt = re.sub(r"\s+", " ", " ".join(re.sub(r"\[[^\]]*\]\s*", "", ph["t"]) for ph in j["phrases"])).strip()
    items = [{"t": txt, "seed": seed, "speed": spd, "out": os.path.join(d, f"t{ti}-f5.wav")} for ti, (seed, spd) in enumerate(F5_TAKES)]
    ref = j["ref"] if os.path.isabs(j["ref"]) else os.path.join(REPO, j["ref"])
    bf = os.path.join(d, "f5-batch.json"); json.dump({"ref": ref, "ref_text": j["ref_text"], "items": items}, open(bf, "w"), ensure_ascii=False)
    subprocess.run([F5_PY, os.path.join(REPO, "pipeline/tts/f5tts_gen.py"), bf], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    wd = stt_words([it["out"] for it in items]); takes = []
    for ti, it in enumerate(items):
        ws = wd[it["out"]]; cut = leak_cut(ws, txt, j["ref_text"])
        ws = [[w, a - cut, e - cut] for w, a, e in ws if a >= cut - 0.02]; hyp = " ".join(w for w, _, _ in ws)
        sc = sim(hyp, txt, toneless=True) + 0.5 * sim(hyp, txt) - 2 * _rep_penalty(hyp, txt)
        takes.append({"take": ti, "path": it["out"], "cut": round(cut, 3), "words": ws, "stt": hyp, "score": round(sc, 3)})
    takes.sort(key=lambda t: -t["score"]); best = takes[0]
    x, sr = read(best["path"]); x = x[int(best["cut"] * sr):].copy()
    if sr != SR:
        import librosa; x = librosa.resample(x, orig_sr=sr, target_sr=SR).astype(np.float32); sr = SR
    db, hop = _rms_db(x, sr); voiced = np.where(db > -40)[0]
    s0 = max(0, voiced[0] * hop - int(0.03 * sr)); s1 = min(len(x), voiced[-1] * hop + int(0.02 * sr * 2) + int(0.03 * sr))
    bounds = align_bounds(best["words"], j["phrases"]) if len(j["phrases"]) > 1 else []
    if bounds is None: bounds = []
    cuts = []; info = []
    for bt in bounds:
        c = int(bt * sr / hop); lo, hi = max(0, c - int(search * sr / hop)), min(len(db) - 1, c + int(search * sr / hop))
        if hi <= lo: cuts.append(None); continue
        k = lo + int(np.argmin(db[lo:hi]))
        if db[k] > sil_db: cuts.append(None); info.append(round(float(db[k]), 1)); continue
        a, b = k, k
        while a > 0 and db[a - 1] < sil_db: a -= 1
        while b < len(db) - 1 and db[b + 1] < sil_db: b += 1
        cuts.append((_zc(x, a * hop + int(0.01 * sr)), _zc(x, b * hop + int(0.01 * sr)))); info.append(round(float(db[k]), 1))
    # assemble: segments between real-silence cuts; phrases without a cut are merged with the next one
    segs = [np.zeros(int(0.06 * SR), np.float32)]; meta = []; t = 0.06; start = s0; group = []
    fd = int(fade * sr)
    def emit(end, gap):
        nonlocal t, start
        y = x[start:end].copy()
        if len(y) > 2 * fd: y[:fd] *= np.linspace(0, 1, fd); y[-fd:] *= np.linspace(1, 0, fd)
        if any(j["phrases"][q].get("emph") for q in group):
            g = 10 ** ((1.5 + max(j["phrases"][q].get("gain", 0) for q in group)) / 20); r = np.ones(len(y), np.float32) * g
            ramp = min(int(0.03 * sr), len(y) // 2); r[:ramp] = np.linspace(1, g, ramp); r[-ramp:] = np.linspace(g, 1, ramp); y *= r
        segs.append(y); meta.append({"text": " ".join(j["phrases"][q]["t"] for q in group), "phrases": list(group), "start": round(t, 3), "end": round(t + len(y) / SR, 3),
                                     "emph": any(j["phrases"][q].get("emph") for q in group), "take": best["take"], "sim": 1.0})
        t += len(y) / SR + gap; segs.append(np.zeros(int(gap * SR), np.float32))
    for pi in range(len(j["phrases"])):
        group.append(pi)
        c = cuts[pi] if pi < len(cuts) else None
        if pi == len(j["phrases"]) - 1: emit(s1, 0)
        elif c is not None:
            nat = (c[1] - c[0]) / sr; gap = max(0.12, j["phrases"][pi].get("gap", 0.2), min(nat, 0.5))
            emit(c[0], gap); start = c[1]; group = []
    if j.get("emph_tail"):  # L-028: harsh emphasis on the key word at the end of a self-blame line: +dB ramp + soft saturation
        n = int(float(j["emph_tail"]) * SR); last = segs[-1] if len(segs[-1]) else segs[-2]
        k = min(n, len(last)); g = 10 ** (float(j.get("emph_db", 3.5)) / 20); ramp = np.linspace(1, g, min(k, int(0.06 * SR)))
        env = np.concatenate([ramp, np.full(k - len(ramp), g)]).astype(np.float32); seg = last[-k:] * env
        last[-k:] = (np.tanh(seg * 1.6) / np.tanh(1.6)).astype(np.float32) * 0.7 + seg * 0.3
    segs.append(np.zeros(int(0.08 * SR), np.float32)); y = np.concatenate(segs); y = y + room_tone(len(y))
    out = []  # one meta entry per spec phrase (captions zip phrases 1:1); merged groups split by syllable share
    for g in meta:
        n = [max(1, len(norm(j["phrases"][q]["t"]))) for q in g["phrases"]]; acc = g["start"]; span = g["end"] - g["start"]
        for q, k in zip(g["phrases"], n):
            e = acc + span * k / sum(n); out.append({**g, "text": j["phrases"][q]["t"], "start": round(acc, 3), "end": round(e, 3), "merged": len(n) > 1}); acc = e
    meta = out
    tmp = os.path.join(d, "line.wav"); write(tmp, y)
    lt = stt([tmp])[tmp]
    j["_take_stt"] = {f"t{t_['take']}": f"{t_['stt']} (score {t_['score']})" for t_ in takes}; j["_leak"] = {f"t{t_['take']}": t_["cut"] for t_ in takes if t_["cut"]}
    j["_cuts"] = {"boundary_db": info, "cut": [c is not None for c in cuts]}
    return tmp, meta, lt, sim(lt, txt), sim(lt, txt, toneless=True)

sys.path.insert(0, os.path.join(REPO, "pipeline/tts"))
import markup as MK   # DL-039: fillers / particles / punctuation markup
F5_UNIT_SEEDS = [11, 23, 37]
F5_EXTRA_SEEDS = [53, 71, 89, 101, 131, 157, 199]   # same seed grid + speed 1.0 for every unit of a character → consistent timbre
SPLIT = r"[.,?!…;:—)”\"]"

def split_units(txt, min_syl=4):
    """Split at punctuation (. , ? ! … ; : — ( ) “ ”) into clause units keeping the mark; "(" and "“" start a unit.
    Units < min_syl syllables merge into the next (last into previous). Returns [(text, char_start, char_end)]."""
    u = []
    for piece in re.finditer(r"[(“\"]?[^(“]*", txt):
        base = piece.start()
        for m in re.finditer(r"[(“\"]?[^.,?!…;:—)”\"(“]+(?:\.\.\.|[.,?!…;:—)”\"]+)?", piece.group(0)):
            if m.group(0).strip() and norm(m.group(0)): u.append((m.group(0).strip(), base + m.start(), base + m.end()))
    out = []
    for t, a, b in u:
        if out and len(norm(out[-1][0])) < min_syl: pt, pa, _ = out.pop(); out.append((pt + " " + t, pa, b))
        else: out.append((t, a, b))
    if len(out) > 1 and len(norm(out[-1][0])) < min_syl: t, _, b = out.pop(); pt, pa, _ = out.pop(); out.append((pt + " " + t, pa, b))
    return out

def end_mark(t):
    t = t.rstrip()
    if t.endswith("..."): return "..."
    return t[-1] if t and t[-1] in MK.PAUSE else ""

def f5_text(unit, character):
    t = MK.auto_particles(unit, character).replace(MK.HES, "...")
    return re.sub(r"\s+", " ", re.sub(r"[()“”\"]", " ", t)).strip()

def _trim_unit(x, sr, thr_db=-50.0, pad=0.04, fade=0.015):
    """Gentle edge trim only (never inside): first/last 10 ms frame above thr_db dBFS, keep 40 ms pads, 15 ms fades."""
    hop = int(sr * 0.01); fr = np.array([np.sqrt(np.mean(x[i:i + hop] ** 2) + 1e-12) for i in range(0, max(1, len(x) - hop), hop)])
    on = np.where(20 * np.log10(fr + 1e-12) > thr_db)[0]
    if len(on) == 0: return x, 0.0, 0.0
    a = max(0, on[0] * hop - int(pad * sr)); b = min(len(x), (on[-1] + 1) * hop + int(pad * sr)); y = x[a:b].copy()
    f = int(fade * sr)
    if len(y) > 2 * f: y[:f] *= np.linspace(0, 1, f); y[-f:] *= np.linspace(1, 0, f)
    return y, a / sr, (len(x) - b) / sr

def bank_clip(character, filler, key):
    d = os.path.join(REPO, "pipeline/tts/filler-bank", character or "x"); fs = sorted(f for f in os.listdir(d) if f.startswith(filler + "-")) if os.path.isdir(d) else []
    if not fs: raise SystemExit(f"filler bank missing for {character}/{filler} (run voice-prosody.py --bank)")
    f = fs[MK.bank_pick(character, filler, key, len(fs))]; x, sr = read(os.path.join(d, f))
    if sr != SR:
        import librosa; x = librosa.resample(x, orig_sr=sr, target_sr=SR).astype(np.float32)
    return x, f

def f5_units(j, d):
    """F5 v5 (DL-038 + DL-039): NO cutting inside any F5 output. Markup expanded (fillers merged into the next unit,
    {bank:…} clips inserted between units, {ngập ngừng} → in-unit "...", {kéo: p} / sentence-final particle → best
    spelling per character), then split at punctuation into clause units (merge < 4 syllables); each unit is its own
    F5 call × 3 fixed seeds; pick = STT − repeat/drop + F0/seed consistency; edge-only trim; pauses per mark with
    room tone; asides "( … )" −4 dB. Returns (wav, meta, stt, sim, sim_toneless)."""
    ch = j.get("speaker")
    raw = re.sub(r"\s+", " ", " ".join(re.sub(r"\[[^\]]*\]\s*", "", ph["t"]) for ph in j["phrases"])).strip()
    exp, bank = MK.expand(raw, ch)
    plan = []   # ("unit", text) | ("bank", filler)
    for k, seg in enumerate(re.split(r"§(\d+)§", exp)):
        if k % 2: plan.append(("bank", bank[int(seg)]))
        elif seg.strip(): plan += [("unit", seg.strip())] if j.get("whole") else [("unit", u[0]) for u in split_units(seg.strip())]  # L-027: whole line = one F5 pass
    units = [t for kind, t in plan if kind == "unit"]
    ref = j["ref"] if os.path.isabs(j["ref"]) else os.path.join(REPO, j["ref"])
    seeds = (F5_UNIT_SEEDS + F5_EXTRA_SEEDS)[:max(3, int(j.get("takes") or 3))]  # L-025: up to 6 takes for hard (respelled) lines
    items = [{"t": f5_text(u, ch), "seed": sd, "speed": float(j.get("speed") or 1.0), "out": os.path.join(d, f"u{ui}s{si}.wav")} for ui, u in enumerate(units) for si, sd in enumerate(seeds)]
    if j.get("alts") and len(units) == 1:  # L-025: alternate spellings of one whole line, takes spread over them
        tk = int(j.get("takes") or 3); al = [units[0]] + list(j["alts"]); grid = [(a, (F5_UNIT_SEEDS + F5_EXTRA_SEEDS)[k // len(al)]) for k, a in zip(range(tk), (al * tk))]
        seeds = [g[1] for g in grid]
        items = [{"t": f5_text(a, ch), "seed": sd, "speed": float(j.get("speed") or 1.0), "out": os.path.join(d, f"u0s{si}.wav")} for si, (a, sd) in enumerate(grid)]
    bf = os.path.join(d, "f5-batch.json"); json.dump({"ref": ref, "ref_text": j["ref_text"], "items": items}, open(bf, "w"), ensure_ascii=False)
    subprocess.run([F5_PY, os.path.join(REPO, "pipeline/tts/f5tts_gen.py"), bf], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    tx = stt([it["out"] for it in items]); cand = {}
    for it in items:
        ui, si = map(int, re.search(r"u(\d+)s(\d+)\.wav", it["out"]).groups())
        x, sr = read(it["out"])
        if sr != SR:
            import librosa; x = librosa.resample(x, orig_sr=sr, target_sr=SR).astype(np.float32); sr = SR
        y, lead, tail = _trim_unit(x, sr); h = tx[it["out"]]; t = it["t"]
        hn, rn = len(norm(h)), max(1, len(norm(t))); drop = max(0, rn - hn) / rn
        sc = sim(h, t, toneless=True) + 0.5 * sim(h, t) - 2 * _rep_penalty(h, t) - 2 * max(0, drop - 0.1)
        cand.setdefault(ui, []).append({"t": t, "seed": seeds[si], "y": y, "stt": h, "score": round(sc, 3), "sim": round(sim(h, t), 3), "drop": round(drop, 3), "f0": f0_stats(y, sr)["f0_med_hz"], "trim": [round(lead, 3), round(tail, 3)]})
    if j.get("energetic"):  # hook: among takes passing STT (sim ≥ 0.8 toneless-aware score), prefer the most energetic (F0 range + loudness)
        for c in cand.values():
            for r in c: r["energy"] = float(np.sqrt(np.mean(r["y"] ** 2))); r["f0r"] = f0_stats(r["y"], SR).get("f0_range_st", 0) or 0
    pick = {ui: max(c, key=lambda r: r["score"]) for ui, c in cand.items()}
    if j.get("energetic"):
        for ui, c in cand.items():
            ok_ = [r for r in c if r["sim"] >= 0.8 and r["drop"] <= 0.05] or [pick[ui]]  # L-025: STT 0.8 is a hard minimum; energy only among passing takes
            pick[ui] = max(ok_, key=lambda r: r["f0r"] + 40 * r["energy"])
    if len(units) > 1:
        med = float(np.median([p["f0"] for p in pick.values() if p["f0"]] or [0])); dom = max(set(p["seed"] for p in pick.values()), key=lambda s: sum(p["seed"] == s for p in pick.values()))
        for ui, c in cand.items():
            def tscore(r): return r["score"] - (0.08 * abs(12 * np.log2(r["f0"] / med)) if r["f0"] and med else 0) + (0.05 if r["seed"] == dom else 0)
            ok_ = [r for r in c if r["score"] >= pick[ui]["score"] - 0.15]; pick[ui] = max(ok_, key=tscore)
    segs = [np.zeros(int(0.06 * SR), np.float32)]; t = 0.06; um = []; ui = 0
    for k, (kind, val) in enumerate(plan):
        last = k == len(plan) - 1
        if kind == "bank":
            y, f = bank_clip(ch, val, raw); gap = 0 if last else 0.14
            segs += [y, np.zeros(int(gap * SR), np.float32)]
            um.append({"kind": "bank", "text": val, "file": f, "start": round(t, 3), "end": round(t + len(y) / SR, 3), "gap_after": gap}); t += len(y) / SR + gap; continue
        y = pick[ui]["y"].copy(); aside = val.lstrip().startswith("(")
        if aside: y *= 10 ** (MK.ASIDE_DB / 20)
        nxt = plan[k + 1][1] if not last and plan[k + 1][0] == "unit" else ""
        gap = 0 if last else max(MK.PAUSE.get(end_mark(val), 0.16), 0.2 if nxt.lstrip().startswith("(") else 0)
        if j.get("gap_max") is not None: gap = min(gap, float(j["gap_max"]))  # rule-55 hook: tight clause gaps
        segs += [y, np.zeros(int(gap * SR), np.float32)]
        um.append({"kind": "unit", "text": val, "f5_text": pick[ui].get("t") or f5_text(val, ch), "aside": aside, "start": round(t, 3), "end": round(t + len(y) / SR, 3), "seed": pick[ui]["seed"], "score": pick[ui]["score"],
                   "stt": pick[ui]["stt"], "f0": pick[ui]["f0"], "trim": pick[ui]["trim"], "gap_after": gap, "alts": [{"seed": r["seed"], "score": r["score"], "sim": r["sim"], "stt": r["stt"], "f0": r["f0"]} for r in cand[ui]]})
        t += len(y) / SR + gap; ui += 1
    if j.get("emph_tail"):  # L-028: harsh emphasis on the key word at the end of a self-blame line: +dB ramp + soft saturation
        n = int(float(j["emph_tail"]) * SR); last = segs[-1] if len(segs[-1]) else segs[-2]
        k = min(n, len(last)); g = 10 ** (float(j.get("emph_db", 3.5)) / 20); ramp = np.linspace(1, g, min(k, int(0.06 * SR)))
        env = np.concatenate([ramp, np.full(k - len(ramp), g)]).astype(np.float32); seg = last[-k:] * env
        last[-k:] = (np.tanh(seg * 1.6) / np.tanh(1.6)).astype(np.float32) * 0.7 + seg * 0.3
    segs.append(np.zeros(int(0.08 * SR), np.float32)); y = np.concatenate(segs); y = y + room_tone(len(y))
    # caption chunks: spec phrases spread over spoken units by cumulative syllables (no audio is cut)
    sp = [(u, max(1, len(norm(u["f5_text"])))) for u in um if u["kind"] == "unit"]; tot = sum(n for _, n in sp)
    def at(frac):
        acc = 0
        for u, n in sp:
            if acc + n >= frac * tot - 1e-9: return u["start"] + (u["end"] - u["start"]) * (frac * tot - acc) / n
            acc += n
        return sp[-1][0]["end"]
    vis = [max(1, len(norm(MK.visible(ph["t"])))) for ph in j["phrases"]]; vt = sum(vis); acc = 0; meta = []
    for ph, n in zip(j["phrases"], vis):
        meta.append({"text": MK.visible(ph["t"]), "start": round(at(acc / vt), 3), "end": round(at((acc + n) / vt), 3), "emph": ph.get("emph", False), "take": None, "sim": 1.0, "merged": True}); acc += n
    tmp = os.path.join(d, "line.wav"); write(tmp, y); lt = stt([tmp])[tmp]; ref_sp = pick[0]["t"] if j.get("alts") and len(units) == 1 else MK.spoken(raw, ch)
    j["_units"] = [u for u in um if u["kind"] == "unit"]; j["_bank"] = [u for u in um if u["kind"] == "bank"]; j["_spoken"] = ref_sp; j["_take_stt"] = {}; j["_leak"] = {}; j["_cuts"] = None
    return tmp, meta, lt, sim(lt, ref_sp), sim(lt, ref_sp, toneless=True)

def make_bank(character, ref, ref_text, fillers=None, seeds=(11, 23, 37)):
    """Cached per-character filler bank: each filler alone as its own F5 call × seeds, edge-trimmed, kept if STT
    hears a vowel-ish token and duration is 0.25–1.4 s. Files: pipeline/tts/filler-bank/<char>/<filler>-<seed>.wav"""
    out = os.path.join(REPO, "pipeline/tts/filler-bank", character); os.makedirs(out, exist_ok=True); d = tempfile.mkdtemp(prefix="bank-")
    fl = fillers or ["ừm", "ờ", "à", "hừm", "ủa", "trời ơi"]
    items = [{"t": MK.FILLERS[f], "seed": s, "out": os.path.join(d, f"{f}-{s}.wav")} for f in fl for s in seeds]
    json.dump({"ref": ref, "ref_text": ref_text, "items": items}, open(os.path.join(d, "b.json"), "w"), ensure_ascii=False)
    subprocess.run([F5_PY, os.path.join(REPO, "pipeline/tts/f5tts_gen.py"), os.path.join(d, "b.json")], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    rep = {}
    for it in items:
        x, sr = read(it["out"])
        if sr != SR:
            import librosa; x = librosa.resample(x, orig_sr=sr, target_sr=SR).astype(np.float32)
        y, _, _ = _trim_unit(x, SR); dur = len(y) / SR; keep = 0.25 <= dur <= 1.4
        rep[os.path.basename(it["out"])] = round(dur, 2)
        if keep: write(os.path.join(out, os.path.basename(it["out"])), y / (np.abs(y).max() + 1e-9) * 0.5)
    return rep

def run(jobs):
    tts = None; results = []
    for j in jobs:
        if "phrases" not in j: j["phrases"] = parse_dsl(j["text"])
        if os.path.exists(j["out"] + ".wav") and os.path.exists(j["out"] + ".json"):
            results.append(json.load(open(j["out"] + ".json"))); continue
        f5 = j.get("engine") == "f5-tts"
        if tts is None and not f5:
            from vieneu import Vieneu; tts = Vieneu()
        d = tempfile.mkdtemp(prefix="vp-"); cands = []
        if f5: tmp, meta, line_tx, line_sim, line_sim_tl = f5_units(j, d)  # v4; f5_line (v3) kept for reference only
        else:
            raws = f5_raw(j, d) if f5 else {}
            if f5 and not raws: raise SystemExit(f"{j['out']}: no F5 take could be aligned to its phrases (STT: {j.get('_take_stt')}); rewrite the line or add takes")
            for pi, ph in enumerate(j["phrases"]):
                tempo = ph.get("tempo", 1.0) * BASE_TEMPO.get(j["voice"], 1.0) * (0.9 if ph.get("emph") else 1.0)
                semi = ph.get("semi", 0) + (ph.get("emph_semi", 0.8) if ph.get("emph") else 0); gain = ph.get("gain", 0) + (1.5 if ph.get("emph") else 0)
                for ti, (temp, k) in enumerate(F5_TAKES if f5 else TAKES):
                    if f5:
                        if (pi, ti) not in raws: continue
                        out = os.path.join(d, f"p{pi}t{ti}.wav")
                        af = (f"silenceremove=start_periods=1:start_threshold=-42dB,areverse,silenceremove=start_periods=1:start_threshold=-42dB,areverse,"
                              f"aresample={SR},rubberband=tempo={tempo:.3f}:pitch={2 ** (semi / 12):.4f}:formant=preserved:transients=smooth,volume={gain}dB")
                        ff(raws[(pi, ti)], out, af); cands.append((pi, ti, out)); continue
                    np.random.seed(1000 * pi + ti)
                    try:
                        import torch; torch.manual_seed(1000 * pi + ti)
                    except Exception: pass
                    raw = os.path.join(d, f"p{pi}t{ti}-raw.wav"); out = os.path.join(d, f"p{pi}t{ti}.wav")
                    tts.save(tts.infer(ph.get("tag", "") + ph["t"], voice=j["voice"], temperature=temp, top_k=k), raw)
                    af = (f"silenceremove=start_periods=1:start_threshold=-42dB,areverse,silenceremove=start_periods=1:start_threshold=-42dB,areverse,"
                          f"aresample={SR},rubberband=tempo={tempo:.3f}:pitch={2 ** (semi / 12):.4f}:formant=preserved:transients=smooth,volume={gain}dB")
                    ff(raw, out, af); cands.append((pi, ti, out))
            tx = stt([c[2] for c in cands]); per = {}
            for pi, ti, out in cands:
                x, sr = read(out); ph = j["phrases"][pi]; s = sim(tx[out], ph["t"]); f = f0_stats(x, sr); a = artifact(x, sr, ph["t"])
                short = len(norm(ph["t"])) <= 3   # whisper is unreliable on <1 s fragments: judge those on the whole line instead
                if short: score = 0.6 * min(f["f0_range_st"] / 8, 1) + 0.4 * (1 - a)
                else: score = (0.55 * s + 0.3 * min(f["f0_range_st"] / 8, 1) + 0.15 * (1 - a)) if s >= 0.7 else s * 0.5
                per.setdefault(pi, []).append({"take": ti, "path": out, "stt": tx[out], "sim": round(s, 2), "score": round(score, 3), **f, "artifact": a})
            rank = {pi: sorted(per[pi], key=lambda r: -r["score"]) for pi in per}; pick = {pi: 0 for pi in per}
            best = None
            for attempt in range(6):
                y, meta = assemble(j, rank, pick)
                tmp = os.path.join(d, "line.wav"); write(tmp, y)
                ref = " ".join(re.sub(r"\[[^\]]*\]", "", p["t"]) for p in j["phrases"])
                line_tx = stt([tmp])[tmp]; line_sim = sim(line_tx, ref); line_sim_tl = sim(line_tx, ref, toneless=True)
                if best is None or line_sim_tl + line_sim > best[0]: best = (line_sim_tl + line_sim, dict(pick), line_tx, line_sim, line_sim_tl)
                if line_sim_tl >= 0.92 and line_sim >= 0.8: break   # gate on base syllables; whisper-small mishears tones on TTS
                # re-roll: short phrases first (not STT-judged alone), then the weakest STT phrase; next-best take
                shorts = sorted([pi for pi in per if pick[pi] + 1 < len(rank[pi])], key=lambda pi: (len(norm(j["phrases"][pi]["t"])) > 3, rank[pi][pick[pi]]["sim"]))
                if not shorts: break
                pick[shorts[0]] += 1
            if best and best[1] != pick:  # never ship a re-roll that scored worse than an earlier attempt
                pick = best[1]; line_tx, line_sim, line_sim_tl = best[2], best[3], best[4]
                y, meta = assemble(j, rank, pick); write(tmp, y)
        os.makedirs(os.path.dirname(j["out"]) or ".", exist_ok=True)
        ff(tmp, j["out"] + ".wav", "highpass=f=70,deesser=i=0.35:m=0.5:f=0.5,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=140:makeup=2,loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000")
        z, _ = read(j["out"] + ".wav")
        m = {"duration": round(len(z) / SR, 3), "envelope": envelope(z, SR), "engine": ("F5-TTS hynt/F5-TTS-Vietnamese-ViVoice (CC-BY-NC-SA-4.0) + voice-prosody v5 (v4 units + fillers/particles/punctuation markup, no intra-output cuts)" if f5 else "VieNeu-TTS v3 Turbo (local ONNX) + voice-prosody v1"), "voice": j["voice"], "leak_trims": j.get("_leak", {}), "take_stt": j.get("_take_stt", {}), "cuts": j.get("_cuts"), "units": [{k: v for k, v in u.items()} for u in j.get("_units", [])], "intra_output_cuts": 0 if j.get("_units") else None, "bank": j.get("_bank", []), "spoken": j.get("_spoken"),
             "phrases": meta, "stt": line_tx, "stt_sim": round(line_sim, 3), "stt_sim_toneless": round(line_sim_tl, 3), "metrics": metrics(j["out"] + ".wav")}
        json.dump(m, open(j["out"] + ".json", "w"), ensure_ascii=False); results.append(m)
        print(f"{os.path.basename(j['out'])}: {m['duration']}s takes={[p['take'] for p in meta]} sims={[p['sim'] for p in meta]} cuts={j.get('_cuts')} stt={line_tx}", file=sys.stderr)
    return results

if __name__ == "__main__":
    if sys.argv[1] == "--metrics":
        print(json.dumps({p: metrics(p) for p in sys.argv[2:]}, ensure_ascii=False, indent=1))
    elif sys.argv[1] == "--bank":   # --bank <character> <ref.wav> "<ref text>"
        print(json.dumps(make_bank(sys.argv[2], sys.argv[3], sys.argv[4]), ensure_ascii=False))
    elif sys.argv[1] == "--stt":
        print(json.dumps(stt(sys.argv[2:]), ensure_ascii=False, indent=1))
    else:
        spec = json.load(open(sys.argv[1])); r = run(spec["jobs"])
        print(json.dumps([{"out": j["out"], "duration": x["duration"]} for j, x in zip(spec["jobs"], r)], ensure_ascii=False))
