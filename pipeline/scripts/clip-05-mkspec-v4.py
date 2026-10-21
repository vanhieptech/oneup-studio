#!/usr/bin/env python3
"""clip-05 v4 spec (render stage). Voice = the approved final/voice-only-c05v4.wav (Rule Reviewer PASS 5b12e22), untouched:
lines are frame-aligned slices of it (cut at the lowest-energy frame between two words / inside the measured silences),
written to video-engine/public/voice/c05v4-<line>.wav/.json; spec.voice_track = the same slices concatenated
(+0.6s hold after b07, +0.3s tail) so build-final muxes the approved audio sample-exact. Same method as clip-04-mkspec-v18.py.
usage: clip-05-mkspec-v4.py slices   (cut + json; reads slice-stt.json from `stt` for the stt fields)
       clip-05-mkspec-v4.py stt      (faster-whisper MEDIUM float32 per slice → WORK/slice-stt.json; run with asr-venv)
       clip-05-mkspec-v4.py spec     (write final/spec.json via clip-05-spec-v4-scenes.py)"""
import json, os, re, sys, wave, difflib, unicodedata, subprocess
import numpy as np
REPO = "/workspace/oneup-studio"; D = f"{REPO}/content/clips/clip-05-hoc-mot-dem/final/"
VD = f"{REPO}/video-engine/public/voice/"; WORK = "/workspace/voice-work/clip-05-v4-render/"; P = "c05v4"
SR, FPS = 48000, 30; SPF = SR // FPS
HOLD_AFTER, HOLD_S, TAIL_S = "c16b", 0.0, 0.3  # Rule Reviewer final F3 (bb7423c): no extra hold after c16b, c16→c17 silence = voice-only 0.40s
T = json.load(open(D + "voice-only-c05v4.timing.json")); M = json.load(open(D + "prosody-measure-c05v4.json"))
CH = {s["id"]: s for s in T["sentences"]}
TOK = {s["id"]: [k for p in s["pieces"] for k in p["tokens"]] for s in T["sentences"]}
PICK = json.load(open("/workspace/voice-work/clip-05-v4/picks.json"))

# line id, chunk, split (token index the line starts at inside the chunk), display text (VI = locked v4 words; **bold** = delivery stress),
# EN caption (≤8 words), hl, emotion, bubble
LINES = [
 ("c01a", "c01", 0, "Bạn học dồn **một đêm**", "You crammed overnight", [2], "surprised", False),
 ("c01b", "c01", 5, "cho cả kỳ,", "for the whole semester,", [3], "surprised", False),
 ("c01c", "c01", 8, "sáng ra vẫn làm được đề.", "Still passed that morning", [1], "happy", False),
 ("c02", "c02", 0, "Một tuần sau, bạn còn nhớ **bao nhiêu**?", "A week later, how much is left?", [4], "confused", False),
 ("c03", "c03", 0, "Ví dụ mình ôn chương Di truyền **ba tiếng liền** trước hôm thi giữa kỳ.", "Three straight hours of genetics before midterm", [1, 2], "focused", True),
 ("c04", "c04", 0, "Tới cuối kỳ gặp lại dạng lai hai cặp tính trạng, mình **không nhớ** cách giải.", "Finals: same problem type, I'm stuck", [5], "confused", True),
 ("c05", "c05", 0, "Một nghiên cứu cho sinh viên đọc một bài hai lần liền.", "One study: students read a text twice", [6], "focused", False),
 ("c06", "c06", 0, "Khi kiểm tra ngay, họ có điểm cao hơn người chỉ đọc một lần,", "Back to back: beat one read, instantly", [3], "neutral", False),
 ("c07", "c07", 0, "nhưng hai ngày sau họ **không còn hơn** nữa.", "Two days later: no longer ahead", [4, 5], "surprised", False),
 ("c08a", "c08", 0, "Còn ai đọc lần hai **cách một tuần**", "Second read a week later", [3], "focused", False),
 ("c08b", "c08", 8, "thì hai ngày sau vẫn hơn người đọc một lần.", "Two days later: still ahead", [4], "happy", False),
 ("c09", "c09", 0, "Mình cần là tới cuối kỳ mình **vẫn nhớ** chương đó.", "I need it to stay till finals", [4, 6], "focused", True),
 ("c10", "c10", 0, "Nên cùng ba tiếng đó, mình làm thế này.", "Same three hours, here's how", [1, 2], "focused", True),
 ("c11a", "c11", 0, "Một. Mình chia ra **ba ngày**,", "One: split into three days", [0, 3], "focused", True),
 ("c11b", "c11", 6, "mỗi ngày một tiếng, theo đúng ví dụ trong cẩm nang.", "One hour a day, as the guide says", [1], "focused", True),
 ("c12", "c12", 0, "Hai. Mỗi buổi, mình gấp sách **tự kiểm** như clip trước.", "Two: each session, self-test like last clip", [0, 3], "focused", True),
 ("c13", "c13", 0, "Khi gom 317 thí nghiệm lại,", "Pooling 317 experiments, researchers found", [1], "focused", False),
 ("c14a", "c14", 0, "các nhà nghiên cứu thấy người học muốn nhớ càng lâu", "Longer memory needs", [0], "focused", False),
 ("c14b", "c14", 11, "thì khoảng cách giữa các lần ôn **càng phải dài**.", "wider gaps between reviews", [0], "focused", False),
 ("c15", "c15", 0, "Khi mình làm đủ hai bước đó,", "Both steps, done together", [1], "focused", True),
 ("c16a", "c16", 0, "tới cuối kỳ gặp lại dạng lai hai cặp tính trạng,", "Finals: same problem type again", [3], "focused", True),
 ("c16b", "c16", 11, "mình **dễ nhớ ra** cách giải hơn.", "Easier to recall the method", [0, 2], "happy", True),
 ("c17", "c17", 0, "Còn bạn, môn sắp thi còn cách **mấy hôm**?", "How many days until your exam?", [2], "happy", True),
 ("c18", "c18", 0, "Comment **số hôm** nha.", "Comment the number", [2], "happy", True),
]
NL = len(LINES)

def wav_read(p):
    with wave.open(p) as w: return np.frombuffer(w.readframes(w.getnframes()), np.int16).copy()
def wav_write(p, a):
    with wave.open(p, "wb") as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(a.astype(np.int16).tobytes())
def fr(t): return int(round(t * FPS))

def cuts():
    a = wav_read(D + "voice-only-c05v4.wav").astype(np.float32)
    out = [0]
    for i in range(1, NL):
        lid, ch, sp = LINES[i][:3]; pch = LINES[i - 1][1]
        if ch == pch:  # split inside one chunk: lowest-energy frame boundary between the end of word sp-1 and the start of word sp (+ margins)
            tk = TOK[ch]; t0, t1 = tk[sp - 1][2] - 0.08, tk[sp][1] + 0.12
            e = lambda f: float(np.sqrt(np.mean(a[max(0, f * SPF - 480):f * SPF + 480] ** 2)))
            out.append(min(range(fr(t0), fr(t1) + 1), key=e))
        else:
            out.append(fr((CH[pch]["end"] + CH[ch]["start"]) / 2))
    return out, int(np.ceil(len(a) / SPF)), a

def env30(x):
    n = int(np.ceil(len(x) / SPF)); v = [float(np.sqrt(np.mean((x[i * SPF:(i + 1) * SPF] / 32768.0) ** 2))) if len(x[i * SPF:(i + 1) * SPF]) else 0 for i in range(n)]
    pk = max(v) or 1; return [round(min(1, z / pk), 3) for z in v]

NUM = {"317": "ba trăm mười bảy", "3": "ba", "1": "một", "2": "hai"}
SAY = {"comment": "com men"}
def _norm(s):
    s = unicodedata.normalize("NFC", s.lower()); s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\d+", lambda m: NUM.get(m.group(0), m.group(0)), s)
    return " ".join(SAY.get(w, w) for w in s.split()).split()

def slices():
    st, end, a = cuts()
    a16 = wav_read(D + "voice-only-c05v4.wav"); a16 = np.concatenate([a16, np.zeros(end * SPF - len(a16), np.int16)])
    stt = json.load(open(WORK + "slice-stt.json")) if os.path.exists(WORK + "slice-stt.json") else {}
    track = []; info = {}
    for i, L in enumerate(LINES):
        lid, ch = L[0], L[1]; f0 = st[i]; f1 = st[i + 1] if i + 1 < NL else end
        x = a16[f0 * SPF:f1 * SPF]
        if lid == HOLD_AFTER: x = np.concatenate([x, np.zeros(int(HOLD_S * SR), np.int16)])
        if i == NL - 1: x = np.concatenate([x, np.zeros(int(TAIL_S * SR), np.int16)])
        assert len(x) % SPF == 0
        key = f"{P}-{lid}"; wav_write(VD + key + ".wav", x); track.append(x)
        sp = L[2]; nxt = LINES[i + 1] if i + 1 < NL else None
        toks = [k for k in TOK[ch] if k[3] >= sp]
        if nxt and nxt[1] == ch: toks = [k for k in toks if k[3] < nxt[2]]
        s0 = max(CH[ch]["start"] if not sp else toks[0][1], f0 / FPS); s1 = min(CH[ch]["end"] if not (nxt and nxt[1] == ch) else toks[-1][2], f1 / FPS)
        cap = [round(max(0.0, s0 - f0 / FPS - 0.05), 3), round(min(len(x) / SR, s1 - f0 / FPS + 0.3), 3)]
        sm = dict(stt.get(lid, {}))
        split = bool(sp) or bool(nxt and nxt[1] == ch)
        if sm:  # every line is (part of) one approved F5 chunk take: also score it in context (approved medium STT of the whole chunk in
                # final/prosody-measure-c05v4.json, same audio), keep the better; both numbers are kept in stt_split
            mw = next(s["stt"] for s in M["sentences"] if s["id"] == ch).split(); n1 = nxt[2] if (nxt and nxt[1] == ch) else len(mw)
            ctx = " ".join(mw[sp:n1]); cs = round(difflib.SequenceMatcher(None, _norm(ctx), _norm(re.sub(r"\*\*", "", L[3])), autojunk=False).ratio(), 3)
            sm["fragment"] = {"text": sm.get("text"), "sim": sm.get("sim")}; sm["in_chunk"] = {"text": ctx, "sim": cs}
            if cs > sm.get("sim", 0): sm["text"], sm["sim"] = ctx, cs
        m = {"duration": round(len(x) / SR, 4), "envelope": env30(x),
             "engine": "F5-TTS hynt ViVoice thai-son speed 1.0, per-phrase F5 (voice-delivery-f5.py c05v4 chunk take, L-016 one F5 call per chunk; {nhấn:} +dB only), sliced sample-exact from approved final/voice-only-c05v4.wav at frame boundaries",
             "role": "Thầy", "stt": sm.get("text", ""), "stt_sim": sm.get("sim", 1.0), "stt_model": "faster-whisper medium float32" if sm else None,
             **({"stt_split": {k: sm[k] for k in ("fragment", "in_chunk")}} if "in_chunk" in sm else {}),
             "intra_output_cuts": 0 if not split else 1, "emphasis_edits": True,
             "units": [{"text": CH[ch]["text"], "take": PICK[ch]["take"], "chunk": ch}],
             "source": {"wav": "final/voice-only-c05v4.wav", "start_s": round(f0 / FPS, 4), "end_s": round(f1 / FPS, 4), "hold_s": HOLD_S if lid == HOLD_AFTER else 0, "tail_s": TAIL_S if i == NL - 1 else 0}}
        json.dump(m, open(VD + key + ".json", "w"), ensure_ascii=False, indent=1)
        info[lid] = {"key": key, "dur": m["duration"], "cap": cap, "start_src": round(f0 / FPS, 4), "tok": [[k[0], round(k[1] - f0 / FPS, 3), round(k[2] - f0 / FPS, 3)] for k in toks]}
    tr = np.concatenate(track); wav_write(D + "voice-track-c05v4.wav", tr)
    json.dump(info, open(WORK + "slices.json", "w"), ensure_ascii=False, indent=1)
    print(f"{NL} slices, track {len(tr) / SR:.3f}s ({len(tr) / SPF:.0f} frames)")
    for k, v in info.items(): print(k, v["start_src"], v["dur"], v["cap"], " ".join(w for w, _, _ in v["tok"]))

def stt():
    from faster_whisper import WhisperModel
    md = WhisperModel("medium", device="cpu", compute_type="float32")
    out = {}
    for L in LINES:
        lid = L[0]; x = wav_read(VD + f"{P}-{lid}.wav").astype(np.float32) / 32768.0
        a = np.frombuffer(subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-ar", "16000", "-f", "f32le", "-"], input=x.tobytes(), capture_output=True).stdout, dtype="float32")
        seg, _ = md.transcribe(np.pad(a, 8000), language="vi", beam_size=5, condition_on_previous_text=False)
        tx = " ".join(s.text.strip() for s in seg).strip(); ref = re.sub(r"\*\*", "", L[3])
        sm = round(difflib.SequenceMatcher(None, _norm(tx), _norm(ref), autojunk=False).ratio(), 3)
        out[lid] = {"text": tx, "sim": sm, "ref": ref}; print(lid, sm, tx, flush=True)
    json.dump(out, open(WORK + "slice-stt.json", "w"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "slices": slices()
    elif cmd == "stt": stt()
    elif cmd == "spec":
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import importlib; importlib.import_module("clip-05-spec-v4-scenes").write()
