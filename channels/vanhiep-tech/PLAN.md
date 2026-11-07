---
title: "PLAN — @vanhiep.tech V1 scaffold"
date: 2026-11-07
id: plan-vanhiep-tech-v1
type: plan
status: active
updated: 2026-11-07
source: "grill-me 2026-11-07"
tags: [plan, vanhiep-tech, v1]
---
# PLAN — @vanhiep.tech V1

Quyết định khóa từ grill-me (2026-11-07). Không đổi lặng lẽ — ghi revision nếu đổi.

## Quyết định
1. Kênh cá nhân `@vanhiep.tech` (không phải `@hi.oneup`)
2. Hybrid: A-roll + overlay + cutaway
3. Không chibi — diagram trung tính
4. CapCut Desktop = NLE cuối
5. Deliverable layer luôn có motion
6. Motion đơn → CapCut; multi-step → HyperFrames pre-render
7. Cutaway = solid MP4; overlay = ProRes alpha (canvas trong suốt, card brand); **cấm** hồng/magenta
8. Sống trong `channels/vanhiep-tech/`
9. HF chỉ xuất layer; brand **One Dark** (`#282C34` / `#56B6C2` / …) — xem `brand/brand-tokens.json`
10. V1: script + id layer; STT-auto sau 2–3 clip
11. `capcut-cli`: doctor/experiment only
12. Master 9:16 · short 45–90s
13. Catalog 5 loại; budget: hook + 1–2 diagram bắt buộc
14. Isolation: AGENTS kênh + pointer root
15. DoD V1: scaffold + `ov-d01` mẫu + smoke CapCut; pilot full = V1.1
16. VI nói + VI overlay
17. Audio: hình + VO riêng sync CapCut
18. Media: layer → `media/channels/...`; A-roll local Mac
19. Id clip: `vht-YYYYMMDD-<slug>`

## Pilot nội dung
- Id: `vht-20261107-oauth-control-plane`
- Xương: Login button (UX) vs Keycloak = control plane
- Punch: login OK / API 401 vì `aud` (bẫy `account`)
- Nguồn rewrite: [Nordic APIs](https://nordicapis.com/oauth-and-oidc-beyond-the-login-button-identity-as-the-api-security-control-plane/) + Keycloak audience docs + Phase Two aud trap
- Layer mẫu V1: `ov-d01` (diagram 2 cột)

## Ngoài scope V1
Mid-form · dual ratio · talking-head-recut composite · CLI compile draft · transcript-auto · đăng pilot đầy đủ

## Revisions
| Date | Note |
|---|---|
| 2026-11-07 | Khóa grill-me + scaffold V1 |
| 2026-11-07 | Render `ov-d01.mov` ProRes 4444 (yuva444p12le) trên box; chờ smoke CapCut trên Mac |
| 2026-11-07 | Đổi palette → One Dark (user swatch); re-render `ov-d01` |
| 2026-11-07 | Layer luôn solid bg; cấm hồng/magenta; render MP4 |
| 2026-11-07 | Bắt buộc dùng brand tokens / `--vht-*` — không bịa hex |
| 2026-11-07 | ov-d01 redesign: minh họa visual (browser login + Keycloak→token→API) |
| 2026-11-08 | Đủ catalog: cu-01 B-roll + ov-hook / ov-d01 / ov-l3 / ov-q overlays |
