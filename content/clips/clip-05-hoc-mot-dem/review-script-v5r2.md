---
title: "clip-05 v5 r2 — Rule Reviewer chấm script (độc lập)"
date: 2026-10-26
clip: clip-05-hoc-mot-dem
draft: content/clips/clip-05-hoc-mot-dem/script-v5-draft-opencreator.md @ 84c4fcc (không đổi tới HEAD ecb8614)
fact_lock: fact-package-v5.md @ 5861e88
trend: research/trends/2026-10-26/clip-05-v5-trend.md @ 30b73d3; final/trend-signals.md @ ecb8614
reviewer: Rule Reviewer (người chấm ≠ người viết, L-076/L-086; không tự viết lại script)
verdict: CHƯA ĐẠT
---

# Verdict: CHƯA ĐẠT (4 lỗi chặn, 9 ghi chú)

Đã đọc lại: logs/lessons.md (tới L-088), logs/rule-checklist.md (A–E, X-01..X-09), skill make-video, short-video-script-craft. Số đo do Rule Reviewer tự chạy, không dùng các dòng «PASS» của người viết.

## Đo tự động (chạy 26/10, trên 84c4fcc)
- `check-rules.py --subjects script-v5-draft-opencreator.md` → 1 check · 0 ✖ · 0 ⚠ → PASS (L-087).
- `check-rules.py --l088 script-v5-draft-opencreator.md` → 7 check · 0 ✖ · 0 ⚠ → PASS (nguồn truy được, lời có dẫn chứng, hook/CTA không giống 5 clip trước, file trend có link, file fact DR). Phần manual gate (a)(b)(c) chấm ở bảng dưới.
- Không có chế độ draft nào khác. check-rules chạy trên spec (rule-55/56/58/60…) chưa chạy được vì chưa có spec v5. Mình soát trước các lỗi spec sẽ bắt (L-046).
- Đếm chữ lời đọc (b01–b07, dòng 22–28): **212 chữ** (29/19/46/48/22/29/19). Nếu tính «317» đọc thành «ba trăm mười bảy» thì là 215 âm tiết.
- So hook/CTA với bản khoá trước (difflib, bỏ dấu): hook so với c05v4 0.29, c04 0.32, c03 0.32, c02 0.37. CTA so với c05v4 0.44, c04 0.43, c03 0.41, c02 0.40 (ngưỡng 0.7). 6 chữ đầu khác hết. CTA không mở bằng «Còn bạn», không có «Comment số/con số/một chữ».

## Câu hỏi mở của OpenCreator: «đọc→hỏi ~3 ngày» ở hook có khớp F1/F2 không?
- Lời hook thật (dòng 22) ghi **«hai hôm sau»**, không có «3 ngày». Kết quả (dòng 27) cũng ghi «hai hôm sau». Cả hai khớp mốc hai ngày của Rawson & Kintsch (F1) → **không lệch**. Deep Research cũng đã xác nhận giữ nguyên.
- Lưu ý để giữ đúng: F1 chỉ nói sau hai ngày nhóm đọc liền **hết hơn** nhóm đọc một lần, chứ không nói là quên sạch. Chữ «trôi mất» ở hook là cảm giác của người xem, dựa trên F2 («quên nhanh»), và không gắn vào nghiên cứu → đạt. Đừng thêm «quên hết/quên sạch» vào b03.
- Nếu ở đâu đó (caption, hình, post) có ghi «~3 ngày» cho khoảng đọc→hỏi thì phải đổi về «2 ngày». Hiện caption b01/b06 ghi «Two days» → đạt.

## Bảng luật

| ID | Luật | Dòng | Kết quả | Ghi chú |
|---|---|---|---|---|
| L-088 (trend) | Có file trend Social Research có link, trend là cái móc ở hook | 12, 38, 47 | ĐẠT | brain stacking chỉ ở hình b01 (callback b04/b06), lời không nói trend giúp nhớ. trend-signals.md đã cập nhật ở ecb8614 |
| L-088 (fact) | Có file fact DR, mọi câu truy được F1–F5 | 56–66 | **CHƯA ĐẠT** | b03 thiếu nhóm so sánh ở vế cuối (lỗi B1) |
| L-088 (a) | Dẫn chứng lồng vào chuyện, một câu ngắn báo là nghiên cứu | 24, 26 | **CHƯA ĐẠT** | b03 đạt («Một nghiên cứu cũng thấy điều tương tự» nối với chuyện b02). b05 là khối nghiên cứu thứ hai đứng riêng, mở bằng «người ta thấy», không gắn vào buổi họp (lỗi B3) |
| L-088 (b) | Hook/CTA không rập khuôn, kiểu hook khác 2 clip trước | 22, 28 | ĐẠT | Hook mới là khoảnh khắc peak (sếp hỏi lại, đứng hình) + câu hỏi «sao». CTA chữ mới |
| L-088 (c) | Thông điệp bám motivation, sống tốt hơn mỗi ngày +1 | 27–28 | ĐẠT (yếu) | Nốt +1 «mỗi ngày một buổi ngắn» đúng mục Motivation của fact-package-v5. CTA mời làm một việc nhỏ. Câu +1 đang nhắc lại ý b04 (xem B2) |
| L-087 | Ví dụ đời thường, không môn học | 22–28, 38–44 | ĐẠT | Việc xuyên suốt là đọc tài liệu cho buổi họp. «làm bài kiểm tra» ở b03 là mô tả nghiên cứu, không phải ví dụ môn học |
| W-16 | hook → vấn đề + nguyên nhân có dẫn chứng → mục tiêu → giải pháp → kết quả → CTA | 22–28 | ĐẠT | b04 nói mục tiêu («để còn nhớ tới lúc sếp hỏi») trước cách làm trong cùng câu. b05 là bằng chứng cho cách làm, đặt trước kết quả, không phá thứ tự |
| P-05/P-06/L-057/L-058 | Nói thẳng nỗi đau với «bạn» + câu hỏi bám đúng nỗi đau, không kể lể, không «nếu giờ…» lửng | 22 | ĐẠT | Câu hỏi bám đúng mốc «hai hôm» và đúng «ý đó». Không có ngôi «mình» trong hook |
| rule-55 / L-021 | Vế đầu hook ≤6 chữ, không mở bằng câu dẫn trung tính | 22 | **CHƯA ĐẠT** | «Hôm họp bạn trình bày rất suôn sẻ» dài 8 chữ, và là vế dẫn tích cực. Nỗi đau tới chữ 16 (lỗi B4) |
| Ngân sách hook (skill craft) | Hook ≤ ~20 chữ | 22 | **CHƯA ĐẠT** | 29 chữ, «hai hôm» lặp 2 lần trong hook (B4) |
| W-14 / rule-7 | Tổng 140–175 chữ (mốc chữ mới nhất, L-075. L-080 chỉ bỏ ép giây, không bỏ ngân sách chữ) | 22–28 | **CHƯA ĐẠT** | 212 chữ, vượt 37 (B2). Xung đột X-01 vẫn còn, nhưng Hiệp đã ưu tiên «ngắn gọn» |
| P-01 / L-054 | Mỗi ý nói một lần, không lặp | 22, 25, 27 | **CHƯA ĐẠT** | «hai hôm» ×2 trong hook. «mỗi ngày một buổi ngắn, thay cho một tối dồn hết» (27) nói lại «chia ra ba ngày, mỗi ngày một tiếng» (25). «sếp hỏi» 3 lần (22, 25, 27): ở 22 và 27 là móc vòng có chủ đích, còn ở 25 là thừa (B2) |
| W-12 | Phần nghiên cứu ≤1 câu, ≤ ~25 chữ, chỉ nghiên cứu mạnh nhất | 24, 26 | **CHƯA ĐẠT** | b03 dài 46 chữ, 3 câu. Thêm b05 22 chữ là nghiên cứu thứ hai (B3) |
| P-03 | Không bịa số hay cơ chế, không hứa kết quả cụ thể | 24–27 | ĐẠT (trừ B1) | Không có %, không cơ chế não, không «đều thống nhất». Kết quả «dễ nhớ ra ý đó hơn» là minh hoạ, không hứa thuyết trình thành công |
| P-07 / L-053 | Không chê năng lực người học | toàn bộ | ĐẠT | Grep «dở/kém/nhớ kém/lười»: 0 |
| P-02 / L-055 | Không có câu an ủi chung chung đứng một mình | toàn bộ | ĐẠT | Không có câu kiểu đó |
| P-04 / L-022 | Không từ hiếm, văn chương hay mơ hồ | 22–28 | ĐẠT (ghi chú N3, N7) | suôn sẻ, đứng hình, trôi mất, úp, sót đều là từ thường. «điều tương tự» hơi chung (N3) |
| P-08 / L-052 | Mềm nhưng tập trung, văn nói, ví dụ đời thật cụ thể | 23, 25 | ĐẠT | Chi tiết làm được: ba tiếng, hai lần liền, úp tài liệu, tự nói lại, lật lên xem sót |
| W-09 | Câu đủ chủ ngữ | 22–28 | ĐẠT | Vế «Gộp 317 thí nghiệm lại» dùng chủ ngữ «người ta» của vế sau. Chấp nhận được, nhưng nếu bỏ b05 thì hết vấn đề |
| W-10 | Câu hỏi với người xem mềm | 28 | ĐẠT | Có «muốn thử» |
| W-14 / rule-64 | Một CTA, một câu hỏi, quay về cách làm | 28 | ĐẠT | Một câu hỏi + lời mời comment |
| rule-56 | Có comment-challenge + loop | 28 | ĐẠT một phần (N5) | Có challenge. Chữ ở CTA không lặp từ khoá hook (sẽ ⚠/✖ khi lên spec) |
| P-10 | Dòng an toàn + credit, không ghi tác giả bảo trợ | 32 | ĐẠT (N6) | Dòng an toàn nguyên văn. Credit đúng chuỗi bắt buộc. Có ghi chú không gợi ý bảo trợ |
| L-045 / L-053 | Ví dụ ngôi «mình» làm mẫu | 23 | ĐẠT (N1) | Xem N1 về góp ý của Deep Research |
| L-084 | Thấy trend ở b01–b02 + dòng «Trend trong clip» | 38, trend-signals 14 | ĐẠT | Chỉ có trong hình. Dòng ở trend-signals.md đã cập nhật (ecb8614) |
| L-086 | Người viết không tự kết luận đạt | 68, commit 84c4fcc | ĐẠT (N8) | Mục tự soát ghi rõ kết luận là của Rule Reviewer. Chữ «PASS» trong commit chỉ là output công cụ |
| P-09 | Caption EN ≤8 từ/chunk | 38–44 | ĐẠT | Chunk dài nhất 8 từ: «Second read a week later: still ahead» 7, «Each evening, flip the pages face down» 7 |

## Lỗi chặn (người viết sửa, Rule Reviewer chấm lại)

**B1. Dòng 24 (b03), vế cuối thiếu nhóm so sánh (fact lock F1, Deep Research cũng bắt được).**
Lời hiện tại: «Còn người đọc lần hai cách một tuần thì hai ngày sau vẫn hơn.» Nguồn chỉ so với nhóm **đọc một lần**. Để trống thì người nghe sẽ hiểu là «hơn người đọc liền».
Sửa: «…thì hai ngày sau vẫn hơn **người đọc một lần**.» Caption b03 cũng thêm «than one read».

**B2. Độ dài 212 chữ, vượt trần 175 (W-14), và có lặp ý (P-01).**
- Dòng 22: «hai hôm» lặp 2 lần («hai hôm sau sếp hỏi…», «Sao mới hai hôm…»).
- Dòng 27: câu thứ hai nói lại ý chia ngày của dòng 25. Giữ một chỗ thôi: hoặc dòng 25 bỏ «mỗi ngày một tiếng» (vì «ba tiếng chia ra ba ngày» đã đủ nghĩa F3), hoặc câu +1 ở dòng 27 nói việc nhỏ hôm nay thay vì nhắc lại cách chia.
- Dòng 25: bỏ «tới lúc sếp hỏi» (mốc này đã có ở hook và ở kết quả), chỉ giữ mục tiêu «để còn nhớ lâu».
- Cộng với B3 (bỏ hoặc rút b05, −22) và B4 (hook −5), tổng còn khoảng 175–180. Người viết chọn chỗ cắt, rồi đếm lại cho ≤175.

**B3. Dòng 26 (b05) là khối nghiên cứu thứ hai đứng riêng (L-088 (a), W-12, Deep Research «một câu báo nghiên cứu duy nhất»).**
«Gộp 317 thí nghiệm lại, người ta thấy…» không gắn vào chuyện buổi họp, và «người ta thấy» là một biến thể của «các nhà nghiên cứu thấy» trong danh sách tránh của L-088.
Sửa, chọn một trong hai:
(a) Bỏ b05 khỏi lời, giữ Cepeda 2006 ở hình hoặc caption góc và end card (F3 đã có «như cẩm nang gợi ý»).
(b) Nếu giữ, viết thành một bước trong chuyện, nối với việc chia ngày ở b04, không mở bằng «người ta thấy», và vẫn đúng F4 (không có số ngày, không «đều thống nhất»).

**B4. Dòng 22 (hook): vế đầu 8 chữ là câu dẫn tích cực, hook dài 29 chữ (rule-55 sẽ ✖ khi lên spec, theo L-046 phải báo ngay. Skill craft giới hạn hook ≤ ~20 chữ).**
Sửa: tách vế đầu ≤6 chữ để nỗi đau tới sớm hơn và bỏ «hai hôm» lần hai. Giữ nguyên ý, giữ mốc «hai hôm», giữ câu hỏi «sao». Ví dụ hướng sửa (không phải câu chốt): «Hôm họp, bạn trình bày trơn tru. Hai hôm sau sếp hỏi lại một ý, bạn đứng hình. Sao ý đó trôi nhanh vậy?»

## Ghi chú không chặn
- **N1, dòng 23, «Mình cũng từng vậy» (Deep Research góp ý đổi thành «Nhiều người làm thế này»).** Rule Reviewer **không xếp là lỗi chặn**. L-053 ghi rõ «Thầy tự nhận mình cũng từng vậy», L-045 yêu cầu ví dụ nói ngôi «mình» làm mẫu, luật 67/X-03 cho phép chi tiết chuyện minh hoạ mà không cần hỏi xác nhận. Người nói là nhân vật Thầy (clip-04 đã dùng ngôi «mình» y vậy). Đổi sang «Nhiều người…» thì mất ngôi «mình» làm mẫu. Nếu Hiệp không muốn lời ngụ ý là chuyện thật của anh, đó là quyết định của Hiệp. Khi trình Hiệp, ghi một dòng cho Hiệp chọn.
- **N2, «buổi» mang 3 nghĩa** (skill craft §3: một từ một nghĩa): «buổi họp» (23, 25), «một buổi ngắn» là buổi ôn (27), «buổi nào» là sự kiện sắp tới (28). Gợi ý: ở CTA nói rõ việc sắp tới (vd «buổi họp hay buổi thuyết trình nào»), hoặc đổi chữ ở 27.
- **N3, dòng 24, «điều tương tự»** hơi chung. Deep Research đã chọn «tương tự» chứ không «y hệt», nên giữ được. Nếu sửa B1/B2 thì có thể nói rõ là «tương tự chuyện đọc liền đó».
- **N4, hình b01/b06, «sếp (chibi)»:** đây là nhân vật mới, trong khi luật 43 chỉ cho rig Hiệp/Omi. FLUX/News nên thể hiện sếp bằng vật (tay cầm bút chỉ slide, bong bóng «?») hoặc hỏi Hiệp trước khi làm rig mới.
- **N5, rule-56:** CTA chưa lặp từ khoá hook (loop). Khi lên spec, cho câu cuối chạm lại «họp» hoặc «đứng hình». Không cần thêm chữ nếu N2 đổi thành «buổi họp…».
- **N6, P-10:** end card chưa có link giấy phép creativecommons.org/licenses/by/4.0 và chữ «đã chuyển thể». Giống tiền lệ v4, phần này nằm ở post.md (rule-13/53 kiểm khi `--final`).
- **N7, dòng 23, «đọc chồng tài liệu»:** nghe dễ vấp nghĩa «chồng». Gợi ý «đọc cả chồng tài liệu».
- **N8:** commit 84c4fcc ghi «--subjects + --l088 PASS». Đó chỉ là output công cụ. Kết luận đạt/chưa đạt là file này (L-086).
- **N9:** trend-signals.md đã được Social Research cập nhật ở ecb8614 (brain stacking thay @ng__phanh). Yêu cầu ở dòng 48 của bản nháp đã xong.

## Bước tiếp
OpenCreator sửa B1–B4, đăng xin duyệt trong group (L-086). Rule Reviewer chạy lại --subjects/--l088, đếm chữ, chấm lại. Chưa Chốt thì không làm giọng hay render (L-072).
