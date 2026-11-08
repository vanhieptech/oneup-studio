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
2. **Read before any HTML** (mandatory — skip = reject redesign):
   - Channel frame: `channels/vanhiep-tech/brand/frame.md`
   - Router: `skills/hyperframes/hyperframes/SKILL.md`
   - Creative: `skills/hyperframes/hyperframes-creative/SKILL.md` then `references/house-style.md`, `video-composition.md`, `composition-patterns.md`, `motion-principles.md`
   - Motion craft: `skills/hyperframes/hyperframes-animation/` + `skills/hyperframes/motion-graphics/` (esp. `categories/lower-thirds`)
   - Overlay zones: `skills/hyperframes/talking-head-recut/` (face/title/L3 safe areas; **layout ref only**, no recut)
3. Author under `clips/<clip-id>/layers/<layer-id>/` (HTML composition).
4. Sync fonts + **brand tokens.css** (gitignored fonts; tokens.css committed or copied):
   ```bash
   LAYER=channels/vanhiep-tech/clips/<clip>/layers/<layer>
   mkdir -p "$LAYER/fonts"
   cp brand/fonts/BeVietnamPro-{Regular,SemiBold,Bold}.ttf "$LAYER/fonts/"
   cp channels/vanhiep-tech/brand/tokens.css "$LAYER/tokens.css"
   ```
5. Colors: **only** `var(--vht-*)` / names in `brand-tokens.json`. No raw invented hex in HTML/CSS/JS (GSAP may read computed `--vht-accent`).
6. Self-check vs `frame.md` before render: real UI/flow (not label cards), depth (bg+mid+fg), video type scale, varied motion, overlay in a zone.
7. `cd` layer dir → `npm i` (gsap) → `npx hyperframes@0.8.150 check`
8. Render by type:
   - **`cu-*` cutaway / B-roll** — solid `var(--vht-bg)` → `--format mp4`
   - **`ov-*` overlay** — `html,body,#main{background:transparent}` + brand cards → `--format mov`
   ```bash
   # cutaway
   npx hyperframes@0.8.150 render --format mp4 -o .../cu-01.mp4 .
   # overlay
   npx hyperframes@0.8.150 render --format mov -o .../ov-d01.mov .
   ```
9. Update `media/MANIFEST.json` after binary lands on disk.
10. Point CapCut import path in `script.md` layer table.

## Design rules
- **Brand colors only:** `brand-tokens.json` + `tokens.css` + `frame.md`
- Cutaway: full solid bg + grid/glow/ghost depth. Overlay: **transparent canvas only** — no zone-filling glass plate; piece fills OK
- Interpret concept as **UI / tokens / flow**, not centered text cards
- **Banned:** pink, magenta, fuchsia; invented hex; left-stripe-only L3; empty void; equal card grids; baking overlay previews onto opaque RGB backgrounds
- Always motion with varied ease/direction; no chibi / OneUp cam accent
- `talking-head-recut` = layout reference only

## CapCut smoke
See `channels/vanhiep-tech/docs/capcut-smoke.md`.
