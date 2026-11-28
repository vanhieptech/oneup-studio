---
title: "pipeline/legacy: script một lần của clip cũ"
date: 2026-11-28
type: guide
tags: [pipeline, legacy, agents]
status: ready
source: "oneup-studio (agent-native setup)"
id: pipeline.legacy
updated: 2026-11-28
---
# pipeline/legacy — script một lần của clip cũ (đóng băng)

Các script `clip-02…clip-05-*` và `stem-prosody.py` được dùng một lần cho clip đã duyệt (nay ở `content/archive/`).
Chúng **không** thuộc pipeline hiện hành (`skills/make-video/SKILL.md` dùng `ideate-clip.py`, `build-final.py`, `check-rules.py`…).

- Chuyển từ `pipeline/scripts/` sang đây ngày 28/11/2026 (agent-native setup) để bỏ đường dẫn box cũ khỏi pipeline chính.
- Đường dẫn tuyệt đối cũ đã thay bằng gốc repo tính từ `__file__` (`_REPO`) và `$VOICE_WORK_DIR` (mặc định `~/oneup-tools/voice-work`).
- Script vẫn trỏ `content/clips/clip-0N-…` như lúc viết; clip đó nay đã nằm ở `content/archive/`. **Không chạy lại** trên clip đã duyệt; chỉ giữ để tra cứu cách làm.
