---
title: "sample-f5 (DL-035): same as sample-natural, voices = F5-TTS"
date: 2026-10-13
status: ready
source: "oneup-studio (soạn trong repo)"
id: sample-f5
type: sample
updated: 2026-10-13
tags: [voice, f5-tts, prosody, DL-035]
---
# sample-f5 (DL-035): same as sample-natural, voices = F5-TTS
Hiệp "F5 · Thái Sơn", Omi "F5 · Mỹ Duyên" (synthetic VieNeu refs, `assets/voice-refs/`). 17.1 s, 1080×1920, 30 fps, −14.0 LUFS, peak −1.4 dBFS. Week ≥5 sample only.
- Build: `F5_NFE=24 python3 pipeline/scripts/build-final.py content/samples/sample-f5/spec.json` (first run ≈46 min on 8-core CPU, then cached).
- F5 line mode: each take = whole line, cut into `phrases` at word timestamps, then gaps/emphasis; 3 takes, STT pick, leakage trim (0 trims needed here).
- Line STT (toneless): L1 Hiệp 0.70 ("tô ích" heard as "tổ ích"; whisper weakness, words otherwise right), L2 Omi 0.92, L3 Omi 0.93, L4 Hiệp 0.92. Omi drops the particle "á" in L2.
- ⚠ Checkpoint CC-BY-NC-SA-4.0 (non-commercial), risk accepted by Hiệp (DL-035). Caption disclosure: "… giọng AI tổng hợp (F5-TTS)."

## v2 (DL-036, fixes "bị vấp")
16.65 s, −14.2 LUFS, peak −1.4 dBFS. F5 v3: one natural take per line (NFE 32), phrases cut only at real silences (boundary minima −36…−68 dB re peak, all 9 cut), no silenceremove/rubberband on F5. check-rules L-007/L-008/L-009 all ✔ (v1 failed L-007/L-008 on all 4 lines). STT of the full mix: all words present; "tô ích" still heard "tố ích", "kỳ" → "tì" (whisper on TTS tones). A/B (v1 processed → raw F5 take → v3 per line): /workspace/hi-oneup/sample-f5/ab.wav (outside repo).

## v3 (DL-038, L-016: no word-level cutting)
14.98 s, −14.1 LUFS, peak −1.5 dBFS. Each line split only at punctuation into clause units (merge < 4 syllables) → 6 units total, each its own F5 call × 3 fixed seeds; no cut inside any F5 output; edge trim −50 dB/40 ms pads/15 ms fades; punctuation pauses + room tone. Unit F0 spread 0.3 st (L2) / 1.2 st (L4). check-rules L-016/L-007/L-008/L-009 ✔. A/B v2 → v3 per line: /workspace/hi-oneup/sample-f5/ab-v3.wav.
