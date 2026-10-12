#!/usr/bin/env python3
"""STT check for voice lines (rule-34 premium bar). Usage: stt_check.py a.wav [b.wav ...]
Prints file | transcript. Needs faster-whisper (box: /workspace/asr-venv)."""
import sys, subprocess, numpy as np
from faster_whisper import WhisperModel
m = WhisperModel("small", device="cpu", compute_type="int8")
for f in sys.argv[1:]:
    pcm = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", f, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(pcm, dtype=np.int16).astype("float32") / 32768
    segs, _ = m.transcribe(a, language="vi")
    print(f.split("/")[-1], "|", " ".join(s.text.strip() for s in segs), flush=True)
