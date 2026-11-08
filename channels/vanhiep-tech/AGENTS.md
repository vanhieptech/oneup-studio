---
title: "AGENTS — @vanhiep.tech"
date: 2026-11-07
id: agents-vanhiep-tech
type: guide
status: active
updated: 2026-11-08
source: "grill-me plan 2026-11-07"
tags: [agents, vanhiep-tech, talking-head, local]
---
# AGENTS — kênh @vanhiep.tech

Kênh cá nhân (tech / lập trình / kỹ năng / tư duy). **Không** dùng luật comic `@hi.oneup` (DL-027, `make-video`, chibi, F5 voice pipeline OneUp).

## Máy làm việc = **local Mac**
- Repo Mac: `/Users/macbook/me/projects/oneup-studio`
- HyperFrames render, CapCut assemble, A-roll/VO, xem `.mov` — **trên Mac**
- **Cấm** lấy deliverable CapCut từ cloud agent (`/opt/cursor/artifacts`), chat link, hay coi `/workspace` box là máy edit
- Box/cloud agent (nếu còn): chỉ sửa HTML/docs/git; **không** là nguồn import CapCut

## Đọc trước khi làm
1. File này
2. `channels/vanhiep-tech/PLAN.md` (quyết định đã khóa)
3. `brand/brand-tokens.json` + `brand/tokens.css` + **`brand/frame.md`**
4. Skill `channels/vanhiep-tech/skills/make-layer/SKILL.md`
5. CapCut paths: `channels/vanhiep-tech/docs/capcut-smoke.md`
6. HyperFrames: router → creative → animation / motion-graphics → talking-head-recut (**layout only**)

## Format video
- A-roll tự quay + VO riêng, sync trong **CapCut Desktop (Mac)**
- Hybrid: overlay trên mặt; cutaway full khi cần
- Master **9:16** · short **45–90s** (V1)
- Không chibi — diagram trung tính
- Layer deliverable = video có motion

## Catalog layer
| Id prefix | Loại | Ghi chú V1 |
|---|---|---|
| `ov-hook` | title / hook | optional |
| `ov-dNN` | diagram explainer | **bắt buộc 1–2** |
| `cu-NN` | cutaway solid | optional ≤1 |
| `ov-l3` | lower-third | optional ≤1 |
| `ov-q` | quote / callout | optional ≤1 |

## Pipeline (local-first)
1. Viết `clips/vht-YYYYMMDD-<slug>/script.md` + marker `[mm:ss layer-id]`
2. Trên **Mac**: HyperFrames render → `media/channels/vanhiep-tech/<clip-id>/`
3. CapCut: import `.mov`/`.mp4` từ path Mac tuyệt đối (xem `docs/capcut-smoke.md`)
4. Cutaway `cu-*` → `.mp4` solid `--vht-bg`; Overlay `ov-*` → `.mov` ProRes alpha, **no plate**
5. Cấm hồng / magenta / fuchsia

## Media
| Loại | Chỗ |
|---|---|
| Source / script / HTML | `channels/vanhiep-tech/` (git) |
| Layer renders | `media/channels/vanhiep-tech/` trên **Mac** (gitignore + MANIFEST) |
| A-roll, VO, CapCut project | **chỉ local Mac** — không git, không cloud |

Mac path mẫu:

`/Users/macbook/me/projects/oneup-studio/media/channels/vanhiep-tech/<clip-id>/`

## Brand + design (generate)
- Tokens: `brand-tokens.json` + `tokens.css` + `frame.md` + generate gate trong `make-layer`
- Overlay: canvas transparent, cấm glass board; piece fill OK; preview giữ alpha — cấm bake MP4 plate
- Safe-zone 1080×1920 · Be Vietnam Pro · Không logo / chibi / cam OneUp

## Cấm
- `skills/make-video` comic cho kênh này
- Vendor footage mặt lên git/cloud
- CapCut từ cloud artifact / box path
- Phụ thuộc `capcut-cli` để ship V1
- Composite full A-roll trong HyperFrames
