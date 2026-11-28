---
title: "Voice Phase-1 benchmark: F5 vs VieNeu on clip-08"
date: 2026-11-28
id: run.voice-phase1-benchmark-2026-11-28
type: note
tags: [voice, benchmark, vieneu, f5-tts, clip-08]
status: ready
source: "pipeline/scripts/voice-vieneu.py + video-engine/public/voice/c08v1-*"
updated: 2026-11-28
---
# Voice Phase-1 A/B — clip-08-dien-thoai-up-ban (2026-11-28)

Máy: Mac local (Apple Silicon). VieNeu venv: `$ONEUP_TOOLS_DIR/vieneu-venv` (package `vieneu` 3.8.5, ONNX). Nghe thử (không commit media): `media/samples/clip-08-vieneu-ab/`.

## Bảng đối chứng

| Engine | Gen wall (s) | Audio (s) | RTF | Median F0 (Hz) | F0 outliers (>2.5 st) | Syl/s | Mean STT sim | EN words |
|---|---:|---:|---:|---:|---|---:|---:|---|
| **F5-TTS** (`c08v1`, thai-son-v2) | (không đo lại lần này; pipeline phrase+pick đa batch) | 53.74 | — | 127.3 | 3 (`b01mid` 2.94, `b02b` 3.19, `b07a` 4.13) | 3.83 | 0.919 | `say` bồi «Oát» cho Ward |
| **VieNeu fp32** (`c08vn1`, 4 khối) | 298.72 | 53.36 | 5.598 | 124.0 | 1 (`b03` 2.77) | 3.82 | 0.865 | giữ `text` gốc (Ward/email/team/comment) |
| **VieNeu int8** (`c08vn1i8`, 4 khối) | 344.41 | 53.84 | 6.397 | 127.3 | 1 (`b02b` 4.88) | 3.79 | (xem report) | giữ `text` gốc |

Ghi chú:
- RTF VieNeu gồm auto-reroll tối đa 2 lần/khối khi L-114/STT lệch; fp32 trên máy này nhanh hơn int8.
- Smoke 1 câu VieNeu fp32 preset Thái Sơn: **10.88 s** wall (`media/samples/clip-08-vieneu-ab/_smoke.wav`).
- F5 vẫn có STT sim cao hơn trên clip này; VieNeu thắng giấy phép (Apache-2.0), code-switch EN–VI, và số outlier F0 clip-wide ít hơn sau reroll.

## Lệnh nghe thử

```bash
cd "$(git rev-parse --show-toplevel)"
# F5 (đã có sẵn Remotion prefix)
afplay video-engine/public/voice/c08v1-b01.wav
# VieNeu listen (gitignored media/)
afplay media/samples/clip-08-vieneu-ab/listen-fp32.wav
afplay media/samples/clip-08-vieneu-ab/listen-int8.wav
# Re-gen
export VIENEU_PYTHON="${ONEUP_TOOLS_DIR:-$HOME/oneup-tools}/vieneu-venv/bin/python"
python3 pipeline/scripts/voice-vieneu.py \
  --spec content/clips/clip-08-dien-thoai-up-ban/final/spec.json \
  --prefix c08vn1 --precision fp32
python3 pipeline/scripts/voice-vieneu.py check-refs
```

## Kết luận Phase-1

1. `audio_utils` + `voice-direct` + `voice-vieneu` + `vieneu_gen` sẵn sàng offline (tests xanh).
2. Trên clip-08, **fp32 ONNX** là mặc định hợp lý hơn int8 trên Mac này.
3. Pha 3: thu 4 ref `hiep-*` đồng tông thật (≤1.0 st) + LoRA backbone để kéo STT/F0 sát F5 mà giữ cảm xúc khối.
