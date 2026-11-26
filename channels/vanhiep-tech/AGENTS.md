---
title: "AGENTS — @vanhiep.tech"
date: 2026-11-07
id: agents-vanhiep-tech
type: guide
status: active
updated: 2026-11-26
source: "grill-me plan 2026-11-07"
tags: [agents, vanhiep-tech, talking-head, local]
---
# AGENTS — kênh @vanhiep.tech

Kênh cá nhân (tech / lập trình / kỹ năng / tư duy). **Không** dùng luật comic `@hi.oneup` (DL-027, `make-video`, chibi, F5 voice pipeline OneUp).

## Máy làm việc = **local Mac**
- Repo Mac: `/Users/macbook/work/oneup-studio`
- HyperFrames render, CapCut assemble, A-roll/VO, xem `.mov` — **trên Mac**
- **Cấm** lấy deliverable CapCut từ cloud agent (`/opt/cursor/artifacts`), chat link, hay coi `/workspace` box là máy edit
- Box/cloud agent (nếu còn): chỉ sửa HTML/docs/git; **không** là nguồn import CapCut

## Đọc trước khi làm
1. File này
2. `channels/vanhiep-tech/PLAN.md` (quyết định đã khóa)
3. `brand/brand-tokens.json` + `brand/tokens.css` + **`brand/frame.md`**
4. Skill `channels/vanhiep-tech/skills/make-layer/SKILL.md` (layers)
5. Skill `channels/vanhiep-tech/skills/make-capcut-draft/SKILL.md` (CLI compile + cutout)
6. CapCut: `channels/vanhiep-tech/docs/capcut-smoke.md`
   - **Gate 0 (trước bản nháp v1):** `python3 pipeline/scripts/gate0.py --channel vht --idea "<ý>" [--arc ARC-NNN] [--memo media/voice-memos/<x>.txt] --out channels/vanhiep-tech/clips/<clip-id>/script.md` nạp 4 mảnh: ý tưởng (`content/idea-bank.md`, kể cả ý `@vanhiep.tech` từ teardown) + fact package · mạch `ARC-NNN` với nhịp 45–90s, **cắt layer `ov-*`/`cu-*` mỗi 3–5s** · chi tiết thật (story-bank hoặc transcript ghi âm nói chay, Voice-First ≥ 80% từ của Hiệp) + từ nối `resources/vn-spoken/connectors.tsv` · lưu ý mới nhất `resources/feedback.md` + `rules/ACTIVE-CHECKLIST.md` §3. Mảnh nào «chưa có» thì đi lấy, không bịa.
   - Viết lời: prompt `docs/prompts/writer-vanhiep-tech.md` (3 hook, bảng mốc · overlay/marker · lời) + `docs/research/craft-brief.md`
   - Audio-Back QA (trước Gate 1 / trước khi quay A-roll & thu VO): `python3 pipeline/scripts/audio-precheck.py channels/vanhiep-tech/clips/<clip-id>/script.md` kiểm nhịp nói tiếng Việt (2.6–3.4 âm tiết/giây), câu > 22 âm tiết thiếu dấu ngắt nhịp `,` / `—` / `...`, và trùng cấu trúc mở đầu giữa 2 beat liên tiếp (tùy chọn `--audition-hook` để nghe thử 20s đầu).
   - Review lời: 2 tầng như `@hi.oneup` — Tầng 1 Hard-Gate (`H1–H4`, trong đó H3 = sai format kênh này: quá 90s, chibi/luật comic, overlay có shadow/blur DL-069, hồng/magenta) là cổng chặn duy nhất; Tầng 2 so sánh cặp Pairwise A/B với bản đã duyệt gần nhất; khẩu ngữ tự nhiên không bị trừ.
   - Cắt video dài thành short: `channels/vanhiep-tech/skills/shorts-cutter/SKILL.md` (cổng bản quyền, Hiệp chọn đoạn, ra `a-roll.mp4` cho pipeline CapCut)
7. HyperFrames: router → creative → animation / motion-graphics → talking-head-recut (**layout only**) · cutout: `remove-background`

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
1. Viết `clips/vht-YYYYMMDD-<slug>/script.md` + marker + cột `a_roll`
2. Mac: HyperFrames layers → `media/channels/vanhiep-tech/<clip-id>/`
3. Mac: đặt `a-roll.mp4`; bake-off cutout → `a-roll-cutout.mov` (`make-capcut-draft`)
4. `capcut-cli compile` từ `capcut-spec.json` → CapCut store (hoặc `lab/out/` nếu app đang mở)
5. CapCut Desktop: refine + VO + export
6. Cutaway `cu-*` → `.mp4`; Overlay `ov-*` → `.mov` alpha, **no soft shadow/blur** (DL-069); optional opaque `hard-scrim` / CapCut `a-roll-blur` (DL-070)
7. Cấm hồng / magenta / fuchsia
8. `remove-background` chỉ cho A-roll cutout — **không** dùng để “sửa” overlay

## Media
| Loại | Chỗ |
|---|---|
| Source / script / HTML / spec | `channels/vanhiep-tech/` (git) |
| Layer + A-roll renders | `media/channels/vanhiep-tech/<clip>/` (gitignore + MANIFEST) |
| CLI draft scratch | `channels/vanhiep-tech/lab/out/` (gitignored) |
| CapCut app drafts | `~/Movies/CapCut/User Data/Projects/com.lveditor.draft` |
| VO | local Mac only |

Mac: `/Users/macbook/me/projects/oneup-studio/media/channels/vanhiep-tech/<clip-id>/`

## Brand + design (generate)
- Tokens: `brand-tokens.json` + `tokens.css` + `frame.md` + generate gate trong `make-layer`
- Overlay: canvas transparent; cấm glass board; piece fill + **hard border** OK; **cấm** `box-shadow` / `text-shadow` / blur (CapCut = halo sương — DL-069)
- Verify ov: `yuva*` + corners clear + soft-alpha mid-frame **&lt; 3%**
- Preview giữ alpha — cấm bake MP4 plate
- Safe-zone 1080×1920 · Be Vietnam Pro · Không logo / chibi / cam OneUp
- UI overlays: floating pieces như `ov-d01` (toast/JWT/phone) — không text-card mỏng

## Cấm
- `skills/make-video` comic cho kênh này
- Vendor footage mặt lên git/cloud
- CapCut từ cloud artifact / box path
- Phụ thuộc CLI `render`/`export` làm bản ship (Desktop mới export)
- Composite full talking-head-recut thay CapCut (HF cutout A-roll OK)
- Soft shadow / blur trên `ov-*`; `remove-background` trên overlay ProRes
- `cu-*` trên side track (main-track gap — CapCut kéo timeline)
