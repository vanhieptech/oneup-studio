# Đo prosody bản giọng nháp — c04v16c (script-v16c, F5 Thái Sơn speed 1.0, plan A)

File: `/workspace/clip-04-v16c-voice-only.m4a` + `content/clips/clip-04-gap-sach-tu-kiem/final/voice-only-c04v16c.wav`. Đo trên chính file giao (sau loudnorm). Nghỉ = đoạn lặng dài nhất (năng lượng, khung 10ms) tại chỗ nối hai cụm; nhấn = độ to (chỉ tính khung có tiếng) của cụm đậm so phần còn lại của câu (bỏ âm tiết cuối) và so 2 âm tiết kề mỗi bên; lên giọng = trung vị F0 âm tiết cuối so 2 âm tiết ngay trước (semitone); STT = faster-whisper small (vi) trên đoạn câu, so với lời (số/từ EN quy về cách đọc).

## Tổng

- **Tổng thời lượng giọng: 55.32s** (giới hạn 58s → ĐẠT); loudness -14.2 LUFS.
- Nói thuần (tổng các cụm, bỏ lặng hai đầu): 45.54s → plan A (≤ 47,9s). Tổng nghỉ đo tại 36 chỗ ngắt: 9.50s.
- Thứ bậc: phẩy dài nhất 0.19s < hết câu ngắn nhất 0.33s ✓.
- Cờ chặn: **2** · cảnh báo: 0.

## Tóm tắt lần sửa (News, 20/10/2026 ~14:20 giờ VN) — Rule Reviewer chấm v16c giọng CHƯA ĐẠT, chỉ làm lại s05, s08, s09

- **Các câu khác giữ nguyên take** (s01–s04, s06, s07, s10–s16). Mức to tổng của cả file được chỉnh lại về -14 LUFS, nên số dB đo có lệch nhẹ so với lần trước.
- **s08** (take mới s08-173, chọn trong 10 seed): nghỉ sau «luggage» đo **0,17s** (plan 0,18s, ≥0,15s ✓). «chữ luggage» to hơn cả câu **+2,3 dB**, hơn các chữ kề **+2,1 dB** ✓. Cách làm: hạ 2 dB ở hai âm tiết kề mỗi bên («bí là», «rồi gấp»), chỉ đổi âm lượng, không chèn nghỉ, không đổi tempo.
- **s09** (take s09-11, chọn trong 8 seed): F5 tự ngừng ≥0,25s ở «nhỏ thì» trong 7/8 seed. Take 11 là take duy nhất không có khoảng lặng ≥0,25s trong cụm: lặng dài nhất là 0,19s ở «lớp có» và 0,22s ở «nhỏ thì». Bản giao **không còn cờ ngắt giữa cụm** ✓. Nhấn «cao hơn»: +2,9 dB so với câu, +2,4 dB so với chữ kề.
- **s05** (take s05-71, chọn trong 10 seed; giữ đúng phiên âm đã duyệt «e pọt, hô ten, tích kịt, pát pọt»):
  - STT tiếng Việt trên cả beat b03 (10.77–18.52s): «Sáng dậy, mình gấp sách viết lại epoch, hotel, tích kịch, bác bọc, tới từ thứ 5 là hành lý thì mình khẩn, không nhớ tiếng Anh là gì.».
  - STT tiếng Anh trên đoạn 4 từ (12.47–14.64s): «Epoch, Hotel, Ticket, Backbox». Ra đúng **hotel, ticket**. airport ra «Epoch», passport ra «Backbox/Backpack».
  - Trong 10 seed không seed nào ra đủ cả 4 từ. Tốt nhất là s05-37 và s05-71, mỗi take ra 3/4 từ khi nghe cả đoạn. passport chưa seed nào ra. Vẫn còn cờ STT, **cần nghe bằng tai**. Nếu cần sửa thì phải đổi phiên âm, và việc đó cần anh Hiệp duyệt.
- **s16** «Comment con số nha»: giữ take tách từ một lần đọc cả b10. Khi nghe cả b10, STT ra «comment con số nha», và STT tiếng Anh trên đúng đoạn từ ra «comment». STT câu ngắn đứng một mình ra «còn mình», nên **CẦN NGHE BẰNG TAI**.
- **Nhấn ở cả 16 câu** (luật mới: ≥ +2 dB so với chữ kề): thấp nhất so với chữ kề là +2,1 dB (s08), thấp nhất so với cả câu là +2,0 dB (s04, s12, s16). s06 «khựng» lúc đầu chỉ 1,9 dB, đã hạ 1,5 dB ở «thì mình» và «không nhớ», giờ đạt +2,6 dB ✓.
- **L-074:** anh Hiệp duyệt đọc nhanh, bỏ trần 5 âm tiết/s. Đã bỏ cột âm tiết/s và cảnh báo này khỏi bảng đo. Speed vẫn 1.0.

## Từng câu

| Câu | Beat | Bắt đầu–kết thúc (s) | Nhấn: dB so câu / so chữ kề (gain đã thêm) | Cuối câu hỏi (st) | STT (khớp) | Take |
|---|---|---|---|---|---|---|
| s01 Học thuộc tối qua, sáng dậy quên sạch? | b01 | 0.03–1.90 | «quên sạch» +2.3 / +3.9 (+10.5) | 0.81 | Học thuật tối qua sáng dạy quên sạch. (0.812) | s01-37.wav |
| s02 Giả sử bây giờ không nhìn sách, bạn còn nhớ được những gì? | b01 | 2.25–5.09 | «không nhìn sách» +3.0 / +2.3 (+6.6) | 4.14 | Giả sử bây giờ không nhìn sách bạn còn nhớ được những gì. (1.0) | s02-11.wav |
| s03 Ví dụ, mình học ba mươi từ tiếng Anh để đi du lịch. | b02 | 5.49–8.09 | «ba mươi từ» +2.4 / +3.5 (+4.5) | — | Ví dụ mình học 30 từ tiếng Anh để đi du lịch. (1.0) | s03-53.wav |
| s04 Tối đó mình đọc đi đọc lại tới thuộc làu. | b02 | 8.44–10.42 | «thuộc làu» +2.0 / +2.5 (+10.4) | — | Tối đó mình đọc đi đọc lại tới thuộc lau. (0.95) | s04-89.wav |
| s05 Sáng dậy, mình gấp sách viết lại: airport, hotel, ticket, passport. | b03 | 10.82–14.55 | «gấp sách» +2.6 / +2.2 (+8.6) | — | Sáng dậy mình gắp sách viết lại epoch, hotel, tích kịch, bác bọc. (0.655) | s05-71.wav |
| s06 Tới từ thứ năm là hành lý thì mình khựng, không nhớ tiếng Anh là gì. | b03 | 14.90–18.44 | «khựng» +2.4 / +2.6 (+8.2) | — | Tới từ thứ 5 là hành lý thì mình khẩn, không nhớ tiếng Anh là gì. (0.938) | s06-97.wav |
| s07 Mình tự hỏi: hay tối qua mình chỉ nhìn chữ đến quen mắt? | b04 | 18.84–21.59 | «quen mắt» +2.5 / +3.9 (+7.5) | 4.79 | Mình tự hỏi, hay tối qua mình chỉ nhìn chữ đến quen lát. (0.923) | s07-37.wav |
| s08 Mình mở sách xem chỗ bí là chữ luggage, rồi gấp lại viết tiếp. | b05 | 21.99–25.01 | «chữ luggage» +2.3 / +2.1 (+9.0) | — | Mình mở sách xem chỗ bí là chữ lắc ghịch rồi gấp lại viết tiếp. (1.0) | s08-173.wav |
| s09 Yang gộp 222 nghiên cứu với hơn 48 ngàn học sinh: lớp có kiểm tra nhỏ thì điểm cao hơn lớp không làm kiểm tra nhỏ, ở mức vừa. | b06 | 25.41–33.55 | «cao hơn» +2.9 / +2.4 (+4.0) | — | Giang gộp 220 .2 nghiên cứu với hơn 48 .000 học sinh lớp có kiểm tra nhỏ thì điểm cao hơn lớp không làm kiểm tra nhỏ ở mức vừa. (0.971) | s09-11.wav |
| s10 Dunlosky xếp các cách học: tự kiểm tra nằm nhóm cao nhất. | b07 | 33.95–36.79 | «nhóm cao nhất» +2.3 / +3.3 (+6.0) | — | Đung lốt kỳ xếp các cách học từ kiểm tra nằm nhóm cao nhất. (0.821) | s10-97.wav |
| s11 Đọc lại, gạch chân nằm nhóm thấp nhất, tuy vẫn có ích nhưng tác dụng hẹp. | b07 | 37.14–40.69 | «nhóm thấp nhất» +3.8 / +2.4 (+7.8) | — | Đọc lại, cạch chân nằm nhóm thấp nhất tuy vẫn có ít nhưng tác dụng hẹp. (0.875) | s11-89.wav |
| s12 Nên mình chia ba mươi thẻ thành ba chồng mười thẻ. | b08 | 41.09–43.41 | «ba chồng» +2.0 / +4.5 (+10.0) | — | nên mình chia 30 thẻ thành 3 trọng 10 thẻ (0.909) | s12-11.wav |
| s13 Học hết chồng nào, mình gấp sách viết lại chồng đó. | b08 | 43.76–46.33 | «viết lại» +2.1 / +3.0 (+6.9) | — | Học hết trồng nào mình gấp sách viết lại trồng đó. (0.818) | s13-53.wav |
| s14 Sáng hôm sau, sách vẫn gấp, mình tự viết được luggage, đúng chữ hôm trước mình bí. | b09 | 46.73–50.93 | «tự viết được» +2.4 / +2.2 (+5.4) | — | Sáng hôm sau sách vẫn gấp mình tự viết được lắc ghịch đúng chữ hôm trước mình bí. (1.0) | s14-53.wav |
| s15 Còn bạn, thử gấp sách lại thì viết được mấy từ? | b10 | 51.33–53.85 | «mấy từ» +2.6 / +2.5 (+3.0) | 1.5 | Còn bạn, thử gấp sắt lại thì viết được mấy tờ. (0.818) | s15-71.wav |
| s16 Comment con số nha. | b10 | 54.20–55.29 | «con số» +2.0 / +2.5 (+10.0) | — | **CẦN NGHE BẰNG TAI** — Còn mình còn số nha (0.5) | s16-53b.wav |

## Nghỉ tại từng ký hiệu (đo / plan)

| Câu | Sau chữ | Ký hiệu | Plan (s) | Đo (s) | Kết quả |
|---|---|---|---|---|---|
| s01 | qua | `/` phẩy/hai chấm | 0.18 | 0.18 | ok |
| s01 | sạch | `//` hết câu | 0.35 | 0.33 | ok |
| s02 | sách | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s02 | gì | `//¦` hết beat | 0.4 | 0.40 | ok |
| s03 | dụ | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s03 | lịch | `//` hết câu | 0.35 | 0.34 | ok |
| s04 | làu | `//¦` hết beat | 0.4 | 0.38 | ok |
| s05 | dậy | `/` phẩy/hai chấm | 0.18 | 0.18 | ok |
| s05 | lại | `/` phẩy/hai chấm | 0.18 | 0.18 | ok |
| s05 | airport | `/` phẩy/hai chấm | 0.18 | 0.18 | ok |
| s05 | hotel | `/` phẩy/hai chấm | 0.18 | 0.18 | ok |
| s05 | ticket | `/` phẩy/hai chấm | 0.18 | 0.18 | ok |
| s05 | passport | `//` hết câu | 0.35 | 0.35 | ok |
| s06 | khựng | `///` lặng có chủ ý | 0.4 | 0.38 | ok |
| s06 | gì | `//¦` hết beat | 0.4 | 0.40 | ok |
| s07 | hỏi | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s07 | mắt | `//¦` hết beat | 0.4 | 0.40 | ok |
| s08 | luggage | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s08 | tiếp | `//¦` hết beat | 0.4 | 0.40 | ok |
| s09 | học | `/` phẩy/hai chấm | 0.18 | 0.18 | ok |
| s09 | nhỏ | `/` phẩy/hai chấm | 0.18 | 0.19 | ok |
| s09 | vừa | `//¦` hết beat | 0.4 | 0.40 | ok |
| s10 | học | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s10 | nhất | `//` hết câu | 0.35 | 0.34 | ok |
| s11 | lại | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s11 | nhất | `/` phẩy/hai chấm | 0.18 | 0.18 | ok |
| s11 | hẹp | `//¦` hết beat | 0.4 | 0.39 | ok |
| s12 | thẻ | `//` hết câu | 0.35 | 0.34 | ok |
| s13 | nào | `/` phẩy/hai chấm | 0.18 | 0.19 | ok |
| s13 | đó | `//¦` hết beat | 0.4 | 0.39 | ok |
| s14 | sau | `/` phẩy/hai chấm | 0.18 | 0.16 | ok |
| s14 | gấp | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s14 | luggage | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s14 | bí | `//¦` hết beat | 0.4 | 0.40 | ok |
| s15 | bạn | `/` phẩy/hai chấm | 0.18 | 0.17 | ok |
| s15 | từ | `//` hết câu | 0.35 | 0.35 | ok |

## Từ tiếng Anh (đọc theo phiên âm, STT tiếng Anh trên đúng đoạn từ đó)

| Câu | Từ | Đọc | t (s) | STT EN nghe ra |
|---|---|---|---|---|
| s05 | airport | «e pọt» | 12.55 | (trống) |
| s05 | hotel | «hô ten» | 13.13 | Oh |
| s05 | ticket | «tích kịt» | 13.77 | Bitcat |
| s05 | passport | «pát pọt» | 14.11 | Backpack |
| s08 | luggage | «lắc ghịt» | 23.58 | You like it |
| s09 | Yang | «Giang» | 25.15 | Yungo |
| s10 | Dunlosky | «Đun lốt ki» | 33.69 | Don't look kiss |
| s14 | luggage | «lắc ghịt» | 49.09 | Good luck, kid! |
| s16 | Comment | «Com men» | 54.07 | comment |

## Không đạt (cờ chặn)

- s05: STT khớp 0.655 (<0.8): «Sáng dậy mình gắp sách viết lại epoch, hotel, tích kịch, bác bọc.»
- s16: STT khớp 0.5 (<0.8): «Còn mình còn số nha»

## Cảnh báo

- (không có)
