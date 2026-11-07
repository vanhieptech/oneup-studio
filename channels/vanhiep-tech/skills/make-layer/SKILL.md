---
name: make-layer
description: >-
  Build and render explainer overlay/cutaway layers for @vanhiep.tech CapCut
  hybrid videos. Use when Hiệp asks for ov-d / ov-hook / cu layers, HyperFrames
  pre-render for vanhiep-tech, or CapCut alpha handoff (ProRes / chroma).
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
4. Sync fonts (gitignored):
   ```bash
   mkdir -p channels/vanhiep-tech/clips/<clip>/layers/<layer>/fonts
   cp brand/fonts/BeVietnamPro-{Regular,SemiBold,Bold}.ttf channels/vanhiep-tech/clips/<clip>/layers/<layer>/fonts/
   ```
5. `cd` layer dir → `npm i` (gsap) → `npx hyperframes@0.8.150 check`
6. Render **solid MP4** (full `#282C34` bg — never transparent / never pink preview):
   ```bash
   npx hyperframes@0.8.150 render --format mp4 \
     -o ../../../../../../media/channels/vanhiep-tech/<clip>/<layer>.mp4 .
   ```
7. Update `media/MANIFEST.json` after binary lands on disk.
8. Point CapCut import path in `script.md` layer table.

## Design rules
- Tokens: `channels/vanhiep-tech/brand/brand-tokens.json` (One Dark; accent `#56B6C2`)
- **Always solid background** `#282C34` on `#main` / `html` / `body`
- **Banned:** pink, magenta, fuchsia (bg or preview)
- No chibi / OneUp logo / cam `#FF5A36`
- Always motion (fromTo children; no static PNG as final deliverable)
- `talking-head-recut` = layout reference only — do not composite A-roll here

## CapCut smoke
See `channels/vanhiep-tech/docs/capcut-smoke.md`.
