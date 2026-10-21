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
