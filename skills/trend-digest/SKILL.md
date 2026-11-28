---
name: trend-digest
description: >-
  Daily (and Sunday weekly-synthesis) trend scan for a "how to live" short-form comic channel.
  Collect ANY hot trends + niche trends from free public sources, brand-safety filter, score
  novelty/saturation and dedupe against past digests and used bridges, observe which hook
  patterns/formats are performing, write a differentiation step (what everyone says vs our
  angle), bridge to a source-book lesson, grow a hook-pattern library, and emit validated
  scene-plan stubs for the top 1-2 ideas so trend -> script -> comic render is seamless.
version: "5.2.1"
metadata:
  author: OneUp Studio
  tags:
    - trends
    - tiktok
    - research
    - ideas
---
# Trend digest v5 (3 streams → Viral DNA → ARC-NNN → idea bank)

## BREAK — Cursor, Antigravity, Claude, Grok (same file)
This skill is `skills/trend-digest/SKILL.md`. `.cursor/skills/trend-digest`, `.claude/skills/trend-digest`, and `.agents/skills/trend-digest` are symlinks to it. One edit applies to every agent. Do not keep a private copy.

Native TikTok path, in order:
1. `python3 pipeline/scripts/tinyfish_client.py tiktok "<topic>" … --out research/trends/DATE/tinyfish/tiktok-candidates.json`
2. `python3 pipeline/scripts/apify-run.py --date DATE --urls-from research/trends/DATE/tinyfish/tiktok-candidates.json --comments <số link>`

The script measures every URL in that file. It does not switch to the hashtag block in `pipeline/trends/apify.yaml`.

When a step cannot run that path, **stop**. Show Hiệp the stderr block that starts with `BREAK trend-digest`, including the `Next:` line. Do not write the digest, do not commit, do not invent a weaker source and continue.

| Situation | What used to happen | What you do now |
|---|---|---|
| Bare `apify-run.py` while TinyFish links exist, or the file is missing/empty | Hashtag basket (`trihoan`, `hoctap`, `cach het tri hoan`) | Script exits `BREAK` before any paid call. Paste that text to Hiệp. |
| `--max-urls` would drop links | Silent slice, default 10 | `BREAK`. Raise `--max-urls` to the full count, or add `--allow-truncate` only after Hiệp says so in this run. |
| More links than the comment default (3) | Comments on 3 clips, presented as done | `BREAK` before spend. Pass `--comments <số link>`, or `--allow-comment-sample` only after Hiệp says so. |
| X MCP missing | One retry, then `x: unavailable` inside the digest and the run continues | Retry `GetDynamicTools` for namespace `x` once. Still missing or erroring: stop and tell Hiệp the exact error. Do not pass `--allow-without-x` yourself. `trend-collect.py` without `--extra` exits `BREAK` before fetching. |
| Apify returns 0 clips, or the comment cap blocks after the dataset is saved | YouTube proxy, or clips.json with no comments, marked done | `BREAK`. Dataset stays on disk. Finish comments with `--comments-only` after the cap is raised. Do not fill TikTok signals from a proxy. |
| Hashtag basket | Default | Only `--allow-hashtag-basket`, and only after Hiệp says so in this run. |

## Purpose
Run the daily (and Sunday weekly) trend digest for @hi.oneup: collect public trends, brand-safety filter, bridge to lessons, and emit scene-plan stubs.


## Inputs (from the channel repo's AGENTS.md)
- Source book index (@hi.oneup: HowToLiveBetter, "phần.mục" ids), `content/theme-map.md`, `content/idea-bank.md`, `content/story-bank.md`, `content/voice-profile.md`.
- Learning state: `research/trends/ingest.md` (tables + Bridges), `research/trends/patterns.md` (hook/format library), last 7 `research/trends/*/raw.json`.
- Series format: comic-only (Remotion comic story beats with Hiệp/Omi chibi rigs + HyperFrames motion explainers). No real footage, no event footage/audio.
- Output root: always the local repo root (`git rev-parse --show-toplevel`; `research/trends/`, `content/idea-bank.md`). Never write to dirs outside the repo, and never to an agent workspace/sandbox copy.

## Three input streams (v5, 26/11/2026) — `pipeline/scripts/trend-streams.py`
Every digest reports the three streams separately. Output: `research/trends/DATE/{digest.md,raw.json,radar.json}` + `research/trends/ingest.md`.
1. **Stream 1 — Multi-Channel Outlier Radar v2.2 (`DL-082`, `DL-084`, `DL-085`, Zero-Token Parallel + Cache + Dedupe):** Local zero-API collector: `python3 pipeline/scripts/radar-fetch.py --date DATE [--lang en|vi] [--workers 6] [--ttl-hours 6] [--use-ego]` fetches watched channels **in parallel** across **5 roles** in `pipeline/trends/radar.yaml` (**`global_niche_source`**, `direct_niche`, `southern_story_voice`, `cross_niche_craft`, `anti_pattern`), uses **YouTube Atom RSS + TTL cache** (warm re-run < 0.1s), and deduplicates against **`research/trends/seen-index.json`** (only surfaces `new` videos or `spike` videos with ≥ +50% views / +100 engagement). With `--use-ego`, uses Hiệp's logged-in `/ego-browser` DOM-only extractors (`ego_crawl.py social <tiktok|x|threads|instagram|youtube>` & `ego_crawl.py comments`) without vision token waste. Weekly auto-discovery: `python3 pipeline/scripts/channel-discover.py --live` writes untracked high-view creators to `research/trends/suggested-channels.md`. Every English outlier carries `lang: "en"` so `trend-match.py` matches it bilingually (EN ↔ VN) and `teardown.py` produces a `localization_vi` cultural bridge.
2. **Stream 2 — Upstream Tech & Productivity news** (3–14 days ahead of TikTok VN). Sources tagged `"stream": "upstream"` (HN, **daily.dev** popular/discussed + tags `ai`/`webdev`/`devops` via Public API + `DAILY_DEV_TOKEN` in `~/oneup-tools/env.sh`, Lobsters, Reddit r/productivity + r/programming via TinyFish search, Product Hunt, The Verge, Ars, GitHub changelog, OpenAI news, Google News AI releases, Bluesky, X via MCP) and `"vn-tech"` (VnExpress Số hoá, Genk, Tinh tế, CafeBiz, Google News VN AI) in `pipeline/trends/sources.yaml`; `collect.json` items carry `stream`. Free daily.dev ≈ 200 req/mo — keep ≤5 `dailydev` sources. For each shortlisted upstream / vn-tech item write into `raw.json`: `"pain"` 1–5 (touches a mass pain), `"story"` 1–5 (can be told as a story or visual metaphor), `"fit": {"hi_oneup": 1–5, "vanhiep_tech": 1–5}`, `"shortlist": true`. Then `python3 pipeline/scripts/trend-streams.py upstream --date DATE --check` → `upstream_score = pain·story·max(fit)/125`, `channel`; exit 1 = an item is unscored, fix before writing the digest.
3. **Stream 3 — Mobile / manual inbox** (`media/footage/inbox/`). Hiệp drops links (`.txt`, `.url`, `.md`, one URL per line or pasted text) or competitor video files. `python3 pipeline/scripts/trend-streams.py inbox --date DATE` dedupes against `ingest.md` + the queue (normalised URL; files by sha256), assigns `trends-DATE-NN`, appends to `research/trends/teardown-queue.json` and to the «Inbox (Luồng 3)» table in `ingest.md`. Inbox files are never moved or deleted.
**Teardown queue:** `python3 pipeline/scripts/trend-streams.py queue` prints each queued row with its exact command (`teardown.py --url … --id … --queue-id …`); a successful teardown marks the row done in the queue and in `ingest.md`.

## Viral DNA + ARC (v5.1, DL-082) — after the queue
Each teardown writes a **7-block Viral DNA Card** (`templates/clip-teardown.md` + `docs/prompts/gemini-teardown.md`: hook mechanics · beat map · winning points · algorithmic triggers · reusable arc + `format_compatibility` · dual-channel angle · Craft, Voice & Emotional Arc Transfer with `emotional_arc` & `spoken_pivots`) and automatically: upserts Khối 5 into the ARC library (`pipeline/arc_library.py`: same source or similarity ≥ 0.6 → add evidence to that `ARC-NNN`, isolating `instructional_list` from `story_metaphor`), regenerates the «Story arcs (ARC-NNN)» table in `research/trends/patterns.md`, pushes Khối 6 angles to `content/idea-bank.md`, and pushes audience pains to `resources/vn-spoken/audience-pain-bank.md`. For local `.mp4` files dropped in `media/footage/inbox/`, `pipeline/scripts/learn-from-channel.py --file <mp4>` transcribes via local `faster-whisper` and extracts spoken pivots for Gate 0. Old teardown JSON: `teardown.py --rerender <json>`. In the digest list: new ARCs, ARCs that gained evidence, ideas added.

## Sources (free and public only; no login, no cookies, no paid API)
Config: `pipeline/trends/sources.yaml` (33 sources verified 2026-10-13). Collector: `pipeline/scripts/trend-collect.py` (stdlib + yt-dlp; parallel, 15 s timeout per source, per-source status, cross-source clustering, keyword safety pre-filter, heuristic heat/fit/bridgeability). Expect 400+ raw items/day.
1. **Script sources** (run by the collector): Google Trends RSS VN+US (approx_traffic) · VnExpress (tin-noi-bat, tin-moi-nhat, so-hoa, giai-tri, doi-song) · Kenh14 (`/rss/home.rss`, `/star.rss`, `/doi-song.rss`) · Thanh Niên · Dân Trí · Genk (`/rss/home.rss`) · CafeBiz · Tinh tế · Tuổi Trẻ via Google News `site:tuoitre.vn` · Google News RSS (VN top, "trend TikTok", "gen Z", US productivity, US TikTok trend) · HN front page (Algolia, points) · **daily.dev** (`type: dailydev`, Bearer `DAILY_DEV_TOKEN`, popular + discussed + tags ai/webdev/devops — primary `@vanhiep.tech` upstream) · Product Hunt · The Verge · Ars · Know Your Meme · Wikipedia top pageviews vi/en · Bluesky trending + top search · Spotify VN daily (kworb) · YouTube niche search (yt-dlp, view counts → saturation/pattern evidence only).
2. **X (MCP only, the agent calls it, a script cannot):** `GetDynamicTools {namespace:"x"}` first, then `get_trends_by_woeid` (23424984 VN, 1 worldwide), `search_news` (2–4 niche queries, max_age_hours 72), optional `search_posts_all`. Save as a JSON list `research/trends/DATE/x-extra.json` with keys source (x-trends-vn / x-trends-ww / x-news), title, url, cat, lang, rank; pass with `--extra`. If the x namespace is missing or errors, retry discovery once. Still missing: **stop** and tell Hiệp the exact error. Do not write `x: unavailable` and continue. Do not pass `--allow-without-x` unless Hiệp says so in this run. `trend-collect.py` without a real `--extra` file exits `BREAK trend-digest` before any fetch. Budget: 30 reads/min, 1000/day.
3. **Known blocked (do not retry daily):** TikTok Creative Center / `clockworks/tiktok-trends-scraper` (0 items) · lexis trending-hashtags (ads cookie) · lexis trending-videos without cookie · parseforge keyword+diacritics · reddit.com JSON/RSS (403) · rsshub.app (403) · Threads (login/JS). Use Apify primary actors in `pipeline/trends/apify.yaml` + Google News "trend TikTok", Kenh14, X News. Retest monthly.

## TikTok-native signals (rule 57, DL-053, L-037) — Apify primary (2026-10-16)
Config: `pipeline/trends/apify.yaml`. Normalize: `pipeline/scripts/trend-apify-normalize.py`. **Local Mac (26/11/2026):** the box MCP `user-Apify` is gone; run `python3 pipeline/scripts/apify-run.py --date DATE --urls-from research/trends/DATE/tinyfish/tiktok-candidates.json --comments <số link>` (REST, token `APIFY_TOKEN` read from `~/oneup-tools/env.sh` via `pipeline/paths.py` `tools_env`, never in the repo; free plan, daily cap in `apify.yaml`, actual cost written to `apify/cost.json`). A bare `apify-run.py` exits `BREAK trend-digest`. It does not fall back to the yaml hashtag basket.

**Discovery first, free (TinyFish, 26/11/2026):** `python3 pipeline/scripts/tinyfish_client.py tiktok "<topic>" … --out research/trends/DATE/tinyfish/tiktok-candidates.json` finds clip links + captions + dates (`search --include-domains tiktok.com`). TinyFish **fetch** of TikTok pages is blocked ("Site Maintenance"), so views/subtitles/comments still come from Apify: pass the candidate links to `apify-run.py --urls-from <candidates.json>` so Apify only measures links already found (cheaper than broad keyword scraping). `trend-collect.py` also has `tinyfish` (web) and `tinyfish_tiktok` source types in `sources.yaml`. Only the free search/fetch meters; no TinyFish agent/browser/dataset/monitor in the daily job.

**Do NOT use** (failed 2026-10-15/16): `clockworks/tiktok-trends-scraper` (Creative Center → 0 items VN+US) · `lexis-solutions/tiktok-trending-hashtags-scraper` (needs ads.tiktok.com cookie) · lexis trending-videos without cookie (~4 brand ads) · `parseforge/tiktok-scraper` with Vietnamese-diacritic **keywords** ("no public video page").

**Primary sources (in order):**
1. **`clockworks/tiktok-scraper`** — `hashtags` + `searchQueries` (prefer ASCII / no-diacritic queries). Set `downloadSubtitlesOptions=DOWNLOAD_SUBTITLES` (VTT in run KV store; prefer this over paid `TRANSCRIBE_*`). `proxyCountryCode=VN` only when geo-blocked (add-on cost). Typical daily: `resultsPerPage` 5–10, `commentsPerPost=0` (comments via #3 on shortlist).
2. **`parseforge/tiktok-scraper`** — **specific `videoUrls` only**; `includeTranscript=true` + `includeComments=true`. Slideshow/edit often lack transcript → fall back to caption + comments. Never diacritic keywords.
3. **`clockworks/tiktok-comments-scraper`** — top comments / caption pain points for 1–5 shortlisted clip URLs.

**Required fields per clip** (fail the day if shortlist rows miss these): `url`, `caption`, `author`, play/like/share/comment counts, `duration`, `music`, `hashtags`, `subtitle_or_transcript` (VTT text or caption fallback), `top_comments[]`. Save under `research/trends/DATE/apify/` (`raw-*.json`, `clips.json`, optional `vtt/`, `comments-*.json`).

News and blog roundups (kenh14, GNews "trend TikTok") stay in the collector. If Apify returns nothing usable, the script exits `BREAK trend-digest`. Do not fill the TikTok signals table with a YouTube proxy and mark the day done. Never Creative Center, never login cookies for discovery.
Output digest section "TikTok signals": keyword · clip URL · views · comments · hook/transcript snippet · sound · brand-safe? · bridge idea. Rank by comments/views then views.

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
2. X via MCP → `x-extra.json`. If X is still missing after one retry, **stop** and tell Hiệp (see BREAK). 2a. TinyFish TikTok discovery → `tinyfish/tiktok-candidates.json`. 2b. `apify-run.py --date DATE --urls-from research/trends/DATE/tinyfish/tiktok-candidates.json --comments <số link>` → `research/trends/DATE/apify/clips.json`. If the script prints `BREAK trend-digest`, stop and show Hiệp that block. Do not rerun without `--urls-from`. 2c. **Stream 1 (tự chạy không cần user nhắc):** chạy `python3 pipeline/scripts/radar-fetch.py --date DATE --use-ego` (quét song song 25 kênh EN+VN, TTL cache, chống trùng `seen-index.json`, kéo comment TikTok qua `/ego-browser` khi cần) + `ego_crawl.py social` (DOM-only cho TikTok/Threads/X nếu cần bổ sung nỗi đau thật) + `trend-streams.py radar --date DATE --enqueue` (ghi `angle` từng dòng). 2d. **Stream 3:** `trend-streams.py inbox --date DATE`. 2e. **Teardown 2–3 outlier mới nhất** qua `trend-streams.py queue` → `teardown.py … --queue-id …` (tự sinh Viral DNA 7 khối + `localization_vi` + ARC + idea-bank). 2f. **Auto-Discovery:** chạy `python3 pipeline/scripts/channel-discover.py --live` cập nhật `research/trends/suggested-channels.md` để trình kênh mới nổi nếu có. 3. Run `python3 pipeline/scripts/trend-collect.py --date DATE --out research/trends/DATE --extra research/trends/DATE/x-extra.json`. A missing `--extra` exits `BREAK trend-digest` before any fetch. Read top non-TikTok items via TinyFish/`ego_crawl.py` before bridging. 4. Safety filter + write `raw.json` (with Stream 2 `pain/story/fit`), run `score`, then `trend-streams.py upstream --date DATE --check`. 5. Pattern mining → update `patterns.md`.
6. Bridges (top 5–8) with differentiation. 7. Ideas + plan stubs for top 1–2, validate.
8. Write `digest.md`: front-matter, sources line, **three stream sections** (Radar table · Upstream table with pain/story/fit/score/channel · Inbox ids), **Viral DNA** (teardowns run, ARC new/updated, ideas pushed), top trends (with rank_score/novelty/saturation), **Learning** (new patterns, saturated topics to avoid), **Bridges** table, **Differentiation**, **Plan stubs** (paths + validate result), **Script hooks** (3–5, mark approval needed), safety notes.
9. Update ingest.md (rows, counts, Bridges with pattern+status) and idea-bank for new ideas. Run `python3 pipeline/scripts/trend-match.py --date DATE` (F2) to preview Top 3 `(Hot Trend < 72h ↔ Unproduced Lesson)` pairs respecting `LIGHT/DARK ≤ 2`.
10. Commit in the repo only your paths: `git add research/trends content/idea-bank.md && git commit -m "trends: YYYY-MM-DD digest"`. Run `python3 pipeline/scripts/check-assets.py`.
11. Report counts (sources ok/total, raw, clusters, kept), top 10 trends, top bridges + differentiation, Top 3 `trend-match.py` pairs, stub paths, source failures.

## Weekly synthesis (Sunday, after the daily run)
1. `python3 pipeline/scripts/trend-learn.py week` for the 7-day roll-up.
2. Read `logs/decision-log.md` retro section for clip metrics Hiệp reported (views, completion, follows). If none, say so; do not invent numbers.
3. Update patterns.md: `uses`/`wins` from published clips, retire tired patterns, promote patterns with wins/uses ≥0.5. Run `python3 pipeline/arc_library.py sync-published` and `python3 pipeline/scripts/golden-sync.py sync-3d` to automatically read `content/published/` (views, completion %, shares/saves), recompute `uses`, `wins`, `win_rate` for `ARC-NNN` + 3D `win_rate` (Archetype × Hook × CTA), and regenerate the ARC table in `research/trends/patterns.md` (empty numbers → no win, never estimate; `gate0.py` prioritizes highest `win_rate`).
4. Write `research/trends/weekly/YYYY-Www.md`: what trended, what saturated, patterns rising/falling, which bridges became clips, 3 recommended angles + 2 topics to avoid next week, proposed rule/skill changes (do not edit rules; propose for Hiệp, rule-33).
5. Append one line to patterns.md "Learnings log".

## Requirements
- Read this skill before acting; follow linked channel/repo AGENTS.md when cited.
- Use tools and paths named in the steps; do not invent alternate pipelines.

## Limitations
- Free/public sources only; no login/cookies/paid APIs in collector.
- Comic-only series format — no real-event footage.
- Writes only inside the repo `research/trends/` and `content/idea-bank.md`.

## Troubleshooting
| Error / symptom | Cause | Fix |
|---|---|---|
| stderr starts with `BREAK trend-digest` | A required step would have been skipped (no X file, no TinyFish URLs, silent hashtag basket, silent comment sample, silent URL cut) | Stop. Show Hiệp the whole block, including `Next:`. Do not continue the digest. |
| Collector empty/partial | Source timeout or YAML drift | Check `pipeline/trends/sources.yaml` + per-source status |
| Duplicate bridges | Dedup tables stale | Compare ingest.md + last 7 raw.json |
| Unsafe topic slipped | Filter miss | Raise brand-safety filter; drop idea |
