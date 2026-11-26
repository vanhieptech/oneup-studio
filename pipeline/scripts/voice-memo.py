#!/usr/bin/env python3
"""Transcribe Hiệp's voice memos (faster-whisper, local) for the voice profile and "talk first" drafting.

  voice-memo.py MEMO.m4a [more files or a folder] [--model medium] [--samples 15]

- Runs pipeline/tts-style faster-whisper inside ASR_PYTHON (pipeline/paths.py; ~/oneup-tools/f5-venv), language vi.
- Writes media/voice-memos/<name>.txt (media/ is gitignored; the memo itself stays outside git).
- Prints 10–20 sample sentences (complete thought, 6–25 words) to paste into content/voice-profile.md §4 «Mẫu thật».
- "Talk first" (make-video §2.0 step 3): the .txt becomes the raw material the script is edited from.
"""
import json, os, re, subprocess, sys
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65

AUDIO = {".m4a", ".mp3", ".wav", ".aac", ".mp4", ".mov", ".ogg", ".flac", ".caf"}
OUT_DIR = P.ROOT / "media/voice-memos"

ASR_CODE = r'''
import json, subprocess, sys
import numpy as np
from faster_whisper import WhisperModel
ffmpeg, model, files = sys.argv[1], sys.argv[2], sys.argv[3:]
m = WhisperModel(model, device="cpu", compute_type="float32")
out = {}
for f in files:
    pcm = subprocess.run([ffmpeg, "-loglevel", "error", "-i", f, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(pcm, dtype=np.int16).astype("float32") / 32768
    segs, _ = m.transcribe(a, language="vi", vad_filter=True)
    out[f] = [s.text.strip() for s in segs]
print(json.dumps(out, ensure_ascii=False))
'''

def collect(args):
    files = []
    for a in args:
        p = Path(a)
        if p.is_dir(): files += sorted(x for x in p.iterdir() if x.suffix.lower() in AUDIO)
        elif p.suffix.lower() in AUDIO: files.append(p)
    return files

def transcribe(files, model):
    r = subprocess.run([P.ASR_PYTHON, "-c", ASR_CODE, P.FFMPEG_BIN, model, *map(str, files)], capture_output=True, text=True, timeout=3600)
    if r.returncode: raise SystemExit(f"ASR failed: {r.stderr.strip()[-400:]}")
    return json.loads(r.stdout.strip().splitlines()[-1])

def sentences(segments):
    text = " ".join(segments)
    parts = re.split(r"(?<=[.!?…])\s+", text)
    return [p.strip() for p in parts if p.strip()]

def pick_samples(segments, n=15):
    """Complete-thought sentences of 6–25 words, longest-varied first, no duplicates."""
    seen, out = set(), []
    for s in sentences(segments):
        w = len(s.split())
        key = s.lower()
        if 6 <= w <= 25 and key not in seen:
            seen.add(key); out.append(s)
    return out[:n]

def main():
    a = sys.argv[1:]
    def opt(n, d=None):
        if n in a:
            i = a.index(n); v = a[i + 1]; del a[i:i + 2]; return v
        return d
    model, n = opt("--model", "medium"), int(opt("--samples", "15"))
    files = collect(a)
    if not files: print(__doc__); return 2
    res = transcribe(files, model)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    allsegs = []
    for f in files:
        segs = res.get(str(f), [])
        allsegs += segs
        (OUT_DIR / f"{f.stem}.txt").write_text("\n".join(segs) + "\n", encoding="utf-8")
        print(f"{f.name}: {len(segs)} đoạn → {OUT_DIR / (f.stem + '.txt')}")
    print("\n# Câu mẫu cho content/voice-profile.md §4 (Hiệp xem lại trước khi dán):")
    for s in pick_samples(allsegs, n): print(f"- «{s}»")
    return 0

if __name__ == "__main__":
    sys.exit(main())
