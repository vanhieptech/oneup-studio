---
id: clip-06.review
type: review
title: "Review độc lập clip-06 v13 r5 — Pairwise A/B vs a-c05 (make-video §4b)"
date: 2026-11-27
updated: 2026-11-27
tags: [review, clip-06, gate-1, pairwise, two-tier, dl-081]
status: draft
source: "docs/prompts/reviewer-script.md (make-video §4b, reviewer độc lập)"
verdict: ĐẠT
pairwise: TIE
anchor: a-c05
anchor_match: "cùng kênh @hi.oneup, giọng miền Nam, một bằng chứng nghiên cứu + CTA hỏi người xem"
script_hash: c8469062ec2f
feedback_seen: 13
reviewer_model: gemini-3.1-pro
---
# Review độc lập `clip-06` (`script-v13-draft.md` · `c8469062ec2f`) vs Anchor `a-c05`

## Bảng đếm âm tiết thực tế từng beat (`b01–b08`)

| Beat | Số câu | Token chữ viết | Âm tiết đọc thực tế | Ghi chú quy đổi số / từ mượn & ngưỡng kiểm |
|---|---:|---:|---:|---|
| `b01` | 1 | 19 | **19** | Không có chữ số/từ mượn · **Đạt** (`≤ 20` âm tiết mục tiêu, `≤ 22` trần cứng; rõ nghĩa ngay 3–6s đầu) |
| `b02` | 2 | 32 | **32** | Không có chữ số/từ mượn · Cộng dồn `b01 + b02` = **51** âm tiết (**Đạt** `≤ 65`) |
| `b03` | 3 | 41 | **41** | Không có chữ số/từ mượn · **Đạt** (`≤ 45`) |
| `b04` | 1 | 34 | **44** (41 nếu đọc gọn) | `2010` = *hai ngàn không trăm mười* (5, hoặc *hai ngàn mười* = 3); `Lally` = *La-li* (2); `18` = *mười tám* (2); `254` = *hai trăm năm mươi tư* (5, hoặc *hai trăm năm tư* = 4); `8` = *tám* (1) · **Đạt** (`≤ 45`; riêng phần thông số kết quả = 27 âm tiết đọc, đã lược bỏ cỡ mẫu/số tuần/món phụ) |
| `b05` | 2 | 33 | **33** | Không có chữ số/từ mượn · **Đạt** (`≤ 45`) |
| `b06` | 2 | 43 | **43** | Không có chữ số/từ mượn · **Đạt** (`≤ 45`) |
| `b07` | 1 | 26 | **26** | `mười phút` đã viết sẵn thành chữ · **Đạt** (`≤ 45`) |
| `b08` | 3 | 43 | **44** | `comment` đọc *còm-men* (2 âm tiết, 1 từ tiếng Anh tự nhiên duy nhất toàn bài); 3 câu gọn (14 + 12 + 17 chữ, không câu nào > 25 chữ) · **Đạt** (`≤ 45`) |
| **Tổng** | **15** | **271** | **282** (279 nếu đọc gọn) | Ước thời lượng đọc tự nhiên (~2.9–3.2 âm tiết/s): ~88–97s lời + ~6–8s nghỉ/chuyển cảnh/end card ≈ **94–105s** (nằm gọn trong mục tiêu 60–180s của kênh, << trần cứng 300s) |

---

## Tầng 1 — Hard Fail (H1–H4)

- **H1 (Fact không nguồn / nói quá / chạm danh sách Cấm của `fact_lock`):** **Không.**
  - Đối chiếu trực tiếp từng câu của bản nháp với `research/fact-packages/factcheck-trends-2026-10-31.md` (mục `clip-06, 4.12 (Lally 2010, mức B)`) và `## Bảng Fact-lock` trong bản nháp:
    - `b04` nêu rõ năm (`2010`), tên tác giả (`nhóm Lally`, màn hình `PHILLIPPA LALLY (2010)`), đúng phạm vi `làm việc nhỏ mỗi ngày` (không nới sang việc phức tạp, không gán chạy bộ thành kết quả đo của nghiên cứu), đúng khoảng `18 ngày` → `254 ngày` và quy đổi số học chuẩn `hơn 8 tháng` (254 ÷ 30 ≈ 8,47 tháng).
    - Không chạm bất kỳ mục nào trong danh sách **Cấm**: không có «66 ngày», không số ngày cố định làm kết luận, không «trung bình», không «hơn hai tháng», không «12 tuần», không bịa cơ chế não («não chưa quen nhịp»), không nói «nhiều nghiên cứu» hay «chứng minh».
    - `b05` («Nhanh nhất người ta còn mất hơn hai tuần, mình mới chạy hai tuần mà oải là quá bình thường — đâu phải không hợp») khớp số học `18 ngày > 14 ngày` và khớp cẩm nang 4.12 («Hai ba tuần vẫn chưa thấy nhẹ là bình thường»).
    - `b06` giữ đúng chủ ngữ «nhóm đó» (1 nghiên cứu) và từ rào «nghỉ một ngày **gần như** hông sao», khớp nguồn Lally 2010 & cẩm nang 4.12 («lỡ một ngày không làm hỏng tiến trình»).
    - `b07` («chạy nhẹ mười phút, mệt thì đi bộ») là ví dụ hành động tối nay của người kể, tách bạch với số liệu nghiên cứu và khai báo minh bạch ở `## Chi tiết đã dựng` theo `rule-67`.
- **H2 (Thời lượng ≥ 300s, `L-099`):** **Không.** Tổng 282 âm tiết đọc thực tế (~94–105s tính cả nghỉ và end card), thấp hơn rất xa ngưỡng chặn 300s.
- **H3 (Sai format kênh / xúc phạm người xem):** **Không.** 100% comic + motion (`DL-027`), không đòi quay mặt/b-roll tự quay, không nhạc nền, không nhắc lịch đăng (`DL-028`), không có cụm chê năng lực người xem (`L-053`).
- **H4 (Lỗi cấu trúc):** **Không.** Mục `## Lời đọc (checker input)` chia đủ 8 beat `1. **[b01]**` → `8. **[b08]**`, không có beat trống, khớp nguyên văn từng chữ với bảng `Pha 2`, `Pha 1` và đoạn `Đọc liền một mạch`.

---

## Tầng 2 — Given–New Conceptual Flow & Anti-Anadiplosis Check

### 1. Kiểm từng cặp câu liên tiếp (`b01` → `b08`, 15 câu / 14 điểm nối)

1. **`b01` → `b02` (câu 1):** *«…mà tập thói quen hai tuần đã muốn dẹp.»* → *«Đợt mới tập chạy bộ hai tuần vẫn oải, mình liền nghĩ “chắc mình hông hợp đâu”.»*
   - **Mạch *Given → New*:** Hạ thẳng từ nghịch lý chung xuống trải nghiệm cụ thể của `mình` («tập chạy bộ hai tuần vẫn oải → nghĩ hông hợp»). Không điệp từ cuối–đầu. **Đạt.**
2. **`b02` (câu 1) → `b02` (câu 2):** *«…mình liền nghĩ “chắc mình hông hợp đâu”.»* → *«Lúc đó quên mất câu “đừng bao giờ khinh thường một bông hoa chưa nở”.»*
   - **Mạch *Given → New*:** Từ tiếng nói nội tâm nản lòng ở tuần thứ 2 (`Lúc đó`), người kể sực nhớ câu trend nhờ đã gieo sẵn hình ảnh «trồng cây đợi mấy tháng» ở `b01` — không nhảy cóc, không dùng câu meta. **Đạt.**
3. **`b02` (câu 2) → `b03` (câu 1):** *«…“đừng bao giờ khinh thường một bông hoa chưa nở”.»* → *«Chạy có hai tuần thì mới nhú cái nụ hà, sao đòi nhẹ tênh liền được.»*
   - **Mạch *Given → New*:** Khai triển trực tiếp «bông hoa chưa nở» thành «mới nhú cái nụ» chiếu lên 2 tuần chạy bộ, đối lập tự nhiên với «vẫn oải» bằng khẩu ngữ miền Nam «nhẹ tênh». **Đạt.**
4. **`b03` (câu 1) → `b03` (câu 2):** *«…sao đòi nhẹ tênh liền được.»* → *«Ủa mà tập một việc mất bao lâu mới thành thói quen?»*
   - **Mạch *Given → New*:** Nhận ra 2 tuần chưa thể nhẹ tênh liền bật ra câu hỏi trung tâm duy nhất của cả bài. Tiểu từ «Ủa mà» tự nhiên, dùng đúng 1 lần toàn bài. **Đạt.**
5. **`b03` (câu 2) → `b03` (câu 3):** *«Ủa mà tập một việc mất bao lâu mới thành thói quen?»* → *«Hồi trước mình cứ đinh ninh ráng hai ba tuần là vô guồng.»*
   - **Mạch *Given → New*:** Hỏi xong tự thú ngay kỳ vọng sai trước đây của chính mình («đinh ninh ráng hai ba tuần là vô guồng»), dựng bệ phóng tâm lý cho cú lật số liệu. **Đạt.**
6. **`b03` (câu 3) → `b04`:** *«Hồi trước mình cứ đinh ninh ráng hai ba tuần là vô guồng.»* → *«Đọc nghiên cứu năm 2010 của nhóm Lally mới ngửa người ra: làm việc nhỏ mỗi ngày, người nhanh nhất mất 18 ngày, chậm nhất tới 254 ngày — hơn 8 tháng mới thành nếp.»*
   - **Mạch *Given → New*:** Kỳ vọng sai «đinh ninh hai ba tuần» va thẳng vào cú tỉnh ngộ «mới ngửa người ra» khi đọc Lally 2010 (*Storytelling the Study*), không vào kiểu Wikipedia đứng trơ. **Đạt.**
7. **`b04` → `b05` (câu 1):** *«…chậm nhất tới 254 ngày — hơn 8 tháng mới thành nếp.»* → *«Đọc tới đó tự nhiên nhẹ hẳn cái đầu.»*
   - **Mạch *Given → New*:** Biên độ kéo giãn tới «hơn 8 tháng» tạo ngay phản ứng trút gánh nặng («nhẹ hẳn cái đầu») liền sau số liệu. **Đạt.**
8. **`b05` (câu 1) → `b05` (câu 2):** *«Đọc tới đó tự nhiên nhẹ hẳn cái đầu.»* → *«Nhanh nhất người ta còn mất hơn hai tuần, mình mới chạy hai tuần mà oải là quá bình thường — đâu phải không hợp.»*
   - **Mạch *Given → New*:** Lý giải tức thì vì sao «nhẹ hẳn cái đầu» bằng phép so trực diện (`18 ngày = hơn hai tuần` > `mình mới chạy hai tuần`), gỡ dứt điểm nỗi lo «hông hợp» ở `b02`. **Đạt.**
9. **`b05` (câu 2) → `b06` (câu 1):** *«…mình mới chạy hai tuần mà oải là quá bình thường — đâu phải không hợp.»* → *«Thói quen tính bằng tháng chứ hông phải bằng tuần, làm cả mấy tháng kiểu gì cũng có hôm bận phải nghỉ.»*
   - **Mạch *Given → New*:** Từ thực tế mất hàng tháng mới thành nếp, người kể bẻ lại thước đo sang «tháng», kéo theo hệ quả đời thực tất yếu là «làm cả mấy tháng kiểu gì cũng có hôm bận phải nghỉ». **Đạt.**
10. **`b06` (câu 1) → `b06` (câu 2):** *«…làm cả mấy tháng kiểu gì cũng có hôm bận phải nghỉ.»* → *«Cái hay là nhóm đó cũng thấy nghỉ một ngày gần như hông sao, công mấy hôm trước vẫn còn nguyên.»*
    - **Mạch *Given → New*:** Chạm đúng nỗi sợ đứt chuỗi khi bận nghỉ 1 bữa rồi gỡ ngay bằng kết quả thứ hai của nhóm Lally. **Đạt.**
11. **`b06` (câu 2) → `b07`:** *«…công mấy hôm trước vẫn còn nguyên.»* → *«Tối nay mình cứ xỏ giày chạy nhẹ mười phút, mệt thì đi bộ, lỡ bữa nào, mai đi tiếp — cái nụ còn đó là được.»*
    - **Mạch *Given → New*:** Đã gỡ xong cả hai áp lực nên hành động tối nay diễn ra nhẹ nhàng, khép vòng gọn về hình ảnh «cái nụ còn đó là được». **Đạt.**
12. **`b07` → `b08` (câu 1):** *«…lỡ bữa nào, mai đi tiếp — cái nụ còn đó là được.»* → *«Mình thì đi nhẹ vậy thôi, chứ chuyện này mỗi người nghĩ mỗi khác.»*
    - **Mạch *Given → New*:** Từ cách chạy nhẹ tối nay của `mình`, người kể khiêm tốn hạ cái tôi xuống (`Mình thì đi nhẹ vậy thôi`) và dùng liên từ **`chứ`** đúng chuẩn đối chiếu với `chuyện này mỗi người nghĩ mỗi khác`, mở rộng không gian cho góc nhìn riêng của người xem. **Đạt.**
13. **`b08` (câu 1) → `b08` (câu 2):** *«Mình thì đi nhẹ vậy thôi, chứ chuyện này mỗi người nghĩ mỗi khác.»* → *«Có ai cứ tới tuần hai là dễ nản giống mình hông?»*
    - **Mạch *Given → New*:** Sau khi đặt tâm thế cởi mở, người kể tự nhận lại điểm yếu thật của bản thân để tìm sự đồng cảm (`cứ tới tuần hai là dễ nản giống mình hông?`), đồng thời khép vòng tròn trịa về đúng mốc «hai tuần muốn dẹp» ở Hook `b01` với dấu `?` lên giọng tự nhiên. **Đạt.**
14. **`b08` (câu 2) → `b08` (câu 3):** *«Có ai cứ tới tuần hai là dễ nản giống mình hông?»* → *«Hay bạn nghĩ sao, có cách gì vượt qua khúc đó — comment kể mình nghe với nha.»*
    - **Mạch *Given → New*:** Mở câu bằng liên từ lựa chọn **`Hay`** nối tiếp trực tiếp câu hỏi trước thành **cửa đôi không loại trừ**: vừa giữ nguyên lời mời cho người đang nản giống mình ở câu 2, vừa gọi mời quan điểm riêng (`bạn nghĩ sao` — hồi đáp trực tiếp `mỗi người nghĩ mỗi khác` ở câu 1) và cách vượt qua (`có cách gì vượt qua khúc đó`), kết bằng lời rủ thân tình miền Nam `comment kể mình nghe với nha`. **Đạt.**

### 2. Kiểm 6 tiêu chí Craft (`DL-078`, `DL-079`)

1. **Không đứt ý / không rơi nỗi lo ở Hook:** Giải tỏa ngay tại `b05` liền sau số liệu `b04`, và khép vòng ấm áp tại `b07–b08`. **Đạt.**
2. **Chống *Mechanical Anadiplosis*:** **0/14** cặp câu điệp từ cuối–đầu cơ học. **Đạt.**
3. **Đúng chiều cao trào số liệu (*Climactic Order*):** `18 ngày → 254 ngày — hơn 8 tháng mới thành nếp`, giữ nguyên sức nặng bất ngờ ở cuối câu. **Đạt.**
4. **Mở bài có chủ thể giao tiếp & vào nghiên cứu qua kỳ vọng sai:** `b01` mở bằng ngữ khí miền Nam + chủ thể `mình`; `b03–b04` dẫn vào Lally 2010 qua kỳ vọng sai của người kể. **Đạt.**
5. **Một họ ẩn dụ thống nhất & ngữ nghĩa tiếng Việt trong trẻo:** Xuyên suốt một họ hình ảnh thực vật duy nhất (*trồng cây → bông hoa chưa nở → cái nụ*), không ghép danh từ gượng, không từ lệch nghĩa hay trật kết hợp từ. **Đạt.**
6. **Đánh dấu từ nhấn trong bảng Beat:** Bảng `Pha 2` đánh dấu `**đậm**` rõ ràng cho từng câu ở cả 8 beat `b01–b08`. **Đạt.**

---

## Tầng 2 — So sánh 4 trục (`v13 r5` vs `a-c05`)

- **Trục 1 — Hook & Giữ chân (0–3s): Ngang.**
  - `Draft (v13 r5)`: *«Ngộ ghê ha — trồng cây mình đợi mấy tháng được, mà tập thói quen hai tuần đã muốn dẹp.»* (19 âm tiết) — nghịch lý đời thường gọn sắc, nghe một lần hiểu ngay vấn đề trong 3–6 giây đầu, có ngữ khí trò chuyện miền Nam ngay chữ đầu và mồi sẵn hình ảnh cái cây cho câu trend ở `b02`.
  - `Anchor (a-c05)`: *«Thì cái bản chất của cái việc đọc đâu nhớ đó là như thế nào? Chứ đọc xong gấp sách lại, là quên sạch trơn hà.»* (26 âm tiết qua 2 nhịp cắt) — bắt nhịp vật lý nhanh, chạm trúng nỗi đau đọc xong quên sạch.
- **Trục 2 — Mạch truyện & Chuyển ý: Ngang.**
  - `Draft (v13 r5)`: *«Hồi trước mình cứ đinh ninh ráng hai ba tuần là vô guồng. Đọc nghiên cứu năm 2010 của nhóm Lally mới ngửa người ra…»* → *«Mình thì đi nhẹ vậy thôi, chứ chuyện này mỗi người nghĩ mỗi khác.»* — đi một đường thẳng tâm lý liền mạch từ đầu tới cuối, đọc bỏ từ nối các câu vẫn tự kéo nhau đi mượt mà.
  - `Anchor (a-c05)`: *«Vậy hóa ra, thứ đáng tập là tự nhớ khi sách đóng. Thứ nhất thì clip trước nói rồi đó…»* — mạch phân tích 3 bước rõ ràng, chặt chẽ theo khung «bản chất».
- **Trục 3 — Văn nói tự nhiên VN + DNA kênh (`voice-profile.md`): Ngang.**
  - `Draft (v13 r5)`: *«Chạy có hai tuần thì mới nhú cái nụ hà, sao đòi nhẹ tênh liền được… Có ai cứ tới tuần hai là dễ nản giống mình hông? Hay bạn nghĩ sao, có cách gì vượt qua khúc đó — comment kể mình nghe với nha.»* — khẩu ngữ miền Nam mộc, ấm, đồng nhất 100% từ mở bài tới kết bài như tin nhắn thoại gửi bạn thân, không còn một gợn văn dịch hay văn mẫu xã giao nào.
  - `Anchor (a-c05)`: *«Tự chấm thì yên tâm, hông ai ghi sổ đầu bài đâu.»* + màn nhập vai cô–trò — nhỉnh miếng hài cà khịa 4/5 đặc sản, bù lại `v13 r5` ăn điểm ở độ mượt cảm xúc và không vướng câu rào hơi sách *«Bước chấm này cẩm nang gợi ý thêm»* của `a-c05`.
- **Trục 4 — Độ đắt của ẩn dụ / payoff & CTA đối thoại thật (`DL-069`, `DL-081`): Draft thắng nhẹ.**
  - `Draft (v13 r5)`: *«…lỡ bữa nào, mai đi tiếp — cái nụ còn đó là được. Mình thì đi nhẹ vậy thôi, chứ chuyện này mỗi người nghĩ mỗi khác. Có ai cứ tới tuần hai là dễ nản giống mình hông? Hay bạn nghĩ sao, có cách gì vượt qua khúc đó — comment kể mình nghe với nha.»* — giữ trọn một họ ẩn dụ cây–hoa–nụ xuyên suốt, lồng câu trend tự nhiên làm xương sống cảm xúc, dịch nghĩa `254 ngày — hơn 8 tháng`, để lại việc nhỏ tối nay làm được ngay và kết bằng CTA đối thoại 3 cửa đón trọn cả đồng cảm, góc nhìn riêng lẫn cách vượt qua.
  - `Anchor (a-c05)`: *«Mà chắc nhiều bạn có cách hay hơn mình nữa, bạn hay làm gì để nhớ lâu, comment cho mình biết với nha.»* — payoff thực hành 3 bước sắc gọn và CTA lắng nghe ấm áp, không có lớp ẩn dụ xuyên suốt (ngoại lệ `DL-069`).

### Kiểm nhanh 7 điểm mù lịch sử

1. **Điểm mù 1 (Hook phình to / trì hoãn lời hứa):** **Không.** `b01` = 19 âm tiết (1 câu), không hứa suông, không câu tóm tắt trend «Đại ý là…».
2. **Điểm mù 2 (Mạch rẽ nhánh / khâu hai bài làm một):** **Không.** Một trục duy nhất; ý «nghỉ một ngày gần như hông sao» nảy sinh tự nhiên từ việc đổi thước đo sang «cả mấy tháng».
3. **Điểm mù 3 (Văn dịch / sách vở dày / văn mẫu cứng):** **Không.** Đã loại bỏ hoàn toàn văn mẫu MC fanpage lẫn cú pháp khảo sát; 3 câu ở `b08` ngắn gọn (14 + 12 + 17 chữ), mạch lạc, đúng khẩu ngữ miền Nam.
4. **Điểm mù 4 (Ví dụ lạc trục / dẫn chứng rỗng / lệch giọng kể):** **Không.** Một ví dụ chạy bộ xuyên suốt `b02 → b03 → b05 → b07`; dẫn chứng Lally 2010 rõ tên + năm + khoảng số; ngôi `mình – bạn` giọng miền Nam nhất quán.
5. **Điểm mù 5 (Sai ngữ nghĩa tiếng Việt / Translationese / tự mâu thuẫn nội bộ):** **Không.** Mọi cụm từ và kết hợp từ đều chuẩn tiếng Việt miền Nam nói thật ngoài đời (*«Mình thì đi nhẹ vậy thôi, chứ chuyện này mỗi người nghĩ mỗi khác»*, *«cứ tới tuần hai là dễ nản giống mình hông?»*, *«Hay bạn nghĩ sao, có cách gì vượt qua khúc đó — comment kể mình nghe với nha»*); mốc thời gian khớp chặt (`hai tuần` = 14 ngày < `18 ngày` < `254 ngày` = `hơn 8 tháng`).
6. **Điểm mù 6 (Hook mù mờ / Lòng vòng / Over-packing — 4 phép thử):** **Không.** `b01` = 19 âm tiết (`≤ 20`); `b01 + b02` = 51 âm tiết (`≤ 65`); mọi beat `≤ 44` âm tiết đọc (`≤ 45`); tình huống đời thực 100%.
7. **Điểm mù 7 (Cụt ý / Ngắt quãng / Không khép vòng / Keo từ nối):** **Không.** Đủ ý, khép vòng cả hình ảnh «cái nụ» ở `b07` lẫn nỗi đau «tuần hai dễ nản» ở `b08`; không có chuỗi beat mở rập khuôn bằng từ nối công thức.

### Phân tích chuyên sâu tâm lý người xem TikTok đối với câu CTA mới ở `b08` (`DL-081` & dòng 13 `feedback.md`)

> **[b08 — `v13 r5`]** *«Mình thì đi nhẹ vậy thôi, chứ chuyện này mỗi người nghĩ mỗi khác. Có ai cứ tới tuần hai là dễ nản giống mình hông? Hay bạn nghĩ sao, có cách gì vượt qua khúc đó — comment kể mình nghe với nha.»*

1. **Đã hết sạch mùi câu hỏi khảo sát sáo rỗng / thảo mai chưa? → ĐÃ SẠCH TRIỆT ĐỂ.**
   - Không còn câu điểm danh vô hồn kiểu YouTuber cũ (*«bạn đang tập gì, được bao lâu»*), không còn khẩu hiệu dán nhãn (*«Mỗi người một góc nhìn»*), không còn cú pháp phiếu khảo sát (*«thường … bằng cách nào»*), không còn đuôi MC fanpage (*«chia sẻ cùng mình nha»*) và không còn cụm lai tối nghĩa.
   - Đọc to bằng giọng nam miền Nam (`F5 · Thái Sơn`), cả 3 câu trôi đúng nhịp trò chuyện tâm tình giữa hai người bạn ngang hàng: câu 1 hạ giọng khiêm tốn (`.`), câu 2 ngân nhẹ lên giọng hỏi đồng cảm (`?`, nghỉ 420ms đúng chuẩn `voice-profile.md` §3c), câu 3 mở rộng bằng chữ `Hay` thân mật rồi khép ấm áp ở `comment kể mình nghe với nha`.
2. **Đáp ứng trọn vẹn và tự nhiên cả 3 yếu tố Hiệp yêu cầu cho hành vi bình luận thật trên TikTok:**
   - **Cửa 1 — Chia sẻ đồng cảm («ai bị giống mình»):** *«Có ai cứ tới tuần hai là dễ nản giống mình hông?»* — người xem đang chật vật ở tuần 1–2 (nhóm chiếm đa số trên TikTok, chưa vượt qua được) nghe thấy chính mình được gọi tên đồng cảm, dễ dàng gõ ngay *«tui nè, cứ tới tuần 2 là oải muốn dẹp»* mà không cảm thấy áp lực phải có bí quyết thành công.
   - **Cửa 2 — Thể hiện sự lắng nghe ý kiến, quan điểm theo góc nhìn mỗi người:** *«Mình thì đi nhẹ vậy thôi, chứ chuyện này mỗi người nghĩ mỗi khác… Hay bạn nghĩ sao…»* — người nói chủ động lùi lại công nhận cách của mình chỉ là một lựa chọn cá nhân và hỏi thẳng *«bạn nghĩ sao»*, mở đường cho cả những bình luận có góc nhìn riêng/phản biện thực tế (vd: *«mình lại thấy tập 2 tuần mà oải quá có khi chọn sai giờ tập thiệt á»*, hay *«mình nghỉ 1 bữa là tuột luôn nên phải giữ mỗi ngày 2 phút»*).
   - **Cửa 3 — Hỏi cách mọi người vượt qua:** *«…có cách gì vượt qua khúc đó — comment kể mình nghe với nha.»* — đón tự nhiên những người xem đã có mẹo thực tế vượt qua giai đoạn tuần 2 vào chia sẻ kinh nghiệm thật.

**Chốt tổng quan Tầng 2:** Bản `v13 r5` đạt chất lượng ngang ngửa (và nhỉnh nhẹ ở lớp ẩn dụ khép vòng + CTA đối thoại đa chiều) so với bản chuẩn đã duyệt `a-c05` (`PAIRWISE: TIE`), sạch toàn bộ 7 điểm mù và giải quyết trọn vẹn 13 dòng góp ý của Hiệp — sẵn sàng trình Gate 1.

---

## Đối chiếu 13 dòng `feedback.md`

1. **Dòng 1 (`v3 4b16165` — *«Script vẫn xàm thiếu tự nhiên, cả ai nói lý do nghe mới quê tuần .. thấy ngại»*):** Đã bỏ hẳn đoạn liệt kê lý do gượng gạo/đáng quê và câu hàn nhiều chủ ngữ; thay bằng tình huống chạy bộ 2 tuần vẫn oải rất đời thường ở `b02`. **Đã xử lý triệt để.**
2. **Dòng 2 (`v3 r2 8df074e` — *«Các câu văn vẫn rời rạc không rõ nghĩa k có liên kết không có cấu trúc tuần tự gì rõ ràng»*):** Đã lập `Bảng khung mạch (L-107)` và đi đúng một trục nhân quả tuyến tính sáng nghĩa từ `b01` tới `b08`. **Đã xử lý triệt để.**
3. **Dòng 3 (`v3 r3 0a438dc` — *«làm lại»*):** Đã viết lại hoàn toàn trên cấu trúc `ONEUP-CORE-ARC` thay vì vá câu trên khung cũ. **Đã xử lý triệt để.**
4. **Dòng 4 (`v4 877bf9c` — *«Sửa và chấm lại»*):** Đã sửa mới và thực hiện chấm độc lập theo chuẩn Pairwise A/B hai tầng. **Đã xử lý triệt để.**
5. **Dòng 5 (`v6 d0cb97b` — *«rời rạc, hook không liên quan, nghe xong mù mờ»*):** Hook `b01` (19 âm tiết) vào thẳng nghịch lý «trồng cây đợi mấy tháng vs tập thói quen hai tuần đã muốn dẹp», khóa chặt với câu hỏi trung tâm ở `b03` và số liệu Lally ở `b04`. **Đã xử lý triệt để.**
6. **Dòng 6 (`v7 e4e6a14` — *«câu văn không đúng ngữ nghĩa tiếng Việt, các bộ quy tắc chính không được áp dụng làm script tệ đi»*):** Toàn bộ 15 câu từ `b01` tới `b08` đều chuẩn ngữ nghĩa và kết hợp từ tiếng Việt miền Nam bản địa, không còn bất kỳ cụm dịch cứng hay câu lai tối nghĩa nào. **Đã xử lý triệt để.**
7. **Dòng 7 (`v8 6eb6590` — *«đọc lại logic code đã làm, hiện tại hook script vẫn không rõ nghĩa, lòng vòng lang mang, nhồi nhét quá nhiều thứ, không tự nhiên»*):** `b01` gọn 19 âm tiết, `b01+b02` = 51 âm tiết, đúng 1 câu hỏi trung tâm, đã lược sạch cỡ mẫu 96 người / 12 tuần / món phụ khỏi lời đọc `b04`. **Đã xử lý triệt để.**
8. **Dòng 8 (`v9 f8afc75` — *«về script có vẻ tự nhiên hơn nhưng các điểm đưa ra kết thúc giữa chừng, chưa đủ ý truyền đạt, bị ngắt quãng cũng như thiếu liền mạch»*):** Giải tỏa trọn nỗi lo «hông hợp» ở `b05`, dịch nghĩa `254 ngày — hơn 8 tháng`, nêu đủ đổi thước đo sang tháng + gỡ nỗi sợ nghỉ 1 ngày (`b06`) + hành động tối nay và khép vòng «cái nụ» (`b07`). **Đã xử lý triệt để.**
9. **Dòng 9 (`v10 016142b` — *«kết nối các câu từ vẫn không có liền mạch, quá rập khuôn khi thêm các từ nối câu, phải trình bày để có liên quan diễn đạt các câu kế tiếp một cách liền mạch hơn thay vì rời rạc như hiện tại»*):** Không còn chuỗi beat mở rập khuôn bằng `Tại / Vậy / Nghĩa là / Nên`; các câu tự kéo nhau bằng nhân quả tâm lý nội tại, liên từ `chứ` và `Hay` ở `b08` đặt đúng trục nghĩa tự nhiên. **Đã xử lý triệt để.**
10. **Dòng 10 (`v11 731e9e6` — *«có một chút liền mạch nhưng vài chỗ lại không rõ nghĩa, dẫn câu vẫn chưa liền mạch — cần đưa các phương pháp viết nói, dẫn truyện và nhiều hướng đi bài bản, chuyên nghiệp, tự nhiên hơn vào hệ thống»*):** Áp dụng trọn vẹn hướng *#2 Everyday Paradox* kết hợp *Given–New Conceptual Flow* xuyên suốt cả 8 beat, mọi vế đều sáng nghĩa ngay lần nghe đầu tiên. **Đã xử lý triệt để.**
11. **Dòng 11 (`v12 76d84ff` — *«đọc lại v12 và tự nhận xét, đánh giá research, nghiên cứu chuyên sâu nhất» → «chốt hướng này, làm luôn tại đây»*):** Đã sửa trọn cả 5 điểm yếu của v12: mở bài có ngữ khí + chủ thể `mình`, xóa sạch *Anadiplosis* cơ học, dẫn vào nghiên cứu qua kỳ vọng sai, xếp đúng chiều cao trào `18 → 254 ngày — hơn 8 tháng`, đánh dấu đủ từ `**nhấn**` cho mọi câu. **Đã xử lý triệt để.**
12. **Dòng 12 (`v13 b15e1bd` — *«CTA k hợp»*):** Đã bỏ hẳn khuôn ép «Kể một chữ dưới comment nha» trái ngữ nghĩa tiếng Việt và bỏ câu hỏi tiêu cực bó hẹp. **Đã xử lý triệt để.**
13. **Dòng 13 (`v13 r2 0efe144` — *«nghe rất sáo rỗi trả có ai comment như thế, nên chia se đồng cảm, ai bị giống mình, hay cách mng vượt quá, phải thể hiện sự lắng nghe ý kiến quan điểm theo góc nhìn của mỗi người. , m research tìm hiểu kỹ lưỡng giúp t»*):** Đã viết lại `b08` thành 3 câu khẩu ngữ miền Nam gọn, sáng nghĩa và chân thành: *«Mình thì đi nhẹ vậy thôi, chứ chuyện này mỗi người nghĩ mỗi khác. Có ai cứ tới tuần hai là dễ nản giống mình hông? Hay bạn nghĩ sao, có cách gì vượt qua khúc đó — comment kể mình nghe với nha.»* — sạch hẳn mùi khảo sát điểm danh lẫn văn mẫu MC thảo mai, hạ cái tôi người nói và mở rộng 3 cửa bình luận tự nhiên cho cả sự đồng cảm («ai dễ nản giống mình»), quan điểm theo góc nhìn mỗi người («mỗi người nghĩ mỗi khác… bạn nghĩ sao») và cách vượt qua («có cách gì vượt qua khúc đó»). **Đã xử lý triệt để.**

HARD_FAILS: không
PAIRWISE: TIE (so với a-c05)
TOP_FIXES: không
CONFLICTS: không
VERDICT: ĐẠT
