---
name: make-layer
description: >-
  Build and render explainer layers for @vanhiep.tech CapCut hybrid videos.
  Cutaways: solid One Dark. Overlays: transparent canvas, hard edges (no soft
  shadow). Colors only from brand-tokens.json / tokens.css. Use for ov-* / cu-*
  HyperFrames pre-render.
version: "1.0.0"
metadata:
  author: OneUp Studio
  tags:
    - hyperframes
    - overlay
    - vanhiep-tech
    - cutaway
---
# Make layer (@vanhiep.tech)

## Purpose
Author and render explainer overlay/cutaway layers for @vanhiep.tech CapCut hybrid videos with brand tokens and hard-edge alpha.


Not `make-video` (comic). Read `channels/vanhiep-tech/AGENTS.md` + `PLAN.md` first.

**Local Mac first:** render + CapCut on the Mac checkout of `oneup-studio`.  
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
6. Self-check vs `frame.md` + **Generate gate** + **Known mistakes** below before render.
7. Grep HTML/CSS for banned overlay soft effects (must be empty on `ov-*`):
   ```bash
   rg -n 'box-shadow|text-shadow|filter:\s*blur|drop-shadow' layers/<id>/index.html
   ```
8. `cd` layer dir → `npm i` (gsap) → `npx hyperframes@0.8.150 check`
9. Render by type:
   - **`cu-*` cutaway / B-roll** — solid `var(--vht-bg)` on `html,body,#main` → `--format mp4`
   - **`ov-*` overlay** — `html,body,#main{background:transparent !important}` · **no zone plate** · **no soft shadow** → `--format mov`
   ```bash
   npx hyperframes@0.8.150 render --format mp4 -o media/.../cu-01.mp4 .
   npx hyperframes@0.8.150 render --format mov -o media/.../ov-d01.mov .
   ```
10. **Verify alpha (ov only)** before shipping — corners alone are **not** enough:
    ```bash
    ffprobe -v error -select_streams v:0 -show_entries stream=pix_fmt -of csv=p=0 LAYER.mov
    # must contain yuva / alpha

    # mid-frame: corners clear + soft-alpha budget
    ffmpeg -y -ss 1.5 -i LAYER.mov -frames:v 1 /tmp/ov-check.png
    python3 - <<'PY'
    from PIL import Image
    im = Image.open("/tmp/ov-check.png").convert("RGBA")
    w, h = im.size
    assert im.getpixel((0, 0))[3] == 0 and im.getpixel((w-1, h-1))[3] == 0
    semi = sum(1 for y in range(0, h, 2) for x in range(0, w, 2)
               if 0 < im.getpixel((x, y))[3] < 250)
    tot = (w // 2) * (h // 2)
    pct = 100 * semi / tot
    print(f"semi-alpha≈{pct:.2f}%")
    assert pct < 3.0, "soft fog too high — strip box-shadow/text-shadow/blur"
    PY
    ```
11. **Preview for human** (ov): export **alpha-preserving** watch file only — animated WebP/APNG (`*-alpha.webp` / `*-alpha.png`) or the ProRes `.mov` itself.  
    **Banned:** baking overlay onto One Dark / fake A-roll / checkerboard into an MP4 and calling that “the overlay video”. MP4 has no alpha → it will always look like it still has a background.
12. Write outputs under Mac `media/channels/vanhiep-tech/<clip>/` and update `media/MANIFEST.json`.
13. Point CapCut to **Mac absolute paths** in `docs/capcut-smoke.md` / `script.md` (`ov-*.mov` only). Never tell the user to import from cloud artifacts.

## Generate gate (fail = rewrite HTML)
| Check | Cutaway `cu-*` | Overlay `ov-*` |
|---|---|---|
| Canvas bg | solid `--vht-bg` | **transparent** — never `#282C34` / glass board on `#main` |
| Zone plate | N/A (full frame is the shot) | **Banned** full-zone frosted/glass. Optional tight `hard-scrim` (uniform opacity OK, DL-070) |
| Piece fills | UI mocks / surfaces OK | Badges / chrome OK; backdrop = `hard-scrim` or CapCut `a-roll-blur`, never CSS blur |
| Outside pieces | painted brand void OK | **alpha = 0** (hard edges) |
| Soft glow | OK on cutaway | **Banned** — no `box-shadow` / `text-shadow` / `filter:blur` / `drop-shadow` |
| Soft-alpha budget | N/A | Mid-frame sampled semi-alpha **&lt; 3%** (see step 10) |
| Face safe zone | N/A | Prefer title/L3 bands; do not park big cards over face/chest |
| Depth without glow | grid / solid fills | Hard `border` + opaque `--vht-surface` only |
| Deliverable | `.mp4` on Mac `media/` | ProRes `.mov` (`yuva*`) on Mac `media/` |
| CapCut source | local Mac path | local Mac path — **not** cloud artifacts |
| User preview | `.mp4` as-is | alpha file on Mac (WebP/APNG/MOV) — never plate-composited MP4 |
| Creative | real UI/flow, depth, video type scale | same + talking-head safe zones |

## Known mistakes (do not repeat — DL-069)
| Symptom in CapCut | False fix | Real cause | Correct fix |
|---|---|---|---|
| Misty / white / blue halo around cards | `remove-background` on overlay | Soft `box-shadow` / `text-shadow` baked semi-alpha into ProRes | Delete soft shadows; hard border only; re-render `--format mov` |
| “Still has background” but `pix_fmt=yuva*` + corners clear | Re-run matting | Soft-alpha % still high (~9–12%) | Enforce &lt;3% semi-alpha gate |
| Overlay looks like thin text card vs `ov-d01` | Accept | Label-card design, not UI pieces | Build floating UI (toast / JWT / phone) like diagram layers |
| Timeline jumps / overlays slide left | Ignore | `cu-*` on side track → main-track gap; CapCut magnetic track collapses | Put `cu-*` on **same main track** as A between A clips (`make-capcut-draft`) |
| Preview “has bg” in chat/MP4 | Panic | MP4 cannot carry alpha | Never ship plate-composited MP4 as the overlay asset |

## Backdrop option (tách motion khỏi A-roll — DL-070)

Khi UI khó đọc trên áo / background busy, chọn **một** mode. Ghi trong `script.md` marker hoặc HTML comment `<!-- backdrop: hard-scrim -->`.

| Mode | Làm gì | Không làm |
|---|---|---|
| `none` (default) | Chỉ piece hard-edge | — |
| `hard-scrim` | Tấm `--vht-bg` / `--vht-surface` + hard `border`, **ôm sát** cluster, `z` dưới pieces. Default `opacity: 0.82` (uniform). Alpha ngoài scrim = 0 | Full-bleed frosted board; `backdrop-filter` / `filter:blur` / soft shadow; feathered edges |
| `a-roll-blur` | Blur/dim **track A-roll** trong bbox (CapCut mask, hoặc plate `boxblur` riêng dưới overlay) | Blur bake vào `ov-*.mov` |

```html
<!-- backdrop: hard-scrim · padding DL-071 -->
<div id="cluster"><!-- outer: L56 R140 · bottom≥420 · near lower φ≈1187 -->
  <div id="scrim" data-backdrop="hard-scrim"></div>
  <div id="inner"><!-- padding:40 · gap:24 --></div>
</div>
```

```css
/* Cluster height MUST be ≥520 — top:960 + bottom:380 ≈ 580. Never top:1120+bottom:420. */
#cluster{ position:absolute; left:56px; right:100px; top:960px; bottom:380px; }
#scrim{
  position:absolute; inset:0;
  border-radius:32px; border:3px solid var(--vht-border);
  background:var(--vht-bg); opacity:0.82; z-index:0;
}
#inner{ position:relative; z-index:1; height:100%; padding:48px; display:flex; flex-direction:column; gap:32px; }
```

Spacing checklist before render: see `frame.md` **Spacing · safe zone · φ** (DL-071). Verify cluster pixel height before shipping.

**Alpha gate với scrim:** corners vẫn `(0,0,0,0)`. Soft-% mid-frame sẽ cao vì plate translucency — OK nếu (1) không `box-shadow`/`blur`, (2) alpha trong scrim **đều**, (3) mép cứng. Fog CapCut = soft edge, không phải plate dim đều.

CapCut `a-roll-blur`: mask hình chữ nhật trùng bbox → Effect Blur trên A-roll. Overlay MOV vẫn hard-edge.

## Design rules
- Brand colors only: `brand-tokens.json` + `tokens.css` + `frame.md`
- Interpret concept as **UI / tokens / flow**, not centered text cards
- **Banned:** pink/magenta/fuchsia; invented hex; left-stripe-only L3; empty void (cutaway); equal card grids; full-zone frosted/glass plates; RGB/MP4-baked overlays; fake-A-roll composite sold as the layer; soft `box-shadow`/`text-shadow`/`blur`/`backdrop-filter` on `ov-*` (CapCut mist — DL-069/070)
- Always motion with varied ease/direction; no chibi / OneUp cam accent
- `talking-head-recut` = layout reference only
- `remove-background` = **A-roll cutout only** — never a substitute for transparent overlay render

## CapCut smoke
See `channels/vanhiep-tech/docs/capcut-smoke.md`.

## Requirements
- Read this skill before acting; follow linked channel/repo AGENTS.md when cited.
- Use tools and paths named in the steps; do not invent alternate pipelines.

## Limitations
- Not comic `make-video`.
- CapCut import source must be local Mac media paths.
- Soft shadows / baked blur on overlays are banned for alpha handoff.

## Troubleshooting
| Error / symptom | Cause | Fix |
|---|---|---|
| Alpha gate fail | Soft shadow or soft-alpha | Strip soft shadows; use hard-scrim |
| Wrong colors | Tokens not synced | Copy brand tokens.css into layer |
| Cloud handoff attempt | Using /opt/cursor/artifacts | Re-render on Mac checkout |
