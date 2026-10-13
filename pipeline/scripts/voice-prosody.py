#!/usr/bin/env python3
"""Human-sounding line synthesis for VieNeu-TTS presets (DL-033). Run with the TTS venv:
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
BASE_TEMPO = {"Đức Trí": 1.12, "Kim Thanh": 1.04}   # gentle; pacing comes from gaps, not stretching
PUNCT_GAP = {",": 0.18, ":": 0.26, "…": 0.38, "...": 0.38, ".": 0.32, "?": 0.34, "!": 0.3}
ALIAS = {"toeic": "tô ích", "tô ít": "tô ích", "ok": "ô kê", "okay": "ô kê"}

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
    return hashlib.sha1(json.dumps([j["voice"], j["phrases"], TAKES, BASE_TEMPO.get(j["voice"]), "vp1"], ensure_ascii=False).encode()).hexdigest()[:12]

def run(jobs):
    tts = None; results = []
    for j in jobs:
        if "phrases" not in j: j["phrases"] = parse_dsl(j["text"])
        if os.path.exists(j["out"] + ".wav") and os.path.exists(j["out"] + ".json"):
            results.append(json.load(open(j["out"] + ".json"))); continue
        if tts is None:
            from vieneu import Vieneu; tts = Vieneu()
        d = tempfile.mkdtemp(prefix="vp-"); cands = []
        for pi, ph in enumerate(j["phrases"]):
            tempo = ph.get("tempo", 1.0) * BASE_TEMPO.get(j["voice"], 1.0) * (0.9 if ph.get("emph") else 1.0)
            semi = ph.get("semi", 0) + (ph.get("emph_semi", 0.8) if ph.get("emph") else 0); gain = ph.get("gain", 0) + (1.5 if ph.get("emph") else 0)
            for ti, (temp, k) in enumerate(TAKES):
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
        for attempt in range(6):
            y, meta = assemble(j, rank, pick)
            tmp = os.path.join(d, "line.wav"); write(tmp, y)
            ref = " ".join(re.sub(r"\[[^\]]*\]", "", p["t"]) for p in j["phrases"])
            line_tx = stt([tmp])[tmp]; line_sim = sim(line_tx, ref); line_sim_tl = sim(line_tx, ref, toneless=True)
            if line_sim_tl >= 0.92 and line_sim >= 0.8: break   # gate on base syllables; whisper-small mishears tones on TTS
            # re-roll: short phrases first (not STT-judged alone), then the weakest STT phrase; next-best take
            shorts = sorted([pi for pi in per if pick[pi] + 1 < len(rank[pi])], key=lambda pi: (len(norm(j["phrases"][pi]["t"])) > 3, rank[pi][pick[pi]]["sim"]))
            if not shorts: break
            pick[shorts[0]] += 1
        os.makedirs(os.path.dirname(j["out"]) or ".", exist_ok=True)
        ff(tmp, j["out"] + ".wav", "highpass=f=70,deesser=i=0.35:m=0.5:f=0.5,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=140:makeup=2,loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000")
        z, _ = read(j["out"] + ".wav")
        m = {"duration": round(len(z) / SR, 3), "envelope": envelope(z, SR), "engine": "VieNeu-TTS v3 Turbo (local ONNX) + voice-prosody v1", "voice": j["voice"],
             "phrases": meta, "stt": line_tx, "stt_sim": round(line_sim, 3), "stt_sim_toneless": round(line_sim_tl, 3), "metrics": metrics(j["out"] + ".wav")}
        json.dump(m, open(j["out"] + ".json", "w"), ensure_ascii=False); results.append(m)
        print(f"{os.path.basename(j['out'])}: {m['duration']}s takes={[p['take'] for p in meta]} sims={[p['sim'] for p in meta]}", file=sys.stderr)
    return results

if __name__ == "__main__":
    if sys.argv[1] == "--metrics":
        print(json.dumps({p: metrics(p) for p in sys.argv[2:]}, ensure_ascii=False, indent=1))
    elif sys.argv[1] == "--stt":
        print(json.dumps(stt(sys.argv[2:]), ensure_ascii=False, indent=1))
    else:
        spec = json.load(open(sys.argv[1])); r = run(spec["jobs"])
        print(json.dumps([{"out": j["out"], "duration": x["duration"]} for j, x in zip(spec["jobs"], r)], ensure_ascii=False))
