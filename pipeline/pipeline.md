---
id: pipeline
type: workflow
status: active
updated: 2026-10-12
tags: [pipeline, workflow]
---
# Pipeline sản xuất 1 clip (theo rules v2)
| # | Bước | Công cụ | Ai làm | Kết quả lưu ở |
|---|---|---|---|---|
| 0 | Đọc lại `logs/decision-log.md` (luật 33) | | Agent | |
| 1 | Chọn ý tưởng + theme | `content/idea-bank.md`, `content/theme-map.md` | Agent | |
| 1b | Đọc `research/trends/ingest.md` + digest mới nhất, chọn ≥1 cụm từ / tình huống (rule-37) | skill trend-digest | Agent | ghi id trend vào script |
| 1c | Chọn bridge (trend → bài học → hook) từ `research/trends/ingest.md` §Bridges, đổi góc so với clip trước (rule-39) | skill trend-digest | Agent | ghi bridge id vào script |
| 2 | Script VI + bản dịch EN + shot list + beat sheet nháp | template trong `content/clips/clip-01-*` | Agent | `content/clips/NN-slug/` |
| 2a | Polish script: humanizer + voice profile, khoá fact, lưu draft vX.Y (rule-40) | `skills/script-polish` | Agent | `script-vX.Y-draft.md` |
| 2b | Storyboard: 1 frame 1080×1920 mỗi beat + contact sheet, tự xem và sửa ≥2 vòng (luật 34–35) | HTML + headless Chrome `pipeline/storyboard/render.py <clip-dir>` đọc `storyboard/spec.json` (rule-36) | Agent | `content/clips/NN-slug/storyboard/` |
| 3 | Duyệt script + storyboard | Hiệp | Tay | |
| 4 | Thu giọng + quay b-roll | iPhone | Hiệp | AirDrop vào `footage/inbox/` |
| 5 | Làm sạch âm thanh (cắt khoảng lặng >0,6s, −14 LUFS) | `scripts/01-audio-clean.sh` (FFmpeg) | Tự động | `footage/NN-slug/` |
| 6 | Transcribe, lấy timestamp từng từ | `scripts/02-transcribe.sh` (whisper.cpp large-v3) | Tự động | `captions.vi.json` |
| 7 | Rải caption EN theo cụm câu | `scripts/03-align-en.py` | Tự động | `captions.en.json` |
| 8 | Beat sheet có thời gian thật | agent | Tự động | `beats.json` |
| 9 | Chọn motion | `skills/motion-picks-per-script` | Tự động | `logs/effects-log.md` |
| 10 | Lấy tài sản (Pexels/Pixabay, Phosphor, SFX CC0) | `scripts/04-fetch-assets.py` | Tự động | `assets/` |
| 11 | Dựng composition | `templates/hyperframes-base` (+ Manim cho biểu đồ) | Agent | `content/clips/NN-slug/comp/` |
| 12 | Render nháp | box | Tự động | `renders/NN-slug/draft.mp4` |
| 13 | QA (lint, snapshot, safe-zone, dấu tiếng Việt, LUFS, checklist anti-AI) | `scripts/05-qa.sh` | Tự động | `qa.md` |
| 14 | Render final | Mac | Tự động | `renders/NN-slug/final.mp4` |
| 15 | Duyệt final + đóng gói (caption, hashtag, credit, cover) | Hiệp duyệt | | `renders/ready/` |
| 16 | Đăng + thêm nhạc TikTok | Hiệp | Tay | |

Công tay của Hiệp: khoảng 30–45' mỗi clip. Máy và agent chạy: khoảng 20–30'.
**Script trong `pipeline/scripts/` còn là placeholder, chưa viết.**

## Vòng góp ý (rule-36)
Hiệp góp ý → ghi vào `logs/decision-log.md` (DL-0xx) → sửa nguồn (`spec.json`, `script.md`, renderer) → render lại → tự xem lại (rule-34) → commit `fix(clip-NN): ... (DL-0xx)` → push.

## Trend hằng ngày (rule-38)
Job trên box chạy skill trend-digest và ghi vào `/workspace/oneup-studio-sync/research/trends/` → agent đóng gói, gửi sang `../.oneup-sync/trends.tgz` → `pipeline/scripts/sync-trends.sh` → commit và push.
