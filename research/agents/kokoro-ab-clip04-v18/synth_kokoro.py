#!/usr/bin/env python3
"""Synth c07/c08/c14 bằng Kokoro-Vietnamese ONNX (CPU), mỗi chunk 1 lần gọi, speed 1.0, rồi chuẩn -14 LUFS (peak <= -0.5 dBFS).
Chạy: /workspace/kokoro-vn/venv/bin/python synth_kokoro.py [--voices a,b] [--force]
CHẶN nếu F5 đang chạy (L-041 / yêu cầu của News: không load hai model cùng lúc)."""
import json, os, subprocess, sys, time
import numpy as np, soundfile as sf, pyloudnorm as pyln
HERE = os.path.dirname(os.path.abspath(__file__)); HF = "/workspace/kokoro-vn/hf"; SR = 24000
def f5_running():
    out = subprocess.run(["ps", "-eo", "pid,args"], capture_output=True, text=True).stdout
    return [l for l in out.splitlines() if ("f5tts" in l.lower() or "f5-venv" in l or "f5_tts" in l) and "synth_kokoro" not in l]
args = sys.argv[1:]
if "--force" not in args and (r := f5_running()):
    sys.exit("F5 đang chạy, KHÔNG load Kokoro:\n" + "\n".join(r))
cfg = json.load(open(os.path.join(HERE, "lines.json")))
voices = (args[args.index("--voices") + 1].split(",") if "--voices" in args else cfg["voicepacks_preregistered"])
import onnxruntime as ort, torch
sys.path.insert(0, "/workspace/kokoro-vn/src/src")
from kokoro_vietnamese.core import phonemize, split_text
from kokoro_vietnamese.onnx_utils import load_config, phonemes_to_input_ids, select_voice_style, speed_input
conf = load_config(f"{HF}/config.json"); ctx = conf["plbert"]["max_position_embeddings"]
so = ort.SessionOptions(); so.intra_op_num_threads = os.cpu_count(); so.inter_op_num_threads = 1
t0 = time.time(); sess = ort.InferenceSession(f"{HF}/kokoro_vi.onnx", so, providers=["CPUExecutionProvider"]); load_s = time.time() - t0
meter = pyln.Meter(SR); log = {"model": "contextboxai/Kokoro-Vietnamese@9f210d6 kokoro_vi.onnx", "load_s": round(load_s, 2), "threads": os.cpu_count(), "runs": []}
for v in voices:
    vp = torch.load(f"{HF}/voicepacks/{v}.pt", map_location="cpu", weights_only=True)
    for L in cfg["lines"]:
        chunks = split_text(L["text"]); assert len(chunks) == 1, (L["id"], chunks)  # 1 chunk = 1 lần gọi, không ghép
        ps = phonemize(chunks[0]); ids = phonemes_to_input_ids(ps, conf["vocab"], context_length=ctx)
        t = time.time(); wav, _ = sess.run(None, {"input_ids": ids, "ref_s": select_voice_style(vp, len(ps)), "speed": speed_input(1.0)}); dt = time.time() - t
        x = np.asarray(wav, np.float32).reshape(-1); dur = len(x) / SR
        lufs_raw = meter.integrated_loudness(x); y = pyln.normalize.loudness(x, lufs_raw, -14.0)
        pk = float(np.max(np.abs(y))); lim = 10 ** (-0.5 / 20)
        if pk > lim: y = y * (lim / pk)  # chỉ hạ gain toàn file, không nén
        out = os.path.join(HERE, "kokoro", f"{L['id']}-kokoro-{v}.wav"); sf.write(out, y, SR, subtype="PCM_16")
        r = {"id": L["id"], "voice": v, "phonemes": ps, "synth_s": round(dt, 3), "audio_s": round(dur, 3), "rtf": round(dt / dur, 4),
             "lufs_raw": round(lufs_raw, 2), "lufs_out": round(meter.integrated_loudness(y), 2), "peak_dbfs": round(20 * np.log10(np.max(np.abs(y))), 2), "out": out}
        log["runs"].append(r); print(json.dumps(r, ensure_ascii=False))
json.dump(log, open(os.path.join(HERE, "kokoro", "synth-log.json"), "w"), ensure_ascii=False, indent=1)
