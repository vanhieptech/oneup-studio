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

# Prosody đo thật — clip-07-final (voice c07v2)

Nghỉ = đoạn lặng dài nhất (năng lượng) giữa hai từ khớp; giữa câu/beat = khoảng lặng thật giữa hai file giọng theo timing.json. Lên giọng = trung vị F0 từ cuối so với phần trước (semitone).

| Câu (key) | bắt đầu–kết thúc (s) | Chỗ ngắt theo plan: đo / mục tiêu | Ngắt giữa cụm | Nghỉ sau câu: đo / mục tiêu | Nhấn (đậm): dB so phần còn lại | Âm tiết/s | Câu hỏi lên giọng (st) | STT (sim) | Kết luận |
|---|---|---|---|---|---|---|---|---|---|
| Sếp nhắn đúng hai chữ (c07v2-b01) | 0.12–1.42 | — | không | 0.27/0.4–0.8 (giữa beat) ⚠ lệch mục tiêu | — | 5.21 | — | Xếp nhắn đúng 2 chữ. (0.6) | ok |
| em ơi, rồi im luôn. (c07v2-b01a) | 1.5–2.73 | — | không | 0.33/0.4–0.8 (giữa beat) ⚠ lệch mục tiêu | — | 7.69 | — | Em rồi im luôn (0.89) | ok |
| mười phút mình mở máy coi năm lần. (c07v2-b01b) | 2.8–4.69 | — | không | 0.78/0.4–0.8 (giữa beat) | — | 5.88 | — | 10 phút mình mở máy coi 5 lần. (0.75) | ok |
| Hông riêng bữa đó đâu. (c07v2-b02) | 5.21–6.52 | — | không | 0.63/0.4–0.8 (giữa beat) | — | 5.49 | — | Hồng riêng bữa đó đâu? (1.0) | ok |
| Ngày thường cứ thấy chấm đỏ, là tay mình tự chụp máy. (c07v2-b02a) | 6.92–9.9 | «đỏ,» 0.14/0.15-0.25 | không | 0.59/0.4–0.8 (giữa beat) | — | 5.36 | — | Ngày thường cứ thấy chấm đỏ là tay mình tự chụp máy. (1.0) | ok |
| Tối về đầu nặng trịch, việc chính còn nguyên, mình lại tự trách sao dễ phân tâm quá. (c07v2-b02b) | 10.3–14.99 | «nguyên,» 0.32/0.15-0.25 ✖ phẩy dài hơn chấm (>0.27s) | không | 0.98/0.4–0.8 (giữa beat) ⚠ lệch mục tiêu | — | 5.41 | — | Tối về đầu nặng trịt, việc chính còn nguyên, mình lại tự trách sao dễ phần tâm quá." (0.94) | **ĐỌC LẠI** |
| Tắt chuông cũng thua. (c07v2-b03) | 15.69–16.87 | — | không | 0.6/0.4–0.8 (giữa beat) | — | 5.88 | — | Tắt chuông cũng thua. (1.0) | ok |
| Mình vẫn lén bật màn hình coi, sợ việc gấp người ta kiếm hông ra. (c07v2-b03a) | 17.27–21.02 | «coi,» 0.25/0.15-0.25 | không | 0.6/0.4–0.8 (giữa beat) | — | 5.68 | — | Mình vẫn lén bật mạng hình coi, sợ việc gấp người ta kiếm hông ra. (0.93) | ok |
| Ủa mà canh liền tay vậy, mình đỡ trễ việc hay chỉ căng đầu thêm? (c07v2-b03b) | 21.42–25.13 | «vậy,» 0.29/0.15-0.25 ✖ phẩy dài hơn chấm (>0.27s) | không | 0.9/0.4–0.8 (giữa beat) | — | 5.7 | 4.26 | Ủa mà canh liền tay vậy, mình đỡ trễ việc hay chỉ căn đầu thêm? (0.93) | **ĐỌC LẠI** |
| Nhóm Cu lép năm hai ngàn mười lăm đo trên i meo nè: (c07v2-b04) | 25.83–28.52 | — | không | 0.61/0.4–0.8 (giữa beat) | — | 5.91 | — | Nhóm Culep năm 2015 đo trên e -mail nè. (0.45) | ok |
| tuần gom còn ba lần một ngày, so với thả cửa hơn mười lăm lần, căng thẳng giảm rõ mức vừa phải. (c07v2-b04a) | 28.92–34.41 | «ngày,» 0.12/0.15-0.25; «lần,» 0.27/0.15-0.25 | không | 0.94/0.4–0.8 (giữa beat) ⚠ lệch mục tiêu | — | 5.24 | — | Tuần gom còn ba lần một ngày so với thả cửa hơn 15 lần, căng thẳng giảm rõ mức vừa phải. (0.93) | ok |
| Số i meo nhận với trả lời vẫn y như cũ. (c07v2-b05) | 35.12–37.45 | — | không | 0.63/0.4–0.8 (giữa beat) | — | 6.04 | — | số email nhận với trả lời vẫn y như củ. (0.86) | ok |
| Nghe vậy tự nhiên nhẹ hẳn cái vai, hóa ra mình hông yếu, chỉ tại mở ra đóng vô cả ngày nên đầu căng hà. (c07v2-b05a) | 37.84–43.72 | «vai,» 0.22/0.15-0.25; «yếu,» 0.24/0.15-0.25 | không | 0.89/0.4–0.8 (giữa beat) | — | 5.02 | — | Nghe vậy tự nhiên nhẹ hẳn cái vai, hóa ra mình không yếu, chỉ tại mở ra đóng vô cả ngày nên đầu căn hà. (0.92) | ok |
| Từ đó mình đổi luật, báo trước với tim, việc gấp thì gọi nha. (c07v2-b06) | 44.42–47.81 | «luật,» 0.25/0.15-0.25 | không | 0.65/0.4–0.8 (giữa beat) | — | 6.19 | — | Từ đó mình đổi luật báo trước với team việc gấp thì gọi nha. (0.93) | ok |
| Còn tin nhắn cứ gom đúng ba khung giờ, chín giờ sáng, một giờ trưa, bốn giờ chiều, mở một lượt rồi xử gọn. (c07v2-b06a) | 48.21–54.64 | «chiều,» 0.27/0.15-0.25 | không | 0.9/0.4–0.8 (giữa beat) | — | 5.15 | — | Còn tin nhắn cứ gom đúng ba khung giờ, 9h sáng, 1h trưa, 4h chiều. Mở một lượt rồi sử gọn. (0.76) | ok |
| Mình gỡ kiểu đó thôi, chứ mỗi chỗ làm mỗi khác. (c07v2-b07) | 55.34–58.02 | «thôi,» 0.22/0.15-0.25 | không | 0.66/0.4–0.8 (giữa beat) | — | 5.53 | — | Mình gỡ kiểu đó thôi, chứ mỗi chỗ làm mỗi khác. (1.0) | ok |
| Có ai cũng hay canh chấm đỏ giống mình hông? (c07v2-b07a) | 58.42–60.73 | — | không | 0.62/0.4–0.8 (giữa beat) | — | 5.43 | 0.38 | Có ai cũng hay canh chấm đỏ giống mình không? (0.9) | **ĐỌC LẠI** |
| Hay bạn nghĩ sao, có cách gì né cảnh đó, còm men kể mình nghe với nha. (c07v2-b07b) | 61.13–65.07 | «sao,» 0.1/0.15-0.25 ✖ phẩy dính (<0.12s) | không | — | — | 5.76 | — | Hay bạn nghĩ sao có cách gì nét cảnh đó? Còn men kể mình nghe với nha! (0.88) | **ĐỌC LẠI** |

Cờ chặn: 4
- c07v2-b02b: sau «nguyên,» nghỉ 0.32s (✖ phẩy dài hơn chấm (>0.27s))
- c07v2-b03b: sau «vậy,» nghỉ 0.29s (✖ phẩy dài hơn chấm (>0.27s))
- c07v2-b07a: câu hỏi cuối 0.38 st (✖ không lên giọng)
- c07v2-b07b: sau «sao,» nghỉ 0.1s (✖ phẩy dính (<0.12s))
