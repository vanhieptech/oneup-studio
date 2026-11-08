---
title: "Apify TikTok-native run 2026-10-21"
date: 2026-10-21
type: research-trends
tags: [apify, tiktok, clockworks, parseforge]
status: ready
source: "Apify MCP user-Apify; runs s5SFZKHFyY11sveqM, DAvaO6rWS82qqLZc3, jVBfRbQCjUfXzuMoC"
id: trends-2026-10-21.apify
updated: 2026-10-21
---
# Apify 2026-10-21
- Discovery `clockworks/tiktok-scraper` run `s5SFZKHFyY11sveqM` (dataset `ZeqXawtfkqdomIJRU`, KV `UN7A9zrrtFdb1LBhY`): hashtags quanlythoigian, taichinhcanhan + searchQueries "tiet kiem tien luong", "luot dien thoai truoc khi ngu", "lam viec hieu qua hon", "met moi sau gio trua"; resultsPerPage 6; DOWNLOAD_SUBTITLES; commentsPerPost 0; proxy None; maxTotalChargeUsd 0,50 → 36 mục, 6/6 input OK (`raw-clockworks.json`, 0,0403 CU). Đổi bộ query sang tiền + thời gian (trụ 1, phần 5) sau 2 ngày học tập/ngủ.
- Shortlist 5 (`shortlist-urls.json`, `dataset-shortlist.json`): @kesanmoi.rf, @cuungodao, @bachhoaxanh.official, @kinhnghiemhungdongy, @loading141092.
- Comments `clockworks/tiktok-comments-scraper` run `DAvaO6rWS82qqLZc3`: 100 comment (`raw-comments.json`, 0,0438 CU). Parseforge enrich run `jVBfRbQCjUfXzuMoC` 3 URL (`raw-parseforge.json`, 0,0412 CU): transcript eng-US (bản dịch), 0 comment mới → `comments-merged.json` 100.
- VTT: 33 file vie-VN trong `vtt/` (link công khai `downloadLink`, không token); 5/5 shortlist có VTT.
- Normalized `clips.json`: 5 clip, 60/60 ô = 100%.
- Bỏ/không shortlist: 4 isAd, các clip rối loạn lo âu (sức khoẻ tâm thần), clip bác sĩ về điện thoại trước ngủ (y khoa + chủ đề bão hoà), @thaylacthien 3M (2024, tâm linh/tiềm thức). @kinhnghiemhungdongy vào shortlist chỉ làm tín hiệu caution (y khoa không nguồn), không bridge.
- Không gọi `clockworks/tiktok-trends-scraper`, lexis hay parseforge bằng từ khoá có dấu. Tổng ~0,125 CU (MCP không báo USD).
