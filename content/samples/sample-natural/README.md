---
id: sample-natural
type: sample
updated: 2026-10-13
tags: [voice, prosody, hyperframes, DL-033]
---
# sample-natural (DL-033): natural-prosody voice + lint-clean HyperFrames explainer
Comic b01 + b03 (Remotion) → e01 explainer (HyperFrames, sub-compositions). ~20 s, 1080×1920, 30 fps, no music, −14 LUFS.
Week ≥5 sample only (Omi present, rule-11).

- Source: `spec.json` (lines carry `phrases` → `pipeline/scripts/voice-prosody.py`).
- Build: `python3 pipeline/scripts/build-final.py content/samples/sample-natural/spec.json` (Node 22 on PATH; output `out/sample-natural.mp4`, gitignored).
- Voice A/B metrics: `voice-ab-metrics.md`. HyperFrames lint/check: `hf-check.txt`. Frames: `contact-sheet.png`.
- Explainer = reference for new explainers (see skills/make-video §2).
