# Kiểm ngắt nghỉ – nhấn – lên giọng · clip-04 v14 (W-08 / L-069)

- **File kiểm:** `/workspace/clip-04-v14-final.mp4` = `final/out/clip-04-v14-final.mp4` (giống hệt từng byte, `cmp`), mtime **20/10/2026 11:26 (giờ VN, UTC+7)**, dài 70,97s. Không có bản mới hơn trong `final/out/`.
- **Audio đo:** giọng gốc từng câu `video-engine/public/voice/c04v14-*.wav` (32 file, sinh 02:44–02:46). Đã đối chiếu với tiếng trong mp4 bằng tương quan chéo: cả 32 câu nằm đúng chỗ `timing.json` ghi (lệch −0,02…+0,05s). Giây trong bảng = `t` của câu + giây trong file câu, sai số khoảng ±0,05s.
- **Lời chốt:** `script-v14.md` dòng 78–87. Chữ `{nhấn:}` lấy theo storyboard: 14 chỗ.
- **Cách đo** (script trong `qa-v14-render/pacing-data/`):
  - Word timestamp dùng faster-whisper small chạy trên từng file câu. b07c/b07d chuyển sang medium chạy trên audio final, vì small bỏ chữ.
  - Căn chữ ASR với chữ gửi TTS theo từng âm tiết. Âm tiết nào ASR không khớp thì nội suy.
  - Khoảng lặng = khung 10ms có RMS thấp hơn đỉnh của câu (phân vị 95) quá 30 dB.
  - Nhấn: so dB trung bình của phần có tiếng và độ dài phần có tiếng của chữ nhấn với các chữ không nhấn trong cùng câu. Không tính âm tiết cuối câu, vì cuối câu tự nhiên đã dài ra.
  - F0 đo bằng librosa pyin.
- **Độ tin:** khoảng lặng và dB là **số đo** trên sóng âm. Vị trí chữ dựa vào ASR nên **nhiễu**:
  - b03b khớp 0/4 chữ, b06a khớp 5/9, b07a khớp 3/6, b10d khớp 4/6. Ở những câu này, vị trí chữ chỉ là ước lượng.
  - Ngưỡng nhấn: «đạt» khi to hơn ≥ +1 dB. «Biên» khi không to hơn nhưng dài hơn ≥ 1,3 lần và không nằm cuối câu. Còn lại là «trượt».
  - F0 cuối câu bị lẫn với thanh điệu tiếng Việt (sắc thì lên, nặng/huyền thì xuống). Vì vậy phần **«nghe như câu kể» là suy đoán**, cần nghe bằng tai.

## Tóm tắt số lỗi

| Loại | Số | Ghi chú |
|---|---|---|
| Phẩy / hai chấm không có nghỉ (<0,15s), đọc dính | **11** | b01a, b02b, b03a, b03b ×3, b03c, b05a, b05b (dấu «:»), b05c, b09a |
| Chấm / hỏi trong câu không có nghỉ (<0,15s) | **0 đo chắc** (1 nghi ở b07d) | Mọi dấu chấm trong câu đều có nghỉ 0,21–0,43s |
| Ngắt giữa cụm ≥0,25s | **1 nghi** (b07d 46,49s, 0,31s) | ASR lệch, nhiều khả năng khoảng nghỉ nằm sau «ích.», tức là đúng chỗ |
| Gãy cụm dưới ngưỡng (0,10–0,20s, nghe khựng) | **7** | b02a «tiếng Anh ‖ để» 0,20s; các chữ nhấn bị chẻ đôi: «lắc‖ghịt» ×3, «Bút‖dừng», «Viết‖trước»; «gạch‖chân» |
| Nghỉ sau phẩy ≥ nghỉ sau chấm/hỏi (sai thứ bậc) | **4** | b01b 0,40s; b08d 0,38s; b10b 0,26s; b07c 0,23s. Trong khi đó dấu chấm trong câu chỉ 0,21–0,29s, sau dấu hỏi b01a chỉ 0,33s |
| Lặng không đúng storyboard | **1** | «Bút dừng.» lặng sau 0,21s, storyboard yêu cầu 0,4s |
| Nghỉ giữa các câu đặt cố định, không theo nhịp | **1 lỗi hệ thống / 31 chỗ** | Cùng beat: 0,33–0,54s (gần như luôn khoảng 0,45–0,50). Sang beat: 0,62–0,69s. Ngoại lệ 0,83s (30,81s) và 1,09s (38,91s) |
| Tốc độ không đều giữa các câu | **5 câu quá nhanh** (>5 âm tiết/s) | b02c 5,48 · b07a 5,41 · b10d 5,36 · b02a 5,15 · b06b 5,04. Câu chậm nhất: b03b 2,88 · b04b 3,40 |
| Nhấn trượt | **9/14** (+3 biên, 2 đạt) | Đạt: b09b «Viết trước» +3,5 dB; b01a «quên sạch» +1,0 dB (sát ngưỡng) |
| Câu hỏi không lên giọng cuối | **3/4** | b01a, b01b, b10c. b04a có lên +7 st nhưng «mắt» thanh sắc nên có thể chỉ do thanh |

## Bảng lỗi theo giây

| Giây | Beat | Câu (lời chốt) | Lỗi | Số đo | Cách sửa cụ thể (không đổi lời) |
|---|---|---|---|---|---|
| 0,12–2,32 | b01 | Học thuộc tối qua, sáng dậy quên sạch? | Lên giọng: hỏi mà xuống. Ngắt: phẩy dính | «qua,» nghỉ 0,00s; «sạch» cuối câu thấp hơn trung vị câu −3,7 st, trong âm tiết đi xuống −1,2 st; ASR ghi dấu «.» | Chèn 0,15s lặng sau «qua,» (cắt tại điểm năng lượng thấp ~1,00s). Nâng pitch âm tiết cuối +2…+3 st (ngược với hàm «stem end fall» sẵn có), hoặc re-roll seed F5 và chọn take có F0 cuối đi lên |
| 0,12–2,32 | b01 | …{nhấn: quên sạch}? | Nhấn đạt sát ngưỡng | +1,0 dB; dài ×1,12 (cuối câu) | Giữ. Nếu sửa pitch câu hỏi thì đo lại |
| 2,32→2,48 | b01a→b01b | (giữa 2 câu hỏi) | Nghỉ sau dấu hỏi ngắn hơn nghỉ sau phẩy ngay sau đó | 0,33s, so với 0,40s ở «sách,» | Đặt sau «?» 0,40s; phẩy 0,18s |
| 3,18 | b01 | {nhấn: Không nhìn sách}, bạn có thể nhớ được những gì? | **Phẩy dài hơn dấu hỏi:** câu hook vỡ thành 2 mẩu | Lặng 0,40s sau «sách,». Do pipeline chẻ câu tại «,»: gap 0,18s + đệm cắt + đuôi F5 | Rút xuống 0,18s (cắt bớt lặng trong file câu) |
| 2,40–5,17 | b01 | …những gì? | Lên giọng: không lên | «gì» −0,3 st so với trung vị, trong âm tiết −1,8 st | Như b01a: +2…+3 st âm cuối, hoặc re-roll |
| 2,40–3,18 | b01 | {nhấn: Không nhìn sách} | Nhấn biên | −0,7 dB; dài ×1,38; F0 +1,9 st | Tăng +3 dB cho cả cụm (crossfade 20ms), không đổi tempo |
| 6,60 | b02 | Ví dụ học từ tiếng Anh ‖ để đi du lịch. | **Ngắt giữa câu không có dấu** | Lặng 0,20s. Spec chẻ câu thành 2 unit TTS, stitch chèn 0,18s | Ghép lại thành 1 unit (bỏ «\|» trong `phrases`), hoặc rút chỗ lặng về ≤0,05s |
| 5,38–7,64 | b02 | Ví dụ học từ tiếng Anh để đi du lịch. | Nhanh | 5,15 âm tiết/s | Tempo 0,92 (rubberband) |
| 8,88 / 9,82 | b02 | Tối đọc đi đọc lại.[0,40] Ba mươi từ,[0,00] tới {nhấn: thuộc làu}. | Phẩy dính; thứ bậc nghỉ trong câu ổn | «lại.» 0,40s đúng; «từ,» 0,00s | Chèn 0,15s sau «từ,» |
| 10,0–10,7 | b02 | …{nhấn: thuộc làu}. | **Nhấn trượt** (nhỏ hơn) | −3,1 dB; dài ×1,77 nhưng ở cuối câu | +3…+4 dB cho «thuộc làu» |
| 11,07–12,06 | b02 | Tưởng mai nhớ hết. | Quá nhanh, câu tự tin sai bị nuốt | 4 âm tiết / 0,73s = 5,48 âm tiết/s | Tempo 0,85 (dài thêm ~0,13s) |
| 13,02 | b03 | Sáng dậy, gấp sách viết lại. | Phẩy dính | «dậy,» 0,00s | Chèn 0,15s |
| 14,37–15,95 | b03 | airport, hotel, ticket, passport. | Liệt kê dính thành một chuỗi; ASR không nhận ra 4 từ (đã báo ở QA trước) | 3 dấu phẩy nghỉ 0,03 / 0,06 / 0,08s; 2,88 âm tiết/s; khớp 0/4 | Sinh lại 4 unit phiên âm (spec 11:28 đã có `e pọt / hô ten / tích kịt / pát pọt` với `keep`, chưa dựng), mỗi phẩy cách 0,18–0,22s |
| 16,85 | b03 | Tới từ thứ năm, hành lý. | Phẩy dính, nghĩa của từ thứ năm bị nuốt | «năm,» 0,00s | Chèn 0,18s |
| 17,99–18,37 | b03 | {nhấn: Bút dừng}. Không nhớ từ tiếng Anh. | **Chữ nhấn bị chẻ + lặng thiếu** ở chỗ khựng chính của truyện | Lặng 0,11s giữa «Bút‖dừng» (rubberband kéo phần tắc «-t»); sau «dừng.» chỉ 0,21s (storyboard 0,4s); nhấn biên −0,7 dB, ×1,35 | Bỏ tempo 0,78 trên «Bút», chỉ +3 dB; nới lặng sau «dừng.» lên 0,40s |
| 20,91 | b04 | Mình chột dạ.[0,43] Hay tối qua chỉ nhìn chữ đến {nhấn: quen mắt}? | Ổn (nghỉ đúng dấu) | 0,43s | — |
| 22,5–23,3 | b04 | …{nhấn: quen mắt}? | Nhấn trượt | −0,1 dB; dài ×1,57 ở cuối câu; F0 cuối +7 st (thanh sắc) | +3 dB cho «quen mắt». Câu hỏi này giữ nguyên pitch |
| 23,50–24,6 | b04 | {nhấn: Giấy trắng} sau passport.[0,29] Dừng ở đó. | Nhấn biên; câu chậm | −1,0 dB; ×1,39; F0 +5,3 st; 3,40 âm tiết/s | +2…+3 dB «Giấy trắng» |
| 26,84 | b05 | Viết không ra, mình {nhấn: mở sách}. | Phẩy dính; nhấn trượt | «ra,» 0,00s; «mở sách» −0,4 dB | Chèn 0,15s; +3 dB «mở sách» |
| 28,94–29,4 | b05 | Xem đúng chỗ bí: {nhấn: luggage}. | **Hai chấm trước từ đáp án không nghỉ; từ khoá bị chẻ; nhấn trượt** | «bí:» 0,00s; «lắc‖ghịt» lặng 0,15s; +0,7 dB, ×0,87 (ngắn hơn) | Chèn 0,25s sau «bí:»; bỏ tempo 0,78, chỉ +3 dB cho cả từ, không cắt giữa |
| 30,32 / 30,81→31,64 | b05→b06 | Gấp lại, viết tiếp. | Phẩy dính; lặng sang b06 dài hơn mọi chỗ chuyển beat khác | «lại,» 0,00s; chuyển beat 0,83s (chỗ khác 0,62–0,69) | Chèn 0,15s; chuyển beat 0,50s |
| 31,55–34,17 | b06 | Yang gộp {nhấn: 222 nghiên cứu}. | **Nhấn trượt** (ASR nhiễu, khớp 5/9) | Cụm số nhỏ hơn −6,3 dB (số đo dB chắc; ranh giới chữ là ước lượng) | Nghe tai. +3…+4 dB cho «hai trăm hai mươi hai nghiên cứu» |
| 34,0–39,1 | b06 | 4 câu ngắn b06a–d | Nghỉ đều đều kiểu đọc liệt kê; b06b nhanh | Nghỉ giữa câu 0,50 / 0,52 / 0,49s; b06b 5,04 âm tiết/s | b06a→b06b 0,25s (cùng một ý nguồn); b06c→b06d 0,30s |
| 38,91→40,0 | b06→b07 | (chuyển Yang → Dunlosky) | Lặng dài nhất clip | 1,09s (chỗ nối 2 phần dựng A/E) | 0,50s |
| 39,92–41,28 | b07 | Dunlosky xếp mười cách. | Quá nhanh, tên riêng bị nuốt | 5,41 âm tiết/s; ASR chỉ khớp 3/6 | Tempo 0,85 |
| 42,2–43,1 | b07 | Tự kiểm nằm {nhấn: nhóm cao nhất}. | Nhấn trượt | −0,9 dB; ×1,19 ở cuối câu | +3 dB |
| 44,10 / 44,60 | b07 | Đọc lại,[0,23] gạch‖chân nằm nhóm thấp nhất. | Phẩy dài hơn dấu chấm ở b03c; gãy «gạch‖chân» | 0,23s / 0,14s | Phẩy 0,18s; cụm «gạch chân» ≤0,05s |
| 46,49 | b07 | Vẫn có ích.[?] Tác dụng hẹp. | Nghi ngắt sai chỗ | Lặng 0,31s; ASR gán sau «có», nhưng xét độ dài thì nhiều khả năng nằm sau «ích.» (suy đoán) | Nghe tai; nếu lặng nằm sau «có» thì sinh lại câu |
| 47,95–49,88 | b08 | Mình chia ba mươi thẻ thành {nhấn: ba chồng}. | **Nhấn không được áp** | `units-stt.json`: emph_found 0/1 (whisper không tìm ra chữ); đo được −0,5 dB | Áp tay +3 dB cho «ba chồng» theo mốc giây |
| 49,9–52,6 | b08 | Mỗi chồng mười thẻ. / Học xong chồng đầu. | Nghỉ đều đều | 0,44 / 0,46 / 0,45s | 0,28–0,30s |
| 53,27 | b08 | Gấp sách,[0,38] viết lại đúng chồng đó. | **Phẩy dài hơn mọi dấu chấm trong câu** | 0,38s | Rút còn 0,18s |
| 55,96 | b09 | Sáng hôm sau, quay lại giấy đó. | Phẩy hơi ngắn | 0,10s | Nới lên 0,18s |
| 57,92 / 58,51 | b09 | Sách vẫn gấp.[0,26] {nhấn: Viết‖trước}. | Nhấn đạt nhưng cụm bị chẻ | +3,5 dB, ×1,41; lặng 0,15s giữa «Viết‖trước» | Bỏ tempo trên «Viết», giữ gain |
| 60,46 | b09 | Lần này viết thêm được {nhấn: luggage}. | **Nhấn trượt (nhỏ hẳn)**, từ bị chẻ | −5,9 dB; ×1,46 ở cuối câu; lặng 0,11s «lắc‖ghịt» | +4 dB cho cả từ, bỏ tempo |
| 61,34–61,9 | b10 | {nhấn: Luggage} bí sáng hôm trước. | Nhấn trượt; từ bị chẻ | −1,9 dB; ×0,85; lặng 0,11s «Lắc‖ghịt» | Như trên |
| 64,42 | b10 | Sáng hôm sau tự viết được,[0,26] không cần sách. | Phẩy bằng/dài hơn dấu chấm (b09b 0,26; b03c 0,21) | 0,26s | 0,18s |
| 65,62–67,17 | b10 | Bạn viết lại được mấy từ? | **Câu hỏi CTA không lên giọng** | «từ» −0,7 st so với trung vị, trong âm tiết −0,6 st | +2…+3 st âm cuối, hoặc re-roll |
| 67,37–68,71 | b10 | Comment con số đó nha. | Quá nhanh ở câu kêu gọi | 5,36 âm tiết/s | Tempo 0,88 |

## Nghỉ giữa các câu (31 chỗ nối)

Số đo là thời gian từ lúc câu trước hết tiếng đến lúc câu sau bắt đầu có tiếng:

- **Cùng beat:** 0,33 · 0,51 · 0,45 · 0,44 · 0,39 · 0,54 · 0,45 · 0,45 · 0,50 · 0,52 · 0,49 · 0,50 · 0,49 · 0,50 · 0,44 · 0,46 · 0,45 · 0,47 · 0,45 · 0,46 · 0,45 · 0,45 (giây).
- **Sang beat:** 0,46 · 0,66 · 0,65 · 0,62 · 0,83 · 1,09 · 0,69 · 0,65 · 0,65 (giây).

Kết luận đo được: khoảng nghỉ **cố định theo vị trí (cùng beat hay sang beat), không theo nghĩa**. Câu nào tiếp nối cùng một ý (b06a→b06b, b08a→b08b→b08c) cũng ngừng ~0,45–0,5s, bằng chỗ đổi ý. Trong khi đó dấu phẩy trong câu thường 0s, có chỗ lại lên 0,4s. Thứ bậc «phẩy < chấm < hỏi < đổi beat» bị đảo ở ít nhất 4 chỗ.

## Nguyên nhân gốc (đọc từ code và file, không suy đoán trừ chỗ ghi rõ)

1. **TTS sinh rời từng câu.** `pipeline/scripts/voice-phrase-f5.py` sinh F5-TTS theo từng unit (32 câu, 36 unit). Unit được chẻ theo dấu «|» trong `spec.phrases`; unit dưới 4 âm tiết bị gộp. Mỗi file câu có sẵn 0,06s lặng đầu và 0,1s lặng cuối. Sau đó engine đặt từng câu lên timeline theo khoảng cố định (`timing.json`: 0,2s trong cùng cảnh, 0,4s sang cảnh, 0,25s ở b06–b07). Ra thực tế là 0,45 / 0,65s đều đặn. Không bước nào tính khoảng nghỉ theo dấu câu hay nghĩa.
2. **Nghỉ trong câu phó mặc cho F5.** F5 gần như bỏ qua dấu phẩy (11 chỗ 0s). Chỗ duy nhất pipeline tự đặt nghỉ là ranh giới unit. Hàm `gap()` chỉ có nhánh cho `… ? ! . :`, còn phẩy hay không dấu đều rơi vào mặc định 0,18s, cộng thêm đệm cắt nên thành 0,40s ở b01b. Spec chẻ «tiếng Anh | để đi du lịch» ở giữa câu nên tạo ra chỗ ngắt sai lúc 6,60s.
3. **Nhấn là chỉnh sau khi sinh và quá nhẹ.** Pipeline tìm chữ bằng whisper small, rồi rubberband chỉnh: tempo 0,78, +0,8 st, +1,5 dB.
   - +1,5 dB nhỏ hơn mức chênh tự nhiên giữa các âm tiết của F5 (±3–5 dB đo được), nên tai không nghe ra.
   - Whisper không tìm ra chữ thì không chỉnh gì: b08a «ba chồng» emph_found 0/1.
   - Kéo tempo trên âm tiết có âm cuối tắc (-c, -t) làm dài khoảng tắc, thành lặng 0,11–0,15s giữa «lắc‖ghịt», «Bút‖dừng», «Viết‖trước». Khoảng lặng là số đo; giải thích cơ chế là suy đoán có cơ sở.
4. **Câu hỏi không có điều khiển ngữ điệu.**
   - Giọng mẫu F5 (`thai-son.wav` + ref_text) là câu kể.
   - Pipeline chỉ có «stem end fall» (hạ giọng), không có nâng giọng cho «?».
   - Ba câu hỏi kết bằng thanh nặng/huyền (sạch, gì, từ) nên đi xuống. Cảm nhận «nghe như câu kể» là suy đoán; ASR cũng ghi dấu «.».
5. **Speed 0.9 không phải nguyên nhân của ngắt sai**, nhưng là nguyên nhân dư thời lượng (đã báo ở QA trước). F5 tự ước độ dài theo từng unit, nên câu ngắn bị đọc vội (5,4 âm tiết/s) còn câu dài thì chậm (3,4–4,0).
6. **Dấu câu không bị mất** trong chữ gửi TTS: `units.json` và `timing.json` vẫn giữ `, . ? :`. Lỗi nằm ở chỗ F5 không theo dấu câu, và pipeline không tự đặt nghỉ theo dấu câu.

## Cách sửa rẻ nhất (không đổi lời chốt, phần lớn không cần sinh giọng lại)

1. **Ghép lại (stitch) bằng file giọng hiện có, không TTS lại.** Đặt nghỉ theo nghĩa:
   - sau «?» 0,40s; sau «.» trong cùng beat 0,30–0,35s; câu nối cùng ý 0,25s; sang beat 0,50s; b06→b07 0,50s.
   - Ước lượng tiết kiệm ~5,4s: giọng hết ở ~63,2s thay vì 68,6s. Vẫn trên 60s nếu tính end card, nên vấn đề thời lượng vẫn còn nguyên như QA trước.
2. **Sửa nghỉ trong file câu, cắt tại điểm năng lượng thấp đã đo.**
   - Chèn 0,15–0,18s ở 11 dấu phẩy và hai chấm đang 0s; riêng «bí:» chèn 0,25s.
   - Rút b01b, b08d, b10b, b07c về 0,18s.
   - Bỏ chỗ ngắt 0,20s ở b02a.
   - Nới «Bút dừng.» lên 0,40s.
3. **Nhấn:**
   - Bỏ tempo 0,78 trên các từ có âm cuối tắc. Dùng gain +3…+4 dB, crossfade 20ms, cho 9 chữ trượt và 3 chữ biên. Áp tay b08a.
   - Thêm vào cổng: chữ nhấn phải to hơn ≥ +2 dB, đo bằng script này.
4. **Câu hỏi:** nâng pitch +2…+3 st ở âm tiết cuối b01a, b01b, b10c. Code đã có cơ chế tương tự cho hạ giọng, chỉ cần đảo dấu. Nếu nghe giả thì re-roll 3 câu này với seed khác và chọn take có F0 cuối đi lên.
5. **b03b:** sinh lại 4 unit phiên âm (spec đã sửa lúc 11:28), phẩy 0,18–0,22s. **Cần Hiệp duyệt cách đọc phiên âm.**
6. **Tùy chọn:** tempo 0,85–0,9 cho b02c, b07a, b10d (thêm ~0,4s).
7. **Sau khi sửa:** chạy lại `pacing-data/analyze.py` + `report.py`, rồi **nghe tai từng câu** (manual gate W-08) trước khi trình.
