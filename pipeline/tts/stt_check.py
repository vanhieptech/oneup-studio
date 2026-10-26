#!/usr/bin/env python3
"""STT check for voice lines (rule-34 premium bar). Usage: stt_check.py a.wav [b.wav ...]
Prints file | transcript. Needs faster-whisper (box: /workspace/asr-venv)."""
import os, sys, subprocess, numpy as np
from faster_whisper import WhisperModel
# ASR_MODEL / ASR_COMPUTE env (L-081: final STT gate uses medium float32; small kept as the default for old callers)
m = WhisperModel(os.environ.get("ASR_MODEL", "small"), device="cpu", compute_type=os.environ.get("ASR_COMPUTE", "int8" if os.environ.get("ASR_MODEL", "small") == "small" else "float32"))
for f in sys.argv[1:]:
    pcm = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", f, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(pcm, dtype=np.int16).astype("float32") / 32768
    if len(a) < 16000 * 1.0: a = np.pad(a, 9600)  # whisper returns "" on very short clips (b01c 0.89s) → pad 0.6s silence; not ≥1.0s (RR 3d8f43d: padding a 1.37s c18 gave «Cô mang»)
    segs, _ = m.transcribe(a, language="vi")
    print(f.split("/")[-1], "|", " ".join(s.text.strip() for s in segs), flush=True)
