# SRT Sidecar Feature - Verification Report

## Summary

Successfully implemented standalone `.srt` subtitle file generation for the oneup-studio short-video pipeline. The feature takes the idea from YILS-LIN/short-video-factory (exporting a standalone .srt file) but implements it from scratch with no code copying.

## Files Changed

### New Files
1. **`pipeline/scripts/generate_srt.py`** (207 lines)
   - Core SRT generation logic
   - Reads `timing.json` and produces standard SRT format
   - Validates monotonic timing and duration coverage

2. **`pipeline/tests/test_srt_generator.py`** (294 lines)
   - 20 comprehensive unit tests
   - Tests formatting, generation, validation, edge cases
   - Integration test with actual clip-01 data

3. **`docs/features/srt-sidecar.md`** (207 lines)
   - Feature documentation
   - Rationale, usage, examples, migration path

### Modified Files
1. **`pipeline/scripts/build-final.py`** (+4 lines)
   - Added SRT generation call after MP4 assembly
   - Only for full clips, not preview scenes

2. **`pipeline/scripts/check-rules.py`** (+115 lines)
   - Added `validate_srt_sidecar()` function
   - Added `parse_srt_time()` helper
   - Validates SRT in `--final` mode

## Key Design Decisions

### English Captions Chosen Over Vietnamese

**Decision:** Use English captions (`en` field) for the SRT content.

**Rationale:**
1. English captions are already displayed on screen
2. Broader accessibility for international viewers
3. Better for SEO and discovery on platforms
4. TikTok/YouTube handle mixed audio/subtitle languages well
5. Primary use case is platform upload utility

**Documented in:** `docs/features/srt-sidecar.md` (lines 9-20)

### File Location

**Decision:** Place SRT files in `final/out/<clip-name>.srt` alongside the MP4.

**Rationale:**
1. Mirrors MP4 location for consistency
2. Keeps related upload artifacts together
3. Follows existing `storage.md` conventions
4. Easy to find when uploading

**Path examples:**
```
content/clips/clip-04-gap-sach-tu-kiem/final/out/clip-04-gap-sach-tu-kiem.mp4
content/clips/clip-04-gap-sach-tu-kiem/final/out/clip-04-gap-sach-tu-kiem.srt
```

### Check-rules Validation Strategy

**Decision:** Validate SRT in `--final` mode, but scope checks to avoid breaking archived clips.

**Implementation:**
- ✔ **Exists:** SRT must be present for new clips
- ✔ **Format:** Must parse as valid SRT
- ✔ **Monotonic:** Each subtitle starts at or after the previous
- ✔ **Coverage:** Duration within 5s of video (warns if more)

**Migration-friendly:** Old archived clips skip this check naturally (they're excluded from `--final` checks per rule-66).

## Test Results

### Unit Tests (20/20 passing)

```bash
$ python3 pipeline/tests/test_srt_generator.py

test_escape_srt_text_basic ... ok
test_escape_srt_text_commas ... ok
test_escape_srt_text_empty ... ok
test_escape_srt_text_newlines ... ok
test_escape_srt_text_whitespace ... ok
test_format_srt_time_hours ... ok
test_format_srt_time_minutes ... ok
test_format_srt_time_negative ... ok
test_format_srt_time_seconds ... ok
test_format_srt_time_zero ... ok
test_generate_srt_basic ... ok
test_generate_srt_commas_in_captions ... ok
test_generate_srt_empty_lines ... ok
test_generate_srt_invalid_duration ... ok
test_generate_srt_monotonic_check ... ok
test_generate_srt_negative_time ... ok
test_generate_srt_no_lines ... ok
test_generate_srt_realistic ... ok
test_generate_srt_sequential_indices ... ok
test_clip_01_timing ... ok

Ran 20 tests in 0.001s
OK
```

**Coverage:**
- Timestamp formatting (zero, seconds, minutes, hours, negative clamping)
- Text escaping (newlines, whitespace, commas, empty strings)
- SRT generation (basic, empty lines, sequential indices)
- Validation (monotonic timing, invalid duration, negative times)
- Edge cases (no lines, overlapping times)
- Integration (real clip-01 timing.json)

### Manual Verification

#### Clip-01 (archived)

```bash
$ python3 pipeline/scripts/generate_srt.py content/archive/clip-01-implementation-intention/final/timing.json

Generated SRT: content/archive/clip-01-implementation-intention/final/out/clip-01-implementation-intention.srt
  13 subtitle entries
  Duration: 60.7s
```

**Output head:**
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
```

#### Clip-04 (active)

```bash
$ python3 pipeline/scripts/generate_srt.py content/clips/clip-04-gap-sach-tu-kiem/final/timing.json

Generated SRT: content/clips/clip-04-gap-sach-tu-kiem/final/out/clip-04-gap-sach-tu-kiem.srt
  11 subtitle entries
  Duration: 83.7s
```

**Output head:**
```srt
1
00:00:00,120 --> 00:00:01,791
You think you just forget easily?

2
00:00:01,872 --> 00:00:06,453
No — you read all night and your head is still empty, because you never actually remembered it in the first place.

3
00:00:06,663 --> 00:00:13,475
Stings to hear that, doesn't it? Exam prep, English — rereading and highlighting everything, and it still won't stick.
```

### Check-rules Validation

```bash
$ python3 pipeline/scripts/check-rules.py content/clips/clip-04-gap-sach-tu-kiem/ --final

...
✔ srt-sidecar SRT file exists: clip-04-gap-sach-tu-kiem.srt
✔ srt-sidecar SRT parsed: 11 entries
✔ srt-sidecar SRT timing is monotonic
✔ srt-sidecar SRT duration 83.5s matches video 83.7s (±5s)
...

140 checks · 14 error(s) · 12 warning(s) → FAIL
```

**Note:** The overall FAIL is due to unrelated existing issues (trend-signals.md missing, etc.). The SRT checks all pass (4/4 ✔).

## Code Quality

### Follows Repo Conventions

1. **Minimal change:** Only touches files directly related to SRT generation
2. **No refactoring:** Doesn't modify unrelated code
3. **Idiomatic:** Uses existing patterns (`sh()` helper, `sys.path` setup, error handling)
4. **Documented:** Follows front-matter conventions for .md files
5. **Tested:** Comprehensive test coverage with clear test names

### Edge Cases Handled

1. **Empty captions:** Lines without `en` text are skipped
2. **Negative times:** Clamped to 0
3. **Invalid duration:** Errors with clear message
4. **Non-monotonic timing:** Detected and reported
5. **Commas in timestamps:** Handled correctly (they're in time format, not text)
6. **Newlines in text:** Converted to spaces
7. **Multiple spaces:** Collapsed to single space

### Error Messages

All error messages are clear and actionable:
- "Line 3 has non-positive duration: 0"
- "Non-monotonic timing: entry 2 starts at 1.0s before entry 1 at 2.0s"
- "SRT file missing: clip-04-gap-sach-tu-kiem.srt (should be generated by build-final.py)"

## Example SRT Output

Full `clip-01-implementation-intention.srt` (13 entries, 1.3KB):

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

4
00:00:11,913 --> 00:00:16,806
It's called an implementation intention: when, where, what cue, THEN what.

5
00:00:17,655 --> 00:00:21,905
Decide while fresh. When the cue shows up, no debate with tired you.

6
00:00:22,756 --> 00:00:25,890
Example: 9 PM, laptop closed, THEN one listening lesson.

7
00:00:26,740 --> 00:00:30,330
Or: Tuesday 8 AM, at my desk, THEN write the intro first.

8
00:00:31,181 --> 00:00:36,771
94 independent tests: if-then planners hit goals more often. Medium-to-large effect.

9
00:00:37,621 --> 00:00:42,191
It helps you start, hold on when interrupted, and quit what can't work.

10
00:00:43,040 --> 00:00:48,850
Common mistake: "when I'm free." Use a time, a place, or a finished task.

11
00:00:49,454 --> 00:00:53,933
Only works for goals you actually want. Takes 1–2 minutes.

12
00:00:54,933 --> 00:00:58,513
Try it now: one if-then line for your "tomorrow". Comment it.

13
00:00:58,713 --> 00:01:00,265
"Tomorrow" has nowhere to hide.
```

## Integration with Existing Pipeline

### Build Process

1. **Before:** `build-final.py` → MP4 only
2. **After:** `build-final.py` → MP4 + SRT (automatic)

**Code change (build-final.py lines 330-334):**
```python
# Generate SRT sidecar (English captions synced to TTS timing)
if not sel:  # only for full clips, not preview scenes
    sh([sys.executable, os.path.join(REPO, "pipeline/scripts/generate_srt.py"), tj])
```

### QA Gates

**Gate 1 (script review):** No change
**Gate 2 (final review):** Now includes SRT validation

From `skills/make-video/SKILL.md`:
```
## 6. Render + self-review
...
python3 pipeline/scripts/check-rules.py <clip>/ --final --stt --out <clip>/final/check-rules.txt
```

This command now validates the SRT file automatically.

### Timing Source

The SRT uses the **same timing data** as the renderer:

```
timing.json (single source of truth)
    ├─> Video renderer (Remotion/HyperFrames)
    └─> SRT generator (generate_srt.py)
```

This ensures **no drift** between the video and standalone subtitles.

## Future Enhancements

The current implementation satisfies the stated requirements, but could be extended:

1. **Vietnamese SRT:** Add `--vietnamese` flag to generate VI subtitles from `say` field
2. **Dual SRT:** Generate both `<clip>-en.srt` and `<clip>-vi.srt` for bilingual support
3. **Styling:** Add basic SRT styling tags for position/color (platform-dependent support)
4. **WebVTT:** Generate `.vtt` format for web players (more features than SRT)

None of these are needed for the current TikTok upload use case, so they're left as future work.

## Conclusion

✅ **Feature complete and tested**
✅ **All 20 tests pass**
✅ **Verified on 2 existing clips**
✅ **check-rules validation works**
✅ **Documentation written**
✅ **PR created: #1**

The SRT sidecar feature is ready for review and merge.
