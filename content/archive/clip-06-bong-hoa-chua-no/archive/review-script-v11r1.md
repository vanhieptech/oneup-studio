---
id: clip-06.review
type: review
title: "clip-06 — review độc lập script v11 vòng 1 (Gate 1, pairwise vs a-c05)"
date: 2026-11-27
tags: [review, clip-06, gate-1, two-tier, pairwise, v11, round-1]
status: draft
source: "docs/prompts/reviewer-script.md (Pairwise A/B, 7 điểm mù, CẤM chấm đạt mạch vì từ nối) · draft content/clips/clip-06-bong-hoa-chua-no/final/script-v11-draft.md (7 beat b01–b07) · anchor content/archive/clip-05-hoc-mot-dem/final/script-final.md (a-c05) · fact-lock research/fact-packages/factcheck-trends-2026-10-31.md mục «clip-06, 4.12 (Lally 2010, mức B)» + bảng Fact-lock trong draft · resources/feedback.md · content/voice-profile.md §2–3 · final/feedback.md (9 dòng) · archive/review-script-v10.md (chỉ để biết lịch sử; chấm lại từ đầu, không lặp lỗi khen keo từ nối)"
verdict: CẦN SỬA
pairwise: LOSE
anchor: a-c05
anchor_match: "cùng kênh @hi.oneup, giọng miền Nam, một bằng chứng nghiên cứu + CTA hỏi người xem"
script_hash: 2996643f6fee
feedback_seen: 9
reviewer_model: claude-opus-5-5
---
# clip-06 v11 — review độc lập vòng 1 (2 tầng)

Chấm từ đầu trên lời đọc hiện tại (hash 2996643f6fee). Kết quả: không Hard Fail, độ dài và ngân sách nhồi nhét đều đạt (b01 15, b01+b02 50, beat dài nhất 42, tổng 219 âm tiết). v11 đã bỏ thật keo từ nối đầu beat, đây là tiến bộ đúng hướng so với v10. Nhưng khi đọc bỏ từ nối để soi quan hệ ý giữa từng cặp câu, vẫn còn ba chỗ hở: (1) b05 dùng «nghỉ ngang», một cụm trong tiếng Việt nghĩa là bỏ giữa chừng, đặt trong clip có thông điệp là đừng bỏ; (2) b02 cho cùng một thói quen hai tuần vừa là «mới gieo hạt» vừa là «cái nụ», hai giai đoạn cây không thể cùng lúc; (3) b05→b06 rẽ sang chuyện nghỉ một bữa rồi mới quay lại «tính bằng tháng» (ý của b04), nên câu đầu b06 không nảy ra từ câu cuối b05. Lỗi (1) là một lỗi sai nghĩa rõ, nên theo điểm mù 5 bắt buộc chấm **LOSE / CẦN SỬA**. Cả ba đều sửa được ngay trên khung hiện tại, không cần viết lại.

## Đếm âm tiết thật (đọc thành lời)

Quy ước: «2010» = «hai nghìn không trăm mười» (5; đọc «hai ngàn lẻ mười» thì 4), «18» = «mười tám» (2), «254» = «hai trăm năm mươi tư» (5), «8» = «tám» (1), «Phillippa Lally» đọc «Phi-líp-pa La-li» (5). `audio-precheck.py` ra 207 vì đếm mỗi con số và mỗi tên riêng thành 1 âm tiết; chênh nhau đúng ở b04 (30 so với 42).

| Beat | Âm tiết | Trần | Kết quả |
|---|---:|---:|---|
| b01 | 15 | ≤ 20 (Clarity ≤ 22) | đạt |
| b02 | 35 (15 + 12 + 8) | ≤ 45 | đạt |
| b01 + b02 | 50 | ≤ 65 | đạt |
| b03 | 17 (11 + 6) | ≤ 45 | đạt |
| b04 | 42 (toàn bộ là lời bằng chứng) | ≤ 45; lời bằng chứng nên ≤ 35, «dài dòng» > 40 | trong trần beat. Lời Lally 42 (41 nếu đọc «hai ngàn lẻ mười») là vượt mốc 40 nhưng không có cỡ mẫu, số tuần hay món phụ, nên chưa tính là dính điểm mù 6. Nên gọn lại (fix 4) |
| b05 | 38 (17 + 14 + 7) | ≤ 45 | đạt |
| b06 | 33 (11 + 9 + 6 + 7) | ≤ 45 | đạt |
| b07 | 39 (12 + 9 + 12 + 6) | ≤ 45 | đạt |
| **Tổng** | **219** | ~210–255 | ≈ 68–76s lời (2,9–3,2 âm tiết/s) + end card ≈ 71–79s |

## Tầng 1 — Hard Fail (H1–H4)

Không có lỗi.

- **H1:** lời bằng chứng có tên + năm («Năm 2010, nhóm Phillippa Lally»). Không chạm danh sách Cấm: không «66 ngày», không «trung bình», không «hơn hai tháng», không «12 tuần», không cơ chế não, không gán số ngày cho chạy bộ, không nới sang việc phức tạp (chạy bộ nằm trong nhóm «vận động đơn giản» có đo).
  - «hơn 8 tháng» = 254 ÷ 30,4 ≈ 8,4 tháng: quy đổi số học đúng.
  - «Giữ một việc cả mấy tháng trời thì kiểu gì cũng có hôm nghỉ…» là suy luận của người nói và đã được ghi rõ như vậy trong bảng Fact-lock. Câu này không gán cho nghiên cứu và không nêu số nào mới.
  - «lỡ nghỉ một ngày gần như hông ảnh hưởng gì» khớp fact package («lỡ một ngày không làm hỏng tiến trình») và có rào «gần như». Vế «công mấy bữa trước vẫn còn nguyên» nói chắc hơn nguồn một chút (vì «còn nguyên» là tuyệt đối), nhưng không chạm Cấm và vẫn là cách nói đời thường của cùng ý. Không phải H1, chỉ nên mềm lại (fix 3).
  - «Thói quen thì tính bằng tháng» là tựa mục cẩm nang 4.12, được nói như lời khuyên, không gán cho nghiên cứu.
- **H2:** ≈ 71–79s, rất xa 300s.
- **H3:** comic + motion; không quay mặt, b-roll, nhạc nền hay nhắc lịch đăng; không chê người xem.
- **H4:** 7 dòng `N. **[bNN]**`, không beat trống.

## Phép thử bỏ từ nối: soi từng cặp câu liền kề

Đọc bỏ hết chữ đầu câu và hỏi ở mỗi cặp: câu sau có nảy ra từ hình ảnh hoặc hệ quả của câu trước không.

| Cặp | Quan hệ ý thật | Đánh giá |
|---|---|---|
| b01 → b02 | «hai tuần vẫn oải → chắc không hợp» rồi «hai tuần mà mình đòi quen liền». Người nói tự bắt lỗi kỳ vọng của mình, chữ «hai tuần» lặp làm điểm neo. | **Nối được.** Đây là cú tự giễu thật, không cần chữ «Tại». |
| trong b02 (câu 1 → câu 2) | «mới gieo hạt đã đòi ra hoa» → «đừng khinh thường bông hoa chưa nở». Chữ «hoa» kéo câu trend vào, không còn câu meta «dạo này có câu trend nói». | **Nối được về chữ, nhưng lệch hình.** Xem điểm mù 5: hạt mới gieo và nụ là hai giai đoạn khác nhau. Chữ «Đúng là» còn là keo nhẹ: nó «đồng ý» với một câu chưa ai nói ra trước đó. |
| trong b02 (câu 2 → câu 3) | «bông hoa chưa nở» → «thói quen mới cũng là cái nụ thôi». Câu này gán hoa = thói quen. | **Nối được.** Nhưng thứ người nói «khinh thường» ở b01 là chính mình («mình không hợp»), không phải thói quen. Cách gán chấp nhận được, chỉ hơi chệch. |
| b02 → b03 | «cái nụ» → «Một việc mới phải mất bao lâu mới thành thói quen?». Bảng khung mạch ghi cầu nối là «vậy nụ này bao lâu mới nở?», nhưng lời đọc không giữ hình nụ mà bật sang câu hỏi văn xuôi. | **Hở nhẹ.** Nghe như bật Q&A. Người nghe vẫn hiểu vì đây là câu hỏi trung tâm, nhưng đổi giọng đột ngột từ ẩn dụ sang hỏi kiểu thuyết trình. |
| b03 câu 1 → câu 2 | «bao lâu?» → «Có người đo hẳn hoi rồi.» | **Nối tốt.** Tự nhiên, đúng giọng. |
| b03 → b04 | «Có người đo» → «Năm 2010, nhóm Phillippa Lally…». Câu sau triển khai đúng chữ «người đo». | **Nối tốt.** |
| trong b04 | «18 ngày mới thành nếp, chậm nhất tới 254 ngày, hơn 8 tháng». Vị ngữ «mới thành nếp» có ở vế 18, vế 254 hiểu ngầm. «Hơn 8 tháng» chỉ nói một lần, không lặp số. | **Rõ.** Có điều 18 ngày không được nối về «hai tuần» của hook (xem trục 4). |
| b04 → b05 | «hơn 8 tháng» → «Giữ một việc cả mấy tháng trời thì kiểu gì cũng có hôm nghỉ…». Câu sau tự rút từ con số. | **Nối được về ý.** Hỏng ở chữ: «nghỉ ngang» (điểm mù 5). |
| trong b05 | «kiểu gì cũng có hôm nghỉ» → «Nhóm đó cũng thấy lỡ nghỉ một ngày gần như hông ảnh hưởng gì». | **Nối tốt.** Đúng kiểu nỗi sợ → dữ kiện gỡ. |
| b05 → b06 | «công mấy bữa trước vẫn còn nguyên» → «Thói quen thì tính bằng tháng chứ hông tính bằng tuần». Câu sau không nảy ra từ câu trước. Ý «tính bằng tháng» là hệ quả của b04 («hơn 8 tháng»), bị b05 chen vào giữa. | **Hở rõ.** Đây đúng kiểu «câu kế tiếp không liên quan» mà Hiệp chê ở dòng 9. Thứ tự tự nhiên là: hơn 8 tháng → vậy thói quen tính bằng tháng → mấy tháng thì kiểu gì cũng có bữa nghỉ → nghỉ một bữa không mất công → tối nay chạy nhẹ, nghỉ thì mai chạy tiếp. |
| trong b06 | «tính bằng tháng» → «Tối nay xỏ giày chạy nhẹ mười phút thôi, mệt thì đi bộ một vòng, nghỉ bữa nào thì mai chạy tiếp». Không có nửa câu nói vì sao «tính bằng tháng» dẫn tới «chạy nhẹ mười phút» (vì đường dài nên đi nhẹ cho bền). Ba lệnh được hàn bằng dấu phẩy, đọc như checklist. Vế thứ ba nhắc chuyện nghỉ lần thứ ba trong khoảng 20 giây. | **Hở nhẹ.** |
| b06 → b07 | «mai chạy tiếp» → «Mới hai tuần thì chưa tới lúc chê mình không hợp đâu». Quay về đúng chữ của hook. | **Nối được** (khép vòng). |
| b07 → CTA | «bông hoa của mình mới là cái nụ» → «Việc gì bạn mới làm chừng hai tuần mà đang tính bỏ?». | **Nối tốt.** «Hai tuần» và «bỏ» bám hook. |

Kết luận phép thử: v11 không còn dán keo từ nối (0 beat mở bằng `Tại / Mà / Vậy / Nghĩa là / Nên / Còn… thì sao`, không câu meta). Đa số cặp câu có quan hệ ý thật. Còn một cặp hở rõ (b05→b06) và hai cặp hở nhẹ (b02→b03, trong b06). Không được chấm mạch là liền chỉ vì đã bỏ được từ nối.

## Tầng 2 — So sánh 4 trục (v11 vs a-c05)

1. **Hook & Giữ chân: Draft thắng.** Draft: «Chạy bộ được hai tuần mà vẫn oải, mình nghĩ: “chắc mình không hợp rồi.”» (15 âm tiết; người lạ nghe 3 giây hiểu ngay chuyện «mới tập mà oải» của mình, câu nội tâm cho thấy cái giá là sắp bỏ). Anchor: «Thì cái bản chất của cái việc đọc đâu nhớ đó là như thế nào?» phải chờ b01b «quên sạch trơn hà» thì mới ra nỗi đau.
2. **Mạch truyện & Chuyển ý: Anchor thắng.** Draft có xương sống đúng (oải → kỳ vọng sai → câu hỏi → Lally → hệ quả → cách làm → khép vòng) và đã bỏ keo từ nối. Nhưng b05 chen nỗi sợ «nghỉ một bữa» vào giữa con số và thước đo «tính bằng tháng», nên b06 mở bằng một câu không nối với câu cuối b05. Ẩn dụ ở b02 đổi giai đoạn (hạt → nụ) ngay trong hai câu liền kề. Anchor: «Đọc lại thì chữ nằm sẵn trên trang» → «Mà chuyện này có thí nghiệm hẳn hoi» → «Vậy hóa ra, thứ đáng tập là tự nhớ khi sách đóng»: mỗi câu là hệ quả của câu trước, không có chỗ quay lui.
3. **Văn nói tự nhiên VN + DNA kênh: Anchor thắng.** Draft có nhiều câu nói thật («Có người đo hẳn hoi rồi», «mấy tháng trời», «công mấy bữa trước vẫn còn nguyên», «xỏ giày»), giọng Nam đều («hông», «nha»), không có «ấy / thế / nhé». Nhưng có một lỗi sai nghĩa rõ («nghỉ ngang một bữa») và vài cụm hơi văn dịch hoặc lệch chủ ngữ: «Giữ một việc», «có hôm … một bữa», «đòi ra hoa», «Nhắn mình một chữ». Gia vị chỉ có câu nội tâm b01 và cú tự giễu «đòi quen liền». Mộc thì không bị trừ, nhưng lỗi nghĩa thì có. Anchor: «hông ai ghi sổ đầu bài đâu», đoạn nhại cô giáo, câu nào cũng là câu miệng.
4. **Độ đắt của ẩn dụ / payoff: Anchor thắng nhẹ.** Draft khép vòng đúng («chưa tới lúc chê mình không hợp đâu, bông hoa của mình mới là cái nụ thôi»), dịch 254 ngày thành «hơn 8 tháng», có một đổi thước đo và một hành động tối nay. Nhưng: (a) ẩn dụ không thống nhất giai đoạn: b02 «mới gieo hạt» rồi «cái nụ», b07 lại «cái nụ»; (b) con số 18 ngày, vốn là chỗ trả lời trực tiếp nỗi lo hai tuần (người nhanh nhất cũng mất 18 ngày, tức hơn hai tuần), bị thả xuống mà không nối về «hai tuần». Người nghe phải tự làm phép trừ, và tới tận b07 (khoảng 25 giây sau) mới nghe kết luận «chưa tới lúc chê mình không hợp». Anchor: «Đọc đâu nhớ đó là tự trả bài vậy đó» chốt gọn một hình xuyên suốt.

## Kiểm 7 điểm mù

- **Điểm mù 1 (hook phình / trì hoãn):** không. b01 một câu; câu hỏi trung tâm tới ở giây khoảng 17, câu trend không lặp lại ý b01.
- **Điểm mù 2 (rẽ nhánh):** nhẹ, không tính là dính. b05 là hệ quả rút từ con số, không phải phát hiện thứ hai tách rời. Lỗi nằm ở **vị trí** của nó (chen trước thước đo «tính bằng tháng»), đã tính ở trục 2.
- **Điểm mù 3 (văn dịch / sách vở):** không có cụm nào trong danh sách cấm. «Giữ một việc» hơi giống dịch từ «keep a habit» (xem điểm mù 5).
- **Điểm mù 4 (ví dụ lạc / dẫn chứng rỗng / đổi ngôi):** không. Chạy bộ xuyên suốt b01–b06, bằng chứng có tên + năm, chỉ đổi sang «bạn» ở CTA như bình thường.
- **Điểm mù 5 (sai nghĩa / văn dịch / mâu thuẫn): DÍNH.**
  1. **b05 «kiểu gì cũng có hôm nghỉ ngang một bữa»: sai nghĩa (lỗi rõ).** Người Việt dùng «nghỉ ngang» để nói bỏ giữa chừng, nghỉ luôn không báo trước («nghỉ ngang đại học», «nhân viên nghỉ ngang»), không ai dùng nó cho nghĩa «nghỉ một ngày». Ghép với «một bữa» thì câu thành ra hai nghĩa đá nhau, và nghĩa đầu tiên người nghe bắt được lại là đúng điều clip khuyên đừng làm (bỏ ngang). Thêm nữa, «có hôm … một bữa» dùng hai đơn vị ngày chồng lên nhau. Nói tự nhiên: «kiểu gì cũng có bữa phải nghỉ» hoặc «kiểu gì cũng có bữa bỏ một buổi».
  2. **b02 «mới gieo hạt đã đòi ra hoa» → «thói quen mới cũng là cái nụ thôi»: ẩn dụ đổi giai đoạn trong hai câu liền kề.** Hạt mới gieo thì chưa có cây; nụ là lúc cây đã lớn, sắp nở. Cùng một thói quen hai tuần không thể vừa là hạt vừa là nụ. Nụ còn gợi ý «sắp nở tới nơi», đá với «chậm nhất tới hơn 8 tháng» ở b04. Lỗi này không nặng bằng (1) nhưng đúng loại «ẩn dụ sai vật lý» trong điểm mù 5. Cách sửa: bỏ hình gieo hạt, giữ một hình nụ duy nhất, ví dụ «Hai tuần mà mình đòi quen liền, như cái nụ mới nhú đã đòi nó nở.»
  3. **b02 «đã đòi ra hoa»: lệch chủ ngữ (nhẹ).** «Đòi + động từ» thường là chủ ngữ tự làm việc đó («đòi ăn», «đòi đi»), nên «mình đòi ra hoa» nghe như chính mình ra hoa. Nói tự nhiên: «đã đòi có hoa» hoặc «đã đòi nó nở». Câu tục ngữ quen là «mới trồng cây đã đòi ăn quả».
  4. **b05 «Giữ một việc cả mấy tháng trời»: hơi văn dịch (nhẹ).** «Giữ» đi với «thói quen», «nhịp», không đi với «việc». Nói tự nhiên: «Làm một việc liền mấy tháng trời».
  5. **b07 «Nhắn mình một chữ thôi nha»: lệch kênh (nhẹ).** Trên TikTok, «nhắn» là nhắn tin riêng, trong khi CTA muốn comment. Anchor dùng «comment cho mình biết với nha».
  - Mốc thời gian không mâu thuẫn: «hai tuần» khớp nhau ở b01, b02, b07; 18 và 254 chỉ ở b04, không áp vào chạy bộ.
  - Các cụm caller yêu cầu soi mà **đạt**: «đòi quen liền» (đúng: «mới hai tuần mà đòi quen liền» là câu miệng tự nhiên), «lỡ nghỉ» (đúng, tự nhiên), «chê mình không hợp» (chấp nhận được trong khẩu ngữ, nghĩa là «tự kết luận mình không hợp»).
- **Điểm mù 6 (mù mờ / lòng vòng / nhồi):** không dính.
  1. Clarity: b01 15 ≤ 20, đạt.
  2. Time-to-Point: b01+b02 50 ≤ 65, câu hỏi tới ở b03 nhưng b02 đã vào thẳng vấn đề (kỳ vọng hai tuần), đạt.
  3. One-Point: một câu hỏi, một ví dụ, không beat nào > 45. Lời Lally 42 vượt mốc 40 của phép thử nhưng không có cỡ mẫu, số tuần hay món phụ, nên ghi là sát ngưỡng chứ chưa nhồi (fix 4).
  4. Plausibility: không có cảnh «lướt trúng trend» hay hành động phi thực tế. Câu trend được kéo vào bằng chữ «hoa», đạt.
- **Điểm mù 7 (cụt ý / ngắt quãng / keo từ nối):**
  1. 219 âm tiết, nỗi lo «không hợp» được khép lại ở b07, đạt.
  2. Trend có hình dẫn («đòi ra hoa»), Lally có câu dẫn («Có người đo hẳn hoi rồi»), đạt.
  3. 254 ngày được dịch «hơn 8 tháng», đạt. 18 ngày chưa được nối về «hai tuần» (fix 2), hụt nhẹ chứ chưa bỏ rơi.
  4. Có đổi thước đo + một hành động + khép vòng, đạt.
  5. Keo từ nối: không còn beat nào mở rập khuôn, không câu meta, đạt. Nhưng bỏ keo mà một chỗ không thay bằng ý (b05→b06), đã tính ở trục 2.

**Chốt:** v11 sửa đúng hướng góp ý dòng 9 (bỏ keo từ nối, câu trend hòa vào hình ảnh) mà không quay lại lỗi nhồi (v8) hay cụt (v9). Nhưng còn một lỗi sai nghĩa rõ («nghỉ ngang»), một ẩn dụ đổi giai đoạn (hạt → nụ) và một chỗ quay lui mạch (b05→b06). Đặt cạnh a-c05, Hiệp nhiều khả năng vẫn thấy hai chỗ này «không liền mạch». Chấm **LOSE**. Sửa ba chỗ này trên chính khung v11 thì có thể lên TIE.

## Trả lời 9 dòng feedback (final/feedback.md)

1. «Script vẫn xàm thiếu tự nhiên, cả ai nói lý do nghe mới quê…» (v3): không còn câu rào hay khoe kiểu «lý do nghe mới quê», lời là câu miệng đời thường. Đã xử lý. Riêng b06 vẫn hàn ba lệnh bằng dấu phẩy (fix 3).
2. «Các câu văn vẫn rời rạc… không có cấu trúc tuần tự» (v3 r2): có bảng khung mạch 7 beat và đoạn liền mạch viết trước. Còn một chỗ quay lui: b05 chen trước thước đo «tính bằng tháng» (fix 1). Xử lý gần đủ.
3. «làm lại» (v3 r3): v11 viết trên khung ONEUP-CORE-ARC, không vá khung cũ. Đã xử lý.
4. «Sửa và chấm lại» (v4): review này là vòng chấm độc lập cho bản hiện tại. Đã xử lý.
5. «rời rạc, hook không liên quan, nghe xong mù mờ» (v6): hook và bằng chứng cùng một câu hỏi (hai tuần oải → bao lâu thành thói quen → 18 ngày tới hơn 8 tháng). Đã xử lý. Nên nối 18 ngày về hai tuần cho trọn (fix 2).
6. «câu văn không đúng ngữ nghĩa tiếng Việt…» (v7): **chưa xử lý hết.** «Nghỉ ngang một bữa» là cụm sai nghĩa; «đòi ra hoa», «Giữ một việc», «Nhắn mình một chữ» là cụm lệch nhẹ (fix 1, 3, 5).
7. «hook… không rõ nghĩa, lòng vòng, nhồi nhét quá nhiều thứ, không tự nhiên» (v8): b01 15, b01+b02 50, một câu hỏi, một ví dụ, lời Lally không có cỡ mẫu, số tuần hay món ăn. Đã xử lý. Lời Lally 42 âm tiết nên gọn lại (fix 4).
8. «…kết thúc giữa chừng, chưa đủ ý… ngắt quãng… thiếu liền mạch» (v9): đủ ý, khép vòng về «không hợp» và nụ hoa, 219 âm tiết (khoảng 75s). Đã xử lý.
9. «kết nối các câu từ vẫn không có liền mạch, quá rập khuôn khi thêm các từ nối câu…» (v10): **xử lý một phần.** Phần rập khuôn từ nối đã hết: không beat nào mở bằng `Tại / Mà / Vậy / Nghĩa là / Nên / Còn… thì sao`, không câu meta, câu trend kéo vào bằng chữ «hoa». Phần «câu kế tiếp phải liên quan» thì còn hở ở b05→b06 (câu b06 không nảy ra từ b05), b02→b03 (bật câu hỏi văn xuôi, bỏ hình nụ) và trong b02 (hạt → nụ). Chưa đạt.

## Khối kết luận

HARD_FAILS: không
PAIRWISE: LOSE (so với a-c05)
TOP_FIXES: 1. b05 + thứ tự b05/b06: «nghỉ ngang một bữa» sai nghĩa (nghỉ ngang = bỏ giữa chừng) → «kiểu gì cũng có bữa phải nghỉ»; đồng thời đưa «Thói quen thì tính bằng tháng chứ hông tính bằng tuần» lên ngay sau con số b04, rồi mới tới «Làm một việc liền mấy tháng trời thì kiểu gì cũng có bữa phải nghỉ. Nhóm đó cũng thấy lỡ nghỉ một ngày gần như hông ảnh hưởng gì…», để mỗi câu nảy ra từ câu trước (hơn 8 tháng → tính bằng tháng → mấy tháng thì có bữa nghỉ → nghỉ không mất công → tối nay); 2. b02 + b04: giữ một hình ẩn dụ duy nhất (nụ), bỏ «mới gieo hạt đã đòi ra hoa» (vừa đổi giai đoạn hạt → nụ vừa lệch chủ ngữ «đòi ra hoa»), vd «Hai tuần mà mình đòi quen liền, như cái nụ mới nhú đã đòi nó nở.»; và nối 18 ngày về hook bằng nửa câu, vd «…nhanh nhất cũng mười tám ngày mới thành nếp, tức là hơn hai tuần rồi…», để b02→b03 cũng có thể hỏi bằng chính hình nụ («Cái nụ như vậy bao lâu mới nở?» rồi mới vào câu hỏi thói quen, không mở bằng «Mà») thay vì bật Q&A; 3. b06: thêm nửa câu vì sao chạy nhẹ (vd «đường dài thì chạy nhẹ cho bền»), bỏ vế «nghỉ bữa nào thì mai chạy tiếp» nếu b05 đã nói chuyện nghỉ (đang là lần thứ ba trong 20 giây), và mềm vế «công mấy bữa trước vẫn còn nguyên» thành «công mấy bữa trước vẫn còn đó» cho khớp rào «gần như»; 4. b04: lời Lally 42 âm tiết, gọn về ≤ 35, vd bỏ «người ta» và gộp «theo dõi … làm một việc nhỏ mỗi ngày» thành «đo một việc nhỏ làm mỗi ngày»; 5. b07: «Nhắn mình một chữ thôi nha» → «Comment một chữ cho mình biết nha» (nhắn = tin riêng); «Mới hai tuần thì … mới là cái nụ» có hai chữ «mới», đổi thành «bông hoa của mình còn là cái nụ thôi».
CONFLICTS: không
VERDICT: CẦN SỬA
