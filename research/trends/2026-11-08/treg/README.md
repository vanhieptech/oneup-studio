---
title: "Treg TikTok research 2026-11-08"
date: 2026-11-08
type: trend-source
id: trends-2026-11-08-treg
status: raw-evidence
updated: 2026-11-08
source: "Treg MCP (team levanhiep-s-team)"
tags: [trends, tiktok, treg]
---
# Treg TikTok research 2026-11-08

Fetched 08/11/2026 ~08:05–08:20 giờ VN (UTC+7). Treg-first theo quyết định Hiệp 08/11. Không dùng Apify (không cần fallback).

## Calls (actual charges)
| job | endpoint (provider) | input | call_id | cost USD |
|---|---|---|---|---|
| search | scrapecreators.tiktok.search.videos | query=met moi sau gio lam, date_posted=this-week, region=VN, trim | 1fe7e63784d4425fb6552e8fad18d636 | 0.00188 |
| search | scrapecreators.tiktok.search.videos | query=tri hoan (same filters) | 77c530694efa4002b59c00d44f435dbf | 0.00188 |
| search | scrapecreators.tiktok.search.videos | query=thoi quen moi ngay | c72a9efb849847ea8f99c9cc4e79f5dd | 0.00188 |
| search | scrapecreators.tiktok.search.videos | query=chu nhat o nha | 3d3320e0853147d0b73ef035bd9e4065 | 0.00188 |
| detail+transcript | scrapecreators.tiktok.video.detail (get_transcript) | @uyph100008 7703081372998503700 | 7fc6e17afe38400d8f67c92dfb948e52 | 0.00188 |
| detail+transcript | scrapecreators.tiktok.video.detail | @hoanglongquoi 7703019605341555975 | f1da332a6c3540d79f2be688be6807ef | 0.00188 |
| detail+transcript | scrapecreators.tiktok.video.detail | @phantai911809 7704918939675118869 | a6708055c718461a82515e26dbd8ff18 | 0.00188 |
| comments | treg.tiktok.video.comments (served by tikhub app-v3) | video_id 7703081372998503700, limit 20 | 4f80c471c4da474db892d8f63dc5e817 | 0.001 |
| comments | treg.tiktok.video.comments (tikhub) | 7703019605341555975 | 7f1943515c2d4e7eb6b3b6c025890e2a | 0.001 |
| comments | treg.tiktok.video.comments (tikhub) | 7704918939675118869 | 30688c142738469bbbdad3596dac8202 | 0.001 |

**Tổng: 10 call, $0.01616** (balance 0.99752 → 0.98136, khớp tổng cost_usd). Route max cost header $0.005 cho comments.

## Coverage & limits
- Videos: 119 kết quả keyword search (4 query × ~30), không phải bảng xếp hạng trend. `date_posted=this-week` và `region=VN` chỉ là bộ lọc gửi upstream; region là vị trí proxy, không lọc nguồn gốc. Ngày đăng thật trong `search-normalized.json` (01–08/11). Số view/like/share là snapshot lifetime lúc fetch, không chứng minh đang tăng hay xếp hạng.
- `trim=true` làm mất trường music trong search → music lấy từ video.detail cho 3 clip shortlist (cả 3 là original sound của creator). Metadata âm thanh không phải quyền dùng lại audio.
- Transcript: 2/3 có WEBVTT do provider trả (@phantai911809, @uyph100008); @hoanglongquoi = null (chỉ có caption). Phụ đề tự động có thể sai chữ (vd «gặp rắn» trong clip @uyph100008).
- Comments: trang đầu 20 comment/clip theo thứ tự của provider, không sort theo like. Mỗi comment là một lời tự kể, không đại diện đám đông, không phải người xem kênh mình.
- Kênh @hi.oneup không được tra trong lượt này.

Files: `raw-search-*.json`, `raw-detail-*.json`, `raw-comments-*.json`, `search-normalized.json`, `shortlist.json`.
