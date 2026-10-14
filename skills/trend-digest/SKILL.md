---
name: Trend digest
version: 3
description: >-
  Daily (and Sunday weekly-synthesis) trend scan for a "how to live" short-form comic channel.
  Collect ANY hot trends + niche trends from free public sources, brand-safety filter, score
  novelty/saturation and dedupe against past digests and used bridges, observe which hook
  patterns/formats are performing, write a differentiation step (what everyone says vs our
  angle), bridge to a source-book lesson, grow a hook-pattern library, and emit validated
  scene-plan stubs for the top 1-2 ideas so trend -> script -> comic render is seamless.
---
# Trend digest v3 (multi-source collector + learning loop)

## Inputs (from the channel repo's AGENTS.md)
- Source book index (@hi.oneup: HowToLiveBetter, "phần.mục" ids), `content/theme-map.md`, `content/idea-bank.md`, `content/story-bank.md`, `content/voice-profile.md`.
- Learning state: `research/trends/ingest.md` (tables + Bridges), `research/trends/patterns.md` (hook/format library), last 7 `research/trends/*/raw.json`.
- Series format: comic-only (Remotion comic story beats with Hiệp/Omi chibi rigs + HyperFrames motion explainers). No real footage, no event footage/audio.
- Output root: unattended runs write to the box sync dir, never directly to the user's computer.

## Sources (free and public only; no login, no cookies, no paid API)
Config: `pipeline/trends/sources.yaml` (33 sources verified 2026-10-13). Collector: `pipeline/scripts/trend-collect.py` (stdlib + yt-dlp; parallel, 15 s timeout per source, per-source status, cross-source clustering, keyword safety pre-filter, heuristic heat/fit/bridgeability). Expect 400+ raw items/day.
1. **Script sources** (run by the collector): Google Trends RSS VN+US (approx_traffic) · VnExpress (tin-noi-bat, tin-moi-nhat, so-hoa, giai-tri, doi-song) · Kenh14 (`/rss/home.rss`, `/star.rss`, `/doi-song.rss`) · Thanh Niên · Dân Trí · Genk (`/rss/home.rss`) · CafeBiz · Tinh tế · Tuổi Trẻ via Google News `site:tuoitre.vn` · Google News RSS (VN top, "trend TikTok", "gen Z", US productivity, US TikTok trend) · HN front page (Algolia, points) · Product Hunt · The Verge · Ars · Know Your Meme · Wikipedia top pageviews vi/en · Bluesky trending + top search · Spotify VN daily (kworb) · YouTube niche search (yt-dlp, view counts → saturation/pattern evidence only).
2. **X (MCP only, the agent calls it, a script cannot):** `GetDynamicTools {namespace:"x"}` first, then `get_trends_by_woeid` (23424984 VN, 1 worldwide), `search_news` (2–4 niche queries, max_age_hours 72), optional `search_posts_all`. Save as a JSON list `research/trends/DATE/x-extra.json` with keys source (x-trends-vn / x-trends-ww / x-news), title, url, cat, lang, rank; pass with `--extra`. If the x namespace is missing or errors, retry discovery once, then record `x: unavailable (<exact error>)`. Budget: 30 reads/min, 1000/day.
3. **Known blocked (do not retry daily):** TikTok Creative Center (SPA; `creative_radar_api` answers `40101 no permission` without browser-signed headers) → use Google News "trend TikTok", Kenh14, X News instead · reddit.com JSON/RSS (403 from the box IP; needs OAuth) · rsshub.app public (403) · Threads (login/JS). Retest monthly; to add a source, test it and append to sources.yaml.

## TikTok-native signals (rule 57, DL-053)
Collect these every day, ahead of the general sources:
- Public TikTok search/tag pages for the channel keywords (VN first: trì hoãn, lười, dí deadline, học tập, thói quen). Take the top clips by views and comments, then record the URL, views, comments, date, the hook line and the comment phrases that repeat.
- News/blog trend roundups about VN TikTok (e.g. 35express "TREND:" posts, kenh14, thethao247). Record the phrase, the format and the sound.
- When TikTok blocks the box (client-rendered pages, yt-dlp fails), use YouTube Shorts/VN videos as a proxy with `yt-dlp --flat-playlist -j "ytsearch8:<kw>"`, then run `yt-dlp -j <url>` for the comment count. Mark these rows as proxy.
- Never use TikTok Creative Center. Never log in. Never use cookies.
Output section "TikTok signals" in the digest has a table: keyword · clip URL · views · comments · trend phrase/format/sound · brand-safe? · bridge idea. Rank by comments/views first and views second.

## Collect
`python3 pipeline/scripts/trend-collect.py --date YYYY-MM-DD --out research/trends/YYYY-MM-DD --extra research/trends/YYYY-MM-DD/x-extra.json` → `collect.json`. Then build `raw.json` = collect items (+ any web-search finds) and **override scores by hand for the shortlist (15–25 items)**: heat_score, fit_score, bridgeability, saturation_signal, patterns, safety_reason. Items of kind `pattern-evidence` (YT niche) feed patterns/saturation, never the top list.
Categories: news · entertainment · sports · memes/slang · viral moments · celebrity · tech/AI · social debates · seasonal · niche productivity/study/office/dev.
Item schema unchanged (id, kind, category, lang, text, summary, heat_score, fit_score, bridgeability, signals{sources, cross_sources, best_rank, metrics}, saturation_signal, patterns[], evidence[], safety).
Quality signals to weigh: cross_sources ≥2, traffic/points/likes/pageviews, X News stories (= real debate), and recency. Lessons and numbers come only from `content/theme-map.md`/the book; never invent a section id or statistic.

## Brand-safety filter (unchanged, apply before bridging)
- Drop: politics, government/legal disputes, religion, tragedies, deaths, accidents, crime, violence, disasters, illness of a named person, profiting from suffering, mocking a person/body/region, gambling promotion, sexual content, unsourced medical claims.
- Caution (needs Hiệp approval): named celebrities (positive/neutral only), big public projects (no criticism), money windfalls (no mocking/envy).
- `safety: ok | caution | drop` + reason. Dropped items stay only in raw.json.

## Learn & score (new in v2)
1. **Dedupe:** same `id`, or ≥60% token overlap with an item in the last digests = same trend; keep the id, bump ingest `count`/`last_seen`.
2. **Score:** run `python3 pipeline/scripts/trend-learn.py score research/trends/YYYY-MM-DD/raw.json`. It writes `novelty` (1/(1+days seen)), `saturation` (recurrence in last 7 days + `saturation_signal`), `already_used` (bridge already mapped to a clip in ingest) and `rank_score = heat*fit*bridgeability*(0.5+novelty)*(1-0.6*saturation)*(0.3 if used)`.
   Rule of thumb: high heat + low saturation = act today; high saturation = only with a contrarian/unique angle; already used = only as callback.
3. **Pattern mining:** for the top YT/X results of the top trends, classify the hook shape (question, number shock, POV, "everyone says X", callout, before/after, list, story-cold-open, seasonal timer). Increment `seen` in `patterns.md`; add a new P-row only when a shape appears in ≥2 high-signal items and is not covered. Never copy lines, audio or visuals; store the abstract template only.
4. **Differentiation (per bridge):** one line "Mọi người đang nói: …" (consensus take, cite 1–2 URLs) vs "Góc của mình: …" which must use at least one of: Hiệp's real story (story-bank only, else `[CẦN HIỆP XÁC NHẬN]`), Omi's jab/companion moment (week ≥5), a book fact the consensus misses, or a contrarian turn. Reject bridges whose angle = consensus.

## Bridges (core)
`trend → relatable moment → lesson (part.item + one-line fact, checked in the book; flag China-only data) → differentiation → VI hook (pattern id) → angle (humor/contrarian/empathy/data/story, vary vs last 3 clips) → theme (LIGHT positive / DARK downside) → target (clip id or new idea)`.

## Plan stubs (new in v2)
For the top 1–2 bridges write an ideas file and run
`python3 pipeline/scripts/trend-learn.py stub research/trends/YYYY-MM-DD/ideas.json research/trends/YYYY-MM-DD/plans/`
(each idea: id, title, trend_id, bridge_id, lesson, angle, pattern, differentiation, theme, week, hook_vi, moment_vi, turn_vi, hook_en, optional beats[] with text/expression/action/pose/background/duration/caption_en).
Then validate each: `cd video-engine && npm run validate -- <plan.json>`. Fix until ✔. Omi is blocked by the validator when week < 5. Stubs are `status: stub-needs-approval`: story lines stay placeholders unless from story-bank; voice per voice-profile (bạn/mình, miền Nam, humor 4/5, 1–3 EN words). Explainer beats are noted in the idea as `explainer:` text for HyperFrames, not rendered by the job.

## Daily steps
1. Read ingest.md, patterns.md, theme map (next 6–8 clips), idea bank, last digest.
2. X via MCP → x-extra.json; run trend-collect.py. 3. Safety filter (confirm the keyword pre-filter by reading the shortlist). 4. Write raw.json, run `score`. 5. Pattern mining -> update patterns.md.
6. Bridges (top 5–8) with differentiation. 7. Ideas + plan stubs for top 1–2, validate.
8. Write `digest.md`: front-matter, sources line, top trends (with rank_score/novelty/saturation), **Learning** (new patterns, saturated topics to avoid), **Bridges** table, **Differentiation**, **Plan stubs** (paths + validate result), **Script hooks** (3–5, mark approval needed), safety notes.
9. Update ingest.md (rows, counts, Bridges with pattern+status) and idea-bank for new ideas.
10. Unattended: stop; sync moves files (AGENTS.md "Trend sync"). Attended: sync, commit "trends: YYYY-MM-DD digest", push if allowed.
11. Report counts (sources ok/total, raw, clusters, kept), top 10 trends, top bridges + differentiation, stub paths, source failures.

## Weekly synthesis (Sunday, after the daily run)
1. `python3 pipeline/scripts/trend-learn.py week` for the 7-day roll-up.
2. Read `logs/decision-log.md` retro section for clip metrics Hiệp reported (views, completion, follows). If none, say so; do not invent numbers.
3. Update patterns.md: `uses`/`wins` from published clips, retire tired patterns, promote patterns with wins/uses ≥0.5.
4. Write `research/trends/weekly/YYYY-Www.md`: what trended, what saturated, patterns rising/falling, which bridges became clips, 3 recommended angles + 2 topics to avoid next week, proposed rule/skill changes (do not edit rules; propose for Hiệp, rule-33).
5. Append one line to patterns.md "Learnings log".
