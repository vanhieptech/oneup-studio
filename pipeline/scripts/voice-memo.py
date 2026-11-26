#!/usr/bin/env python3
"""Transcribe Hiệp's voice memos (faster-whisper, local) for the voice profile and "talk first" drafting.

  voice-memo.py MEMO.m4a [more files or a folder] [--model medium] [--samples 15]
  voice-memo.py keep MEMO.txt DRAFT.md [--min 0.8]   # Voice-First Input: share of the draft's content words found in the memo

- Runs pipeline/tts-style faster-whisper inside ASR_PYTHON (pipeline/paths.py; ~/oneup-tools/f5-venv), language vi.
- Writes media/voice-memos/<name>.txt (media/ is gitignored; the memo itself stays outside git).
- Prints 10–20 sample sentences (complete thought, 6–25 words) to paste into content/voice-profile.md §4 «Mẫu thật».
- "Talk first" (make-video §2.0 step 3): the .txt becomes the raw material the script is edited from.
- keep (resources/vn-spoken/voice-first.md): ≥ 80% of the draft's content words should be Hiệp's own words from the memo;
  fillers/particles and numbers are ignored, `{nguồn: …}` spans (citations) are left out of the count. Exit 1 below --min.
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

FILLERS = set("à á ạ ả ã ừ ừm ờ ơ ồ ủa nha nhé nhen nghen hen hén nè đó đấy thôi luôn hông khum ha hả á vậy dậy thì là mà và với cái con của".split())

def _content_words(text):
    import unicodedata
    t = re.sub(r"\{nguồn:[^}]*\}", " ", unicodedata.normalize("NFC", text).lower())
    t = re.sub(r"\{[^}:]*:\s*([^}]*)\}", r"\1", t)
    return [w for w in re.findall(r"[a-zà-ỹđ]+", t) if w not in FILLERS and len(w) > 1]

def draft_text(md):
    """Spoken words of a draft: `N. **[bNN]** lời` lines when present, else the whole body without front-matter."""
    lines = re.findall(r"^\s*\d+\.\s*\*\*\[[^\]]*\]\*\*\s*(.+)$", md, re.M)
    if lines: return "\n".join(lines)
    return md.split("\n---", 1)[1] if md.startswith("---") and "\n---" in md else md

def keep_ratio(memo, draft):
    """(ratio, kept, total, missing[:20]): draft content words (tokens) that also occur in the memo's vocabulary."""
    vocab = set(_content_words(memo)); words = _content_words(draft_text(draft))
    if not words: return 0.0, 0, 0, []
    kept = [w for w in words if w in vocab]
    missing = sorted({w for w in words if w not in vocab})
    return round(len(kept) / len(words), 3), len(kept), len(words), missing[:20]

def keep_main(a):
    mn = float(a[a.index("--min") + 1]) if "--min" in a else 0.8
    memo, draft = Path(a[0]).read_text(encoding="utf-8"), Path(a[1]).read_text(encoding="utf-8")
    r, k, n, miss = keep_ratio(memo, draft)
    print(f"Voice-First: {k}/{n} từ có nghĩa của nháp nằm trong ghi âm = {r:.0%} (mục tiêu ≥ {mn:.0%})")
    if miss: print("  từ mới (không có trong ghi âm): " + ", ".join(miss))
    return 0 if r >= mn else 1

def main():
    a = sys.argv[1:]
    if a and a[0] == "keep":
        if len(a) < 3: print(__doc__); return 2
        return keep_main(a[1:])
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
