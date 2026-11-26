---
title: "clip-06 v4 — §4b kiểm claim + chấm rubric"
date: 2026-11-26
type: review
tags: [review, clip-06, gate-1, howtolivebetter-4.12]
status: draft
source: "archive/script-v4-draft.md (e0cde74) · HTB book/04 mục 12 (đọc trực tiếp) · Lally et al. 2010 abstract (Wiley, mở được 26/11) · Gardner, Lally & Wardle 2012 BJGP (PMC3505409) · logs/rule-scoring-rubric.md §3"
verdict: "ĐẠT VỀ ĐIỂM — chờ Hiệp quyết X-A (hook rubric gốc vs L-103–105) và xác nhận chuyện đi bộ (86 theo L-103–105; 75 theo neo A gốc)"
score: 86
script_hash: 529042a178c8
feedback_seen: 4
---
# clip-06 v4 — §4b kiểm claim + chấm điểm

**Lượt 2 (r1, 26/11, sau Hiệp «Sửa và chấm lại»):** đã sửa 3 dòng theo mục 5 của lượt 1 (b04, b05, b06). Lượt 1 được 77, CHƯA ĐẠT, commit 877bf9c. Hash nháp mới là `f074d4b82697`. check-rules --draft PASS, 0 lỗi, 4 cảnh báo heuristic (khung liệt kê và cụm lặp cố ý, xem B).

**Bản được chấm:** `archive/script-v4-draft.md` (commit e0cde74), 9 beat. Bản này **không phải r3**: Hiệp đã nói «làm lại» sau r3 (0a438dc), nên r3 bị thay. Hash nháp tính trên 9 dòng lời VI (lượt 1: `368bcf1cbf64`, lượt 2: `f074d4b82697`). Chưa có spec nên chưa có caption EN theo dòng.

**Ngưỡng và trọng số** vẫn là đề xuất của rubric §6 (câu 1, 2, 3, 5 chưa được Hiệp duyệt). Bản review này dùng tạm theo §4b.

## 1. Bảng claim

| Claim (như được phép nói) | Nguồn gốc (tác giả/năm + đoạn khớp) | Nguồn độc lập thứ 2 | Độ tin | Cách nói được phép | Cách nói cấm |
|---|---|---|---|---|---|
| b03: năm 2010, nhóm Lally theo dõi 96 người, 12 tuần, mỗi người một việc ăn/uống/vận động, làm mỗi ngày cùng một bối cảnh (ví dụ sau bữa sáng), tự chấm mỗi ngày | Lally 2010 abstract: «96 volunteers chose an eating, drinking or activity behaviour to carry out daily in the same context (for example ‘after breakfast’) for 12 weeks… completed the SRHI each day» · HTB 4.12 Lợi ích | Gardner, Lally & Wardle 2012 (cùng nhóm tác giả, **không độc lập hẳn**) | vừa | như v4 | «nghiên cứu lớn», «hàng trăm người» |
| b04: lỡ một lượt gần như không ảnh hưởng tới quá trình thành thói quen | Lally 2010: «Missing one opportunity to perform the behaviour did not materially affect the habit formation process» · HTB «không ảnh hưởng thực chất» | Gardner 2012: «did not seriously impair… gains soon resumed after one missed performance» | vừa | «lỡ một lượt gần như không ảnh hưởng» | «lỡ bao nhiêu cũng được», «không sao hết» (nguồn nói **một** lượt) |
| b04: «hôm mình về trễ, mình chưa mất gì hết» | suy luận của người nói từ dòng trên | — | suy luận | **đã sửa (r1):** «gần như chưa mất gì» | «chưa mất gì hết» (mạnh hơn «not materially») |
| b05: mỗi người mất 18 tới 254 ngày để quen gần tới mức cao nhất của chính họ | Lally 2010: «time it took participants to reach 95% of their asymptote of automaticity ranged from 18 to 254 days» · HTB «tính ra… 18 ngày, chậm phải 254 ngày» | Gardner 2012 chỉ nêu trung bình 66 ngày, không nêu dải | vừa | **đã sửa (r1):** «nhóm tính ra mỗi người cần bao lâu để quen gần hết mức của chính họ. Người nhanh nhất cần 18 ngày, còn người chậm nhất cần tới 254 ngày» | «người chậm nhất **mất** 254 ngày» như đã quan sát (nghiên cứu chỉ kéo dài 84 ngày, 254 là số mô hình ngoại suy, chỉ trên 62 người mô hình khớp); «trung bình», «66 ngày» (fact lock cấm) |
| b05: «30 ngày chỉ là con số tròn… không phải mốc ai tới cũng quen» | suy luận từ dải 18–254 | — | suy luận | giữ, đã là ý của người nói | «nghiên cứu chứng minh 30 ngày vô dụng» |
| b06: một nghiên cứu, việc đơn giản; việc khó như chạy ba buổi/tuần chưa ai đo | HTB 4.12 Ghi chú (nguyên văn) | Gardner 2012: việc phức tạp hơn (50 cái gập bụng) lên đỉnh chậm hơn | vừa | **đã sửa (r1):** «thì cuốn sách ghi là tới giờ chưa ai đo» (gán cho sách, vì «chưa ai đo» là khẳng định phủ định toàn cục) | — |
| b07: câu nếu… thì… (gọi lại clip-01) | HTB 4.1 (Gollwitzer & Sheeran 2006), không nêu số | — | gọi lại | như v4 | nêu hiệu ứng |

Không có dòng `chặn`. Ví dụ đời thường (đi bộ 15 phút, ngày thứ năm, «lỡ vài bữa») không mang số nghiên cứu (L-052 đạt).

## 2. Điểm (rubric §3)

| Mục | Điểm | Trừ (trích dòng) | Đo |
|---|---:|---|---|
| A Hook 20 | **15** theo L-103–105 · **4** theo neo gốc | (không đổi so với lượt 1) Theo L-103–105: có chuyện, cái giá (bỏ cả lộ trình) và bất ngờ («ý nghĩ làm mình bỏ là sai»), nhưng hook dài 5 câu, cú lật ở câu cuối (−3); P08 cần log thật mà chuyện đang dựng (−2). Theo neo gốc: không câu hỏi −8, kể ngôi «mình» −8, đồng thời dính lỗi chặn 4 → xem X-A | tay |
| B Mạch 15 | 13 | «Về điều thứ nhất… / Về điều thứ hai…», «Chỗ thứ nhất… / Chỗ thứ hai…» đọc như gạch đầu dòng (−2). Mạch tuần tự và vòng kết đạt | tay + check-rules L-089 ⚠ |
| C Rõ ý 20 | 18 | «Cái làm mình mất cả lộ trình là ý nghĩ đứt rồi thì thôi» (b04) vụng (−2). b05 đã đổi thành «quen gần hết mức của chính họ», dễ hiểu hơn (lượt 1 bị −2) | tay |
| D Fact 15 | 15 | Lượt 1 bị −6. Đã sửa: b05 «nhóm tính ra… cần», b04 «gần như chưa mất gì», b06 gán cho sách. «quen gần hết mức của chính họ» khớp «95% of their asymptote… limit of automaticity», đây là cách nói lại, chưa có Deep Research | tay, đối chiếu nguồn |
| E Độ dài/caption 15 | 15 | ƯỚC ~150s < 300s; caption EN trong kế hoạch ≤8 từ/chunk. Chưa có spec nên chưa đo phrase/hl | một phần |
| F Tone 10 | 7 | b03 khô như báo cáo («Mỗi người chọn một việc nhỏ về ăn, uống hoặc vận động…») (−3). b05 hết trừu tượng (lượt 1 bị −1). Chưa đánh `{nhấn:}` (làm ở spec) | tay |
| G CTA/hồ sơ 5 | 3 | CTA comment đo được (ngày thứ mấy) · thiếu cột Hành động/Cảm xúc (−2) | tay |
| **Tổng** | **86** (75 theo neo A gốc) · lượt 1: 77 / 66 | | |

## 3. Lỗi chặn
- (1) Bịa/phóng đại fact: không. Ở lượt 1, b05 sát ranh giới; đã sửa ở r1.
- (2) Chê năng lực người xem: không.
- (3) Dòng an toàn + credit CC BY 4.0: có trong end card. Wording credit chưa đối chiếu C-1 (vẫn chờ Hiệp).
- (4) Hook không có «bạn» + câu hỏi: **dính nếu theo rubric gốc** → xung đột X-A.
- (5) Voice/render/publish trước Chốt: không (chưa có gì ngoài chữ).
- (6) Y khoa/pháp lý ngoài nguồn: không.
- **Chặn quy trình ngoài rubric:** chuyện cá nhân (đi bộ, ngày thứ năm, hơn một tháng) đang là dựng. make-video §0 cấm bịa chuyện cá nhân, và P08 «fits real Hiệp logs only». Cần Hiệp xác nhận hoặc cho phép dựng.

## 4. Xung đột mở (không tự chọn bên)
- **X-A — neo hook của rubric vs L-103/L-104/L-105.** Rubric A và lỗi chặn 4 đòi câu 1 có «bạn» + pain + đúng 1 câu hỏi, và trừ 8 nếu hook kể ngôi «mình». L-103–105 (Hiệp 12/11, mới hơn rubric) đòi hook kể chuyện như nói với bạn thân, cho phép ngôi một. v4 theo L-103–105. Chấm theo bên nào thì tổng chênh 11 điểm, và có hay không có lỗi chặn.
- **X-B (ĐÃ ĐÓNG d5b24f2, xem mục 6) — §4b `script_hash` vs luật 08/11 «không dựng gì trước Chốt».** check-rules tính `script_hash` trên `final/spec.json`. Spec chỉ dựng sau Chốt lời, nên ở giai đoạn nháp không có hash thật; khi dựng spec, review này sẽ thành stale và phải chạy §4b lại. Cần quyết định: dựng spec chỉ có chữ trước gate 1, hay cho phép review nháp dùng hash của file .md.
- C-1 (wording credit), C-3 (rule-55 frame 0, tầng spec), C-4 (hashtag, tầng gói đăng): vẫn mở như rubric §6, không ảnh hưởng điểm lời.

## 5. Sửa đề xuất

Đã làm ở r1: ba dòng b04, b05, b06 bên dưới. Các dòng còn lại vẫn chỉ là đề xuất (b03 cho đỡ khô, b04 câu vụng, khung «điều thứ nhất»). Mỗi dòng sửa được chừng +1 tới +3 điểm, nhưng không bắt buộc để qua ngưỡng.

- b04: «mình chưa mất gì hết» → «mình gần như chưa mất gì».
- b05: «nhóm đo xem mỗi người mất bao lâu để quen gần tới mức cao nhất của chính họ. Người nhanh nhất mất 18 ngày, còn người chậm nhất mất tới 254 ngày» → «Nhóm tính ra, người nhanh nhất cần 18 ngày là việc đó gần như tự chạy, còn người chậm nhất cần tới 254 ngày». «Gần như tự chạy» thay cho «95% trần» vẫn cần Hiệp duyệt cách nói.
- b06: «thì tới giờ chưa ai đo» → «thì cuốn sách ghi là chưa ai đo».
- b03: thêm một chi tiết cho đỡ khô, ví dụ «có người chọn ăn một trái cây sau bữa trưa» (HTB Ghi chú có ví dụ này).
- b04/b07: bớt khung «điều thứ nhất / chỗ thứ nhất» nếu Hiệp thấy giống liệt kê. Hiệp đã đòi «cấu trúc tuần tự», nên giữ hay bỏ là để Hiệp chọn.

## 6. Trả lời từng góp ý trong `final/feedback.md` (feedback_seen: 4)

| # | Góp ý của Hiệp (nguyên văn) | v4 r1 đáp thế nào |
|---|---|---|
| 1 | «Script vẫn xàm thiếu tự nhiên, cả ai nói lý do nghe mới quê tuần .. thấy ngại» | Câu «lý do nghe mới quê» thuộc v3 và không còn ở v4. Theo L-106, mỗi câu chỉ một ý, dùng từ văn nói («về trễ», «xỏ giày», «vô ích»), không chèn câu tự giễu chỉ để tạo giọng. Còn một câu vụng: b04 «Cái làm mình mất cả lộ trình là ý nghĩ đứt rồi thì thôi» (C −2). Chưa ai đọc to thử. |
| 2 | «Các câu văn vẫn rời rạc không rõ nghĩa k có liên kết không có cấu trúc tuần tự gì rõ ràng» | v4 có bảng khung mạch L-107: chuyện bỏ → hai niềm tin → nghiên cứu kiểm → điều 1 sai → điều 2 sai → giới hạn → sửa đúng hai chỗ → kết. Số thứ tự ở b04/b05/b07 khớp với b02. check-rules còn cảnh báo L-089/L-094 heuristic ở các chỗ chuyển beat, đã chấm tay ở B 13/15. |
| 3 | «làm lại» | Đã đổi ý tưởng gốc theo L-095: v3 «việc ghét ba năm» được thay bằng v4 «lộ trình 30 ngày, lỡ một ngày là bỏ luôn» (e0cde74). Độ giống hook với v2 là 0,33, chuỗi beat 0,39 (đều dưới ngưỡng). |
| 4 | «Sửa và chấm lại» | Đã sửa b04/b05/b06 theo mục 5 lượt 1 (5593c26) và chấm lại: 86/100. |

**X-B đã đóng (d5b24f2):** `script_hash` giờ tính trên lời VI đã chuẩn hoá, nên nháp và spec cùng lời sẽ cùng hash. Hash của v4 r1 là `529042a178c8`. Không chấm lại vì lời không đổi.
