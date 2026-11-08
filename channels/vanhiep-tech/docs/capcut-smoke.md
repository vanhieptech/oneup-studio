---
title: "CapCut smoke — B-roll + overlays"
date: 2026-11-08
id: docs-vht-capcut-smoke
type: guide
status: draft
updated: 2026-11-08
source: "channels/vanhiep-tech PLAN"
tags: [capcut, vanhiep-tech]
---
# CapCut smoke — đủ kịch bản

**Cấm** nền preview hồng/magenta. Dùng màu brand hoặc A-roll thật.

## Outputs (sau sync media)
`media/channels/vanhiep-tech/vht-20261107-oauth-control-plane/`

| File | Dùng trong CapCut |
|---|---|
| `cu-01.mp4` | **B-roll**: cắt full frame thay A-roll |
| `ov-hook.mov` | Overlay track (alpha) |
| `ov-d01.mov` | Overlay track (alpha) |
| `ov-q.mov` | Overlay track (alpha) |
| `ov-l3.mov` | Overlay track (alpha) |

## Test nhanh
1. Project 9:16 · thả A-roll (hoặc solid `--vht-bg` tạm)
2. Import 4 file `.mov` lên Overlay — quanh card phải thấy A-roll/nền dưới
3. Import `cu-01.mp4` trên main track đoạn `[0:28]` — full cutaway
4. Fail alpha ProRes → báo trong `PLAN.md` Revisions; tạm scale card MP4 solid (không dùng hồng)

## Render lại
Xem `skills/make-layer/SKILL.md` — cutaway `mp4`, overlay `mov`.

## Alpha note
- Overlay deliverable = `.mov` ProRes (`yuva*`). Outside graphic pieces, alpha=0.
- QuickTime / many players composite alpha on **black** — that black is *viewer*, not baked bg.
- CapCut: put `.mov` on a track above A-roll.
- **Never** send plate-composited MP4 (fake A-roll / One Dark bake) as the overlay — MP4 has no alpha so it always “still has background”. Human preview = WebP/APNG with alpha or the `.mov`.
- Glass plate / full-zone board is banned (`brand/frame.md`).
