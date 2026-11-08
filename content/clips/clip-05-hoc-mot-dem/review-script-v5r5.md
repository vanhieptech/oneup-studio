---
title: "clip-05 v5 r5 / r5.1 — Rule Reviewer chấm (cổng đọc to L-089 trước)"
date: 2026-10-27
clip: clip-05-hoc-mot-dem
draft: content/clips/clip-05-hoc-mot-dem/script-v5-draft-opencreator.md @ 25b5b78 (r5.1; r5 = 7a9661e)
fact_lock: fact-package-v5.md @ 5861e88
trend: final/trend-signals.md @ cf8f291
reviewer: Rule Reviewer (người chấm ≠ người viết; không tự viết lại script)
verdict: CHƯA ĐẠT
---

# Verdict: CHƯA ĐẠT (1 lỗi chặn ở cổng đọc to; các luật khác đạt)

Bản chấm là **r5.1 (25b5b78)**. Sau khi giao việc chấm r5 (7a9661e), OpenCreator đã commit thêm r5.1 với b03 theo câu Deep Research đề xuất. Mình chấm bản mới nhất và ghi riêng phần thay đổi r5 → r5.1 ở b03.

## 1. Cổng đọc to liền mạch (L-089), làm trước khi chấm luật
Đọc to b01→CTA một mạch như người xem (văn bản liền ở dòng 28 khớp đúng 6 beat):

> Hôm họp, bạn trình bày trơn tru. Vậy mà hai hôm sau, sếp hỏi lại một ý, bạn đứng hình. Sao ý đó trôi nhanh thế? Có thể vì tối trước buổi họp, bạn dồn ba tiếng đọc chồng tài liệu hai lần liền. Một nghiên cứu về cách đọc cũng thấy vậy. Đọc liền hai lần thì ngay sau đó nhớ hơn người đọc một lần, nhưng hai ngày sau không còn hơn. Còn nếu đọc lần hai cách một tuần, hai ngày sau vẫn hơn. Vậy muốn nhớ tới lúc bị hỏi lại, bạn có thể chia ba tiếng ra ba ngày, như cẩm nang gợi ý. Mỗi tối, bạn thử úp tài liệu, tự nói lại ý chính, rồi lật lên xem sót chỗ nào. Rồi lúc sếp hỏi lại, bạn dễ nhớ ra ý đó hơn. Bạn chỉ cần mỗi ngày một buổi ngắn, nhích thêm một chút. Sắp tới bạn có buổi thuyết trình nào muốn thử cách này không? Kể OneUp nghe dưới comment nha.

Nhận xét bằng lời thường:
- **Tốt hơn r4 rõ rệt.** Cả bài một ngôi «bạn», không còn nhảy bạn→mình→bạn. Mỗi beat nối với beat trước: «Vậy mà» (đảo kỳ vọng trong hook), «Có thể vì» (trả lời câu hỏi hook), «cũng thấy vậy» (nghiên cứu đi ra từ chuyện đọc dồn), «Vậy muốn nhớ…» (mục tiêu rồi cách làm), «Rồi lúc sếp hỏi lại» (quay về chỗ khựng). Không còn cụm khâu lặp kiểu «X, mà càng X». b03 nghe như kể tiếp, không còn đọc như danh sách nhóm.
- **Chỗ còn vấp (chặn):** câu «Bạn chỉ cần mỗi ngày một buổi ngắn, nhích thêm một chút.» ở b05. Câu trước vừa đóng vòng xong («bạn dễ nhớ ra ý đó hơn»), câu này như khẩu hiệu dán thêm vào, không có chữ nối. «nhích thêm một chút» lại là cụm mơ hồ mà r3 (N2) đã bắt và r4 đã bỏ. Đây đúng loại lỗi «+1 gắn thêm» Hiệp vừa chê ở r4 (L-089 (c)).
- Chỗ nghe hơi gợn (không chặn): CTA «thử **cách này**» là đại từ trống (skill craft §3). «Kể OneUp nghe» được, vì người kể chưa xưng «mình» lần nào.

## 2. Đo tự động (Rule Reviewer tự chạy trên 25b5b78)
- `check-rules.py --flow` → 6 check · 0 ✖ · **1 ⚠**: «câu chốt/motivation đứng trơ cuối beat: b05 «Bạn chỉ cần mỗi ngày một buổi ngắn, nhích thêm một chút.»». Các cờ khác ✔: ngôi kể nhất quán (bạn ở cả 6 beat, b03 trung tính), không khâu lặp, beat nào cũng mở bằng mối nối, không liệt kê song song. Để đối chứng, r4 (499376d) bị cờ 5 ⚠.
- `check-rules.py --subjects` → PASS, 0 ⚠. `check-rules.py --l088` → 7 check · 0 ✖ · 0 ⚠ → PASS.
- **171 chữ** (26/18/43/41/24/19), lời không có «317». File ghi 171 là đúng. Commit r5 ghi 175 là số của bản r5 trước khi sửa b03.
- Hook: vế đầu «Hôm họp,» 2 chữ, cả hook 26 chữ (~20 là mức skill, hơi dài nhưng nhờ có «Vậy mà» nên nghe liền). Hook giống clip trước nhiều nhất 0.41, CTA 0.46 (ngưỡng 0.7).
- Caption EN: chunk dài nhất 8 từ («A week apart: still ahead after two days», «Got a presentation coming up to try this?») → đạt P-09.
- trend-signals.md @ cf8f291: b01 + callback b04/b05 khớp r5.1.

## 3. b03 so với F1 và các quy định của Deep Research
- **r5 (7a9661e):** «Đọc liền hai lần giúp nhớ tốt ngay sau khi đọc, nhưng hai ngày sau không còn hơn người đọc một lần. Còn nếu đọc lần hai cách một tuần, hai ngày sau cái lợi đó vẫn còn.» → **Đồng ý với Deep Research, câu này lệch:** «cái lợi đó» chỉ ngược về «nhớ tốt ngay sau khi đọc», nghe như nhóm cách một tuần sau hai ngày vẫn nhớ tốt y như lúc vừa đọc. F1 không nói vậy. Vế đầu lại thiếu mốc so «người đọc một lần» cho kết quả kiểm tra ngay.
- **r5.1 (25b5b78), dòng 23:** «Đọc liền hai lần thì ngay sau đó nhớ hơn người đọc một lần, nhưng hai ngày sau không còn hơn. Còn nếu đọc lần hai cách một tuần, hai ngày sau vẫn hơn.» Đây đúng câu Deep Research đề xuất → **đạt F1**:
  - Mốc «người đọc một lần» nói rõ ở vế đầu. Hai vế sau («không còn hơn», «vẫn hơn») tỉnh lược cùng mốc đó, nằm ngay sát nhau, có «vẫn» nối lại. Mốc so không còn mơ hồ. Lưu ý: r2 (B1) Rule Reviewer đòi nói lại mốc so ở vế cuối, vì khi đó vế đầu là cả một câu dài chen giữa. Ở r5.1 mốc đứng ngay câu trước và chính Deep Research (người giữ fact) xác nhận đủ rõ, nên chấp nhận.
  - Không nói đọc hai lần là vô ích: «ngay sau đó nhớ hơn» → đạt.
  - Nghiên cứu chỉ thử khoảng cách **một tuần**, còn «ba ngày» được gán cho cẩm nang («như cẩm nang gợi ý», F3) ở b04 → không trộn → đạt.
  - Số chữ: b03 r5.1 = 43 chữ, tổng 171 ≤ 175 → đạt.
- Câu báo nghiên cứu «Một nghiên cứu về cách đọc cũng thấy vậy» nối vào giả thuyết «Có thể vì… đọc… hai lần liền» của b02 → dẫn chứng đi ra từ chuyện (L-088 (a)).

## 4. Bảng luật
| ID | Luật | Dòng | Kết quả |
|---|---|---|---|
| **L-089** | Cổng đọc to: một ngôi kể, mỗi beat có mối nối, không câu gắn thêm, dẫn chứng từ chuyện, không ép câu vì số chữ | 21–26 | **CHƯA ĐẠT**: b05 câu +1 gắn thêm (B1). Phần còn lại đạt |
| P-05/P-06/L-057/L-058, rule-55 | Nỗi đau nói với «bạn» + câu hỏi «sao» bám đúng nỗi đau, vế đầu ≤6 chữ | 21 | ĐẠT |
| W-16 / L-077 | hook → nguyên nhân (b02) + dẫn chứng (b03) → mục tiêu («muốn nhớ tới lúc bị hỏi lại») → cách làm → kết quả → CTA | 21–26 | ĐẠT |
| L-088 | Có nguồn, có file trend/fact, dẫn chứng lồng vào chuyện, hook/CTA mới, +1 | 21–26 | ĐẠT (nốt +1: xem B1) |
| P-03 / fact | F1 (b03, r5.1), F2 (hook), F3 (b04), F5 (b04). F4 chỉ còn ở hình b04 + end card. Không dùng gì trong danh sách Cấm, không hứa kết quả | 21–25 | ĐẠT |
| L-087 | Ví dụ đời thường, không môn học | toàn bộ | ĐẠT |
| W-09 | Câu đủ chủ ngữ | 21–26 | ĐẠT (N3: «Đọc liền hai lần» làm chủ ngữ) |
| W-10 / L-045 | Câu với người xem mềm: «có thể chia», «thử úp», «muốn thử» | 24, 26 | ĐẠT |
| W-14 | 171 chữ, một CTA | 21–26 | ĐẠT |
| P-01 | Mỗi ý một lần: «hỏi lại» b01/b04/b05 là móc vòng, «hai lần liền» b02→b03 là cầu nối | 21–26 | ĐẠT |
| P-04 | Không cụm mơ hồ | 25, 26 | **CHƯA ĐẠT** ở «nhích thêm một chút» (gộp vào B1). «cách này» xem N1 |
| P-07 / P-02 | Không chê người học, không câu an ủi chung | toàn bộ | ĐẠT |
| W-12 | Phần nghiên cứu ≤ ~25 chữ | 23 | CHẤP NHẬN CÓ ĐIỀU KIỆN: 43 chữ vì F1 bắt nói đủ 3 nhóm |
| rule-56 | Có challenge + loop («thuyết trình» gọi lại «trình bày») | 26 | ĐẠT |
| P-09 | Caption ≤8 từ, cùng nghĩa | 38–43 | ĐẠT |
| P-10 | Dòng an toàn + credit, không ghi tác giả bảo trợ | 32 | ĐẠT (N5) |
| L-084 | Thấy trend ở b01 + dòng trend-signals | 38, cf8f291 | ĐẠT |

## 5. Lỗi chặn
**B1. Dòng 25 (b05), câu 2: «Bạn chỉ cần mỗi ngày một buổi ngắn, nhích thêm một chút.»** Câu +1 đứng trơ sau câu đóng vòng, không có chữ nối (L-089 (c), `--flow` ⚠). «nhích thêm một chút» mơ hồ (P-04). «buổi ngắn» lại làm «buổi» mang hai nghĩa (buổi họp/thuyết trình và buổi ôn).
Sửa, chọn một trong hai, rồi đọc to lại b05→CTA:
(a) Gộp nốt +1 vào câu kết quả bằng chữ nối, nói việc nhỏ đếm được theo F3: ví dụ hướng «Rồi lúc sếp hỏi lại, bạn dễ nhớ ra ý đó hơn, mà mỗi tối chỉ tốn chừng một tiếng.» (b05 còn 20 chữ, tổng ≈ 167).
(b) Bỏ câu đó (L-089 (e): bỏ ý chứ không ép câu) và để CTA mang nốt +1 (việc nhỏ làm từ tối nay). Không được bỏ hẳn tinh thần +1 của L-088.

## 6. Ghi chú không chặn
- **N1, dòng 26, «thử cách này»:** skill craft §3 tránh đại từ trống («nó», «cách này») trong lời. Gợi ý nói rõ việc: «muốn thử chia ra ba ngày không?». Caption b06 sửa theo.
- **N2, dòng 26, «Kể OneUp nghe»:** khi làm giọng phải phiên âm «OneUp» trong `say` (L-025 brand-respell), nếu không F5 đọc sai.
- **N3, dòng 23, «Đọc liền hai lần thì… nhớ hơn người đọc một lần»:** chủ ngữ là một việc nhưng lại so với một người. Nói được, Deep Research đã duyệt. Nếu đọc to vẫn gợn thì đổi «Người đọc liền hai lần…».
- **N4, ngôi «bạn» kể cả bài vs L-045/L-053 («mình» làm mẫu):** L-089 (Hiệp 27/10) mới nhất nên thắng. Câu với người xem đã mềm («có thể», «thử»), không thành ra lệnh. Mục H1 cũ (b02 «Thường thì» / «Mình cũng từng vậy») không còn, vì b02 giờ là «Có thể vì…».
- **N5, post.md:** bắt buộc có link https://creativecommons.org/licenses/by/4.0/ và chữ «đã chuyển thể» (rule-13/53).
- **N6, hình:** «sếp (chibi)» là nhân vật mới, luật 43 chỉ cho rig Hiệp/Omi (FLUX/News xử lý). b04 41 chữ ≈ 10s > 8s/cảnh, nên khi làm spec phải tách cảnh. Dải lịch Cepeda ở b04 giờ không có lời đi kèm: hình phải tự nói được «nhớ lâu hơn thì giãn xa hơn», hoặc bỏ.

## 7. Hiệp quyết
- **H2, dòng 21: «nhanh thế» hay «nhanh vậy».** Vẫn còn. L-082 cho phép cả hai (âm tiết cuối thanh nặng được miễn lên giọng, câu hỏi nhận qua «Sao» + «?»). Giọng miền Nam nghiêng về «vậy». Rule Reviewer khuyên «vậy», người viết giữ «thế». Không chặn.

## Bước tiếp
OpenCreator sửa B1 (và N1 nếu đồng ý), rồi xin duyệt trong group. Rule Reviewer đọc to lại cả bài (L-089) rồi mới chấm luật. Chưa Chốt thì không làm giọng hay render.
