---
title: "Trend digest 2026-11-07"
source: "pipeline/scripts/trend-collect.py + X MCP extra + Apify clockworks"
id: trends-2026-11-07
type: trend-digest
status: draft-needs-review
updated: 2026-11-07
tags: [trends, digest, daily]
date: 2026-11-07
collector: pipeline/scripts/trend-collect.py + X MCP + Apify
skill: trend-digest v4
---
# Trend digest 2026-11-07 (thứ Bảy)

**Nguồn:** 33/36 collector ok. Lỗi: kym-memes (HTTP 403), wiki-vi + wiki-en (HTTP 404, ngày thứ 23). **X MCP: có chạy.** Trends VN 20 mục («Thứ 7», «Thứ Bảy», «Cuối», «Sáng», «Chào», «Chúc», «Ngày», «Thứ 6» là móc giờ; còn lại fandom Thái / crypto — bỏ). Worldwide 20 mục (chính trị Mỹ, Nhật, bóng đá — không dùng). Thêm 59 story X News duy nhất từ 4 query (productivity/burnout, AI at work/vibe coding, Gen Z Vietnam, motivation/habits/sleep; max_age 72h). Gộp vào `x-extra.json` (99 mục), bản gốc trong `x-raw/`.
**Apify TikTok-native: CÓ chạy** (hạn mức vẫn hồi). Quota check rẻ SUCCEEDED (`TfvMKPifNazwRwOg2`, 5 clip). Full discovery SUCCEEDED (`269BN4t8jvJsm5OWa`, 64 clip, ~0,13 CU). Comments SUCCEEDED (`1Q8VWGDmTQncOr1kR`, 73 comment / 5 URL). Normalize `apify/clips.json` fields coverage 100%. Xem `apify/README.md`.
**Số lượng:** collector 482 thô → 469 cụm. raw.json 474 mục (thêm 5 TikTok-native shortlist): 366 ok · 11 caution · 97 drop (35 drop tay). **~377 qua lọc.** Chấm tay ~20 mục; mục chưa soát giới hạn fit và bridgeability ≤0,4; YT niche chỉ làm bằng chứng pattern. Drop tay: chính trị / bầu cử / ICE, nhãn y khoa (ADHD, visceral fat), rượu/cần sa, bi kịch/showbiz, Vietlott/vàng, UK quiet quitting (bão hoà), AI-at-work generic, day-of-week greetings, Olympia/môn học (L-087).

Dữ liệu: `collect.json`, `collect.log`, `x-extra.json`, `x-raw/`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `apify/`.

## Top 10 (đã lọc)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | Bone-deep tiredness: mệt mà ngủ thêm cũng không hết (tóm tắt X nêu ~6h33 — chưa tự kiểm) | 0.945 | 1.0 / 0.05 | [X News](https://x.com/i/trending/2118649260149494132) | 3.3 (đăng #15) | DARK |
| 2 | AI users mệt vì phải đọc quá nhiều output model («never have I read so much») | 0.838 | 1.0 / 0.07 | [X News](https://x.com/i/trending/2118406568739770865) | 3.6 (đăng #11) | DARK |
| 3 | TikTok «Còn trẻ không phải để làm hết — chọn đúng những thứ đáng làm» (@hoaquynh0000, 381,1k; comment «tập 10 phút / giữ kỷ luật») | 0.562 | 0.5 / 0.1 | [TikTok @hoaquynh0000](https://www.tiktok.com/@hoaquynh0000/video/7696719796678774034) | 4.8 / ô #27 LIGHT | LIGHT |
| 4 | Embracing nonchalance / ngừng để ý chuyện không kiểm soát được | 0.533 | 1.0 / 0.1 | [X News](https://x.com/i/trending/2118735323895337000) | 3.16 (ý tưởng / nói không) | — |
| 5 | TikTok trì hoãn + nằm lướt ĐT (@nghemoi.official, 850,5k) — ngày 2 | 0.518 | 1.0 / 0.3 | [TikTok @nghemoi.official](https://www.tiktok.com/@nghemoi.official/video/7640877396073188629) | 4.9 (bằng chứng B-trihoan-dt-01) | DARK |
| 6 | IDGAF era / detachment for personal peace | 0.477 | 1.0 / 0.12 | [X News](https://x.com/i/trending/2118369274461052991) | 3.16 / 3.20 (bằng chứng phụ) | — |
| 7 | Genk: mỏi mắt — đừng đổ lỗi máy tính/ĐT, hãy xem lại đèn bàn | 0.420 | 1.0 / 0.05 | [Genk](https://genk.vn/hay-bi-moi-mat-dung-voi-do-loi-cho-may-tinh-dien-thoai-den-ban-ban-dang-dung-co-the-moi-la-thu-can-xem-lai-165261106165921461.chn) | 3.6 (bằng chứng phụ đời thường) | — |
| 8 | TikTok «giữ nguyên tắc và giới hạn riêng» (@tinhchua_podcast, 112,5k) | 0.360 | 1.0 / 0.07 | [TikTok @tinhchua_podcast](https://www.tiktok.com/@tinhchua_podcast/video/7653995941699063060) | 3.16 (pattern) | — |
| 9 | Kenh14: gia đình 4 người giảm tiền ăn 9→6 triệu/tháng | 0.327 | 1.0 / 0.07 | [Kenh14](https://kenh14.vn/tu-9-trieu-xuong-6-trieu-tien-an-moi-thang-gia-dinh-4-nguoi-tiet-kiem-them-3-trieu-nhung-phai-thay-doi-nhung-gi-215261106072524463.chn) | 5.x tiền (caution; dòng an toàn) | — |
| 10 | VnExpress: AI lấy dữ liệu từ điện thoại đang khóa (Anthropic model) | 0.327 | 1.0 / 0.2 | [VnExpress](https://vnexpress.net/ai-lay-du-lieu-tu-dien-thoai-dang-khoa-the-nao-5141195.html) | 14.10 (bằng chứng phụ cạnh B-otp-01) | DARK |

Đã xem và bỏ khỏi top: UK quiet quitting (bão hoà 3.13); adult gamers / vibe coding (đã bridge 06/11); DST Mỹ (VN không đổi giờ); ADHD nhãn; so sánh/brain stacking; CCCD; Vietlott/vàng/showbiz/bệnh/chính trị; query Apify «tan lam het pin» = mẹo pin shop.

## TikTok signals
| keyword | nguồn | tín hiệu | brand-safe? | bridge |
|---|---|---|---|---|
| còn trẻ chọn đúng | [Apify @hoaquynh0000](https://www.tiktok.com/@hoaquynh0000/video/7696719796678774034) | 381,1k; comment kỷ luật / tập 10p | ok (tránh góc ly hôn trong comment top) | B-chonviec-01 → #27 / 4.8 |
| trì hoãn + lướt ĐT | [Apify @nghemoi.official](https://www.tiktok.com/@nghemoi.official/video/7640877396073188629) | 850,5k / comment «nghe xong cũng lười» | ok | B-trihoan-dt-01 evidence |
| giới hạn / nguyên tắc riêng | [Apify @tinhchua_podcast](https://www.tiktok.com/@tinhchua_podcast/video/7653995941699063060) | 112,5k | ok | 3.16 pattern |
| #phattrienbanthan | Apify hashtag | mindset / tài chính cá nhân lẫn ads | ok / caution | — |
| tan lam het pin | Apify search | **toàn mẹo tiết kiệm pin iPhone** (shop) | drop | đổi query lần sau |
| ngu bu cuoi tuan | Apify search | ít clip hữu ích / lệch | — | — |

## Learning
- Không thêm P-row. Bone-deep tiredness khớp P10+P12. AI reading fatigue khớp P10+P03. Chọn việc / nonchalance khớp P03. P03/P10/P12 +1.
- Apify vẫn chạy được (ngày 2 sau khi hồi). Lesson query: `tan lam het pin` bị hiểu theo nghĩa pin điện thoại — lần sau dùng `tan lam met moi` / `het nang luong sau gio lam`. Tránh `#nangluong` tâm linh.
- Chủ đề «mệt nhưng ngủ không hết» + «đọc AI đến mệt» là hai góc mới cho trụ 3 (3.3) và trụ 2 (3.6) — cả hai DARK; chuỗi theme đăng cần kiểm quy tắc 4 khi xếp lịch.
- 4.9 tiếp tục có bằng chứng TikTok 850k (ngày 2); không stub mới.
- Bão hoà nên tránh: bông hoa chưa nở, brain stacking, so sánh, AI-at-work generic, UK quiet quitting, CCCD, vibe-coding ảo giác tiến độ (đã dùng 06/11), adult gamers (đã stub 3.11).

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-mettamsau-01 | Bone-deep tiredness | tối ngủ sớm hơn vẫn dậy nặng mắt; cả tuần «chỉ sáu tiếng» | 3.3 | "Cả mạng đang than một kiểu mệt mà ngủ thêm cũng không hết — mệt hơn cả thể chất." (P10+P12) | empathy / data | đăng #15 (3.3) hook trend | DARK |
| B-airead-01 | AI reading fatigue | hỏi AI một câu, nhận cả trang, hỏi lại thêm trang nữa | 3.6 | "Có người viết đúng một câu: chán đọc output của model quá, chưa bao giờ trong đời phải đọc nhiều chữ đến vậy." (P10+P03) | empathy / data | đăng #11 (3.6) hook trend | DARK |
| B-chonviec-01 | TikTok còn trẻ chọn đúng | cuối tuần liệt mười việc «phải làm», không việc nào xong | 4.8 | "TikTok đang có clip nói: còn trẻ không phải để làm hết mọi thứ — mà để chọn đúng những thứ đáng làm." (P03+P10) | contrarian / empathy | ô #27 LIGHT / 4.8 | LIGHT |
| B-nonchal-01 | Nonchalance / IDGAF | mỗi thông báo group đều mở, tối về hết pin chú ý | 3.16 | "Cả mạng đang rủ nhau «ngừng để ý chuyện không kiểm soát được». Nghe nhẹ, mà khó giữ." (P03) | empathy | 3.16 ý tưởng (phụ B-noikhong-01) | — |

Cầu nối về trục kênh: trend chỉ là móc. B-mettamsau-01: ngủ sớm hơn 30 phút (+1), không bù cuối tuần. B-airead-01: một câu hỏi → một khung → đóng. B-chonviec-01: chọn đúng một việc có ngày hạn (callback 4.1/4.8). B-nonchal-01: nói không với một tin nhắn ngoài việc hôm nay.

## Differentiation
- **B-mettamsau-01**: Mọi người đang nói: mệt «xương» mà ngủ không hết ([X News](https://x.com/i/trending/2118649260149494132); số 6h33 chưa tự kiểm). Góc của mình: không chẩn đoán, không bảo «yếu». 3.3 = thiếu giờ ngủ mãi; khác B-gameenergy-01 (3.11 chợp 10 phút sau tan làm).
- **B-airead-01**: Mọi người đang nói: AI giúp code nhanh mà đọc output thì kiệt ([X News](https://x.com/i/trending/2118406568739770865)). Góc của mình: không phải AI-jobs; là chi phí ngắt quãng 3.6. Khác vibe-coding «ảo giác tiến độ» (4.7).
- **B-chonviec-01**: Mọi người đang nói: còn trẻ phải trải hết ([TikTok @hoaquynh0000](https://www.tiktok.com/@hoaquynh0000/video/7696719796678774034)). Góc của mình: 4.8 một việc có hạn — không listicle «10 thói quen».

## Plan stubs
- `plans/plan-1-met-sau-hon-ngu-sau-tieng.json`: ✔ validate 9 cảnh, 70,00s (stub-needs-approval). Trend nói thành lời ở b01 (L-084: thẻ chữ «mệt mà ngủ không hết · X News 06/11»). Ví dụ đời thường: giường, báo thức, điện thoại úp. Tuần 3, không Omi. Theme dark.
- `plans/plan-2-doc-ai-met-mat-mot-liet.json`: ✔ validate 9 cảnh, 70,00s (stub-needs-approval). Trend ở b01 (thẻ chữ «mệt vì đọc AI · X News 05/11»). Ví dụ: laptop, một cửa sổ chat, đóng tab. Tuần 2, không Omi. Theme dark.
- `check-rules.py --subjects` (ideas + 2 stub): PASS (L-087).
- Kịch bản thật do OpenCreator viết sau Deep Research (Walker/3.3; chi phí ngắt quãng 3.6) và Rule Reviewer duyệt. Số «6 giờ 33» voice phải nói là lời tóm tắt trên mạng.

## Script hooks (cần Hiệp duyệt)
1. "Cả mạng đang than một kiểu mệt mà ngủ thêm cũng không hết — mệt hơn cả thể chất." (B-mettamsau-01, 3.3, đăng #15, DARK). Vì sao dừng: đúng cảm giác dậy vẫn nặng dù đã ngủ.
2. "Có người viết đúng một câu: chán đọc output của model quá, chưa bao giờ trong đời phải đọc nhiều chữ đến vậy." (B-airead-01, 3.6, đăng #11, DARK). Vì sao dừng: đúng mệt sau một buổi «hỏi AI».

## Trạng thái đang chờ
- clip-06 «bông hoa chưa nở» v1 và clip-05 v10 r10.2: đã ĐẠT review, vẫn chờ Hiệp chốt.
- 4.9 Dọn liền tay r3 ĐẠT, chờ chốt (+ bằng chứng TikTok 850k ngày 2). 5.27: B-tietkiem-01 và B-thuongtet-01 (L-096/mức C).
- clip-29 (14.10): B-otp-01 + B-cccd-01 (+ hôm nay AI phone lock bằng chứng phụ).
- Đăng #26 (4.3): B-yeuviec-01. clip-20 (3.21): B-mongbantot-01. clip-08: B-thongbao-01. Ô #27: B-thang11-01, B-muathoigian-01, **+ B-chonviec-01**.
- Đăng #10 (4.15): B-texthip-01. Đăng #12 (3.13): B-chunhat-01.
- Đăng #16 (3.11): B-gameenergy-01. Đăng #18 (2.17): B-onhalau-01 (không map 22.6 MDD).
- **Mới:** đăng #15 (3.3) có B-mettamsau-01; đăng #11 (3.6) có B-airead-01.
- Apify: chạy được ngày 2 liên tiếp (quota hồi từ 06/11).
- Commit gần đây + hôm nay chưa push (Mac của Hiệp; News giữ bundle).

## Safety notes
- B-mettamsau-01: không nhãn bệnh, không «mệt mỏi mãn tính», số 6h33 phải nói là tóm tắt mạng. Không khuyên thuốc.
- B-airead-01: không logo model/hãng; không nói AI lấy việc; không số % chưa kiểm.
- B-chonviec-01: bỏ góc ly hôn trong comment nguồn; không listicle «phải trải hết».
- Chính trị, tội phạm, bệnh, bi kịch, tâm linh, vàng, xổ số, rượu bia, đời tư người nổi tiếng: bỏ.
