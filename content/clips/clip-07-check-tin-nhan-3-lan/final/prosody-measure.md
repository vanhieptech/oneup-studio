---
title: "Clip 07 Prosody Measure"
date: 2026-11-28
id: clip-07.prosody-measure
type: report
status: ready
updated: 2026-11-28
tags: [clip-07, prosody]
source: "pipeline/scripts/prosody-check.py"
---

# Prosody đo thật — clip-07-final (voice c07v1)

Nghỉ = đoạn lặng dài nhất (năng lượng) giữa hai từ khớp; giữa câu/beat = khoảng lặng thật giữa hai file giọng theo timing.json. Lên giọng = trung vị F0 từ cuối so với phần trước (semitone).

| Câu (key) | bắt đầu–kết thúc (s) | Chỗ ngắt theo plan: đo / mục tiêu | Ngắt giữa cụm | Nghỉ sau câu: đo / mục tiêu | Nhấn (đậm): dB so phần còn lại | Âm tiết/s | Câu hỏi lên giọng (st) | STT (sim) | Kết luận |
|---|---|---|---|---|---|---|---|---|---|
| Sếp nhắn đúng hai chữ. (c07v1-b01) | 0.12–1.66 | — | không | 0.34/0.4–0.8 (giữa beat) ⚠ lệch mục tiêu | — | 4.67 | — | Xếp nhắn đúng 2 chữ. (0.6) | ok |
| em ơi, rồi im luôn (c07v1-b01a) | 1.74–3.12 | «ơi,» 0.18/0.15-0.25 | không | 0.36/0.4–0.8 (giữa beat) | — | 6.76 | — | Em ơi! Rồi im luôn! (1.0) | ok |
| mười phút mình mở máy coi năm lần. (c07v1-b01b) | 3.2–5.31 | — | không | 0.78/0.4–0.8 (giữa beat) | — | 5.23 | — | 10 phút mình mở máy coi 5 lần. (0.75) | ok |
| Hông riêng bữa đó đâu. (c07v1-b02) | 5.81–7.16 | — | không | 0.6/0.4–0.8 (giữa beat) | — | 5.15 | — | Hồng riêng bữa đó đâu? (1.0) | ok |
| Ngày thường cứ thấy chấm đỏ, là tay mình tự chụp máy. (c07v1-b02a) | 7.57–10.88 | «đỏ,» 0.15/0.15-0.25 | không | 0.66/0.4–0.8 (giữa beat) | — | 5.06 | — | Ngày thường cứ thấy chấm đỏ là tay mình tự chụp máy. (1.0) | ok |
| Tối về đầu nặng trịch, việc chính còn nguyên, mình lại tự trách sao dễ phân tâm quá. (c07v1-b02b) | 11.28–16.2 | «nguyên,» 0.26/0.15-0.25 | không | 0.9/0.4–0.8 (giữa beat) | — | 5.03 | — | Tối về đầu nặng trịt, việc chính còn nguyên, mình lại tự trách sao dễ phân tâm quá. (0.94) | ok |
| Tắt chuông cũng thua. (c07v1-b03) | 16.9–18.15 | — | không | 0.65/0.4–0.8 (giữa beat) | — | 5.8 | — | Tắt chuông cũng thua. (1.0) | ok |
| Mình vẫn lén bật màn hình coi, sợ việc gấp người ta kiếm hông ra. (c07v1-b03a) | 18.55–22.61 | «coi,» 0.25/0.15-0.25 | không | 0.6/0.4–0.8 (giữa beat) | — | 4.93 | — | Mình vẫn lén bật màn hình coi, sợ việc gấp người ta kiếm hông ra. (1.0) | ok |
| Ủa mà canh liền tay vậy, mình đỡ trễ việc hay chỉ căng đầu thêm? (c07v1-b03b) | 23.01–27.04 | «vậy,» 0.22/0.15-0.25 | không | 0.95/0.4–0.8 (giữa beat) ⚠ lệch mục tiêu | — | 5.21 | 3.6 | Ủa mà canh liền tay vậy, mình đỡ trái việc hay chỉ căn đầu thêm? (0.87) | ok |
| Nhóm Cu lép năm hai ngàn mười lăm đo trên i meo nè: (c07v1-b04) | 27.74–30.76 | — | không | 0.64/0.4–0.8 (giữa beat) | — | 5.08 | — | nhóm Culep năm 2015 đo trên e -mail nè. (0.45) | ok |
| tuần gom còn ba lần một ngày, so với thả cửa hơn mười lăm lần, căng thẳng giảm rõ mức vừa phải. (c07v1-b04a) | 31.16–37.34 | «ngày,» 0.15/0.15-0.25; «lần,» 0.26/0.15-0.25 | không | 0.98/0.4–0.8 (giữa beat) ⚠ lệch mục tiêu | — | 4.55 | — | Tuần góm còn ba lần một ngày so với thả cửa hơn 15 lần, căng thẳng giảm rõ mức vừa phải. (0.93) | ok |
| Số i meo nhận với trả lời vẫn y như cũ. (c07v1-b05) | 38.04–40.78 | — | không | 0.65/0.4–0.8 (giữa beat) | — | 5.0 | — | số e -mail nhận với trả lời vẫn y như cũ. (0.82) | ok |
| Nghe vậy tự nhiên nhẹ hẳn cái vai, hóa ra mình hông yếu, chỉ tại mở ra đóng vô cả ngày nên đầu căng hà. (c07v1-b05a) | 41.19–47.92 | «vai,» 0.28/0.15-0.25 ✖ phẩy dài hơn chấm (>0.27s); «yếu,» 0.22/0.15-0.25 | không | 0.93/0.4–0.8 (giữa beat) ⚠ lệch mục tiêu | — | 4.38 | — | Nghe vậy tự nhiên nhẹ hẳn cái vai, hóa ra mình không yếu, chỉ tại mở ra đóng vô cả ngày nên đầu căn hà. (0.92) | **ĐỌC LẠI** |
| Từ đó mình đổi luật, báo trước với tim, việc gấp thì gọi nha. (c07v1-b06) | 48.61–52.56 | «luật,» 0.25/0.15-0.25; «tim,» 0.05/0.15-0.25 ✖ phẩy dính (<0.12s) | không | 0.6/0.4–0.8 (giữa beat) | — | 5.13 | — | Từ đó mình đổi luật báo trước với tim việc gấp thì gọi nha. (1.0) | **ĐỌC LẠI** |
| Còn tin nhắn cứ gom đúng ba khung giờ, chín giờ sáng, một giờ trưa, bốn giờ chiều, mở một lượt rồi xử gọn. (c07v1-b06a) | 52.97–60.25 | «chiều,» 0.27/0.15-0.25 | không | 0.95/0.4–0.8 (giữa beat) ⚠ lệch mục tiêu | — | 4.48 | — | Còn tin nhắn cứ gồm đúng 30 giờ, 9 giờ sáng, 1 giờ trưa, 4 giờ chiều, mở một lượt rồi xử gọn. (0.81) | ok |
| Mình gỡ kiểu đó thôi, chứ mỗi chỗ làm mỗi khác. (c07v1-b07) | 60.95–63.88 | «thôi,» 0.24/0.15-0.25 | không | 0.66/0.4–0.8 (giữa beat) | — | 4.98 | — | Mình gỡ kiểu đó thôi, chứ mỗi chỗ là mỗi khác. (0.91) | ok |
| Có ai cũng hay canh chấm đỏ giống mình hông? (c07v1-b07a) | 64.28–66.74 | — | không | 0.67/0.4–0.8 (giữa beat) | — | 5.15 | 0.67 | Có ai cũng hay kênh chấm đỏ giống mình không? (0.8) | ok |
| Hay bạn nghĩ sao, có cách gì né cảnh đó, còm men kể mình nghe với nha. (c07v1-b07b) | 67.14–71.44 | «sao,» 0.28/0.15-0.25 ✖ phẩy dài hơn chấm (>0.27s) | không | — | — | 5.57 | — | Hay bạn nghĩ sao? Có cách gì nế cảnh đó? Còn men kể mình nghe với nha! (0.94) | **ĐỌC LẠI** |

Cờ chặn: 3
- c07v1-b05a: sau «vai,» nghỉ 0.28s (✖ phẩy dài hơn chấm (>0.27s))
- c07v1-b06: sau «tim,» nghỉ 0.05s (✖ phẩy dính (<0.12s))
- c07v1-b07b: sau «sao,» nghỉ 0.28s (✖ phẩy dài hơn chấm (>0.27s))
