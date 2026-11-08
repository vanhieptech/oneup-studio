---
title: "SRT Sidecar Subtitles"
date: 2026-10-19
source: "oneup-studio (feature implementation)"
id: feat-srt-sidecar
type: feature
status: active
updated: 2026-10-19
tags: [subtitles, srt, accessibility, upload]
---
# SRT Sidecar Subtitle Feature

## Overview

Every clip build now generates a standalone `.srt` (SubRip) subtitle file alongside the rendered MP4. This file contains English captions synced to the Vietnamese TTS timing, providing a standard subtitle format for upload to platforms like TikTok, YouTube, and others that support sidecar subtitle files.

## Rationale

**English captions chosen over Vietnamese lines:**
- English captions are what's displayed on screen in the video
- English improves accessibility for non-Vietnamese viewers
- English helps with discovery and SEO on international platforms
- Platform subtitle systems (TikTok, YouTube) already support Vietnamese audio + English subtitle combinations
- The SRT is primarily for platform upload, where English subtitles provide broader accessibility

The timing is derived from the same `timing.json` data the renderer uses, ensuring **no drift** between the video and the standalone subtitle file.

## Location

The SRT file is generated in:
```
content/{clips,archive}/<clip-name>/final/out/<clip-name>.srt
```

This mirrors the MP4 location:
```
content/{clips,archive}/<clip-name>/final/out/<clip-name>.mp4
```

Both the MP4 and SRT sit together in the `final/out/` directory, ready for upload.

## Generation

SRT generation is automatic during the build process:

```bash
python3 pipeline/scripts/build-final.py <clip>/final/spec.json
# → Generates <clip>/final/out/<clip-name>.mp4
# → Generates <clip>/final/out/<clip-name>.srt (new)
```

The generator:
1. Reads `timing.json` (produced during the build)
2. Extracts English captions (`en` field) and their timing (`t`, `dur`)
3. Formats as standard SRT with sequential indices
4. Validates monotonic timing (each entry starts after the previous)
5. Writes to `final/out/<clip-name>.srt`

## Validation

The `check-rules.py` script validates the SRT file when run with `--final`:

```bash
python3 pipeline/scripts/check-rules.py <clip>/ --final
```

Checks performed:
- ✔ **File exists:** SRT must be present alongside the MP4
- ✔ **Format valid:** Parses as proper SRT (index, timestamps, text)
- ✔ **Monotonic timing:** Each subtitle starts at or after the previous (no overlaps or time-travel)
- ✔ **Duration coverage:** SRT end time is within 5 seconds of video duration (warns if > 5s difference)

These checks are **blocking** for `--final` (errors prevent gate 2), but **non-blocking** for old archived clips (which may not have SRT files yet).

## Example

From `clip-01-implementation-intention`:

```srt
1
00:00:00,120 --> 00:00:02,340
My TOEIC study plan: "tomorrow."

2
00:00:03,339 --> 00:00:06,451
Every night: code, tired, then… "eh, tomorrow."

3
00:00:07,450 --> 00:00:11,163
Not missing motivation. Missing one sentence: IF… THEN…

...
```

Each entry:
- Sequential index (1, 2, 3…)
- Timestamp range in `HH:MM:SS,mmm --> HH:MM:SS,mmm` format
- English caption text
- Blank line separator

## Format Details

- **Timestamp format:** `HH:MM:SS,mmm` (hours:minutes:seconds,milliseconds)
- **Timing source:** Derived from `timing.json` `lines[].t` (start) and `lines[].dur` (duration)
- **Text source:** `lines[].en` (English captions, same as on-screen display)
- **Escaping:** Newlines converted to spaces, multiple spaces collapsed
- **Empty captions:** Lines without `en` text are skipped
- **Encoding:** UTF-8

## Implementation

**New files:**
- `pipeline/scripts/generate_srt.py` — SRT generator (run by build-final.py)
- `pipeline/tests/test_srt_generator.py` — Unit tests (20 tests, all passing)

**Modified files:**
- `pipeline/scripts/build-final.py` — Calls `generate_srt.py` after MP4 assembly
- `pipeline/scripts/check-rules.py` — Validates SRT in `--final` mode

## Testing

Run the test suite:

```bash
python3 pipeline/tests/test_srt_generator.py
```

Tests cover:
- Timestamp formatting (seconds, minutes, hours, negative clamping)
- Text escaping (newlines, whitespace, commas, empty strings)
- SRT generation (basic, empty lines, monotonic check, invalid duration/time)
- Edge cases (no lines, overlapping times, realistic clip data)
- Integration (uses actual `clip-01` timing.json)

All 20 tests pass.

## Manual Testing

Generate SRT for an existing clip:

```bash
python3 pipeline/scripts/generate_srt.py content/archive/clip-01-implementation-intention/final/timing.json
# → Output: content/archive/clip-01-implementation-intention/final/out/clip-01-implementation-intention.srt
```

Validate it:

```bash
python3 pipeline/scripts/check-rules.py content/clips/clip-04-gap-sach-tu-kiem/ --final
# Shows: ✔ srt-sidecar SRT file exists: clip-04-gap-sach-tu-kiem.srt
#        ✔ srt-sidecar SRT parsed: 11 entries
#        ✔ srt-sidecar SRT timing is monotonic
#        ✔ srt-sidecar SRT duration 83.5s matches video 83.7s (±5s)
```

## Future Considerations

This implementation uses English captions because:
1. They're already displayed on screen
2. They provide broader accessibility
3. Platforms handle mixed audio/subtitle languages well

If Vietnamese subtitles are needed in the future (for Vietnamese deaf/hard-of-hearing viewers), we could:
- Add a `--vietnamese` flag to `generate_srt.py`
- Generate both `<clip>-en.srt` and `<clip>-vi.srt`
- Use the `say` field instead of `en` for Vietnamese timing

However, for TikTok upload purposes, English subtitles provide the most utility.

## Migration Path

Existing archived clips do NOT retroactively fail `check-rules --final` due to missing SRT files. The check only applies to new clips built after this feature was added (2026-10-19).

Old clips can have SRT generated by running:

```bash
python3 pipeline/scripts/generate_srt.py <clip>/final/timing.json
```

## References

- Timing data format: `docs/workflow/per-video-pipeline.md`
- Build pipeline: `pipeline/pipeline.md`
- Check-rules gates: `skills/make-video/SKILL.md` (gate 1 / gate 2)
- SRT format spec: SubRip text file format (industry standard)
