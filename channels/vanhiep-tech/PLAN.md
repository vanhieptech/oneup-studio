---
title: "PLAN — @vanhiep.tech V1 / V1.1"
date: 2026-11-07
id: plan-vanhiep-tech-v1
type: plan
status: active
updated: 2026-11-08
source: "grill-me 2026-11-07 + 2026-11-08 CapCut CLI"
tags: [plan, vanhiep-tech, v1]
---
# PLAN — @vanhiep.tech V1 / V1.1

Quyết định khóa từ grill-me. Không đổi lặng lẽ — ghi revision nếu đổi.

## Quyết định
1. Kênh cá nhân `@vanhiep.tech` (không phải `@hi.oneup`)
2. Hybrid: A-roll + overlay + cutaway
3. Không chibi — diagram trung tính
4. CapCut Desktop = NLE / export cuối
5. Deliverable layer luôn có motion
6. Motion đơn → CapCut; multi-step → HyperFrames pre-render
7. Cutaway = solid MP4; overlay = ProRes alpha (**no zone plate**); **cấm** hồng/magenta
8. Sống trong `channels/vanhiep-tech/`
9. HF xuất layer (+ cutout A-roll); brand **One Dark** — `brand/brand-tokens.json`
10. V1: script + id layer; STT-auto sau 2–3 clip
11. **`capcut-cli` V1.1:** `compile` scaffold draft từ `capcut-spec.json` = **allowed**; Desktop refine + export. `render`/`export` CLI không phải delivery. Doctor vẫn bắt buộc trước session.
12. Master 9:16 · short 45–90s
13. Catalog 5 loại; budget: hook + 1–2 diagram bắt buộc
14. Isolation: AGENTS kênh + pointer root
15. DoD V1: scaffold + layers + smoke; pilot full = V1.1
16. VI nói + VI overlay
17. Audio: hình + VO riêng sync CapCut (**VO không trong compile**)
18. Media + CapCut: **local Mac only** — `/Users/macbook/me/projects/oneup-studio`
19. Id clip: `vht-YYYYMMDD-<slug>`
20. Không dùng `/opt/cursor/artifacts` / box làm nguồn CapCut
21. Dual A-roll: `a-roll.mp4` + `a-roll-cutout.mov` trong `media/channels/vanhiep-tech/<clip>/` + MANIFEST
22. Cutout default = HF `remove-background`; bake-off vs CapCut `matting` (edge thắng) — skill `make-capcut-draft`
23. Script: cột `a_roll: full|cutout`; marker `[mm:ss ov-d01 cutout]` optional
24. Fail CLI → fallback `docs/capcut-smoke.md` + `lab/capcut-cli-notes.md`
25. Effect sâu trên A-roll = ngoài V1.1 (HF motion chỉ `ov-*`/`cu-*`)

## Pilot nội dung
- Id: `vht-20261107-oauth-control-plane`
- Spec CapCut: `clips/.../capcut-spec.json`
- Skill draft: `skills/make-capcut-draft/SKILL.md`

## Ngoài scope V1.1
Mid-form · dual ratio · talking-head-recut full composite · CLI final export · Whisper caption bắt buộc · deep A-roll FX · đăng pilot

## Revisions
| Date | Note |
|---|---|
| 2026-11-07 | Khóa grill-me + scaffold V1 |
| 2026-11-07 | Render ov-d01 ProRes; palette One Dark; brand tokens only |
| 2026-11-08 | Full layer pack; local Mac only |
| 2026-11-08 | Grill CapCut CLI: compile V1.1 allowed; dual A-roll; cutout bake-off; `make-capcut-draft` |
| 2026-11-08 | `compile --check` OK; draft viết `lab/out/` (CapCut app đang mở — chưa đẩy store). Chờ A-roll thật cho bake-off |
