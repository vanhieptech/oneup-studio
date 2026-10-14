---
name: Make video (@hi.oneup end-to-end)
description: >-
  Use whenever Hiệp asks for a clip ("Làm clip tiếp theo", "Làm clip về <chủ đề/trend>",
  "làm lại clip-NN", or beat feedback like "b03: đổi câu …"). The single workflow from
  intake to post package that keeps every clip consistent with rules/video-rules.md:
  read sources → script → humanizer → check-rules → review gate 1 → render → check-rules
  --final → review gate 2 → log decisions. Edits go to the spec, never a regenerate.
---
# Make video (one workflow, rule-48)

Repo: `oneup-studio` (box clone `/workspace/oneup-studio`, Mac `/Users/macbook/me/projects/oneup-studio`).
Reference implementation: `content/clips/clip-01-implementation-intention/final/` (spec, explainer template, script-final, post).

## 0. How Hiệp asks (intake)
| Hiệp writes | Agent does |
|---|---|
| `Làm clip tiếp theo` | next row in `content/theme-map.md` without a `final/` folder → its topic, theme, week |
| `Làm clip về <chủ đề / trend>` | pick the best Bridge for it in `research/trends/ingest.md` (or make one, rule-39) → map to a HowToLiveBetter lesson → next free clip id; theme by tone (rule-17) |
| `Làm lại clip-NN` / `clip-NN v2` | reuse `content/clips/clip-NN-*/final/spec.json`, add a `revisions` row |
| Optional add-ons in the same message | `tuần N` (default: theme-map week) · `có Omi` / `không Omi` · `dark`/`light` · `chuyện: S-xx` (story-bank id) |
Ask only what blocks a decision (rule: ask before deciding). Never invent a personal story; unknown details stay generic and go to the confirm list.

## 1. Read before writing (always, in this order)
0. **`logs/lessons.md` (rule-49)**: read every lesson; avoid each known failure in this clip. On ANY correction from Hiệp: first add/update the lesson (symptom in his words, root cause, fix, detection) and, if measurable, a `L-NNN` check in `pipeline/scripts/check-rules.py`; then fix; then re-run check-rules (✖ blocks review).
1. `AGENTS.md` → `rules/video-rules.md` (current version) → `logs/decision-log.md` (all DL, rule-33).
2. `content/voice-profile.md`, `content/story-bank.md`, `content/theme-map.md` (theme + week; Omi only week ≥ 5, rule-11).
3. `research/trends/ingest.md` + newest `research/trends/YYYY-MM-DD/` digest (+ `patterns.md`) → ≥1 trend phrase/situation (rule-37), note its id.
4. The HowToLiveBetter source section → write the **Fact lock** list.
5. `logs/effects-log.md` (avoid repeating signature effects back-to-back).

## 2. Script draft → `final/spec.json` (the ONE source of truth)
Write the script directly as the spec (format below). Structure rule-41: hook 0–3s → struggle → turn → lesson/explainer (3–4 motion beats) → evidence → payoff → CTA question, last line loops to the hook. 150–170 VI words, 55–60s.
- Story beats = comic (`engine: remotion`); explain/evidence beats = motion graphics (`engine: hyperframes`), rule-42.
- Voice: "bạn", Southern particles on some (not all) lines, humor 4/5 aimed at habits, 1–3 English words.
- Every line: `speaker`, `emotion`, `text` (bubble, `**bold**` = emphasis), `en` (caption, English only), `hl` (indexes of highlighted EN words), optional `say` (phonetic spelling for TTS, e.g. TOEIC → "tô ích", numbers as read), optional `take`.
- **Voices (DL-035):** Hiệp = "F5 · Thái Sơn", Omi = "F5 · Mỹ Duyên" (F5-TTS, synthetic VieNeu references in `pipeline/tts/f5-refs/`; checkpoint CC-BY-NC-SA, risk accepted by Hiệp — do not re-ask, but flag it if the channel starts direct monetisation). F5 runs on CPU ≈40–70 s per take × 3 takes per phrase: a 55–60 s clip ≈ 60–90 min voice stage the first time (cached afterwards, so revise per line, not whole spec). Leakage of the reference sentence ("hôm nay trời Sài Gòn…") at a take's start is auto-trimmed; check `leak_trims` in the voice JSON and re-listen if many. F5 v4 (DL-038, L-016 — v2/v3 word-level cutting still stuttered): the line is split ONLY at punctuation (. , ? ! … ; :) into clause units, each unit is a separate F5 call (units < 4 syllables are merged), audio is never cut inside an F5 output; pauses come from punctuation (`,` 180 ms, `.` 350, `?`/`!` 400, `…` 500). So **write phrasing with punctuation**: to add a pause or isolate a punch word, add `,` / `...` / `.` in the text. For F5 lines `phrases` only set caption chunks (`en`); `gap`/`tempo`/`semi`/`emph` are ignored. Units and their seeds/scores are in the voice JSON `units`; check-rules L-016 fails any intra-output cut.
- **Voice prosody (required for new lines, DL-033):** give every line `phrases` so it sounds human, not read. `build-final.py` then voices it with `pipeline/scripts/voice-prosody.py` instead of the old sentence+stretch path:
  `"phrases": [{"t": "Kế hoạch học tô ích của mình là...", "gap": 0.42, "tempo": 0.96, "semi": -0.3}, {"t": "mai học.", "emph": true, "en": "…"}]`
  0. **Naturalness markup (DL-039, cheat-sheet in `content/voice-profile.md` §3c):** punctuation drives delivery (`?` rise, `!` energy, `…` trail, `—` interruption, `( )` quieter aside); fillers `{ừm}` `{ờ}` `{à}` `{ơ}` `{hừm}` `{ủa}` `{trời ơi}` `{thì là}` (spoken inside the next unit), `{bank:ừm}` (cached filler clip between units), `{ngập ngừng}`, `{kéo: nha}`. Particles are read plain by default (Hiệp prefers plain, DL-040/L-018); `{kéo: …}` lengthening is optional, explicit only, ≤ 1 per clip. Caps: ≤ 1 filler/line, ≤ max(2, lines/4)/clip (check-rules L-017). Markup only in `phrases[].t`, never in `text`/`en`.
  1. Split into breath groups of 3–8 syllables; keep each phrase's own punctuation (`...` trails off, `?` rises, `,` continues, `:` sets up). Never phrases of 1–2 syllables except a particle/interjection (`Ủa?`, `Nè,`).
  2. `gap` after each phrase 0.15–0.42 s (comma ≈0.18, colon ≈0.26, ellipsis ≈0.38, before the punchline ≈0.4). Gaps are filled with room tone.
  3. One `emph` per line (the punch word/phrase) → slower, +0.8 st, +1.5 dB. For a falling statement end use `"emph_semi": -0.5` (otherwise it can sound like a question).
  4. Vary `tempo` (0.9–1.08) and `semi` (−0.5…+1.2): question/tease up, tired/sad down. Particles (á, nha, hông, ủa, nè) at phrase ends or as a lead-in, max 1–2 per line, and keep them inside a ≥3-syllable phrase (alone they get mangled).
  5. Don't use `[cười]` / `[thở dài]` tags (VieNeu or F5): STT showed they get spoken as words ("Thì…", "hờt"). Show the laugh/sigh in the face instead.
  6. The script picks the best of 3 takes per phrase (STT ≥ 0.7 gate, F0 range, artifacts), checks the whole line by STT (toneless ≥ 0.92) and re-rolls weak phrases; a `warn: … line STT sim` in the build log = rewrite the phrase or the `say` spelling.
  7. Optional per-phrase `en` = caption chunk timed to that phrase (better sync than one EN line spread evenly).

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
**HyperFrames skills (required, rule-42, DL-032).** Before writing or editing any `engine: hyperframes` beat, read `skills/hyperframes/README.md` and then in order `hyperframes/SKILL.md` (router), `hyperframes-core`, `hyperframes-animation`, `hyperframes-creative` (brand rules win on palette/font), `hyperframes-registry` (check for a block before hand-building), `hyperframes-cli`. Run `npx hyperframes lint` (Node ≥ 22) on the explainer before rendering. Open gaps in the clip-01 reference: `logs/hyperframes-audit-2026-10-13.md`.

Explainer visuals: copy **`content/samples/sample-natural/explainer/`** (the lint-clean reference, DL-033: host `index.html.tpl` + one sub-composition per section in `compositions/<eNN>.html.tpl` + `compositions/captions.html.tpl`). Every `*.tpl` receives `__TIMING__`, `__DUR__` and per section `__START_<id>__` / `__DUR_<id>__`, used as the section host's real `data-start`/`data-duration` (the runtime hides it outside its window; never fake visibility with opacity). Inside a section: animate children with `fromTo` (never the clip, no CSS transform on tweened nodes, no exit tweens except the last scene), convert times with `t - __START_<id>__`. Captions = brand-styled adaptation of registry `caption-pill-karaoke` (group ≤4 words, karaoke step, hard-kill at group end), host carries `data-track-kind="captions"`. Section-to-section transitions: `hyperframes-animation/transitions/catalog.md` (push slide primary). Gate: `npx hyperframes lint` **and** `npx hyperframes check` must both report 0 errors / 0 warnings (build-final runs lint before rendering). GSAP local, Be Vietnam Pro.
Motion: run `skills/motion-picks-per-script` → one main effect per beat (`motion` field + table in script-final.md) → append to `logs/effects-log.md`.

## 3. Polish
Run `skills/script-polish` (humanizer + voice profile) on `text`/`en`. Fact lock unchanged. Unconfirmed personal details → generic wording + listed under `[CẦN HIỆP XÁC NHẬN]`.

## 4. Automated rules gate
```bash
python3 pipeline/scripts/build-final.py <clip>/final/spec.json --stage plans   # TTS (cached) + timing.json + plans + explainer html
python3 pipeline/scripts/check-rules.py <clip>/ --stt                          # must PASS (0 ✖) before gate 1
```
`check-rules` covers: length 55–60s, word count, hook/CTA, scene ≤ 8s, Omi week (rule-11), theme vs theme-map, beat ids, comic vs motion engine, EN-only captions + highlight indexes, no emoji, Be Vietnam Pro only + no CDN, no music, SFX allowed + sourced, every transition has an SFX + ambience bed (rule-50, DL-042: default whoosh-soft at part xfades, swish at scene/section changes, 0.12s lead, quiet; continuous ambience; never music), AI-tell phrases, particles / "bạn" / English mix, unconfirmed story items, voice presets (no cloning), STT of every line, post package (credit + license link + "đã chuyển thể", AI toggle + disclosure), video-engine validator; with `--final` also MP4 spec, −14 LUFS, contact sheet. A line failing STT: fix `say` or bump `take`, rebuild.

## 5. Review gate 1 (Hiệp): script
Send `final/script-final.md` (beat table: **beat · time · visual · VI line · EN caption · voice emotion**, motion picks, fact lock, confirm list) + storyboard contact sheet (`storyboard/` or a draft render's `contact-sheet.png`) + one-line summary of voices/theme/week. Stop and wait.

## 6. Render + self-review
```bash
python3 pipeline/scripts/build-final.py <clip>/final/spec.json        # voice → plans → Remotion + HyperFrames → join, SFX, grain, −14 LUFS
python3 pipeline/scripts/build-final.py <clip>/final/spec.json --stage assemble   # mix/SFX only, reuses rendered parts (no re-voice/re-render)
ffmpeg -i <clip>/final/out/<id>.mp4 -vf "fps=1/2,scale=216:384,tile=8x4:padding=6:color=0x111111" -frames:v 1 <clip>/final/contact-sheet.png
python3 pipeline/scripts/check-rules.py <clip>/ --final --stt --out <clip>/final/check-rules.txt
```
Look at full-size frames of every beat at least 2 rounds (rule-34): text inside safe area, nothing clipped, captions not covering faces, highlight on the right word, logo present. Fix in spec/template, add a `revisions` row, rebuild.

## 7. Review gate 2 (Hiệp): final
Send the MP4 + `post.md` (caption VI in "bạn" voice that asserts no unconfirmed fact, hashtags, HowToLiveBetter CC BY 4.0 credit + license link + "đã chuyển thể", AI toggle + disclosure line naming the characters who speak, exact form: "Giọng của Hiệp (nhân vật) và Omi trong video là giọng AI tổng hợp (F5-TTS)." — rule-46/DL-035, check-rules errors if "F5-TTS" is missing) + `check-rules.txt` summary + confirm list. Agent never posts.

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
