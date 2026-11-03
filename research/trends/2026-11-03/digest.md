---
title: "Trend digest 2026-11-03"
source: "pipeline/scripts/trend-collect.py + X MCP extra (Apify unavailable)"
id: trends-2026-11-03
type: trend-digest
status: draft-needs-review
updated: 2026-11-03
tags: [trends, digest, daily]
date: 2026-11-03
collector: pipeline/scripts/trend-collect.py + X MCP
skill: trend-digest v4
---
# Trend digest 2026-11-03 (thứ Ba)

**Nguồn:** 33/36 collector ok. Lỗi: kym-memes (HTTP 403), wiki-vi + wiki-en (HTTP 404, ngày thứ 19). vnexpress-sohoa lỗi SSL EOF ở lần chạy đầu; chạy lại cả collector một lần thì ok. **X MCP: có chạy.** Trends VN 20 mục («Thứ 3», «Thứ Ba», «Sáng», «Chào»… là móc giờ; còn lại là fandom Thái, $GLYPH). Worldwide 20 mục (Nhật, WWE, NFL; không dùng được). Thêm 40 story X News từ 4 query (productivity habits, AI at work, Gen Z Vietnam, self improvement motivation; max_age 72h). Tất cả gộp vào `x-extra.json` (80 mục), bản rút gọn trong `x-raw/`.
**Apify TikTok-native: không chạy, vẫn hết hạn mức.** Kiểm rẻ 1 lần (`clockworks/tiktok-scraper`, hashtag `thoiquen`, resultsPerPage 5, commentsPerPost 0) bị từ chối: “Your remaining usage of $0.132525 this billing cycle isn't enough for this run”. Không có run id, 0 clip. Xem `apify/README.md`.
**Số lượng:** collector 466 thô → 448 cụm. raw.json có 448 mục: 277 ok · 14 caution · 157 drop (102 drop tay). **291 qua lọc.** Chấm tay 30 mục; mục chưa soát giới hạn fit ≤0,4; YT niche chỉ làm bằng chứng pattern. Drop tay: chính trị/chính sách (Olympia bị so sánh với chào kiểu phát xít, quan hệ quốc phòng, cấm nhập máy cũ, chủ trương thưởng Tết của lãnh đạo TP.HCM), tội phạm (trốn trại giam, tham ô, lừa sổ tiết kiệm), bệnh và claim y khoa (ung thư, đột quỵ, ADHD, ăn ít sống lâu, ngủ đủ giảm cân), vàng/chứng khoán/Binance, tâm linh («đi chùa online»), tử vi, đời tư/ngoại hình người nổi tiếng.
Dữ liệu: `collect.json`, `collect.log`, `x-extra.json`, `x-raw/`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `apify/README.md`.

## Top 10 (đã lọc)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | «Người xung quanh đang thầm mong bạn làm tốt»: người phỏng vấn mong bạn trả lời tốt, người hẹn mong buổi tối vui, khán giả mong nội dung hay | 0.753 | 1.0 / 0.0 | [X News 02/11](https://x.com/i/trending/2117361072449765528) | 3.21 (clip-20) | LIGHT |
| 2 | Rục rịch thưởng Tết: lao động trẻ mong nhận từ tháng 11–12 để chia nhỏ khoản chi, có người tính «dành dụm một khoản dự phòng» | 0.612 | 1.0 / 0.0 | [Thanh Niên 03/11](https://thanhnien.vn/ruc-rich-chuyen-thuong-tet-lao-dong-tre-mong-som-doanh-nghiep-can-nhac-185261102221425143.htm) | 5.27 (caution) | DARK |
| 3 | #trusttheprocess30days: mỗi ngày đăng một cảnh quay ngắn, cuối tháng 11 ghép 30 cảnh thành một câu chuyện, coi trọng đều đặn hơn hoàn hảo | 0.544 | 1.0 / 0.05 | [X News 03/11](https://x.com/i/trending/2116920006264898004) | 4.12 (format clip-30) | LIGHT |
| 4 | «Đầu óc tỉnh táo là tài sản bị định giá thấp nhất»: chuyển màn hình trắng đen, tắt thông báo không cần (số «bớt 20 phút/ngày» chỉ từ tóm tắt, chưa tự kiểm) | 0.449 | 1.0 / 0.2 | [X News 01/11](https://x.com/i/trending/2116805922794443189) | 3.1 (củng cố B-thongbao-01) | DARK |
| 5 | «Run your own race», đừng so hậu trường của mình với highlight của người khác (claim lo âu/trầm cảm chỉ từ tóm tắt, không dùng) | 0.369 | 1.0 / 0.3 | [X News 02/11](https://x.com/i/trending/2117185449966047489) | 3.20 (clip-22, bão hoà ngày 5) | DARK |
| 6 | «Ai cũng dành gần 1/3 cuộc đời trên giường»: tuổi 30 đổi cách tiêu tiền, nâng cấp thứ dùng mỗi ngày (bài có màu quảng cáo ga giường) | 0.354 | 1.0 / 0.17 | [Kenh14 02/11](https://kenh14.vn/ai-cung-danh-gan-1-3-cuoc-doi-tren-giuong-dieu-thuc-su-khien-toi-nghi-khac-di-ve-chuyen-tieu-tien-215261102210016517.chn) | 4.14 (củng cố B-muathoigian-01) | — |
| 7 | Thử thách không điện thoại ở NYU: «Hopefully that sticks» (mới đọc tiêu đề) | 0.328 | 1.0 / 0.15 | [Washington Square News qua Google News](https://news.google.com/rss/articles/CBMijwFBVV95cUxQdzJZREl4eVRsakM4RUczMTc0YXhKYVlrUjNFNDNFNS1wakJ6UjFuaDNva25RVEF2bFhTbERDU2hESDBITlNURnEtYWdoWG9tckZmS190Sk0wREV1RzR0ZkIzcDdfZnlWRmJtSzI4bkpaV05CUzRJQ1ZBY3M3bjJLbjlaZi02ODhfYTB3Nkd4OA?oc=5) | 4.15 / 3.1 (bằng chứng) | — |
| 8 | Thợ sửa iPhone khuyên tắt thông báo cho đỡ hao pin (ngày 2) | 0.264 | 0.5 / 0.45 | [X News 01/11](https://x.com/i/trending/2116895165457875038) | 3.1 (B-thongbao-01, đã có stub) | DARK |
| 9 | Video picnic công ty chia hai phe về đời 9-5 (ngày 2) | 0.214 | 1.0 / 0.2 | [X News 02/11](https://x.com/i/trending/2116695189918019785) | 4.18 (B-commute-03) | — |
| 10 | Hai kiểu cuối tuần va nhau: nhà ngủ nướng và nhà 6h sáng đã dọn dẹp chạy việc | 0.193 | 0.5 / 0.25 | [X News 01/11](https://x.com/i/trending/2116850383804883427) | 3.2 (chưa bridge) | — |

Đã xem và bỏ khỏi top dù có điểm: phong bì cưới 500K vs mâm cỗ 3,5 triệu (Kenh14; dễ chê người); «không làm nail, ăn ngoài ≤50k/ngày» (tiết kiệm cực đoan, dễ so); kỹ sư 10 năm «chạy đua với AI đến kiệt sức» (AI ở chỗ làm bão hoà, gần nhãn sức khoẻ); «niềm tin từ cha mẹ và vợ/chồng» (dễ thành áp lực gia đình); «đi chùa online» (tâm linh); bông hoa chưa nở (ngày 8, sat 0.95); brain stacking (ngày 9); X VN «Thứ Ba»/«Sáng» (chỉ móc giờ).

## TikTok signals
Hôm nay không có dữ liệu Apify. Dưới đây là proxy từ báo và X, không có view/comment/transcript tự đo nên không xếp hạng:
| keyword | nguồn | tín hiệu | brand-safe? | bridge |
|---|---|---|---|---|
| #trusttheprocess30days | [X News 03/11](https://x.com/i/trending/2116920006264898004) | thử thách quay mỗi ngày một cảnh trong tháng 11, nhiều creator đang đăng (lời tóm tắt, chưa tự kiểm số người) | ok: chỉ mượn khung «mỗi ngày một mảnh», không dùng clip/nhạc của người khác | B-30canh-01 → clip-30 / 4.12 |
| bông hoa chưa nở (biến hình) | Google News «trend TikTok» (Tuổi Trẻ, Tin tức 24h) | vẫn lên báo, có bài «bẻ lái» (lời báo) | ok nếu tự trào bằng thói quen | clip-06 (script v1 chờ chốt); bão hoà |
| «đi chùa online» | Google News «trend TikTok» (Vietnam.vn) | «hút 600.000 người» (lời báo, chưa tự kiểm) | drop: tâm linh | — |
| ferritin face, Earl Grey breakfast, bedazzling | Google News US | không khớp kênh / claim sức khoẻ | bỏ | — |

## Learning
- Không thêm P-row. Câu «mọi người đang thầm mong bạn làm tốt» khớp P03 (mọi người nói X, sách nói thêm Y) + P10. Thưởng Tết khớp P05 (mốc mùa). Thử thách 30 ngày khớp P08 + F04. P03/P05/P08/P10 +1, F04 +1.
- Mục 3.21 (spotlight effect + liking gap) lần đầu có trend bắc vào. Đây là trend LIGHT, khớp đúng đăng #20 (LIGHT) trong theme map.
- Mốc mùa tiền cuối năm bắt đầu: thưởng Tết (11–12), mùa cưới (phong bì). Từ nay tới Tết sẽ còn nhiều tin kiểu này. Chỉ dùng góc tự quản tiền của mình, không so lương hay chê người.
- X VN hôm nay vẫn chỉ có móc giờ và fandom. Tín hiệu đáng dùng đến từ X News và báo đời sống.
- Bão hoà nên tránh: so sánh / run your own race (ngày 5: chọn bình yên, growth over envy, others' wins), bông hoa chưa nở (ngày 8), brain stacking (ngày 9), AI ở chỗ làm, tắt thông báo (ngày 2, đã có stub, chỉ dùng làm bằng chứng thêm).

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-mongbantot-01 | «người xung quanh thầm mong bạn làm tốt» | báo cáo tới con số thứ ba thì đọc nhầm, câu sau nói nhỏ hẳn, tối về vẫn tua lại | 3.21 (Gilovich 2000 + Boothby 2018, mức B) | "Cả mạng đang chia nhau một câu: người phỏng vấn mong bạn trả lời tốt, người hẹn bạn mong buổi tối vui. Vậy sao vừa nói vấp trong cuộc họp, bạn lại thấy cả phòng đang nhìn mình?" (P03+P10) | contrarian / data | clip-20 (3.21) hook trend | LIGHT |
| B-thuongtet-01 | rục rịch thưởng Tết | thưởng chưa về, giỏ hàng đã có vé xe, quà biếu, điện thoại mới | 5.27 (mức C) | "Thưởng Tết năm nay đang rục rịch về sớm, nhiều người mong nhận từ tháng mười một cho kịp mua sắm. Tiền chưa về, bạn đã chia nó cho mấy món rồi?" (P05+P03) | empathy / contrarian | 5.27 hook thay thế không người nổi tiếng (cạnh B-tietkiem-01) | DARK |
| B-30canh-01 | #trusttheprocess30days | đầu tháng hứa mỗi ngày một việc nhỏ, lỡ ngày thứ tư là bỏ luôn cả tháng | 4.12 (Lally 2010, mức B) | "Có người đang rủ nhau mỗi ngày quay một cảnh ngắn, hết tháng ghép lại thành một bộ phim. Thử làm vậy với một thói quen nhỏ của bạn, lỡ một ngày cũng không sao." (P08+F04) | empathy | clip-30 (tổng kết, LIGHT) format / callback 4.12 | LIGHT |

Cầu nối về trục kênh (luật 26/10): trend chỉ là cái móc ở hook. Thông điệp mỗi bridge là một việc nhỏ làm được hôm nay. B-mongbantot-01: lần tới nói vấp thì chia đôi cảm giác «ai cũng thấy» rồi nói tiếp câu sau. B-thuongtet-01: cộng ra chi tiêu cố định một tháng, viết lên giấy. B-30canh-01: chọn một việc nhỏ làm mỗi ngày, ghi một dòng, cuối tháng đọc lại.

## Differentiation
- **B-mongbantot-01**: Mọi người đang nói: người phỏng vấn, người hẹn, khán giả đều thầm mong bạn làm tốt, nên đừng sợ ([X News 02/11](https://x.com/i/trending/2117361072449765528)). Góc của mình: câu đó mới đúng một nửa. Sách 3.21 (mức B) đưa hai thí nghiệm. Gilovich 2000: người mặc áo in hình một ca sĩ đoán 46% người trong phòng nhận ra, thật ra chỉ 23%, tức đoán gấp đôi. Boothby 2018: sau khi trò chuyện, người ta thường đoán đối phương thích mình ít hơn thực tế. Sách cũng ghi rõ: lúc bị chấm thật, như phỏng vấn hay đánh giá, thì vẫn phải chuẩn bị. Phần cần giảm chỉ là cảm giác «ai cũng đang nhìn mình» hằng ngày. Đây là nghiên cứu nhỏ trong phòng lab và trường học, chưa có bằng chứng trực tiếp cho chuyện nói sai trong họp, nên voice chỉ nói «đoán gấp đôi», không dùng số như hệ số.
- **B-thuongtet-01**: Mọi người đang nói: nhận thưởng sớm để chủ động mua sắm lúc giá còn dễ chịu, chia nhỏ khoản chi, tránh dồn vào cận Tết ([Thanh Niên 03/11](https://thanhnien.vn/ruc-rich-chuyen-thuong-tet-lao-dong-tre-mong-som-doanh-nghiep-can-nhac-185261102221425143.htm)). Góc của mình: chia sớm thì phần đầu tiên nên vào quỹ dự phòng, và đếm quỹ đó bằng số tháng chi tiêu chứ không bằng số tiền. Sách 5.27 nói thẳng mốc 3–6 tháng là kinh nghiệm chung, chưa tìm thấy nguồn gốc nghiên cứu (mức C). Voice nói đúng như vậy, không gắn «nghiên cứu cho thấy». Không dùng số bảo hiểm tiền gửi của Trung Quốc trong sách.
- **B-30canh-01**: Mọi người đang nói: đăng đều mỗi ngày, quan trọng là đều chứ không cần hoàn hảo ([X News 03/11](https://x.com/i/trending/2116920006264898004)). Góc của mình: cái làm người ta bỏ không phải thiếu hoàn hảo mà là lỡ một ngày rồi nghĩ mình hỏng cả tháng. Sách 4.12 (Lally 2010, mức B): lỡ một lần không làm hỏng quá trình tạo thói quen. Theo ràng buộc Deep Research 30/10, không nêu số ngày tạo thói quen.

## Plan stubs
- `plans/plan-1-ai-cung-mong-ban-lam-tot-chia-doi.json`: ✔ validate 9 cảnh, 64,00s (stub-needs-approval). Trend ở b01 (L-084: thẻ chữ «Người xung quanh đang thầm mong bạn làm tốt · X News 02/11», câu trend nói ở b01). Ví dụ đời thường: báo cáo trong cuộc họp, buổi phỏng vấn, kỳ đánh giá cuối năm. Dẫn chứng có tên, năm, A so với B và kết quả (L-096). Không tên ca sĩ, không nói «sinh viên». Sách 3.21 mức B. Tuần 4, không có Omi.
- `plans/plan-2-thuong-tet-ve-som-quy-du-phong-truoc.json`: ✔ validate 9 cảnh, 62,00s (stub-needs-approval). Trend ở b01 (thẻ chữ «Rục rịch chuyện thưởng Tết · Thanh Niên 03/11»). Ví dụ: vé xe về quê, quà biếu, giỏ hàng, tiền nhà, tiền gửi về nhà. Không có số tiền cụ thể. Sách 5.27 mức C, nói rõ trong voice.
- `check-rules.py --subjects ideas.json`: PASS (L-087).
- Kịch bản thật do OpenCreator Studio viết sau khi Deep Research kiểm fact và Rule Reviewer duyệt.

## Script hooks (cần Hiệp duyệt)
1. "Cả mạng đang chia nhau một câu: người phỏng vấn mong bạn trả lời tốt, người hẹn bạn mong buổi tối vui. Vậy sao vừa nói vấp trong cuộc họp, bạn lại thấy cả phòng đang nhìn mình?" (B-mongbantot-01, 3.21, clip-20, LIGHT)
2. "Thưởng Tết năm nay đang rục rịch về sớm, nhiều người mong nhận từ tháng mười một cho kịp mua sắm. Tiền chưa về, bạn đã chia nó cho mấy món rồi?" (B-thuongtet-01, 5.27, DARK, caution tiền + mức C)
3. "Có người đang rủ nhau mỗi ngày quay một cảnh ngắn, hết tháng ghép lại thành một bộ phim. Thử làm vậy với một thói quen nhỏ của bạn, lỡ một ngày cũng không sao." (B-30canh-01, 4.12, clip-30 format, LIGHT)

## Trạng thái đang chờ
- clip-06: script v1 «bông hoa chưa nở» đã ĐẠT review cuối 31/10 (9a962b9), vẫn chờ Hiệp chốt. Trend bông hoa đã tới ngày 8 (sat 0.95).
- clip-05 v10 r10.2 đã ĐẠT review, chờ Hiệp chốt (theo digest 01/11; hôm nay không thấy commit mới).
- clip-08: có hai hook trend mới gần đây, B-thongbao-01 (02/11, stub) và «mental clarity» (hôm nay, chỉ làm bằng chứng thêm).
- 5.27: B-tietkiem-01 (Musk, script r3 ĐẠT 31/10, mâu thuẫn L-096/mức C chờ Hiệp quyết). Hôm nay thêm B-thuongtet-01 làm hook thay thế không dùng người nổi tiếng. Mâu thuẫn mức C vẫn như cũ.
- 4.9 Dọn liền tay: script r3 ĐẠT review 31/10 (53a01a5), chờ chốt.
- clip-22: B-ghenti-01 chờ fact 3.20. Hook thay thế đang có: B-30tuoi-01, B-yenlang-01, B-dixa-01. Chủ đề so sánh đã bão hoà (ngày 5), nên chọn sớm.
- Ô #27 (LIGHT trống): ứng viên B-thang11-01 (4.8, để dành cho 1/12) và B-muathoigian-01 (4.14). Bài Kenh14 «1/3 cuộc đời trên giường» hôm nay củng cố thêm cho 4.14.
- Apify: hết hạn mức từ 22/10 (còn $0,1325). Theo quyết định của Hiệp ngày 22/10: chờ chu kỳ mới, không nâng gói.

## Safety notes
- B-mongbantot-01: không nêu tên người nổi tiếng trong thread X (Chamath, Pompliano, ZUBY), không nêu tên ca sĩ trên áo trong thí nghiệm. Giữ câu «phỏng vấn/đánh giá thật thì vẫn chuẩn bị» để không thành lời khuyên «đừng lo gì hết».
- B-thuongtet-01: bỏ phần chủ trương và tên lãnh đạo TP.HCM trong bài. Chỉ dùng «thưởng Tết đang rục rịch». Không so mức thưởng, không số tiền, không phải lời khuyên đầu tư. Chưa đủ quỹ thì ưu tiên quỹ, nhưng không bảo ai bỏ quà biếu cha mẹ.
- B-30canh-01: không dùng clip, nhạc hay tên creator của thử thách. Không nêu số ngày tạo thói quen.
- Phong bì cưới, tiết kiệm cực đoan: không bridge (dễ chê người). Ngủ đủ giảm cân, ăn ít sống lâu: claim y khoa, bỏ.
- Chính trị, tội phạm, bệnh, bi kịch, tâm linh, vàng/chứng khoán, đời tư người nổi tiếng: bỏ.
