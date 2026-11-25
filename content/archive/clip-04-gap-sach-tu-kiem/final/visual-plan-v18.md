---
title: "Clip 04 v18 — bảng minh hoạ chi tiết (FLUX Visual)"
date: 2026-10-20
type: visual-plan
tags: [clip-04, visual, v18]
source: "final/script-v18-LOCKED.md, final/script-v18-table.md"
status: ready
rules: không chữ trong hình (L-050), nghĩa qua vật/hành động, không mặt người giả, nhân vật phải x≈0.72, props trái y≤1400, 1 hiệu ứng chính/beat; không ảnh AI trong video
---

## Nhịp hình (nguồn)
- Clip TikTok dạng thông tin chạy tốt đổi hình khoảng 0,33 lần/giây, tức ~3 giây một lần (cắt, zoom, vật mới); nhanh hơn nữa thì người xem bỏ giữa chừng nhiều hơn ([Dost & Huang 2026](https://archives.marketing-trends-congress.com/2026/pages/PDF/paper_professor_DOST_HUANG.pdf)).
- Vật chuyển động chỉ đúng chỗ đang nói giúp mắt theo kịp ([Dynamic signals, Applied Cognitive Psychology](https://doi.org/10.1002/acp.3973)).
→ Clip ~49 s: khoảng 15–17 lần đổi hình. Mỗi beat có 1 hiệu ứng chính; các nhịp con bên dưới là hành động của vật/nhân vật, không phải thêm hiệu ứng.

## Vật xuyên suốt (để người xem nhận ra ngay)
- **Cái vali nhỏ** = chữ "hành lý / luggage". Không viết chữ, chỉ vẽ vali.
- **Tờ giấy 10 dòng + cây bút**: cùng một tờ ở b01, b02, b04, b07.
- **Cửa sổ trăng → mặt trời**: thay mốc "tối qua / sáng hôm sau / +2 ngày" (không dùng lịch có chữ số).

## Từng beat
| Beat | Nhịp con (~3 s/lần) | Ghi chú kiểm |
|---|---|---|
| b01 Hook 0–5 | (1) Cận tờ giấy trắng, bút đang dừng giữa không trung. (2) Cửa sổ sau lưng: mặt trời mọc; sách gấp bên trái; nhân vật nhìn thẳng, sững. | Title trên cùng phải đủ dấu (lỗi v14). |
| b02 Ví dụ 5–12 | (1) Cửa sổ có trăng, đèn bàn bật, sách mở, trang lật nhanh 3 lần, nhân vật gật tự tin. (2) Cắt sang sáng: sách gấp, bút viết 4 dòng nét nguệch ngoạc (không đọc được chữ). (3) Dòng 5: hiện bóng mờ cái vali rồi tan, bút khựng, «bí». | Nét viết là đường mực, không ra chữ thật. |
| b03 Nguyên nhân 12–19 | (1) Hai nhóm hình tròn không mặt: trái cầm sách mở, phải cầm giấy+bút. (2) Mốc "ngay": thanh trái cao hơn, nhóm trái giơ ngón cái. (3) Mặt trời mọc 2 lần trên cửa sổ, thanh phải vượt hẳn, ngón cái nhóm trái xìu xuống. | Không số trên thanh; tên tác giả chỉ ở caption nguồn. |
| b04 Mục tiêu 19–23 | (1) Về tờ giấy b02, mặt trời mọc 1 lần, sách vẫn gấp. (2) Push nhẹ vào dòng 5 còn trống. | Bỏ "mũi tên tới sáng hôm sau" nếu có chữ. |
| b05 Cách làm 23–31 | (1) 30 thẻ trắng xổ ra rồi gom thành 3 xấp. (2) Lấy xấp 1, gấp sách, bút viết; đặt dấu tích không chữ lên xấp. (3) Tới chỗ bí: sách mở đúng một trang, liếc, gấp lại ngay. | Thẻ trắng, không chữ. Sách chỉ mở 1 lần. |
| b06 Bằng chứng 31–38 | (1) Chồng tài liệu cao dần (gợi 222 nghiên cứu, không cần đếm đủ). (2) Hai thanh điểm, thanh "có kiểm tra nhỏ" (gắn icon tờ quiz nhỏ) cao hơn vừa phải, tay nhân vật chỉ vào. | Chênh lệch vừa, không phóng đại. |
| b07 Kết quả 38–43 | (1) Cùng tờ giấy, mặt trời ngoài cửa sổ, sách gấp. (2) Bút viết liền dòng 5, cái vali hiện rõ, đặc màu, nảy nhẹ. (3) Nhân vật cười nhẹ. | Phải khớp khung b01/b02 (cùng góc, cùng tờ). |
| b08 CTA 43–47 | (1) Nhân vật nhìn camera, gấp sách lại. (2) Tay chỉ xuống vùng comment, bút đặt cạnh tờ giấy. | — |
| end 47–49 | End card tĩnh, credit + dòng an toàn. | — |

## Thumbnail / cover (template A, Cover.tsx)
- Ảnh chính: tờ giấy với dòng 5 trống + bóng vali mờ, sách gấp, bút dừng; nhân vật bên phải sững.
- Chữ lớn do template A đặt (không vẽ chữ vào ảnh). Đề xuất chữ cover cho Production chọn: «Tối thuộc, sáng quên?»
- Một bản dùng chung cho TikTok/Reels/Shorts 1080×1920; Threads/Instagram feed cắt 1080×1350 giữ tờ giấy + nhân vật ở giữa.

## Cập nhật theo bộ xu hướng (Social Research, research/tiktok-trend-pack-study-2026-10-20.md)
- Nhịp đổi hình rút xuống 2–3 s/lần.
- Thẻ đố từ (sửa theo Rule Reviewer/OpenCreator): b02 chỉ có tấm thẻ trắng úp với bóng vali mờ; caption b02 giữ đúng «Stuck at word five», không chữ «L», không ô trống; nếu cần nhãn trên thẻ tối đa «Hành lý → ?». b07 thẻ lật ngửa thành vali rõ + dấu tích, caption mới được hiện «luggage ✓». Không vẽ chữ khác vào hình (L-050).
- b03 ngón cái xìu xuống chỉ là hình; caption/mô tả không thêm ý «tự tin» hay «nhớ kém».
- Ghi chú phạm vi (Deep Research kiểm): nhịp ~3 s lấy từ 50 clip talking-head TikTok kênh Đức + thí nghiệm 242 người, bài hội thảo, không phải hoạt hình → mốc tham khảo, không phải luật cứng.
