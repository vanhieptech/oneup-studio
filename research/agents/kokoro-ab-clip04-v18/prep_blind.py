#!/usr/bin/env python3
"""Ghép mù A/B: F5 v18 (take News đã chọn) vs Kokoro (voicepack đã chọn). Chuẩn -14 LUFS cả hai, resample 48k, đặt tên ngẫu nhiên.
Chạy: /workspace/kokoro-vn/venv/bin/python prep_blind.py --voice manh_dung --f5 c07=/path.wav,c08=/path.wav,c14=/path.wav
Đáp án ghi riêng ở blind-key.json (không mở trước khi nghe xong)."""
import json, os, random, subprocess, sys
import numpy as np, soundfile as sf, pyloudnorm as pyln
HERE = os.path.dirname(os.path.abspath(__file__)); a = sys.argv[1:]; V = a[a.index("--voice") + 1]
F5 = dict(kv.split("=", 1) for kv in a[a.index("--f5") + 1].split(","))
def load48(p): return np.frombuffer(subprocess.run(["ffmpeg", "-loglevel", "error", "-i", p, "-ac", "1", "-ar", "48000", "-f", "f32le", "-"], capture_output=True, check=True).stdout, np.float32).copy()
m = pyln.Meter(48000); key = {"kokoro_voice": V, "pairs": {}}; rng = random.SystemRandom()
for cid, f5p in F5.items():
    src = {"f5": f5p, "kokoro": os.path.join(HERE, "kokoro", f"{cid}-kokoro-{V}.wav")}; lab = ["X", "Y"]; rng.shuffle(lab)
    for eng, l in zip(("f5", "kokoro"), lab):
        x = load48(src[eng]); y = pyln.normalize.loudness(x, m.integrated_loudness(x), -14.0); pk = np.max(np.abs(y)); lim = 10 ** (-0.5 / 20)
        if pk > lim: y = y * (lim / pk)
        out = os.path.join(HERE, "blind", f"{cid}-{l}.wav"); sf.write(out, y, 48000, subtype="PCM_16")
        key["pairs"].setdefault(cid, {})[l] = {"engine": eng, "src": src[eng], "lufs": round(m.integrated_loudness(y), 2)}
json.dump(key, open(os.path.join(HERE, "blind-key.json"), "w"), ensure_ascii=False, indent=1); print("ok -> blind/, key -> blind-key.json")
