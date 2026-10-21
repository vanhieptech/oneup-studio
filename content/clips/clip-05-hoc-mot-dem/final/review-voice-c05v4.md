# Rule Reviewer: chấm giọng clip-05 v4 (c05v4), 22/10/2026 ~01:00 (giờ VN, UTC+7)

Bản chấm: `final/voice-only-c05v4.wav` của commit `958e09d` (53,57s). Lời chuẩn: `script-v4-LOCKED.md`.
Cách đo: whisper **medium float32** (L-081), chạy riêng từng chunk theo `voice-only-c05v4.timing.json`. Lượt 1 không gợi ý, lượt 2 có `initial_prompt` là đúng câu khóa. Lặng đo bằng `silencedetect -35dB d=0.12` và RMS khung 20–50ms. Cao độ đo bằng librosa pyin. E1/L-070/L-027 lấy từ hàm của `check-rules.py`, chạy thẳng trên `prosody-measure-c05v4.json`.
Lưu ý: nếu lượt 2 đúng còn lượt 1 sai thì nhiều khả năng do STT đoán nhầm. Gợi ý bằng đúng câu khóa kéo STT rất mạnh, nên lượt 2 đúng **không** chứng minh chữ đọc rõ. Lượt 1 dưới 0,8 vẫn bị chặn (L-025).

## Tổng

- Tổng giọng 53,57s ✓ (≤58s). Loudness −14,1 LUFS ✓, true peak −1,2 dBTP, không clip ✓. LRA 2,0 LU.
- Chỗ nối chunk: không có click (bước nhảy mẫu ≤0,07 so với đỉnh tại mọi mép ghép) ✓.
- «317» đọc «ba trăm mười bảy» ✓ (medium ra «317»).
- Câu hỏi: c02 «nhiêu» lên **+3,8 st** ✓, c17 «hôm» lên **+1,3 st** ✓.
- «Một.» có nghỉ thật **0,25s** (29,77–30,02) ✓.
- **«Hai.» KHÔNG có nghỉ** ✖ (xem c12).
- **Ngắt giữa cụm** ✖: c14 «càng lâu | thì» 0,31s.
- `check-rules.py --prosody` dừng ngay ở `rule-48 missing final/spec.json`. Đây là lỗi tool: chế độ chỉ có giọng không nên đòi spec. Gọi thẳng các hàm trong file thì ra:
  - ✖ L-070 «delivery plan present ()»: tool tìm `final/script-*-delivery.md`, mà clip này dùng `prosody-plan.md`. Đây là lỗi giấy tờ hoặc tên file, không phải lỗi giọng.
  - ✖ L-070 c18 STT 0,6. Đo lại bằng medium thì **đạt 1,0**, nên cờ này do whisper small (L-081).
  - ✖ **E1 c14 0,31s** (thật, đúng).
  - ⚠ E1 c04/c12/c14 0,12s (`cặp|tính`, `sách|tự`, `cách|giữa`): đây là chỗ ngậm của phụ âm cuối -p/-ch, không phải chỗ ngắt. Bỏ qua.
  - ✔ L-027 hook (3 chỗ nối ≤0,1s).
- **Lỗi đo của tool:** `prosody-measure` ghi «sau Hai 0,30s», nhưng đoạn «Hai» được đặt ở 33,92–34,09 là **lặng số** (−65…−89 dB). Chữ «Hai» thật nằm liền với «Mỗi» ở 34,35. Tool phải kiểm tra đoạn số đếm có tiếng (RMS > −30 dB) trước khi đo nghỉ.

## Từng chunk

| Chunk | Giây | STT medium tự do / có gợi ý | Kết quả |
|---|---|---|---|
| c01 | 0,01–2,88 | 1,0 / 1,0 | **Đạt** |
| c02 | 2,96–4,60 | 1,0 / 1,0; lên +3,8 st | **Đạt** |
| c03 | 5,00–8,16 | **0,73** «ôm **chân di chuyển** … giới kỳ» (chân 0,96, di chuyển 0,84–0,95) / 0,93 («thí») | **Chưa đạt**: dưới 0,8. «chương Di truyền» nghe thành «chân di chuyển» với độ tin cao, khả năng cao là đọc không rõ thật. Đã khớp với nghi vấn «chương»→«chân» News nêu ở c09. |
| c04 | 8,51–11,87 | 0,94 «like hai cặp» / 1,0 | Đạt, cần nghe tai «lai» ~9,6s. Lượt có gợi ý ra đúng, nên nhiều khả năng do STT (chữ «lai» hiếm). |
| c05 | 12,27–14,80 | 1,0 / 1,0 | **Đạt** |
| c06 | 15,15–18,10 | 1,0 / 1,0; phẩy «ngay,» 0,17s | **Đạt** |
| c07 | 18,28–20,14 | 1,0 / 1,0 | **Đạt** |
| c08 | 20,49–24,17 | 1,0 / 1,0 | **Đạt** |
| c09 | 24,57–26,89 | 1,0 / 1,0 («chương đó» đúng) | **Đạt**. Nghi vấn «chân đó» là do whisper small. |
| c10 | 27,29–29,23 | 1,0 / 1,0; phẩy «đó,» 0,18s (28,33–28,50) | **Đạt**. Chỗ ngắt nằm giữa hai vế «Nên cùng ba tiếng đó / mình làm thế này», đúng ranh giới tự nhiên. |
| c11 | 29,58–33,57 | 0,94 «cẩm **năng**» (0,67) / 1,0; «Một.» nghỉ 0,25s; phẩy 0,17/0,17s | Đạt, cần nghe tai «cẩm nang» ~33,3s. |
| c12 | 33,92–36,91 | 1,0 / 1,0 nhưng «Hai» chỉ 0,38 | **Chưa đạt**: đoạn «Hai» đặt ở 33,92–34,09 là lặng. «Hai» thật ở 34,35 đọc dính liền «Mỗi», không có chút lặng nào, nên mất nhịp đếm «Một./Hai.» mà Hiệp yêu cầu. Kéo theo chỗ nối c11→c12 có lặng **0,63s** (33,73–34,36), dài quá ngưỡng 0,6 và nghe hụt. |
| c13 | 37,31–39,11 | 0,89 «thuyết nghiệm» / 1,0 | Đạt, cần nghe tai «thí» ~38,3s. |
| c14 | 39,29–44,06 | 1,0 / 1,0 | **Chưa đạt**: lặng **0,31s** ở **41,67–41,98** giữa «càng lâu | thì», chỗ không có dấu câu và gần bằng nghỉ hết câu (0,35). E1 chặn; plan cũng ghi đây là cụm cấm ngắt. |
| c15 | 44,46–45,81 | 1,0 / 1,0 | **Đạt** |
| c16 | 45,99–50,00 | 0,94 «**lại** hai cặp» / 1,0; phẩy «trạng,» 0,19s | Đạt, nghe tai «lai» ~47,1s (giống c04). |
| c17 | 50,40–52,36 | 0,89 «bạn **muốn** sắp thi» (0,41) / 1,0; phẩy «bạn,» 0,18s (50,81–50,99); lên +1,3 st | Đạt theo ngưỡng. «môn»→«muốn» lặp lại ở cả small và medium nên **phải nghe tai** ~51,0s; tai nghe ra «muốn» thì làm lại. Chỗ phẩy sau «Còn bạn,» là ranh giới tự nhiên. |
| c18 | 52,71–53,53 | **1,0 «Comment số hôm nha»** / 1,0; STT tiếng Anh nghe ra «Comment» | **Đạt**. Cờ 0,6 là do whisper small (L-081). Vẫn nên nghe tai một lần ~52,7s. |

## Phải làm lại (3 chunk), gợi ý cho News

1. **c12 «Hai. Mỗi buổi, …»**: cần nghỉ thở thật 0,25–0,33s sau «Hai».
   - Chọn take mà giữa «Hai» và «Mỗi» có điểm lặng (≥0,08s, dưới −40 dB), rồi cắt và đặt nghỉ 0,28s như cách đã làm với «Một».
   - Nếu không có take nào: thử chữ nhập F5 «Hai… Mỗi buổi, mình gấp sách tự kiểm như clip trước.» (chỉ đổi chữ nhập, caption giữ nguyên).
   - Sau khi ghép, kiểm tra đoạn «Hai» có tiếng (RMS > −30 dB) và chỗ nối c11→c12 khoảng 0,35s.
   - `line5-b05.wav` phải dựng lại theo.
2. **c03 «… chương Di truyền …»**: làm lại ≥6 seed, chọn take bằng **medium** (không dùng small), yêu cầu STT tự do ≥0,9 và nghe ra đúng «chương» và «di truyền».
   - Gợi ý chữ nhập F5: «di truyền» viết thường (chữ D hoa có thể làm F5 đọc lệch); caption vẫn «Di truyền».
   - Giữ «ba tiếng liền» là chỗ nhấn.
3. **c14 «các nhà nghiên cứu … càng phải dài.»**: làm lại để không có lặng ≥0,12s ở «càng lâu thì».
   - Nếu 6 seed vẫn ngắt: được phép rút đúng đoạn lặng thật (dưới −50 dB) xuống ~0,10s tại 41,67–41,98, theo cách `fixcommas.py`. Ghi rõ ngoại lệ trong `prosody-measure`.
   - Giữ chỗ nhấn «càng phải dài».

**Không làm lại, nhưng phải nghe tai trước khi gửi Hiệp:** «lai» (c04 9,6s, c16 47,1s), «cẩm nang» (c11 33,3s), «thí» (c13 38,3s), «môn» (c17 51,0s), «Comment» (c18 52,7s). Nếu tai nghe ra «muốn» ở c17 thì làm lại c17 luôn.

**Sửa tool (không chặn clip này):**
- `check-rules.py --prosody` không được đòi `spec.json`.
- L-070 phải nhận `prosody-plan.md` làm plan.
- Bước đo nghỉ sau số đếm phải kiểm tra đoạn số có tiếng.
- STT để chọn take và đo cuối dùng `ASR_MODEL=medium`.

## Kết luận

**CHƯA ĐẠT, chưa gửi Hiệp, chưa render.** 15/18 chunk đạt. Phải làm lại c12 (mất nghỉ sau «Hai.»), c03 (STT 0,73, «chương Di truyền» không rõ) và c14 (ngắt giữa cụm 0,31s). Làm xong thì đo lại bằng medium, rồi gửi Rule Reviewer chấm lại chỉ 3 chunk này cùng chỗ nối c11→c12.

---

# Vòng 2: chấm commit `f6d7d38`, 22/10/2026 ~01:45 (giờ VN, UTC+7)

Đo cùng cách vòng 1: whisper medium float32 từng chunk (tự do và có gợi ý), silencedetect, RMS, pyin, quét bước nhảy mẫu. Ngoài ra STT riêng các take c17 trong `/workspace/voice-work/clip-05-v4/`.

## Tổng
- Tổng 52,70s ✓, −14,2 LUFS ✓, true peak −1,2 dBTP ✓, LRA 1,7 LU.
- Chunk không đổi (c01–c02, c04–c11, c13–c16, c18): STT medium giống hệt vòng 1, không có lỗi mới. Mọi mép ghép chunk sạch (bước nhảy mẫu ≤0,08 so với đỉnh).
- Hàm check-rules: ✔ L-070 (0 cờ chặn), ✔ E1 (hết cờ chặn; còn ⚠ 0,12s ở c04 «cặp|tính» và c14 «cách|giữa», là chỗ ngậm của phụ âm cuối -p/-ch, bỏ qua), ✔ L-027. Còn ✖ «delivery plan present ()» do tool chưa nhận `prosody-plan.md`. Đây là lỗi tool, không phải lỗi giọng.
- Khớp lời: STT medium tự do ≥0,889 ở mọi chunk, không chunk nào thừa hay thiếu chữ so với bản khóa (News có `assert` chuỗi 219 chữ).

## Chunk đã sửa

| Chunk | Đo | Kết quả |
|---|---|---|
| c03 (5,00–8,00) | STT tự do **1,0** «ôn chương di truyền …», có gợi ý 0,93 (vẫn «thí») | **Đạt** |
| c12 (33,76–36,37) | «Hai» là **tiếng thật** (33,77–34,03, khoảng −10 dB). Nghỉ thở **0,25–0,28s** (34,05–34,30). Nối c11→c12 khoảng 0,33s. STT tự do 1,0 («2. Mỗi buổi …»). | **Đạt**. Lượt có gợi ý ra «ự kiểm», nên nghe tai «tự» ~35,5s. |
| c14 (38,74–43,30) | Lặng «lâu|thì» còn **0,10s** (41,12–41,22). Nền lặng −46…−59 dB là tiếng phòng, không phải lặng số. Mép cắt không click (0,003 và 0,034). «lâu» tắt dần tự nhiên, tiếng bật của «thì» ở 41,22 còn nguyên. STT 1,0/1,0. | **Đạt** (ngoại lệ E1 đã ghi) |
| c17 (49,64–51,49) | STT tự do 1,0 «môn». «Còn bạn.» chỉ nghỉ 0,15s và giọng «bạn» đi lên ở cuối (104→131 Hz), không rơi như hết câu, nên đây là ranh giới tự nhiên, ổn. **Lỗi: click ở 51,238s** (đầu «hôm», chỗ bắt đầu đoạn nâng giọng): mẫu tụt từ 0,61 xuống 0, rồi fade-in khoảng 8ms. Bước nhảy 0,72 so với đỉnh, mức nhảy lớn nhất của cả file (cả câu c17 bình thường ≤0,35). Take gốc c17-11p không có lỗi này (0,21), nên lỗi do bước nâng giọng ghép cứng. «hôm» trong file đi từ 206 xuống 157 Hz (bản gốc 152→118), không thấy méo âm sắc rõ, STT «hôm?» 1,0. Lên giọng đo theo cách của tôi (so trung vị «cách/mấy») khoảng 0 st, của News +0,91 st, nên ở sát ngưỡng. Nghe vẫn là câu hỏi vì «hôm» bắt đầu cao ngang đỉnh «mấy». | **Chưa đạt**: phải làm mượt chỗ click |

## Chọn take c17
STT medium tự do trên file take:
- **c17-11p**: «môn» 0,84 ✓ (có gợi ý cũng «môn» 0,84)
- c17-11m: «**món**» 0,36
- c17-127: «**muốn**» 0,62
- c17-37p: «muốn» 0,50
- c17-37m: «món … **đi**»

**Chọn c17-11p**, take duy nhất đọc rõ «môn». Dấu chấm ở chữ nhập không tạo ngắt lạ (0,15s, cỡ một dấu phẩy, giọng không rơi). Chỉ cần làm lại bước nâng giọng «hôm»:
- Nối bằng crossfade đều năng lượng 15–20ms, đặt mép ở chỗ năng lượng thấp nhất của phụ âm /h/ đầu «hôm» (hoặc tại điểm cắt qua 0).
- Không để mẫu tụt thẳng về 0.
- Đo lại: bước nhảy mẫu trong c17 ≤0,35 so với đỉnh, STT «hôm» vẫn đúng, «hôm» cao hơn «mấy/cách» ≥ +0,5 st theo plan.
- Nếu nâng làm méo thì giảm xuống khoảng +3 st. Câu vẫn nghe là câu hỏi nhờ có «mấy» và dấu «?» trên phụ đề.

## Thay cho nghe tai (chỉ là ước lượng, vẫn nên nghe 1 lần)
- **«lai» (c04 9,40–9,56; c16 46,30–46,44):** giữa «lai» và «hai» **không có chỗ ngậm của âm tắc** (c04 năng lượng liền ≥ −17 dB; c16 chỉ xuống −29 dB ở /h/ đầu «hai»). «like» cần một quãng ngậm /k/ gần như lặng, nên kết luận nghe ra «like» là do STT đoán. F2 khoảng 1,5 kHz lướt lên, đúng kiểu nguyên âm đôi /ai/. **Rủi ro thấp.**
- **«cẩm nang» (c11 33,12–33,36):** phần nguyên âm hữu thanh dài 0,27s (cuối câu). F1/F2 (khoảng 520/2040 Hz) nằm trong vùng của «dạng/trạng» cùng clip. Ước lượng LPC kém tin cậy với âm /ă/ ngắn, nên đây chỉ là bằng chứng yếu. Lượt có gợi ý ra «nang». **Rủi ro thấp–vừa**, nghe tai 1 lần.
- Còn lại cần nghe tai: «thí» (c13 ~37,8s; STT tự do «thuyết», 0,57), «tự» (c12 ~35,5s), «Comment» (c18 ~51,8s, STT vi 1,0).

## Kết luận vòng 2
**CHƯA ĐẠT, chỉ còn 1 lỗi**: click ở 51,238s (c17, đầu «hôm»). c03, c12, c14 **đạt**. Giữ take **c17-11p**, chỉ nối lại đoạn nâng giọng bằng crossfade. Không cần sinh lại F5. Sửa xong chỉ cần chấm lại c17 cùng chỗ nối c16→c17 và c17→c18. Đạt thì gửi Hiệp nghe, kèm danh sách chữ cần nghe tai ở trên.
