---
title: "Routine: @hi.oneup trend digest v5"
date: 2026-10-16
type: plan
tags: [docs, routine, trend, apify]
status: ready
source: "oneup-studio (soạn trong repo); lessons Apify 2026-10-16"
id: docs.plans.trend-routine-prompt-v5
updated: 2026-10-16
---

# Routine: @hi.oneup trend digest v5
Schedule: daily ~07:55 (Asia/Saigon). On Sundays, after the daily run, also run the weekly synthesis.
Folder / routine name: `hi-oneup-daily-trend-digest` (update existing routine prompt to this text).

Prompt:
Run the @hi.oneup trend digest using skill "Trend digest" v4 (repo: skills/trend-digest/SKILL.md).
1. `cd /workspace/oneup-studio` (ONLY project dir; never /workspace/oneup-studio-sync). Clone https://github.com/vanhieptech/oneup-studio there only if missing. Do not pull/reset over local unpushed commits.
2. X: discover MCP namespace "x", then get VN+worldwide trends and 2–4 niche news queries (habits/productivity, AI work, Vietnam gen Z), max_age_hours 72. Save research/trends/YYYY-MM-DD/x-extra.json. If discovery fails, retry once, then log the exact error.
3. **TikTok-native via Apify (MCP user-Apify, free plan, keep cost tiny)** — config `pipeline/trends/apify.yaml`:
   - PRIMARY: call clockworks/tiktok-scraper with hashtags + ASCII/no-diacritic searchQueries, `downloadSubtitlesOptions=DOWNLOAD_SUBTITLES`, small resultsPerPage (≈5–10), commentsPerPost=0. Use proxyCountryCode=VN only if geo-blocked.
   - DO NOT call: clockworks/tiktok-trends-scraper, lexis trending-hashtags, lexis trending-videos without cookie, parseforge with Vietnamese-diacritic keywords.
   - Shortlist 3–8 brand-safe clips; optionally enrich specific videoUrls with parseforge/tiktok-scraper (includeTranscript + includeComments; caption+comments fallback for slideshows).
   - Pull top comments for shortlist via clockworks/tiktok-comments-scraper.
   - Normalize with `python3 pipeline/scripts/trend-apify-normalize.py` → research/trends/YYYY-MM-DD/apify/clips.json. Every shortlist row must have: url, caption, author, play/like/share/comment counts, duration, music, hashtags, subtitle_or_transcript (VTT or caption), top_comments.
4. Run `python3 pipeline/scripts/trend-collect.py --date YYYY-MM-DD --out research/trends/YYYY-MM-DD --extra research/trends/YYYY-MM-DD/x-extra.json`. Expect ≥30 sources ok and ≥150 raw items; if fewer, say which failed. Do not try TikTok Creative Center, Reddit or rsshub.app. Never log in, never put tokens/cookies in repo.
5. Build raw.json (include Apify TikTok-native section), hand-review 15–25 shortlist, `python3 pipeline/scripts/trend-learn.py score <raw.json>`.
6. Mine patterns, write bridges with differentiation, plan stubs for top 1–2 (`trend-learn.py stub` + `cd video-engine && npm run validate`).
7. Write digest.md (with TikTok signals table), update ingest.md, patterns.md, content/idea-bank.md. Commit only: `git add research/trends content/idea-bank.md && git commit -m "trends: YYYY-MM-DD digest"`. Run check-assets.py. Do not push unattended (Mac git-bundle per AGENTS.md). Do not send messages/posts.
8. If Sunday: weekly synthesis → research/trends/weekly/YYYY-Www.md. Never invent performance numbers.
9. ALWAYS end by delivering the final message below to the user in this chat.

Final message (Vietnamese, to Hiệp):
"Trend hôm nay (DD/MM): quét N/M nguồn, X mục thô → Y mục qua lọc. Apify TikTok: A clip (run id …), fields coverage …%.
Top 10: <tên trend> – <nguồn có link> – <bài học/clip> (×10)
2 ý nên làm: <bridge + Mọi người nói / Góc của mình> + đường dẫn bản nháp kịch bản
Học được: <pattern mới / chủ đề bão hoà nên tránh>
Nguồn lỗi: <nguồn: lý do>
Cần bạn duyệt: <mục caution / chuyện thật cần xác nhận>"
