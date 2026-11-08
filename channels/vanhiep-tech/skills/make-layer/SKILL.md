---
name: make-layer
description: >-
  Build and render explainer layers for @vanhiep.tech CapCut hybrid videos.
  Cutaways: solid One Dark. Overlays: transparent canvas (no plate). Colors only
  from brand-tokens.json / tokens.css. Use for ov-* / cu-* HyperFrames pre-render.
---
# Make layer (@vanhiep.tech)

Not `make-video` (comic). Read `channels/vanhiep-tech/AGENTS.md` + `PLAN.md` first.

**Local Mac first:** render + CapCut trên `/Users/macbook/me/projects/oneup-studio`.  
**Banned handoff:** `/opt/cursor/artifacts`, cloud chat links, box `/workspace/...` as CapCut import source.

## When to use
- New `ov-*` / `cu-*` for a `vht-YYYYMMDD-*` clip
- Revise an existing layer HTML after feedback
- Smoke-test CapCut alpha handoff **on Mac**

## Steps
1. Confirm clip id + layer id from `script.md` markers. Prefer running this skill on the Mac checkout.
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
5. Colors: **only** `var(--vht-*)` / names in `brand-tokens.json`. No raw invented hex in HTML/CSS/JS.
6. Self-check vs `frame.md` + **Generate gate** below before render.
7. `cd` layer dir → `npm i` (gsap) → `npx hyperframes@0.8.150 check`
8. Render by type:
   - **`cu-*` cutaway / B-roll** — solid `var(--vht-bg)` on `html,body,#main` → `--format mp4`
   - **`ov-*` overlay** — `html,body,#main{background:transparent !important}` · **no zone plate** → `--format mov`
   ```bash
   npx hyperframes@0.8.150 render --format mp4 -o media/.../cu-01.mp4 .
   npx hyperframes@0.8.150 render --format mov -o media/.../ov-d01.mov .
   ```
9. **Verify alpha (ov only)** before shipping:
   ```bash
   ffprobe -v error -select_streams v:0 -show_entries stream=pix_fmt -of csv=p=0 LAYER.mov
   # must contain yuva / alpha. Corners of a mid-frame PNG must be RGBA (0,0,0,0).
   ```
10. **Preview for human** (ov): export **alpha-preserving** watch file only — animated WebP/APNG (`*-alpha.webp` / `*-alpha.png`) or the ProRes `.mov` itself.  
    **Banned:** baking overlay onto One Dark / fake A-roll / checkerboard into an MP4 and calling that “the overlay video”. MP4 has no alpha → it will always look like it still has a background.
11. Write outputs under Mac `media/channels/vanhiep-tech/<clip>/` and update `media/MANIFEST.json`.
12. Point CapCut to **Mac absolute paths** in `docs/capcut-smoke.md` / `script.md` (`ov-*.mov` only). Never tell the user to import from cloud artifacts.

## Generate gate (fail = rewrite HTML)
| Check | Cutaway `cu-*` | Overlay `ov-*` |
|---|---|---|
| Canvas bg | solid `--vht-bg` | **transparent** — never `#282C34` / glass board on `#main` |
| Zone plate | N/A (full frame is the shot) | **Banned** — no full-width frosted card covering the zone |
| Piece fills | UI mocks / surfaces OK | Only on badges, buttons, phone/server chrome — not a backdrop |
| Outside pieces | painted brand void OK | **alpha = 0** |
| Deliverable | `.mp4` on Mac `media/` | ProRes `.mov` (`yuva*`) on Mac `media/` |
| CapCut source | local Mac path | local Mac path — **not** cloud artifacts |
| User preview | `.mp4` as-is | alpha file on Mac (WebP/APNG/MOV) — never plate-composited MP4 |
| Creative | real UI/flow, depth, video type scale | same + talking-head safe zones |

## Design rules
- Brand colors only: `brand-tokens.json` + `tokens.css` + `frame.md`
- Interpret concept as **UI / tokens / flow**, not centered text cards
- **Banned:** pink/magenta/fuchsia; invented hex; left-stripe-only L3; empty void (cutaway); equal card grids; overlay zone glass plates; RGB/MP4-baked overlays; fake-A-roll composite sold as the layer
- Always motion with varied ease/direction; no chibi / OneUp cam accent
- `talking-head-recut` = layout reference only

## CapCut smoke
See `channels/vanhiep-tech/docs/capcut-smoke.md`.
