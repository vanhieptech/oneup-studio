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

| Id | Vai trò | Canvas | Output |
|---|---|---|---|
| `ov-hook` | Overlay hook card | transparent + card brand | `…/ov-hook.mov` (ProRes alpha) |
| `ov-d01` | Overlay diagram compact | transparent + cards | `…/ov-d01.mov` |
| `cu-01` | **B-roll / cutaway** full visual | solid `--vht-bg` | `…/cu-01.mp4` |
| `ov-q` | Overlay quote `aud` trap | transparent + card | `…/ov-q.mov` |
| `ov-l3` | Overlay lower-third | transparent + bar | `…/ov-l3.mov` |

**CapCut (local Mac only):**

```
/Users/macbook/me/projects/oneup-studio/media/channels/vanhiep-tech/vht-20261107-oauth-control-plane/
  cu-01.mp4
  ov-hook.mov
  ov-d01.mov
  ov-l3.mov
  ov-q.mov
```

Overlays = track Overlay (alpha); `cu-01` = B-roll full frame. **Không** import từ cloud/`/opt/cursor/artifacts`.

## V1 DoD
- [x] Đủ 5 kịch bản layer (hook · diagram overlay · cutaway · quote · L3)
- [x] Render outputs + MANIFEST (sync/`media-sync` về Mac)
- [ ] Smoke CapCut trên Mac (path local ở trên)
- [ ] Pilot quay + ghép = V1.1
