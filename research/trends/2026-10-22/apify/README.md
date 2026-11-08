---
title: "Apify TikTok-native run 2026-10-22"
date: 2026-10-22
type: research-trends
tags: [apify, tiktok, clockworks]
status: blocked
source: "Apify MCP user-Apify"
id: trends-2026-10-22.apify
updated: 2026-10-22
---
# Apify 2026-10-22 — không chạy được
- `clockworks/tiktok-scraper` bị từ chối 2 lần (lần 1: hashtags kynangmem, dilam + 4 searchQueries, resultsPerPage 6, maxTotalChargeUsd 0,50; lần 2: thu nhỏ 1 hashtag + 2 query, resultsPerPage 5, maxTotalChargeUsd 0,10, memory 1024). Lỗi nguyên văn: "Your remaining usage of $0.132525 this billing cycle isn't enough for this run. Increase your limit by upgrading to a paid plan".
- Không có run id, không dataset, không VTT, không comments. Không gọi parseforge/comments vì không có shortlist URL.
- Không gọi actor bị cấm. Không đổi sang trình duyệt hay cookie.
- Cần Hiệp quyết: nâng gói Apify, chờ chu kỳ mới, hoặc tạm dùng proxy (Google News "trend TikTok", Kenh14) như hôm nay.
