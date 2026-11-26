---
title: "Thư viện script mode (công thức khung từ clip nhiều view)"
date: 2026-11-26
id: research.blueprints
type: research
status: living
updated: 2026-11-26
tags: [blueprints, script-mode, teardown, trend]
source: "pipeline/scripts/teardown.py (Gemini CLI) gộp mục `formula` của mỗi bản phân tích; templates/clip-teardown.md mục 11"
---
# Thư viện script mode

Mỗi script mode là một công thức khung 4–6 bước, trừu tượng, dùng được cho chủ đề khác (không chứa nội dung clip gốc). `teardown.py` tự gộp: công thức giống một mode có sẵn ≥ 0,6 thì `seen` + 1 và thêm nguồn; không thì tạo mode mới `SMnn`.

`index.json`: `{"modes": [{"id", "formula": [...], "seen", "uses", "wins", "sources": [...]}]}`
- `seen`: số clip nhiều view dùng khung này (từ teardown).
- `uses`: số clip của mình dùng khung này (make-video gate 0 ghi khi Hiệp chọn).
- `wins`: số clip của mình dùng khung này có số liệu tốt (trend-digest weekly, theo `content/published/README.md`).

Gate 0 (make-video §2.0) đọc thư viện này để gieo góc; ưu tiên mode `seen` cao, chưa dùng ở 3 clip gần nhất.
