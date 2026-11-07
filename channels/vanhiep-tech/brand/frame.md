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

## Must (from hyperframes-creative)
- Interpret concept → **real UI / real tokens / real flow**, not label cards
- Video density: background treatment + midground content + foreground accents
- Type at video scale (headlines ≥64px on cutaway; overlay titles ≥40px)
- Ambient motion on decoratives; entrance choreography with **varied** ease/direction
- Brand hex only (`tokens.css`) — never invent; never pink/magenta

## Lazy defaults to avoid
- Left-edge accent stripe as the only design idea
- Identical equal card grids with equal weight
- Empty dark void behind content
- Pure web “centered card on blank”
- Cyan glow at 5% opacity (must be visible on video)

## Cutaway (`cu-*`)
Full-frame solid `--vht-bg`. Depth: grid + radial accent glow + ghost type. Asymmetric split UX vs control plane. Story readable with sound off.

## Overlay (`ov-*`)
Transparent canvas. Graphic lives in a **zone** (hook / lower-mid / lower-third / callout). Card/surface uses brand fills; soft depth via offset shadow in brand colors. Designed to sit on talking-head without looking like a website widget.
