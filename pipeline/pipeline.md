---
id: pipeline
type: workflow
status: active
updated: 2026-10-13
tags: [pipeline, workflow]
---
# Pipeline sản xuất 1 clip (theo rules v3.1, series comic-only)
| # | Bước | Công cụ | Ai làm | Kết quả lưu ở |
|---|---|---|---|---|
| 0 | Đọc lại `logs/decision-log.md` (luật 33) | | Agent | |
| 1 | Chọn ý tưởng + theme | `content/idea-bank.md`, `content/theme-map.md` | Agent | |
| 1a | Xem plan stub + dòng khác biệt trong digest mới nhất (`research/trends/<ngày>/plans/`), dùng làm điểm xuất phát cho `content/clips/NN-slug/comic/plan.json` (rule-47) | skill trend-digest v2 | Agent | |
| 1b | Đọc `research/trends/ingest.md`, `patterns.md` + digest mới nhất, chọn ≥1 cụm từ / tình huống (rule-37) | skill trend-digest | Agent | ghi id trend vào script |
| 1c | Chọn bridge (trend → bài học → hook) từ `research/trends/ingest.md` §Bridges, đổi góc so với clip trước (rule-39) | skill trend-digest | Agent | ghi bridge id vào script |
| 1d | Chọn chuyện thật từ `content/story-bank.md`, hỏi Hiệp những chi tiết còn thiếu (rule-41) | | Agent + Hiệp | |
| 2 | Script VI + bản dịch EN + danh sách câu cần thu + beat sheet nháp (comic/motion cho từng beat) | template trong `content/clips/clip-01-*` | Agent | `content/clips/NN-slug/` |
| 2a | Polish script: humanizer + voice profile, khoá fact, lưu draft vX.Y (rule-40) | `skills/script-polish` | Agent | `script-vX.Y-draft.md` |
| 2b | Storyboard: 1 frame 1080×1920 mỗi beat + contact sheet, tự xem và sửa ≥2 vòng (luật 34–35) | HTML + headless Chrome `pipeline/storyboard/render.py <clip-dir>` đọc `storyboard/spec.json` (rule-36) | Agent | `content/clips/NN-slug/storyboard/` |
| 3 | Duyệt script + storyboard | Hiệp | Tay | |
| 4 | Thu giọng (không quay hình, luật 6) | iPhone | Hiệp | AirDrop vào `footage/inbox/` |
| 5 | Làm sạch âm thanh (cắt khoảng lặng >0,6s, −14 LUFS) | `scripts/01-audio-clean.sh` (FFmpeg) | Tự động | `footage/NN-slug/` |
| 6 | Transcribe, lấy timestamp từng từ | `scripts/02-transcribe.sh` (whisper.cpp large-v3) | Tự động | `captions.vi.json` |
| 7 | Rải caption EN theo cụm câu | `scripts/03-align-en.py` | Tự động | `captions.en.json` |
| 8 | Beat sheet có thời gian thật | agent | Tự động | `beats.json` |
| 9 | Chọn motion | `skills/motion-picks-per-script` | Tự động | `logs/effects-log.md` |
| 10 | Lấy tài sản (Phosphor, SFX CC0; không stock người thật) | `scripts/04-fetch-assets.py` | Tự động | `assets/` |
| 10b | Giọng Omi (nếu tuần ≥ 5 và Omi nói) | `npm run voice` (VieNeu-TTS local, luật 46) → `plan.voiced.json` + ASR kiểm chữ | Tự động | `video-engine/public/voice/` |
| 10c | Prosody giọng (DL-033): line có `phrases` → cụm hơi + nghỉ 150–420ms + nhấn + 3 take/cụm chọn theo STT/F0/lỗi + master | `pipeline/scripts/voice-prosody.py` (gọi từ `build-final.py`; `--metrics a.wav` để đo F0/pause) | Tự động | `video-engine/public/voice/vp-*.wav|json` |
| 11 | Dựng composition | Beat kể chuyện: `video-engine/` (Remotion, plan JSON, luật 45). Beat giải thích: `templates/hyperframes-base` (HyperFrames, Node ≥ 22; + Manim cho biểu đồ). **Bắt buộc đọc trước** `skills/hyperframes/` (router → core → animation → creative → registry → cli) và chạy `hyperframes lint`. Ghép: `pipeline/scripts/join-beats.sh` | Agent | `content/clips/NN-slug/comp/`, `out/*.mp4` |
| 12 | Render nháp | box | Tự động | `renders/NN-slug/draft.mp4` |
| 13 | QA (lint, snapshot, safe-zone, dấu tiếng Việt, LUFS, checklist anti-AI) | `scripts/05-qa.sh` | Tự động | `qa.md` |
| 14 | Render final | Mac | Tự động | `renders/NN-slug/final.mp4` |
| 15 | Duyệt final + đóng gói (caption, hashtag, credit, cover) | Hiệp duyệt | | `renders/ready/` |
| 16 | Hiệp tự đăng (không có nhắc, luật 32) + thêm nhạc TikTok (+ bật nhãn "AI-generated content" nếu có giọng Omi, luật 46) | Hiệp | Tay | |

Công tay của Hiệp: khoảng 30–45' mỗi clip. Máy và agent chạy: khoảng 20–30'.
**Script trong `pipeline/scripts/` còn là placeholder, chưa viết.**

## Vòng góp ý (rule-36)
Hiệp góp ý → ghi vào `logs/decision-log.md` (DL-0xx) → sửa nguồn (`spec.json`, `script.md`, renderer) → render lại → tự xem lại (rule-34) → commit `fix(clip-NN): ... (DL-0xx)` → push.

## Trend hằng ngày (rule-38)
Job trên box chạy skill trend-digest trong `/workspace/oneup-studio`, ghi thẳng vào `research/trends/` → commit trên box → agent đẩy bundle qua Mac → push. `check-assets.py` chặn asset nằm ngoài repo.
