---
title: "@hi.oneup motion layer, based on gongnyang/awesome-ai-motion"
date: 2026-10-12
source: "oneup-studio (soạn trong repo)"
id: research.motion-layer
type: research
status: reference
updated: 2026-10-12
tags: [motion]
---
# @hi.oneup motion layer, based on gongnyang/awesome-ai-motion

Local clone: `resources/refs/awesome-ai-motion (clone, xem resources/refs/README.md)` (shallow clone, 2026-10-12)

## 1. What the repo actually contains
- **What it is:** a motion-technique *field guide* (a reference library), not a video generator and not an AI video model. It contains no generative AI video at all. Every clip is a deterministic HTML/CSS/GSAP/SVG/canvas/WebGL animation that Playwright captures and ffmpeg encodes.
- **637 effect cards** (`effects/<slug>/README.md`). Each card has a definition, when to use it, a parameter table (default and range), easing, things to avoid, a code snippet, sources, and prompts for Claude Code and Codex. The cards are mostly in Korean, with English fields in `index.json`.
  - Families: transitions 98, data 74, texture 59, generative 47, explainer 48, ui 47, loop 44, entrance 38, type 33, depth 33, shape 32, principles 26, camera 22, emphasis 22, caption 14.
  - Runtimes: gsap 213, svg 128, webgl 114, css 103, canvas 79.
  - 352 cards are tagged for short-form (숏폼) media.
- **Rendered clips:** every effect folder has `clip.mp4`, `preview.gif` and `poster.jpg`. `_클립 모음/` holds 51 curated reference mp4s. The README says 128 are "reference clips". These are abstract demos on paper/ink/vermilion stages, not footage. Only 2 effects/recipes are authored at a vertical size (720x1280).
- **11 recipes** (`recipes/`): shorts-hook, edu-hook, data-story, concept-explainer, before-after, product-demo, quote-card, title-opener, chapter-transition, ai-principle, scrolldeck-scene. Each is a timed sequence of effects. `shorts-hook` is a 5s vertical one: kinetic beats → zoom-through → count-up.
- **7 routes** (`routes/*.md`, Korean only): shorts, video editing, promo, infographic, thumbnail, newsletter, deck & site. **`routes/쇼츠.md` (shorts) is the most valuable file for us.** It covers the 9:16 1080×1920 canvas, the hook in the first 1–3s, safe areas, 4.5:1 contrast, no flashes, "one main effect + at most one accent per beat", jump cut → insert → stable synced caption for talky segments, and pairing J/L cuts with captions.
- **Agent skill:** `SKILL.md` describes the workflow: intent → decision tables → read card → recipe/route → swap content and render via `node scripts/render.mjs`.
- **Tech:** Node 20, Playwright/Chromium, ffmpeg, GSAP 3.14 (bundled). There is **no Remotion** in the repo.

**Verdict:** it's a deep, well-parameterised vocabulary with timing defaults. It is not a pipeline. None of it touches real footage, voice or captions sync. The value we take from it is *parameters and editorial rules*, re-implemented in Remotion. We don't take its renderer.

## 2. License
- Repo: **MIT** (© 2026 gongnyang). `ATTRIBUTIONS.md` states that all cards, clips and prompts are original and MIT, so reuse with modification is allowed. If we copy substantial code, we keep the MIT notice. Re-implementing ideas and parameter values in our own Remotion code needs no notice, though a credit is courteous.
- Bundled `lib/gsap.min.js` is covered by the GreenSock Standard "no charge" license, which is free. **We don't need it**, because Remotion's `interpolate`/`spring`/`Easing` reproduce the same eases (power2.out ≈ `Easing.out(Easing.quad)`, power3.out ≈ `Easing.out(Easing.cubic)`, back.out ≈ `Easing.out(Easing.back(1.7))`).
- Fonts are under OFL 1.1. Some cited *concept* sources (e.g. react-bits) are MIT + Commons Clause, but those are only cited. Don't copy from those sources directly.
- Fits the "free tools only" rule: Remotion is free for individuals, and FFmpeg is free.

## 3. Useful vs not
**Useful:** caption-family cards (karaoke-caption, word-pop-caption), camera (push-in, zoom-to-detail, ken-burns), editing (jump-cut, cutaway, split-edit/J-L, match-cut, hard-cut), emphasis/type (highlight-sweep, underline-draw, strikethrough-replace, kinetic-beats), data (count-up, unit-grid), explainers (step-recap), lower-third-reveal, the shorts route rules, and the shorts-hook/edu-hook/data-story recipe timings.

**Not useful / off-rules:** webgl/generative/texture families (fractal zoom, glitch, film dust; heavy and off-brand), AI-concept explainers (next-token, embedding-space), scrolldeck/web-UI effects, flashy transitions (zoom-flash, whip-pan except at most once), and the HTML→Playwright renderer. Our pipeline is Remotion on the Mac.

## 4. The motion layer: 10 picks
Canvas 1080×1920 at 30fps. Rule: **one main effect + at most one accent per beat**. Keep captions and graphics out of the bottom ~20% (TikTok UI) and the right ~120px. The brand accent replaces the repo's #FFD400. Brand hex/font are still pending from Hiệp.

| # | Technique (repo card) | Use in our clips | Remotion implementation | Params (from card, adapted) |
|---|---|---|---|---|
| 1 | **karaoke-caption** | Default EN caption on every clip | `<Caption>`: phrase window from VI sentence timestamps (whisper.cpp on VI audio). Words get equal sub-windows; the active word's color/bg is interpolated | 4–6 words/line, 150ms highlight transition, ±50ms offset, contrast ≥7:1 |
| 2 | **word-pop-caption** | Hook line and CTA line only | Per word: `spring()` scale 0.85→1.08→1 | 160ms/word, 3 words/page, back.out(2) |
| 3 | **jump-cut** + subtle **punch-in** | Talking head: cut silences, alternate 100%/112% framing per cut | Detect silence with FFmpeg `silencedetect` → `<Series>` of `<OffthreadVideo>` with alternating `scale` | Zoom 1.0 ↔ 1.12. Never jump on a negation or the key action word |
| 4 | **push-in** | Slow drift on the key sentence (talking head or b-roll) | `interpolate(frame,[0,d],[1,1.08])` with `Easing.inOut(Easing.quad)` | Card uses 1.3–1.7 for text; for faces use 1.05–1.10 over 1.4–2.1s |
| 5 | **ken-burns** | Static desk/stock stills, slow b-roll | scale 1.0→1.06 plus a small translate across the shot | Linear or power1.inOut, whole shot |
| 6 | **cutaway / split-edit (J/L cut)** | Face → desk b-roll while the voice continues | Audio track continuous; video `<Sequence>` swaps 6–10 frames before/after sentence boundary | Caption stays on the voice timing, not the cut |
| 7 | **highlight-sweep** | Key phrase on screen ("if → then") | Rect `scaleX` 0→1 from the left, behind the text | 0.7–1.0s (shortened for shorts), 0.3s delay after the text appears |
| 8 | **strikethrough-replace** | "Not 'I'll do this'" → the correct sentence | SVG line `strokeDashoffset` 1→0, then the new text fades/slides in | Strike 0.4s, replace 0.3s, hold ≥1s |
| 9 | **count-up** (+ optional **unit-grid**) | Stats such as "94 studies" | `Math.round(interpolate(...))` with `Easing.out(Easing.quad)`; label appears after arrival | 0.3s hold at 0, then 1.0–1.65s to 94, label at the end; optional grid of 94 dots with 0.01s stagger |
| 10 | **lower-third-reveal** + logo | Term card ("Implementation intention") plus a persistent small OneUp logo | Mask reveal (clipPath width) for the term; logo top-left at 70% opacity | Reveal 0.4s, hold to sentence end |

Optional accents (at most once per clip): **zoom-to-detail** for app screen recordings (weeks 3–4), **step-recap** for 3-point tips, **match-cut** face→face.

## 5. Updated pipeline
```mermaid
flowchart TD
  A[Script draft VI + EN] --> B{Hiệp approves script}
  B --> C[Hiệp records VI voice on iPhone + footage]
  C --> D[Drop files to ~/Movies/hi-oneup/clipNN on I-Am-Focused]
  D --> E[FFmpeg: normalize audio, silencedetect, 1080x1920 30fps proxies]
  E --> F[whisper.cpp VI timestamps -> map EN phrases per sentence]
  F --> G[Motion spec per beat (this doc): technique + params JSON]
  G --> H[Remotion composition: footage track, jump cuts/punch-ins, J/L cuts]
  H --> I[Motion layer: karaoke captions, highlight/strike, count-up, lower-third, logo]
  I --> J[Safe-area + contrast check, still frames at beat midpoints]
  J --> K[Render H.264 MP4, no music]
  K --> L{Hiệp approves final}
  L --> M[Upload package: mp4 + caption w/ CC BY credit + reminder Mon/Wed/Fri/Sun 7PM]
```

## 6. Clip 1 motion spec ("implementation intention", ~38s)
Timings follow the script's beats. They get re-snapped to the real VI voice timestamps after recording. The karaoke caption (#1) runs throughout unless noted, and the logo stays persistent.

| Time | Footage | Main effect | Accent | Caption / on-screen |
|---|---|---|---|---|
| 0.0–3.0 | Face, framed tight at 112% | **word-pop-caption** on the hook | push-in 1.00→1.06 over 3s | "You keep writing 'I'll do it tomorrow.'" / "That's why it never starts." |
| 3.0–5.0 | J-cut to desk POV (voice leads by ~8 frames) | **cutaway** | — | "Change one sentence." |
| 5.0–7.5 | Notebook, hand writing "I'll do this" | **strikethrough-replace** on the written/overlaid "I'll do this" | — | "Not 'I'll do this.'" |
| 7.5–12.0 | Hand writes the if-then line | **highlight-sweep** under "Tuesday 8am at my desk → draft the intro" (arrow in brand color) | ken-burns 1.0→1.05 | Same line as overlay text (caption hidden to avoid duplication) |
| 12.0–15.5 | Hands/desk b-roll | **lower-third-reveal**: "Implementation intention" term card | — | "Psychologists call it an implementation intention." |
| 15.5–21.0 | Text over dimmed b-roll (60% dark overlay) | **count-up** 0→94, label "studies" | optional unit-grid of 94 dots | "Across 94 studies, if-then plans raise follow-through." |
| 21.0–28.0 | Clock/calendar b-roll | **kinetic beats**: three cards "Medium-to-large effect" / "Zero cost" / "1–2 minutes", 0.3s stagger, scale 1.4→1 settle 0.2s | — | Captions are the cards themselves |
| 28.0–33.0 | Face (or text if faceless), jump-cut punch-in 100→112% | **jump-cut** | highlight-sweep on "one if-then line" | "Tonight: one if-then line for one real task." |
| 33.0–38.0 | Face/desk, hold | **word-pop-caption** CTA | — | "Next: why you delay even when you know what to do." Hold the last frame 0.5s |

Guardrails: no flashes or whip-pans in clip 1. Each card holds ≥1s after completion. Everything stays above y≈1530 px. Fix in the script file: the shoot note "No logo required" contradicts the rules, so the logo stays on.

## 7. Open items
- OneUp brand hex codes, font and logo file. These replace the placeholder accent.
- A Remotion project scaffold on the Mac (`npx create-video@latest`) plus whisper.cpp for VI timestamps. Both are free.
