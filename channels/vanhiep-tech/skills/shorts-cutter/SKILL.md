---
name: shorts-cutter
description: >-
  Use when Hiệp gives a long video he owns or has permission to use (MP4 or YouTube link: talk,
  livestream, podcast, long @vanhiep.tech recording) and asks to cut it into vertical shorts
  ("cắt video này thành Shorts", "lấy đoạn hay nhất từ video dài này"). Rights gate first,
  transcribe locally, propose 45–90s segments with reasons, wait for Hiệp to pick, then cut 9:16
  A-roll for the normal @vanhiep.tech CapCut pipeline. Never ships a final export itself.
version: "1.0.0"
metadata:
  author: OneUp Studio
  tags:
    - vanhiep-tech
    - shorts
    - recut
    - ffmpeg
---
# Shorts cutter (@vanhiep.tech)

Rebuilt from the retired box agent `docs/legacy-box/workflows-agents/shorts-cutter.md` (26/11/2026). Highlight-scoring idea from [Anil-matcha/AI-Youtube-Shorts-Generator](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator) (MIT); nothing vendored. Read `channels/vanhiep-tech/AGENTS.md` first: this skill only produces cut A-roll, and the channel's rules (CapCut Desktop export, layers, no chibi, no @hi.oneup comic rules) still decide the rest.

## Gate 0: rights (stop if missing)
Hiệp must say the source is his own, or who gave permission. Third-party video with no clear permission: stop, don't download or cut. The MIT license of the reference repo covers code only, never the footage.

## Steps
1. **Source.** Local file → copy to `media/channels/vanhiep-tech/<src-id>/source.<ext>`. YouTube link of Hiệp's own channel → `yt-dlp` into the same folder (ask before installing anything missing). Add the file to `media/MANIFEST.json`; footage never goes into git or cloud.
2. **Transcribe locally** with faster-whisper through the repo's ASR Python (`pipeline/paths.py` → `ASR_PYTHON`, normally `~/oneup-tools/f5-venv/bin/python`), model `medium`, language `vi` (or auto for mixed EN). Cache `source.srt` + word timestamps next to the source; reuse the cache, don't re-run.
3. **Propose segments (Hiệp picks; nothing is cut before that).** Read the full transcript and score candidate windows 0–100 on: hook in the first 3s, one clear idea, a payoff or turn, quotable line, practical value, stands alone without earlier context. 45–90s each (channel V1), drop windows overlapping >50%, default 3 proposals. Send a table: `#` · start–end in the source · length · score · first spoken line (the hook) · one-line reason · what context the viewer would miss. Wait.
4. **Cut** the picked segments with local ffmpeg (`ffmpeg-skill` for recipes):
   - Snap in/out points to sentence boundaries from the word timestamps; no mid-word cuts.
   - Reframe to 1080×1920: keep Hiệp's face inside the safe zone through the whole segment. Use a fixed crop when he stays put; when he moves, split into keyframed crops and check the frames. Never stretch.
   - Keep the original voice; no TTS, no music (Hiệp adds sound in CapCut/TikTok).
   - Output `media/channels/vanhiep-tech/vht-YYYYMMDD-<slug>/a-roll.mp4` + `a-roll.srt` (segment-relative times) and add to the manifest.
5. **Self-check twice:** a contact sheet at start, middle and end of each cut, plus every crop change; face never cut off; audio starts and ends on whole words; transcript matches what's said; speech loudness close to −14 LUFS (measure; normalize in CapCut if off).
6. **Hand-off:** each picked segment becomes a normal clip folder `channels/vanhiep-tech/clips/vht-YYYYMMDD-<slug>/` with `script.md` built from the transcript (marker + `a_roll` column), then continue with `make-layer` (1–2 `ov-dNN` diagrams) and `make-capcut-draft`. The final export happens in CapCut Desktop, never from this skill.

## Report to Hiệp
Per segment: source timestamps, length, score + reason, rights note, check results, files written, and anything left undone (for example a crop that needs a manual pass).

## Hard stops
- No rights confirmation, or cutting before Hiệp picks the segments.
- Face cropped out, or cuts mid-word.
- Missing tool or model: say which one, ask before installing; don't switch to a paid cloud API without Hiệp agreeing.
