---
title: "Trend digest 2026-10-30"
source: "pipeline/scripts/trend-collect.py + X MCP extra (Apify unavailable)"
id: trends-2026-10-30
type: trend-digest
status: draft-needs-review
updated: 2026-10-30
tags: [trends, digest, daily]
date: 2026-10-30
collector: pipeline/scripts/trend-collect.py + X MCP
skill: trend-digest v4
---
# Trend digest 2026-10-30 (Thứ Sáu)

**Nguồn:** 33/36 collector ok. Lỗi: kym-memes (HTTP 403), wiki-vi + wiki-en (HTTP 404, ngày thứ 15). **X MCP: có chạy**, trends VN 20 (Binance hack, “Thứ 6/Thứ Sáu”, Jisoo, quảng cáo Thái, crypto; chỉ móc giờ là dùng được) + worldwide 20 (Patrick Stewart/Star Trek, bóng đá, NFL; bỏ hết) + 39 story X News (4 query: productivity habits, AI at work, Gen Z Vietnam, money saving young people; max_age 72h) → `x-extra.json` 79 mục.
**Apify TikTok-native: không chạy, vẫn hết hạn mức.** Kiểm rẻ 1 lần (`clockworks/tiktok-scraper`, hashtag `hoctap`, resultsPerPage 5) bị từ chối: “Your remaining usage of $0.132525 this billing cycle isn't enough for this run”. Chưa reset. Không run id, 0 clip. Xem `apify/README.md`.
**Số lượng:** collector 462 thô → 440 cụm; raw.json 440 mục (292 ok · 17 caution · 131 drop, gồm 74 drop tay) → 309 qua lọc. Chấm tay 17 mục, hạ fit 18 mục lạc đề do heuristic khớp chữ “habits/productivity” (GM, NBA, Intel…). Drop tay: chính trị/quân sự (Serbia, Triều Tiên, Putin, Obama, Lầu Năm Góc, LHQ), tiền ảo/cá cược (Binance hack, Polymarket, Kalshi, EIP-7702), tội phạm/lừa đảo/rửa tiền, bi kịch (tàu Tây Ban Nha, hài cốt liệt sĩ, sinh tồn), bệnh và claim y khoa (ebola, não mô cầu, ung thư, huyết áp, đột quỵ, kẹo an thần, ferritin face, GLP-1), tâm linh, chế giễu nợ người nổi tiếng, một bài nêu môn học (L-087).
Dữ liệu: `collect.json`, `collect.log`, `x-extra.json`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `apify/README.md`.

## Top 10 (đã lọc)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | “Maxxing” là Từ của năm 2026 (Dictionary.com, công bố 25–26/10): tối ưu mọi thứ, “đến nằm không cũng phải tối ưu” | 1.208 | 1.0 / 0.05 | [Kenh14 29/10](https://kenh14.vn/maxxing-tu-cua-nam-2026-den-nam-khong-cung-phai-toi-uu-215261029071432772.chn), [Dictionary.com](https://www.dictionary.com/word-of-the-year), [BBC](https://www.bbc.com/news/articles/cmy4xwp22xyqo) | 4.12 (clip-06) | DARK |
| 2 | “Doing hard things early brings peace”: việc né càng lâu càng to trong đầu (Sahil Bloom) | 0.660 | 1.0 / 0.07 | [X News](https://x.com/i/trending/2115816342687510634) | 4.9 (B-tucantro-01) | DARK |
| 3 | Lời nhắc “so với timeline của mình, đừng ghen tị” khi bạn bè đi nhanh hơn | 0.647 | 1.0 / 0.10 | [X News](https://x.com/i/trending/2115788633512817077) | 3.20 (clip-22) | DARK |
| 4 | Mẹo giữ năng lượng ngày bận cuối năm | 0.286 | 1.0 / 0.25 | [VnExpress](https://vnexpress.net/meo-giu-nang-luong-trong-nhung-ngay-ban-ron-5138357.html) | 3.x năng lượng, dễ lặp | — |
| 5 | Overthinking = nghĩ mà không chốt (ngày 2) | 0.270 | 0.5 / 0.42 | [X News](https://x.com/i/trending/2115434315777789983) | 3.14 (B-overthink-01) | LIGHT |
| 6 | Nên để bao nhiêu tiền trong tài khoản thanh toán? (số Mỹ chưa tự kiểm) | 0.262 | 1.0 / 0.05 | [X News](https://x.com/i/trending/2115880094736802078) | 5.27 (B-giulai-01), caution | — |
| 7 | Ráng việc mình ghét, bỏ việc riêng nhanh (ngày 2) | 0.229 | 0.5 / 0.42 | [X News](https://x.com/i/trending/2115525365678711129) | 4.12 (B-kiennhan-01) | DARK |
| 8 | Lương 46 triệu, chi 15 triệu/tháng tiền nhà thuê | 0.220 | 1.0 / 0.05 | [Kenh14](https://kenh14.vn/luong-46-trieu-nu-nhan-vien-van-phong-chi-15-trieu-thang-de-o-nha-thue-215261029181409983.chn) | 4.18 (B-commute-02), caution | — |
| 9 | Halloween Việt 2026 (mai 31/10, hết hạn trước khi kịp làm clip) | 0.194 | 1.0 / 0.30 | [Kenh14](https://kenh14.vn/duong-dua-halloween-viet-nam-nay-dep-nuc-no-nhin-qua-da-thay-lam-tien-nhap-vai-hon-minh-tinh-man-bac-215261029202015909.chn) | — | — |
| 10 | Hà Nội: nhiều người đổi thói quen đi lại vì phí gửi xe tăng | 0.152 | 1.0 / 0.0 | [Dân trí](https://dantri.com.vn/o-to-xe-may/nhieu-nguoi-o-ha-noi-doi-thoi-quen-di-lai-vi-phi-gui-xe-tang-20261029162114792.htm) | caution (chính sách) | — |

Đã xem và bỏ: millennials đi bar tới sáng rồi đi làm (tô vẽ rượu bia, thiếu ngủ), người thành công coi việc là sở thích (ngày 3, số liệu chưa tự kiểm), Ian Fleming (ngày 3, đã có B-fleming-01), AI ở chỗ làm (bão hoà), brain stacking (ngày 6), “I’m So Sorry” (ngày 5, sat 0.95; B-imsorry-01 vẫn giữ cho clip-08), fibermaxxing (quảng cáo thực phẩm chức năng).

## TikTok signals
Không có dữ liệu Apify hôm nay. Proxy tin tức, không có view/comment/transcript tự đo nên không xếp hạng:
| keyword | nguồn | tín hiệu | brand-safe? | bridge |
|---|---|---|---|---|
| maxxing (looksmaxxing, fibermaxxing, cozymaxxing…) | Dictionary.com, BBC, Axios, Kenh14 | theo Dictionary.com: báo số dùng “maxxing” gần 19 lần nhiều hơn trong 8/2026 so với trung bình tháng 2025 (chưa tự kiểm) | ok nếu tránh looksmaxxing/ngoại hình và manosphere | B-maxxing-01 |
| “I’m So Sorry” slideshow | Google News “trend TikTok” (Mashable, Her Campus) | ngày 5 | ok, chỉ chibi | B-imsorry-01 (cũ) |
| Brainstacking | Google News US (The Hill) | ngày 6 | ok, bão hoà | B-brainstack-01 (cũ) |
| Ferritin face, fibermaxxing | Google News US | trend sức khoẻ/thực phẩm chức năng | drop | — |

## Learning
- Không thêm P-row. “Everyone is maxxing something… what’s yours?” khớp P11 (gọi tên một nhãn đang lan) + P13 (tự xếp mình vào phe). P03/P10/P11/P13/P15 +1.
- Tín hiệu mạnh nhất hôm nay là một **từ** chứ không phải một clip: “maxxing” có mặt ở báo VN (Kenh14), báo Mỹ và Anh trong cùng tuần. Móc nhìn thấy được (L-084): thẻ chữ “MAXXING · Từ của năm 2026”.
- Bão hoà nên tránh: brain stacking (ngày 6), I’m So Sorry (ngày 5), AI ở chỗ làm, mệt/ngủ cuối tháng 10.
- Halloween (31/10) là mốc mùa đã quá hạn với tốc độ làm clip hiện tại; lần sau mốc mùa cần báo trước ít nhất 7 ngày.

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-maxxing-01 | maxxing, Từ của năm | đầu tháng bật cả chục thói quen, tuần thứ ba chỉ còn app nhắc nhở kêu | 4.12 | "Năm nay ai cũng đang “maxxing” một thứ gì đó. Còn bạn, đang maxxing cùng lúc mấy thứ, và tới tuần thứ ba còn giữ được mấy thứ?" (P11+P03+P15) | humor / contrarian | clip-06 (4.12), lựa chọn thứ ba cạnh B-bonghoa-01 và B-kiennhan-01 | DARK |
| B-ghenti-01 | so với timeline của mình | lướt thấy bạn cũ khoe chìa khoá nhà mới, nhìn lại sổ tiết kiệm của mình | 3.20 | "Bạn bè người đổi xe, người mua nhà, còn kế hoạch của bạn thì cứ dời qua tháng sau?" (P03+P15) | empathy / contrarian | clip-22 (3.20) | DARK |
| B-viecne-01 | làm việc khó sớm | cuộc gọi cần gọi né cả tuần, gọi thật thì mười phút | 4.9 | "Cuộc gọi bạn né cả tuần nay, gọi thật chắc mất mười phút. Vậy sao nó to dữ vậy trong đầu?" (P10+P03) | empathy | củng cố B-tucantro-01 (4.9 đã dùng ở clip-02, chỉ làm callback) | DARK |

Cầu nối về trục kênh (rule 26/10): trend chỉ là cái móc ở hook. Thông điệp mỗi bridge là một việc nhỏ làm được hôm nay: giữ đúng một thói quen và tính theo tháng · ghi một thứ mình nhích lên so với ba tháng trước · mở việc đang né ra trong năm phút.

## Differentiation
- **B-maxxing-01**: Mọi người đang nói “maxxing” là chứng ám ảnh tối ưu, Gen Z tối ưu cả việc nằm không, câu hỏi là thế nào là đủ ([Kenh14](https://kenh14.vn/maxxing-tu-cua-nam-2026-den-nam-khong-cung-phai-toi-uu-215261029071432772.chn), [BBC](https://www.bbc.com/news/articles/cmy4xwp22xyqo)). Góc của mình: không chê ai muốn tốt hơn, tự nhận trước là mình cũng từng bật cả chục thói quen (P15). Cái sai là muốn tốt hơn mười thứ trong ba tuần. Sách (4.12): một việc nhỏ đã mất 18–254 ngày mới quen. Giữ một thứ, cộng một mỗi ngày. Chuyện thật của Hiệp: [CẦN HIỆP XÁC NHẬN].
- **B-ghenti-01**: Mọi người đang chia sẻ quote “đừng ghen tị, mỗi người một timeline, đừng bỏ cuộc” ([X News](https://x.com/i/trending/2115788633512817077)). Góc của mình: không bắt hết ghen tị, chỉ đổi thước đo sang chính mình ba tháng trước và ghi ra đúng một thứ. Fact phải lấy từ sách 3.20; claim tâm lý trong tóm tắt X chưa tự kiểm, không dùng.
- **B-viecne-01**: Mọi người đang nói làm việc khó trước thì nhẹ đầu ([X News](https://x.com/i/trending/2115816342687510634)). Góc của mình: không “eat the frog” cả buổi sáng, chỉ mở việc ra năm phút (4.9: trì hoãn là né cảm giác khó chịu). Chủ đề đã dùng ở clip-02 nên chỉ làm callback.

## Plan stubs
- `plans/plan-1-maxxing-mot-thoi-quen.json`: ✔ validate 9 cảnh, 58,00s (stub-needs-approval). Trend ở b01 (L-084: thẻ chữ “MAXXING · Từ của năm 2026”). Fact theo ràng buộc Deep Research 27/10 (18–254 ngày, lỡ một lần; không dùng 66 ngày). Ví dụ đời thường (dậy sớm, ly nước, đi bộ, giờ ngủ, app nhắc nhở), không môn học (`check-rules.py --subjects` PASS).
- `plans/plan-2-ban-be-di-nhanh-so-voi-minh-ba-thang-truoc.json`: ✔ validate 9 cảnh, 58,00s (stub-needs-approval). b05 để trống chờ fact 3.20 từ Deep Research. Ví dụ nhà, xe, sổ tiết kiệm, ghi chú điện thoại. `check-rules.py --subjects` PASS.
- Kịch bản thật do OpenCreator Studio viết sau khi Deep Research kiểm fact và Rule Reviewer duyệt.

## Script hooks (cần Hiệp duyệt)
1. "Năm nay ai cũng đang “maxxing” một thứ gì đó. Còn bạn, đang maxxing cùng lúc mấy thứ, và tới tuần thứ ba còn giữ được mấy thứ?" (B-maxxing-01, clip-06, DARK)
2. "Bạn bè người đổi xe, người mua nhà, còn kế hoạch của bạn thì cứ dời qua tháng sau?" (B-ghenti-01, clip-22, DARK)
3. "Cuộc gọi bạn né cả tuần nay, gọi thật chắc mất mười phút. Vậy sao nó to dữ vậy trong đầu?" (B-viecne-01, callback 4.9, DARK)

## Safety notes
- B-maxxing-01: không dùng looksmaxxing, ngoại hình, cơ thể, manosphere; không dùng fibermaxxing (thực phẩm chức năng). Số 19 lần / 700% của Dictionary.com chỉ là bằng chứng trend, chưa tự kiểm, không vào voice.
- B-ghenti-01: tiền và so sánh là vùng caution: không nêu số lương/giá nhà, không chế giễu ai chậm, không ảnh người thật.
- B-viecne-01: các nghiên cứu nhắc trong tóm tắt X chưa tự kiểm, không dùng.
- Chính trị, quân sự, tiền ảo, bệnh, bi kịch: bỏ.
