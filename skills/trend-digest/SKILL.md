---
name: Trend digest
version: 2
description: >-
  Daily (and Sunday weekly-synthesis) trend scan for a "how to live" short-form comic channel.
  Collect ANY hot trends + niche trends from free public sources, brand-safety filter, score
  novelty/saturation and dedupe against past digests and used bridges, observe which hook
  patterns/formats are performing, write a differentiation step (what everyone says vs our
  angle), bridge to a source-book lesson, grow a hook-pattern library, and emit validated
  scene-plan stubs for the top 1-2 ideas so trend -> script -> comic render is seamless.
---
# Trend digest v2 (learning loop)

## Inputs (from the channel repo's AGENTS.md)
- Source book index (@hi.oneup: HowToLiveBetter, "phần.mục" ids), `content/theme-map.md`, `content/idea-bank.md`, `content/story-bank.md`, `content/voice-profile.md`.
- Learning state: `research/trends/ingest.md` (tables + Bridges), `research/trends/patterns.md` (hook/format library), last 7 `research/trends/*/raw.json`.
- Series format: comic-only (Remotion comic story beats with Hiệp/Omi chibi rigs + HyperFrames motion explainers). No real footage, no event footage/audio.
- Output root: unattended runs write to the box sync dir, never directly to the user's computer.

## Sources (free and public only; record status per source in raw.json `sources_tried`)
1. Google Trends RSS VN + US: `curl -s "https://trends.google.com/trending/rss?geo=VN"` (also `geo=US`). `approx_traffic` -> heat.
2. YouTube via yt-dlp (`yt-dlp --flat-playlist -J "ytsearch20:<query>"`, add `--extractor-args` only if needed): for each top trend AND each niche query, record view_count / upload age of top results -> `signals.yt_views_median`, `signals.yt_results_7d` (saturation proxy). Note titles' hook shapes for pattern mining.
3. X public reads: `get_trends_by_woeid` (VN 23424984, worldwide 1), `search_posts_all` (7 days, min_faves) -> `signals.x_posts`, `signals.x_top_likes`. On 429 retry once, log.
4. News RSS / web search: VnExpress, Tuổi Trẻ, Kenh14, global tech/pop; "trend TikTok Việt Nam hôm nay", "câu nói hot <tháng năm>". `get_news`/`search_news` from the X tools if available.
5. TikTok Creative Center / hashtag pages via fetch; if JS-only mark `blocked`. Never log in, never extract cookies.

## Collect (20–40 candidates)
Categories: news · entertainment · sports · memes/slang · viral moments · celebrity · tech/AI · social debates · seasonal · niche productivity/study/office/dev.
Each item: `id` (kebab, stable across days), kind, category, lang, summary, `heat_score` 0–1 (normalised from traffic), `fit_score` 0–1 (audience fit), `bridgeability` 0–1, `signals{}` (raw numbers), `saturation_signal` 0–1 (how many creators already cover it with the SAME lesson angle; from YT/X counts), `patterns[]` (pattern ids seen in top-performing external content), ≥1 dated evidence URL, safety verdict.

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
2. Collect all sources (+ signals). 3. Safety filter. 4. Write raw.json, run `score`. 5. Pattern mining -> update patterns.md.
6. Bridges (top 5–8) with differentiation. 7. Ideas + plan stubs for top 1–2, validate.
8. Write `digest.md`: front-matter, sources line, top trends (with rank_score/novelty/saturation), **Learning** (new patterns, saturated topics to avoid), **Bridges** table, **Differentiation**, **Plan stubs** (paths + validate result), **Script hooks** (3–5, mark approval needed), safety notes.
9. Update ingest.md (rows, counts, Bridges with pattern+status) and idea-bank for new ideas.
10. Unattended: stop; sync moves files (AGENTS.md "Trend sync"). Attended: sync, commit "trends: YYYY-MM-DD digest", push if allowed.
11. Report top 5 trends, top bridges + differentiation, stub paths, source failures.

## Weekly synthesis (Sunday, after the daily run)
1. `python3 pipeline/scripts/trend-learn.py week` for the 7-day roll-up.
2. Read `logs/decision-log.md` retro section for clip metrics Hiệp reported (views, completion, follows). If none, say so; do not invent numbers.
3. Update patterns.md: `uses`/`wins` from published clips, retire tired patterns, promote patterns with wins/uses ≥0.5.
4. Write `research/trends/weekly/YYYY-Www.md`: what trended, what saturated, patterns rising/falling, which bridges became clips, 3 recommended angles + 2 topics to avoid next week, proposed rule/skill changes (do not edit rules; propose for Hiệp, rule-33).
5. Append one line to patterns.md "Learnings log".
