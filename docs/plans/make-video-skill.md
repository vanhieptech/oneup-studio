---
title: "Make video (one workflow, rule-48)"
date: 2026-10-15
type: plan
tags: [docs]
status: draft
source: "oneup-studio (soạn trong repo)"
name: Make video (@hi.oneup end-to-end)
description: >-
  Use whenever Hiệp asks for a clip ("Làm clip tiếp theo", "Làm clip về <chủ đề/trend>",
  "làm lại clip-NN", or beat feedback like "b03: đổi câu …"). The single workflow from
  intake to post package that keeps every clip consistent with rules/video-rules.md:
  read sources → script → humanizer → check-rules → review gate 1 → render → check-rules
  --final → review gate 2 → log decisions. Edits go to the spec, never a regenerate.
---
# Make video (one workflow, rule-48)

## Duration and approval override — 2026-11-08
This override applies to active rewrites and new clips; retain historical archives unchanged. Target 2–3 minutes (120–180 seconds), NOT a mandatory minimum. The HARD limit is total duration strictly below 300 seconds, including endcard, pauses and transitions; exactly 300 seconds fails.

This supersedes older 45–60s/55–60s limits, total-word hard caps (including 142–175 words), per-beat word budgets and approximately 50-word quotas before the method. Preserve natural pacing and enough context, explicit subjects/referents, connected reasoning, source/comparison/finding/limits. Do not add filler or repeat ideas to fill time, truncate evidence, or accelerate speech to fit. Keep one central takeaway and all source/meaning/craft requirements, including W-16's sourced cause; extra time does not authorize extra unsupported claims.

Before wording approval (Chốt), timing is ESTIMATED from natural speech only. Human read-aloud/listen-once evidence remains NOT TESTED unless genuinely performed on the exact wording. Do not generate images, TTS, render previews/video or publish before Chốt. In particular, do NOT run the legacy `build-final.py --stage plans` recipe below before Chốt: it can invoke voice. At wording review deliver the script and text-only scene/motion plans, not generated stills/contact sheets/covers; actual-image checks are a separate post-Chốt production gate. Any older instructions below requiring pre-Chốt images/cover/TTS are overridden. After Chốt, measure actual finished total duration and enforce <300 seconds including endcard; 120–180 seconds remains a target, not a hard minimum.

Old 55–60s TTS runtime estimates below are historical examples only, not a runtime promise for a 2–3-minute clip. Legacy checker/template limits must be reconciled through the code/storage owner; do not call an obsolete-length failure a waiver or claim the checker has been updated without evidence. All unrelated rules below remain in force.


Repo: `oneup-studio` (box clone `/workspace/oneup-studio`, Mac `/Users/macbook/me/projects/oneup-studio`).
Reference implementation: `content/archive/clip-01-implementation-intention/final/` (spec, explainer template, script-final, post).

## 0. How Hiệp asks (intake)
| Hiệp writes | Agent does |
|---|---|
| `Làm clip tiếp theo` | next row in `content/theme-map.md` without a `final/` folder → its topic, theme, week |
| `Làm clip về <chủ đề / trend>` | pick the best Bridge for it in `research/trends/ingest.md` (or make one, rule-39) → map to a HowToLiveBetter lesson → next free clip id; theme by tone (rule-17) |
| `Làm lại clip-NN` / `clip-NN v2` | reuse `content/clips/clip-NN-*/final/spec.json`, add a `revisions` row |
| Optional add-ons in the same message | `tuần N` (default: theme-map week) · `có Omi` / `không Omi` · `dark`/`light` · `chuyện: S-xx` (story-bank id) |
Ask only what blocks a decision (rule: ask before deciding). Never invent a personal story; unknown details stay generic and go to the confirm list.

## 1. Read before writing (always, in this order)
1. `AGENTS.md` → `rules/video-rules.md` (current version) → `logs/decision-log.md` (all DL, rule-33).
2. `content/voice-profile.md`, `content/story-bank.md`, `content/theme-map.md` (theme + week; Omi only week ≥ 5, rule-11).
3. `research/trends/ingest.md` + newest `research/trends/YYYY-MM-DD/` digest (+ `patterns.md`) → ≥1 trend phrase/situation (rule-37), note its id.
4. The HowToLiveBetter source section → write the **Fact lock** list.
5. `logs/effects-log.md` (avoid repeating signature effects back-to-back).

## 2. Script draft → `final/spec.json` (the ONE source of truth)
Write the script directly as the spec (format below). Structure rule-41: hook 0–3s → struggle → turn → lesson/explainer (3–4 motion beats) → evidence → payoff → CTA question, last line loops to the hook. Target 120–180s at natural pacing, not a hard minimum; finished total strictly <300s including endcard, pauses and transitions. No hard word quota. Before Chốt use ESTIMATED timing only.
- Story beats = comic (`engine: remotion`); explain/evidence beats = motion graphics (`engine: hyperframes`), rule-42.
- Voice: "bạn", Southern particles on some (not all) lines, humor 4/5 aimed at habits, 1–3 English words.
- Every line: `speaker`, `emotion`, `text` (bubble, `**bold**` = emphasis), `en` (caption, English only), `hl` (indexes of highlighted EN words), optional `say` (phonetic spelling for TTS, e.g. TOEIC → "tô ích", numbers as read), optional `take`.

```jsonc
{ "id": "clip-NN-final", "clip": "clip-NN", "title": "…", "week": 1, "theme": "light", "pillar": "…", "trend": "<ingest id>",
  "revisions": [{ "date": "YYYY-MM-DD", "dl": "DL-0xx", "note": "…" }],
  "parts": [
    { "id": "A", "engine": "remotion", "transitionOut": "slideleft",
      "scenes": [{ "id": "b01", "beat": "clip-NN.b01", "part": "hook", "background": "bed|desk|paper|grid|ink",
                   "framing": "medium", "push": 0.05, "transition": "cut|slide|iris|fade|wipe", "narration": "11:48 PM",
                   "cast": [{ "id": "hiep", "x": 0.5, "pose": "sitting", "action": "idle", "expression": "sad", "facing": "right", "enter": "pop" }],
                   "lines": [{ "speaker": "hiep", "emotion": "sad", "text": "…", "say": "…", "en": "…", "hl": [4],
                               "set": { "omi": { "expression": "happy", "action": "reacting" } } }],
                   "sfx": [{ "name": "pop|ding|whoosh", "atLine": 0, "offset": 0 }] }] },
    { "id": "E", "engine": "hyperframes", "dir": "explainer", "transitionOut": "circleopen",
      "sections": [{ "id": "e01", "beat": "clip-NN.b05", "part": "explain|evidence", "motion": "<awesome-ai-motion slug>", "lines": [ … ] }] },
    { "id": "B", "engine": "remotion", "scenes": [ … last scene part: "cta" … ] }
  ] }
```
Explainer visuals: copy `clip-01…/final/explainer/` (fonts, logo, package.json) and write `index.html.tpl` for the new content. It receives `__TIMING__` (sections → lines → `words[].start` for each spoken VI word, `cap`) and `__DUR__`; tie each animation to the spoken word that names it. GSAP local, transforms only (HyperFrames lint), Be Vietnam Pro.
Motion: run `skills/motion-picks-per-script` → one main effect per beat (`motion` field + table in script-final.md) → append to `logs/effects-log.md`.

## 3. Polish
Run `skills/script-polish` (humanizer + voice profile) on `text`/`en`. Fact lock unchanged. Unconfirmed personal details → generic wording + listed under `[CẦN HIỆP XÁC NHẬN]`.

## 4. Automated rules gate
```bash
python3 pipeline/scripts/build-final.py <clip>/final/spec.json --stage plans   # TTS (cached) + timing.json + plans + explainer html
python3 pipeline/scripts/check-rules.py <clip>/ --stt                          # must PASS (0 ✖) before gate 1
```
`check-rules` covers: finished total <300s including endcard/pauses/transitions, 120–180s target warning only, no hard total-word quota, hook/CTA, scene ≤ 8s, Omi week (rule-11), theme vs theme-map, beat ids, comic vs motion engine, EN-only captions + highlight indexes, no emoji, Be Vietnam Pro only + no CDN, no music, SFX allowed + sourced, AI-tell phrases, particles / "bạn" / English mix, unconfirmed story items, voice presets (no cloning), STT of every line, post package (credit + license link + "đã chuyển thể", AI toggle + disclosure), video-engine validator; with `--final` also MP4 spec, −14 LUFS, contact sheet. A line failing STT: fix `say` or bump `take`, rebuild.

## 5. Review gate 1 (Hiệp): script
Send `final/script-final.md` (beat table: **beat · time · visual · VI line · EN caption · voice emotion**, motion picks, fact lock, confirm list) + storyboard contact sheet (`storyboard/` or a draft render's `contact-sheet.png`) + one-line summary of voices/theme/week. Stop and wait.

## 6. Render + self-review
```bash
python3 pipeline/scripts/build-final.py <clip>/final/spec.json        # voice → plans → Remotion + HyperFrames → join, SFX, grain, −14 LUFS
ffmpeg -i <clip>/final/out/<id>.mp4 -vf "fps=1/2,scale=216:384,tile=8x4:padding=6:color=0x111111" -frames:v 1 <clip>/final/contact-sheet.png
python3 pipeline/scripts/check-rules.py <clip>/ --final --stt --out <clip>/final/check-rules.txt
```
Look at full-size frames of every beat at least 2 rounds (rule-34): text inside safe area, nothing clipped, captions not covering faces, highlight on the right word, logo present. Fix in spec/template, add a `revisions` row, rebuild.

## 7. Review gate 2 (Hiệp): final
Send the MP4 + `post.md` (caption VI in "bạn" voice that asserts no unconfirmed fact, hashtags, HowToLiveBetter CC BY 4.0 credit + license link + "đã chuyển thể", AI toggle + disclosure line naming the characters who speak) + `check-rules.txt` summary + confirm list. Agent never posts.

## 8. Feedback loop
Hiệp gives feedback by beat id, one per line:
```
b03: đổi câu "…" thành "…"
b05: chậm lại / chữ to hơn / bỏ hiệu ứng
e03: số liệu sai → …
all: giọng Omi nhanh quá
```
For each: add `DL-NNN` (quote him) → edit `final/spec.json` (line text/emotion/take, cast, sfx) or `explainer/index.html.tpl` → append `revisions` → rebuild only what changed (TTS cache by text+preset+emotion+take) → steps 6–7 → commit `clip-NN: … (DL-NNN)`. Same feedback twice → promote to a rule or this skill (rule-33).

## 9. Close out
Copy deliverables if asked; `python3 pipeline/scripts/build-index.py`; commit; push (or bundle when the Mac is offline, AGENTS.md). Media stays out of git (`final/out/` is ignored).
