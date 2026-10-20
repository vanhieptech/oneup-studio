# Clip-04: script v18, bản đọc chi tiết cho F5 (rev 1, theo W-08 / L-016 / L-069 / L-070 / L-074). Giữ nguyên 100% lời v18

Dựa trên `final/script-v18-LOCKED.md` (Hiệp đã duyệt lời; 187 chữ, 13 câu, 8 beat). Chữ nhấn và beat lấy từ `final/script-v18-table.md`. Mình đã `diff` `script-v18.md` với `script-v18-LOCKED.md` và hai file **giống hệt nhau**. Người làm giọng: News (F5 · Thái Sơn, speed 1.0, theo L-074 đọc nhanh, không kéo chậm). OpenCreator soạn, chờ Rule Reviewer soát. File này không đổi chữ nào trong lời.

## Ký hiệu và luật

- `/` là dấu phẩy, nghỉ 0,15–0,2s (plan A 0,18s). `//` là hết câu trong beat, nghỉ 0,35s. `//|` là hết beat, nghỉ 0,4s. Không có `///` (bản này không có chỗ lặng riêng).
- **Chỉ nghỉ ở dấu câu có sẵn.** Không ngắt giữa cụm, không nghỉ nào quá 0,5s. Thứ bậc nghỉ: phẩy < hết câu < hết beat.
- **F5 không có SSML**, nên làm như sau: mỗi «chunk» dưới đây là **một lần gọi F5** (cờ `keep`, không gộp, không cắt bên trong output, theo L-016), rồi ghép lại bằng khoảng nghỉ ghi ở cột «Nghỉ sau» (có room tone). Dấu phẩy nằm **bên trong** một chunk thì để F5 tự nghỉ, sau đó đo lại; nếu dưới 0,12s thì chèn cho đủ 0,18s tại điểm năng lượng thấp, nếu trên 0,25s thì cắt về 0,18s (L-070).
- Chunk chỉ kết thúc ở dấu chấm, dấu hỏi hoặc dấu phẩy. **Không có chunk dưới 4 âm tiết** (L-016). Cụm ngắn như «Còn bạn,», «ở mức vừa.», «mỗi phần mười từ.», «Comment con số nha.» thì gộp vào chunk dài bên cạnh.
- **Nhấn** (**đậm**, khớp `{nhấn:}` của bảng): nếu chữ nhấn nằm giữa chunk thì **không chèn nghỉ trước nó**. Chỉ tăng âm lượng cụm đậm ≥ +2 dB so với phần còn lại của câu, không đổi tempo, không chẻ chữ. Nếu chữ nhấn đứng cuối chunk thì cũng +2 dB, giữ đuôi rơi tự nhiên (câu kể không lên giọng). ↗ là câu hỏi: âm tiết cuối phải lên ≥ +0,5 st khi đo F0 (L-070).
- **Phiên âm / chuẩn hoá chỉ áp vào chữ nhập cho F5.** Lời, bong bóng, caption và spec giữ nguyên chữ gốc (L-010, L-025).

## Chunk theo beat

| Beat | # | Chunk (lời gốc, ký hiệu nghỉ bên trong) | Chữ nhập F5 (nếu khác) | Nghỉ sau | Nhấn | Cảm xúc / giọng |
|---|---|---|---|---|---|---|
| b01 Hook | c01 | Học thuộc tối qua / sáng dậy **quên sạch** ↗ | — | 0,35 `//` | «quên sạch» cuối chunk, +2 dB | Sững, hỏi thẳng, đồng cảm. Câu là một chunk để ngữ điệu hỏi đi liền tới cuối |
| | c02 | Giả sử bây giờ **không nhìn sách** / bạn còn nhớ được những gì ↗ | — | 0,4 `//\|` | «không nhìn sách» giữa chunk, +2 dB, không nghỉ trước | Mềm, mời («giả sử»), lên giọng ở «những gì» |
| b02 Ví dụ | c03 | Mình học **ba mươi từ** tiếng Anh / đọc đi đọc lại tới thuộc làu | — | 0,35 `//` | «ba mươi từ» +2 dB | Kể, tự tin dần |
| | c04 | Sáng dậy mình gấp sách viết thử / | — | 0,18 `/` | — | Bình thường, hơi chậm lại |
| | c05 | tới từ thứ năm là hành lý thì mình **bí** | — | 0,4 `//\|` | «bí» cuối chunk, +2 dB, rơi giọng | Khựng, hụt. Hình có «lặng ở bí»: dùng đúng 0,4s cuối beat, không kéo thêm |
| b03 Nguyên nhân | c06 | Một thí nghiệm năm 2006 thấy / | Một thí nghiệm năm hai nghìn lẻ sáu thấy, | 0,18 `/` | — | Chuyển sang kể bằng chứng, chắc giọng, không giảng |
| | c07 | nếu **kiểm tra ngay** thì nhóm đọc lại làm tốt hơn | — | 0,35 `//` | «kiểm tra ngay» giữa chunk, +2 dB | Trung tính, thừa nhận đọc lại có lợi lúc đầu |
| | c08 | Nhưng **hai ngày sau** / nhóm tự kiểm tra lại nhớ hơn hẳn | — | 0,4 `//\|` | Bảng ghi 2 chỗ: «hai ngày sau», «hơn hẳn» (xem rủi ro R3) | Bất ngờ, đảo chiều: «Nhưng» mở chunk, có lực |
| b04 Mục tiêu | c09 | Mình cần là **sáng hôm sau** / gấp sách lại mình vẫn viết ra được | — | 0,4 `//\|` | «sáng hôm sau» +2 dB | Chắc, nói kiểu mục tiêu cá nhân, bình tĩnh |
| b05 Cách làm | c10 | Nên mình chia ba mươi từ thành **ba phần** / mỗi phần mười từ | — | 0,35 `//` | «ba phần» +2 dB | Hướng dẫn, đều nhịp |
| | c11 | Học hết phần nào / mình **gấp sách** viết lại phần đó / | — | 0,18 `/` | «gấp sách» giữa chunk, +2 dB | Đều |
| | c12 | chỗ nào bí mình mới mở sách | — | 0,4 `//\|` | «mở sách» cuối chunk, +2 dB (bảng có 2 nhấn trong câu này, xem R3) | Nhẹ, chốt cách làm |
| b06 Bằng chứng | c13 | Nhóm của Yang tổng hợp 222 nghiên cứu / | Nhóm của Giang tổng hợp hai trăm hai mươi hai nghiên cứu, | 0,18 `/` | — | Chắc, đúng mức, không cường điệu |
| | c14 | thấy lớp có kiểm tra nhỏ thì điểm **cao hơn** lớp không làm kiểm tra nhỏ / ở mức vừa | — | 0,4 `//\|` | «cao hơn» giữa chunk, +2 dB | «ở mức vừa» hạ giọng nhẹ. Gộp «ở mức vừa» (3 âm tiết) vào chunk này |
| b07 Kết quả | c15 | Sáng hôm sau / sách vẫn gấp / | — | 0,18 `/` | — | Ấm, chậm vừa |
| | c16 | mình **tự viết được** luggage / đúng chữ hành lý hôm trước mình bí | mình tự viết được lắc ghịt, đúng chữ hành lý hôm trước mình bí. (thử cả hai: chữ gốc «luggage» và «lắc ghịt», xem R5) | 0,4 `//\|` | «tự viết được» +2 dB | Nhẹ nhõm, cười nhẹ. Chữ tiếng Anh nằm giữa chunk 14 âm tiết |
| b08 CTA | c17 | Còn bạn / thử gấp sách lại thì viết được **mấy từ** ↗ // Comment **con số** nha | …mấy từ? Com men con số nha. | — (hết thoại, sang end card) | «mấy từ» +2 dB và lên giọng; «con số» +2 dB | Ấm, rủ nhẹ. **Sinh cả beat một lần** (2 câu), rồi chỉnh nghỉ giữa hai câu về 0,35s tại điểm lặng, không tách «Comment con số nha» thành lần gọi riêng (R6) |

Đếm: 17 chunk. 16 dấu phẩy (8 ở ranh giới chunk, 8 nằm trong chunk), 5 chỗ hết câu trong beat, 8 chỗ hết beat. Khớp 16 dấu phẩy và 13 dấu chấm/hỏi trong lời v18.

## Thời lượng ước tính (đo lại khi có giọng thật)

- Tốc độ F5 speed 1.0 đo ở v16c là ≈ 4,48 chữ/s nói thuần (`prosody-measure-v16c.md`). 187 chữ → **≈ 41,7s**. Khi đọc thành chữ, «2006» (4 âm tiết) và «222» (5 âm tiết) thêm khoảng 7 âm tiết, tức **+1,6s → ≈ 43,3s nói thuần**.
- Nghỉ: 16 phẩy × 0,18 = 2,88s · 5 hết câu × 0,35 = 1,75s · 7 hết beat × 0,4 = 2,8s (b08 không tính, vì sau đó là end card) → **≈ 7,4s**.
- **Giọng ≈ 50,7s, cộng end card 2s ≈ 52,7s tổng.** Mức trần là ≤ 58s giọng và ≤ 60s tổng. Bảng giây trong `script-v18-table.md` (≈ 49s) chưa tính phần đọc số, nên khi có giọng thật cần re-snap lại.

## Rủi ro F5 / ghi chú chuẩn hoá đầu vào (chỉ ở chữ nhập F5, lời giữ nguyên)

- **R1, số 2006 (c06):** F5 hay đọc sai chữ số. Chữ nhập: «hai nghìn lẻ sáu». Giọng Nam có thể nghe tự nhiên hơn với «hai ngàn lẻ sáu» (v16c đã đọc «48 ngàn» đạt STT): thử cả hai, chọn bằng STT và nghe tai. Caption và bong bóng vẫn ghi «2006».
- **R2, «Yang» và «222» (c13):** ở v16c, STT nghe «Yang» thành «Giang» và «222» thành «220 .2» (s09). Chữ nhập: «Giang», «hai trăm hai mươi hai». Ghép «Nhóm của» với «Yang» trong cùng chunk để tên không đứng trơ.
- **R3, nhấn kép trong một câu:** bảng đặt 2 `{nhấn:}` trong câu c08 («hai ngày sau», «hơn hẳn») và 2 chỗ trong câu c11–c12 («gấp sách», «mở sách»). W-08/L-031 quy định đúng 1 chỗ nhấn mỗi câu. **Không tự bỏ nhấn.** Báo Rule Reviewer quyết. Nếu giữ cả hai, chữ nhấn thứ hai chỉ +2 dB, không thêm nghỉ.
- **R4, ngắt giữa cụm có khả năng xảy ra:** ở v16c, F5 tự ngừng ≥ 0,25s tại «nhỏ thì» trong 7/8 seed. Câu c14 có lại cụm «kiểm tra nhỏ thì điểm», còn c07 có «kiểm tra ngay thì». Nên sinh 8–10 seed cho c07 và c14, chọn take không có lặng ≥ 0,25s trong cụm. **c08 «nhóm tự kiểm tra lại nhớ hơn hẳn»:** «lại» ở đây nghĩa là «thì ngược lại». Nếu F5 ngừng sau «lại», người nghe sẽ hiểu thành «tự kiểm tra lại» (kiểm tra thêm lần nữa). Phải chọn take đọc liền «lại nhớ hơn hẳn», không có lặng giữa «kiểm tra» và «lại nhớ». Đây là rủi ro nghĩa của lời đã khóa. Mình chỉ báo, không đổi chữ.
- **R5, «luggage» (c16):** nằm giữa chunk dài, đúng yêu cầu. Ở v16c, chữ nhập gốc ra STT «lắc ghịch» (s08, sim 1.0). Phiên âm «lắc ghịt» chưa được Hiệp duyệt bằng tai. Mặc định thử chữ gốc trước, chấm thêm bằng STT tiếng Anh trên đúng đoạn từ đó.
- **R6, «Comment con số nha» (c17):** ở v16c, khi sinh câu ngắn riêng, STT ra «còn mình». Vì vậy sinh cả b08 một lần. Chữ nhập «Com men» (phiên âm đề xuất ở v16c) hoặc chữ gốc, chọn bằng STT.
- **R7, hook c01:** ở v16c, STT nghe «Học thuộc… sáng dậy» thành «Học thuật… sáng dạy» (s01, 0,81). Nên sinh 6 take, chọn take STT ≥ 0,9, hoặc nghe tai xác nhận «thuộc» và «dậy».
- **R8, chữ cần tránh:** lời v18 không có «chột», «xong», «Viết trước» (đã quét). Không có dấu «:» hay «;» trong lời.
- **R9, «Mình cần là sáng hôm sau,» (c09):** F5 có thể ngừng sau «là» vì cấu trúc lạ. Chọn take đọc liền «cần là sáng hôm sau».

## Checklist News kiểm sau khi sinh giọng (ghi kết quả vào `final/prosody-measure-v18.md`)

1. Lời khớp 100% `script-v18-LOCKED.md` (STT từng chunk, sau khi quy số/tên về cách đọc).
2. Không có lặng ≥ 0,25s ở chỗ không có dấu câu. Soi kỹ «nhỏ thì», «ngay thì», «kiểm tra lại nhớ», «cần là sáng».
3. Nghỉ đo được: phẩy 0,12–0,22s · hết câu ≈ 0,35s (≥ 0,3) · hết beat ≈ 0,4s · không nghỉ nào > 0,5s · phẩy dài nhất < hết câu ngắn nhất.
4. Mỗi chữ nhấn to hơn phần còn lại của câu và chữ kề ≥ +2 dB. Không kéo tempo.
5. Ba câu hỏi (c01, c02, c17 phần 1) lên giọng ≥ +0,5 st ở âm tiết cuối.
6. 2006, 222, Yang, luggage, comment nghe rõ (STT tiếng Việt và tiếng Anh như ghi ở R1–R6). Chỗ nào STT nghi ngờ thì ghi «cần nghe tai».
7. Tổng giọng ≤ 58s (ước tính ≈ 50,7s), tổng gồm end card ≤ 60s. Loudness −14 LUFS ±1.
8. Một take cho mỗi chunk, không cắt bên trong output F5 (`intra_output_cuts = 0`, L-016). Chạy `check-rules.py` L-070 trên `prosody-measure` của bản này.

## Quyết định Rule Reviewer (2026-10-20 23:17)
- R3: P-08 cho tối đa 2 nhấn/beat; b03 và b05 đang 3. Bỏ nhấn «hơn hẳn» (giữ «hai ngày sau» là chữ đảo chiều) và «mở sách» (giữ «gấp sách» là bước chính). Đã sửa bảng + file này; lời không đổi.
- R4: đồng ý — chỉ nhận take đọc liền «lại nhớ hơn hẳn», không lặng giữa «kiểm tra» và «lại».
- «nhóm» 2 nghĩa: ghi nhận cho clip sau, không sửa bản khoá.
- Đề xuất 8–10 take cho c07/c14: đồng ý.
- Diff từng chữ chunk vs LOCKED: 187/187 khớp.

### Quyết định Rule Reviewer R8 (20/10/2026 23:30, theo Kokoro Voice báo lệch L-027)
- Hook b01 (c01–c02) theo **L-027**: khoảng ghép giữa c01 và c02 **≤ 0,1s** (thay cho 0,35 `//`). Không chèn thêm lặng ở dấu phẩy trong c01 hay c02: để F5 tự nghỉ, và không được chèn lên 0,18s. Sau hook (c02 → c03) vẫn nghỉ 0,4s như cũ.
- Lý do: L-027 là lỗi Hiệp đã bắt (hook vấp, cụt). W-17 chỉ đòi nghỉ đúng ranh giới cụm, không đòi nghỉ dài, nên hai luật không mâu thuẫn. Tốc độ giữ như hiện tại (Hiệp 20/10: đọc nhanh, không chậm lại).
- Ngắt giữa cụm (đề xuất E1 của Kokoro): ở các cụm cấm ngắt «ngay thì», «nhỏ thì», «kiểm tra lại nhớ», «cần là sáng», «gấp sách lại thì», lặng ≥ 0,12s là trả lại take. Ở chỗ khác không có ký hiệu ngắt: lặng ≥ 0,12s ghi cảnh báo vào `prosody-measure-v18.md`, lặng ≥ 0,25s là trả lại take. Ngưỡng chặn chung sẽ đo lại trên giọng F5 Thái Sơn sau v18.
