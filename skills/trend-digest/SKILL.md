---
name: Trend digest
description: >-
  Use for the daily (or on-demand) trend scan for a "how to live" short-form channel:
  collect ANY hot trends (VN + global news, entertainment, sports, memes, viral moments,
  pop culture, tech, social debates, seasonal events) plus niche productivity trends
  from free public sources, brand-safety filter them, write storytelling bridges from
  each strong trend to a lesson in the channel's source book, then save a dated
  digest + raw.json, update the rolling ingest library, and propose script hooks.
---
# Trend digest

## Inputs (from the channel repo's AGENTS.md)
- Source book index (for @hi.oneup: HowToLiveBetter, 34 parts, "phần.mục" ids) and the clip plan / theme map.
- Audiences: for @hi.oneup, VN gen Z, students, office workers, devs, plus global English-speaking viewers.
- Output root. Unattended runs write to the box sync dir, never directly to the user's computer.

## Sources (free and public only; record a status for each in raw.json)
1. **Google Trends RSS** for VN and US/global: `curl -s "https://trends.google.com/trending/rss?geo=VN"` (also `geo=US`). Parse title, approx_traffic, news_item_title, news_item_url.
2. **X public tools:** `get_trends_by_woeid` (VN 23424984, worldwide 1) and `search_posts_all` (last 7 days, min_faves). On a 429 error, retry once and log it.
3. **Web search**, broad: "trend TikTok Việt Nam hôm nay", "câu nói hot <tháng năm>", "viral <date>", "<keyword> là gì". Niche: "<niche> TikTok trend <month year>".
4. **Agent Reach on the box:** YouTube search via yt-dlp (`ytsearch20:<query>`; the old /feed/trending page no longer works), RSS feeds (VnExpress, Tuổi Trẻ, Kenh14 giải trí), Reddit (r/OutOfTheLoop, r/productivity, r/vozforums when reachable).
5. **TikTok Creative Center and hashtag pages** via fetch. These are often JS-only; if so, mark `blocked`, never log in.

## Collect (aim for 20–40 candidates, then rank)
Categories: news · entertainment/K-pop/film · sports · memes/slang · viral moments · celebrity · tech/AI · social debates · seasonal/holidays · niche productivity/study/office/dev.
Each item records: kind, category, language, a one-line summary, traffic or heat signal, ≥1 dated evidence URL, platforms, and a safety verdict.

## Brand-safety filter (apply before bridging)
- **Drop:** politics, government or legal disputes, religion, tragedies, deaths, accidents, crime, violence (including domestic violence plots), disasters, illness of a named person, and anything where the lesson would profit from someone's suffering.
- **Drop:** content that mocks a person, body or region, gambling promotion, sexual content, and medical claims without a source.
- **Caution (needs approval):** named celebrities (positive or neutral framing only), big public projects (don't criticise), money windfalls (don't mock or envy the winner).
- Record `safety: ok | caution | drop` with a reason. Dropped items stay in raw.json only.

## Bridges (the core step)
For each strong trend (ok or caution), write 1–3 bridges:
`trend → relatable moment (what the viewer actually lives through) → lesson (source book part.item + one-line fact, checked in the book) → VI hook line → angle → target (existing clip id or "new idea")`.
- Angles: humor · contrarian · empathy · data · story. Vary the angles across the digest.
- The lesson fact must come from the source book as written. Flag lessons whose data is country-specific (for example China-only numbers) and that need a local equivalent.
- The hook mentions the trend, the lesson carries the value. Never copy the trend's video, audio or lines.

## Steps
1. Read `ingest.md`, the theme map (next 6–8 clips) and the idea bank.
2. Collect from all sources. Dedupe against ingest by id.
3. Apply the safety filter, then rank by heat × audience fit × bridgeability.
4. Write bridges for the top 5–8 trends and look up each lesson in the source book.
5. Write `research/trends/YYYY-MM-DD/raw.json` (every item, its safety verdict, `sources_tried`).
6. Write `research/trends/YYYY-MM-DD/digest.md`:
   - front-matter and a sources line
   - top trends (general and niche) with links
   - a **Bridges** table
   - **Script hooks**: 3–5 concrete uses for upcoming clips, marked as needing approval if they change an approved script
   - safety notes
7. Update `ingest.md`: add or bump rows in each table, including **Bridges**, and refresh `updated:`. Add new-idea bridges to `content/idea-bank.md`.
8. If running unattended, stop here and let the sync move the files into the repo (AGENTS.md "Trend sync"). Otherwise, sync, commit "trends: YYYY-MM-DD digest", and push if allowed.
9. Report the top 5 trends, top bridges with links, and any source failures.
