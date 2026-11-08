---
title: "@vanhiep.tech layer frame"
date: 2026-11-08
palette: one-dark
bg: "#282C34"
fg: "#ABB2BF"
accent: "#56B6C2"
accentAlt: "#61AFEF"
warn: "#E5C07B"
ok: "#98C379"
danger: "#E06C75"
title: "#FFFFFF"
font: "Be Vietnam Pro"
aspect: "9:16"
safeZone: "top 220 / bottom 380 / left 56 / right 140"
tokens: "brand/tokens.css"
---

# Frame — layer graphics @vanhiep.tech

Hard rules for **every** generate. Skill: `channels/vanhiep-tech/skills/make-layer/SKILL.md`.

## Must (from hyperframes-creative)
- Interpret concept → **real UI / real tokens / real flow**, not label cards
- Cutaway density: background treatment + midground content + foreground accents
- Type at video scale (headlines ≥64px on cutaway; overlay titles ≥40px)
- Ambient motion on decoratives; entrance choreography with **varied** ease/direction
- Brand hex only (`tokens.css`) — never invent; never pink/magenta

## Lazy defaults to avoid
- Left-edge accent stripe as the only design idea
- Identical equal card grids with equal weight
- Empty dark void behind cutaway content
- Pure web “centered card on blank”
- Cyan glow at 5% opacity (must be visible on video)
- **Overlay glass / frosted board** filling a zone (looks like “still has background”)

## Cutaway (`cu-*`)
Full-frame solid `--vht-bg`. Depth: grid + radial accent glow + ghost type. Asymmetric split UX vs control plane. Story readable with sound off. Deliver `.mp4`.

## Overlay (`ov-*`) — generate rules
1. `html, body, #main { background: transparent !important; }`
2. **No plate:** do not draw a full-width/full-zone rounded rect behind the whole graphic.
3. Only **piece** fills (badge, button, phone chrome, token chip). Type may use text-shadow for legibility.
4. Outside pieces → alpha **0**. Mid-frame corner pixels must be `(0,0,0,0)`.
5. Deliverable for CapCut: ProRes `.mov` on **local Mac** `media/channels/vanhiep-tech/<clip>/` (`pix_fmt` contains `yuva`). Not cloud artifacts.
6. Human watch preview: **keep alpha** (WebP/APNG/MOV) on Mac.  
   **Do not** composite onto fake A-roll / One Dark into MP4 — MP4 cannot be transparent, so that preview always “still has background”.
7. Never ship RGB-flattened PNG/MP4 as the CapCut overlay asset.
