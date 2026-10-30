# Review clip-05 v9 r9.1 (4387835), Rule Reviewer, 30/10/2026 18:2x

**Kết luận: CHƯA ĐẠT.** Đây là vòng vá thứ 2 của r9 (L-094: tới vòng 3 mà còn lỗi thì phải viết lại cả bài, không vá tiếp).

Check tự động (--subjects, --l088, --trend, --flow, --fresh, --link, --repeat, --clarity): 1 ✖, 3 ⚠.
- ✖ L-090 (--trend): trend_id 2116046143289172179 không có trong research/trends/**, tức chưa phải trend đã lưu nghiên cứu.
- ⚠ --flow b02 «Như…», ⚠ --link S1→S2, S2→S3: đối chiếu bảng cặp câu thì hai cặp này nối được, chấp nhận.
- ⚠ --clarity: câu hỏi b01 tới trước tình huống. Gộp vào M1.
- --fresh 0.18/0.17 ✔ (L-095). --repeat ✔. Câu dài nhất ≤25 chữ ✔. 173 chữ ✔.
- K4 đã xong: fact-package-v5 dòng 12 ghi F5 = Cẩm nang 23.14; Yang 2021; Dunlosky 2013, khớp end card.

## Lỗi (chỉ nêu lỗi + dòng, không viết câu thay, L-093b)
- **M1. Hook S1 (K1 chưa sửa; luật hook, L-095, L-090, L-091).** S1 vẫn mở bằng chuyện «Trên mạng đang bàn học thuộc lòng có còn đáng không». Nỗi đau «chỉ nói được «hay lắm»» nằm cuối câu, sau khoảng 17 chữ, quá 3 giây đầu. Chữ nối «mà sao» vẫn là kiểu khâu hai chuyện đã bị bắt 4 lần (R1, G1, H1, J1). Trend này chưa có trong research/trends (✖ L-090). Deep Research từng báo học thuộc lòng không khớp F5, và chưa có xác nhận mới trong repo. Cần: Social Research lưu trend vào research/trends (hoặc chọn trend khác đã lưu), Deep Research xác nhận trend khớp F5, và OpenCreator đưa nỗi đau lên 3 giây đầu.
- **M2. Phạm vi S1 với S3/S9 (K2 chưa sửa; L-094).** S1 «đọc hết cuốn», S3 «đọc một chương», S9 «đọc hết một chương». Chuyển từ cả cuốn sang một chương mà không có câu dẫn. Hình b01 «ôm cuốn sách dày vừa đọc hết» cũng theo «hết cuốn».
- **M3. Chữ trong hình (K3 mới sửa một phần; L-050).** b01, b03 đã đạt. Còn: b02 «lật lại «×2»» và «“hay lắm” nhỏ dần» (chữ hiện trong cảnh); b05 «tờ ghi chú «lần sau»»; b06 «dấu «+1» bật». Chữ chỉ đi theo lời và phụ đề.
- **M4. Trạng thái fact.** Front matter status ghi «chờ Deep Research soát fact», chưa có file/commit xác nhận của Deep Research cho r9.1.

## Phân vai
- OpenCreator: M1 (phần lời), M2, M3. Vòng vá 2 của r9, vòng sau mà còn lỗi thì viết lại cả bài.
- Social Research: M1 (lưu/chọn trend trong research/trends).
- Deep Research: M1 (trend có khớp F5 không), M4.

Chưa Chốt. Không làm giọng, không render.
