---
name: Trend digest
description: >-
  Use for the daily (or on-demand) trend scan for a short-form content channel:
  collect current memes, formats, comment phrases, hashtags, topics and sound names
  in the channel's niche from free public sources, write a dated digest + raw.json,
  update the rolling ingest library, and propose script hooks for upcoming clips.
---
# Trend digest

## Inputs (from the channel repo's AGENTS.md)
- Niche and audiences. For @hi.oneup: productivity, self-improvement, study, office, dev; VN + global.
- Clip plan / theme map, used to map findings to clips.
- Output root. Unattended runs write to the box sync dir, never directly to the user's computer.

## Sources (free and public only)
1. Web search: "<niche> TikTok trend <month year>", "trend TikTok Việt Nam <tháng năm>", "câu nói hot giới trẻ", "<slang> là gì".
2. X public search tool (`search_posts_all`, last 7 days, min_faves filter). On 429 errors, retry once, then log it in `sources_tried`.
3. Agent Reach on the box: YouTube search (yt-dlp), RSS, Reddit (r/productivity, r/getdisciplined, r/studytips, r/vozforums when reachable).
4. TikTok Creative Center (hashtags, songs, VN region) and public TikTok hashtag pages via web fetch. These pages are often JS-only; if so, mark `blocked`, never log in.
5. Google Trends VN (trends.google.com/trending?geo=VN) via fetch, if it is reachable.

## What to collect
Each item records: kind (meme / format / phrase / slang / hashtag / topic / sound / search), language, audience, a one-line meaning, ≥1 evidence URL with a date, platforms, which pillar it fits, and candidate clip ids.

## Rules
- Do not copy other creators' video, audio, or verbatim lines. Borrow only situations and common phrases.
- Respect platform terms of service. No logged-in scraping, no cookie extraction, no paid APIs.
- Every item needs a citation. Mark anything unverified as such. Drop items without evidence.
- Trend facts never replace source facts. Scripts keep their factual source (for example HowToLiveBetter).
- Skip edgy or political slang that clashes with the brand. Words like "bá khí" are for comment replies only.

## Steps
1. Read the current `ingest.md` and the theme map (the next 6 clips).
2. Query the sources. Aim for 15–40 candidate items, then dedupe against ingest by id.
3. Write `research/trends/YYYY-MM-DD/raw.json`, holding every item plus `sources_tried` with a status for each source.
4. Write `research/trends/YYYY-MM-DD/digest.md`. Include front-matter, a sources line, the top 5 with links, and a **Script hooks** section: 3–5 concrete ways to weave today's findings into specific upcoming clips (by clip id and theme), each marked as needing approval if it changes an approved script. End with compliance notes.
5. Update `ingest.md`. Add new rows (first_seen = last_seen = today, count 1). For existing rows, increment count and set last_seen. Update `updated:`.
6. If running unattended, stop here. The sync step (AGENTS.md "Trend sync") moves the files into the repo. Otherwise, sync, commit as "trends: YYYY-MM-DD digest", and push if allowed.
7. Report the top 5 with links and any source failures.
