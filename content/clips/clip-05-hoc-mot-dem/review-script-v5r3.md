---
title: "clip-05 v5 r3 — Rule Reviewer chấm lại script (độc lập)"
date: 2026-10-26
clip: clip-05-hoc-mot-dem
draft: content/clips/clip-05-hoc-mot-dem/script-v5-draft-opencreator.md @ 774afe1 (không đổi tới HEAD cf8f291)
previous_review: review-script-v5r2.md @ 5dbaa8b
fact_lock: fact-package-v5.md @ 5861e88
trend: research/trends/2026-10-26/clip-05-v5-trend.md @ 30b73d3; final/trend-signals.md @ cf8f291
reviewer: Rule Reviewer (người chấm ≠ người viết; không tự viết lại script)
verdict: CHƯA ĐẠT
---

# Verdict: CHƯA ĐẠT (2 lỗi chặn nhỏ, sửa được mà không tăng số chữ)

B1–B4 của r2 đã sửa đúng. Còn 2 lỗi mới: b04 mất câu mục tiêu (W-16) và có một câu thiếu chủ ngữ (W-09); CTA nói «chia buổi thuyết trình ra ba ngày» nên bị sai nghĩa.

## Đo tự động (Rule Reviewer tự chạy trên 774afe1)
- `check-rules.py --subjects` → 1 check · 0 ✖ · 0 ⚠ → PASS.
- `check-rules.py --l088` → 7 check · 0 ✖ · 0 ⚠ → PASS. Nguồn tìm thấy: Rawson & Kintsch 2005, Cepeda (et al.) 2006, Dunlosky et al. 2013, Yang et al. 2021.
- Đếm chữ lời đọc (dòng 21–26): **175 chữ** (24/18/48/46/20/19). Lời không còn «317», nên đọc kiểu nào cũng ra 175. Vừa chạm trần W-14 (140–175).
- Hook: vế đầu «Hôm họp,» 2 chữ, câu đầu 7 chữ, cả hook **24 chữ** (người viết ghi 23). Skill craft cho khoảng ~20 → chấp nhận.
- Hook/CTA so với bản khoá trước (difflib, bỏ dấu): hook 0.21 / 0.24 / 0.35 / 0.39 (c05v4/c04/c03/c02). CTA 0.49 / 0.47 / 0.50 / 0.43. Ngưỡng 0.7 → đạt. Hook giống r2 0.82, nhưng r2 là nháp chưa khoá của chính clip này, nên không tính.
- Caption EN: 22 chunk, dài nhất 7 từ → đạt P-09.
- trend-signals.md @ cf8f291: dòng «Trend trong clip: b01 … callback b04 … và b05», ghi đúng r3 774afe1 và có 2 link → đạt L-084/L-088.

## Soát lại B1–B4 (review r2)
| Lỗi r2 | Kết quả r3 | Dòng |
|---|---|---|
| B1 b03 thiếu «người đọc một lần» | **ĐÃ SỬA.** «…vẫn hơn người đọc một lần», caption có «Still ahead of one read» | 23, 38 |
| B2 212 chữ + lặp ý | **ĐÃ SỬA.** 175 chữ, hook chỉ một «hai hôm», ý chia ngày chỉ ở b04, bỏ «tới lúc sếp hỏi». Nhưng câu mục tiêu bị bỏ theo → B5 | 21–26 |
| B3 b05 khối nghiên cứu thứ hai | **ĐÃ SỬA.** Bỏ «Gộp 317 thí nghiệm… người ta thấy». F4 chỉ còn một vế lý do ở b04, Cepeda nằm ở hình và end card. Chỉ còn một câu báo nghiên cứu (b03) | 24, 39 |
| B4 hook vế đầu 8 chữ / 29 chữ | **ĐÃ SỬA.** Vế đầu 2 chữ, 24 chữ, câu hỏi «sao» bám đúng nỗi đau | 21 |

## Bảng luật r3
| ID | Luật | Dòng | Kết quả | Ghi chú |
|---|---|---|---|---|
| P-05/P-06/L-057/L-058 | Nói thẳng nỗi đau với «bạn» + câu hỏi bám đúng nỗi đau, không «nếu giờ…» | 21 | ĐẠT | Nỗi đau rơi vào chữ 8–18, câu hỏi «Sao ý đó trôi nhanh thế?» |
| rule-55 | Vế đầu ≤6 chữ | 21 | ĐẠT | «Hôm họp,» |
| L-088 (b) | Hook/CTA mới, kiểu hook khác 2 clip trước | 21, 26 | ĐẠT | Khoảnh khắc peak + câu hỏi «sao» |
| L-088 (a) | Dẫn chứng lồng vào chuyện, chỉ một câu báo nghiên cứu | 23–24 | ĐẠT | b03 nối với b02 bằng «cũng thấy điều tương tự», b04 dùng F4 làm lý do cho cách làm. Không có «người ta thấy» hay «các nhà nghiên cứu thấy» |
| L-088 (c) | Trend chỉ là móc, thông điệp +1 | 25, 36–40 | ĐẠT (N2) | Nốt +1 «nhích thêm một chút» hơi chung chung |
| L-088 / P-03 fact | F1–F5, không bịa số hay cơ chế, không hứa kết quả | 21–25 | ĐẠT | b03 = F1 đúng 3 nhóm, đều so với «đọc một lần». b04 câu 1 = F4 (không lịch, không «đều thống nhất»). Câu 2 = F3 («như cẩm nang gợi ý»). Câu 3 = F5. b05 «dễ nhớ ra hơn» là minh hoạ. Không dùng gì trong danh sách Cấm |
| L-087 | Ví dụ đời thường, không môn học | toàn bộ | ĐẠT | Đọc tài liệu cho buổi họp |
| **W-16 / L-077** | Có câu mục tiêu trước giải pháp | 24 | **CHƯA ĐẠT** | B5 |
| **W-09 / L-071** | Câu đủ chủ ngữ | 24 | **CHƯA ĐẠT** | «Càng muốn nhớ lâu, …» không có người muốn (B5) |
| W-14 / rule-7 | 140–175 chữ, một CTA | 21–26 | ĐẠT | 175 chữ, một câu hỏi + lời mời comment |
| CTA rõ nghĩa | CTA đúng ý cách làm | 26 | **CHƯA ĐẠT** | B6 |
| «buổi» một nghĩa | skill craft §3 | 22, 26 | ĐẠT | Chỉ còn nghĩa sự kiện (buổi họp / buổi thuyết trình) |
| P-01 / L-054 | Mỗi ý một lần | 21–26 | ĐẠT | Chỉ lặp có chủ đích: «hai lần liền» b02→b03 (nhân vật sống lại nghiên cứu), «sếp hỏi lại» b01→b05 (đóng vòng), «người đọc một lần» ×2 ở b03 (fact lock bắt buộc) |
| W-12 | Phần nghiên cứu ≤ ~25 chữ | 23 | CHẤP NHẬN CÓ ĐIỀU KIỆN (N4) | b03 dài 48 chữ vì F1 bắt nói đủ 3 nhóm. Tổng chữ vẫn trong trần |
| P-04 | Không từ hiếm hay mơ hồ | 23, 25 | ĐẠT (N2, N3) | |
| P-07 | Không chê người học | toàn bộ | ĐẠT | |
| P-08 / L-024 | Văn nói, mềm, miền Nam | 21 | ĐẠT (N1) | «thế» là giọng Bắc |
| W-10 | Câu hỏi với người xem mềm | 26 | ĐẠT | |
| rule-56 | Có challenge + loop | 26 | ĐẠT | «thuyết trình» gọi lại «trình bày» ở hook |
| P-09 | Caption EN ≤8 từ/chunk, cùng nghĩa với lời | 36–41 | ĐẠT (N5) | |
| P-10 | Dòng an toàn + credit, không ghi tác giả bảo trợ | 30 | ĐẠT (N6) | |
| L-084 | Thấy trend ở b01 + dòng trend-signals | 36, trend-signals 14 | ĐẠT | cf8f291 |
| L-045/L-053 | Ví dụ ngôi «mình» | 22 | ĐẠT, chờ Hiệp quyết (H1) | |

## Lỗi chặn
**B5. Dòng 24 (b04), câu 1: «Càng muốn nhớ lâu, các lần ôn càng nên cách xa nhau.»**
Câu này là nguyên tắc chung, không phải mục tiêu của nhân vật. W-16/L-077 bắt buộc có mục tiêu trước giải pháp. Hiệp đã từng bắt lỗi đúng chuyện «mục tiêu là gì mà đã đưa giải pháp». Vế «Càng muốn nhớ lâu» cũng thiếu chủ ngữ (W-09).
Sửa: thêm người muốn + mục tiêu ngay trong câu này, giữ nguyên nghĩa F4. Ví dụ hướng: «Mình muốn nhớ lâu, mà càng muốn nhớ lâu thì các lần ôn càng nên cách xa nhau.» (+3 chữ). Để bù chữ: dòng 23 «điều tương tự» → «vậy» (−2, cũng xử lý N3), dòng 22 bỏ «cả» (−1) → tổng vẫn 175.

**B6. Dòng 26 (CTA): «…buổi thuyết trình nào muốn chia ra ba ngày không?»**
Câu này nói chia *buổi thuyết trình* ra ba ngày, trong khi cách làm là chia *việc ôn hay chuẩn bị*. Caption «Got a presentation coming up?» cũng đã bỏ mất nửa ý này.
Sửa (không tăng chữ): «…buổi thuyết trình nào muốn **ôn trong** ba ngày không?» («ôn» khớp «các lần ôn» ở b04). Caption gợi ý: «Prepping a talk over three days?».

## Ghi chú không chặn
- **N1, dòng 21, «nhanh thế»:** «thế» là giọng Bắc, kênh dùng văn nói miền Nam (L-024). Người viết bỏ «vậy» vì sợ thanh nặng khó lên giọng, nhưng L-082 đã miễn luật lên giọng cho âm tiết cuối mang thanh nặng/huyền: câu hỏi vẫn nhận ra nhờ «Sao» + dấu «?». Có thể đổi lại «vậy». Không chặn.
- **N2, dòng 25, «Mỗi ngày, mình chỉ nhích thêm một chút.»:** «một chút» hơi chung chung, mà Hiệp không thích cụm mơ hồ. Nên gắn vào việc đếm được, vẫn đúng mục Motivation của fact-package-v5 («mỗi ngày một buổi ngắn»). Ví dụ hướng: «Mỗi tối chỉ một buổi ngắn, mà mình tiến lên được một chút.» Câu sửa không được nhắc lại cách chia ngày.
- **N3, dòng 23, «điều tương tự»:** hơi chung. Đổi «vậy» như gợi ý ở B5.
- **N4, W-12:** b03 dài 48 chữ, quá mức ~25 của W-12, nhưng F1 bắt nói đủ 3 nhóm và Deep Research đã khoá nghĩa này. Chấp nhận vì tổng chữ nằm trong trần. Nếu Hiệp chê b03 dài thì rút b03 trước tiên, nhưng phải giữ «người đọc một lần».
- **N5, caption b03 (dòng 38):** «…still ahead · Still ahead of one read» lặp chữ. Gộp thành một chunk: «A week apart: still ahead of one read» (8 từ).
- **N6, P-10 / rule-13 / rule-53:** end card đã có dòng an toàn nguyên văn, credit đúng chuỗi bắt buộc và câu không ghi tác giả bảo trợ. **post.md bắt buộc** có thêm link giấy phép https://creativecommons.org/licenses/by/4.0/ và chữ «đã chuyển thể» (check-rules `--final` sẽ chặn nếu thiếu).
- **N7, hình:** «sếp (chibi)» là nhân vật mới, trong khi luật 43 chỉ cho rig Hiệp/Omi. FLUX/News thể hiện sếp bằng tay/bút chỉ slide + bong bóng «?», hoặc hỏi Hiệp trước. b04 đang gánh 2 cảnh (dải lịch Cepeda + tách 3 chồng): lời 46 chữ ≈ 11s > 8s/cảnh (rule-9), nên khi làm spec phải tách cảnh, mỗi cảnh một hiệu ứng chính (W-01).
- **N8:** dòng 8 frontmatter «format» vẫn ghi beat «bằng chứng» riêng như r2. Chỉ là tài liệu cũ, sửa cho khớp 6 beat.

## Hiệp quyết
- **H1, dòng 22, «Thường thì tối trước buổi họp, mình dồn…»** (Deep Research đã đổi từ «Mình cũng từng vậy»). Đã kiểm: câu mới không còn khẳng định trải nghiệm thật một lần, chỉ còn «mình» chỉ thói quen chung. L-053/L-045 cho phép cả hai cách. Hiệp chọn giữ «Thường thì…» hay đổi lại «Mình cũng từng vậy.» (Thầy tự nhận). Không chặn.

## Rủi ro còn lại
- 175 chữ là đúng trần. Sửa B5/B6 phải bù chữ như đã gợi ý, nếu không sẽ vượt.
- Chưa có spec, nên rule-55/56/58/60/61/62/64 chỉ mới soát tay. Khi lên spec phải chạy check-rules đầy đủ (L-046).
- Trend brain stacking chỉ có trong hình. Nếu hình không đọc ra «chồng sách/cà phê/điện thoại úp» thì người xem không thấy trend (L-084, soát still).

## Bước tiếp
OpenCreator sửa B5/B6 (N1–N3, N5 nên sửa luôn), đăng xin duyệt trong group. Rule Reviewer đếm chữ và chấm lại. Chưa Chốt thì không làm giọng hay render.
