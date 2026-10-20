# Đo prosody bản giọng nháp — c04v18 (script-v18-LOCKED, F5 Thái Sơn speed 1.0, plan A)

File: `/workspace/clip-04-v18-voice-only.m4a` + `content/clips/clip-04-gap-sach-tu-kiem/final/voice-only-c04v18.wav`. Đo trên chính file giao (sau loudnorm). Nghỉ = đoạn lặng dài nhất (năng lượng, khung 10ms) tại chỗ nối hai cụm; nhấn = độ to (chỉ tính khung có tiếng) của cụm đậm so phần còn lại của câu (bỏ âm tiết cuối) và so 2 âm tiết kề mỗi bên; lên giọng = trung vị F0 âm tiết cuối so 2 âm tiết ngay trước (semitone); STT = faster-whisper medium float32 (vi) trên đoạn câu, so với lời (số/từ EN quy về cách đọc).

## Tổng

- **Tổng thời lượng giọng: 46.03s** (giới hạn 58s → ĐẠT); loudness -14.2 LUFS.
- Nói thuần (tổng các cụm, bỏ lặng hai đầu): 40.76s → plan A (≤ 47,9s). Tổng nghỉ đo tại 28 chỗ ngắt: 6.82s.
- Thứ bậc: phẩy dài nhất 0.20s < hết câu ngắn nhất 0.34s ✓.
- Cờ chặn: **0** · cảnh báo: 0.

## Từng câu

| Câu | Beat | Bắt đầu–kết thúc (s) | Nhấn: dB so câu / so chữ kề (gain đã thêm) | Cuối câu hỏi (st) | STT (khớp) | Take |
|---|---|---|---|---|---|---|
| c01 Học thuộc tối qua, sáng dậy quên sạch? | b01 | 0.04–1.70 | «quên sạch» +2.3 / +3.2 (+7.1) | 0.8 | Học thuộc tối qua sáng dậy quên sạch (1.0) | c01-71.wav |
| c02 Giả sử bây giờ không nhìn sách, bạn còn nhớ được những gì? | b01 | 1.78–4.46 | «không nhìn sách» +2.8 / +2.4 (+8.6) | 5.48 | Giả sử bây giờ không nhìn sách bạn còn nhớ được những gì? (1.0) | c02-71.wav |
| c03 Mình học ba mươi từ tiếng Anh, đọc đi đọc lại tới thuộc làu. | b02 | 4.86–7.72 | «ba mươi từ» +2.6 / +2.5 (+3.0) | — | Mình học 30 từ tiếng Anh, đọc đi đọc lại tới thuộc Lào. (0.929) | c03-37.wav |
| c04 Sáng dậy mình gấp sách viết thử, | b02 | 8.07–9.58 | — | — | Sáng dậy mình gấp sách viết thử. (1.0) | c04-11.wav |
| c05 tới từ thứ năm là hành lý thì mình bí. | b02 | 9.76–11.65 | «bí» +2.4 / +3.7 (+6.2) | — | Tới từ thứ 5 là hành lý thì mình bí. (1.0) | c05-11.wav |
| c06 Một thí nghiệm năm 2006 thấy, | b03 | 12.05–13.84 | — | — | Một thí nghiệm năm 2006 thấy (1.0) | c06-71n.wav |
| c07 nếu kiểm tra ngay thì nhóm đọc lại làm tốt hơn. | b03 | 14.03–16.30 | «kiểm tra ngay» +3.0 / +2.5 (+6.3) | — | Nếu kiểm tra ngay thì nhóm đọc lại làm tốt hơn. (1.0) | c07-113.wav |
| c08 Nhưng hai ngày sau, nhóm tự kiểm tra lại nhớ hơn hẳn. | b03 | 16.65–19.19 | «hai ngày sau» +3.6 / +2.3 (+8.6) | — | Nhưng hai ngày sau, nhóm tự kiểm tra lại nhớ hơn hẳn. (1.0) | c08-37.wav |
| c09 Mình cần là sáng hôm sau, gấp sách lại mình vẫn viết ra được. | b04 | 19.59–22.51 | «sáng hôm sau» +2.9 / +2.5 (+6.3) | — | Mình cần là sáng hôm sau, gấp sách lại mình vẫn viết ra được. (1.0) | c09-11.wav |
| c10 Nên mình chia ba mươi từ thành ba phần, mỗi phần mười từ. | b05 | 22.91–25.65 | «ba phần» +2.3 / +3.2 (+10.2) | — | Nên mình chia 30 từ thành 3 phần, mỗi phần 10 từ. (1.0) | c10-37.wav |
| c11 Học hết phần nào, mình gấp sách viết lại phần đó, | b05 | 26.00–28.43 | «gấp sách» +3.1 / +2.3 (+6.6) | — | Học hết phần nào, mình gấp sách viết lại phần đó. (1.0) | c11-11.wav |
| c12 chỗ nào bí mình mới mở sách. | b05 | 28.61–29.85 | — | — | Chỗ nào bí mình mới mở sách? (1.0) | c12-11.wav |
| c13 Nhóm của Yang tổng hợp 222 nghiên cứu, | b06 | 30.25–32.75 | — | — | Nhóm của Giang tổng hợp 222 nghiên cứu (1.0) | c13-11.wav |
| c14 thấy lớp có kiểm tra nhỏ thì điểm cao hơn lớp không làm kiểm tra nhỏ, ở mức vừa. | b06 | 32.95–37.19 | «cao hơn» +2.4 / +2.6 (+4.0) | — | Thấy lớp có kiểm tra nhỏ thì điểm cao hơn lớp không làm kiểm tra nhỏ ở mức vừa. (1.0) | c14-89.wav |
| c15 Sáng hôm sau, sách vẫn gấp, | b07 | 37.59–38.83 | — | — | Sáng hôm sau sách vẫn gấp. (1.0) | c15-11.wav |
| c16 mình tự viết được luggage, đúng chữ hành lý hôm trước mình bí. | b07 | 39.01–41.99 | «tự viết được» +3.0 / +2.4 (+9.1) | — | Mình tự viết được lắc gịch đúng chữ hành lý hôm trước mình bí. (0.929) | c16-71r.wav |
| c17a Còn bạn, thử gấp sách lại thì viết được mấy từ? | b08 | 42.39–44.88 | «mấy từ» +3.3 / +3.7 (+2.9) | 0.92 | Còn bạn, thử gấp sách lại thì viết được mấy tư. (0.955) | c17a-113.wav |
| c17b Comment con số nha. | b08 | 45.23–46.01 | «con số» +2.3 / +3.3 (+9.6) | — | Comment con số nha! (1.0) | c17b-101o.wav |

## Nghỉ tại từng ký hiệu (đo / plan)

| Câu | Sau chữ | Ký hiệu | Plan (s) | Đo (s) | Kết quả |
|---|---|---|---|---|---|
| c01 | sạch | `//hook` ghép hook (L-027 ≤0,1s) | 0.08 | 0.08 | ok |
| c02 | gì | `//¦` hết beat | 0.4 | 0.39 | ok |
| c03 | làu | `//` hết câu | 0.35 | 0.35 | ok |
| c04 | thử | `/` phẩy/hai chấm | 0.18 | 0.19 | ok |
| c05 | bí | `//¦` hết beat | 0.4 | 0.40 | ok |
| c06 | thấy | `/` phẩy/hai chấm | 0.18 | 0.19 | ok |
| c07 | hơn | `//` hết câu | 0.35 | 0.35 | ok |
| c08 | hẳn | `//¦` hết beat | 0.4 | 0.39 | ok |
| c09 | được | `//¦` hết beat | 0.4 | 0.41 | ok |
| c10 | từ | `//` hết câu | 0.35 | 0.34 | ok |
| c11 | đó | `/` phẩy/hai chấm | 0.18 | 0.16 | ok |
| c12 | sách | `//¦` hết beat | 0.4 | 0.39 | ok |
| c13 | cứu | `/` phẩy/hai chấm | 0.18 | 0.20 | ok |
| c14 | vừa | `//¦` hết beat | 0.4 | 0.39 | ok |
| c15 | gấp | `/` phẩy/hai chấm | 0.18 | 0.18 | ok |
| c16 | bí | `//¦` hết beat | 0.4 | 0.39 | ok |
| c17a | từ | `//` hết câu | 0.35 | 0.34 | ok |
| c01 | qua | `/` phẩy trong chunk (hook ≤0,1s) | 0.1 | 0.07 | ok |
| c02 | sách | `/` phẩy trong chunk (hook ≤0,1s) | 0.1 | 0.07 | ok |
| c03 | Anh | `/` phẩy trong chunk | 0.18 | 0.17 | ok |
| c08 | sau | `/` phẩy trong chunk | 0.18 | 0.17 | ok |
| c09 | sau | `/` phẩy trong chunk | 0.18 | 0.14 | ok |
| c10 | phần | `/` phẩy trong chunk | 0.18 | 0.18 | ok |
| c11 | nào | `/` phẩy trong chunk | 0.18 | 0.18 | ok |
| c14 | nhỏ | `/` phẩy trong chunk | 0.18 | 0.19 | ok |
| c15 | sau | `/` phẩy trong chunk | 0.18 | 0.17 | ok |
| c16 | luggage | `/` phẩy trong chunk | 0.18 | 0.17 | ok |
| c17a | bạn | `/` phẩy trong chunk | 0.18 | 0.17 | ok |

## Từ tiếng Anh (đọc theo phiên âm, STT tiếng Anh trên đúng đoạn từ đó)

| Câu | Từ | Đọc | t (s) | STT EN nghe ra |
|---|---|---|---|---|
| c13 | Yang | «Giang» | 30.62 | Thank you. Thank you. |
| c16 | luggage | «lắc ghịt» | 39.74 | Good luck, good! |
| c17b | Comment | «Com men» | 45.13 | (trống) |

## Mọi chỗ lặng ≥0,05s giữa hai chữ (`silences` trong .json, R8 + E1)

Ngưỡng R8: trong cụm cấm ngắt («ngay thì», «nhỏ thì», «kiểm tra lại nhớ», «cần là sáng», «gấp sách lại thì») lặng ≥0,12s là trả take; chỗ khác không có ký hiệu ngắt: ≥0,12s cảnh báo, ≥0,25s trả take. Lặng được gán vào ranh giới chữ theo điểm giữa của đoạn lặng.

Tổng 71 chỗ lặng ≥0,05s · ở chỗ không có ký hiệu: 43 (≥0,12s: 0).

| Chunk | t (s) | Lặng (s) | Ký hiệu | Trước | Sau | Kết quả |
|---|---|---|---|---|---|---|
| c01 | 0.15–0.25 | 0.10 | none | Học | thuộc tối qua | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c01 | 0.35–0.45 | 0.10 | none | Học thuộc | tối qua sáng | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c01 | 0.86–0.93 | 0.07 | comma | thuộc tối qua | sáng dậy quên | đúng ký hiệu |
| c01→c02 | 1.70–1.78 | 0.08 | sentence | dậy quên sạch | Giả sử bây | đúng ký hiệu |
| c02 | 3.11–3.18 | 0.07 | comma | không nhìn sách | bạn còn nhớ | đúng ký hiệu |
| c02 | 3.96–4.01 | 0.05 | none | còn nhớ được | những gì Mình | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c02→c03 | 4.47–4.86 | 0.39 | beat | được những gì | Mình học ba | đúng ký hiệu |
| c03 | 5.13–5.21 | 0.08 | none | gì Mình học | ba mươi từ | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c03 | 5.76–5.81 | 0.05 | none | ba mươi từ | tiếng Anh đọc | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c03 | 6.20–6.37 | 0.17 | comma | từ tiếng Anh | đọc đi đọc | đúng ký hiệu |
| c03 | 6.48–6.55 | 0.07 | none | tiếng Anh đọc | đi đọc lại | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c03 | 6.79–6.85 | 0.06 | none | đọc đi đọc | lại tới thuộc | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c03 | 7.08–7.13 | 0.05 | none | đi đọc lại | tới thuộc làu | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c03 | 7.34–7.41 | 0.07 | none | lại tới thuộc | làu Sáng dậy | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c03→c04 | 7.72–8.07 | 0.35 | sentence | tới thuộc làu | Sáng dậy mình | đúng ký hiệu |
| c04 | 8.77–8.82 | 0.05 | none | dậy mình gấp | sách viết thử | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c04 | 8.95–9.06 | 0.11 | none | mình gấp sách | viết thử tới | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c04 | 9.16–9.25 | 0.09 | none | gấp sách viết | thử tới từ | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c04→c05 | 9.58–9.77 | 0.19 | comma | sách viết thử | tới từ thứ | đúng ký hiệu |
| c05 | 9.89–9.94 | 0.05 | none | viết thử tới | từ thứ năm | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c05→c06 | 11.65–12.05 | 0.40 | beat | thì mình bí | Một thí nghiệm | đúng ký hiệu |
| c06 | 12.18–12.24 | 0.06 | none | mình bí Một | thí nghiệm năm | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c06→c07 | 13.85–14.04 | 0.19 | comma | năm 2006 thấy | nếu kiểm tra | đúng ký hiệu |
| c07 | 15.29–15.38 | 0.09 | none | thì nhóm đọc | lại làm tốt | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c07 | 15.78–15.86 | 0.08 | none | đọc lại làm | tốt hơn Nhưng | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c07 | 15.96–16.05 | 0.09 | none | lại làm tốt | hơn Nhưng hai | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c07→c08 | 16.30–16.65 | 0.35 | sentence | làm tốt hơn | Nhưng hai ngày | đúng ký hiệu |
| c08 | 17.38–17.55 | 0.17 | comma | hai ngày sau | nhóm tự kiểm | đúng ký hiệu |
| c08 | 17.73–17.78 | 0.05 | none | ngày sau nhóm | tự kiểm tra | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c08→c09 | 19.20–19.59 | 0.39 | beat | nhớ hơn hẳn | Mình cần là | đúng ký hiệu |
| c09 | 20.92–21.06 | 0.14 | comma | sáng hôm sau | gấp sách lại | đúng ký hiệu |
| c09 | 21.38–21.47 | 0.09 | none | sau gấp sách | lại mình vẫn | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c09 | 22.12–22.20 | 0.08 | none | mình vẫn viết | ra được Nên | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c09→c10 | 22.51–22.92 | 0.41 | beat | viết ra được | Nên mình chia | đúng ký hiệu |
| c10 | 23.28–23.33 | 0.05 | none | Nên mình chia | ba mươi từ | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c10 | 23.84–23.89 | 0.05 | none | ba mươi từ | thành ba phần | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c10 | 24.63–24.81 | 0.18 | comma | thành ba phần | mỗi phần mười | đúng ký hiệu |
| c10 | 25.37–25.43 | 0.06 | none | mỗi phần mười | từ Học hết | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c10→c11 | 25.66–26.00 | 0.34 | sentence | phần mười từ | Học hết phần | đúng ký hiệu |
| c11 | 26.12–26.18 | 0.06 | none | mười từ Học | hết phần nào | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c11 | 26.32–26.40 | 0.08 | none | từ Học hết | phần nào mình | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c11 | 26.82–27.00 | 0.18 | comma | hết phần nào | mình gấp sách | đúng ký hiệu |
| c11 | 27.44–27.52 | 0.08 | none | mình gấp sách | viết lại phần | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c11 | 27.63–27.69 | 0.06 | none | gấp sách viết | lại phần đó | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c11 | 27.92–27.98 | 0.06 | none | sách viết lại | phần đó chỗ | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c11→c12 | 28.44–28.60 | 0.16 | comma | lại phần đó | chỗ nào bí | đúng ký hiệu |
| c12→c13 | 29.86–30.25 | 0.39 | beat | mới mở sách | Nhóm của Yang | đúng ký hiệu |
| c13 | 30.85–30.90 | 0.05 | none | Nhóm của Yang | tổng hợp 222 | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c13 | 31.24–31.30 | 0.06 | none | Yang tổng hợp | 222 nghiên cứu | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c13→c14 | 32.75–32.95 | 0.20 | comma | 222 nghiên cứu | thấy lớp có | đúng ký hiệu |
| c14 | 33.25–33.35 | 0.10 | none | cứu thấy lớp | có kiểm tra | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c14 | 33.44–33.50 | 0.06 | none | thấy lớp có | kiểm tra nhỏ | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c14 | 34.25–34.33 | 0.08 | none | tra nhỏ thì | điểm cao hơn | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c14 | 35.15–35.25 | 0.10 | none | cao hơn lớp | không làm kiểm | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c14 | 35.61–35.66 | 0.05 | none | lớp không làm | kiểm tra nhỏ | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c14 | 36.37–36.56 | 0.19 | comma | kiểm tra nhỏ | ở mức vừa | đúng ký hiệu |
| c14 | 36.76–36.86 | 0.10 | none | nhỏ ở mức | vừa Sáng hôm | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c14→c15 | 37.20–37.59 | 0.39 | beat | ở mức vừa | Sáng hôm sau | đúng ký hiệu |
| c15 | 37.97–38.14 | 0.17 | comma | Sáng hôm sau | sách vẫn gấp | đúng ký hiệu |
| c15 | 38.44–38.53 | 0.09 | none | hôm sau sách | vẫn gấp mình | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c15→c16 | 38.83–39.01 | 0.18 | comma | sách vẫn gấp | mình tự viết | đúng ký hiệu |
| c16 | 39.93–40.03 | 0.10 | none | tự viết được | luggage đúng chữ | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c16 | 40.19–40.36 | 0.17 | comma | viết được luggage | đúng chữ hành | đúng ký hiệu |
| c16 | 41.49–41.54 | 0.05 | none | lý hôm trước | mình bí Còn | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c16→c17a | 42.00–42.39 | 0.39 | beat | trước mình bí | Còn bạn thử | đúng ký hiệu |
| c17a | 42.89–43.06 | 0.17 | comma | bí Còn bạn | thử gấp sách | đúng ký hiệu |
| c17a | 43.48–43.59 | 0.11 | none | thử gấp sách | lại thì viết | ghi nhận (<0,12s; thường là âm tắc/khép miệng) · trong cụm «gấp sách lại thì» nhưng <0,12s |
| c17a | 44.13–44.18 | 0.05 | none | lại thì viết | được mấy từ | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c17a | 44.29–44.35 | 0.06 | none | thì viết được | mấy từ Comment | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c17a | 44.54–44.61 | 0.07 | none | viết được mấy | từ Comment con | ghi nhận (<0,12s; thường là âm tắc/khép miệng) |
| c17a→c17b | 44.89–45.23 | 0.34 | sentence | được mấy từ | Comment con số | đúng ký hiệu |

## Nghe kiểm tra kỹ (STT model nhỏ < 0,9 → chạy lại bằng whisper medium float32 trên đúng đoạn)

| Chunk | Lời | STT small | STT medium | Kết luận |
|---|---|---|---|---|
| c01 | Học thuộc tối qua, sáng dậy quên sạch? | Học thuật tối qua sáng dậy quên sạch (0.875, take c01-37 trước đó) | Học thuộc tối qua sáng dậy quên sạch (1.0) | ĐẠT. Medium nghe đúng «Học thuộc … quên sạch». Đổi take c01-71 vì take này chỉ cần nâng +1,5 st ở «sạch» (đo lên +0,8 st); các take khác cần ≥2,5 st và khi đó medium nghe «quên xác/xạc» (thanh nặng bị đẩy thành sắc). |
| c03 | Mình học ba mươi từ tiếng Anh, đọc đi đọc lại tới thuộc làu. | Mình học 30 từ tiếng Anh, đọc đi đọc lại tới thuộc Lào (0.929) | Mình học 30 từ tiếng Anh, đọc đi đọc lại tới thuộc Lào. (0.929) | Cần nghe tai 1 chữ: «thuộc làu» ra «thuộc Lào» ở cả small lẫn medium (làu là từ hiếm, gần âm với Lào). Các chữ còn lại khớp. Không có take nào STT ra «làu» (7 take). |
| c13 | Nhóm của Yang tổng hợp 222 nghiên cứu, | (v16c s09) «220 .2» | Nhóm của Giang tổng hợp 222 nghiên cứu (1.0) | ĐẠT. Medium ra «Nhóm của Giang tổng hợp 222 nghiên cứu»: «222» được đọc đủ «hai trăm hai mươi hai» (STT tự đổi về chữ số). «Yang» đọc theo phiên âm đã duyệt «Giang». |
| c16 | mình tự viết được luggage, đúng chữ hành lý hôm trước mình bí. | lắc ghịch (take thô, sim 1.0) | Mình tự viết được lắc gịch đúng chữ hành lý hôm trước mình bí. (0.929) | Cần nghe tai: tiếng Việt medium ra «lắc gịch» (đúng phiên âm), STT tiếng Anh trên đúng đoạn chữ đó ra «Good luck, good!», chưa ra «luggage». |
| c17a | Còn bạn, thử gấp sách lại thì viết được mấy từ? | …gấp sắt lại thì viết được máy từ (0.818–0.864) | Còn bạn, thử gấp sách lại thì viết được mấy tư. (0.955) | ĐẠT ngưỡng 0,9 (0,955), cần nghe tai chữ cuối: câu hỏi phải lên giọng ≥0,5 st; «từ» (thanh huyền) phải nâng +4 st mới đạt (đo +0,92 st), medium nghe thành «mấy tư». Thử 4 take khác ở +1,5…3 st đều ra «tờ/tư». Xung đột giữa luật lên giọng câu hỏi và thanh huyền, nhờ Rule Reviewer quyết. |
| c17b | Comment con số nha. | Con mê/Còn mình còn số nha (0.5–0.6) | Comment con số nha! (1.0) | ĐẠT. Take c17b-101o (chữ nhập gốc «Comment», R6 cho phép). Whisper medium vi và en đều ra «Comment con số nha». |

## Không đạt (cờ chặn)

- (không có)

## Cảnh báo

- (không có)
