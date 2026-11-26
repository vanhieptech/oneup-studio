---
title: "Teardown selftest-clip02"
date: 2026-11-26
id: teardown.selftest-clip02
type: teardown
status: draft
updated: 2026-11-26
tags: [teardown, trend]
source: "clip-02-final-720.mp4 · Gemini CLI agy 1.5.18 · model gemini-4-hydrogen-high"
---
# Teardown `selftest-clip02` (tự kiểm trên clip của kênh)

Chạy 26/11/2026 bằng `agy` (Antigravity) model `gemini-4-hydrogen-high` trên `media/clips/clip-02-procrastination-discomfort/clip-02-final-720.mp4`, không gộp vào blueprints. Độ chính xác mốc cắt so với `timing.json` thật: 15 mốc, lệch trung bình 0,47 s, tối đa 1,43 s, 13/15 lệch ≤ 1 s. Lời hook chép đúng nguyên văn spec.

Theo `templates/clip-teardown.md`. Mục 2, 3, 5, 6, 7 do Gemini điền (quan sát/suy đoán ghi trong JSON); mục 0, 1, 4, 8 từ Apify; 9–11 Claude tổng hợp.

## 2. Hook 0–3 giây
- Lời: Thì cái bản chất của cái việc mở laptop rồi lướt TikTok là gì? (nguyên văn: True)
- Chữ trên màn hình: BẢN CHẤT LÀ GÌ? | Thì cái bản chất... của cái việc mở laptop rồi lướt TikTok... là gì? | // TODO OneUp | So what's the essence... of opening your laptop, then scrolling TikTok?
- Hình / hành động: 00:00 nhân vật hoạt hình đứng mở đầu, 00:01 chuyển sang cảnh nằm giường ban đêm với mặt trăng, laptop mở sẵn và điện thoại hiện biểu tượng TikTok bật lên.
- Cơ chế: tò mò — Mở bằng câu hỏi đi tìm bản chất ('Bản chất là gì?') đánh vào sự tò mò (quan sát, 00:00–00:03), đồng thời gắn với tình huống quen thuộc dễ gây đồng cảm (suy đoán).
- Lời hứa ngầm: Sẽ giải mã nguyên nhân thật sự đằng sau việc định làm việc nhưng lại chuyển sang lướt điện thoại.

## 3. Xương sống
| mốc | vai trò | tóm ý | chuyển ý |
|---|---|---|---|
| 00:00–00:03 | câu hỏi | Đặt câu hỏi mở về bản chất của hành vi mở laptop định làm nhưng lại lướt TikTok. | Nhân vật thứ hai chen lời biện minh 'coi clip xíu thôi' ở 00:04. |
| 00:04–00:24 | dẫn dắt | Mô tả 3 bước của vòng lặp trì hoãn (lướt lặp trên giường, thấy khó chịu là đổi việc, tự chửi bản thân lười rồi dời sang mai). | Xóa bối cảnh ở 00:25, nhân vật giật mình rồi đặt câu hỏi 'Nghe quen hông?' ở 00:26. |
| 00:25–00:36 | chứng minh | Dẫn nghiên cứu tổng hợp 691 kết quả của Steel (2007) chỉ ra trì hoãn liên quan 3 yếu tố: độ khó chịu, cảm giác làm được không, và độ cuốn của thứ trước mắt. | Chuyển cảnh sang bàn làm việc có dải băng phân tách khái niệm ở 00:37. |
| 00:37–00:44 | lật kèo | Bác bỏ cách hiểu tự trách 'lười/chưa đủ cố gắng', khẳng định trì hoãn là né cảm giác khó chịu và cho nhân vật thứ hai xác nhận. | Chuyển sang cảnh gõ laptop và thanh công thức hành động ở 00:45. |
| 00:45–00:57 | áp dụng | Đưa cách xử lý thực tế: hỏi khó chịu chỗ nào, chia nhỏ việc còn 1 dòng, gắn khung giờ 21:00 ngồi vào bàn gõ 1 dòng và tự đặt ngày xong. | Cắt về khung hình tối giản chính giữa màn hình ở 00:58. |
| 00:58–01:02 | kết | Chốt lại 'Không lười, chỉ đang né' và mời người xem bình luận một chữ về điểm khiến họ thấy khó chịu. |  |
- Trả lời lời hứa ở: 00:37

## 5. Nhịp & ngắt nhịp
- Trung bình mỗi lần đổi: None giây
- 00:01 Chuyển từ nền trắng tối giản sang bối cảnh giường ngủ ban đêm kèm laptop và điện thoại bật lên (quan sát)
- 00:04 Đổi sang giọng nhân vật thứ hai cầm điện thoại kèm pill đỏ 'XÍU THÔI?' ở 00:05 (quan sát)
- 00:12 Đổi bối cảnh sang bàn làm việc, hiện dấu '?' trên đầu nhân vật và nhãn 'THỨ HAI · ĐỔI VIỆC' ở 00:17 (quan sát)
- 00:19 Xuất hiện mây mưa xám, pill đỏ 'LƯỜI!' (00:20) và tờ lịch deadline lật từ 'HÔM NAY' sang 'MAI / HOÃN x1' (00:22) (quan sát)
- 00:25 Xóa sạch bối cảnh về nền trắng, nhân vật giật mình mở mắt to rồi dựng sơ đồ nghiên cứu từ 00:26 đến 00:35 (quan sát)
- 00:37 Chuyển sang cảnh nhân vật nhỏ giọt nước mắt bên dải băng phân cách 'TRÁNH KHÓ CHỊU ≠ CHƯA CỐ GẮNG' (quan sát)
- 00:43 Ngắt nhịp bằng giọng nhân vật thứ hai thừa nhận 'À... mình đang né thiệt' (quan sát)
- 00:45 Đổi sang biểu cảm cười gõ laptop kèm thanh công thức hành động 'KHÓ CHỊU CHỖ NÀO? → CHIA NHỎ / 1 DÒNG' (quan sát)
- 00:58 Thu gọn về nhân vật đứng giữa nền sáng kèm pill đỏ 'COMMENT 1 CHỮ' ở 00:59 (quan sát)

## 6. Âm thanh & năng lượng
- Nhịp nói: Nhịp nói vừa phải, rõ chữ, ngắt ngắn giữa các vế; giọng nhân vật thứ hai có nhịp nhanh và cao hơn để tạo đối đáp. · tone: chia sẻ kinh nghiệm · nhạc: Không nghe rõ nhạc nền; âm thanh chủ yếu là giọng đọc sạch và hiệu ứng chuyển cảnh.
- nhấn 00:00: Nhấn nhẹ vào cụm 'bản chất'
- nhấn 00:04: Đổi sang giọng thứ hai nhấn vào 'xíu thôi'
- nhấn 00:19: Nhấn mạnh 'chửi bản thân mình cho đã' rồi hạ nhịp ở 'rồi mai lại né'
- nhấn 00:26: Lên giọng hỏi 'Nghe quen hông?'
- nhấn 00:37: Nhấn rõ 'tránh cảm giác khó chịu' khi chốt bản chất
- nhấn 00:58: Nhấn gọn vào chữ 'né' trong câu chốt
- SFX 00:00: Tiếng pop/whoosh mở đầu
- SFX 00:04: Tiếng pop khi điện thoại và thoại thứ hai xuất hiện
- SFX 00:12: Tiếng whoosh chuyển cảnh sang bàn làm việc
- SFX 00:19: Tiếng chuyển cảnh sang khung mây mưa và lịch deadline
- SFX 00:25: Tiếng pop/whoosh ngắt cảnh trước khi dựng sơ đồ
- SFX 00:37: Tiếng chuyển cảnh sang phần lật định nghĩa
- SFX 00:45: Tiếng chuyển cảnh sang phần giải pháp
- SFX 00:58: Tiếng chuyển cảnh về màn hình kết

## 7. Kết & CTA
- Kiểu: kêu gọi hành động · CTA: Việc bạn né khó chịu chỗ nào? Comment một chữ nha!

## 9. Vì sao nó chạy (Gemini, suy đoán)
- Tạo sự đồng cảm nhanh bằng cách gọi tên chính xác chuỗi hành vi tự mâu thuẫn trước khi đưa lý thuyết. (00:00–00:24)
- Xen kẽ giọng nhân vật thứ hai đóng vai tiếng nói nội tâm giúp cắt đơn điệu và giữ nhịp đối thoại. (00:04, 00:23, 00:43)
- Đẩy cảm giác tự trách lên cao ở 00:19–00:24 rồi giải oan ở 00:37 tạo cú giải tỏa tâm lý khiến người xem muốn nghe tiếp cách xử lý. (00:19–00:41)
- Neo lập luận vào con số cụ thể (691 kết quả) và hiện từng thẻ sơ đồ theo nhịp nói giúp tăng độ tin cậy và giữ mắt chờ đủ 3 yếu tố. (00:26–00:36)
- Thu nhỏ giải pháp xuống mức tối thiểu và thiết kế CTA chỉ yêu cầu bình luận một chữ giúp giảm rào cản tương tác ở cuối video. (00:45–01:02)

## 11. Công thức khung
1. Mở bằng câu hỏi bản chất gắn với một hành vi nghịch lý quen thuộc.
2. Liệt kê 2–3 bước mô tả vòng lặp sai lầm để tạo đồng cảm và đẩy căng thẳng lên đỉnh.
3. Ngắt cảnh đột ngột và đưa dẫn chứng hoặc mô hình ngắn có số lượng ý rõ ràng.
4. Lật lại ngộ nhận phổ biến để giải tỏa tâm lý và trả lời câu hỏi ở phần mở.
5. Đề xuất một hành động siêu nhỏ gắn với bối cảnh cụ thể để làm ngay.
6. Chốt bằng một câu đúc kết ngắn và kêu gọi tương tác tốn ít công sức nhất.

## Kiểm độ chính xác mốc cắt (so với timing.json)
- {'n': 15, 'mean_s': 0.47, 'max_s': 1.43, 'within_1s': 13}
