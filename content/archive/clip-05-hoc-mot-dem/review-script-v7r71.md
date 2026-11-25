# Review clip-05 r7.1 (832413d) — Rule Reviewer, 29/10/2026 15:2x (heartbeat)

**Verdict: CHƯA ĐẠT.** r7.1 chỉ sửa fact b04 theo Deep Research, commit 1 phút sau review r7 (665b962) nên chưa xử lý R1–R10. Chỉ liệt kê lỗi kèm dòng; OpenCreator sửa (L-093b). Đây là vòng vá 1 sau bản viết lại r7 (chưa tới ngưỡng 3 vòng của L-094).

## Máy (7/7 mode PASS)
--subjects ✔ · --trend ✔ · --l088 ✔ · --repeat ✔ · --clarity ✔ · --flow ⚠ (b03, b05 mở beat không nối) · --link ⚠ 5/13 cặp (b01→b01, b03→b03, b04→b05, b05→b06, b06→b06; phần lớn là báo nhầm, cổng tay quyết).

## Đã xử lý ở r7.1
- R5: S8 (dòng 59) «chỉ hơn lúc đầu» khớp mốc «kiểm tra ngay» của F1. ✔
- R9 phần b04: caption b04 (dòng 76) khớp S8–S11. ✔
- R6 một phần: bỏ «không cần chờ đủ một tuần», «chỉ khuyên»; S8→S9 có «Vì vậy». ✔

## Còn mở (từ review-script-v7r7.md, chưa sửa)
- R1 S3 (dòng 54): «khó dùng tới» thiếu tân ngữ; «nhất là khi trên mạng đang bàn…» không phải lý do chuyện quên nặng hơn → trend vẫn gắn vào.
- R2 S3→S4 (dòng 54–55): «Vậy» không rút ra từ S3; «đọc» (S1) đổi thành «xem» (S4).
- R3 S6 (dòng 57): «cách của bạn nhớ hơn» — hơn nhóm nào chưa nói.
- R4 S7 (dòng 58): «Sau hai ngày» — sau mốc nào chưa nói (nguồn dòng 85: hai ngày sau lần đọc cuối); «cách cuối» bắt nhớ thứ tự liệt kê.
- R6 còn lại S9 (dòng 60): «cẩm nang» xuất hiện lần đầu, chưa dẫn vào nguồn mới (L-094).
- R7 S10 (dòng 61): không nói tự kể làm lúc nào (mốc thời gian); «chỗ bạn hụt là tự kể» gọi lại S2 quá xa, nghe một lần lủng củng (L-091).
- R8 caption b03 (dòng 75): «Read once, reread right away, or a week later» = 9 chữ (>8).
- R9 caption b03 (dòng 75): «rereading wins» cùng lỗi R3 (thắng ai).
- R10 S5 (dòng 56): ba nhóm nhồi một câu 23 chữ ngay sau câu hỏi (L-091).

## Ghi chú mới
- Caption b04 «Spread it over a few days instead» (dòng 76): «it» không rõ chỉ gì (việc đọc lại?) — kiểm khi sửa.

## Rủi ro báo Hiệp khi đạt
Tín hiệu trend yếu (bài X News gốc mất, chưa có comment TikTok), quota Apify hết, spec/hình chưa dựng. Chưa Chốt, không giọng/render.
