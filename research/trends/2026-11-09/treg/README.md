---
title: "Treg TikTok research 2026-11-09"
date: 2026-11-09
type: trend-source
id: trends-2026-11-09-treg
status: raw-evidence
updated: 2026-11-09
source: "Treg MCP (team levanhiep-s-team)"
tags: [trends, tiktok, treg]
---
# Treg TikTok research 2026-11-09

Fetched 09/11/2026 ~08:10–08:25 giờ VN (UTC+7). Treg-first theo quyết định Hiệp 08/11. **Không dùng Apify** (Treg đủ, không cần fallback). Đã đọc `catalog_get` (schema + giá) cho search, video.detail, video.comments (route) và music chart trước khi gọi.

## Calls (actual charges)
| job | endpoint (provider) | input | call_id | cost USD |
|---|---|---|---|---|
| search | scrapecreators.tiktok.search.videos | query=thu hai di lam, date_posted=this-week, region=VN, trim=true | e2cae9a639604ce7b06d1172726a5511 | 0.00188 |
| search | scrapecreators.tiktok.search.videos | query=so sanh ban than voi nguoi khac (same filters) | 2b822a767295416d804a1276df4c6fa5 | 0.00188 |
| search | scrapecreators.tiktok.search.videos | query=khong co dong luc | 6cdc927dc6a642af98b66b3c508a9418 | 0.00188 |
| search | scrapecreators.tiktok.search.videos | query=tiet kiem tien luong | cd06fd2624f14a108df11f41f686baa2 | 0.00188 |
| search | scrapecreators.tiktok.search.videos | query=moi ngay 1000 chu | f4574c913d72478bbb48c2775e135cff | 0.00188 |
| sound chart | tikhub.x.tiktok-app-v3-fetch-music-chart-list | scene=1 (Viral 50), count=20 | d2c3d44e5b2844ec8dd17219693b90a1 | 0.001 |
| detail+transcript | scrapecreators.tiktok.video.detail (get_transcript) | @cafef_official 7704990703348305160 | 14e8b3c722744763b0bdb17e532b623a | 0.00188 |
| detail+transcript | scrapecreators.tiktok.video.detail | @tranen1990 7704573745087663378 | 1dbe30abb75f45afa7cd54286154110d | 0.00188 |
| detail+transcript | scrapecreators.tiktok.video.detail | @radio.mi.ngy0 7704714527283236117 | 279aa543cc55496091005b485957b91d | 0.00188 |
| comments | treg.tiktok.video.comments (served by tikhub app-v3) | 7704990703348305160, limit 20 | 9c290d61f0fe4f89a850a2308b731664 | 0.001 |
| comments | treg.tiktok.video.comments (tikhub) | 7704573745087663378 | 7587cd1c867b40d5bd0805814a5f0a3a | 0.001 |
| comments | treg.tiktok.video.comments (tikhub) | 7705026216276937992 | 2206b7f600fa42ff9ff506b54ec6130d | 0.001 |

Call id cũng nằm trong trường `call_id` của từng file raw và trong `search-normalized.json`.
**Tổng: 12 call, $0.01904** (balance 0.98091 → 0.96187, khớp đúng tổng `cost_usd`). Header `X-Treg-Route-Max-Cost: 0.005` cho comments; cả 3 trúng ngay provider đầu (tikhub), không trả thêm cho provider khác.

## Coverage & limits
- **Videos:** 5 keyword search, 140 kết quả (110 từ 4 query chủ đề + 30 từ «moi ngay 1000 chu», toàn spam follow chéo, bỏ). Đây là keyword search, **không phải bảng xếp hạng trend**. `date_posted=this-week` và `region=VN` chỉ là bộ lọc gửi upstream; region là vị trí proxy. Kết quả trả về: ngày đăng thật 02–09/11 (không mục nào ngoài tuần), trường `region` trả về VN hoặc JP. Lượt xem/like/share là snapshot lifetime lúc fetch, không chứng minh đang tăng hay xếp hạng. Không sort theo like.
- **Sound:** search `trim=true` không trả music (giống 08/11). Music lấy qua video.detail cho 3 clip: cả 3 là original sound của creator. **Viral 50** (tikhub, scene=1): chart_info update 09/11 07:00 giờ VN; **provider không có bộ lọc vùng**, không nói chart của nước nào; trường `trend` = 4 cho mọi dòng, nghĩa không được tài liệu hoá. `user_count` là số video dùng sound (lifetime), không phải tốc độ. Metadata âm thanh không phải quyền dùng lại audio.
- **Transcript:** 2/3 detail có WEBVTT do provider trả (@cafef_official, @radio.mi.ngy0); @tranen1990 = null (chỉ có caption). Phụ đề tự động có thể sai chữ.
- **Comments:** trang đầu 20 comment/clip theo thứ tự provider, không sort theo like. @tranen1990: 20/20 là lời chào, sticker, khen ngoại hình: **không có bằng chứng pain** (ghi nhận, không dùng). Mỗi comment là một lời tự kể, không đại diện đám đông, không phải người xem kênh mình.
- Kênh @hi.oneup không được tra trong lượt này.

Files: `raw-search-*.json`, `raw-detail-*.json`, `raw-comments-*.json`, `raw-music-chart-viral50.json`, `search-normalized.json`, `shortlist.json`.
