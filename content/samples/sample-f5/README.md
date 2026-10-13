---
id: sample-f5
type: sample
updated: 2026-10-13
tags: [voice, f5-tts, prosody, DL-035]
---
# sample-f5 (DL-035): same as sample-natural, voices = F5-TTS
Hiệp "F5 · Thái Sơn", Omi "F5 · Mỹ Duyên" (synthetic VieNeu refs, `pipeline/tts/f5-refs/`). 17.1 s, 1080×1920, 30 fps, −14.0 LUFS, peak −1.4 dBFS. Week ≥5 sample only.
- Build: `F5_NFE=24 python3 pipeline/scripts/build-final.py content/samples/sample-f5/spec.json` (first run ≈46 min on 8-core CPU, then cached).
- F5 line mode: each take = whole line, cut into `phrases` at word timestamps, then gaps/emphasis; 3 takes, STT pick, leakage trim (0 trims needed here).
- Line STT (toneless): L1 Hiệp 0.70 ("tô ích" heard as "tổ ích"; whisper weakness, words otherwise right), L2 Omi 0.92, L3 Omi 0.93, L4 Hiệp 0.92. Omi drops the particle "á" in L2.
- ⚠ Checkpoint CC-BY-NC-SA-4.0 (non-commercial), risk accepted by Hiệp (DL-035). Caption disclosure: "… giọng AI tổng hợp (F5-TTS)."
