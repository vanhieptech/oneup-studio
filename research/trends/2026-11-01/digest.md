---
title: "Trend digest 2026-11-01"
source: "pipeline/scripts/trend-collect.py + X MCP extra (Apify unavailable)"
id: trends-2026-11-01
type: trend-digest
status: draft-needs-review
updated: 2026-11-01
tags: [trends, digest, daily, weekly]
date: 2026-11-01
collector: pipeline/scripts/trend-collect.py + X MCP
skill: trend-digest v4
---
# Trend digest 2026-11-01 (Chủ nhật, kèm tổng hợp tuần W44)

**Nguồn:** 33/36 collector ok. Lỗi: kym-memes (HTTP 403), wiki-vi + wiki-en (HTTP 404, ngày thứ 17). **X MCP: có chạy**: trends VN 20 (Halloween, Chủ Nhật, Tháng 11, phim Thái, Binance; chỉ «Tháng 11» dùng được) + worldwide 20 (Halloween, thể thao, Nhật; «Happy New Month» dùng được) + 40 story X News (4 query: productivity habits, AI at work, Gen Z Vietnam, self improvement motivation; max_age 72h) → `x-extra.json` 80 mục, bản gốc trong `x-raw/`.
**Apify TikTok-native: không chạy, vẫn hết hạn mức.** Kiểm rẻ 1 lần (`clockworks/tiktok-scraper`, hashtag `hoctap`, resultsPerPage 5) bị từ chối: “Your remaining usage of $0.132525 this billing cycle isn't enough for this run”. Không có run id, 0 clip. Xem `apify/README.md`.
**Số lượng:** collector 465 thô → 443 cụm; raw.json 443 mục (285 ok · 10 caution · 148 drop, trong đó 130 drop tay) → 295 qua lọc. Chấm tay 30 mục; mục chưa soát giới hạn fit ≤0,4. Mở lại 1 story X bị bộ lọc từ khoá chặn nhầm (growth over envy). Drop tay: chính trị/chiến sự (Ba Lan, Iran, Ukraine, bầu cử Mỹ, nhân sự), tội phạm/bi kịch (Mr Pips, vụ bắn, tai nạn hầm chui, Patrick Stewart qua đời), bệnh và claim y khoa (đột quỵ, thận, ADHD, ferritin), tiền ảo/vàng/chứng khoán (Binance, giá vàng, trading), ngoại tình và đời tư/ngoại hình người nổi tiếng, quảng cáo/cuộc thi, thủ tục hành chính.
Dữ liệu: `collect.json`, `collect.log`, `x-extra.json`, `x-raw/`, `raw.json`, `score.txt`, `week.txt`, `ideas.json`, `plans/`, `apify/README.md`.

## Top 10 (đã lọc)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | Mùng 1 tháng 11: X VN «Tháng 11» top 5, X worldwide «Happy New Month»; Forbes 31/10 «2 thói quen nhỏ để kết tháng vui hơn» (làm xong một việc nhỏ còn dở + kế hoạch nếu–thì) | 0.825 (Forbes 0.526, Happy New Month 0.419) | 1.0 / 0.05 | [X VN](https://x.com/search?q=Th%C3%A1ng%2011), [X WW](https://x.com/search?q=Happy%20New%20Month), [Forbes 31/10](https://www.forbes.com/sites/traversmark/2026/10/31/2-small-habits-to-end-every-month-happier-than-it-began-by-a-psychologist/) | 4.8 (+4.1 callback clip-01) | LIGHT |
| 2 | «Chọn bình yên bằng cách coi như không thấy ồn ào trên mạng» (X News 01/11) + «so sánh lấy mất bình yên, you vs you» (X News 31/10) | 0.560 / 0.509 | 1.0 / 0.1 | [X News 01/11](https://x.com/i/trending/2116684926288322666), [X News 31/10](https://x.com/i/trending/2116541178405679336) | 3.20 (clip-22) | DARK |
| 3 | Bà nội trợ 58 tuổi giữ nhà sạch nhờ xử lý việc nhỏ ngay trong ngày, việc khó dồn một buổi mỗi tuần | 0.509 | 1.0 / 0.1 | [Kenh14 01/11](https://kenh14.vn/58-tuoi-ba-noi-tro-khien-dan-mang-ne-phuc-vi-can-nha-sach-nhu-moi-hoa-ra-chi-giu-5-thoi-quen-don-gian-nay-215261101072938069.chn) | 4.9 (củng cố B-donlientay-01) | LIGHT |
| 4 | Musk «tiết kiệm cho tương lai là vô nghĩa» ngày 2; thêm bài chuyên gia an toàn AI ngừng tiết kiệm hưu trí | 0.384 / 0.326 | 0.5 / 0.35 | [VnExpress](https://vnexpress.net/elon-musk-tiet-kiem-tien-cho-tuong-lai-la-vo-nghia-5138848.html), [CafeBiz 01/11](https://cafebiz.vn/chuyen-gia-an-toan-ai-ngung-tiet-kiem-huu-tri-vi-tin-chac-loai-nguoi-sap-bi-diet-vong-176261031165413584.chn) | 5.27 (B-tietkiem-01, caution) | DARK |
| 5 | Gen Z đầu tiên sắp 30 (cụm millennials 30, ngày 4) | 0.317 | 1.0 / 0.23 | [X News 01/11](https://x.com/i/trending/2116550198352605584) | 3.20 (B-30tuoi-01) | DARK |
| 6 | «Bông hoa chưa nở» ngày 5, rẽ sang nhánh tự trào (Tuổi Trẻ 31/10) | 0.257 / 0.163 | 0.25–0.5 / 0.45–0.95 | [Tuổi Trẻ Cười 31/10](https://cuoi.tuoitre.vn/trend-dung-khinh-thuong-mot-bong-hoa-chua-no-be-lai-kho-ngo-100261031132037316.htm), [Tuổi Trẻ 30/10](https://tuoitre.vn/dung-khinh-thuong-mot-bong-hoa-chua-no-bigbang-gay-sot-cung-loat-xu-huong-ran-ran-coi-mang-100261030233222016.htm) | 4.12 (clip-06, script v1 chờ Hiệp chốt) | DARK |
| 7 | «Clean as you go» ngày 2 | 0.251 | 0.5 / 0.38 | [X News](https://x.com/i/trending/2116206747459420656) | 4.9 (B-donlientay-01) | LIGHT |
| 8 | Xăng giảm từ 0h 1/11 (số trong tiêu đề, chưa tự kiểm) | 0.247 | 1.0 / 0.0 | [CafeBiz 01/11](https://cafebiz.vn/xang-giam-gia-manh-hon-1800-dong-lit-tu-0h-ngay-1-11-176261101062709948.chn) | 5.27 (móc tiền nhỏ, chưa bridge) | — |
| 9 | Lời nhắc «đo tiến bộ bằng bước của mình» ngày 3 | 0.215 | 0.5 / 0.42 | [X News](https://x.com/i/trending/2115788633512817077) | 3.20 (B-ghenti-01) | DARK |
| 10 | Nhân viên văn phòng làm thêm 3 tối/tuần ở nhà (Singapore) | 0.175 | 1.0 / 0.05 | [Kenh14 31/10](https://kenh14.vn/nhan-vien-van-phong-32-tuoi-lam-viec-tai-nha-3-toi-moi-tuan-thu-nhap-ngoai-luong-dat-10-trieu-dong-thang-215261031130346666.chn) | 12.18, caution (tiền) | — |

Đã xem và bỏ khỏi top dù điểm cao: mâm cơm nhà MC Olympia / Lan Khuê (đời tư người nổi tiếng, không bắc được bài học); vợ Mr Hunter «tiền ai nấy giữ» (tranh chấp pháp lý); Halloween (hết hạn); X VN «Chủ Nhật» (chỉ móc giờ); I'm so sorry (ngày 6, sat 1.0); hard things early (ngày 4, sat 0.72); giá điện giảm (chính sách); AI ở chỗ làm (bão hoà).

## TikTok signals
Hôm nay không có dữ liệu Apify. Dưới đây là proxy từ báo, không có view/comment/transcript tự đo nên không xếp hạng:
| keyword | nguồn | tín hiệu | brand-safe? | bridge |
|---|---|---|---|---|
| bông hoa chưa nở, nhánh tự trào | Tuổi Trẻ Cười 31/10, Tuổi Trẻ 30/10, Google News «trend TikTok» | người dùng tự trêu mình bằng màn «nở hoa» không theo khuôn mẫu (lời báo, chưa tự kiểm) | ok nếu tự trào bằng thói quen; bỏ ví dụ cân nặng và ngoại hình trong bài | clip-06 (script v1 đã dùng bông hoa) |
| I'm so sorry (AI photo reveal) | Google News US (Mashable 31/10) | ngày 6 | ok, bão hoà | B-imsorry-01 (cũ) |
| Totem pole, wine, Keon & Kavon | Google News US | không khớp kênh | bỏ | — |

## Learning
- Không thêm P-row. «Tháng 11 / Happy New Month» khớp P05 (seasonal) + P12. «Chọn bình yên» khớp P03 + P15. Nhà sạch nhờ việc nhỏ khớp P10. P03/P05/P10/P12/P15 +1, F04 +1 (bông hoa tự trào).
- Mốc đầu tháng chỉ sống một ngày. Theo bài học 30/10 (mốc mùa cần báo trước ≥7 ngày), hook 1/11 hôm nay đã muộn, nên để dành cho **mùng 1/12** (tháng cuối năm, mạnh hơn) hoặc ô đăng #27 đang trống cần LIGHT.
- «Bông hoa chưa nở» đã bão hoà (sat 0.95 cho bài 31/10). Nếu Hiệp chốt clip-06 v1 thì nên làm sớm. Nhánh tự trào là bằng chứng mới cho góc tự nhận trước (P15), không phải hook mới.
- Bão hoà nên tránh: AI ở chỗ làm, ngủ/Gen Z, I'm so sorry, hard things early (ngày 4).

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-thang11-01 | Tháng 11 / Happy New Month / Forbes | cái hộp đồ định thanh lý nằm góc phòng từ tháng chín; cuộc gọi hỏi chủ nhà chuyện tiền điện hẹn mai hoài | 4.8 (+4.1) | "Mùng một tháng mười một rồi. Bạn có muốn tháng này xong được một việc đã dời từ tháng trước không?" (P05+P15) | empathy / data | ô đăng #27 (LIGHT trống) hoặc ý tưởng mới 4.8; dời sang 1/12 nếu lỡ mốc | LIGHT |
| B-yenlang-01 | chọn bình yên + so sánh lấy mất bình yên | chưa đánh răng đã biết bạn cũ đổi xe | 3.20 | "Cả mạng đang rủ nhau chọn bình yên, coi như không thấy gì hết. Vậy sáng nay vừa mở mắt, bạn đã lướt qua đời bao nhiêu người rồi?" (P03+P15) | contrarian / empathy | clip-22 hook thay thế, cạnh B-ghenti-01 / B-30tuoi-01 | DARK |
| B-donlientay-02 | Kenh14 nhà sạch nhờ việc nhỏ trong ngày | vết bẩn mới lau vài chục giây, để mấy ngày thành cả buổi | 4.9 | "Có người giữ nhà sạch mà không tổng vệ sinh cả ngày Chủ nhật. Bí quyết của họ là cái bạn đang để tới mai." (P10+P03) | empathy | củng cố B-donlientay-01 (script r3 đã ĐẠT review 31/10) | LIGHT |
| B-tietkiem-02 | chuyên gia AI ngừng tiết kiệm hưu trí | nghe «tương lai không cần tiền» rồi bỏ luôn khoản để dành tháng này | 5.27 | (dùng hook B-tietkiem-01) | contrarian | bằng chứng ngày 2 cho B-tietkiem-01 (script r3 ĐẠT, chờ Hiệp quyết mâu thuẫn L-096/mức C) | DARK |

Cầu nối về trục kênh (luật 26/10): trend chỉ là cái móc ở hook. Thông điệp mỗi bridge là một việc nhỏ làm được hôm nay: ghi một dòng «nếu… thì…» có ngày vào lịch điện thoại · tắt một mục gợi ý người quen trên một app · lau vết bẩn lúc nó còn mới · đặt một lệnh chuyển tự động nhỏ.

## Differentiation
- **B-thang11-01**: Mọi người đang nói: chúc tháng mới vui vẻ, hứa «tháng này sẽ khác» ([X VN](https://x.com/search?q=Th%C3%A1ng%2011)); Forbes khuyên kết tháng bằng một việc nhỏ còn dở ([Forbes](https://www.forbes.com/sites/traversmark/2026/10/31/2-small-habits-to-end-every-month-happier-than-it-began-by-a-psychologist/)). Góc của mình: không lập danh sách tháng mới. Chỉ một việc đã dời, cho nó một ngày hạn. Sách 4.8 (Buehler 1994, mức B): có hạn người khác đặt 80,6% xong trước hạn, tự ước chỉ 38,7%. Hạn tự đặt chưa ai đo trực tiếp, sách ghi là suy ra. Hành động lấy 4.1 (mức A). Không dùng claim Zeigarnik của bài Forbes (chỉ từ tóm tắt, chưa tự kiểm).
- **B-yenlang-01**: Mọi người đang nói: chọn bình yên bằng cách coi như không thấy, lo việc mình ([X News](https://x.com/i/trending/2116684926288322666)). Góc của mình: cố coi như không thấy thì vẫn là đã thấy. Sách 3.20 (mức A): chặn từ chỗ nó hiện ra, tắt gợi ý hoặc giới hạn 10 phút mỗi app (Hunt 2018). Phần phân tích gộp chỉ là tương quan, nói rõ trong voice. Không dùng nhãn bệnh.
- **B-donlientay-02**: Mọi người đang nói: khen người giữ nhà sạch là chăm ([Kenh14](https://kenh14.vn/58-tuoi-ba-noi-tro-khien-dan-mang-ne-phuc-vi-can-nha-sach-nhu-moi-hoa-ra-chi-giu-5-thoi-quen-don-gian-nay-215261101072938069.chn)). Góc của mình: không phải chăm hơn, mà làm lúc việc còn chưa kịp khó chịu (4.9, Steel 2007, mức A). «Vài chục giây so với hàng chục phút» là lời bài báo, không phải số của sách, không vào voice.

## Plan stubs
- `plans/plan-1-thang-11-mot-viec-co-ngay-han.json`: ✔ validate 9 cảnh, 58,00s (stub-needs-approval). Trend ở b01 (L-084: thẻ «Tháng 11 · X VN 01/11» + «Happy New Month», chỉ chữ). Ví dụ đời thường: hộp đồ thanh lý, gọi chủ nhà về tiền điện, lịch điện thoại. Sách 4.8 mức B + 4.1 mức A.
- `plans/plan-2-chon-binh-yen-bot-luot-doi-nguoi.json`: ✔ validate 9 cảnh, 57,00s (stub-needs-approval). Trend ở b01 (thẻ «Choosing peace · X News 01/11»). Ví dụ: điện thoại buổi sáng, bạn cũ đổi xe, cài đặt app. Sách 3.20 mức A.
- `check-rules.py --subjects ideas.json`: PASS (L-087).
- Kịch bản thật do OpenCreator Studio viết sau khi Deep Research kiểm fact và Rule Reviewer duyệt.

## Script hooks (cần Hiệp duyệt)
1. "Mùng một tháng mười một rồi. Bạn có muốn tháng này xong được một việc đã dời từ tháng trước không?" (B-thang11-01, 4.8, LIGHT; đổi thành «mùng một tháng mười hai» nếu đăng 1/12)
2. "Cả mạng đang rủ nhau chọn bình yên, coi như không thấy gì hết. Vậy sáng nay vừa mở mắt, bạn đã lướt qua đời bao nhiêu người rồi?" (B-yenlang-01, clip-22, DARK)
3. "Có người giữ nhà sạch mà không tổng vệ sinh cả ngày Chủ nhật. Bí quyết của họ là cái bạn đang để tới mai." (B-donlientay-02, 4.9, LIGHT)

## Trạng thái đang chờ
- clip-06: script v1 «bông hoa chưa nở» đã ĐẠT review cuối 31/10 18:40 (giờ VN), commit 9a962b9, đang chờ Hiệp chốt. Hook thay thế vẫn còn: B-kiennhan-01 (Justin Welsh), B-maxxing-01 (không nêu số ngày). Trend bông hoa đã bão hoà (sat 0.95), nên chốt thì làm sớm.
- 5.27 Musk (B-tietkiem-01) và 4.9 Dọn liền tay (B-donlientay-01): script r3 ĐẠT review 31/10 (53a01a5), Musk còn mâu thuẫn L-096/mức C chờ Hiệp.
- clip-22: B-ghenti-01 chờ fact 3.20. Có thêm B-30tuoi-01 và B-yenlang-01 làm hook thay thế.

## Safety notes
- B-thang11-01: không dùng phần «quy định mới tháng 11» (chính sách). Số 80,6%/38,7% là số sách (mẫu sinh viên, không nói trong voice), Deep Research kiểm.
- B-yenlang-01: không «trầm cảm», «lo âu» trong voice; nói rõ là tương quan; Allcott là người dùng Mỹ trước bầu cử 2018, không dùng.
- Bông hoa tự trào: bỏ ví dụ cân nặng và ngoại hình trong bài báo; không tên/ảnh người nổi tiếng.
- Chuyên gia AI ngừng tiết kiệm: bỏ phần «diệt vong», chỉ dùng như bằng chứng có tranh luận tiền.
- Chính trị, tội phạm, bệnh, bi kịch, tiền ảo/vàng: bỏ.
