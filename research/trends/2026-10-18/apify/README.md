---
title: "Apify TikTok-native run 2026-10-18"
date: 2026-10-18
type: research-trends
tags: [apify, tiktok, clockworks, parseforge]
status: ready
source: "Apify MCP user-Apify; runs N2Peq658RINF7MURa, QoeNaQ18A27icJKuy, pwwOMApu0ChyPSWO8"
id: trends-2026-10-18.apify
updated: 2026-10-18
---
# Apify 2026-10-18
- Discovery `clockworks/tiktok-scraper` run `N2Peq658RINF7MURa` (dataset `kLKVCzCIjYTsfxHqv`, KV `geaTq9ficLF2fAOrd`): hashtags kyluatbanthan, sinhvien, divlam, songtichcuc + searchQueries "luoi qua phai lam sao", "cach tap trung hoc bai", "nghien dien thoai"; resultsPerPage 7; DOWNLOAD_SUBTITLES; commentsPerPost 0; maxTotalChargeUsd 0,50 → 43 mục (42 hợp lệ; `divlam` là gõ nhầm `dilam` → 1 mục NOT_FOUND) (`raw-clockworks.json`, 0,0436 CU).
- Shortlist 6 (`shortlist-urls.json`, `dataset-shortlist.json`); comments `clockworks/tiktok-comments-scraper` run `QoeNaQ18A27icJKuy` 100 comment (`raw-comments.json`, 0,0503 CU); parseforge enrich run `pwwOMApu0ChyPSWO8` 3 URL cụ thể (`raw-parseforge.json`, 0,0303 CU). Ghép comment parseforge cho @biquyetdodaihoc → `comments-merged.json` 110.
- VTT: 23 file vie-VN trong `vtt/` (tải qua link công khai `downloadLink`, không dùng token). Transcript parseforge là bản dịch EN nên dùng VTT; @nycuataodau_22 không lời → caption fallback.
- Normalized `clips.json`: 6 clip; fields coverage 71/72 ô = 98,6% (caption 5/6 vì @hoang_hao209 đăng không caption; 11/12 trường 100%).
- Bỏ khỏi shortlist: @diepquy1512 “bỏ lọ đi” (3,6M view — nội dung tình dục/NoFap), @tthanhtichcuc (isAd=true quảng cáo). Chỉ 1/6 clip đăng trong 7 ngày (@nycuataodau_22, 12/10); còn lại là clip evergreen từ 12/2025–7/2026.
- Không gọi `clockworks/tiktok-trends-scraper`, lexis hay parseforge bằng từ khoá có dấu.
