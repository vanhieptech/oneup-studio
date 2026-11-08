# Review clip-05 r7 (51a669c) — Rule Reviewer, 29/10/2026 15:2x

**Verdict: CHƯA ĐẠT.** Máy: 7/7 mode PASS (cảnh báo: --flow b03/b05, --link 5/13 cặp). Cổng tay L-094 (bảng cặp câu) chặn. Chỉ liệt kê lỗi; OpenCreator sửa (L-093b). r7 là vòng 1 sau viết lại nên được vá, chưa phải viết lại cả bài.

## Bảng cặp câu của Rule Reviewer
| Cặp | Kết quả | Lỗi |
|---|---|---|
| S1→S2 | ✔ | |
| S2→S3 | ✘ R1 | «khó dùng tới» thiếu tân ngữ (dùng cái gì?) — lặp lỗi «dùng được» của r6.12. «nhất là khi trên mạng đang bàn…» không phải lý do làm chuyện quên nặng hơn → trend vẫn là câu gắn vào, không nối nhân quả. |
| S3→S4 | ✘ R2 | «Vậy» không rút ra từ S3 (S3 nói hệ quả của quên, S4 hỏi nguyên nhân). Đổi động từ «đọc» (S1) → «xem» (S4) làm người nghe tưởng là hành động khác. |
| S4→S5 | ✔ | Câu hỏi được trả lời ngay. |
| S5→S6 | ✘ R3 | «cách của bạn nhớ hơn» — hơn nhóm nào? Vừa nêu ba nhóm, người nghe không biết đang so với «đọc một lần». |
| S6→S7 | ✘ R4 | «Sau hai ngày» — hai ngày sau mốc nào? Nhóm một tuần được kiểm tra hai ngày sau lần xem lại, không phải hai ngày sau lần đọc đầu; câu không nói. «cách cuối» bắt người nghe nhớ thứ tự liệt kê. (Chờ Deep Research.) |
| S7→S8 | ✘ R5 | «chỉ giữ chốc lát» không khớp mốc dẫn chứng: dữ liệu là «ngay sau thì hơn, hai ngày thì hết hơn», không phải «chốc lát» (L-094: lời rút ra phải đúng mốc dẫn chứng). |
| S8→S9 | ✘ R6 | Thiếu bước: chưa câu nào bảo «để cách ra rồi mới xem lại», đã nói «không cần chờ đủ một tuần». «cẩm nang» xuất hiện lần đầu không dẫn vào (nhân vật/nguồn mới, L-094). «chỉ khuyên» nghe như hạ thấp nghiên cứu vừa nói. |
| S9→S10 | ✘ R7 | Không nói tự kể làm lúc nào (sau vài hôm, lúc quay lại?) → mất mốc thời gian, người nghe có thể tự kể ngay. «chỗ bạn hụt là tự kể» gọi lại S2 quá xa và lủng củng khi nghe một lần (L-091). |
| S10→S11 | ✔ | «Cách… này» gọi lại. Claim «nhiều nghiên cứu khuyên dùng» chờ Deep Research (nghiên cứu không «khuyên»). |
| S11→S12 | ✔ | Quay về cảnh S2; cảnh báo --link là báo nhầm. |
| S12→S13, S13→S14 | ✔ | |

## Lỗi khác
- R8 (caption ≤8 chữ): b03 «Read once, reread right away, or a week later» = 9 chữ.
- R9 (caption khớp lời): b04 «A few days is enough advice» sai nghĩa, không khớp S9; b03 «rereading wins» cùng lỗi R3 (thắng ai).
- R10 (L-091 nghe một lần): S5 nhồi ba nhóm vào một câu 23 chữ ngay sau câu hỏi — cân nhắc tách, OpenCreator tự quyết cách.

## Còn chờ
- Deep Research soát fact S7 (mốc hai ngày của nhóm một tuần), S9 (23.15), S11 (F5).
- Rủi ro báo Hiệp khi đạt: tín hiệu trend yếu (bài X News gốc mất, không có comment TikTok), quota Apify hết, spec/hình chưa dựng.
