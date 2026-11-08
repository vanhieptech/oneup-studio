# QA bản dựng clip-04 v14 — Rule Reviewer (2026-10-20, giờ VN UTC+7)

File: /workspace/clip-04-v14-final.mp4 (giống hệt final/out/clip-04-v14-final.mp4, cmp OK), bản nhẹ /workspace/clip-04-v14-light.mp4.
Chỉ đọc/kiểm, không sửa/render file nào. Mốc giây = giây trong video final.

## Tóm tắt
| Mục | Verdict |
|---|---|
| 1. Giọng khớp chữ | CHƯA ĐẠT (text vào TTS khớp 100%; nghe thật nghi lỗi b03b + vài chỗ cần nghe tai) |
| 2. Thời lượng | CHƯA ĐẠT — 71,0s, vượt luật 45–60s 11s |
| 3. Khổ hình/âm | ĐẠT |
| 4. Phụ đề | CHƯA ĐẠT — thiếu 4 chunk EN đã chốt + tiêu đề hook mất dấu tiếng Việt |
| 5. Thẻ cuối | ĐẠT |
Ghi chú: chính gate của production `final/check-rules.txt` (03:11) đã báo **FAIL 10 lỗi** (STT b03/e06/e07/b08/b09, rule-55, rule-17 theme…) nhưng bản vẫn được trình.

## 1. Giọng đọc
(a) ĐO ĐƯỢC — text đưa vào F5 (units trong video-engine/public/voice/c04v14-*.json) so với lời b01–b10 script-v14 (bỏ {nhấn:}, |): 209 từ, **khớp 100% từng chữ** sau khi quy đổi các phiên âm cố ý: Yang→"Giang", Dunlosky→"Đun lốt ki", Comment→"Com men", luggage→"lắc ghịt", 222→"hai trăm hai mươi hai", 48 ngàn→"bốn mươi tám ngàn". Riêng **airport, hotel, ticket, passport đưa vào TTS nguyên chữ tiếng Anh** (bảng SAY trong clip-04-mkspec-v14.py có "e pọt/hô ten/tích kịt/pát pọt" nhưng không được áp vào phrase gửi F5).
(b) ASR faster-whisper small + medium (asr-venv), chạy trên audio final (cắt theo từng câu, từng beat) và trên stem sạch, cả vi lẫn en. Kết quả trong asr/. ASR khá nhiễu với giọng F5 + ambience (có cả câu bịa "Hãy subscribe…"), nên chỉ coi là nghi khi sai lặp lại ở nhiều lần chạy:
- **14,37–15,95s b03b "airport, hotel, ticket, passport"** — NGHI THẬT, nặng nhất. Mọi lần chạy đều không ra 4 từ: STT production "À POT, hôm nay thích bắt POT" (0,0); small "A port, hầu and tích pass port"; medium "Aboard HotecTik Passport"; ASR tiếng Anh trên stem sạch "Apport Hotetic Passport" (4 từ nghe thành 3, hotel+ticket dính nhau). 4 từ nhồi trong 1,59s.
- 31,55–34,17s b06a "…hai trăm hai mươi hai nghiên cứu" — nghi vừa: small "222 .000 cứu", medium "2.222 nghi", stem medium ra rác. Có thể "nghiên" nghe như "nghìn". Cần nghe tai.
- 51,45–52,62s b08c "Học xong chồng đầu" — nghi vừa: 4 lần ra "Học sống/gọc sông/Học sơ". Cần nghe tai chữ "xong".
- 20,19–21,0s b04a "chột dạ" — nghi nhẹ: lần nào cũng "chục/trọc/trục dạ".
- Số 48 ngàn (34,42–36,09s): các lần đều ra "48.000" → ổn. "Passport" ở b04b (23,5s) ra đúng "passport". luggage (27,98s; 59,14s; 61,34s) luôn ra "lắc ghệt/lát ghệt" = đúng kiểu phiên âm đã chọn, không thiếu từ; ASR tiếng Anh không nhận ra "luggage" → giọng Việt hoá, chấp nhận được nếu Hiệp ok cách đọc này.
- Khả năng lỗi ASR (không tính lỗi giọng): dậy→dạy, sách→sắp/sát, thuộc làu→lao/lau, bút→bước, lớp→lấp, viết→vih, Comment→Còn bên.
- Không thấy từ lặp/thừa đáng tin (1 lần medium nghe "tới từ từ thứ 5" ở 16,2s, lần khác không có → coi là ASR).

## 2. Thời lượng — 71,0s
ĐO ĐƯỢC: video 71,000s, audio 70,972s; phần dựng 68,987s + thẻ cuối 2,01s (68,99–71,00; audio lặng hẳn từ 68,64s).
Tổng giọng 32 câu = **59,95s** (F5 speed 0.9) — riêng giọng đã gần bằng cả mốc 60s. Phần lặng/đệm trong beat = 9,04s (khoảng nghỉ giữa câu 0,2s; b06–b07 0,25s; đầu/cuối beat 0,15/0,25s, b06 0,47/0,55s, b07 0,30/0,48s). silencedetect không thấy khoảng lặng nào >0,57s trong phần thoại → không có lặng thừa lớn, không có đoạn lặp.
| Beat | Thật | Mốc | Lệch | Giọng |
|---|---|---|---|---|
| b01 0,00–5,23 | 5,23 | 5 | +0,23 | 4,97 |
| b02 5,23–12,31 | 7,08 | 6 | +1,08 | 6,28 |
| b03 12,31–20,04 | 7,74 | 7 | +0,74 | 6,94 |
| b04 20,04–26,04 | 5,99 | 6 | −0,01 | 5,39 |
| b05 26,04–31,08 | 5,04 | 4 | +1,04 | 4,42 |
| b06 31,08–39,62 | 8,54 | 5 | **+3,54** | 6,77 |
| b07 39,62–47,98 | 8,36 | 6 | **+2,36** | 6,83 |
| b08 47,98–55,11 | 7,13 | 6 | +1,13 | 6,30 |
| b09 55,11–61,19 | 6,09 | 6 | +0,09 | 5,29 |
| b10 61,19–68,99 | 7,79 | 7 | +0,79 | 6,77 |
| thẻ cuối | 2,01 | 2 | 0 | – |
Kết luận: 71s vượt luật clip ngắn 45–60s 11s. Nguyên nhân chính là **giọng thật ~60s** (lời 209 từ, check-rules đã cảnh báo 219 từ vs mục tiêu 140–175) chứ không phải lặng thừa; b06+b07 dư nhiều nhất (+5,9s). "Cộng 2s thẻ cuối" không phải lý do — storyboard đã tính 2s thẻ cuối trong 60s.
SUY ĐOÁN (chưa đo): cắt toàn bộ khoảng nghỉ xuống ~0,1s chỉ được ~65s → vẫn vượt. Phải nhanh giọng (sinh lại speed 1.0, ước giọng ~54s → tổng ~59s) hoặc rút lời (cần Hiệp chốt lại).

## 3. Khổ hình — ĐẠT
H.264 1080x1920 yuv420p 30fps; AAC 48kHz **mono**; loudness tích hợp −14,6 LUFS, LRA 2,3 LU, đỉnh mẫu −1,2 dB. Không nhạc nền (đúng production-v14: Hiệp tự thêm nhạc TikTok), chỉ ambience + SFX. Bản nhẹ 540x960, 71s, có audio.

## 4. Phụ đề — CHƯA ĐẠT
Phụ đề EN cháy vào hình (karaoke), có cả bong bóng thoại tiếng Việt. Không có file srt/vtt; đối chiếu bằng timing.json + khung trích (line-*.jpg, sheet-lines-*.jpg). 32 chunk, dài nhất 6 từ (≤8 OK), mỗi chunk bám đúng mốc câu thoại (hiện từ t của câu tới câu kế).
Lỗi:
- **Tiêu đề hook 0,00–~2s "HOC THUOC TOI QUA, SANG DAY QUEN SACH?" mất toàn bộ dấu tiếng Việt** (at-00.00s.jpg, zoom-b01-b03-pen.jpg). Nguồn: clip-04-mkspec-v14.py dòng 152 viết sẵn không dấu. (Cover hero cũng không dấu: "HOC THUOC TOI QUA?" dòng 157.)
- **Thiếu 4 chunk EN đã chốt trong storyboard** (mkspec L.pop() bỏ): b02 "Until they felt fluent" (~9,4s), b03 "Couldn't recall English word" (~18,5s), b04 "I stopped right there" (~25s), b10 "Without opening the book" (~64–65s). Hệ quả: lời "thuộc làu", "Không nhớ từ tiếng Anh", "Dừng ở đó", "không cần sách" không có EN.
- Nhẹ: b02a 5,38s caption "thirty" xuất hiện trước khi lời nói "ba mươi" (theo storyboard, chấp nhận).
- `luggage` trước b05: ĐẠT — lần đầu ở lời/caption là b05b 27,98s (b03 chỉ nói "hành lý"; khung 13–26s không có chữ luggage).

## 5. Thẻ cuối — ĐẠT
68,99–71,00s (at-70.50s.jpg, zoom-endcard.jpg): có nguyên văn "Thông tin tham khảo, không thay thế tư vấn chuyên gia" và "Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/" (URL xuống dòng sau ".io/", vẫn đọc được, không cắt mép). Không có chữ gợi ý tác giả chứng thực. Nhẹ: nền trơn, không phải "nền bàn học" như storyboard.

## 6. Ghi nhận hình
- Khung đầu 0–3s và b03 (13–19,3s): **không thấy cây bút** trên giấy hay trong tay — đồng ý FLUX.
- Thêm (FLUX chưa nêu): b06–b07 (31,1–48,0s) là màn trắng riêng chỉ có giấy/thẻ/thanh, **không có bàn học, sách, nhân vật** — trái storyboard "lồng trong cùng cảnh bàn học, không cắt sang cảnh giảng tách rời".

## Cách sửa ít tốn nhất (chưa làm)
1. Giọng + thời lượng (một lần): sinh lại giọng F5 speed 1.0 cho cả 32 câu (lời giữ nguyên), b03b dùng phiên âm "e pọt, hô ten, tích kịt, pát pọt" có ngắt; nghe tai b06a, b08c, b04a; giảm nghỉ b06/b07 về 0,2/0,15s. Nếu không muốn sinh lại: atempo ~1,1 trên stem hiện có + chỉ sinh lại b03b (rủi ro giọng méo). Nếu vẫn >60s thì phải rút lời → cần Hiệp chốt.
2. Phụ đề: sửa narration hook thành "HỌC THUỘC TỐI QUA, SÁNG DẬY QUÊN SẠCH?"; trả lại 4 chunk EN đã chốt.
3. Hình: thêm bút ở b01/b03; FLUX xem lại b06–b07.
4. Chạy lại check-rules --final --stt phải 0 lỗi trước khi trình.
