---
title: "Mẫu Viral DNA Card (teardown clip đối thủ đạt chuẩn outlier)"
date: 2026-11-26
id: template.clip-teardown
type: template
status: ready
updated: 2026-11-26
tags: [template, trend, teardown, retention, viral-dna, arc]
source: "oneup-studio: 7 khối Viral DNA + Craft Transfer (nâng cấp từ 6 khối 26/11); prompt docs/prompts/gemini-teardown.md; renderer pipeline/scripts/teardown.py"
---
# Viral DNA Card: <tên ngắn> (`<creator>-<tiktok id>`)

Một file mỗi clip: `research/trends/<YYYY-MM-DD>/teardowns/<id>.md` + `<id>.json` (cùng cấu trúc). `teardown.py` sinh file này; Claude chỉ bổ sung chỗ ghi «—». Nguồn mỗi ý: **[Apify / yt-dlp]** số liệu / phụ đề / comment, **[agy]** model xem + nghe video (Antigravity CLI, `teardown.py`), **[Claude]** tổng hợp. Mỗi ý ghi `quan sát` (có mốc giờ) hoặc `suy đoán`. Không chép câu, hình, âm thanh vào clip của mình; chỉ mượn khung trừu tượng và kỹ thuật kể chuyện.

Chỉ teardown clip đạt chuẩn outlier của radar (`pipeline/scripts/radar-fetch.py` / `trend-streams.py radar`: view ÷ follower ≥ 3, hoặc view ÷ median ≥ 3, hoặc comment/share tăng đột biến trong 24–72 giờ) hoặc clip Hiệp ném vào inbox. Ghi rõ `role` kênh (`direct_niche` · `cross_niche_craft` · `anti_pattern`).

## Khối 0 — Số liệu [Apify]
| link | creator | follower | view | view/follower | comment | share | độ dài | ngày đăng |
|---|---|---|---|---|---|---|---|---|

## Khối 1 — Hook Mechanics (0–3 giây) [agy + phụ đề Apify]
- Câu mở đầu (nguyên văn khi nghe rõ, chỉ để phân tích): …
- Visual / text hook trên màn hình: …
- Cơ chế tâm lý: **phản trực giác · nỗi đau · tò mò · kết quả sốc** · khác (`suy đoán`)
- Lời hứa ngầm với người xem: …

## Khối 2 — Story Arc & Beat Map [agy]
4–6 beat theo mốc giờ, phủ toàn video. Vai trò chỉ dùng: hook, dẫn dắt, câu hỏi, chứng minh, lật kèo, giải thích, áp dụng, kết.
| mốc | giây | vai trò | chức năng giữ chân | tóm ý | chuyển ý (câu / kỹ thuật) sang beat sau |
|---|---|---|---|---|---|
- Giây trả lời lời hứa của hook: …

## Khối 3 — Winning Points [agy + Claude]
- Ẩn dụ / ví dụ đời thường đắt nhất (mốc giờ): …
- Câu đáng lưu / share (quotable line, mốc giờ): …
- Tần suất ngắt nhịp hình / âm thanh: … lần / 10 giây; các điểm nổi bật `0:04 SFX + zoom` …
- Dịch sang kênh: @hi.oneup = đổi cảnh comic, hit motion + SFX (luật 50, 51), không quay, không b-roll, không nhạc (DL-027, luật 21) · @vanhiep.tech = overlay `ov-*` / cutaway `cu-*` mỗi 3–5 giây (`make-layer`).

## Khối 4 — Algorithmic Triggers [agy + comment Apify]
- Kích bình luận (tranh luận / đồng cảm / hỏi thêm): … — người xem thật nói gì (cụm ngắn kèm link, không ghi tên).
- Kích lưu / chia sẻ (checklist / kiến thức ngách / gửi bạn bè): …

## Khối 5 — Reusable Story Arc (`ARC-NNN`) [agy → Claude]
Khung xương trống, mọi nội dung riêng thay bằng `[...]`, dùng được cho chủ đề khác:
1. [...]
- `teardown.py` tự gộp vào thư viện (`pipeline/arc_library.py`): giống mạch có sẵn ≥ 0,6 hoặc cùng nguồn → cộng bằng chứng vào `ARC` đó; không thì cấp `ARC-NNN` mới. Bảng: `research/trends/patterns.md` › Story arcs.

## Khối 6 — Dual-Channel Angle [agy / Claude, `suy đoán`, Hiệp chọn ở Gate 0]
- **@hi.oneup** (comic + motion, 120–180 s): ý · hook nháp · độ dài.
- **@vanhiep.tech** (talking-head + overlay, 45–90 s): ý · hook nháp · độ dài.
- Tự đẩy vào `content/idea-bank.md` › Từ teardown (ARC), kèm mã `ARC-NNN` và link file này.

## Khối 7 — Craft & Voice Transfer (Kỹ thuật ngôn ngữ & Nhịp cắt học được) [agy + comment]
- **Ẩn dụ chuyển hóa khái niệm khó → đời thường:** cách tác giả biến khái niệm trừu tượng/kỹ thuật thành hình ảnh mắt thấy tai nghe.
- **Cách ngắt câu & nhịp nói:** độ dài câu, cách dùng câu ngắn/dừng nhịp/từ nối để giữ người xem không tụt chú ý.
- **Kỹ thuật giữ nhịp mỗi 3–5s:** visual interrupt, đổi góc/overlay/đạo cụ hoặc micro-payoff mỗi 3–5 giây (áp sang comic+motion hoặc `ov-*`/`cu-*`).
- **Câu hỏi / nỗi đau thật từ comment khán giả:** cụm câu hỏi/nỗi đau ẩn danh tự động đẩy sang `resources/vn-spoken/audience-pain-bank.md`.

## Vì sao nó chạy [agy / Claude] (`suy đoán`, mỗi ý chỉ vào bằng chứng ở Khối 1–4)
1. …
