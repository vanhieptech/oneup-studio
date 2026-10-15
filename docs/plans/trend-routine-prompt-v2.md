# Routine: @hi.oneup trend digest v2
Schedule: daily 07:55 (Asia/Saigon). On Sundays, after the daily run, also run the weekly synthesis.

Prompt:
Run the @hi.oneup trend digest using skill "Trend digest" v2 (repo copy: skills/trend-digest/SKILL.md).
1. `cd /workspace/oneup-studio-sync` (clone https://github.com/vanhieptech/oneup-studio if missing); `git pull --ff-only` to read the latest ingest.md, patterns.md, theme-map, idea-bank, story-bank, voice-profile, rules. If /workspace/oneup-studio has newer unpushed commits, read those files from there instead.
2. Collect from free public sources only (Google Trends RSS VN+US, yt-dlp ytsearch with view counts, X public trends/search, news RSS/web search, TikTok Creative Center if reachable). Never log in, never use cookies or paid APIs.
3. Apply the brand-safety filter. Write research/trends/YYYY-MM-DD/raw.json, then run `python3 pipeline/scripts/trend-learn.py score <raw.json>`.
4. Mine hook patterns into research/trends/patterns.md, write bridges with a differentiation line (consensus vs our Hiệp/Omi comic + HowToLiveBetter angle), and generate plan stubs for the top 1–2 ideas with `trend-learn.py stub`, validated by `cd video-engine && npm run validate -- <plan>` (npm ci first if node_modules is missing; if validation can't run, say so).
5. Write digest.md, update ingest.md and idea-bank. Do not commit/push the user's repo, do not send messages, do not post anything.
6. If today is Sunday: run the weekly synthesis (skill section "Weekly synthesis"), writing research/trends/weekly/YYYY-Www.md. Never invent performance numbers.
7. Final message in Vietnamese: top 5 trends (link), top 2 bridges with differentiation + stub paths, patterns learned, source failures, items needing Hiệp's approval (caution items).
