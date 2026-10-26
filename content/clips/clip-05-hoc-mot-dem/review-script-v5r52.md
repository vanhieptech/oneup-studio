---
title: "clip-05 v5 r5.2 — Rule Reviewer chấm (cổng đọc to L-089 trước, chấm chặt)"
date: 2026-10-27
clip: clip-05-hoc-mot-dem
draft: content/clips/clip-05-hoc-mot-dem/script-v5-draft-opencreator.md @ 732f2a1
previous_review: review-script-v5r5.md @ 659e705
fact_lock: fact-package-v5.md @ 5861e88
trend: final/trend-signals.md @ cf8f291
reviewer: Rule Reviewer (người chấm ≠ người viết; không tự viết lại script)
verdict: CHƯA ĐẠT
---

# Verdict: CHƯA ĐẠT (3 lỗi chặn nhỏ ở cổng đọc to; mọi luật khác đạt)

Theo yêu cầu sau khi Hiệp bác r4: đọc to mà vấp chỗ nào, chữ trỏ không rõ, cụm nói gượng thì đều chặn.
**Lỗi B1 do chính gợi ý N1 ở review r5 của Rule Reviewer («thử chia ra ba ngày»)** làm quay lại đúng lỗi B6 của r3. Gợi ý đó đã không qua cổng đọc to (L-089 (e)). Ghi nhận đây là lỗi của Rule Reviewer.

## 1. Cổng đọc to liền mạch (L-089)
Đọc to b01→CTA như người xem (văn bản liền ở dòng 28 khớp 6 beat):

> Hôm họp, bạn trình bày trơn tru. Vậy mà hai hôm sau, sếp hỏi lại một ý, bạn đứng hình. Sao ý đó trôi nhanh thế? Có thể vì tối trước buổi họp, bạn dồn ba tiếng đọc chồng tài liệu hai lần liền. Một nghiên cứu về cách đọc cũng thấy vậy. Đọc liền hai lần thì ngay sau đó nhớ hơn người đọc một lần, nhưng hai ngày sau không còn hơn. Còn nếu đọc lần hai cách một tuần, hai ngày sau vẫn hơn. Vậy muốn nhớ tới lúc bị hỏi lại, bạn có thể chia ba tiếng ra ba ngày, như cẩm nang gợi ý. Mỗi tối, bạn thử úp tài liệu, tự nói lại ý chính, rồi lật lên xem sót chỗ nào. Rồi lúc sếp hỏi lại, bạn dễ nhớ ra ý đó hơn, mà mỗi tối chỉ tốn chừng một tiếng. Sắp tới bạn có buổi thuyết trình nào muốn thử chia ra ba ngày không? Kể OneUp nghe dưới comment nha.

Nhận xét bằng lời thường:
- **Mạch tổng thể giờ liền.** Một ngôi «bạn» suốt bài. Chuỗi «Vậy mà → Có thể vì → cũng thấy vậy → Vậy muốn… → Rồi lúc sếp hỏi lại → mà mỗi tối chỉ tốn…» kéo một chuyện từ đầu tới cuối. Câu khẩu hiệu ở b05 đã bỏ. Nốt +1 giờ nằm trong câu kết quả, có chữ nối «mà».
- **Chỗ vấp 1 (CTA, B1):** «buổi thuyết trình nào muốn thử **chia ra ba ngày**». Nghe như chia *buổi thuyết trình* ra ba ngày, trong khi thứ cần chia là ba tiếng *ôn*. Chữ trỏ sai đối tượng.
- **Chỗ vấp 2 (b03, B2):** «**Đọc liền hai lần** thì ngay sau đó nhớ hơn **người đọc một lần**». Lấy một *việc* so với một *người*, nói lên nghe gượng.
- **Chỗ vấp 3 (b02, B3):** «dồn ba tiếng **đọc chồng tài liệu**». Nghe dễ hiểu thành «đọc chồng lên nhau». Lỗi này đã ghi ở r2/r4 nhưng chưa sửa.
- Không vấp: «cũng thấy vậy» trỏ đúng giả thuyết «đọc dồn hai lần liền» của b02. «Vậy muốn nhớ tới lúc bị hỏi lại» nối được nghiên cứu sang mục tiêu, và «ba ngày» được gán cho cẩm nang nên không lẫn với «một tuần» của nghiên cứu. «mà mỗi tối chỉ tốn chừng một tiếng» là vế nối, không thành câu dán thêm.

## 2. Đo tự động (Rule Reviewer tự chạy trên 732f2a1)
- `--flow` → 6 check · 0 ✖ · 0 ⚠ (ngôi kể nhất quán, không khâu lặp, beat nào cũng mở bằng mối nối, không liệt kê, không câu chốt gắn thêm). Lưu ý: `--flow` chỉ đo được cấu trúc. Nó không bắt được lỗi trỏ sai đối tượng (B1) hay chủ ngữ gượng (B2). Những lỗi đó chỉ bắt được khi đọc to.
- `--subjects` → PASS, 0 ⚠. `--l088` → 7 check · 0 ✖ · 0 ⚠.
- **169 chữ** (26/18/43/41/20/21), khớp với số OpenCreator ghi. Lời không có «317».
- CTA giống clip trước nhiều nhất 0.41. Hook không đổi so với r5.1 (giống nhiều nhất 0.41, vế đầu 2 chữ).
- Caption EN: 20 chunk, dài nhất 8 từ. b05 đã cập nhật («Just about an hour each evening»). Hai chunk cũ «One short session a day» / «A little better each day» đã bỏ. Không còn caption cũ, trừ b06 sẽ phải đổi theo B1.

## 3. Fact F1–F5
- b03 = F1 (giữ như r5.1, Deep Research đã duyệt). Mốc «người đọc một lần» ở vế đầu, không nói đọc hai lần là vô ích, «một tuần» là của nghiên cứu.
- b04 «chia ba tiếng ra ba ngày, như cẩm nang gợi ý» = F3. «úp tài liệu, tự nói lại, lật lên xem sót» = F5.
- **b05 «mỗi tối chỉ tốn chừng một tiếng»:** ba tiếng chia ba ngày ra một tiếng mỗi ngày, đúng ví dụ F3 của cẩm nang («3 ngày × 1 tiếng»). «chừng» chỉ làm mềm, không thêm số mới. Đạt.
- F2 ở hook: «trôi» là cảm giác của người xem, không gắn vào nghiên cứu. F4 chỉ còn ở hình b04 + end card.
- Không dùng gì trong danh sách Cấm. Không hứa kết quả («dễ nhớ ra ý đó hơn»).

## 4. Nốt +1 (L-088 (c))
Câu khẩu hiệu đã bỏ. Thông điệp +1 giờ là: **một việc nhỏ mỗi tối (chừng một tiếng) đổi được chỗ đứng hình**, nói ở b05, rồi CTA mời làm việc nhỏ đó cho buổi sắp tới. Hình b05 có dấu «+1» trên mỗi chồng đã úp. Vẫn ra đúng trục «sống tốt hơn mỗi ngày +1», chỉ là nói trong mạch chuyện chứ không thành khẩu hiệu → **đạt**. Rủi ro: nếu hình b05 không thấy rõ «+1» thì nốt +1 trong lời khá kín. FLUX soát still.

## 5. Bảng luật
| ID | Luật | Dòng | Kết quả |
|---|---|---|---|
| **L-089** | Cổng đọc to | 22, 23, 26 | **CHƯA ĐẠT**: B1, B2, B3 |
| P-05/P-06/L-057/L-058, rule-55 | Nỗi đau nói với «bạn» + câu hỏi «sao», vế đầu ≤6 chữ | 21 | ĐẠT |
| W-16 | hook → nguyên nhân + dẫn chứng → mục tiêu → cách làm → kết quả → CTA | 21–26 | ĐẠT |
| L-088 | Nguồn / trend / fact / dẫn chứng lồng vào chuyện / hook-CTA mới / +1 | 21–26 | ĐẠT |
| P-03 | F1–F5, không bịa, không hứa | 21–25 | ĐẠT |
| L-087 | Ví dụ đời thường | toàn bộ | ĐẠT |
| W-09 | Câu đủ chủ ngữ | 23 | ĐẠT về hình thức (B2 là chỗ gượng) |
| W-10 | Câu với người xem mềm | 24, 26 | ĐẠT |
| W-14 | 169 chữ, một CTA | 21–26 | ĐẠT |
| P-01 | Mỗi ý một lần | 21–26 | ĐẠT («hỏi lại» b01/b04/b05 là móc vòng) |
| P-04 | Không mơ hồ / gượng | 22, 23, 26 | **CHƯA ĐẠT** (B1–B3) |
| P-07 / P-02 | Không chê người học | toàn bộ | ĐẠT |
| W-12 | Nghiên cứu ≤ ~25 chữ | 23 | CHẤP NHẬN CÓ ĐIỀU KIỆN (43 chữ vì F1) |
| rule-56 | Có challenge + loop | 26 | ĐẠT |
| P-09 | Caption ≤8 từ, khớp lời | 38–43 | ĐẠT (b06 đổi theo B1; N1) |
| P-10 | Dòng an toàn + credit | 32 | ĐẠT (N3) |
| L-084 | Trend ở b01 + trend-signals | 38, cf8f291 | ĐẠT |

## 6. Lỗi chặn
- **B1, dòng 26 (CTA):** «Sắp tới bạn có buổi thuyết trình nào muốn thử chia ra ba ngày không?» → chia sai đối tượng.
  Sửa (không thêm chữ): «…muốn thử **ôn trong** ba ngày không?» (cách nói đã duyệt ở r4, «ôn» khớp với cách làm). Caption b06: «Presentation coming? Try prepping over three days» (7 từ).
- **B2, dòng 23 (b03, câu 2):** «Đọc liền hai lần thì ngay sau đó nhớ hơn người đọc một lần…» → việc so với người.
  Sửa: «**Người** đọc liền hai lần thì ngay sau đó nhớ hơn người đọc một lần, nhưng hai ngày sau không còn hơn.» (+1 chữ). Đây là câu fact nên nhờ Deep Research xác nhận lại. Nghĩa F1 không đổi.
- **B3, dòng 22 (b02):** «đọc chồng tài liệu» → «đọc **cả** chồng tài liệu» (+1 chữ).
- Sau khi sửa: 171 chữ (≤175). Chạy lại `--flow`, rồi đọc to lại cả bài.

## 7. Ghi chú không chặn
- **N1, caption b03 «Twice in a row: strong right after»:** lời nói là «nhớ hơn người đọc một lần», còn «strong» thì mạnh hơn lời. Gợi ý: «Twice in a row: ahead of one read» (7 từ).
- **N2, «Kể OneUp nghe»:** phải phiên âm «OneUp» trong `say` khi làm giọng (L-025).
- **N3, post.md:** bắt buộc có link https://creativecommons.org/licenses/by/4.0/ + chữ «đã chuyển thể» (rule-13/53).
- **N4, hình:**
  - Sếp chibi là nhân vật mới (luật 43).
  - b04 41 chữ ≈ 10s, phải tách cảnh khi làm spec.
  - Dải lịch Cepeda ở b04 không có lời đi kèm, nên hình phải tự nói được ý hoặc bỏ.
  - Dấu «+1» ở b05 phải đọc rõ.

## 8. Hiệp quyết
- **H2, dòng 21: «Sao ý đó trôi nhanh thế?» hay «…nhanh vậy?».** L-082 cho phép cả hai. Giọng miền Nam nghiêng về «vậy». Rule Reviewer khuyên «vậy». Không chặn.

## 9. Rủi ro còn lại
- `--flow` PASS không có nghĩa là liền mạch (B1/B2 lọt qua máy). Cổng đọc to vẫn là cổng quyết định.
- Luật chạy trên spec (rule-55/56/58/60/61/62/64) chưa chạy. rule-58 có thể báo «Có thể vì», «Một nghiên cứu…» không nằm trong danh sách từ nối (X-04/X-09: báo cả hai, không quay lại câu mẫu).
- Nốt +1 phụ thuộc hình b05.
- Chưa Chốt thì không làm giọng hay render (L-072).
