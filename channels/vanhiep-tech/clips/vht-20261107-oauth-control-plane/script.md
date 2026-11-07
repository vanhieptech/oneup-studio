---
title: "OAuth control plane — Login button vs Keycloak"
date: 2026-11-07
id: vht-20261107-oauth-control-plane
type: script
status: draft
updated: 2026-11-07
source: "Nordic APIs + Keycloak audience docs + Phase Two aud trap (rewrite)"
tags: [vanhiep-tech, oauth, oidc, keycloak, script]
---
# vht-20261107-oauth-control-plane

## Meta
- **Góc:** Nút login = UX; Keycloak / authorization server = control plane API security
- **Punch:** Login OK nhưng API 401 vì `aud` (thường thấy `account`, chưa map API)
- **Nguồn:** [Nordic APIs](https://nordicapis.com/oauth-and-oidc-beyond-the-login-button-identity-as-the-api-security-control-plane/) · [Keycloak Audience](https://github.com/keycloak/keycloak/blob/main/docs/documentation/server_admin/topics/clients/oidc/con-audience.adoc) · [Phase Two aud trap](https://phasetwo.io/tutorials/getting-started/your-first-token/)

## Timeline (~60–75s)

| Giây | Marker | Lời (VO — nháp) | Hình |
|---|---|---|---|
| 0:00 | | Nhiều team nghĩ xong OAuth khi đã có nút «Sign in with…». | A-roll |
| 0:08 | `[0:08 ov-d01]` | Nhưng quyết định bảo mật API không nằm ở nút đó. Nó nằm ở authorization server — với mình thường là Keycloak. | Overlay diagram |
| 0:28 | | Ai được token, token cho API nào, xác thực mạnh tới đâu, sống bao lâu, client auth thế nào — đã quyết trước khi request tới gateway. | A-roll + overlay hold |
| 0:48 | | Ví dụ đời thường: login Keycloak thành công, API vẫn 401. Không phải API hư — access token chưa có `aud` đúng (hay gặp mặc định `account`). | A-roll |
| 1:02 | `[1:02 ov-l3]` optional | Takeaway: coi identity như control plane, không như trang login. | A-roll + L3 |
| 1:12 | | Bạn đang verify `aud` trên từng API chưa? | A-roll CTA |

## Layer manifest
| Id | Loại | Path source | Output (sau render) |
|---|---|---|---|
| ov-d01 | diagram | `layers/ov-d01/` | `media/channels/vanhiep-tech/vht-20261107-oauth-control-plane/ov-d01.mov` |
| ov-l3 | lower-third | CapCut text hoặc layer sau | optional V1.1 |

## V1 DoD
- [x] Scaffold + script + `ov-d01` HTML
- [x] Render ProRes `media/.../ov-d01.mov` (yuva444p12le) — **smoke CapCut còn lại trên máy bạn**
- [ ] Pilot quay + ghép = V1.1
