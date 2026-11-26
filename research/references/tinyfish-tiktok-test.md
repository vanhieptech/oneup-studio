---
title: "TinyFish với TikTok: kết quả thử 26/11/2026"
date: 2026-11-26
id: references.tinyfish-tiktok-test
type: research
status: ready
updated: 2026-11-26
tags: [tinyfish, tiktok, apify, trend]
source: "Thử trực tiếp CLI tinyfish 0.59.0 + MCP TinyFish, 26/11/2026"
---
# TinyFish với TikTok: kết quả thử

| Tính năng | Kết quả | Chi phí |
|---|---|---|
| `search` + `--include-domains tiktok.com` | **Dùng được.** Trả link clip, caption (đoạn trích), ngày đăng. Lần chạy 26/11: 12 link cho 3 truy vấn | 0 (Hobby) |
| `fetch content get` trang clip TikTok (CLI và MCP) | **Bị chặn.** Trả trang «Site Maintenance / Oops! Something went wrong» | 0 |
| `fetch` trang tìm kiếm TikTok | Chỉ có menu, không có clip | 0 |
| `browser session create --browser-profile stealth --proxy-country VN` | **Chưa chạy.** Lệnh bị bộ phân loại an toàn của Claude Code (auto mode) từ chối với lý do «Unauthorized Access»; không có session nào được tạo, không tốn tiền | 0 |
| `agent run` | Không thử (đắt hơn, 0,016 USD/bước) | — |

## Kết luận dùng trong pipeline
- TinyFish = **tìm** clip (`pipeline/scripts/tinyfish_client.py tiktok …`), miễn phí.
- Apify = **đo** clip đã tìm (số liệu, phụ đề, comment): `pipeline/scripts/apify-run.py --urls-from …`. Lần chạy 26/11: 10 clip, 8 phụ đề, comment 3 clip, 0,038 USD.
- Nếu Hiệp muốn thử browser session: tự chạy lệnh trên trong terminal (cần cho phép), ghi kết quả vào đây.
