# Review clip-05 v10 r10.1 (dff0075), Rule Reviewer, 31/10 18:10

**Kết luận: CHƯA ĐẠT, còn 1 lỗi chặn + 3 lỗi nhỏ.** 11 mode tự động (--subjects, --l088, --trend, --flow, --fresh, --link, --repeat, --clarity, --evidence, --choppy) PASS. ⚠ --clarity (câu hỏi b01 trước tình huống) chấp nhận vì luật hook là nói thẳng nỗi đau + hỏi, và S2 trả lời ngay. rule-48 (spec.json) chưa tính vì còn nháp. Đây là vòng vá 1 của v10.

## Ba lỗi chặn của r10: đã sửa
1. S5 gọi tên «tự nhớ như vậy là tự kiểm tra» trước khi S6 dùng «Cách này». Đạt L-094.
2. S2 «Muốn nhớ sách» đặt mục đích nhớ trước «cách ôn». Đạt về chữ, nhưng xem lỗi chặn mới bên dưới.
3. S2 trả lời câu hỏi hook ngay sau S1. Đạt.

## Lỗi chặn
1. **S3 (L-090 manual gate, L-096 (4), L-094): ví dụ gượng, không phải việc người theo trend thật sự làm.**
   - Hook (S1) là người đổi giờ lướt điện thoại sang đọc sách, tức đọc một lượt cho vui rồi gấp lại. Nỗi đau trong bằng chứng xã hội (E5, E6 «đọc xong quên hết») cũng là đọc một lượt rồi quên.
   - S3 lại cho người xem «đọc một chương hai lượt», để khớp với đọc đi đọc lại của Dunlosky. Người đọc sách giải trí hiếm khi đọc lại một chương hai lần, nên ví dụ được dựng cho vừa dẫn chứng chứ không lấy từ trải nghiệm thật.
   - Hệ quả: S2 «có khi do cách ôn» giả định người xem có ôn bằng đọc lại, trong khi người theo trend thường không ôn gì. Chuỗi lý lẽ S1→S2→S3→S6 bị hở đúng chỗ Hiệp hay bắt (L-096 «trend phải là trải nghiệm thật»).
   - «sáng bị hỏi»: chưa rõ ai hỏi và vì sao lại hỏi về cuốn sách đang đọc giải trí (L-094: không đưa hành động/người chưa dẫn vào).
   - Hướng (không viết câu thay, L-093b): OpenCreator chọn một trong hai, rồi Deep Research xác nhận dẫn chứng còn đúng phạm vi: (a) giữ trend đọc sách, đổi ví dụ thành việc người đọc thật sự làm và chọn dẫn chứng so đúng việc đó; hoặc (b) giữ Dunlosky đọc lại và đổi sang tình huống người xem thật sự đọc lại để nhớ.

## Lỗi nhỏ (sửa cùng lượt)
2. **S10 (P-03 không bịa):** «bạn thường nói được vài ý» là lời hứa kết quả chưa có nguồn trong evidence-lines-v10 hay F5. Cần Deep Research xác nhận câu này truy được về 23.14, hoặc hạ xuống mức nguồn cho phép.
3. **Caption b02/b03 lệch beat:** «Maybe it's the review method» nằm ở b03 nhưng lời tương ứng ở b02 (S2). Caption b02 thiếu ý «muốn nhớ sách», b03 thiếu ý «tự nhớ như vậy là tự kiểm tra».
4. **Caption b05:** chỉ «Say three main ideas out loud», trong khi S8 là «kể hoặc viết ra».

## Đạt
- L-096 (1) lý do dừng lướt có ghi; (2) câu dẫn chứng S5–S6 đủ ai, so A với B, kết quả đúng chữ evidence-lines-v10 cách A, không «vô ích»; (3) 1/11 câu ≤10 chữ, không hai câu cộc liền; L-095 ba concept + khoảnh khắc «bộp» có ghi.
- L-093: không từ >5%, không cụm 3 chữ lặp. L-087: không môn học. 175 chữ, câu dài nhất 23 chữ. Caption EN ≤8 từ mỗi chunk.
- End card: câu an toàn, CC BY 4.0, nguồn, không ghi bảo trợ.

## Ghi chú
- Chưa có bảng cảnh 9 cột (W-04), làm sau khi Hiệp Chốt, trước giọng.
- Nếu r10.2 còn trượt và tới vòng vá 3 thì theo L-094 phải viết lại toàn bài.
