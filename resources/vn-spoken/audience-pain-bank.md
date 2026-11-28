---
title: "Kho Nỗi Đau & Câu Hỏi Khán Giả Thật (Audience Pain Bank từ comment)"
date: 2026-11-26
id: resources.vn-spoken.audience-pain-bank
type: resource
status: ready
updated: 2026-11-26
tags: [audience, pain-bank, comments, vn-spoken, teardown, gate-0]
source: "Tự động gom từ comment thật qua pipeline/scripts/teardown.py (Khối 7) và radar-fetch.py (audience-language.md); hạt giống ban đầu từ Apify comments 16/10 & 26/11"
---
# Kho Nỗi Đau & Câu Hỏi Khán Giả Thật (Audience Pain Bank)

Nơi tích lũy các câu hỏi, nỗi đau và cách diễn đạt cửa miệng của khán giả thật (ẩn danh, không lưu tên tài khoản cá nhân) lấy từ comment video outlier và teardown. Dùng làm hạt giống cho **Gate 0** và **Gate 0.5 Hook Arena (Pain-Mirror)** để đảm bảo ví dụ và hook chạm đúng nỗi đau có thật (`L-090`).

## Bảng nỗi đau & câu hỏi từ comment

| ngày | nguồn teardown / video | chủ đề | câu hỏi / nỗi đau khán giả (ẩn danh) | ghi chú dùng cho hook |
|---|---|---|---|---|
| 2026-10-16 | clip-03 (Apify comments) | trì hoãn, dọn phòng | «phòng chất đầy đồ, tuần nào cũng hứa cuối tuần dọn mà để cả năm» | Pain-Mirror cho chia nhỏ việc (`clip-03`) |
| 2026-10-16 | clip-03 (Apify comments) | trì hoãn, học tập | «Muốn học mà mắc lười» | Nỗi đau thật: muốn làm nhưng không bắt đầu nổi |
| 2026-11-26 | manghocls-7366613156908600583 | học thuộc, nhớ lâu | «chiều thi mà giờ học chưa xong, làm sao để nhớ lâu» | Đổi bối cảnh sang đời thường nếu dùng cho `@hi.oneup` (`L-087`) |
| 2026-11-26 | thayqueo (Apify vtt/comments) | trì hoãn | «đợi khi nào thật sự sẵn sàng rồi làm, từ từ đã» | Niềm tin phổ biến để bẻ gãy ở Counter-Intuitive Hook |
| 2026-11-27 | trends-2026-11-27-01 | hoc-tap, productivity | «Nỗi sợ U30 đã quá muộn để học lại, thi lại hoặc đổi hướng cuộc đời» | Tự động trích từ Khối 7 / comment |
| 2026-11-27 | trends-2026-11-27-01 | hoc-tap, productivity | «Tâm lý ngại ánh nhìn và sự chênh lệch tuổi tác khi học chung với người nhỏ hơn hoặc thầy cô trẻ hơn» | Tự động trích từ Khối 7 / comment |
| 2026-11-27 | trends-2026-11-27-01 | hoc-tap, productivity | «Áp lực cân bằng giữa chi phí, quãng đường, thời gian cày cuốc và mục tiêu điểm số cao» | Tự động trích từ Khối 7 / comment |
| 2026-11-27 | trends-2026-11-27-14 | Tự giễu nỗi đau học tập nhưng lật kèo khoe thành quả thực chiến | «Học hàng trăm từ vựng mỗi tuần nhưng gặp lại trong đề vẫn chỉ thấy 'quen quen' mà không bật ra được nghĩa chính xác.» | Tự động trích từ Khối 7 / comment |
| 2026-11-27 | trends-2026-11-27-14 | Tự giễu nỗi đau học tập nhưng lật kèo khoe thành quả thực chiến | «Áp lực khối lượng đề ôn thi dày đặc và nỗi sợ học nhiều nhưng đi thi vẫn quên.» | Tự động trích từ Khối 7 / comment |
| 2026-11-27 | trends-2026-11-27-14 | Tự giễu nỗi đau học tập nhưng lật kèo khoe thành quả thực chiến | «Tâm lý vừa muốn đồng cảm với bạn đồng trang lứa vừa bị kích thích bởi thành tích điểm cao (39/40, 40/40) của người khác.» | Tự động trích từ Khối 7 / comment |
| 2026-11-28 | trends-2026-11-28-04 | hoc-tap, productivity | «Biết rõ việc cần làm rất quan trọng nhưng vẫn vô thức trốn sang giải trí (chơi game, lướt mạng).» | Tự động trích từ Khối 7 / comment |
| 2026-11-28 | trends-2026-11-28-04 | hoc-tap, productivity | «Nhìn một đầu việc quá rộng nên thấy ngợp, không biết bước nhỏ đầu tiên phải làm gì.» | Tự động trích từ Khối 7 / comment |
| 2026-11-28 | trends-2026-11-28-04 | hoc-tap, productivity | «Tự nhủ trong đầu sẽ tập trung nhưng bộ não nhanh chóng tìm cớ bỏ ngang.» | Tự động trích từ Khối 7 / comment |
| 2026-11-28 | trends-2026-11-28-01 | tu-duy, productivity | «Cảm giác những điều tưởng rất cơ bản như tập luyện đều, có tiền tiết kiệm, hẹn hò hay có người chủ động nhắn tin ngoài đời thật đang ngày càng khó chạm tới.» | Tự động trích từ Khối 7 / comment |
| 2026-11-28 | trends-2026-11-28-01 | tu-duy, productivity | «Thói quen chăm chỉ làm những việc lành mạnh trong thế giới ảo (nơi có hướng dẫn và phản hồi rõ ràng) nhưng lại trì hoãn đúng những việc đó ngoài đời thật.» | Tự động trích từ Khối 7 / comment |
| 2026-11-28 | trends-2026-11-28-01 | tu-duy, productivity | «Sự hụt hẫng khi giải trí không còn mang lại cảm giác tự do mà lại gợi nhớ áp lực việc nhà hằng ngày.» | Tự động trích từ Khối 7 / comment |
