# Đo prosody bản giọng nháp — c04v16c (script-v16c, F5 Thái Sơn speed 1.0, plan A)

File: `/workspace/clip-04-v16c-voice-only.m4a` + `content/clips/clip-04-gap-sach-tu-kiem/final/voice-only-c04v16c.wav`. Đo trên chính file giao (sau loudnorm). Nghỉ = đoạn lặng dài nhất (năng lượng, khung 10ms) tại chỗ nối hai cụm; nhấn = độ to (chỉ tính khung có tiếng) của cụm đậm so phần còn lại của câu (bỏ âm tiết cuối) và so 2 âm tiết kề mỗi bên; lên giọng = trung vị F0 âm tiết cuối so 2 âm tiết ngay trước (semitone); STT = faster-whisper small (vi) trên đoạn câu, so với lời (số/từ EN quy về cách đọc).

## Tổng

- **Tổng thời lượng giọng: 55.50s** (giới hạn 58s → ĐẠT); loudness -14.2 LUFS.
- Nói thuần (tổng các cụm, bỏ lặng hai đầu): 45.72s → plan A (≤ 47,9s). Tổng nghỉ đo tại 36 chỗ ngắt: 9.46s.
- Thứ bậc: phẩy dài nhất 0.19s < hết câu ngắn nhất 0.33s ✓.
- Cờ chặn: **5** · cảnh báo: 15.

## Tóm tắt (News, 20/10/2026 ~14:00 giờ VN)

- Làm theo lệnh «Làm voice t xem» của anh Hiệp trên v16c. Chỉ có giọng: không hình, không render, không sửa spec.
- Câu s03–s14 và s16 dùng lại take của bản v16b (lời giống hệt), có sinh thêm seed cho s01, s09, s11. Câu s02 (b01 câu 2) và s15 (b10) sinh mới, mỗi câu 4 seed.
- s16 «Comment con số nha»: đọc riêng thì F5 sinh 0,9s cho 5 âm tiết, STT nghe thành «con mẹ / còn mình», nên đã bỏ hết 6 take đó. Em sinh cả b10 trong một lần F5, rồi cắt ra ở chỗ lặng sau «mấy từ». Nghe cả câu b10 thì STT tiếng Việt ra đúng «comment con số nha», STT tiếng Anh trên đúng đoạn đó cũng ra «comment». Riêng STT cho câu ngắn đứng một mình thì vẫn ra «còn bên», nên còn cờ ✖ STT 0,5. Cần nghe bằng tai.
- Cả 4 câu hỏi đều lên giọng ở âm cuối: s01 +0,67 st, s02 +4,14 st, s07 +4,79 st, s15 +1,5 st. Cách làm là nâng cao độ âm tiết cuối, không kéo tempo.
- Nhấn chỉ tăng âm lượng, không kéo tempo, không chẻ chữ. Cột «gain đã thêm» khá lớn (+3 đến +10 dB) vì bộ giới hạn đỉnh khi đưa về -14 LUFS ăn bớt độ nhấn, phải bù lại.
- Nhịp nói: cả 15 câu nói thường đều trên 5 âm tiết/s (5,06–6,64). F5 speed 1.0 nói nhanh như vậy với mọi seed. Không tăng/giảm speed vì luật giữ speed 1.0, nên còn là cảnh báo.
- STT của whisper small dao động giữa các lần chạy: s01 lần này ra «Tối qua, sáng dậy…» (mất «Học thuộc», 0,857), lần pick trước ra đủ câu (1,0). Đây là lỗi nhận dạng của STT, không phải take thiếu chữ. Vẫn cần nghe tai.

## Từng câu

| Câu | Beat | Bắt đầu–kết thúc (s) | Nhấn: dB so câu / so chữ kề (gain đã thêm) | Cuối câu hỏi (st) | Âm tiết/s | STT (khớp) | Take |
|---|---|---|---|---|---|---|---|
| s01 Học thuộc tối qua, sáng dậy quên sạch? | b01 | 0.03–1.89 | «quên sạch» +2.3 / +3.9 (+10.3) | 0.67 | 5.59 | Tối qua, sáng dậy quên sạch! (0.857) | s01-37.wav |
| s02 Giả sử bây giờ không nhìn sách, bạn còn nhớ được những gì? | b01 | 2.24–5.07 | «không nhìn sách» +3.1 / +2.4 (+6.6) | 4.14 | 5.06 | Giả sử bây giờ không nhìn sách bạn còn nhớ được những gì. (1.0) | s02-11.wav |
| s03 Ví dụ, mình học ba mươi từ tiếng Anh để đi du lịch. | b02 | 5.47–8.07 | «ba mươi từ» +2.4 / +3.5 (+4.0) | — | 5.94 | Ví dụ mình học 30 từ tiếng Anh để đi du lịch. (1.0) | s03-53.wav |
| s04 Tối đó mình đọc đi đọc lại tới thuộc làu. | b02 | 8.42–10.40 | «thuộc làu» +2.0 / +2.6 (+10.4) | — | 5.85 | Tối đó mình đọc đi đọc lại tới thuộc lau. (0.95) | s04-89.wav |
| s05 Sáng dậy, mình gấp sách viết lại: airport, hotel, ticket, passport. | b03 | 10.80–14.50 | «gấp sách» +2.4 / +2.0 (+9.6) | — | 6.64 | Sáng dậy mình gấp sách viết lại app bọt hotel, tích kịch, bác bọt. (0.667) | s05-53.wav |
| s06 Tới từ thứ năm là hành lý thì mình khựng, không nhớ tiếng Anh là gì. | b03 | 14.85–18.39 | «khựng» +2.8 / +2.0 (+10.3) | — | 5.33 | Tới từ thứ 5 là hành lý thì mình khẩn, không nhớ tiếng Anh là gì. (0.938) | s06-97.wav |
| s07 Mình tự hỏi: hay tối qua mình chỉ nhìn chữ đến quen mắt? | b04 | 18.79–21.54 | «quen mắt» +2.4 / +3.8 (+7.0) | 4.79 | 5.58 | Mình tự hỏi, hay tối qua mình chỉ nhìn chữ đến quen lát. (0.923) | s07-37.wav |
| s08 Mình mở sách xem chỗ bí là chữ luggage, rồi gấp lại viết tiếp. | b05 | 21.94–25.13 | «chữ luggage» +2.3 / +1.8 (+9.4) | — | 5.75 | Mình mở sách xem chỗ bí là chữ lác ghịch rồi gấp lại viết tiếp. (1.0) | s08-97.wav |
| s09 Yang gộp 222 nghiên cứu với hơn 48 ngàn học sinh: lớp có kiểm tra nhỏ thì điểm cao hơn lớp không làm kiểm tra nhỏ, ở mức vừa. | b06 | 25.53–33.73 | «cao hơn» +3.9 / +2.2 (+7.6) | — | 5.28 | Giang gột 222 nghiên cứu với hơn 48 .000 học sinh lớp có kiểm tra nhỏ, thì điểm cao hơn lớp không làm kiểm tra nhỏ ở mức vừa. (0.943) | s09-89.wav |
| s10 Dunlosky xếp các cách học: tự kiểm tra nằm nhóm cao nhất. | b07 | 34.13–36.97 | «nhóm cao nhất» +2.3 / +3.4 (+6.0) | — | 6.28 | Đung lốt kỳ xếp các cách học từ kiểm tra nằm nhóm cao nhất. (0.821) | s10-97.wav |
| s11 Đọc lại, gạch chân nằm nhóm thấp nhất, tuy vẫn có ích nhưng tác dụng hẹp. | b07 | 37.32–40.87 | «nhóm thấp nhất» +3.8 / +2.4 (+7.7) | — | 6.11 | Đọc lại, cạch chân nằm nhóm thấp nhất tuy vẫn có ít nhưng tác dụng hẹp. (0.875) | s11-89.wav |
| s12 Nên mình chia ba mươi thẻ thành ba chồng mười thẻ. | b08 | 41.27–43.59 | «ba chồng» +2.1 / +4.5 (+9.9) | — | 5.12 | nên mình chia 30 thẻ thành 3 trọng 10 thẻ (0.909) | s12-11.wav |
| s13 Học hết chồng nào, mình gấp sách viết lại chồng đó. | b08 | 43.94–46.51 | «viết lại» +2.1 / +3.1 (+6.7) | — | 5.53 | Học hết trồng nào mình gấp sách viết lại trồng đó. (0.818) | s13-53.wav |
| s14 Sáng hôm sau, sách vẫn gấp, mình tự viết được luggage, đúng chữ hôm trước mình bí. | b09 | 46.91–51.11 | «tự viết được» +2.5 / +2.3 (+5.1) | — | 5.61 | Sáng hôm sau, sách vẫn gấp mình tự viết được lác ghịch đúng chữ hôm trước mình bí. (1.0) | s14-53.wav |
| s15 Còn bạn, thử gấp sách lại thì viết được mấy từ? | b10 | 51.51–54.03 | «mấy từ» +2.6 / +2.5 (+2.9) | 1.5 | 5.61 | Còn bạn, thử gấp sắt lại thì viết được mấy tờ. (0.818) | s15-71.wav |
| s16 Comment con số nha. | b10 | 54.38–55.47 | «con số» +2.0 / +2.6 (+9.8) | — | 4.63 | Còn bên còn số nha (0.5) | s16-53b.wav |

## Nghỉ tại từng ký hiệu (đo / plan)

| Câu | Sau chữ | Ký hiệu | Plan (s) | Đo (s) | Kết quả |
|---|---|---|---|---|---|
| s01 | qua | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s01 | sạch | `//` hết câu | 0.35 | 0.33 | ok |
| s02 | sách | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s02 | gì | `//¦` hết beat | 0.4 | 0.39 | ok |
| s03 | dụ | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s03 | lịch | `//` hết câu | 0.35 | 0.34 | ok |
| s04 | làu | `//¦` hết beat | 0.4 | 0.39 | ok |
| s05 | dậy | `/` phẩy/hai chấm | 0.18 | 0.18 | ok |
| s05 | lại | `/` phẩy/hai chấm | 0.18 | 0.18 | ok |
| s05 | airport | `/` phẩy/hai chấm | 0.18 | 0.18 | ok |
| s05 | hotel | `/` phẩy/hai chấm | 0.18 | 0.18 | ok |
| s05 | ticket | `/` phẩy/hai chấm | 0.18 | 0.19 | ok |
| s05 | passport | `//` hết câu | 0.35 | 0.35 | ok |
| s06 | khựng | `///` lặng có chủ ý | 0.4 | 0.37 | ok |
| s06 | gì | `//¦` hết beat | 0.4 | 0.40 | ok |
| s07 | hỏi | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s07 | mắt | `//¦` hết beat | 0.4 | 0.40 | ok |
| s08 | luggage | `/` phẩy/hai chấm | 0.18 | 0.14 | ✖ phẩy <0.15s |
| s08 | tiếp | `//¦` hết beat | 0.4 | 0.39 | ok |
| s09 | học | `/` phẩy/hai chấm | 0.18 | 0.18 | ok |
| s09 | nhỏ | `/` phẩy/hai chấm | 0.18 | 0.18 | ok |
| s09 | vừa | `//¦` hết beat | 0.4 | 0.40 | ok |
| s10 | học | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s10 | nhất | `//` hết câu | 0.35 | 0.34 | ok |
| s11 | lại | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s11 | nhất | `/` phẩy/hai chấm | 0.18 | 0.18 | ok |
| s11 | hẹp | `//¦` hết beat | 0.4 | 0.39 | ok |
| s12 | thẻ | `//` hết câu | 0.35 | 0.34 | ok |
| s13 | nào | `/` phẩy/hai chấm | 0.18 | 0.19 | ok |
| s13 | đó | `//¦` hết beat | 0.4 | 0.39 | ok |
| s14 | sau | `/` phẩy/hai chấm | 0.18 | 0.18 | ok |
| s14 | gấp | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s14 | luggage | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s14 | bí | `//¦` hết beat | 0.4 | 0.40 | ok |
| s15 | bạn | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s15 | từ | `//` hết câu | 0.35 | 0.35 | ok |

## Từ tiếng Anh (đọc theo phiên âm, STT tiếng Anh trên đúng đoạn từ đó)

| Câu | Từ | Đọc | t (s) | STT EN nghe ra |
|---|---|---|---|---|
| s05 | airport | «e pọt» | 12.52 | Epoch |
| s05 | hotel | «hô ten» | 12.97 | Park Hotel |
| s05 | ticket | «tích kịt» | 13.74 | That's good |
| s05 | passport | «pát pọt» | 14.05 | Backpack! |
| s08 | luggage | «lắc ghịt» | 23.6 | You look good |
| s09 | Yang | «Giang» | 25.07 | Next, Django. |
| s10 | Dunlosky | «Đun lốt ki» | 33.87 | Don't look kiss |
| s14 | luggage | «lắc ghịt» | 49.27 | (trống) |
| s16 | Comment | «Com men» | 54.25 | comment |

## Không đạt (cờ chặn)

- s08: nghỉ sau «luggage» (phẩy/hai chấm) 0.14s, plan 0.18s (✖ phẩy <0.15s)
- s05: STT khớp 0.667 (<0.8): «Sáng dậy mình gấp sách viết lại app bọt hotel, tích kịch, bác bọt.»
- s08: nhấn «chữ luggage» chỉ 2.3 dB so câu / 1.8 dB so chữ kề (<2 dB)
- s09: ngắt giữa cụm «nhỏ thì» 0.29s
- s16: STT khớp 0.5 (<0.8): «Còn bên còn số nha»

## Cảnh báo

- s01: 5.59 âm tiết/s (>5; đã chọn take chậm nhất đạt STT trong 1 seed)
- s02: 5.06 âm tiết/s (>5; đã chọn take chậm nhất đạt STT trong 4 seed)
- s03: 5.94 âm tiết/s (>5; đã chọn take chậm nhất đạt STT trong 3 seed)
- s04: 5.85 âm tiết/s (>5; đã chọn take chậm nhất đạt STT trong 6 seed)
- s05: 6.64 âm tiết/s (>5; đã chọn take chậm nhất đạt STT trong 6 seed)
- s06: 5.33 âm tiết/s (>5; đã chọn take chậm nhất đạt STT trong 6 seed)
- s07: 5.58 âm tiết/s (>5; đã chọn take chậm nhất đạt STT trong 3 seed)
- s08: 5.75 âm tiết/s (>5; đã chọn take chậm nhất đạt STT trong 6 seed)
- s09: 5.28 âm tiết/s (>5; đã chọn take chậm nhất đạt STT trong 1 seed)
- s10: 6.28 âm tiết/s (>5; đã chọn take chậm nhất đạt STT trong 6 seed)
- s11: 6.11 âm tiết/s (>5; đã chọn take chậm nhất đạt STT trong 5 seed)
- s12: 5.12 âm tiết/s (>5; đã chọn take chậm nhất đạt STT trong 3 seed)
- s13: 5.53 âm tiết/s (>5; đã chọn take chậm nhất đạt STT trong 6 seed)
- s14: 5.61 âm tiết/s (>5; đã chọn take chậm nhất đạt STT trong 6 seed)
- s15: 5.61 âm tiết/s (>5; đã chọn take chậm nhất đạt STT trong 7 seed)
