---
title: "AGENTS — @vanhiep.tech"
date: 2026-11-07
id: agents-vanhiep-tech
type: guide
status: active
updated: 2026-11-07
source: "grill-me plan 2026-11-07"
tags: [agents, vanhiep-tech, talking-head]
---
# AGENTS — kênh @vanhiep.tech

Kênh cá nhân (tech / lập trình / kỹ năng / tư duy). **Không** dùng luật comic `@hi.oneup` (DL-027, `make-video`, chibi, F5 voice pipeline OneUp).

## Đọc trước khi làm
1. File này
2. `channels/vanhiep-tech/PLAN.md` (quyết định đã khóa)
3. `brand/brand-tokens.json` + `brand/tokens.css` + **`brand/frame.md`** (density / UI / zones)
4. Skill `channels/vanhiep-tech/skills/make-layer/SKILL.md` khi tạo/render layer
5. HyperFrames (bắt buộc trước HTML):
   - Router `skills/hyperframes/hyperframes/SKILL.md`
   - Creative `skills/hyperframes/hyperframes-creative/` (`house-style`, `video-composition`, `composition-patterns`, `motion-principles`)
   - Motion `skills/hyperframes/hyperframes-animation/` + `skills/hyperframes/motion-graphics/` (lower-thirds)
   - Overlay zones: `skills/hyperframes/talking-head-recut/` (**layout only**)

## Format video
- A-roll tự quay + VO riêng, sync trong **CapCut Desktop**
- Hybrid: overlay trên mặt khi giải thích; cutaway full khi cần thấy rõ
- Master **9:16** · short **45–90s** (V1)
- Không nhân vật chibi — diagram / icon / doodle trung tính
- Mọi layer deliverable = **video có motion** (không thả PNG tĩnh làm shot cuối)

## Catalog layer (id trong script)
| Id prefix | Loại | Ghi chú V1 |
|---|---|---|
| `ov-hook` | title / hook card | optional ngoài budget tối thiểu |
| `ov-dNN` | diagram explainer (overlay) | **bắt buộc 1–2** |
| `cu-NN` | cutaway full, nền solid | optional ≤1 |
| `ov-l3` | lower-third / label | optional ≤1 |
| `ov-q` | quote / callout | optional ≤1 |

Budget short V1: **bắt buộc** hook cảm (có thể làm trong CapCut) + **1–2 diagram**; cutaway / L3 / quote ≤1 mỗi loại.

## Pipeline
1. Viết `clips/vht-YYYYMMDD-<slug>/script.md` với marker `[mm:ss layer-id]`
2. Pre-render layer phức tạp bằng HyperFrames → `media/channels/vanhiep-tech/<clip-id>/`
3. Motion đơn (fade/scale) có thể làm trong CapCut từ SVG/PNG đã animate nhẹ
4. Ghép CapCut: A-roll + VO + layers theo marker
5. **Hai kiểu render:**
   - **Cutaway / B-roll (`cu-*`)**: full-frame solid `var(--vht-bg)` → `--format mp4`
   - **Overlay (`ov-*`)**: canvas **transparent**, card/bar dùng màu brand → `--format mov` (ProRes alpha)
6. **Cấm** hồng / magenta / fuchsia (kể cả nền preview)

## Media
| Loại | Chỗ |
|---|---|
| Source / script / HTML layer | `channels/vanhiep-tech/` (git) |
| Render layer (mov/webm/mp4) | `media/channels/vanhiep-tech/` (gitignore + MANIFEST) |
| A-roll, VO, CapCut draft | **chỉ local Mac** — không lên git/box |

## Brand + design
- **Nguồn màu duy nhất:** `brand/brand-tokens.json` + `brand/tokens.css` (`--vht-*`)
- **Frame / density:** `brand/frame.md` — UI thật / token / flow, depth bg+mid+fg, type video-scale, zones overlay
- **Luôn** dùng token đã định nghĩa — **cấm** bịa hex ngoài file token
- Cutaway: full-frame `var(--vht-bg)` + atmosphere. Overlay: transparent canvas + surface brand trong safe zone
- **Cấm** hồng / magenta / fuchsia; left-stripe-only L3; empty void; equal text-card grids
- Safe-zone 1080×1920 · Font Be Vietnam Pro · Không logo / chibi / cam OneUp

## Cấm
- `skills/make-video` comic cho clip kênh này
- Vendor footage mặt vào repo
- Phụ thuộc `capcut-cli` để ship V1 (chỉ `doctor` / experiment)
- Composite full A-roll trong HyperFrames (`talking-head-recut` chỉ tham khảo layout)
