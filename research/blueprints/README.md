---
title: "Thư viện mạch cốt truyện ARC-NNN (khung xương từ clip đối thủ đạt chuẩn outlier)"
date: 2026-11-26
id: research.blueprints
type: research
status: living
updated: 2026-11-26
tags: [blueprints, arc, story-arc, viral-dna, teardown, trend]
source: "pipeline/arc_library.py gộp Khối 5 của mỗi Viral DNA Card (pipeline/scripts/teardown.py); SM01 cũ chuyển thành ARC-001 ngày 26/11"
---
# Thư viện mạch cốt truyện `ARC-NNN`

Mỗi `ARC` là một khung xương 4–6 bước, trống (`[...]`), dùng được cho chủ đề khác, kèm nhịp beat (vai trò · giây · chức năng giữ chân) và danh sách bằng chứng (clip đối thủ đạt chuẩn outlier đã teardown).

`index.json` là nguồn máy đọc (nguồn duy nhất):
- `arcs`: `{"id": "ARC-NNN", "legacy_id"?, "name", "skeleton": [...], "beats": [...], "hook_mechanism", "seen", "uses", "wins", "evidence": [{"source", "creator", "ratio", "views", "followers", "date", "teardown"}]}`
  - `seen` = số bằng chứng (tính lại mỗi lần ghi; cùng nguồn chạy lại không cộng thêm).
  - `uses`: số clip của mình dùng mạch này (Gate 0 ghi khi Hiệp chọn). `wins`: clip dùng mạch có số liệu trên trung vị kênh (trend-digest weekly, theo `content/published/README.md` cột «ARC»).
- `ideas`: góc chuyển thể Khối 6 (`arc`, `channel`, `idea`, `hook`, `length_s`, `teardown`, `date`, `status`).

Bảng người đọc được sinh lại từ JSON, không sửa tay: `research/trends/patterns.md` › Story arcs (ARC-NNN) và `content/idea-bank.md` › Từ teardown (ARC). Sửa `uses`, `wins`, `status`, `name` trong `index.json` rồi chạy `python3 pipeline/scripts/teardown.py --rerender <teardown.json>` (hoặc bất kỳ teardown nào) để làm mới bảng.

Gộp mạch: cùng nguồn → làm mới `ARC` đó; không thì độ giống (chuỗi vai trò beat + chữ khung, bỏ phần trong `[...]`) ≥ 0,6 → cộng bằng chứng; còn lại → `ARC` mới. Gate 0 (`pipeline/scripts/gate0.py`) đọc thư viện để gắn mạch cho ý tưởng.
