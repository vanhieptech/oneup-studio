---
title: "GUIDE: đọc gì trước khi làm"
date: 2026-10-15
type: guide
tags: [guide, storage, reuse-first]
status: ready
source: "Hiệp content-bot prompt (docs/prompts/content-bot-prompt.md)"
id: guide
---
# GUIDE: đọc gì trước khi làm

Repo đã có guide, file này chỉ trỏ tới, không chép lại:
- Nơi lưu mọi loại file, bảng ánh xạ từ cấu trúc mặc định của prompt: `docs/conventions/storage.md` (nguồn chuẩn duy nhất).
- Cách AI làm việc trong repo: `AGENTS.md`. Cây thư mục: `README.md`. Danh mục: `INDEX.md` (sinh bằng `pipeline/scripts/build-index.py`).
- Quy trình một video: `docs/workflow/per-video-pipeline.md`. Luật: `rules/video-rules.md`. Bài học: `logs/lessons.md`.
- Front-matter bắt buộc cho file `.md` nội dung: `title, date, type, tags, status, source` (`check-assets.py` chặn khi thiếu).
- Commit: `<loại>: <mô tả>` (feat, fix, docs, chore, content, research, refactor).
- Reuse-first: tìm (`git grep`, `INDEX.md`, `pipeline/scripts/dup-scan.py`) trước khi tạo; trùng thì đề xuất gộp, không xoá.
