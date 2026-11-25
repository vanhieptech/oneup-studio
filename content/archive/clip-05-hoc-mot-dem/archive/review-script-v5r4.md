---
title: "clip-05 v5 r4 — Rule Reviewer chấm lại script (độc lập)"
date: 2026-10-26
clip: clip-05-hoc-mot-dem
draft: content/clips/clip-05-hoc-mot-dem/script-v5-draft-opencreator.md @ 499376d (không đổi tới HEAD)
previous_review: review-script-v5r3.md @ 3887210
fact_lock: fact-package-v5.md @ 5861e88
trend: research/trends/2026-10-26/clip-05-v5-trend.md @ 30b73d3; final/trend-signals.md @ cf8f291
reviewer: Rule Reviewer (người chấm ≠ người viết; không tự viết lại script)
verdict: ĐẠT — HẾT HIỆU LỰC (superseded): Hiệp bác 27/10 02:37 «Xàm quá… rời rạc», xem L-089
---

> **HẾT HIỆU LỰC (27/10 02:37, L-089):** Hiệp bác bản r4 này: «Xàm quá dậy lúc review m đọc k thấy nó rời rạc à». Review dưới đây chấm luật từng ô mà không đọc to cả bài, nên bỏ sót: đổi ngôi bạn→mình→bạn, b03 thả nghiên cứu thành danh sách, b04 «Mình muốn nhớ lâu, mà càng muốn nhớ lâu» gượng, b05 «Lần này…» nhảy cóc + câu +1 gắn thêm. `check-rules.py --flow` trên 499376d cờ đủ 5 lỗi này. Giữ file để làm bằng chứng, không dùng làm verdict.

# Verdict (cũ): ĐẠT, trình được Hiệp kèm 2 việc Hiệp quyết

Không còn lỗi chặn. B5 và B6 đã sửa đúng. Ghi chú N2–N4 của r3 đã xử lý. Còn vài ghi chú nhỏ không chặn.
Đây là ĐẠT ở bước script. Chưa có spec, nên các luật chạy trên spec (rule-55/56/58/60/61/62/64) sẽ chạy khi Hiệp đã Chốt và lên spec.

## Đo tự động (Rule Reviewer tự chạy trên 499376d)
- `check-rules.py --subjects` → 1 check · 0 ✖ · 0 ⚠ → PASS.
- `check-rules.py --l088` → 7 check · 0 ✖ · 0 ⚠ → PASS.
- Đếm chữ lời đọc (dòng 21–26): **174 chữ** (24/17/46/50/18/19). Lời không có «317», nên đọc kiểu nào cũng 174. Nằm trong 140–175 (W-14). Người viết ghi 174 trong tin nhắn nhưng commit ghi 175: số đúng là 174.
- Hook không đổi so với r3: vế đầu 2 chữ, 24 chữ. Độ giống so với c05v4/c04/c03/c02 là 0.21/0.24/0.35/0.39.
- CTA r4 so với CTA c05v4/c04/c03/c02: 0.47/0.47/0.45/0.43 (ngưỡng 0.7) → đạt.
- Caption EN: chunk dài nhất 8 từ («A week apart: still ahead of one read») → đạt P-09.
- trend-signals.md @ cf8f291 khớp beat r4 (b01, callback b04 và b05), có 2 link → đạt L-084/L-088.

## Soát lại lỗi r3
| Lỗi r3 | Kết quả r4 | Dòng |
|---|---|---|
| B5 b04 thiếu mục tiêu + thiếu chủ ngữ | **ĐÃ SỬA.** «Mình muốn nhớ lâu, mà càng muốn nhớ lâu thì các lần ôn càng nên cách xa nhau.» Có mục tiêu của nhân vật trước cách làm (W-16), có chủ ngữ (W-09). F4 giữ đúng nghĩa: không lịch, không «đều thống nhất», không «người ta thấy». «muốn nhớ lâu» lặp một lần làm cầu nối, trong giới hạn P-01 | 24 |
| B6 CTA sai nghĩa | **ĐÃ SỬA.** «…buổi thuyết trình nào muốn ôn trong ba ngày không?». Caption «Prepping a talk over three days?» cùng nghĩa | 26, 41 |
| N2 «nhích thêm một chút» mơ hồ | **ĐÃ SỬA.** «Mỗi ngày mình chỉ cần một buổi ngắn.» Đúng chữ mục Motivation +1 của fact-package-v5, không nhắc lại cách chia, không hứa kết quả | 25 |
| N3 «điều tương tự» | **ĐÃ SỬA.** «Một nghiên cứu cũng thấy vậy.» | 23 |
| N4 caption b03 lặp | **ĐÃ SỬA.** «A week apart: still ahead of one read» | 38 |

## Bảng luật r4
| ID | Luật | Dòng | Kết quả |
|---|---|---|---|
| P-05/P-06/L-057/L-058, rule-55 | Nỗi đau nói thẳng với «bạn» + câu hỏi «sao» bám đúng nỗi đau, vế đầu ≤6 chữ, không «nếu giờ…» | 21 | ĐẠT |
| L-088 (a) | Một câu báo nghiên cứu (b03), F4 là lý do trong b04, không mở kiểu trích dẫn | 23–24 | ĐẠT |
| L-088 (b) | Hook/CTA mới, kiểu hook khác 2 clip trước | 21, 26 | ĐẠT |
| L-088 (c) | Trend chỉ ở hình, thông điệp +1 «mỗi ngày một buổi ngắn» | 25, 36–41 | ĐẠT |
| L-088 / P-03 fact | F1 (b03, đủ 3 nhóm, đều so «đọc một lần»), F2 (hook), F3 (b04 «như cẩm nang gợi ý», b05), F4 (b04), F5 (b04). Không dùng gì trong danh sách Cấm, không hứa kết quả | 21–25 | ĐẠT |
| L-087 | Ví dụ đời thường (tài liệu buổi họp), không môn học | toàn bộ | ĐẠT |
| W-16 / L-077 | hook → ví dụ → nguyên nhân + dẫn chứng → mục tiêu → cách làm → kết quả → CTA | 21–26 | ĐẠT |
| W-09 | Câu đủ chủ ngữ | 21–26 | ĐẠT |
| W-14 / rule-7 | 174 chữ, một CTA, quay về cách làm | 21–26 | ĐẠT |
| P-01 / L-054 | Mỗi ý một lần (chỉ lặp có chủ đích: «hai lần liền» b02→b03, «sếp hỏi lại» b01→b05, «người đọc một lần» ×2 do fact lock) | 21–26 | ĐẠT |
| P-04 | Không từ hiếm hay mơ hồ | 21–26 | ĐẠT (N2, N3) |
| P-07 / P-02 | Không chê người học, không câu an ủi chung chung | toàn bộ | ĐẠT |
| P-08 / L-024 | Văn nói, mềm, miền Nam | 21 | ĐẠT (H2 «thế») |
| W-10 | Câu hỏi với người xem mềm («muốn ôn») | 26 | ĐẠT |
| rule-56 | Có challenge + loop («thuyết trình» gọi lại «trình bày») | 26 | ĐẠT |
| W-12 | Phần nghiên cứu ≤ ~25 chữ | 23 | CHẤP NHẬN CÓ ĐIỀU KIỆN: b03 46 chữ vì F1 bắt nói đủ 3 nhóm, tổng chữ vẫn trong trần |
| P-09 | Caption ≤8 từ, cùng nghĩa với lời | 36–41 | ĐẠT (N4) |
| P-10 | Dòng an toàn + credit, không ghi tác giả bảo trợ | 30 | ĐẠT (N5) |
| L-084 | Thấy trend ở b01 + dòng trend-signals | 36, cf8f291 | ĐẠT |
| L-045/L-053 | Ví dụ ngôi «mình» | 22 | ĐẠT, chờ Hiệp quyết (H1) |

## Phán quyết «nhanh thế» và «nhanh vậy» (dòng 21)
- **Lý do người viết đưa ra không khớp L-082.** L-082 ghi: câu hỏi mà âm tiết cuối mang thanh huyền/nặng thì **được miễn luật lên giọng, cấm nâng pitch nhân tạo**, câu hỏi nhận ra nhờ từ hỏi + dấu «?». Tức là L-082 không bắt tránh thanh nặng ở cuối câu hỏi. Nó chỉ bỏ yêu cầu lên giọng. «Sao ý đó trôi nhanh vậy?» có từ hỏi «Sao» nên vẫn đạt L-082. Lý do «vậy khó lên giọng» vì thế không cần.
- **Luật giọng vùng miền:** luật 41/105/211 và voice-profile ghi «miền Nam». «thế» là chữ giọng Bắc, «vậy» là chữ miền Nam. Nhưng không có luật hay check nào cấm «thế», nên đây không phải lỗi chặn.
- **Kết luận:** hai luật này **không thật sự xung đột**, vì L-082 đã xử lý chuyện thanh điệu. Luật viết nghiêng về «vậy». Không chặn. Rule Reviewer khuyên dùng «vậy». Vì người viết muốn giữ «thế», ghi thành mục **H2** cho Hiệp chọn. Nếu chọn «vậy» thì không cần News thử giọng trước khi chốt, theo L-082.

## Ghi chú không chặn
- **N1, dòng 25 + 22 + 26, chữ «buổi» lại mang 2 nghĩa:** «buổi họp» (22) và «buổi thuyết trình» (26) là sự kiện, còn «một buổi ngắn» (25) là buổi ôn. Lỗi này do chính gợi ý N2 ở r3 của Rule Reviewer dùng «buổi ngắn» để khớp chữ fact package. Nghĩa vẫn hiểu được nhờ ngữ cảnh nên chấp nhận. Nếu muốn sạch thì đổi 25 thành «một tiếng ngắn» hoặc «một lần ôn ngắn», nhưng phải cân với chữ của fact package.
- **N2, dòng 25, «mình dễ nhớ ra hơn»:** bỏ «ý đó» để bù chữ, nên vòng quay về chỗ khựng còn dựa vào «sếp hỏi lại». Vẫn đạt W-06. Nếu Hiệp muốn rõ hơn thì thêm lại «ý đó» (+2 chữ, vẫn ≤175 nếu bớt một chữ chỗ khác).
- **N3, dòng 22, «đọc chồng tài liệu»:** bỏ «cả» để bù chữ, nên chữ «chồng» lại dễ vấp như r2 (N7). Không chặn, News nghe thử khi làm giọng.
- **N4, caption b05, «Just one short session a day»:** khớp nghĩa lời.
- **N5, post.md (rule-13/53, P-10):** end card đã có dòng an toàn nguyên văn, credit đúng chuỗi bắt buộc và ghi chú không bảo trợ. **post.md bắt buộc** có thêm link https://creativecommons.org/licenses/by/4.0/ và chữ «đã chuyển thể». check-rules `--final` chặn nếu thiếu.
- **N6, hình (từ r3, vẫn còn):**
  - «sếp (chibi)» là nhân vật mới, luật 43 chỉ cho rig Hiệp/Omi. Nên thể hiện bằng tay/bút chỉ slide + bong bóng «?», hoặc hỏi Hiệp.
  - b04 dài 50 chữ ≈ 12s > 8s/cảnh (rule-9), nên khi làm spec phải tách cảnh, mỗi cảnh một hiệu ứng chính (W-01).
- **N7, tài liệu:** dòng 8 frontmatter «format» và mục «Trend signal» (ghi ecb8614, giờ là cf8f291) còn chữ cũ. Commit ghi 175 chữ, thực tế 174. Không ảnh hưởng lời.

## Hiệp quyết
- **H1, dòng 22:** giữ «Thường thì tối trước buổi họp, mình dồn…» (cách làm phổ biến, không khẳng định là chuyện thật) hay đổi lại «Mình cũng từng vậy. Tối trước buổi họp, mình dồn…» (Thầy tự nhận, L-053, +3 chữ, phải bớt chữ chỗ khác để ≤175). Cả hai đều đúng luật.
- **H2, dòng 21:** «Sao ý đó trôi nhanh **thế**?» (người viết giữ) hay «…nhanh **vậy**?» (miền Nam, Rule Reviewer khuyên). L-082 cho phép cả hai, không cần thử giọng trước.

## Rủi ro còn lại
- 174/175 chữ: mọi chữ thêm vào (H1, N2) đều phải bớt chữ chỗ khác.
- Luật chạy trên spec chưa chạy được, đặc biệt rule-58 (từ nối đầu beat theo danh sách: «Thường thì», «Mình muốn», «Lần này» có thể ✖, xem X-04/X-09, báo cả hai chứ không quay lại câu mẫu) và rule-56 (comment-challenge).
- Trend brain stacking chỉ có trong hình. Phải soát still b01 để thấy rõ chồng tài liệu, ly cà phê, điện thoại úp (L-084).
- Chưa Chốt thì không làm giọng hay render (L-072).
