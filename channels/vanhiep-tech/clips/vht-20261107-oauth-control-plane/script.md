---
title: "OAuth control plane — Login button vs Keycloak"
date: 2026-11-07
id: vht-20261107-oauth-control-plane
type: script
status: draft
updated: 2026-11-08
source: "Nordic APIs + Keycloak audience docs + Phase Two aud trap (rewrite)"
tags: [vanhiep-tech, oauth, oidc, keycloak, script]
---
# vht-20261107-oauth-control-plane

## Meta
- **Góc:** Nút login = UX; Keycloak = control plane
- **Punch:** Login OK / API 401 vì `aud`
- **Nguồn:** Nordic APIs · Keycloak Audience · Phase Two aud trap

## Timeline (~60–75s)

| Giây | Marker | Lời (VO — nháp) | Hình |
|---|---|---|---|
| 0:00 | `[0:00 ov-hook]` | Nhiều team nghĩ xong OAuth khi đã có nút «Sign in with…». | A-roll + overlay hook |
| 0:10 | `[0:10 ov-d01]` | Nhưng quyết định bảo mật API không nằm ở nút đó — nằm ở authorization server (Keycloak). | A-roll + overlay diagram |
| 0:28 | `[0:28 cu-01]` | Ai được token, `aud` nào, MFA, TTL, client auth — đã quyết trước khi request tới gateway. | **B-roll cutaway** full |
| 0:48 | `[0:48 ov-q]` | Login Keycloak thành công, API vẫn 401. Không phải API hư — token thiếu `aud` đúng (hay `account`). | A-roll + quote overlay |
| 1:05 | `[1:05 ov-l3]` | Takeaway: identity = control plane, không phải trang login. | A-roll + lower-third |
| 1:15 | | Bạn đang verify `aud` trên từng API chưa? | A-roll CTA |

## Layer package (đủ catalog)

| Id | Vai trò | Canvas | Output | a_roll |
|---|---|---|---|---|
| `ov-hook` | Overlay hook | transparent | `…/ov-hook.mov` | full |
| `ov-d01` | Overlay diagram | transparent | `…/ov-d01.mov` | full |
| `cu-01` | Cutaway B-roll | solid `--vht-bg` | `…/cu-01.mp4` | — (replaces A) |
| `ov-q` | Overlay quote | transparent | `…/ov-q.mov` | full |
| `ov-l3` | Overlay L3 | transparent | `…/ov-l3.mov` | full |

Marker shorthand: `[mm:ss ov-d01 cutout]` khi cần A-cutout.

**CapCut (local Mac):**

```
/Users/macbook/me/projects/oneup-studio/media/channels/vanhiep-tech/vht-20261107-oauth-control-plane/
  a-roll.mp4              # full (thật hoặc placeholder)
  a-roll-cutout.mov       # sau bake-off HF
  cu-01.mp4
  ov-*.mov
```

Compile: `capcut-spec.json` + skill `make-capcut-draft`. Fallback: `docs/capcut-smoke.md` Path B.

## V1 / V1.1 DoD
- [x] Đủ 5 layer + MANIFEST
- [x] `capcut-spec.json` + `compile --check` OK
- [x] Draft compile → `lab/out/` (đóng CapCut rồi đẩy vào store)
- [ ] A-roll thật + bake-off HF vs matting
- [ ] Smoke mở draft trong CapCut Desktop + VO
- [ ] Pilot quay + export = V1.1 done
