---
title: "Trend digest 2026-10-29"
source: "pipeline/scripts/trend-collect.py + X MCP extra (Apify unavailable)"
id: trends-2026-10-29
type: trend-digest
status: draft-needs-review
updated: 2026-10-29
tags: [trends, digest, daily]
date: 2026-10-29
collector: pipeline/scripts/trend-collect.py + X MCP
skill: trend-digest v4
---
# Trend digest 2026-10-29 (Thứ Năm)

**Nguồn:** 33/36 collector ok. Lỗi: kym-memes (HTTP 403), wiki-vi + wiki-en (HTTP 404, ngày thứ 14). vnexpress-doisong lỗi SSL (`UNEXPECTED_EOF_WHILE_READING`) ở lần chạy 1, chạy lại thì ok (số trên là lần 2). **X MCP: có chạy**, trends VN 30 (“Thứ 5/Thứ Năm”, “Chào/Sáng”, quảng cáo Thái, crypto; chỉ móc giờ là dùng được) + worldwide 30 (chính trị Brazil, bóng đá, Nhật; bỏ hết) + 38 story X News (4 query: productivity habits, AI at work, Gen Z Vietnam, sleep phone morning routine; max_age 72h) → `x-extra.json` 98 mục.
**Apify TikTok-native: không chạy, vẫn hết hạn mức.** Kiểm rẻ 1 lần (`clockworks/tiktok-scraper`, hashtag `hoctap`, resultsPerPage 5) bị từ chối: “Your remaining usage of $0.132525 this billing cycle isn't enough for this run”. Chu kỳ chưa reset. Không run id, 0 clip. Xem `apify/README.md`.
**Số lượng:** collector 479 thô → 458 cụm; raw.json 458 mục (329 ok · 17 caution · 112 drop, gồm 68 drop tay) → 346 qua lọc. Chấm tay 18 mục. Drop tay: chính trị (Brazil, Putin, Obama, FCC, Greenland, Ventura), tội phạm/lừa đảo, bi kịch/tai nạn (人身事故, thợ mỏ, sinh tồn), bệnh và claim y khoa (đột quỵ, ung thư, truyền trắng, ferritin face, ADHD), thiên tai (gió giật cấp 9), tâm linh (con giáp), scandal showbiz, tiền ảo, và một bài nêu tên môn học (L-087).
Dữ liệu: `collect.json`, `collect.log`, `x-extra.json`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `apify/README.md`.

## Top 10 (đã lọc; bỏ mục heuristic lạc đề như nhện sói, carbon removal, MacBook OLED)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | Phim ngắn AI “chủ tịch giả nghèo”, “tổng tài bá đạo” dừng ở cao trào; người xem thức tới gần 3h sáng; báo gọi “thối não” | 0.949 | 1.0 / 0.07 | [VnExpress 28/10](https://vnexpress.net/thoi-nao-vi-nghien-phim-ngan-ai-5136786.html) | 4.15 + 3.9 (clip-10) | LIGHT |
| 2 | “Overthinking isn’t thinking too much. It’s thinking without deciding.” | 0.573 | 1.0 / 0.05 | [X News](https://x.com/i/trending/2115434315777789983) | 3.14 (clip-24) | LIGHT |
| 3 | Dữ liệu Apple Watch: giờ ngủ trung bình ở Mỹ ~23:37, ngủ ~6h40 (số chưa tự kiểm) | 0.465 | 1.0 / 0.23 | [X News](https://x.com/i/trending/2115476763782291480) | 3.2 + 3.9 (clip-14) | DARK |
| 4 | Justin Welsh: ráng nhiều năm với việc mình ghét, bỏ việc riêng sau vài tháng | 0.420 | 1.0 / 0.05 | [X News](https://x.com/i/trending/2115525365678711129) | 4.12 (clip-06) | DARK |
| 5 | “No.” với lời khuyên chờ 60–90 phút mới uống cà phê sáng | 0.381 | 1.0 / 0.10 | [X News](https://x.com/i/trending/2115105229792293192) | 3.4 (clip-17) | DARK |
| 6 | 3 câu nghe như quan tâm mà làm bạn thấy có lỗi | 0.292 | 1.0 / 0.0 | [Kenh14 28/10](https://kenh14.vn/co-3-cau-noi-nghe-nhu-quan-tam-nhung-thuc-chat-dang-khien-ban-cam-thay-co-loi-215261028071748312.chn) | 3.16, caution | — |
| 7 | “Không ai đọc hết sách PDF” | 0.283 | 1.0 / 0.17 | [X News](https://x.com/i/trending/2114973689565294784) | gần clip-04/05, dễ lặp | — |
| 8 | Giải mã thói quen tự cản trở bản thân (ngày 3) | 0.258 | 0.5 / 0.40 | [VnExpress](https://vnexpress.net/giai-ma-thoi-quen-tu-can-tro-ban-than-5137355.html) | 4.9 (B-tucantro-01) | DARK |
| 9 | “I’m So Sorry”: slideshow gỡ từng lớp chỉnh sửa ảnh (ngày 4) | 0.181 | 0.25 / 0.88 | [Know Your Meme](https://knowyourmeme.com/memes/im-so-sorry-tiktok-trend), [Her Campus 27/10](https://www.hercampus.com/culture/how-to-im-so-sorry-trend-tiktok-without-ai/), [Mashable 23/10](https://me.mashable.com/digital-culture/77568/what-is-tiktoks-im-so-sorry-trend-the-ai-photo-reveals-explained) | 3.1 (clip-08) | DARK |
| 10 | Trà sữa “điếu cày” chai dài ~700ml | 0.126 | 1.0 / 0.0 | [Kenh14 29/10](https://kenh14.vn/tra-sua-dieu-cay-dang-gay-sot-binh-cu-ruou-moi-cuoc-dua-ban-trai-nghiem-cua-nganh-do-uong-215261029000358297.chn) | chưa có mục khớp | — |

Đã xem và bỏ: ADHD habits (nhãn chẩn đoán), Gen Z “thriving” thấp kỷ lục và Millennials burnout (sức khoẻ tâm thần, dễ than thở), AI ở chỗ làm (bão hoà, nỗi sợ mất việc), giáo sư bỏ chấm bài vì AI (nêu tên môn, L-087), lương và lạm phát (caution tiền, dễ thành bình luận chính sách), Tesla tuyển người ở VN (người nổi tiếng/thương hiệu), brain stacking (ngày 5, sat 0.97), thứ Hai mệt và social jetlag (ngày 4).

## TikTok signals
Không có dữ liệu Apify hôm nay. Proxy tin tức, không có view/comment/transcript tự đo nên không xếp hạng:
| keyword | nguồn | tín hiệu | brand-safe? | bridge |
|---|---|---|---|---|
| Phim ngắn AI “chủ tịch giả nghèo” | VnExpress (ảnh chụp app phim ngắn) | báo lớn viết riêng một bài; số trong bài: 29% trong khảo sát 1.000+ độc giả VnExpress thường bị cuốn vào phim ngắn AI, lượt tải app phim ngắn ở VN quý IV/2025 +271% (Adjust) | caution: bỏ phần bệnh viện tâm thần, chữ “nghiện” và claim về não | B-phimngan-01 |
| “I’m So Sorry” slideshow | Google News “trend TikTok” (Her Campus), KYM, Mashable | KYM: bắt đầu 8/2026, bùng 10/2026; theo KYM, bài gốc của @theywanthunter có hơn 25,6 triệu view (chưa tự kiểm trên TikTok) | ok nếu chỉ dùng chibi, không ảnh trẻ em thật, không AI ảnh người thật | B-imsorry-01 |
| Brain stacking | Google News US (Mashable, KXAN) | ngày 5 | ok, bão hoà | B-brainstack-01 (cũ) |
| Ferritin face, skull cap | Google News US | trend sức khoẻ/ngoại hình | drop | — |

## Learning
- Thêm **P16 Edit-reveal confession** + **F09 slideshow gỡ từng lớp** (KYM, Her Campus, Mashable). Từ 25/10 đến 27/10 mình bỏ trend này vì “không khớp kênh”. Hôm nay map được sang 3.1: thứ bị giấu trong ảnh là cái điện thoại.
- P01/P03/P04/P10/P11/P12/P15 +1 (patterns.md).
- Tín hiệu VN mạnh nhất hôm nay là phim ngắn AI dạng cliffhanger. Móc này cụ thể và nhìn thấy được (thẻ tựa phim “chủ tịch giả nghèo”, khung “còn tiếp”), hợp L-084.
- Bão hoà nên tránh: brain stacking (ngày 5), mệt mỏi và giấc ngủ cuối tháng 10 trên X (ngày 3–4), AI ở chỗ làm.

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-phimngan-01 | phim ngắn AI | dặn lòng xem thêm một tập, ngẩng lên gần 3h sáng | 4.15 (+3.9) | "Tập “chủ tịch giả nghèo” tối nay dừng ngay khúc gay cấn? Kệ nó, cắm sạc điện thoại ngoài phòng khách rồi đi ngủ." (P01+P15) | empathy / contrarian | clip-10 (4.15) | LIGHT |
| B-kiennhan-01 | ráng việc mình ghét, bỏ việc riêng | việc không thích ráng ba năm, ly nước sau bữa sáng ba tuần đã lơ | 4.12 | "Công việc mình không thích thì ráng được ba năm, mà thói quen mới mới ba tuần chưa thấy gì đã muốn bỏ?" (P03+P10) | contrarian / humor | clip-06 (4.12), thay thế B-bonghoa-01 | DARK |
| B-imsorry-01 | “I’m So Sorry” | góc làm việc “siêu tập trung”, gỡ từng lớp thì lộ điện thoại úp cạnh laptop | 3.1 | "Đây là góc làm việc siêu tập trung của mình… gỡ ra từng lớp nha. I’m so sorry." (P16+P15) | humor / self-own | clip-08 (3.1) | DARK |
| B-overthink-01 | overthinking = nghĩ mà không chốt | nằm nghĩ đi nghĩ lại một chuyện mà chưa chốt | 3.14 | "“Overthinking không phải nghĩ nhiều, mà là nghĩ mà không chốt.” Lần tới thấy mình nghĩ vòng vòng, đứng dậy rửa cái ly trước đã." (P03) | contrarian / empathy | clip-24 (3.14) | LIGHT |
| B-bedtime-01 | giờ ngủ Apple Watch + mệt cuối tháng 10 | định ngủ sớm, đặt điện thoại xuống thì đã quá nửa đêm | 3.2 (+3.9) | "Tối qua mấy giờ bạn mới chịu đặt điện thoại xuống? Thử ghi lại giờ đó bảy ngày liền." (P12) | data / empathy | clip-14 (3.2) | DARK |
| B-caphesang-01 | “No.” với chờ cà phê sáng | cả feed cãi chờ 90 phút, ly 3 giờ chiều không ai nhắc | 3.4 | "Cả mạng đang cãi sáng dậy phải chờ chín mươi phút mới được uống cà phê. Mà ly đáng lo là ly lúc ba giờ chiều." (P11+P03) | contrarian | clip-17 (3.4) | DARK |

Cầu nối về trục kênh (rule 26/10): trend chỉ là cái móc ở hook. Thông điệp mỗi bridge là một việc nhỏ làm được hôm nay: cắm sạc ngoài phòng khách · làm lại thói quen đúng một lần · cất điện thoại khỏi tầm mắt · đứng dậy làm một việc phải động tay · ghi giờ đặt máy xuống · dời ly cà phê chiều.

## Differentiation
- **B-phimngan-01**: Mọi người đang nói phim ngắn AI làm “thối não”, bào mòn trí nhớ, nên phải cai ([VnExpress](https://vnexpress.net/thoi-nao-vi-nghien-phim-ngan-ai-5136786.html)). Góc của mình: không hù chuyện não, không bắt bỏ phim. Cái mất đo được là giờ ngủ, và việc nhỏ nhất làm được tối nay là đổi chỗ cắm sạc. Tập phim thì sáng mai vẫn còn, giấc ngủ đêm nay mất là mất luôn. Tự nhận trước (P15): mình cũng từng xem “thêm một tập”. Chuyện thật của Hiệp: [CẦN HIỆP XÁC NHẬN].
- **B-kiennhan-01**: Mọi người đang nói mình kiên nhẫn với việc mình ghét mà bỏ việc riêng quá nhanh, nên cho dự án riêng thời gian dài hơn ([X News](https://x.com/i/trending/2115525365678711129)). Góc của mình: đem chính sự kiên nhẫn đó áp vào một thói quen nhỏ. Sách (4.12) nói thói quen tính theo tháng: 18–254 ngày, và lỡ một lần không ảnh hưởng đáng kể. Không nói chuyện nghỉ việc hay khởi nghiệp.
- **B-imsorry-01**: Mọi người đang dùng trend này để thú nhận ảnh hồi nhỏ hoặc đồ hoá trang Halloween ([KYM](https://knowyourmeme.com/memes/im-so-sorry-tiktok-trend), [Mashable](https://me.mashable.com/digital-culture/77568/what-is-tiktoks-im-so-sorry-trend-the-ai-photo-reveals-explained)). Góc của mình: thứ bị “photoshop” đi là cái điện thoại. Sách (3.1, Ward 2017) nói điện thoại chỉ cần nằm cạnh, kể cả khi mình nhịn được không xem, cũng làm giảm phần sức nghĩ còn dùng được.
- **B-overthink-01**: Mọi người đang chia sẻ câu trích và mẹo “worry period” ([X News](https://x.com/i/trending/2115434315777789983)). Góc của mình: không đặt lịch lo âu, mà đứng dậy làm một việc phải động tay. Sách (3.14) ghi rõ “đổi việc” là kinh nghiệm của tác giả; tài liệu chỉ đỡ được ý “đánh lạc hướng tốt hơn cứ nghĩ vòng vòng”.
- **B-caphesang-01**: Mọi người đang cãi nhau chuyện chờ 90 phút mới uống cà phê sáng ([X News](https://x.com/i/trending/2115105229792293192)). Góc của mình: ly sáng không phải ly đáng lo, mốc trong sách là sau 2 giờ chiều (3.4).

## Plan stubs
- `plans/plan-1-phim-ngan-sac-phong-khach.json`: ✔ validate 9 cảnh, 57,00s (stub-needs-approval). Trend ở b01 (L-084: thẻ tựa “chủ tịch giả nghèo” dừng ở “còn tiếp”). Ví dụ đời thường (giường, đi làm sớm, cục sạc, phòng khách), không môn học (`check-rules.py --subjects` PASS). Dẫn chứng b04 (Exelmans & Van den Bulck 2016, 844 người lớn, nghiên cứu tương quan) do Deep Research kiểm. Không dùng Carter 2016 (trẻ em) và số Trung Quốc.
- `plans/plan-2-ghet-viec-van-ra-thoi-quen-bo.json`: ✔ validate 9 cảnh, 57,00s (stub-needs-approval). Đây là hook thay thế cho clip-06, chạy theo ràng buộc Deep Research 27/10 (18–254 ngày, lỡ một lần; không dùng 66 ngày). Ví dụ ly nước sau bữa sáng, không dùng ví dụ dậy sớm. `check-rules.py --subjects` PASS.
- Kịch bản thật do OpenCreator Studio viết sau khi Deep Research kiểm fact và Rule Reviewer duyệt.

## Script hooks (cần Hiệp duyệt)
1. "Tập “chủ tịch giả nghèo” tối nay dừng ngay khúc gay cấn? Kệ nó, cắm sạc điện thoại ngoài phòng khách rồi đi ngủ." (B-phimngan-01, clip-10, LIGHT)
2. "Công việc mình không thích thì ráng được ba năm, mà thói quen mới mới ba tuần chưa thấy gì đã muốn bỏ?" (B-kiennhan-01, clip-06, DARK, thay thế bông hoa)
3. "Đây là góc làm việc siêu tập trung của mình… gỡ ra từng lớp nha. I’m so sorry." (B-imsorry-01, clip-08, DARK)
4. "“Overthinking không phải nghĩ nhiều, mà là nghĩ mà không chốt.” Lần tới thấy mình nghĩ vòng vòng, đứng dậy rửa cái ly trước đã." (B-overthink-01, clip-24, LIGHT)

## Safety notes
- B-phimngan-01: bài gốc có bệnh viện tâm thần, mất ngủ kéo dài, đau đầu, chữ “nghiện”. Không dùng phần nào trong số đó. Không nói dopamine hay “não thối”. Thẻ tựa phim là tựa giả, không dùng hình phim thật, không logo app.
- B-kiennhan-01: số 22% và “một nửa doanh nghiệp đóng cửa” chỉ có trong tóm tắt X, chưa tự kiểm, không dùng. Không chê công việc hay sếp cụ thể.
- B-imsorry-01: không dùng ảnh trẻ em thật, không dùng AI chỉnh ảnh người thật, không dùng biến thể hoá trang xúc phạm. Nhạc gốc chỉ ghi tên.
- B-bedtime-01: 23:37, 6h40, 17 triệu đêm, 61.000 người dùng chỉ có trong tóm tắt X, chưa tự kiểm, là dữ liệu Mỹ, không vào hook.
- Chính trị Brazil/Mỹ, thiên tai, bệnh, ADHD, ferritin face, tiền ảo: bỏ.
