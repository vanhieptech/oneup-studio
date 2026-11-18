---
name: write-script
description: >-
  Use whenever anyone asks to write, rewrite or fix the SPOKEN SCRIPT of a @hi.oneup
  clip ("viết script", "làm script clip-NN", "làm lại script", "script có Omi", hook
  concepts, beat lines) before Hiệp says "Chốt". Single entry point that loads the
  current gates (lessons L-087..L-105, L-099 duration, W-16 order, Omi week rule),
  the brief, the template and the review hand-off, so every agent writes to the same
  standard. Not for render/voice/visuals (make-video after Chốt) and not for
  @vanhiep.tech (channels/vanhiep-tech/AGENTS.md).
version: "1.0.0"
metadata:
  author: OneUp Studio
  tags:
    - script
    - hook
    - storytelling
    - hi-oneup
    - omi
---
# Write script (@hi.oneup, before Chốt)

## Purpose
One standard way for any agent (Claude Code, Codex, Cursor, box agents) to go from a
locked fact + a real trend/pain to a spoken script Hiệp can approve. It does not copy
rules; it tells you which canonical file to read for each step and what the output must
contain. Writing only: no images, TTS, render or publish before Chốt (L-098 (5)).

## Inputs
Read fresh every time, in this order (never from memory):

| # | File | Why |
|---|---|---|
| 1 | `AGENTS.md`, `docs/conventions/storage.md` | where files go (rule-65/66) |
| 2 | `logs/lessons.md` — all, newest last (L-087..L-105 are the hook/flow gates) | rule-49: never repeat a known failure |
| 3 | `logs/rule-checklist.md`, `logs/rule-scoring-rubric.md` | P/W/X gates + 100-point rubric the reviewer uses |
| 4 | `rules/video-rules.md` (rule-11 Omi, rule-41 story, rule-46 voices, rule-56 CTA) + `logs/decision-log.md` | current law |
| 5 | `templates/script.md` | required beat table + markup (`|`, `{nhấn: …}`) |
| 6 | `content/voice-profile.md` (§2 Hiệp, §3b Omi, §3c markup), `content/story-bank.md`, `content/theme-map.md` | voice, true stories, theme + week |
| 7 | `research/trends/ingest.md`, `research/trends/patterns.md` (P01–P16 / F01–F09), newest 3 digests in `research/trends/YYYY-MM-DD/` | trend + hook pattern (rule-37, L-090, L-100) |
| 8 | Clip fact lock: `content/clips/<clip>/fact-package*.md` or `research/fact-packages/*<clip>*` | only claims allowed in the lines (P-03) |
| 9 | `research/craft/hook-script-study-2026-11-11.md`, `research/script-writer-prompt.md` (hook table H, rubric R) | craft reference, not law |
| 10 | Previous two clips' `final/script-final.md` (hook + CTA) and every rejected draft of THIS clip | L-088 no template reuse, L-095 freshness |

Missing fact lock or trend file → stop and hand back to Deep Research / Social Research
(`workflows/agents/*.md`); do not write around the gap.

## Steps
1. **Brief (write it at the top of the draft, empty box = do not write lines yet).**
   One sentence for the whole clip · fact lock (verbatim, with source) · viewer pain in
   a real person's words + link · one action doable today · trend id + link · theme/week
   from theme-map · speakers · lines Hiệp already locked (keep verbatim, L-046).
2. **Three concepts, one line each (L-095)** with "vì sao người lướt sẽ dừng". If this is
   a redo after Hiệp rejected, each concept must change the hook, opening situation and
   line of reasoning — not just words. Pick one and say why it differs from rejected ones.
3. **Hook gate before writing the body.** Hook = start of a story told like to a close
   friend (L-103, L-105): a real situation the viewer recognises (L-101, L-087 daily life,
   no school-subject example), a cost worth caring about + a surprise or reversal within
   3s (L-104, L-096 (1)), and a question a real person would ask. No report numbers,
   "theo một thí nghiệm", "trung bình", "người ta" in the first 2 sentences; no literary
   images ("im bặt", "cứ nghĩ mãi"). Name the method in the hook or promise it explicitly
   (L-102). Map the actual hook words to an active P/F pattern with its source row; no fit
   → UNMAPPED, do not force a code (L-100).
4. **Causal chain first, then sentences.** Order W-16 (L-077): pain → example → sourced
   cause → goal said personally → method → evidence → result back at the same pain → one
   CTA. Evidence sentence = who/which source + A vs B + result in the source's words, told
   inside the story with a lead-in (L-088, L-096 (2)); never "nhiều nghiên cứu thấy".
5. **Write the lines.** Every sentence can be understood heard once, has a subject, and
   grows out of the previous one (L-092, L-094, L-102). No two sentences under 8 words in a
   row (L-096 (3)); no word >5% or repeated 3-word phrase (L-093); one meaning per word;
   one narrator person ("bạn" to viewer, L-089); particles per voice-profile §3c limits;
   1–3 English words; numbers written as spoken.
6. **Omi (only if theme-map week ≥ 5, rule-11; validator blocks earlier).** Omi is the AI
   companion of the OneUp app, voice "F5 · Mỹ Duyên": short lines, teasing habits not
   people (P02 "Omi calls it out"), never states facts Hiệp's line didn't source, no hands
   (cannot type). Hiệp chibi = "F5 · Thái Sơn". Put each speaker in the `Người nói` column
   and an `emotion` per Omi line. Week < 5 → no Omi; offer the Omi version as a note only.
7. **Duration (L-099).** No word quota. Write ƯỚC = natural reading + pauses + transitions
   + end card; target 120–180s is a warning only, finished total strictly < 300s.
8. **Polish** with `skills/script-polish` (uses `skills/humanizer`) without touching any
   fact, number or citation.
9. **Self-audit tables inside the draft** (the reviewer re-does them independently):
   hook–pain–promise–payoff with line refs (L-098 (1)) · referent table for every "cách
   này / điều đó / nó" (L-098 (2)) · sentence-pair table with the linking words quoted
   (L-094) · claim → source per beat · hook ↔ P/F mapping (L-100) · EN captions ≤ 8
   words/chunk matching each beat · end card (safety line, CC BY 4.0 credit + link,
   sources, no endorsement) · human read-aloud: `CHƯA KIỂM` unless a person really did it.
10. **Machine checks (support only, L-098 (4)).** Text-only modes of
    `python3 pipeline/scripts/check-rules.py` (`--l088 --flow --clarity --link --repeat
    --evidence --choppy --fresh --trend --subjects`) on the draft; ✖ blocks hand-off, ✔ is
    never proof of meaning.
11. **Save + hand off.** Draft → `content/clips/<clip>/archive/script-vX.Y-draft.md`
    (only `final/`, `archive/`, `README.md` allowed at clip root, rule-66). Hand to Rule
    Reviewer (`workflows/agents/rule-reviewer.md`); never self-approve (L-086). After
    Chốt → `skills/make-video` §2 onward (spec, voice, render).

## Requirements
- Read this skill and the files in Inputs before writing; cite the lesson id for every gate you apply.
- Facts only from the clip fact lock; personal stories only from `content/story-bank.md`, else `[CẦN HIỆP XÁC NHẬN]`.
- On any correction from Hiệp: add/update the lesson in `logs/lessons.md` first (rule-49), then fix the named lines (rule-36); after the 3rd patch round of the same draft, rewrite (L-094).

## Limitations
- Writing gate only; it cannot approve. Rule Reviewer scores, Hiệp says "Chốt".
- Does not research trends or verify facts (Social Research / Deep Research).
- Duration is an estimate until audio exists; measure after Chốt.
- Not for @vanhiep.tech talking-head scripts.

## Troubleshooting
| Symptom (Hiệp's words) | Likely cause | Fix (lesson) |
|---|---|---|
| "Hook xàm" | number/technical question, no viewer situation | L-101, L-104: situation + cost + surprise |
| "Sến, giả, không giống người nói" | literary images, staged "bạn" past actions | L-105: say it like to a friend, first person or direct |
| "Cộc lốc, rời rạc" | sentences cut to fit a quota, no links | L-096 (3), L-103, L-099 |
| "Dẫn chứng đâu" | "nhiều nghiên cứu" / source hidden | L-096 (2): who + A vs B + result |
| "Nhạt, làm lại từ đầu" | same chain with new words | L-095: three new concepts first |
| Checker green but Hiệp rejects | treated ✔ as meaning proof | L-098 (4), manual gates in step 9 |
| Omi blocked by validator | week < 5 | rule-11: remove Omi or move clip to week ≥ 5 (Hiệp decides) |
