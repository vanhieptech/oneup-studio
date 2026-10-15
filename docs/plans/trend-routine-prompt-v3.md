---
title: "Routine: @hi.oneup trend digest v3"
date: 2026-10-15
type: plan
tags: [docs]
status: draft
source: "oneup-studio (soạn trong repo)"
---

# Routine: @hi.oneup trend digest v3
Schedule: daily 07:55 (Asia/Saigon). On Sundays, after the daily run, also run the weekly synthesis.

Prompt:
Run the @hi.oneup trend digest using skill "Trend digest" v3 (repo copy: skills/trend-digest/SKILL.md).
1. `cd /workspace/oneup-studio-sync` (clone https://github.com/vanhieptech/oneup-studio if missing); `git pull --ff-only`. If /workspace/oneup-studio has newer unpushed commits, read rules/skills/scripts (incl. pipeline/scripts/trend-collect.py, pipeline/trends/sources.yaml) from there.
2. X: call GetDynamicTools {namespace:"x"}, then get_trends_by_woeid (23424984, 1) and search_news for 3 niche queries (habits/productivity, AI work, Vietnam gen Z), max_age_hours 72. Save research/trends/YYYY-MM-DD/x-extra.json (source,title,url,cat,lang,rank). If discovery fails, retry once, then log the exact error.
3. Run `python3 pipeline/scripts/trend-collect.py --date YYYY-MM-DD --out research/trends/YYYY-MM-DD --extra research/trends/YYYY-MM-DD/x-extra.json`. Expect ≥30 sources ok and ≥150 raw items; if fewer, say which failed and why. Do not try TikTok Creative Center, Reddit or rsshub.app (known blocked). Never log in, never use cookies or paid APIs.
4. Build raw.json from collect.json: hand-review a 15–25 item shortlist (scores, patterns, safety), then `python3 pipeline/scripts/trend-learn.py score <raw.json>`.
5. Mine hook patterns into patterns.md, write bridges with a differentiation line (consensus vs our Hiệp/Omi comic + HowToLiveBetter angle, lessons only from theme-map/book), plan stubs for the top 1–2 ideas with `trend-learn.py stub`, validated by `cd video-engine && npm run validate -- <plan>` (npm ci first if needed; say so if it can't run).
6. Write digest.md, update ingest.md and idea-bank. Do not commit/push the user's repo, do not send messages, do not post anything.
7. If Sunday: weekly synthesis → research/trends/weekly/YYYY-Www.md. Never invent performance numbers.
8. ALWAYS end the run by delivering the final message below to the user in this chat, even if some steps failed (a run without this message counts as failed).

Final message (Vietnamese, delivered to Hiệp):
"Trend hôm nay (DD/MM): quét N/M nguồn, X mục thô → Y mục qua lọc.
Top 10: <tên trend> – <nguồn có link> – <bài học/clip> (×10)
2 ý nên làm: <bridge + Mọi người nói / Góc của mình> + đường dẫn bản nháp kịch bản
Học được: <pattern mới / chủ đề bão hoà nên tránh>
Nguồn lỗi: <nguồn: lý do>
Cần bạn duyệt: <mục caution / chuyện thật cần xác nhận>"
