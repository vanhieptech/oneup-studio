---
title: "Apify TikTok sample run (clockworks search + VTT + comments)"
date: 2026-10-16
type: research-trends
tags: [apify, tiktok, sample, clockworks]
status: ready
source: "Apify MCP user-Apify; run au2F9eFcWhzuaXWnz"
id: trends-2026-10-16.apify-sample
updated: 2026-10-16
---
# Apify sample 2026-10-16

- **Actor:** `clockworks/tiktok-scraper`
- **Run id:** `au2F9eFcWhzuaXWnz` (SUCCEEDED ~26s)
- **Input:** searchQueries=`["Vay thi ban chat cua"]` (ASCII, no diacritics), searchSection=`/video`, resultsPerPage=3, `downloadSubtitlesOptions=DOWNLOAD_SUBTITLES`, commentsPerPost=5
- **Items:** 3 clips · 15 comments · 4 VTT keys in KV store `XVyunFSbkllzZYCim`
- **Fields coverage:** 100% of required fields (url, caption, author, play/like/share/comment, duration, music, hashtags, subtitle_or_transcript=VTT, top_comments)
- **Files:** `run-meta.json`, `raw-clips.json`, `raw-comments.json`, `clips.json` (normalized), `vtt/*.vtt`

Verified lesson: ASCII search + DOWNLOAD_SUBTITLES yields VTT in KV store without paid TRANSCRIBE; comments land in a separate dataset (`commentsDatasetUrl`).
