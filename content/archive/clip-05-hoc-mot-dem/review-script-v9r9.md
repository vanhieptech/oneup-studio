# Review clip-05 v9 r9 (77fe141), Rule Reviewer, 30/10/2026

**Kết luận: CHƯA ĐẠT.** Kết quả check tự động: 8 nhóm PASS. `--fresh` ra 0.24/0.17 (✔ L-095). Có 3 cảnh báo, đã đối chiếu với bảng cặp câu: S1→S2 trả lời câu hỏi «sao», S2→S3 mở ví dụ bằng «Như». Hai cặp này nối được.

Cổng L-095: ý tưởng này khác hẳn r8.2. Khoảnh khắc bong bóng «hay lắm» trống rồi đầy là điểm đáng nhớ, đạt.

## Lỗi
- **K1. Hook S1, 3 giây đầu (luật hook, L-095, L-092).** Câu mở là cuộc bàn «đọc nhiều có giúp viết hay hơn không», chưa phải nỗi đau của người xem. Người xem chỉ nghe tới «hay lắm» ở khoảng giây thứ 5–6. Chữ «mà» nối chuyện viết hay sang chuyện không kể lại được, và đây vẫn là chỗ nối đã bị bắt lỗi 4 lần (R1, G1, H1, J1). Trend cũng khác với hướng đã thống nhất trong phòng lúc 18:03 (trend học thuộc). Deep Research lại báo trend học thuộc không khớp với F5. Vì vậy Social Research và OpenCreator cần chọn một trend nối thẳng vào chuyện đọc xong không kể lại được. Nếu không có trend nào như vậy, theo luật L-090, hook và format phải bám đúng mẫu trend đã nghiên cứu. Cái chốt lại phải là: nỗi đau «hay lắm» nằm trong 3 giây đầu.
- **K2. Phạm vi đổi giữa S1 và S3 (L-094).** S1 nói «đọc hết cuốn», nhưng S3 và S9 lại nói «một chương». Chuyển từ cả cuốn sang một chương mà không có câu dẫn.
- **K3. Hình b01, b02, b03 (L-050).** Chữ «hay lắm» nằm trong bong bóng ý, và b03 có các nhãn chữ «đọc lại», «tự kể → dò», «Cẩm nang 23.14». Theo lưu ý của FLUX, bong bóng phải trống, chỉ có «…» hoặc ngôi sao, còn chữ chỉ đi theo lời đọc và phụ đề. Nhãn nguồn thì để ở end card.
- **K4. Nguồn trên end card.** Nguồn ghi «Yang et al. 2021 · Dunlosky et al. 2013». Cần Deep Research xác nhận cả hai nằm trong F5 / fact-package-v5 trước.

## Phân vai
- OpenCreator sửa K1, K2, K3. Đây là vòng vá thứ 1 của r9.
- Social Research chốt trend cho K1.
- Deep Research xử lý K4 và soát fact.

Chưa Chốt. Không làm giọng, không render.
