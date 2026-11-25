#!/usr/bin/env python3
"""STT check for voice lines (rule-34 premium bar). Usage: stt_check.py a.wav [b.wav ...]
Prints file | transcript. Needs faster-whisper (local: ~/oneup-tools/f5-venv)."""
import os, sys, subprocess
from pathlib import Path
import numpy as np
from faster_whisper import WhisperModel

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import paths as P

# ASR_MODEL / ASR_COMPUTE env (L-079/L-081: default float32; int8 hallucinates on ctranslate2)
m = WhisperModel(
    os.environ.get("ASR_MODEL", "small"),
    device=os.environ.get("ASR_DEVICE", "cpu"),
    compute_type=os.environ.get("ASR_COMPUTE", "float32"),
)
for f in sys.argv[1:]:
    pcm = subprocess.run([P.FFMPEG_BIN, "-loglevel", "error", "-i", f, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(pcm, dtype=np.int16).astype("float32") / 32768
    if len(a) < 16000 * 1.0:
        a = np.pad(a, 9600)  # whisper returns "" on very short clips (b01c 0.89s) → pad 0.6s silence; not ≥1.0s
    segs, _ = m.transcribe(a, language="vi")
    print(f.split("/")[-1], "|", " ".join(s.text.strip() for s in segs), flush=True)
