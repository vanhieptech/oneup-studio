# Review clip-05 r7.3 (3b48efd) — Rule Reviewer, 29/10/2026 15:4x (heartbeat)

**Verdict: CHƯA ĐẠT.** Đây là vòng vá thứ 3 trên bản viết lại r7 → theo L-094 (≥3 vòng vá) **yêu cầu OpenCreator viết lại cả bài**, không vá tiếp. Rule Reviewer chỉ liệt kê lỗi kèm dòng (L-093b), không viết câu thay.

## Máy (7/7 mode PASS)
--subjects ✔ · --trend ✔ · --l088 ✔ · --repeat ✔ (G3 đã hết) · --clarity ✔ · --flow ⚠ b03 mở beat (chấm tay: «đúng chuyện này» nối được) · --link ⚠ 5/13 (b01→b01, b02→b03, b04→b04, b05→b06, b06→b06; chấm tay: báo nhầm). Mode mặc định cần final/spec.json, chưa dựng (chưa Chốt).

## Đã xử lý ở r7.3
- G2: S9 có tân ngữ «việc ôn»; caption b04 «Spread your review over days». ✔
- G3: không còn cụm 3 chữ lặp. ✔
- G1: S3 đã mở bằng «Quên như vậy» — xem H1, mối nối sang trend vẫn chưa đạt.

## Bảng cặp câu (L-094, chấm tay)
| Cặp | Nối nhờ | Kết quả |
|---|---|---|
| S1→S2 | hệ quả thời gian «Vài hôm sau» | ✔ |
| S2→S3 | «Quên như vậy» gọi lại S2 | ✔ vế đầu; ✖ vế trend (H1) |
| S3→S4 | «quên» lặp, «Hai lần» gọi lại S1 | ✔ |
| S4→S5 | «đúng chuyện này» báo câu trả lời | ✔ |
| S5→S6→S7→S8 | liệt kê ba nhóm, «Kiểm tra ngay», «Nhưng» | ✔ |
| S8→S9 | «cũng» | ✖ H2 |
| S9→S10 | «Mỗi lần ôn» | ✖ H3 (hành động mới không lý do) |
| S10→S11 | «Cách… này» | ✔ |
| S11→S12 | «Nhờ vậy», quay về «có ai hỏi» | ✔ |
| S12→S13→S14 | CTA tự kể, «chương», «nhớ» | ✔ |

## Lỗi
| Id | Câu (dòng) | Lỗi | Luật |
|---|---|---|---|
| H1 | S3 (dòng 25, 54) | Một câu 22 chữ ôm hai ý: hệ quả của quên + trend. Trend gắn bằng «mà», người nghe phải tự suy ra «đọc nhiều mà quên thì cũng chẳng giúp viết». Đây là lần thứ 3 chỗ nối này bị bắt (R1, G1). | L-091 (một ý/câu), L-092, L-094 |
| H2 | S8→S9 (dòng 26–27, 59–60) | Dẫn chứng vừa nêu mốc «một tuần», lời khuyên chuyển sang «vài ngày» không có câu nối; «cũng khuyên» ngụ ý nghiên cứu đã khuyên, trong khi S5–S8 chỉ nêu kết quả. «Cẩm nang sống đáng giá» là nguồn mới đưa vào chỉ bằng chữ «cũng». | L-094 (lời khuyên đúng mốc dẫn chứng; nguồn mới phải dẫn vào) |
| H3 | S10 (dòng 27, 61) | Hành động «gấp sách kể trước, mở ra xem sót» chưa hề có trong chuỗi S1–S9 (nghiên cứu chỉ nói về lúc đọc lại) và không có lý do vì sao phải tự kể — đúng kiểu lỗi L-094 ghi cho r6.12. Mối nối duy nhất là chữ «kể» ở S2, quá xa. | L-094 |
| H4 | Bảng cặp câu (dòng 39, 43), «Tự soát» (dòng 91), «Chuỗi lý lẽ» (dòng 22) | Trích chữ không còn trong lời: «có đọc nhiều… cũng khó dùng», «Vì vậy», «vì chỗ bạn hụt là tự kể». Bảng cặp câu phải dùng đúng chữ đang có trong script. | L-094 |

## Yêu cầu
OpenCreator viết lại cả bài (r8), giữ fact_lock fact-package-v5 + cẩm nang 23.15/23.14, giữ trend b02; dựng chuỗi lý lẽ từ câu đầu tới CTA trước rồi mới viết câu; bảng cặp câu khớp từng chữ với lời. Deep Research soát fact sau khi có r8. Chưa Chốt, không giọng/render.

## Rủi ro (báo Hiệp khi đạt)
Tín hiệu trend yếu (bài X News gốc mất, chưa có comment TikTok), quota Apify hết, spec/hình chưa dựng.
