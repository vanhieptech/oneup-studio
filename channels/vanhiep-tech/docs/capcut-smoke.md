---
title: "CapCut smoke — local Mac only"
date: 2026-11-08
id: docs-vht-capcut-smoke
type: guide
status: active
updated: 2026-11-08
source: "channels/vanhiep-tech PLAN"
tags: [capcut, vanhiep-tech, local]
---
# CapCut smoke — **local Mac only**

**Không** dùng cloud agent `/opt/cursor/artifacts`, box path `/workspace/...`, hay link chat làm nguồn CapCut.
Mọi import CapCut lấy file trên **Mac local** sau khi media đã sync về repo.

## Repo Mac
`/Users/macbook/me/projects/oneup-studio`

## CapCut import (đường dẫn tuyệt đối)
Thư mục clip:

`/Users/macbook/me/projects/oneup-studio/media/channels/vanhiep-tech/vht-20261107-oauth-control-plane/`

| File | Track CapCut |
|---|---|
| `cu-01.mp4` | Main / B-roll cutaway full |
| `ov-hook.mov` | Overlay (ProRes alpha) |
| `ov-d01.mov` | Overlay (ProRes alpha) |
| `ov-l3.mov` | Overlay (ProRes alpha) |
| `ov-q.mov` | Overlay (ProRes alpha) |

Đường dẫn đầy đủ:

```
/Users/macbook/me/projects/oneup-studio/media/channels/vanhiep-tech/vht-20261107-oauth-control-plane/cu-01.mp4
/Users/macbook/me/projects/oneup-studio/media/channels/vanhiep-tech/vht-20261107-oauth-control-plane/ov-hook.mov
/Users/macbook/me/projects/oneup-studio/media/channels/vanhiep-tech/vht-20261107-oauth-control-plane/ov-d01.mov
/Users/macbook/me/projects/oneup-studio/media/channels/vanhiep-tech/vht-20261107-oauth-control-plane/ov-l3.mov
/Users/macbook/me/projects/oneup-studio/media/channels/vanhiep-tech/vht-20261107-oauth-control-plane/ov-q.mov
```

## Sync media về Mac (nếu file chưa có)
Từ box chỉ **pack**; unpack + CapCut trên Mac:

```bash
# box (optional pack)
python3 pipeline/scripts/media-sync.py pack

# Mac — sau khi có part.* trong .git/media-sync/
python3 pipeline/scripts/media-sync.py unpack
python3 pipeline/scripts/media-sync.py verify
```

Ưu tiên: **render HyperFrames trực tiếp trên Mac** vào `media/channels/vanhiep-tech/<clip-id>/` — khỏi cloud.

## Test nhanh (Mac + CapCut Desktop)
1. Project 9:16 · A-roll local (không upload cloud)
2. Import 4 file `.mov` từ đường dẫn Mac ở trên → Overlay — quanh graphic phải thấy A-roll
3. Import `cu-01.mp4` đoạn cutaway
4. Fail alpha → ghi `PLAN.md` Revisions; tạm MP4 solid brand (không hồng)

## Alpha
- Deliverable CapCut = `.mov` ProRes (`yuva*`) trên đĩa Mac.
- QuickTime đen quanh graphic = viewer, không phải bake nền.
- Cấm glass plate zone; cấm bán MP4 flatten làm overlay.
