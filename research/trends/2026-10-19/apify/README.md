---
title: "Apify TikTok-native run 2026-10-19"
date: 2026-10-19
type: research-trends
tags: [apify, tiktok, clockworks, parseforge]
status: ready
source: "Apify MCP user-Apify; runs MUd3jqleOKKbk36dK, qrvghHpuOWGnjjsbp, uKufN2qe3jeKSMAE0"
id: trends-2026-10-19.apify
updated: 2026-10-19
---
# Apify 2026-10-19
- Discovery `clockworks/tiktok-scraper` run `MUd3jqleOKKbk36dK` (dataset `UcO1WLsoGu1hFd2hM`, KV `WhxYLaEbXnOubueRO`): hashtags dilam, vanphong, genz + searchQueries "luot tiktok ca ngay", "vua lam vua luot dien thoai", "tin nhan cong viec ngoai gio"; resultsPerPage 7; DOWNLOAD_SUBTITLES; commentsPerPost 0; maxTotalChargeUsd 0,50 → 42 mục, 6/6 input OK (`raw-clockworks.json`, 0,0244 CU). `#dilam` lẫn clip nước ngoài (tên riêng Dilam), `#genz` chủ yếu clip tiếng Anh.
- Shortlist 6 (`shortlist-urls.json`, `dataset-shortlist.json`); comments `clockworks/tiktok-comments-scraper` run `qrvghHpuOWGnjjsbp` 99 comment (`raw-comments.json`, 0,0409 CU; @vtv24news tắt comment); parseforge enrich run `uKufN2qe3jeKSMAE0` 3 URL cụ thể (`raw-parseforge.json`, 0,0355 CU; comment parseforge trùng hết với clockworks → `comments-merged.json` 99).
- VTT: 12 file vie-VN trong `vtt/` (tải qua link công khai `downloadLink`, không dùng token). @vanphongsono không lời → caption fallback.
- Normalized `clips.json`: 6 clip; script báo 100% (12 trường × 6 clip), thực chất 71/72 ô = 98,6% vì `top_comments` của @vtv24news rỗng (clip tắt comment).
- Bỏ khỏi shortlist: @chuyennhathachden (chửi thề trong lời thoại), @_quangminhtao_ và @thetelegraph (isAd), @korbi.explains (biểu tình, chính trị).
- 4/6 clip shortlist đăng trong 30 ngày (28/09–14/10); @kbhoanganh (08/2025) và @kieu06011993 (04/2024) là evergreen.
- Không gọi `clockworks/tiktok-trends-scraper`, lexis hay parseforge bằng từ khoá có dấu. Tổng ~0,10 CU.
