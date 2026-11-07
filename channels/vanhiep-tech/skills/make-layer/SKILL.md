---
name: make-layer
description: >-
  Build and render explainer layers for @vanhiep.tech CapCut hybrid videos.
  Always solid One Dark bg; colors only from brand-tokens.json / tokens.css.
  Use for ov-d / ov-hook / cu HyperFrames pre-render.
---
# Make layer (@vanhiep.tech)

Not `make-video` (comic). Read `channels/vanhiep-tech/AGENTS.md` + `PLAN.md` first.

## When to use
- New `ov-*` / `cu-*` for a `vht-YYYYMMDD-*` clip
- Revise an existing layer HTML after feedback
- Smoke-test CapCut alpha handoff

## Steps
1. Confirm clip id + layer id from `script.md` markers.
2. Read HyperFrames router: `skills/hyperframes/hyperframes/SKILL.md` then core → animation → creative → cli.
3. Author under `clips/<clip-id>/layers/<layer-id>/` (HTML composition).
4. Sync fonts + **brand tokens.css** (gitignored fonts; tokens.css committed or copied):
   ```bash
   LAYER=channels/vanhiep-tech/clips/<clip>/layers/<layer>
   mkdir -p "$LAYER/fonts"
   cp brand/fonts/BeVietnamPro-{Regular,SemiBold,Bold}.ttf "$LAYER/fonts/"
   cp channels/vanhiep-tech/brand/tokens.css "$LAYER/tokens.css"
   ```
5. Colors: **only** `var(--vht-*)` / names in `brand-tokens.json`. No raw invented hex in HTML/CSS/JS (GSAP may read computed `--vht-accent`).
6. `cd` layer dir → `npm i` (gsap) → `npx hyperframes@0.8.150 check`
7. Render **solid MP4** (`background: var(--vht-bg)` — never transparent / never pink preview):
   ```bash
   npx hyperframes@0.8.150 render --format mp4 \
     -o ../../../../../../media/channels/vanhiep-tech/<clip>/<layer>.mp4 .
   ```
8. Update `media/MANIFEST.json` after binary lands on disk.
9. Point CapCut import path in `script.md` layer table.

## Design rules
- **Brand colors only:** `channels/vanhiep-tech/brand/brand-tokens.json` + `tokens.css`
- **Always solid background** `var(--vht-bg)` on `#main` / `html` / `body`
- **Banned:** pink, magenta, fuchsia; any hex not in tokens
- No chibi / OneUp logo / cam OneUp
- Always motion (fromTo children; no static PNG as final deliverable)
- `talking-head-recut` = layout reference only — do not composite A-roll here

## CapCut smoke
See `channels/vanhiep-tech/docs/capcut-smoke.md`.
