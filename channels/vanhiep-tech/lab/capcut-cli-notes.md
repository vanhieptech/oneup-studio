---
source: "oneup-studio (soạn trong repo)"
title: "lab — capcut-cli notes"
date: 2026-11-08
id: lab-vht-capcut-cli
type: lab
status: active
updated: 2026-11-08
tags: [vanhiep-tech, capcut-cli, lab]
---
# lab — capcut-cli / cutout bake-off

## Environment (2026-11-08)
- `npx capcut-cli` 0.33.1 — `doctor` OK (Node 24, ffmpeg/ffprobe)
- Drafts: `~/Movies/CapCut/User Data/Projects/com.lveditor.draft`
- Whisper: missing (caption CLI not required V1.1)

## Bake-off log
| Date | Clip | A (HF remove-background) | B (CapCut matting) | Winner | Notes |
|---|---|---|---|---|---|
| 2026-11-08 | vht-20261107-oauth-control-plane | **HF done** — sample `a-roll-cutout-bakeoff-12s.mov` (~6m19s, 700MB, 303ms/f) + full `a-roll-cutout.mov` (1686f, ~8m7s, 3.2GB, 289ms/f, CoreML ProRes) | pending — Desktop `matting` on A segment; compare hair/shoulders vs HF | pending | Real A-roll from `copy_F3329B9A-….MOV`. |

## Compile log
| Date | Spec | Result | Notes |
|---|---|---|---|
| 2026-11-08 | `capcut-spec.json` | `--check` OK | 6 tracks / 7 items |
| 2026-11-08 | → `lab/out/vht-20261107-oauth-control-plane` | OK | CapCut app was open — store write refused (`editor-open`). Re-run with CapCut closed into `--drafts` store. Template seeded 6.5.0 bundled. |
| 2026-11-08 | → `lab/out/…` (recompile) | OK | Real A-roll 56.2s; timeline scaled (cutaway @21s); duration_us=56210000. CapCut still open → stay in lab/out. |
| 2026-11-08 | → CapCut store `…/com.lveditor.draft/vht-20261107-oauth-control-plane` | OK | CapCut closed. Template seed `0324` (app 8.3.0). First write had main-track gap (cutaway on side track) — CapCut would collapse 9s. |
| 2026-11-08 | store recompile (cutaway on A-main) | OK | `cu-01` on same main track between A clips. lint clean (0 issues). 5 tracks / 7 segs / 56.21s. |
| 2026-11-08 | store `vht-20261107-oauth-bakeoff-matting` | OK | Twin draft + `capcut matting` flag=3 on both A-roll segs. Open in Desktop so app computes matte; compare edge vs HF `a-roll-cutout.mov`. |
| 2026-11-08 | overlays redesign + store recompile | OK | `ov-hook`/`ov-q`/`ov-l3` rewritten as floating UI (like `ov-d01`), ProRes `yuva` direct — no remove-bg. CapCut seed now 9.7.1. |
| 2026-11-08 | root-cause: soft shadow → CapCut fog | fixed | `box-shadow`/`text-shadow` baked ~9–12% semi-alpha; CapCut showed misty “background”. Stripped shadows; hard borders only; hook UI moved below face. semi% → ~0.2–1.5%. Store recompiled. |

## Failures / schema
_(append CapCut version + error JSON here)_
