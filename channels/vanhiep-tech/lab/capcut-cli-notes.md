---
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
| 2026-11-08 | vht-20261107-oauth-control-plane | blocked — placeholder slate only | blocked | — | Replace `media/.../a-roll.mp4` with real talking-head then rerun |

## Compile log
| Date | Spec | Result | Notes |
|---|---|---|---|
| 2026-11-08 | `capcut-spec.json` | `--check` OK | 6 tracks / 7 items |
| 2026-11-08 | → `lab/out/vht-20261107-oauth-control-plane` | OK | CapCut app was open — store write refused (`editor-open`). Re-run with CapCut closed into `--drafts` store. Template seeded 6.5.0 bundled. |

## Failures / schema
_(append CapCut version + error JSON here)_
