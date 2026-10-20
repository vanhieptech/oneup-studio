---
title: "Apify TikTok-native run 2026-10-20"
date: 2026-10-20
type: research-trends
tags: [apify, tiktok, clockworks, parseforge]
status: ready
source: "Apify MCP user-Apify; runs jRLleUhL5eClvRAgR, gm8VC17Ft1iCBacpv, 9wLv8eZmFNuHpN1Fk"
id: trends-2026-10-20.apify
updated: 2026-10-20
---
# Apify 2026-10-20
- Discovery `clockworks/tiktok-scraper` run `jRLleUhL5eClvRAgR` (dataset `GvdmHQdlZ0rvdhKJC`, KV `XGBbJMuxEBXmLYZp0`): hashtags congso, onthi + searchQueries "hoc bai xong quen het", "thuc khuya chay deadline", "uong ca phe buoi chieu mat ngu", "ngoi lam viec ca ngay"; resultsPerPage 6; DOWNLOAD_SUBTITLES; commentsPerPost 0; proxy None; maxTotalChargeUsd 0,50 → 36 mục, 6/6 input OK (`raw-clockworks.json`, 0,0260 CU). Đổi bộ query sang học tập + ngủ/cà phê (trụ 3, trụ 5) sau 1 ngày công sở.
- Shortlist 5 (`shortlist-urls.json`, `dataset-shortlist.json`): @ng__phanh, @hoc.di.roi.biet, @camreadwonder, @sabito_0668, @motionlab.fit.
- Comments `clockworks/tiktok-comments-scraper` run `gm8VC17Ft1iCBacpv`: 82 comment (`raw-comments.json`, 0,0327 CU). Parseforge enrich run `9wLv8eZmFNuHpN1Fk` 3 URL cụ thể (`raw-parseforge.json`, 0,0336 CU; lần gọi đầu MCP timeout, gọi lại 1 lần không chờ rồi poll). Gộp → `comments-merged.json` 85.
- VTT: 16 file vie-VN trong `vtt/` (link công khai `downloadLink`, không token). @ng__phanh và @camreadwonder không lời → caption fallback.
- Normalized `clips.json`: 5 clip, 60/60 ô = 100%.
- Bỏ/không shortlist: @chezycongso (isAd), @linh.85.bondauxanhdo (1,6M nhưng dán nhãn đồng nghiệp “hai mang”, fit thấp), @truecraft.coffee (quảng bá thương hiệu), @baothanhnien.official (tắt comment; giữ làm tín hiệu).
- Không gọi `clockworks/tiktok-trends-scraper`, lexis hay parseforge bằng từ khoá có dấu. Tổng ~0,09 CU (≈ 0,03 USD theo giá CU free plan; MCP không báo USD).
