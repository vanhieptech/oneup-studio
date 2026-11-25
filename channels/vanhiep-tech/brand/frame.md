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
safeZone: "top 220 / bottom 420 / left 56 / right 140"
tokens: "brand/tokens.css"
updated: 2026-11-08
---

# Frame — layer graphics @vanhiep.tech

Hard rules for **every** generate. Skill: `channels/vanhiep-tech/skills/make-layer/SKILL.md` (DL-069 · DL-070 · DL-071).

## Spacing · safe zone · φ (1080×1920) — DL-071

Sources: Vibeboard 9:16 placement · WaveSpeed safe presets · OD2 Reels margins · channel prior `safeZone`.

| Rule | Value @ 1080×1920 | Why |
|---|---|---|
| Top clear | ≥ **220** (≈11.5%) | Status / tabs |
| Bottom clear | ≥ **420** (≈22%) | Caption / sound / progress |
| Left clear | ≥ **56** (≈5%) | Edge bleed |
| Right clear | ≥ **140** (≈13%) | Like/share rail |
| Upper φ line | **y ≈ 733** | Face / eyes |
| Lower φ line | **y ≈ 1187** | Payoff / overlay cluster |
| 8-pt grid | 8 · 16 · 24 · 32 · **40** · 48 · 64 | All pad/gap |
| Outer → scrim | L≥56 · R≥100 · bottom clear ≥380 | Never hug canvas / button rail |
| Scrim → content (**inner pad**) | **48** all sides (min 40) | Content never flush to scrim border |
| Gap between pieces | **32** (min 24) | Phone / cards / chips |
| Title → scene | **32** | Hierarchy breath |
| **Cluster min height** | ≥ **520** (prefer ~560–600) | `top + bottom` must leave room — **do not** use top≈1120 + bottom≈420 (→ ~380px crush) |

**Overlay cluster:** start ≈960–1000 (below face), end above bottom 380–420. Usable height ≈560+. Inner pad 48 + gap 32. Scene `min-height ≥ 280`.

**Banned spacing:** flush-to-edge text; pad &lt; 24; zero inner pad; **short cluster** that compresses padding; parking UI in bottom 420 or right 140.

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
- **Soft `box-shadow` / `text-shadow` / `filter:blur` / `drop-shadow` on overlays** — bakes semi-alpha fog; CapCut reads it as leftover background / halo around every piece (DL-069)
- Parking big overlay cards over face/chest (use lower / title bands from `safeZone`)

## Cutaway (`cu-*`)
Full-frame solid `--vht-bg`. Depth: grid + radial accent glow + ghost type. Asymmetric split UX vs control plane. Story readable with sound off. Deliver `.mp4`. Soft glow **allowed** here (opaque plate).

## Overlay (`ov-*`) — generate rules
1. `html, body, #main { background: transparent !important; }`
2. **No full-zone plate:** do not draw a full-width frosted/glass board covering the safe zone.
3. Only **piece** fills (badge, button, phone chrome, token chip) with **hard borders**. Depth = border + opaque `--vht-surface`, not blur.
4. **No soft shadow / blur** on `ov-*` CSS (`box-shadow` / `text-shadow` / `filter:blur` / `backdrop-filter` / `drop-shadow`). Legibility = contrast + piece fill.
5. Outside pieces → alpha **0**. Mid-frame corners `(0,0,0,0)` **and** sampled soft-alpha **&lt; 3%** (see `make-layer` verify step).
6. Deliverable for CapCut: ProRes `.mov` on **local Mac** `media/channels/vanhiep-tech/<clip>/` (`pix_fmt` contains `yuva`). Not cloud artifacts.
7. Human watch preview: **keep alpha** (WebP/APNG/MOV) on Mac.  
   **Do not** composite onto fake A-roll / One Dark into MP4 — MP4 cannot be transparent, so that preview always “still has background”.
8. Never ship RGB-flattened PNG/MP4 as the CapCut overlay asset.
9. Never “fix” overlay fog with `hyperframes remove-background` — that tool is for **A-roll cutout**, not overlay authoring.
10. **Backdrop option (DL-070)** when A-roll fights the UI: `hard-scrim` (tight panel behind cluster; default `opacity: 0.82`, uniform hard edge) and/or CapCut `a-roll-blur` on the A-roll track inside the same bbox. Never bake background blur / soft feather into the overlay MOV.
11. **Padding (DL-071):** scrim must leave **40px** inner pad to content; cluster respects platform safe clear (T220 / B420 / L56 / R140).
