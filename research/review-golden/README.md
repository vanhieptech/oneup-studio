---
title: "Bộ mẫu chuẩn review script: các bản Hiệp duyệt và bác thật"
date: 2026-11-26
id: review-golden
type: reference
status: active
updated: 2026-11-26
tags: [review, golden-set, reviewer, script, calibration, clip-05, clip-06]
source: "logs/lessons.md (L-084…L-107), logs/decision-log.md (DL-041, DL-063, DL-069), git history (git show <commit>:<path>), content/archive/clip-0{1..5}-*/final/"
---

# Bộ mẫu chuẩn review script

Đây là bộ mẫu để hiệu chỉnh reviewer độc lập và người viết script. Mỗi mẫu là một lần Hiệp thật sự duyệt hoặc bác: lời của bản đó, câu Hiệp nói nguyên văn, và bài học rút ra. Reviewer chấm một bản nháp mới phải cho ra cùng kết luận với Hiệp trên các mẫu này. Nếu không, reviewer đang lệch.

## Cấu trúc

- `index.json` là danh sách máy đọc của mọi mẫu.
- `rejected/<id>.md` chứa từng bản bị bác: front-matter, «Hiệp nói», lời bản bị bác (chép nguyên văn từ nguồn), và «Vì sao bác».
- Bản được duyệt chỉ trỏ tới file trong `content/archive/` và không chép lời sang đây.

Mỗi mẫu trong `index.json` có các trường:

| Trường | Nghĩa |
|---|---|
| `id` | `r-cNN-<bản>` (bị bác) hoặc `a-cNN` (duyệt) |
| `verdict` | `approved` hoặc `rejected` |
| `source` | đường dẫn file, hoặc `git show <commit>:<path>` |
| `hiep_quote` | lời Hiệp nguyên văn; dấu `|` tách các tin nhắn khác nhau |
| `quote_kind` | `verbatim` (Hiệp gõ), `relayed` (lời agent chuyển lại), `verbatim-instruction` (nguyên văn nhưng chỉ là lệnh «làm lại», không có lý do), `none` |
| `lesson` / `lesson_id` | bài học, kèm id `L-NNN` / `DL-NNN` nếu có |
| `excerpt_file`, `found` | file trích lời; `found: false` nghĩa là chưa tìm thấy lời của bản đó |

## Số mẫu

Có 25 mẫu: 5 bản duyệt và 20 bản bị bác. Trong 20 bản bị bác, 16 bản có lời đầy đủ. Bản r15.3 chỉ có ba câu hook, lấy từ nguồn thứ cấp. 4 bản chưa tìm thấy lời.

| id | bản | Hiệp nói (rút gọn) | lesson |
|---|---|---|---|
| r-c05-v2 | clip-05 v2 | Sao không có trend gì hết | L-084 |
| r-c05-v4 | clip-05 v4 (đã Chốt) | …lấy ví dụ từ sinh học không phổ biến lạc đề… | L-087 |
| r-c05-r4 | v5 r4 | Xàm quá dậy lúc review m đọc k thấy nó rời rạc à | L-089 |
| r-c05-r53b | v5 r5.3b | …sao t thấy m review ngu quá / ví dụ ngu… | L-090 |
| r-c05-r65 | r6.5 | Trong 3 ý đầu hơi lòng vòng… | L-091 |
| r-c05-r67b | r6.7b | Ý 2 đọc không liên quan giữa các câu | L-092 |
| r-c05-r68 | r6.8 | …chưa có chiều sâu còn lủng củng lặp từ quá nhiều | L-093 |
| r-c05-r612 | r6.12 | Quá lộn xộn các câu thiếu liên kết… | L-094 |
| r-c05-r82 | r8.2 | Tệ quá làm lại từ đầu… sáng tạo hơn xem | L-095 |
| r-c05-r92 | v9 r9.2 | …hook đâu dẫn chứng đâu câu văn cộc lôc xàm | L-096 |
| r-c05-r114 | r11.4 | (không có nguyên văn, chỉ có lời chuyển) | L-098 |
| r-c05-r153 | r15.3 (chỉ hook) | hook xàm (lời chuyển) | L-101 |
| r-c05-r174 | r17.4 | nghĩa rời rạc (lời chuyển); **chưa tìm thấy lời** | L-102 |
| r-c05-r183 | r18.3 | …hook vẫn cộc lốc… theo hướng story telling; **chưa tìm thấy lời** | L-103 |
| r-c05-r1921 | r19.2.1 | Xàm quá; **chưa tìm thấy lời** | L-104 |
| r-c05-r201 | r20.1 C1 | Xàm / Lời văn sến, giả, không giống người nói; **chưa tìm thấy lời** | L-105 |
| r-c06-v2 | clip-06 v2 | làm lại script mới | (không có lý do) |
| r-c06-v3 | clip-06 v3 | Script vẫn xàm thiếu tự nhiên… | L-106 |
| r-c06-v3r2 | v3 r2 | …rời rạc… không có cấu trúc tuần tự… | L-107 |
| r-c06-v3r3 | v3 r3 | làm lại | (không có lý do) |
| a-c01…a-c05 | clip-01…05 bản cuối | xem `index.json` | |

## Cách dùng

1. **Reviewer:** đọc các mẫu duyệt trước để biết thế nào là đạt, rồi đọc các mẫu bị bác. Khi chấm bản mới, đối chiếu xem bản đó có mắc đúng lỗi của mẫu nào không, và nêu `id` mẫu đó. Không chấm đạt một bản giống mẫu bị bác chỉ vì nó qua checker. Hầu hết các mẫu bị bác ở đây đều đã qua checker và đã được Rule Reviewer chấm ĐẠT.
2. **Người viết:** không chép câu từ mẫu nào, kể cả mẫu duyệt. Mẫu cho biết lỗi cần tránh, không phải câu để dùng lại.
3. **Hiệu chỉnh:** chạy reviewer trên từng mẫu, ẩn `hiep_quote` và `lesson`. Reviewer phải trả CHƯA ĐẠT cho mọi mẫu `rejected` có `found: true`, và ĐẠT cho mẫu `approved`.
4. **Thêm mẫu:** mỗi lần Hiệp duyệt hoặc bác, thêm một mục vào `index.json`. Với bản bị bác, thêm `rejected/<id>.md` với lời chép bằng `git show`, không gõ lại.

## Giới hạn và chỗ còn thiếu

- **Chưa tìm thấy lời** của r17.4, r18.3 (`ea3236c0`), r19.2.1 (`f60b1ced`) và r20.1 C1 (`85c30f19`). Các hash này nằm trong lessons nhưng không có trong lịch sử git của repo này, có lẽ là commit trên box cũ. File của bốn bản chỉ có câu Hiệp nói và bài học. Lời không được dựng lại.
- **r15.3:** file nháp gốc không có trong repo. Ba câu hook S01–S03 được chép từ `research/craft/hook-script-study-2026-11-11.md:230`.
- **r11.4:** không có câu Hiệp nói nguyên văn. L-098 chỉ ghi tóm tắt của Rule Reviewer, nên `hiep_quote` để `null`.
- **Lời chuyển:** r15.3 và r17.4 là lời agent chuyển lại, không phải tin Hiệp gõ trực tiếp (`quote_kind: relayed`).
- **clip-06 v2 và v3 r3:** Hiệp chỉ nói «làm lại», không nêu lý do. Phần «Vì sao bác» không suy diễn thêm.
- **Bản duyệt clip-04:** mẫu trỏ tới `final/script-v18-LOCKED.md`, không trỏ tới `final/script-final.md`, vì file script-final.md đó là nháp script-v07 cũ (status: draft).
- **Bản duyệt clip-01 và clip-02:** chưa tìm thấy chữ duyệt nguyên văn. Mục trong index chỉ ghi nguồn gián tiếp (DL-041; post.md «Hiệp duyệt bản v17 final 16/10»). Front-matter script-final.md của clip-02 vẫn ghi `status: draft`.
- **Không đưa vào:** r16 C1–C3 (Hiệp bác 11/11 nhưng không có câu nguyên văn) và r10.2 (không có kết luận của Hiệp).

## Kết quả đo reviewer

| Ngày | Model | Bắt đúng bản bị bác | Cho qua bản đã duyệt | Ghi chú |
|---|---|---|---|---|
| 2026-11-26 | sonnet | 15/15 (100%) | 0/3 (0%), thêm 2 bản không có verdict | **Reviewer quá khắt khe: bác mọi bản, kể cả bản Hiệp đã duyệt.** Chưa dùng được làm cổng. Cần nới quy tắc verdict trong `docs/prompts/reviewer-script.md`, rồi đo lại. Chi phí 8,67 USD. Chi tiết: `eval-2026-11-26.json` |
| 2026-11-26 (b) | sonnet | 14/15 (93%) | 1/5 (20%) | Reviewer 2 tầng (DL-074), verdict tính bằng `pipeline/review_tiers.py`. Bản duyệt được 68–85 điểm, bản bị bác 57–87: thang điểm bị nén. Điểm trừ ở bản duyệt đến từ chuyện cá nhân chưa xác nhận, markup spec, claim không mở được nguồn, kiểu CTA. Bản bị bác lọt: r-c06-v3r3 (87; Hiệp chỉ nói «làm lại»). Chi phí 8,90 USD. `eval-2026-11-26b.json` |
| 2026-11-26 (c) | sonnet | đang chạy | đang chạy | Thêm neo điểm (bản duyệt gần nhất = 88), danh sách không trừ điểm, bỏ markup khỏi nháp khi đo. Kết quả ghi khi chạy xong: `eval-2026-11-26c.json` |
