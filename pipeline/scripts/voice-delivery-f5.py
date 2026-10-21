#!/usr/bin/env python3
"""Voice-only straight from a delivery plan (script-vNN-delivery.md), no spec needed (clip-04 v16b preview, W-08 / L-070).
  python3 pipeline/scripts/voice-delivery-f5.py parse   <final dir> --script script-v16b.md --delivery script-v16b-delivery.md --work DIR
  python3 pipeline/scripts/voice-delivery-f5.py batch   ... --seeds 11,37,53 [--only s03,s07]      # F5 batch json (whole sentences)
  /workspace/asr-venv/bin/python ... pick    ...            # STT + rate pick, gain stress, question rise, split at every delivery mark
  /workspace/asr-venv/bin/python ... voice   ... --plan A|B --prefix c04v16b --m4a OUT
  /workspace/asr-venv/bin/python ... measure ... --prefix c04v16b --out final/prosody-measure-v16b.md
Root rules (pacing-v14.md, L-070): F5 gets WHOLE sentences (never a lone word; English words respelled inside their sentence); every delivery mark
('/', '//', '//|', '///') becomes a cut at the real low-energy point between the two words, then the exact plan pause is laid in; stress = gain
on the **bold** chunk (≥2 dB over the rest of the sentence and over its neighbours), no tempo change, no word split; '↗' questions get the last
syllable raised and proven by F0; takes picked by STT match minus a penalty above 5 syllables/s.
"""
import json, os, re, sys, subprocess, difflib, unicodedata, glob
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
PLANS = {"A": {"/": 0.18, "//breath": 0.28, "//": 0.35, "//beat": 0.4, "///": 0.4, "//hook": 0.08}, "B": {"/": 0.15, "//breath": 0.25, "//": 0.3, "//beat": 0.4, "///": 0.4, "//hook": 0.08}}  # //hook: L-027 splice ≤0.1s inside the hook (v18 R8)  # plan C forbidden (W-08)
RESP = {"airport": "e pọt", "hotel": "hô ten", "ticket": "tích kịt", "passport": "pát pọt", "luggage": "lắc ghịt", "dunlosky": "Đun lốt ki",
        "yang": "Giang", "comment": "Com men", "317": "ba trăm mười bảy", "222": "hai trăm hai mươi hai", "48": "bốn mươi tám", "2006": "hai ngàn lẻ sáu"}
REF = os.path.join(REPO, "assets/voice-refs/thai-son.wav")
REF_TEXT = "Hôm nay trời Sài Gòn mát mẻ, mình ngồi cà phê một chút rồi về nhà làm việc tiếp nha."
def arg(k, d=None): return sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
def fold(s): return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn").replace("đ", "d")
WRE = r"[\wÀ-ỹ]+"
def final_tone(text):
    """tone of the last syllable: huyen | nang | sac | hoi | nga | ngang (L-082)"""
    ws_ = re.findall(WRE, text or "")
    if not ws_: return "ngang"
    d = unicodedata.normalize("NFD", ws_[-1].lower())
    return "huyen" if "\u0300" in d else "nang" if "\u0323" in d else "sac" if "\u0301" in d else "hoi" if "\u0309" in d else "nga" if "\u0303" in d else "ngang"
L082 = ("huyen", "nang")  # L-082: question ending on huyền/nặng → no artificial pitch lift, rise check exempt
def resp_word(w): return RESP.get(w.lower(), w)
def syl(w): return len(re.findall(WRE, resp_word(w)))

def parse(fd):
    """sentences from the delivery rows (marks, bold, ↗) + punctuation from the script's sentence table; words must match 1:1."""
    dl = open(os.path.join(fd, arg("--delivery"))).read().splitlines(); stream = []
    for row in dl:
        if not re.match(r"\| b\d\d \|", row): continue
        beat = row.split("|")[1].strip(); cell = [x.strip() for x in row.replace("\\|", "¦").strip("|").split("|")][1]
        if "//" not in cell: continue  # other tables (budget) also start with «| b01 |»
        bold = False
        for tok in re.findall(r"\*\*|/{1,3}¦?|↗|" + WRE, cell):
            if tok == "**": bold = not bold
            elif tok == "↗": stream[-1]["rise"] = True
            elif tok.startswith("/"): stream[-1]["mark"] = "//beat" if tok.endswith("¦") else tok
            else: stream.append({"w": tok, "beat": beat, "mark": "", "bold": bold, "rise": False})
        if stream[-1]["mark"] == "//": stream[-1]["mark"] = "//beat"
    sc = open(os.path.join(fd, arg("--script"))).read(); sec = sc.split("## Kiểm chủ ngữ từng câu")[1].split("\n## ")[0]
    sents = [r.split("|")[2].strip() for r in sec.splitlines() if re.match(r"\| b\d\d \|", r)]
    out = []; pos = 0
    for k, s in enumerate(sents):
        ws = re.findall(WRE, s); seg = stream[pos:pos + len(ws)]
        if [fold(x["w"]) for x in seg] != [fold(w) for w in ws]: sys.exit(f"script/delivery word mismatch in sentence {k + 1}: {s}")
        if seg[-1]["mark"] not in ("//", "//beat"): sys.exit(f"sentence {k + 1} does not end on // or //|: {s}")
        f5 = re.sub(WRE, lambda m_: resp_word(m_.group(0)), s); f5 = f5.replace("Comment", "Com men")
        out.append({"id": f"s{k + 1:02d}", "beat": seg[0]["beat"], "text": s, "f5": f5, "q": s.endswith("?"), "rise": any(x["rise"] for x in seg),
                    "words": [{"w": x["w"], "mark": x["mark"], "bold": x["bold"], "syl": syl(x["w"])} for x in seg]})
        pos += len(ws)
    if pos != len(stream): sys.exit(f"delivery has {len(stream) - pos} words not in the script sentence table")
    W = arg("--work"); os.makedirs(W, exist_ok=True); json.dump(out, open(os.path.join(W, "sentences.json"), "w"), ensure_ascii=False, indent=1)
    cnt = {}
    for s in out:
        for w in s["words"]: cnt[w["mark"]] = cnt.get(w["mark"], 0) + 1
    print(len(out), "sentences,", pos, "words, marks", cnt)
    for s in out: print(s["id"], s["beat"], ("↗ " if s["rise"] else "") + s["f5"], "| bold:", " ".join(w["w"] for w in s["words"] if w["bold"]))

def batch(fd):
    W = arg("--work"); S = json.load(open(os.path.join(W, "sentences.json"))); only = (arg("--only") or "").split(",")
    items = [{"t": s["f5"], "seed": int(sd), "speed": 1.0, "out": f"{W}/{s['id']}-{sd}.wav"} for s in S if only == [""] or s["id"] in only for sd in arg("--seeds", "11,37,53").split(",")]
    p = os.path.join(W, arg("--name", "batch.json")); json.dump({"ref": REF, "ref_text": REF_TEXT, "items": items}, open(p, "w"), ensure_ascii=False, indent=1); print(len(items), "items ->", p)


# ---------------------------------------------------------------- DSP (asr-venv: numpy + faster-whisper + ffmpeg rubberband)
SR = 48000
LEAK = set("hôm nay trời sài gòn mát mẻ mình ngồi cà phê một chút rồi về nhà làm việc tiếp nha".split())
EN_ALIAS = [(k, v.lower()) for k, v in RESP.items() if not k.isdigit()] + [("nghìn", "ngàn"), ("ghịch", "ghịt"), ("lác", "lắc"), ("ngàn không trăm lẻ", "ngàn lẻ")]
DIG = "không một hai ba bốn năm sáu bảy tám chín".split()
def num_vi(n):
    n = int(n)
    if n < 10: return DIG[n]
    if n < 100:
        t, u = divmod(n, 10); s = ("mười" if t == 1 else DIG[t] + " mươi")
        return s + ("" if u == 0 else " " + ("mốt" if u == 1 and t > 1 else "lăm" if u == 5 else DIG[u]))
    if n < 1000:
        h, r = divmod(n, 100); return DIG[h] + " trăm" + ("" if r == 0 else (" lẻ " + DIG[r] if r < 10 else " " + num_vi(r)))
    th, r = divmod(n, 1000)
    return num_vi(th) + " ngàn" + ("" if r == 0 else " " + (("không trăm " + ("lẻ " if r < 10 else "")) if r < 100 else "") + num_vi(r))
def norm(s):
    s = unicodedata.normalize("NFC", s.lower()); s = re.sub(r"(\d)[.,](\d{3})", r"\1\2", s)
    s = re.sub(r"\d+", lambda m_: " " + num_vi(m_.group(0)) + " ", s); s = re.sub(r"[^\w ]", " ", s); s = " " + " ".join(s.split()) + " "
    for a, b in EN_ALIAS: s = s.replace(" " + a + " ", " " + b + " ")
    return s.split()
def tl(ws): return [fold(w) for w in ws]
def sim(h, t): return round(0.5 * difflib.SequenceMatcher(None, h, t, autojunk=False).ratio() + 0.5 * difflib.SequenceMatcher(None, tl(h), tl(t), autojunk=False).ratio(), 3)
_M = None
def model():
    global _M
    if _M is None:
        from faster_whisper import WhisperModel; _M = WhisperModel(os.environ.get("ASR_MODEL", "small"), device="cpu", compute_type=os.environ.get("ASR_COMPUTE", "float32"), cpu_threads=int(os.environ.get("ASR_THREADS", "0")))  # L-078: int8 hallucinates on this box since 20/10 ~23:00
    return _M
def pcm(f, sr=SR):
    import numpy as np
    return np.frombuffer(subprocess.run(["ffmpeg", "-loglevel", "error", "-i", f, "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"], capture_output=True).stdout, dtype="float32").copy()
def to16(x):
    import numpy as np
    return np.frombuffer(subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-ar", "16000", "-f", "f32le", "-"], input=x.astype("float32").tobytes(), capture_output=True).stdout, dtype="float32")
def stt(x48, lang="vi", words=True, target=None):
    """faster-whisper small; two paddings (whisper sometimes drops a short clip's first words or returns nothing for one of them):
    keep the variant closest to `target` tokens when given, else the longest."""
    import numpy as np
    a = to16(x48); best = None; bs = -1
    for pad in ((8000, 0, 4000) if target else (8000, 0)):
        segs, _ = model().transcribe(np.pad(a, pad), language=lang, beam_size=5, condition_on_previous_text=False, word_timestamps=words)
        ws = [(w.word.strip(), max(0.0, w.start - pad / 16000), max(0.0, w.end - pad / 16000)) for s in segs for w in s.words] if words else [(s.text.strip(), 0, 0) for s in segs]
        sc = sim([t for w, _, _ in ws for t in norm(w)], target) if target else len(ws)
        if sc > bs: best, bs = ws, sc
        if not words: break
    return best
def rb_pitch(x, semi):
    import numpy as np
    if len(x) < SR * 0.05: return x
    p = subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-af", f"rubberband=tempo=1.0:pitch={2 ** (semi / 12)}", "-f", "f32le", "-"], input=x.astype("float32").tobytes(), capture_output=True).stdout
    y = np.frombuffer(p, dtype="float32").copy(); return y[:len(x)] if len(y) >= len(x) else np.concatenate([y, np.zeros(len(x) - len(y), "float32")])
def frames(x, hop=None):
    import numpy as np
    hop = hop or int(0.01 * SR); n = len(x) // hop
    return np.sqrt(np.mean(x[:n * hop].reshape(n, hop) ** 2, axis=1)) if n else np.zeros(0)
def sil_thr(e):
    import numpy as np
    return max(0.006, 0.06 * float(np.percentile(e, 95))) if len(e) else 0.01
def active_db(x, a, b, thr):
    """loudness of the voiced frames only in [a,b) seconds (so a pause inside the span does not dilute it)."""
    import numpy as np
    e = frames(x[int(max(0, a) * SR):int(max(0, b) * SR)]); e = e[e > thr]
    return 20 * np.log10(float(np.sqrt(np.mean(e ** 2)))) if len(e) else None
def f0(x16):
    import numpy as np
    sr = 16000; hop = int(.01 * sr); win = int(.04 * sr); o = []
    for j in range(0, len(x16) - win, hop):
        fr = x16[j:j + win] - x16[j:j + win].mean()
        if np.sqrt(np.mean(fr ** 2)) < 0.015: o.append(0); continue
        ac = np.correlate(fr, fr, "full")[win - 1:]; lo, hi = int(sr / 300), int(sr / 70); k = lo + int(np.argmax(ac[lo:hi])); o.append(sr / k if ac[k] > 0.35 * ac[0] else 0)
    return np.array(o)
def rise_st(x48, t_last, t_start, t_end):
    """median F0 of the last syllable vs the 2 syllables before it (semitones): the end of the question, where a rise is heard; the whole-sentence
    median is useless here because F5 declines ~5 st over a sentence and sắc syllables early on sit high."""
    import numpy as np
    F = f0(to16(x48)); a, b, c = max(0, int(t_start * 100)), max(0, int(t_last * 100)), max(0, int(t_end * 100))
    p, s = F[a:b], F[b:c]; p, s = p[p > 0], s[s > 0]
    return float(12 * np.log2(np.median(s) / np.median(p))) if len(p) > 3 and len(s) > 2 else None
def targets(s):
    """respelled syllable tokens of the sentence + the word index each belongs to."""
    T = []
    for i, w in enumerate(s["words"]):
        for tok in re.findall(WRE, resp_word(w["w"]).lower()): T.append((tok, i))
    return T
def align(ws, T, dur):
    """target token k -> (t0, t1) from whisper words (a word normalising to n tokens is split evenly); unmatched tokens interpolated."""
    flat = []
    for w, a, b in ws:
        nt = norm(w)
        for j, tok in enumerate(nt): flat.append((tok, a + (b - a) * j / len(nt), a + (b - a) * (j + 1) / len(nt)))
    sm = difflib.SequenceMatcher(None, tl([f[0] for f in flat]), tl([t for t, _ in T]), autojunk=False); tm = {}
    for a_, b_, n_ in sm.get_matching_blocks():
        for d in range(n_): tm[b_ + d] = flat[a_ + d][1:]
    out = []; ks = sorted(tm)
    for k in range(len(T)):
        if k in tm: out.append(list(tm[k])); continue
        lo = max([j for j in ks if j < k], default=None); hi = min([j for j in ks if j > k], default=None)
        t0 = tm[lo][1] if lo is not None else (ws[0][1] if ws else 0.0); t1 = tm[hi][0] if hi is not None else (ws[-1][2] if ws else dur)
        n0 = lo if lo is not None else -1; n1 = hi if hi is not None else len(T); fr0 = (k - n0 - 1) / (n1 - n0 - 1); fr1 = (k - n0) / (n1 - n0 - 1)
        out.append([t0 + (t1 - t0) * fr0, t0 + (t1 - t0) * fr1])
    return out, len(tm) / max(1, len(T))
def take_stats(f, s, T):
    import numpy as np
    tgt = [t for t, _ in T]
    x = pcm(f); ws = stt(x, target=tgt); i = 0; cut = 0.0
    while i < len(ws) and norm(ws[i][0]) and norm(ws[i][0])[0] in LEAK and norm(ws[i][0])[0] != fold(tgt[0]) and fold(norm(ws[i][0])[0]) != fold(tgt[0]) and ws[i][2] < 1.5:
        cut = ws[i][2] + 0.03; i += 1
    ws = [(w, a - cut, b - cut) for w, a, b in ws[i:]]; x = x[int(cut * SR):]
    hyp = [t for w, _, _ in ws for t in norm(w)]; sc = sim(hyp, tgt)
    e = frames(x); thr = sil_thr(e)
    a0, a1 = (ws[0][1], ws[-1][2]) if ws else (0, len(x) / SR)
    voiced = max(0.3, float((e[int(a0 * 100):int(a1 * 100)] > thr).sum()) * 0.01); rate = len(tgt) / voiced
    tt, cov = align(ws, T, len(x) / SR); rs = rise_st(x, tt[-1][0], tt[max(0, len(tt) - 3)][0], tt[-1][1] + 0.05) if s["q"] else None
    return {"x": x, "ws": ws, "hyp": " ".join(w for w, _, _ in ws), "sim": sc, "rate": round(rate, 2), "rise": None if rs is None else round(rs, 2), "tt": tt, "cov": round(cov, 2), "thr": thr}

def stress_of(x, toks, sd, thr):
    """(dB vs rest of sentence without its last syllable, dB vs 2 syllables each side, ka, kb) of the bold chunk; toks = [tok, t0, t1, word_idx]."""
    import numpy as np
    bk = [i for i, k in enumerate(toks) if sd["words"][k[3]]["bold"]]
    if not bk: return None
    ka, kb = bk[0], bk[-1]; last = len(toks) - 1; e_db = active_db(x, toks[ka][1], toks[kb][2], thr)
    def grp(ix):
        if not ix: return None
        seg = np.concatenate([x[int(max(0, toks[i][1]) * SR):int(toks[i][2] * SR)] for i in ix]); return active_db(seg, 0, len(seg) / SR, thr)
    r_db = grp([i for i in range(len(toks)) if (i < ka or i > kb) and i != last]); n_db = grp(list(range(max(0, ka - 2), ka)) + list(range(kb + 1, min(len(toks), kb + 3))))
    return (None if e_db is None or r_db is None else round(e_db - r_db, 1)), (None if e_db is None or n_db is None else round(e_db - n_db, 1)), ka, kb

def pick(fd):
    import numpy as np
    W = arg("--work"); S = json.load(open(os.path.join(W, "sentences.json"))); only = [o for o in (arg("--only") or "").split(",") if o]
    resf = os.path.join(W, "picks.json"); res = json.load(open(resf)) if os.path.exists(resf) else {}
    for s in S:
        if only and s["id"] not in only: continue
        T = targets(s); cands = []
        EVF = arg("--evals"); EVJ = json.load(open(EVF)) if EVF else None  # v18 R8: evals.json from a gate script; takes with ok=false are rejected
        for f in sorted(glob.glob(f"{W}/{s['id']}-[0-9]*.wav")):
            if EVJ is not None and not EVJ.get(os.path.basename(f), {}).get("ok"): continue
            st = take_stats(f, s, T); st["take"] = os.path.basename(f)
            st["score"] = st["sim"] + (0.05 if s["q"] and (st["rise"] or -9) > 0 else 0) + (0.01 * max(-5.0, min(3.0, st["rise"] or -5.0)) if s["q"] else 0)
            cands.append(st)
        if not cands: print(s["id"], "no takes"); continue
        b = max(cands, key=lambda c: c["score"]); x = b["x"].copy(); tt = b["tt"]; thr = b["thr"]
        # question: raise the last syllable (adaptive vs the take's own fall), tempo unchanged
        semi = None
        if s["q"] and final_tone(s["text"]) in L082: print(s["id"], "L-082: final syllable", final_tone(s["text"]), "→ no pitch lift", flush=True)
        elif s["q"]:
            # nặng/huyền/hỏi endings fall several st on their own: raise until the delivered last syllable measures ≥ +1 st (cap 8 st)
            lw = int(tt[-1][0] * SR); semi = 1.0; x0 = x  # smallest shift that proves the rise (v18: start gentle, Kokoro note: no big push on huyền/nặng)
            while True:
                x = np.concatenate([x0[:lw], rb_pitch(x0[lw:], semi)]); r_ = rise_st(x, tt[-1][0], tt[max(0, len(tt) - 3)][0], tt[-1][1] + 0.05)
                if (r_ is not None and r_ >= 0.6) or semi >= 6.0: break  # v18: +3–4 st on a nặng/huyền ending turns the tone into sắc («sạch»→«xác», «từ»→«tờ», whisper medium)
                semi = min(6.0, semi + 0.5)
        # stress: gain on the bold chunk, ≥2 dB (target 2.5) over the rest of the sentence AND over its 2 neighbour syllables each side; no tempo
        bk = [k for k, (_, wi) in enumerate(T) if s["words"][wi]["bold"]]; emph = None
        if bk:
            ka, kb = bk[0], bk[-1]; last = len(T) - 1
            def deltas(y):
                e_db = active_db(y, tt[ka][0], tt[kb][1], thr)
                rest = [(tt[k][0], tt[k][1]) for k in range(len(T)) if (k < ka or k > kb) and k != last]
                nb = [(tt[k][0], tt[k][1]) for k in list(range(max(0, ka - 2), ka)) + list(range(kb + 1, min(len(T), kb + 3)))]
                def grp(iv):
                    if not iv: return None
                    seg = np.concatenate([y[int(a * SR):int(c * SR)] for a, c in iv]); return active_db(seg, 0, len(seg) / SR, thr)
                r_db, n_db = grp(rest), grp(nb)
                return (None if e_db is None or r_db is None else e_db - r_db), (None if e_db is None or n_db is None else e_db - n_db)
            d0 = deltas(x); have = min([d for d in d0 if d is not None], default=0.0); g = float(min(7.0, max(0.0, 2.6 - have)))
            if g > 0:
                a, c = int(tt[ka][0] * SR), int(tt[kb][1] * SR); xf = int(0.02 * SR); m_ = np.ones(len(x), "float32"); k_ = 10 ** (g / 20); m_[a:c] = k_
                m_[max(0, a - xf):a] = np.linspace(1, k_, a - max(0, a - xf)); m_[c:min(len(x), c + xf)] = np.linspace(k_, 1, min(len(x), c + xf) - c); x = x * m_
            d1 = deltas(x); emph = {"words": " ".join(w["w"] for w in s["words"] if w["bold"]), "before_db": [None if d is None else round(d, 1) for d in d0], "gain_db": round(g, 1), "after_db": [None if d is None else round(d, 1) for d in d1]}
        # split at every delivery mark inside the sentence: cut at the quietest point between the two words
        e = frames(x); cuts = []; ends = []
        kend = {}
        for k, (_, wi) in enumerate(T): kend[wi] = k
        for wi, w in enumerate(s["words"][:-1]):
            if w["mark"] not in ("/", "///", "//breath"): continue  # //breath: short breath after a counted number («Một.», «Hai.», clip-05 v4)
            k1 = kend[wi]; k2 = k1 + 1; A = int(((tt[k1][0] + tt[k1][1]) / 2) * 100); B = int(((tt[k2][0] + tt[k2][1]) / 2) * 100)
            A, B = max(0, min(A, len(e) - 1)), max(1, min(B, len(e)))
            if B <= A + 1: c = int(tt[k1][1] * 100)
            else:
                seg = e[A:B]; sil = seg < thr; best = (0, 0); cur = 0
                for j, v in enumerate(sil):
                    cur = cur + 1 if v else 0
                    if cur > best[0]: best = (cur, j)
                c = A + (best[1] - best[0] // 2 if best[0] else int(np.argmin(seg)))
            cuts.append(c * int(0.01 * SR)); ends.append(w["mark"])
        bounds = [0] + cuts + [len(x)]; pieces = []; marks = ends + [s["words"][-1]["mark"]]
        fade = int(0.008 * SR)
        for j in range(len(bounds) - 1):
            p_ = x[bounds[j]:bounds[j + 1]].copy(); idx = np.where(np.abs(p_) > max(0.004, thr * 0.5))[0]
            a0 = max(0, idx[0] - int(0.015 * SR)) if len(idx) else 0; a1 = min(len(p_), idx[-1] + int(0.04 * SR)) if len(idx) else len(p_)
            p_ = p_[a0:a1]
            if j > 0: p_[:fade] *= np.linspace(0, 1, min(fade, len(p_)))[:len(p_[:fade])]
            if j < len(bounds) - 2: p_[-fade:] *= np.linspace(1, 0, min(fade, len(p_)))[-len(p_[-fade:]):]
            off = (bounds[j] + a0) / SR; fn = f"{s['id']}-p{j}.npy"; np.save(os.path.join(W, fn), p_.astype("float32"))
            toks = [[T[k][0], round(tt[k][0] - off, 3), round(tt[k][1] - off, 3), T[k][1]] for k in range(len(T)) if bounds[j] / SR - 0.02 <= (tt[k][0] + tt[k][1]) / 2 < bounds[j + 1] / SR]
            pieces.append({"file": fn, "mark_after": marks[j], "dur": round(len(p_) / SR, 3), "tokens": toks})
        res[s["id"]] = {"take": b["take"], "sim": b["sim"], "rate": b["rate"], "rise_raw": b["rise"], "rise_shift_st": semi, "align_cov": b["cov"], "stt": b["hyp"], "emphasis": emph,
                        "pieces": pieces, "candidates": [(c["take"], c["sim"], c["rate"], c["rise"]) for c in cands]}
        print(s["id"], "->", b["take"], "sim", b["sim"], "rate", b["rate"], "rise", b["rise"], "cov", b["cov"], "| cands", [(c["take"][-6:-4], c["sim"], c["rate"], c["rise"]) for c in cands], "| emph", emph and (emph["before_db"], emph["gain_db"], emph["after_db"]), "| pieces", len(pieces), "|", b["hyp"], flush=True)
        json.dump(res, open(resf, "w"), ensure_ascii=False, indent=1)

def voice(fd):
    import numpy as np
    W = arg("--work"); S = json.load(open(os.path.join(W, "sentences.json"))); P = json.load(open(os.path.join(W, "picks.json"))); pre = arg("--prefix", "c04v16b")
    PCS = {p["file"]: np.load(os.path.join(W, p["file"])) for s in S for p in P[s["id"]]["pieces"]}
    THR = sil_thr(frames(np.concatenate(list(PCS.values()))))  # same relative silence threshold as measure()
    def edges(x):
        e = frames(x); i = np.where(e >= THR)[0]
        return (i[0] * 0.01, len(x) / SR - (i[-1] + 1) * 0.01) if len(i) else (0.0, 0.0)
    pure = sum(len(PCS[p["file"]]) / SR - sum(edges(PCS[p["file"]])) for s in S for p in P[s["id"]]["pieces"])
    plan = arg("--plan", "auto")
    if plan == "auto": plan = "A" if pure <= 47.9 else "B"
    G = PLANS[plan]; out = []; t = 0.0; prev = None; rows = []
    for s in S:
        sr_ = {"id": s["id"], "beat": s["beat"], "text": s["text"], "pieces": []}
        for p in P[s["id"]]["pieces"]:
            x = PCS[p["file"]]; lead, tail = edges(x); pad = 0.0; sh_ = 0.0
            if prev is not None:
                pad = max(0.0, G[prev[0]] - prev[1] - lead)
                if prev[0] == "//hook" and prev[1] + lead > G["//hook"]:  # L-027: the hook join must measure ≤0.1s → shave the quiet tail/lead (no speech removed)
                    ex = prev[1] + lead - G["//hook"]; cut_t = min(ex, max(0.0, prev[1] - 0.01)); n_ = int(round(cut_t * SR))
                    if n_ > 0: out[-1] = out[-1][:-n_].copy(); fo_ = min(len(out[-1]), int(0.006 * SR)); out[-1][-fo_:] *= np.linspace(1, 0, fo_); t -= n_ / SR; sr_prev = rows[-1] if rows and not sr_["pieces"] else sr_; sr_prev["pieces"][-1]["tail_shaved_s"] = round(cut_t, 3)
                    ex -= cut_t; cut_l = min(ex, max(0.0, lead - 0.01)); n2 = int(round(cut_l * SR))
                    if n2 > 0: x = x[n2:]; lead -= n2 / SR; sh_ = n2 / SR
                    fl_ = min(len(x), int(0.006 * SR)); x = x.copy(); x[:fl_] *= np.linspace(0, 1, fl_)
                out.append(np.zeros(int(round(pad * SR)), "float32")); t += int(round(pad * SR)) / SR
            st = t; out.append(x); t += len(x) / SR; prev = (p["mark_after"], tail)
            sr_["pieces"].append({"start": round(st + lead, 3), "end": round(t - tail, 3), "file_start": round(st, 3), "mark_after": p["mark_after"], "plan_pause": G[p["mark_after"]],
                                  "tokens": [[k[0], round(st + k[1] - sh_, 3), round(st + k[2] - sh_, 3), k[3]] for k in p["tokens"]]})
        sr_["start"] = sr_["pieces"][0]["start"]; sr_["end"] = sr_["pieces"][-1]["end"]; rows.append(sr_)
    y = np.concatenate(out); raw = os.path.join(W, f"voice-only-{pre}-raw.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", raw], input=y.astype("float32").tobytes(), check=True)
    wav = os.path.join(fd, f"voice-only-{pre}.wav"); m4a = arg("--m4a", f"/workspace/clip-04-v16b-voice-only.m4a")
    # -14 LUFS: linear gain + fast peak limiter (speech crest factor needs ~4 dB of peak limiting). The limiter shaves the loudest words first,
    # i.e. the stressed ones, so: measure every sentence's stress on the DELIVERED signal and add gain to the bold chunk until it is ≥2.3 dB (≤3 rounds).
    Sd = {s["id"]: s for s in S}; extra = {}
    for v_ in P.values(): v_.pop("extra_gain_db", None)
    def render(yy):
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", raw], input=yy.astype("float32").tobytes(), check=True)
        I0 = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", subprocess.run(["ffmpeg", "-hide_banner", "-i", raw, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr)[-1])
        gdb = -14.0 - I0
        for _ in range(3):  # the limiter lowers the integrated loudness: re-aim until within 0.3 LU of -14
            pk = 20 * np.log10(float(np.max(np.abs(yy))) + 1e-9) + gdb
            af = f"volume={gdb:.2f}dB" + (",alimiter=limit=0.84:attack=1:release=30:level=disabled" if pk > -1.5 else "")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af", af, "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le", wav], check=True)
            I1 = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", subprocess.run(["ffmpeg", "-hide_banner", "-i", wav, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr)[-1])
            if abs(I1 + 14.0) <= 0.3: break
            gdb += -14.0 - I1
        return pcm(wav)
    for rnd in range(6):  # v18: up to 5 boost rounds (limiter keeps shaving the loudest words)
        z = render(y); thr_z = sil_thr(frames(z)); todo = 0
        if rnd == 5: break
        for r_ in rows:
            toks = [k for p_ in r_["pieces"] for k in p_["tokens"]]; so = stress_of(z, toks, Sd[r_["id"]], thr_z)
            if not so: continue
            have = min([d for d in so[:2] if d is not None], default=9.0)
            if have >= 2.3: continue
            add = min(3.0, 2.7 - have); extra[r_["id"]] = round(extra.get(r_["id"], 0) + add, 1); todo += 1
            a, c = int(max(0, toks[so[2]][1]) * SR), int(toks[so[3]][2] * SR); xf = int(0.02 * SR); m_ = np.ones(len(y), "float32"); k_ = 10 ** (add / 20); m_[a:c] = k_
            m_[max(0, a - xf):a] = np.linspace(1, k_, a - max(0, a - xf)); m_[c:min(len(y), c + xf)] = np.linspace(k_, 1, min(len(y), c + xf) - c); y = y * m_
        print("stress round", rnd, "sentences boosted", todo, flush=True)
        if not todo: break
    for sid_, g_ in extra.items(): P[sid_]["extra_gain_db"] = g_
    json.dump(P, open(os.path.join(W, "picks.json"), "w"), ensure_ascii=False, indent=1)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-c:a", "aac", "-b:a", "96k", "-ac", "1", "-movflags", "+faststart", m4a], check=True)
    tj = {"prefix": pre, "plan": plan, "plan_pauses": G, "pure_speech_s": round(pure, 2), "total_s": round(len(y) / SR, 3), "wav": os.path.relpath(wav, REPO), "m4a": m4a, "sentences": rows}
    json.dump(tj, open(os.path.join(fd, f"voice-only-{pre}.timing.json"), "w"), ensure_ascii=False, indent=1)
    print("plan", plan, "pure", round(pure, 2), "total", round(len(y) / SR, 2), "->", wav, m4a)

def measure(fd):
    """re-measure the DELIVERED wav: pause at every delivery mark vs plan, breaks inside phrases, stress dB, question F0, STT per sentence, rate, totals."""
    import numpy as np
    pre = arg("--prefix", "c04v16b"); TJ = json.load(open(os.path.join(fd, f"voice-only-{pre}.timing.json"))); W = arg("--work")
    S = {s["id"]: s for s in json.load(open(os.path.join(W, "sentences.json")))}; P = json.load(open(os.path.join(W, "picks.json")))
    x = pcm(os.path.join(REPO, TJ["wav"])); e = frames(x); thr = sil_thr(e); sil = e < thr; G = TJ["plan_pauses"]
    def run_at(a, b):
        a, b = max(0, int(a * 100)), min(len(sil), int(np.ceil(b * 100))); best = cur = 0
        for v in sil[a:b]: cur = cur + 1 if v else 0; best = max(best, cur)
        return best / 100
    TGT = {"/": (0.15, 0.2), "//": (G["//"] - 0.03, G["//"] + 0.05), "//beat": (G["//beat"] - 0.03, G["//beat"] + 0.05), "///": (G["///"] - 0.03, G["///"] + 0.05), "//hook": (0.0, 0.1), "//breath": (G.get("//breath", 0.28) - 0.04, G.get("//breath", 0.28) + 0.05)}
    NAME = {"/": "phẩy/hai chấm", "//": "hết câu", "//beat": "hết beat", "///": "lặng có chủ ý", "//hook": "ghép hook (L-027 ≤0,1s)", "//breath": "nghỉ thở sau số đếm"}
    rows = []; flags = []; warns = []; allp = []; comma_max = 0; period_min = 9
    flat = [(s, j, p) for s in TJ["sentences"] for j, p in enumerate(s["pieces"])]
    for n_, (s, j, p) in enumerate(flat[:-1]):
        q = flat[n_ + 1][2]; pz = run_at(p["end"] - 0.03, q["start"] + 0.03); mk = p["mark_after"]; lo, hi = TGT[mk]
        last_w = S[s["id"]]["words"][p["tokens"][-1][3]]["w"] if p["tokens"] else "?"
        stt_ = "ok"
        if pz > 0.8: stt_ = "✖ >0.8s"
        elif pz > 0.5: stt_ = "✖ >0.5s"
        elif mk == "/" and pz < 0.15: stt_ = "✖ phẩy <0.15s"
        elif mk == "//hook" and pz > 0.1: stt_ = "✖ hook >0.1s (L-027)"
        elif mk not in ("/", "//hook") and pz < 0.1: stt_ = "✖ hết câu <0.1s"
        elif not (lo - 0.005 <= pz <= hi + 0.005): stt_ = "⚠ lệch plan"
        allp.append({"sid": s["id"], "after": last_w, "mark": mk, "kind": NAME[mk], "plan": G[mk], "pause": round(pz, 3), "status": stt_})
        if mk == "/": comma_max = max(comma_max, pz)
        elif mk != "//hook": period_min = min(period_min, pz)
        if stt_.startswith("✖"): flags.append(f"{s['id']}: nghỉ sau «{last_w}» ({NAME[mk]}) {pz:.2f}s, plan {G[mk]}s ({stt_})")
        elif stt_.startswith("⚠"): warns.append(f"{s['id']}: nghỉ sau «{last_w}» {pz:.2f}s, plan {G[mk]}s")
    # silences (E1 schema, check-rules.py) + inner commas. Every silence run ≥0.05s between the first and last spoken word is attributed by its
    # midpoint to the word boundary k with mid(word k) ≤ run-mid < mid(word k+1) (STT word edges often swallow pauses, e.g. stop closures).
    HOOKB = set((arg("--hook-beats", "b01") or "").split(","))
    MARKAT = {"/": "comma", "//": "sentence", "//hook": "sentence", "//beat": "beat", "///": "beat", "//breath": "sentence"}
    wl = []  # word-level: [chunk_id, word_idx, word, start, end, mark_after (piece end) or None]
    for s in TJ["sentences"]:
        sd = S[s["id"]]
        for p in s["pieces"]:
            for i, k in enumerate(p["tokens"]):
                k0, k1 = min(max(k[1], p["start"]), p["end"]), min(max(k[2], p["start"]), p["end"])  # STT edges can spill into the join silence
                if wl and wl[-1][0] == s["id"] and wl[-1][1] == k[3]: wl[-1][4] = k1
                else: wl.append([s["id"], k[3], sd["words"][k[3]]["w"] if 0 <= k[3] < len(sd["words"]) else k[0], k0, k1, None])
            wl[-1][5] = p["mark_after"]
    mids = [(w[3] + w[4]) / 2 for w in wl]
    def at_mark(k):
        A, B = wl[k], wl[k + 1]
        if A[0] != B[0] or (A[5] and A[5] != "/"): return MARKAT.get(A[5], "beat")
        if A[1] + 1 in (S[A[0]].get("inner_commas") or []) or A[5] == "/": return "comma"  # inner_commas = index of the word AFTER the comma
        return "none"
    silences = []; bmax = {}; cur = None
    for j_, v in enumerate(list(sil) + [False]):
        if v and cur is None: cur = j_
        if not v and cur is not None:
            d = (j_ - cur) / 100; c_ = (cur + j_) / 200
            if d >= 0.05 and mids[0] < c_ < mids[-1]:
                k = max(i for i in range(len(wl) - 1) if mids[i] <= c_); bmax[k] = max(bmax.get(k, 0), d)
                silences.append({"chunk_id": wl[k][0] if wl[k][0] == wl[k + 1][0] else f"{wl[k][0]}→{wl[k + 1][0]}", "t_start": round(cur / 100, 2), "t_end": round(j_ / 100, 2), "dur_s": round(d, 2),
                                 "at_mark": at_mark(k), "context_before": " ".join(w[2] for w in wl[max(0, k - 2):k + 1]), "context_after": " ".join(w[2] for w in wl[k + 1:k + 4])})
            cur = None
    # inner commas (inside one F5 output, not a join) as pauses too. Hook beat (L-027, v18 R8): ≤0.1s; elsewhere 0.12–0.22s.
    for k in range(len(wl) - 1):
        A = wl[k]
        if A[0] != wl[k + 1][0] or A[1] + 1 not in (S[A[0]].get("inner_commas") or []): continue
        pz = bmax.get(k, 0.0); hook = S[A[0]]["beat"] in HOOKB
        stt_ = ("✖ phẩy trong hook >0.1s (L-027)" if pz > 0.1 else "ok") if hook else ("ok" if 0.12 <= pz <= 0.22 else "✖ phẩy trong chunk ngoài 0.12–0.22s")
        allp.append({"sid": A[0], "after": A[2], "mark": "/", "inner": True, "kind": "phẩy trong chunk" + (" (hook ≤0,1s)" if hook else ""), "plan": 0.1 if hook else 0.18, "pause": round(pz, 3), "status": stt_})
        if not hook: comma_max = max(comma_max, pz)
        if stt_.startswith("✖"): flags.append(f"{A[0]}: phẩy sau «{A[2]}» {pz:.2f}s ({stt_})")
    if comma_max >= period_min: flags.append(f"thứ bậc nghỉ: phẩy dài nhất {comma_max:.2f}s ≥ hết câu ngắn nhất {period_min:.2f}s")
    total_pause = 0.0
    for s in TJ["sentences"]:
        sd = S[s["id"]]; pk = P[s["id"]]; toks = [k for p in s["pieces"] for k in p["tokens"]]; T = targets(sd); r = {"id": s["id"], "beat": s["beat"], "text": sd["text"], "start": s["start"], "end": s["end"]}
        # breaks inside a phrase (no mark): silence > 0.25s between consecutive tokens of the same piece
        mid = []
        for p in s["pieces"]:
            for a, b in zip(p["tokens"], p["tokens"][1:]):
                z = run_at(a[2] - 0.03, b[1] + 0.03)
                if z > 0.25: mid.append(f"«{a[0]} {b[0]}» {z:.2f}s")
        r["mid_breaks"] = mid
        for m_ in mid: flags.append(f"{s['id']}: ngắt giữa cụm {m_}")
        # stress
        r["stress"] = None; so = stress_of(x, toks, sd, thr)
        if so:
            dr, dn = so[0], so[1]
            r["stress"] = {"words": " ".join(w["w"] for w in sd["words"] if w["bold"]), "vs_rest_db": dr, "vs_neighbours_db": dn, "gain_applied_db": round((pk.get("emphasis") or {}).get("gain_db", 0) + (pk.get("extra_gain_db") or 0), 1)}
            if (dr is not None and dr < 2) or (dn is not None and dn < 2): flags.append(f"{s['id']}: nhấn «{r['stress']['words']}» chỉ {dr} dB so câu / {dn} dB so chữ kề (<2 dB)")
        # question rise (measured on the delivered audio)
        r["rise_st"] = None; r["final_tone"] = final_tone(sd["text"]); r["pitch_shift_st"] = pk.get("rise_shift_st") or 0
        if sd["q"]:
            rs = rise_st(x, toks[-1][1], toks[max(0, len(toks) - 3)][1], toks[-1][2] + 0.05); r["rise_st"] = None if rs is None else round(rs, 2)
            if r["final_tone"] in L082:
                r["rise_exempt"] = "L-082"
                if r["pitch_shift_st"]: flags.append(f"{s['id']}: câu hỏi kết thúc thanh {r['final_tone']} nhưng có nâng pitch {r['pitch_shift_st']} st (L-082 cấm)")
            elif rs is None or rs < 0.5: flags.append(f"{s['id']}: câu hỏi cuối {r['rise_st']} st (cần lên giọng ≥ +0.5 st)")
        # STT of the delivered sentence vs the text
        seg = x[int(max(0, s["start"] - 0.05) * SR):int((s["end"] + 0.08) * SR)]; ws = stt(seg, target=[t for t, _ in T]); hyp = [t for w, _, _ in ws for t in norm(w)]
        r["stt"] = " ".join(w for w, _, _ in ws); r["stt_sim"] = sim(hyp, [t for t, _ in T])
        if r["stt_sim"] < 0.8: flags.append(f"{s['id']}: STT khớp {r['stt_sim']} (<0.8): «{r['stt']}»")
        ee = e[int(s["start"] * 100):int(s["end"] * 100)]; voiced = max(0.3, float((ee > thr).sum()) * 0.01); r["syll_per_s"] = round(len(T) / voiced, 2)
        r["speech_s"] = round(sum(p["end"] - p["start"] for p in s["pieces"]), 2)
        # L-074 (2026-10-20): no syllables/s cap — fast reading approved by Hiệp; pace is judged only via STT (swallowed words)
        r["take"] = pk["take"]; r["candidates"] = pk["candidates"]; rows.append(r)
    # English words of b03 (respelled): English STT on each word span
    en = []
    for s in TJ["sentences"]:
        sd = S[s["id"]]
        for wi, w in enumerate(sd["words"]):
            if w["w"].lower() in ("airport", "hotel", "ticket", "passport", "luggage", "comment", "dunlosky", "yang", "clip"):
                tk = [k for p in s["pieces"] for k in p["tokens"] if k[3] == wi]
                if not tk: continue
                a, b = tk[0][1] - 0.06, tk[-1][2] + 0.08; h = stt(x[int(max(0, a) * SR):int(b * SR)], lang="en", words=False)
                en.append({"sid": s["id"], "word": w["w"], "said": resp_word(w["w"]), "t": round(tk[0][1], 2), "en_stt": " ".join(z[0] for z in h)})
    lufs = subprocess.run(["ffmpeg", "-hide_banner", "-i", os.path.join(REPO, TJ["wav"]), "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
    I = re.findall(r"I:\s+(-?[\d.]+) LUFS", lufs)[-1]
    tot = TJ["total_s"]; pause_sum = round(sum(p["pause"] for p in allp), 2); speech = round(sum(r["speech_s"] for r in rows), 2)
    res = {"voice_prefix": pre, "plan": TJ["plan"], "plan_pauses": G, "total_s": tot, "speech_s": speech, "pause_at_marks_s": pause_sum, "pure_speech_pre_s": TJ["pure_speech_s"], "lufs": float(I),
           "limit_s": 58.0, "over_s": round(max(0, tot - 58.0), 2), "pauses": allp, "silences": silences, "sentences": rows, "english": en, "flags": flags, "warnings": warns}
    if tot > 58.0: flags.append(f"tổng giọng {tot:.2f}s > 58s (dư {tot - 58:.2f}s)")
    out = arg("--out", os.path.join(fd, f"prosody-measure-{pre}.md")); json.dump(res, open(out[:-3] + ".json", "w"), ensure_ascii=False, indent=1)
    md = [f"# Đo prosody bản giọng nháp — {pre} ({arg('--script-name', 'script-v16c')}, F5 Thái Sơn speed 1.0, plan {TJ['plan']})", "",
          f"File: `{TJ['m4a']}` + `{TJ['wav']}`. Đo trên chính file giao (sau loudnorm). Nghỉ = đoạn lặng dài nhất (năng lượng, khung 10ms) tại chỗ nối hai cụm; nhấn = độ to (chỉ tính khung có tiếng) của cụm đậm so phần còn lại của câu (bỏ âm tiết cuối) và so 2 âm tiết kề mỗi bên; lên giọng = trung vị F0 âm tiết cuối so 2 âm tiết ngay trước (semitone); STT = faster-whisper {os.environ.get('ASR_MODEL', 'small')} float32 (vi) trên đoạn câu, so với lời (số/từ EN quy về cách đọc).", "",
          "## Tổng", "",
          f"- **Tổng thời lượng giọng: {tot:.2f}s** (giới hạn 58s → {'ĐẠT' if tot <= 58 else f'DƯ {tot - 58:.2f}s'}); loudness {I} LUFS.",
          f"- Nói thuần (tổng các cụm, bỏ lặng hai đầu): {TJ['pure_speech_s']:.2f}s → plan {TJ['plan']} ({'≤' if TJ['pure_speech_s'] <= 47.9 else '>'} 47,9s). Tổng nghỉ đo tại {len(allp)} chỗ ngắt: {pause_sum:.2f}s.",
          f"- Thứ bậc: phẩy dài nhất {comma_max:.2f}s < hết câu ngắn nhất {period_min:.2f}s {'✓' if comma_max < period_min else '✖'}.",
          f"- Cờ chặn: **{len(flags)}** · cảnh báo: {len(warns)}.", "",
          "## Từng câu", "", "| Câu | Beat | Bắt đầu–kết thúc (s) | Nhấn: dB so câu / so chữ kề (gain đã thêm) | Cuối câu hỏi (st) | STT (khớp) | Take |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        st_ = r["stress"]; em = "—" if not st_ else f"«{st_['words']}» {st_['vs_rest_db']:+} / {st_['vs_neighbours_db']:+} (+{st_['gain_applied_db']})"
        md.append(f"| {r['id']} {r['text']} | {r['beat']} | {r['start']:.2f}–{r['end']:.2f} | {em} | {'—' if not S[r['id']]['q'] else (str(r['rise_st']) + ' · thanh ' + r['final_tone'] + (' · miễn L-082, không nâng pitch' if r.get('rise_exempt') else ' · nâng ' + str(r['pitch_shift_st']) + ' st'))} | {r['stt']} ({r['stt_sim']}) | {r['take']} |")
    md += ["", "## Nghỉ tại từng ký hiệu (đo / plan)", "", "| Câu | Sau chữ | Ký hiệu | Plan (s) | Đo (s) | Kết quả |", "|---|---|---|---|---|---|"]
    md += [f"| {p['sid']} | {p['after']} | `{p['mark'].replace('//beat', '//|').replace('|', '¦')}` {p['kind']} | {p['plan']} | {p['pause']:.2f} | {p['status']} |" for p in allp]
    md += ["", "## Từ tiếng Anh (đọc theo phiên âm, STT tiếng Anh trên đúng đoạn từ đó)", "", "| Câu | Từ | Đọc | t (s) | STT EN nghe ra |", "|---|---|---|---|---|"]
    md += [f"| {z['sid']} | {z['word']} | «{z['said']}» | {z['t']} | {z['en_stt'] or '(trống)'} |" for z in en]
    md += ["", "## Không đạt (cờ chặn)", ""] + ([f"- {f_}" for f_ in flags] or ["- (không có)"]) + ["", "## Cảnh báo", ""] + ([f"- {w_}" for w_ in warns] or ["- (không có)"])
    open(out, "w").write("\n".join(md) + "\n"); print("total", tot, "flags", len(flags), "warns", len(warns), "->", out)

if __name__ == "__main__":
    cmd = sys.argv[1]; fd = os.path.abspath(sys.argv[2])
    {"parse": parse, "batch": batch, "pick": lambda f: pick(f), "voice": lambda f: voice(f), "measure": lambda f: measure(f)}[cmd](fd)
