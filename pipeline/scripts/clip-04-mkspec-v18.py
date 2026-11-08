#!/usr/bin/env python3
"""clip-04 v18 spec (Stage 2 render). Voice = the approved final/voice-only-c04v18.wav (Rule Reviewer PASS c0ec507), untouched:
lines are frame-aligned slices of it (cut inside the measured silences), written to video-engine/public/voice/c04v18-<line>.wav/.json;
spec.voice_track = the same slices concatenated (+1.0s hold after b07, L-080) so build-final muxes the approved audio sample-exact.
usage: clip-04-mkspec-v18.py slices   (cut + json; needs slice-stt.json from `stt` for stt fields)
       clip-04-mkspec-v18.py stt      (faster-whisper medium float32 per slice → /workspace/voice-work/clip-04-v18c/slice-stt.json; run with asr-venv)
       clip-04-mkspec-v18.py spec     (write final/spec.json)"""
import json, os, re, sys, wave, difflib, unicodedata
import numpy as np
REPO = "/workspace/oneup-studio"; D = f"{REPO}/content/clips/clip-04-gap-sach-tu-kiem/final/"
VD = f"{REPO}/video-engine/public/voice/"; WORK = "/workspace/voice-work/clip-04-v18c/"; P = "c04v18"
SR, FPS = 48000, 30; SPF = SR // FPS
HOLD_AFTER, HOLD_S, TAIL_S = "c16b", 1.0, 0.3
T = json.load(open(D + "voice-only-c04v18.timing.json")); M = json.load(open(D + "prosody-measure-v18.json"))
CH = {s["id"]: s for s in T["sentences"]}
TOK = {s["id"]: [k for p in s["pieces"] for k in p["tokens"]] for s in T["sentences"]}
PICK = json.load(open(WORK + "picks.json"))

# line id, chunk, split (token index the line starts at inside the chunk), display text (VI, **bold** = delivery stress), EN caption, hl, emotion, bubble
LINES = [
 ("c01a", "c01", 0, "Học thuộc tối qua,", "Memorized last night,", [0], "surprised", False),
 ("c01b", "c01", 4, "sáng dậy **quên sạch**?", "gone by morning?", [0], "surprised", False),
 ("c02", "c02", 0, "Giả sử bây giờ **không nhìn sách**, bạn còn nhớ được những gì?", "Book closed: what do you still remember?", [1], "confused", False),
 ("c03", "c03", 0, "Mình học **ba mươi từ** tiếng Anh, đọc đi đọc lại tới thuộc làu.", "I reread thirty English words until fluent", [2], "happy", True),
 ("c04", "c04", 0, "Sáng dậy mình gấp sách viết thử,", "Next morning, book closed, I wrote", [3], "focused", True),
 ("c05", "c05", 0, "tới từ thứ năm là hành lý thì mình **bí**.", "Stuck at word five", [0], "confused", True),
 ("c06", "c06", 0, "Một thí nghiệm năm 2006 thấy,", "A 2006 study found:", [1], "focused", False),
 ("c07", "c07", 0, "nếu **kiểm tra ngay** thì nhóm đọc lại làm tốt hơn.", "Tested at once, rereaders did better", [3], "neutral", False),
 ("c08", "c08", 0, "Nhưng **hai ngày sau**, nhóm tự kiểm tra lại nhớ hơn hẳn.", "Two days later, self-testing remembered more", [3], "surprised", False),
 ("c09", "c09", 0, "Mình cần là **sáng hôm sau**, gấp sách lại mình vẫn viết ra được.", "Goal: book closed next morning, still recall", [2], "focused", True),
 ("c10", "c10", 0, "Nên mình chia ba mươi từ thành **ba phần**, mỗi phần mười từ.", "Thirty words, three parts of ten", [2], "focused", True),
 ("c11", "c11", 0, "Học hết phần nào, mình **gấp sách** viết lại phần đó,", "Finish a part, close the book, write", [3], "focused", True),
 ("c12", "c12", 0, "chỗ nào bí mình mới **mở sách**.", "Stuck? Only then open the book", [3], "confused", True),
 ("c13", "c13", 0, "Nhóm của Yang tổng hợp 222 nghiên cứu,", "Yang 2021: 222 studies combined", [2], "focused", False),
 ("c14", "c14", 0, "thấy lớp có kiểm tra nhỏ thì điểm **cao hơn** lớp không làm kiểm tra nhỏ, ở mức vừa.", "Quizzed classes scored moderately higher", [4], "focused", False),
 ("c15", "c15", 0, "Sáng hôm sau, sách vẫn gấp,", "Next morning, book still closed", [4], "neutral", True),
 ("c16a", "c16", 0, "mình **tự viết được** luggage,", "I wrote luggage on my own", [2], "happy", True),
 ("c16b", "c16", 6, "đúng chữ hành lý hôm trước mình bí.", "The very word I got stuck on", [5], "happy", True),
 ("c17a", "c17a", 0, "Còn bạn, thử gấp sách lại thì viết được **mấy từ**?", "Your turn: book closed, how many words?", [5], "happy", True),
 ("c17b", "c17b", 0, "Comment **con số** nha.", "Comment your number below", [2], "happy", True),
]
NL = len(LINES)

def wav_read(p):
    with wave.open(p) as w: return np.frombuffer(w.readframes(w.getnframes()), np.int16).copy()
def wav_write(p, a):
    with wave.open(p, "wb") as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(a.astype(np.int16).tobytes())
def fr(t): return int(round(t * FPS))

def cuts():
    """frame index where each line starts (line 0 = 0) and the end frame of the last line."""
    a = wav_read(D + "voice-only-c04v18.wav").astype(np.float32)
    out = [0]
    for i in range(1, NL):
        lid, ch, sp = LINES[i][:3]; pch = LINES[i - 1][1]
        if ch == pch:  # split inside one chunk: lowest-energy frame boundary between the two words
            tk = TOK[ch]; t0, t1 = tk[sp - 1][1] + 0.1, tk[sp][1] + 0.15
            cand = range(fr(t0), fr(t1) + 1)
            e = lambda f: float(np.sqrt(np.mean(a[max(0, f * SPF - 480):f * SPF + 480] ** 2)))
            out.append(min(cand, key=e))
        else:
            out.append(fr((CH[pch]["end"] + CH[ch]["start"]) / 2))
    end = int(np.ceil(len(a) / SPF))
    return out, end, a

def env30(x):
    n = int(np.ceil(len(x) / SPF)); v = [float(np.sqrt(np.mean((x[i * SPF:(i + 1) * SPF] / 32768.0) ** 2))) if len(x[i * SPF:(i + 1) * SPF]) else 0 for i in range(n)]
    pk = max(v) or 1; return [round(min(1, z / pk), 3) for z in v]

def slices():
    st, end, a = cuts(); ai = a.astype(np.int16) if a.dtype != np.int16 else a
    a16 = wav_read(D + "voice-only-c04v18.wav"); a16 = np.concatenate([a16, np.zeros(end * SPF - len(a16), np.int16)])
    stt = json.load(open(WORK + "slice-stt.json")) if os.path.exists(WORK + "slice-stt.json") else {}
    track = []; info = {}
    for i, L in enumerate(LINES):
        lid, ch = L[0], L[1]; f0 = st[i]; f1 = st[i + 1] if i + 1 < NL else end
        x = a16[f0 * SPF:f1 * SPF]
        if lid == HOLD_AFTER: x = np.concatenate([x, np.zeros(int(HOLD_S * SR), np.int16)])
        if i == NL - 1: x = np.concatenate([x, np.zeros(int(TAIL_S * SR), np.int16)])
        assert len(x) % SPF == 0
        key = f"{P}-{lid}"; wav_write(VD + key + ".wav", x); track.append(x)
        sp = L[2]; toks = [k for k in TOK[ch] if k[3] >= (TOK[ch][sp][3] if sp else -1)]
        nxt = LINES[i + 1] if i + 1 < NL else None
        if nxt and nxt[1] == ch: toks = [k for k in toks if k[3] < TOK[ch][nxt[2]][3]]
        s0 = max(CH[ch]["start"] if not sp else toks[0][1], f0 / FPS); s1 = min(CH[ch]["end"] if not (nxt and nxt[1] == ch) else toks[-1][2], f1 / FPS)
        cap = [round(max(0.0, s0 - f0 / FPS - 0.05), 3), round(min(len(x) / SR, s1 - f0 / FPS + 0.3), 3)]
        sm = dict(stt.get(lid, {}))
        split = bool(L[2]) or bool(nxt and nxt[1] == ch)
        if split and sm:  # a split line is part of one F5 take: also score it in context (approved medium STT of the whole chunk, measure-v18), keep the better
            mw = next(x["stt"] for x in M["sentences"] if x["id"] == ch).split(); n0 = L[2]; n1 = nxt[2] if (nxt and nxt[1] == ch) else len(mw)
            ctx = " ".join(mw[n0:n1]); cs = round(difflib.SequenceMatcher(None, _norm(ctx), _norm(re.sub(r"\*\*", "", L[3])), autojunk=False).ratio(), 3)
            sm["fragment"] = {"text": sm.get("text"), "sim": sm.get("sim")}; sm["in_chunk"] = {"text": ctx, "sim": cs}
            if cs > sm.get("sim", 0): sm["text"], sm["sim"] = ctx, cs
        m = {"duration": round(len(x) / SR, 4), "envelope": env30(x),
             "engine": "F5-TTS hynt ViVoice thai-son speed 1.0, per-phrase F5 (voice-delivery-f5.py v18 chunk take, L-016 one F5 call per chunk; {nhấn:} +dB only), sliced sample-exact from approved final/voice-only-c04v18.wav at frame boundaries inside silences",
             "role": "Thầy", "stt": sm.get("text", ""), "stt_sim": sm.get("sim", 1.0), "stt_model": "faster-whisper medium float32" if sm else None, **({"stt_split": {k: sm[k] for k in ("fragment", "in_chunk")}} if "in_chunk" in sm else {}),
             "intra_output_cuts": 0 if L[2] == 0 and not (nxt and nxt[1] == ch) else 1, "emphasis_edits": True,
             "units": [{"text": CH[ch]["text"], "take": PICK[ch]["take"], "chunk": ch}], "source": {"wav": "final/voice-only-c04v18.wav", "start_s": round(f0 / FPS, 4), "end_s": round(f1 / FPS, 4), "hold_s": HOLD_S if lid == HOLD_AFTER else 0, "tail_s": TAIL_S if i == NL - 1 else 0}}
        json.dump(m, open(VD + key + ".json", "w"), ensure_ascii=False, indent=1)
        info[lid] = {"key": key, "dur": m["duration"], "cap": cap, "start_src": f0 / FPS, "tok": [[k[0], round(k[1] - f0 / FPS, 3), round(k[2] - f0 / FPS, 3)] for k in toks]}
    tr = np.concatenate(track); wav_write(D + "voice-track-c04v18.wav", tr)
    json.dump(info, open(WORK + "slices.json", "w"), ensure_ascii=False, indent=1)
    print(f"{NL} slices, track {len(tr) / SR:.3f}s ({len(tr) / SPF:.0f} frames)")
    for k, v in info.items(): print(k, v["dur"], v["cap"])

NUM = {"2006": "hai ngàn lẻ sáu", "222": "hai trăm hai mươi hai", "30": "ba mươi", "10": "mười", "5": "năm", "3": "ba"}
SAY = {"luggage": "lắc ghịt", "yang": "giang"}  # F5 input spelling of the approved takes (c16-71r respelled, c13 «Giang»)
def _norm(s):
    s = unicodedata.normalize("NFC", s.lower()); s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\d+", lambda m: NUM.get(m.group(0), m.group(0)), s)
    return " ".join(SAY.get(w, w) for w in s.split()).split()
def stt():
    from faster_whisper import WhisperModel
    md = WhisperModel("medium", device="cpu", compute_type="float32")
    out = {}
    for L in LINES:
        lid = L[0]; p = VD + f"{P}-{lid}.wav"
        import subprocess
        x = wav_read(p).astype(np.float32) / 32768.0  # same path as voice-delivery-f5.py: 16 kHz float + 0.5s pad, no VAD
        a = np.frombuffer(subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-ar", "16000", "-f", "f32le", "-"], input=x.tobytes(), capture_output=True).stdout, dtype="float32")
        seg, _ = md.transcribe(np.pad(a, 8000), language="vi", beam_size=5, condition_on_previous_text=False)
        tx = " ".join(s.text.strip() for s in seg).strip()
        ref = re.sub(r"\*\*", "", L[3])
        sm = round(difflib.SequenceMatcher(None, _norm(tx), _norm(ref), autojunk=False).ratio(), 3)
        out[lid] = {"text": tx, "sim": sm, "ref": ref}; print(lid, sm, tx, flush=True)
    json.dump(out, open(WORK + "slice-stt.json", "w"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "slices": slices()
    elif cmd == "stt": stt()
    elif cmd == "spec":
        sys.path.insert(0, os.path.dirname(__file__)); import importlib; importlib.import_module("clip-04-spec-v18-scenes").write()
