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

## Timeline (A-roll 56.2s — scaled từ plan 75s)

| Giây | Marker | Lời (VO — nháp) | Hình / motion |
|---|---|---|---|
| 0:00 | `[0:00 ov-hook]` · 7.5s · `backdrop:hard-scrim` | Nhiều team nghĩ xong OAuth khi đã có nút «Sign in with…». | Phone Sign-in → myth ✓ → bust ✕ |
| 0:08 | `[0:08 ov-d01]` · 12s · `backdrop:hard-scrim` | Nhưng quyết định bảo mật API không nằm ở nút đó — nằm ở authorization server (Keycloak). | UX ✕ → Keycloak plane → APIs |
| 0:21 | `[0:21 cu-01]` · 15s | Ai được token, `aud` nào, MFA, TTL, client auth — đã quyết trước khi request tới gateway. | **B-roll** 5 quyết định + gateway |
| 0:36 | `[0:36 ov-q]` · 12s · `backdrop:hard-scrim` | Login Keycloak thành công, API vẫn 401. Không phải API hư — token thiếu `aud` đúng (hay `account`). | Login✓ → 401 → JWT aud=`account` |
| 0:49 | `[0:49 ov-l3]` · 7s · `backdrop:hard-scrim` | Takeaway: identity = control plane, không phải trang login. + CTA verify `aud`. | Chips UX/Plane/Gate + CTA |

Optional CapCut: `a-roll-blur` mask trùng bbox scrim (DL-070) nếu còn thấy A-roll lọt mép.

A-roll source: `clips/copy_F3329B9A-….MOV` → `media/.../a-roll.mp4` (1080×1920@30) + `a-roll-source.MOV`.

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
  a-roll.mp4              # full talking-head (from copy_F3329B9A)
  a-roll-source.MOV       # original 4K60 archive
  a-roll-cutout.mov       # HF remove-background (bake-off)
  cu-01.mp4
  ov-*.mov
```

Compile: `capcut-spec.json` + skill `make-capcut-draft`. Fallback: `docs/capcut-smoke.md` Path B.

## V1 / V1.1 DoD
- [x] Đủ 5 layer + MANIFEST
- [x] `capcut-spec.json` + `compile --check` OK
- [x] Draft compile → `lab/out/` + CapCut store (`~/Movies/CapCut/.../vht-20261107-oauth-control-plane`)
- [x] A-roll thật (`a-roll.mp4` 56.2s)
- [x] HF cutout → `a-roll-cutout.mov` (+ 12s bake-off sample)
- [ ] CapCut matting side of bake-off (Desktop) → pick winner
- [ ] Smoke mở draft trong CapCut Desktop + VO
- [ ] Pilot quay + export = V1.1 done
