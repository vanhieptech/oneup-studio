---
title: "clip-05 v5 r5.3b — Rule Reviewer chấm (cổng đọc to L-089 trước, chấm chặt)"
date: 2026-10-27
clip: clip-05-hoc-mot-dem
draft: content/clips/clip-05-hoc-mot-dem/script-v5-draft-opencreator.md @ ac691a8 (r5.3b; r5.3 = f20a919)
previous_review: review-script-v5r52.md @ a956c8c
fact_lock: fact-package-v5.md @ 5861e88
trend: final/trend-signals.md @ cf8f291
reviewer: Rule Reviewer (người chấm ≠ người viết; không tự viết lại script)
verdict: ĐẠT (đưa Hiệp Chốt; còn H2)
---

# Verdict: ĐẠT ở tầng script. Không còn lỗi chặn. Hiệp quyết H2 rồi Chốt.

Phạm vi chấm: lúc chấm, OpenCreator đã commit thêm **ac691a8 (r5.3b)**, có câu song song của Deep Research. Rule Reviewer chấm bản mới nhất này. f20a919 (r5.3) vẫn còn «Còn nếu đọc lần hai…» và 171 chữ, nên nghi ngờ của bên giao việc đúng với f20a919. ac691a8 đã sửa chỗ đó, giờ là 172 chữ.

## 1. Cổng đọc to liền mạch (L-089), làm trước
> Hôm họp, bạn trình bày trơn tru. Vậy mà hai hôm sau, sếp hỏi lại một ý, bạn đứng hình. Sao ý đó trôi nhanh thế? Có thể vì tối trước buổi họp, bạn dồn ba tiếng đọc cả chồng tài liệu hai lần liền. Một nghiên cứu về cách đọc cũng thấy vậy. Người đọc liền hai lần thì ngay sau đó nhớ hơn người đọc một lần, nhưng hai ngày sau không còn hơn. Còn người đọc lần hai cách một tuần thì hai ngày sau vẫn hơn. Vậy muốn nhớ tới lúc bị hỏi lại, bạn có thể chia ba tiếng ra ba ngày, như cẩm nang gợi ý. Mỗi tối, bạn thử úp tài liệu, tự nói lại ý chính, rồi lật lên xem sót chỗ nào. Rồi lúc sếp hỏi lại, bạn dễ nhớ ra ý đó hơn, mà mỗi tối chỉ tốn chừng một tiếng. Sắp tới bạn có buổi thuyết trình nào muốn thử ôn trong ba ngày không? Kể OneUp nghe dưới comment nha.

Bằng lời thường:
- Bài là **một chuyện liền**: trình bày trơn → bị hỏi lại thì đứng hình → có thể vì đọc dồn → nghiên cứu cũng thấy vậy → nên chia ra ba ngày, mỗi tối tự nói lại → lần sau sếp hỏi thì nhớ ra, mỗi tối chỉ chừng một tiếng → hỏi người xem có buổi nào sắp tới muốn thử không.
- Cả bài một ngôi «bạn». Beat nào cũng có mối nối. Không có câu dán thêm.
- Ba chỗ vấp của r5.2 đã hết:
  - CTA «ôn trong ba ngày» là chia việc ôn, không phải chia buổi thuyết trình.
  - b03 giờ so người với người.
  - «đọc cả chồng tài liệu» không còn dễ nghe nhầm.
- **b03 câu song song**: «Người đọc liền hai lần thì… Còn người đọc lần hai cách một tuần thì…». Đây là kiểu «A thì…, còn B thì…» quen trong văn nói. Hai nhóm được đặt cạnh nhau rõ, và «vẫn hơn» trỏ được về mốc «người đọc một lần» đã nói ở câu trước.
  - Đọc to thì ngắt nhẹ sau «một tuần», đúng như News nhận xét, không vấp.
  - «người đọc» lặp 3 lần trong 2 câu, hơi dày, nhưng đổi lại người nghe hiểu rõ ai hơn ai. **Không chặn.**

## 2. Đo tự động (Rule Reviewer tự chạy trên ac691a8)
- `--subjects` → PASS, 0 ⚠. `--l088` → 7 check · 0 ✖ · 0 ⚠.
- `--flow` → 6 check · 0 ✖ · **1 ⚠**: «câu cùng mở bằng một cụm, đọc như danh sách: b03 («người đọc…»)».
  - Câu OpenCreator ghi «--flow PASS» chỉ đúng nghĩa không có ✖. Cảnh báo này có thật và do chính câu song song gây ra.
  - Khi đọc to, Rule Reviewer xếp nó là **so sánh hai vế có «Còn», không phải liệt kê** (máy dò này viết để bắt kiểu liệt kê nhóm «Người A… Người B… Người C…»). Chấp nhận cảnh báo, ghi lại đây.
- **172 chữ** (26/19/45/41/20/21), dưới trần 175. Một CTA. Lời không có «317».
- Luật chạy trên spec (rule-55/56/58/60/61/62/64): **chưa chạy được cho v5**. `final/spec.json` hiện có là spec của v4 (e9a1a5b), bản bị bỏ vì vi phạm L-087. Chạy trên file đó là chấm nhầm bản. Phải chạy khi OpenCreator làm spec v5 (xem mục 9).
- Hook/CTA: không đổi so với r5.2 về kiểu câu. CTA giống clip trước nhiều nhất ≤0.41, dưới ngưỡng 0.7.

## 3. Fact F1–F5
- b03 = F1 đủ cả ba vế:
  - đọc liền hai lần thì ngay sau đó hơn người đọc một lần;
  - hai ngày sau thì không còn hơn;
  - đọc lần hai cách một tuần thì hai ngày sau vẫn hơn người đọc một lần.
- Không nói đọc hai lần là vô ích. «một tuần» là của nghiên cứu. Deep Research đã xác nhận câu song song.
- b04: «chia ba tiếng ra ba ngày, như cẩm nang gợi ý» = F3. «úp, tự nói lại, lật lên xem sót» = F5.
- b05: «mỗi tối chỉ tốn chừng một tiếng» = 3 tiếng / 3 ngày (F3). «dễ nhớ ra hơn» không phải lời hứa.
- F2 chỉ là cảm giác ở hook. F4 chỉ ở hình và end card. Không dùng gì trong danh sách Cấm.

## 4. Caption EN
20 chunk, dài nhất 8 từ, khớp lời.
- b03 «Twice in a row: ahead of one read» khớp «nhớ hơn người đọc một lần».
- b06 «Presentation coming? Try prepping over three days» khớp «ôn trong ba ngày».
- b05 không còn caption cũ.
- Câu b03 mới không cần đổi caption, vì «A week apart: still ahead after two days» vẫn khớp.

## 5. Bảng luật
| ID | Luật | Dòng | Kết quả |
|---|---|---|---|
| L-089 | Cổng đọc to | 21–26 | ĐẠT (⚠ b03 «người đọc» đã xét, chấp nhận) |
| P-05/P-06/L-057/L-058, rule-55 | Nỗi đau với «bạn» + câu hỏi «sao» | 21 | ĐẠT |
| W-16 | hook → nguyên nhân + dẫn chứng → mục tiêu → cách làm → kết quả → CTA | 21–26 | ĐẠT |
| L-088 | Nguồn / trend / fact / dẫn chứng lồng vào chuyện / hook-CTA mới / +1 (một việc nhỏ mỗi tối) | 21–26 | ĐẠT |
| P-03 | F1–F5, không bịa, không hứa | 21–25 | ĐẠT |
| L-087 | Ví dụ đời thường | toàn bộ | ĐẠT |
| W-09 | Vế nào cũng có chủ ngữ | 21–26 | ĐẠT (b03 giờ có «Người đọc…») |
| W-10 | Câu với người xem mềm | 24, 26 | ĐẠT |
| W-14 | 140–175 chữ (172), một CTA | 21–26 | ĐẠT |
| P-01 | Mỗi ý một lần | 21–26 | ĐẠT |
| P-04 | Không mơ hồ / gượng | 21–26 | ĐẠT |
| P-07 / P-02 | Không chê người học | toàn bộ | ĐẠT |
| W-12 | Nghiên cứu ≤ ~25 chữ | 23 | CHẤP NHẬN CÓ ĐIỀU KIỆN (45 chữ vì F1 có ba vế) |
| rule-56 | Có challenge + loop | 26 | ĐẠT |
| P-09 | Caption ≤8 từ, khớp lời | 38–43 | ĐẠT |
| P-10 | Dòng an toàn + credit | 32 | ĐẠT (N3) |
| L-084 | Trend ở b01 + trend-signals | 38, cf8f291 | ĐẠT |
| spec rules | 55/56/58/60/61/62/64 | — | CHƯA CHẠY (chưa có spec v5) |

## 6. Lỗi chặn
Không có.

## 7. Ghi chú không chặn
- **N1, giấy tờ cũ trong draft:**
  - heading vẫn ghi «# clip-05 v5 r5»;
  - `status:` vẫn ghi «DRAFT r5 — chờ…»;
  - mục «Thay đổi r5.3» ghi «171 chữ» trong khi đúng là 172;
  - «Tự soát» còn ghi chủ ngữ «đọc liền hai lần».
  Sửa khi Chốt.
- **N2:** phải phiên âm «OneUp» trong `say` (L-025).
- **N3, post.md:** bắt buộc có link https://creativecommons.org/licenses/by/4.0/ và chữ «đã chuyển thể». `final/post.md` hiện là bản v4, phải viết lại cho v5.
- **N4, hình:**
  - Sếp chibi là nhân vật mới (luật 43).
  - b03 45 chữ và b04 41 chữ đều ≈10s, phải tách cảnh.
  - Dải lịch Cepeda ở b04 không có lời đi kèm, nên hình phải tự nói được ý.
  - Dấu «+1» ở b05 phải đọc rõ, vì nốt +1 trong lời nằm kín trong «mỗi tối chỉ tốn chừng một tiếng».
- **N5, giọng b03:** ngắt nhẹ sau «một tuần». Không được ngắt sau «Còn người đọc», nếu không «lần hai» sẽ nghe tách khỏi «đọc».

## 8. Hiệp quyết
- **H2, dòng 21: «Sao ý đó trôi nhanh thế?» hay «…nhanh vậy?».** L-082 cho phép cả hai. Giọng miền Nam nghiêng về «vậy». Rule Reviewer khuyên «vậy». Không chặn, số chữ không đổi.

## 9. Rủi ro còn lại
- Luật chạy trên spec chưa chạy. Khi có spec v5, rule-58 có thể báo các mở beat «Có thể vì», «Một nghiên cứu…» (X-04/X-09: báo cả hai, không quay lại câu mẫu).
- `final/` còn toàn đồ v4 (spec, post, voice, timing). Phải dựng lại, không dùng lại.
- Nốt +1 phụ thuộc hình b05.
- Chưa Chốt thì không làm giọng hay render (L-072).
