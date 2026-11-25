---
title: "401 vs 403 trong 30 giây — bảo vệ hỏi «anh là ai» hay «tầng này anh không được lên»"
date: 2026-11-25
id: vht-20261125-401-vs-403
type: script
status: draft
updated: 2026-11-25
source: "RFC 9110 §15.5.2 (401) + §15.5.4 (403) · RFC 6750 §3.1 (invalid_token → 401, insufficient_scope → 403)"
tags: [vanhiep-tech, http, auth, oauth, 401, 403, script, draft]
---
# vht-20261125-401-vs-403

## Meta
- **Id:** `vht-20261125-401-vs-403`
- **Chủ đề:** 401 vs 403, phân biệt trong 30 giây
- **Người xem:** dev đi làm 1–5 năm (backend, frontend, mobile)
- **Tone:** anh em dev ngồi cà phê, thẳng, hơi xéo xắt nhưng có ích
- **Góc / takeaway 1 câu:** 401 là «mày là ai?», 403 là «biết mày rồi, không cho». Trả nhầm là frontend xử lý sai luôn.
- **Thông điệp chính:**
  1. 401 = chưa xác thực được (không có token, token sai, token hết hạn). 403 = xác thực rồi nhưng không đủ quyền.
  2. Test nhanh nhất: đăng nhập lại có hết lỗi không. Hết → 401. Vẫn bị → 403.
  3. Trả nhầm có cái giá thật: hết hạn mà trả 403 thì app không refresh token; thiếu quyền mà trả 401 thì app đá về login hoài.
- **Nối series:** clip pilot `vht-20261107-oauth-control-plane` («login OK mà API vẫn 401 vì `aud`»).
- **Khung giữ chân:** học theo công thức 5 bước (hook «bản chất» gắn hình ảnh quen → 3 mảnh ghép đánh số → ví dụ + phản ví dụ → ngắt nhịp 3–5 s → payoff áp dụng ngay). Không lấy nội dung gốc.

## Nguồn (chỉ dùng đúng những điều này)

| Claim trong lời | Nguồn |
|---|---|
| 401 = request thiếu credential hợp lệ cho resource; server trả 401 **phải** gửi header `WWW-Authenticate` | RFC 9110 §15.5.2 |
| 403 = server hiểu request nhưng từ chối; nếu đã gửi credential thì server coi là không đủ quyền; client **không nên** tự gửi lại với cùng credential | RFC 9110 §15.5.4 |
| Bearer token: `invalid_token` (hết hạn, bị thu hồi, sai, hỏng) → 401; `insufficient_scope` (thiếu scope) → 403 | RFC 6750 §3.1 |
| Muốn giấu resource có tồn tại hay không thì server được trả 404 thay cho 403 | RFC 9110 §15.5.4 (không đưa vào lời V1, để dành nếu có comment hỏi) |

Hai cái giá ở thông điệp 3 (không refresh token / đá về login hoài) là **hệ quả thường gặp** khi frontend xử lý theo đúng chuẩn mà backend trả nhầm mã, không phải trích dẫn từ RFC. Lời nói theo kiểu kinh nghiệm («hay gặp»), không gán cho RFC.

## 1. Ba phương án hook (0–3 s), Hiệp chọn một

| # | Kiểu | Lời (0–3 s) | Hình 0–3 s | Vì sao người lướt dừng |
|---|---|---|---|---|
| **A** | Đánh vào nỗi đau | «User đăng nhập xong bị đá ra login. Đăng nhập lại, bị đá tiếp. Nhiều khi thủ phạm chỉ là một con số.» | Cận mặt, thở dài. Text bật lên `LOGIN → 🔁 → LOGIN` xoay vòng | Dev nào cũng từng debug vòng lặp login. Câu cuối hứa nguyên nhân cực nhỏ, muốn biết là số nào |
| **B** | Phản trực giác | «Token hết hạn mà backend trả 403 là sai nha. Phải là 401. Nhầm cái này là app khỏi refresh token luôn.» | Chỉ thẳng camera. Text `403 ❌ → 401 ✅` gạch đổi | Nhiều người nghĩ «hết hạn = bị cấm» là đúng. Bị nói sai thẳng mặt thì muốn nghe tiếp để cãi hoặc để sửa |
| **C** | Đi thẳng vào kết quả | «Cho mình 30 giây. Xong clip này bạn nhìn log là biết 401 hay 403, khỏi đoán.» | Giơ đồng hồ bấm giờ, text `30s` đếm ngược bắt đầu chạy góc trên | Hứa kết quả đo được, có đồng hồ đếm ngược làm người xem tự cam kết xem hết |

**Đề xuất: A.** Nỗi đau cụ thể nhất, và kịch bản bên dưới trả lời đúng câu đó ở giây ~45 (payoff vòng lặp). Nếu chọn B hoặc C, chỉ thay dòng 0:00–0:03, phần còn lại giữ nguyên.

## 2. Kịch bản chi tiết (~68 s, bản dùng hook A)

Ký hiệu hình: `A-roll` = Hiệp nói trực diện trước camera · `ov-*` = overlay trong suốt trên mặt · `cu-*` = cutaway full màn · `[cut]` = đổi cỡ cảnh/zoom trên A-roll (punch-in CapCut). Mỗi dòng ≤ 5 s có ít nhất một cú ngắt nhịp.

| Mốc thời gian | Hình ảnh / Cắt cảnh / Text màn hình | Lời thoại (văn nói) |
|---|---|---|
| **0:00–0:03** | A-roll cận mặt, thở dài. `[0:00 ov-hook]` text `LOGIN → 🔁 → LOGIN` xoay vòng | User đăng nhập xong bị đá ra login. Đăng nhập lại, bị đá tiếp. |
| 0:03–0:06 | `[cut]` punch-in 115%. Text bật `401?` `403?` hai bên mặt | Nhiều khi thủ phạm chỉ là một con số. 401 hay 403. |
| 0:06–0:10 | A-roll trung, giơ tay như cầm thẻ nhân viên quẹt cửa. Text `🏢 Bảo vệ tòa nhà` | Thật ra bản chất hai thằng này là ông bảo vệ tòa nhà. |
| 0:10–0:14 | `[0:10 ov-d01]` diagram bước 1: cửa tòa nhà, bảo vệ hỏi, bong bóng **«Anh là ai?»** nhãn `401` | 401 là ông hỏi: anh là ai? Chưa quẹt thẻ, hay thẻ hết hạn. |
| 0:14–0:18 | ov-d01 bước 2: thang máy, bảo vệ lắc đầu, bong bóng **«Biết anh rồi. Tầng này anh không được lên.»** nhãn `403` | 403 là: biết anh là ai rồi. Nhưng tầng này anh không được lên. |
| 0:18–0:21 | A-roll, giơ 1 ngón tay. Text `① Nghe câu hỏi` | Vậy phân biệt sao cho lẹ? Ba bước. Một: nghe câu hỏi. |
| 0:21–0:25 | `[cut]` góc nghiêng nhẹ. Text 2 dòng: `401 = chưa biết bạn là ai` · `403 = biết rồi, không cho` | 401 là server chưa biết bạn là ai. 403 là biết rồi, mà không cho. |
| 0:25–0:29 | A-roll, giơ 2 ngón. Text `② Đăng nhập lại thử` | Hai: đăng nhập lại thử. Đây là test lẹ nhất nè. |
| 0:29–0:33 | `[0:29 ov-d02]` sơ đồ rẽ nhánh: `Login lại` → `Hết lỗi → 401` / `Vẫn lỗi → 403` | Login lại mà hết lỗi, đó là 401. Login lại vẫn bị, đó là 403. |
| 0:33–0:37 | A-roll, giơ 3 ngón, nghiêng người tới. Text `③ Đọc header` | Ba, cái này nhiều người bỏ qua. Mở header response ra coi. |
| 0:37–0:42 | `[0:37 cu-01]` cutaway full: terminal giả lập, dòng `HTTP/1.1 401` + `WWW-Authenticate: Bearer error="invalid_token"` highlight vàng | Trả 401 thì phải có header WWW-Authenticate. Chuẩn HTTP bắt buộc vậy luôn. |
| 0:42–0:46 | cu-01 tiếp: dòng thứ hai `HTTP/1.1 403` + `error="insufficient_scope"` highlight đỏ | Token sai hay hết hạn là invalid_token, 401. Thiếu scope là insufficient_scope, 403. |
| 0:46–0:50 | A-roll, mặt nghiêm lại. `[cut]` punch-in. Text `Trả nhầm thì sao?` | Rồi, giờ mới tới phần đau nè. Trả nhầm thì sao? |
| 0:50–0:55 | `[0:50 ov-q]` quote overlay: `Hết hạn → trả 403` ❌ · `→ app không refresh token` | Token hết hạn mà trả 403, app tưởng bị cấm. Không refresh token, user kẹt luôn. |
| 0:55–1:00 | ov-q đổi dòng: `Thiếu quyền → trả 401` ❌ · `→ đá về login 🔁` | Còn thiếu quyền mà trả 401, app tưởng chưa login. Đá ra login. Login xong lại bị đá. |
| 1:00–1:03 | A-roll, gõ tay xuống bàn. Text `🔁 = vòng lặp đầu clip` | Đó, cái vòng lặp hồi đầu clip đó. Thường là nó đó. |
| 1:03–1:06 | `[1:03 ov-l3]` lower-third: `401: bạn là ai? · 403: biết rồi, không cho` | Nhớ gọn: 401 hỏi bạn là ai. 403 biết rồi, không cho. |
| 1:06–1:08 | A-roll, nhướng mày nhìn camera. Text `Bạn từng trả nhầm chưa? 👇` | Còn API của bạn, đang trả đúng chưa? Đi coi thử đi. |

**Thời lượng ước:** lời khoảng 240 âm tiết ≈ 54 s ở nhịp 4,5 âm tiết/giây, cộng ngắt nhịp, cử chỉ và khoảng lặng ở 0:46 → khoảng 65–68 s. Trong khung 45–90 s của PLAN.md.

## 3. Nhịp độ & pattern interrupts

- **Góc máy:** một góc A-roll cố định (giống công thức khung), đổi nhịp bằng punch-in CapCut `[cut]`, tay đếm 1-2-3, overlay và một cutaway.
- **Ngắt nhịp chính:**
  - 0:00 text vòng lặp xoay (hook visual).
  - 0:06 tay quẹt thẻ, đổi sang ẩn dụ bảo vệ tòa nhà (liên tưởng quen thuộc, vai trò như «Mario» trong khung).
  - 0:10–0:18 ov-d01 hai bước bảo vệ (giải thích bằng hình, không thuật ngữ).
  - 0:18 / 0:25 / 0:33 tay giơ 1 / 2 / 3 ngón, text số bật lên.
  - 0:37 cutaway terminal (phần «bằng chứng» kỹ thuật).
  - 0:46 đổi giọng nghiêm, «giờ mới tới phần đau» (tăng năng lượng trước payoff).
  - 1:00 callback vòng lặp đầu clip (payoff khép hook).

## 4. Âm thanh & năng lượng

- Nhịp nhanh vừa, câu ngắn. Nhấn mạnh ở «anh là ai», «không được lên», «đăng nhập lại», «header», «phần đau».
- Đoạn ẩn dụ bảo vệ (0:10–0:18) có thể đổi giọng nhại ông bảo vệ cho vui, đúng tinh thần «làm mẫu phóng đại» của khung.
- Nhạc nền nhẹ, tắt hẳn 0.3 s ở 0:46 trước «phần đau» để tạo khoảng lặng.
- SFX: «ting» khi text số bật, «click» khi đổi dòng terminal. Không chớp sáng.

## 5. Kết thúc & CTA

- Kết ở câu nhớ gọn (1:03) rồi một câu hỏi ngắn, không kêu follow.
- CTA ngầm: «đi coi thử đi», người xem tự mở log API của mình. Text gợi comment `Bạn từng trả nhầm chưa? 👇`.

## 6. Layer manifest (V1: hook + 2 diagram + ≤1 mỗi loại)

| Id | Loại | Canvas | Output (local Mac) | a_roll | Nội dung |
|---|---|---|---|---|---|
| `ov-hook` | hook | transparent | `media/channels/vanhiep-tech/vht-20261125-401-vs-403/ov-hook.mov` | full | `LOGIN → 🔁 → LOGIN` xoay vòng |
| `ov-d01` | diagram | transparent | `…/ov-d01.mov` | cutout | Bảo vệ tòa nhà: cửa «Anh là ai?» 401 → thang máy «Tầng này không được lên» 403 |
| `ov-d02` | diagram | transparent | `…/ov-d02.mov` | full | Rẽ nhánh «Login lại → hết lỗi 401 / vẫn lỗi 403» |
| `cu-01` | cutaway | solid `--vht-bg` | `…/cu-01.mp4` | — | Terminal: 401 + `WWW-Authenticate … invalid_token`, 403 + `insufficient_scope` |
| `ov-q` | quote | transparent | `…/ov-q.mov` | full | Hai dòng trả nhầm và hệ quả |
| `ov-l3` | lower-third | transparent | `…/ov-l3.mov` | full | `401: bạn là ai? · 403: biết rồi, không cho` |

Màu chỉ từ `channels/vanhiep-tech/brand/brand-tokens.json` (One Dark): 401 dùng `yellow`, 403 dùng `red`, đúng / sai dùng `green` / `red`. Cấm hồng, magenta. Chữ Be Vietnam Pro, trong safe-zone (top 220, bottom 380, left 56, right 140).

## 7. Tự soát

| Kiểm | Kết quả |
|---|---|
| Câu < 15 từ | Đạt (đếm máy): mọi câu dưới 15 từ, câu dài nhất 13 từ |
| Không cụm sáo rỗng (rule đầu vào 3) | Đạt: không có «trong thế giới công nghệ», «hãy cùng khám phá», «bạn có bao giờ tự hỏi», «đừng bỏ lỡ», «tóm lại là», «chìa khóa», «không thể phủ nhận» |
| Ngắt nhịp mỗi 3–5 s | Đạt: mỗi dòng bảng ≤ 5 s và có text/overlay/cut/cử chỉ mới |
| Hook có câu hỏi ngầm được trả lời | «Thủ phạm là con số nào?» → trả lời 0:50–1:03 (trả nhầm 401/403 gây vòng lặp) |
| Không sao chép nội dung khung gốc | Đạt: chỉ học cấu trúc (bản chất + hình ảnh quen, 3 mảnh đánh số, phản ví dụ, payoff). Không Mario, không giọng Ý |
| Claim kỹ thuật có nguồn | Đạt: RFC 9110 §15.5.2, §15.5.4; RFC 6750 §3.1. Hệ quả trả nhầm nói như kinh nghiệm, không gán RFC |
| Kênh | @vanhiep.tech: talking-head + overlay, không chibi, không luật comic @hi.oneup |
| Người thật đọc to | CHƯA KIỂM |
