# Rule Review — clip-05 r15.1 PATCH1, review delta (chỉ đọc), 08/11/2026 ~14:05 giờ VN
- File: SHA 57322fba…0183c, khớp.
- Lời: ee0e5aa8…0652, khớp (trích sau dòng marker + LF, giữ LF cuối); 433 từ.
- Diff lời so với r15: chỉ đổi S01 (dòng đầu khối lời). S02–S21 giữ nguyên byte, gồm cả S18 «nhỉnh hơn».
- Luật/skill (mtime 13:06 / 12:40 / 13:02) không đổi.

## Kết luận: ĐỦ CHUYỂN SANG GATE NGUỒN (Deep/Social trên SHA ee0e5aa8). KHÔNG phải PASS tổng.

### K1 — ĐÓNG ở mức văn bản
S01 mới: «Trong thí nghiệm, đọc lại thua tự viết về số ý sinh viên nhớ đúng sau hai ngày, ở hai đoạn khác nhau.»
- Bỏ «cùng đoạn». Câu nói rõ hai thao tác làm trên hai đoạn khác nhau, khớp với S07 và lock §3. Không còn hình sai thiết kế.
- «thua» tạo thế so tài rõ hơn bản cũ. Chiều kết quả 2 ngày đúng; không đọc 68/54.
- S03 «thí nghiệm năm 2006 này» giờ có chỗ quy chiếu là «thí nghiệm» ở S01. Rõ.
- Nghe một lần: CHƯA KIỂM bằng người thật.

### Rủi ro còn lại trong delta (sở thích / rủi ro, không chặn)
- Đuôi «ở hai đoạn khác nhau» đứng cuối câu như một vế phụ, dễ bị nghe lướt. «Trong thí nghiệm» chưa xác định thí nghiệm nào (S03 mới nói rõ). Cụm danh từ «về số ý sinh viên nhớ đúng» nghe khá văn bản.
- R1 của r15 vẫn còn: hook nói về sinh viên, «bạn» xuất hiện ở S04. Hook vẫn thiên giọng báo chí. Đây là rủi ro craft cần người thật nghe, không phải blocker luật. Không đặt thêm điều kiện về pain cá nhân.

### K2 «nhỉnh hơn» (S18) — CHƯA ĐÓNG, chuyển cho Deep
- Câu không đổi. Theo phân vai, đây là rủi ro diễn đạt mức độ (wording) thuộc gate nguồn của Deep. Rule Reviewer không tự khóa effect size.
- Nếu Deep đánh dấu, phải sửa trước khi trình Hiệp. Nếu Deep chấp nhận, ghi rõ lý do trong verdict nguồn.

### Không mở lại
Toàn bộ mục "Đạt" ở /workspace/clip05-r15-rule-review-2026-11-08.md vẫn áp dụng, vì S02–S21 giữ nguyên byte.

## Còn thiếu (riêng từng gate)
- Deep/Social verdict trên SHA ee0e5aa8: CHƯA CÓ.
- Checker đầy đủ trong thư mục clip: CHƯA CHẠY.
- Đọc to / người lạ nghe hook / nghe một lần: CHƯA KIỂM.
- Timing thật: CHƯA KIỂM. ƯỚC khoảng 179–203s: target 120–180s chỉ cảnh báo, tổng <300s. Không ảnh trước Chốt.
