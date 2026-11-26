---
name: script-polish
description: >-
  Use after a short-form video script is drafted (facts checked) and before it goes
  to the creator for approval: remove AI-writing tells with the vendored humanizer
  skill, adapt to spoken Vietnamese, and match the creator's voice profile, without
  changing any fact, number or citation.
version: "1.5.0"
metadata:
  author: OneUp Studio
  tags:
    - script
    - vietnamese
    - voice
    - humanizer
---
# Script polish (VI voice)

## Purpose
Polish a fact-checked short-form script into spoken Vietnamese that matches the creator voice profile, removing both AI-writing vocabulary and structural AI-tells without changing facts.


## Inputs
While the words are still being found (draft v1 and v2), load only three things: the two approved scripts `a-c01` and `a-c04`, the idea plus the core fact, and the rule that each next sentence answers the question the previous one raised. Do not load `connectors.tsv`, `bookish.tsv`, `ai-blacklist.tsv`, `cadence-patterns.tsv` or `style-pairs.md` into that pass.

This polish pass runs after the monologue exists and after the 25–30% cut. It may then look at:
- Draft script (VI voice lines + EN captions).
- `content/voice-profile.md` and the two approved scripts above. Their rhythm overrides a ban list.
- `resources/feedback.md`: what Hiệp rejected, in his words.
- Optional **voice memo transcript** (`media/voice-memos/<name>.txt`). Keep ≥ 80% of his words when one exists.
- `skills/humanizer/SKILL.md` in embedded mode, for tells that survive the cut. Do not use it to stuff connectors.

## Two tiers — Hard-Gate + Pairwise A/B — what this pass may and may not "fix"
- **Tier 1, hard fails (`H1–H4`, sole hard blocker; never introduce, always fix):** H1 fact without source / beyond the source · H2 total ≥ 300 s (L-099) · H3 wrong brand/format for the channel (@hi.oneup DL-027; @vanhiep.tech its AGENTS.md) or mocking the viewer (L-053) · H4 broken draft/spec structure.
- **Tier 2, Pairwise A/B** (replaces absolute ≥85 score threshold): compared side-by-side against the theme/format-matched approved anchor clip on 4 relative axes (`Hook & Giữ chân`, `Mạch truyện & Chuyển ý`, `Văn nói tự nhiên VN`, `Độ đắt của ẩn dụ/payoff`). Also run `python3 pipeline/scripts/audio-precheck.py <draft.md>` to check spoken VN rhythm (2.6–3.4 syl/s, pacing contrast, no repeated consecutive beat openers). A narrative breath of about 15–25 syllables with a comma is healthy. A landing line of about 5–10 syllables is a punch, not a defect. Warn only on an unbroken span over 32 syllables.
- **Soft warnings are not errors.** Do NOT "correct" natural spoken variants that match the voice profile: particles (nè, á, hông, nghen), spoken connectors («thật ra thì», «nhưng mà khoan», «nghe quen không», «nói thẳng ra là», «thế mới có chuyện»), short punchy sentences, rhetorical questions that hold attention. Polishing these into tidy written Vietnamese is exactly what Hiệp rejects (L-105, L-106).

## Cut, then listen
1. Delete every sentence that explains again what the listener just understood, and every moral that repeats the image. That cut is about 25–30% on a stuffed draft. If what remains is 75–90 s, keep it.
2. Do not add a sentence so a beat has an "anchor", a connector, or a number. A physical detail stays only when the story was already using it.
3. `check-rules.py --draft` at the end is for hard errors (H1–H4, and any ✖ the draft gate still raises). `check-rules.py --audit` prints bookish, ai-structure and choppy. Leave a natural line alone when clearing the warning would make it sound written.

## Emotional and logical flow
A beat is not a slide. The last sentence of a beat plants the question the next beat answers. «Nhưng mà» and «thành ra» are for that turn, not a connector quota. If the next beat could be moved anywhere without the listener noticing, rewrite the join in the monologue before touching word choice.

## Steps
1. **Fact lock.** List every fact, number, study, date and citation in the draft. These must appear unchanged in the output.
2. **Humanizer pass** on the VI lines and EN captions. The structural tells apply in any language. In Vietnamese, watch for:
   - "Không phải X, mà là Y" used just for emphasis.
   - Triads ("nhanh, gọn, hiệu quả").
   - Closers that only repeat the point ("Và đó chính là chìa khoá.").
   - Inflated words: "bí quyết", "thay đổi cuộc đời", "đỉnh cao", "chìa khoá vàng".
   - Staged openers: "Bạn có biết…", "Hãy cùng tìm hiểu…".
   - Every sentence the same length.
   - **Paste test** (adapted from mankidev/antialgorithm, MIT): a line that could go into another clip unchanged is too general. Rewrite it around the concrete thing in this clip (something Hiệp saw, did or said, the study's real detail), not a bigger claim. Don't swap a cliché for its known opposite. Don't add a time, date or number just to sound concrete; keep one only when the viewer needs it. Never invent a fact to fill the gap (step 1 still holds).
3. **Spoken VI pass.** Read the cut monologue aloud. A written tell («tuy nhiên», «do đó», «bạn có biết») goes only if the sentence still sounds like the same person after the change. Do not open `connectors.tsv` to insert a join. One «nha» is enough. Numbers are written the way they are read aloud ("chín mươi sáu").
4. **Voice pass.** Apply the confirmed profile:
   - Use the profile's region and particles, sparingly.
   - Use its humor style. For @hi.oneup that is 4/5 sly teasing aimed at habits and at the creator himself, never at viewers or groups.
   - Use its English-mix rule: 1–3 words per clip, to lighten the mood or stress the key idea.
   - Copy the do/don't examples in the profile.
5. **Story pass (rule-41).** Prefer a personal story arc (situation → struggle → turn → lesson → invite) built from a story-bank entry. Mark each unconfirmed detail `[CẦN HIỆP XÁC NHẬN]`. Never invent outcomes, like "it worked", that the creator hasn't confirmed.
5b. **Voice-First Input** (when a memo transcript exists, `resources/vn-spoken/voice-first.md`): edit from Hiệp's words. Keep his vocabulary, comparisons and examples; only cut repeats, move the hook first, split beats and add connectors / source lines. Check `python3 pipeline/scripts/voice-memo.py keep <memo.txt> <draft.md>` ≥ 80%.
6. **Voice details.**
   - Use only the creator's real phrases, examples and level of humor from the profile.
   - Never invent a personal story. If a line needs one, insert `[VÍ DỤ THẬT CỦA HIỆP: ...]` as a placeholder.
7. **Trend check (rule-37).** At least one current phrase or situation from `research/trends/ingest.md` must stay in the script, used naturally.
8. **Diff + verify.** Output the old and new lines side by side, list the facts and confirm each is unchanged, and apply L-099: total strictly <300s INCLUDING end card, pauses and transitions; 60–180s is the target, and 60–119s is not a warning. No word quotas, no padding, no speed-up. Before Chốt label natural-reading duration ƯỚC/estimate; measure actual audio/video only after Chốt. This is not Chốt and does not waive W-16.
9. Save as `script-vX.Y-draft.md` next to the approved version. Never overwrite the approved script until the creator approves.

## Requirements
- Read this skill before acting; follow linked channel/repo AGENTS.md when cited.
- Use tools and paths named in the steps; do not invent alternate pipelines.

## Limitations
- Must not change facts, numbers, or citations.
- Depends on `content/voice-profile.md` and `skills/humanizer`.
- Not a topic researcher — facts must already be checked.

## Troubleshooting
| Error / symptom | Cause | Fix |
|---|---|---|
| Facts drifted | Over-aggressive rewrite | Diff against fact-lock list; restore numbers/citations |
| Still sounds AI | Residual humanizer tells | Re-run humanizer pass on VI + EN captions |
| Wrong pronouns/particles | Profile ignored | Re-read `content/voice-profile.md` samples |
| Reviewer flags colloquial lines | Soft warning treated as error | Soft warnings score 0 (rubric §3b); keep the line if it matches the voice profile |
| Voice-First ratio < 80% | Writer replaced Hiệp's words | Restore his phrasing from the memo; change order, not words |
