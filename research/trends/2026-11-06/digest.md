---
title: "Trend digest 2026-11-06"
source: "pipeline/scripts/trend-collect.py + X MCP extra + Apify clockworks"
id: trends-2026-11-06
type: trend-digest
status: draft-needs-review
updated: 2026-11-06
tags: [trends, digest, daily]
date: 2026-11-06
collector: pipeline/scripts/trend-collect.py + X MCP + Apify
skill: trend-digest v4
---
# Trend digest 2026-11-06 (thứ Sáu)

**Nguồn:** 33/36 collector ok. Lỗi: kym-memes (HTTP 403), wiki-vi + wiki-en (HTTP 404, ngày thứ 22). **X MCP: có chạy.** Trends VN 20 mục («Thứ 6», «Thứ Sáu», «Ngày», «Chào», «Sáng», «Chúc», «Cuối» là móc giờ; còn lại fandom Thái / crypto / Trump — bỏ). Worldwide 20 mục (Nhật, bóng đá, Paraguay, Russell Brand; không dùng được). Thêm 53 story X News duy nhất từ 4 query (productivity habits, AI at work, Gen Z Vietnam, motivation/burnout; max_age 72h). Gộp vào `x-extra.json` (93 mục), bản gốc trong `x-raw/`.
**Apify TikTok-native: CÓ chạy** (hạn mức đã hồi). Quota check rẻ SUCCEEDED (`ske0ofAafDdl0Pf2V`, 5 clip). Full discovery SUCCEEDED (`U4Q4IU8uOOEibxDxV`, 48 clip, ~0,17 CU). Comments SUCCEEDED (`B4eASt8kYPF5bR1U9`, 54 comment / 3 URL). Normalize `apify/clips.json` fields coverage 100% (subtitle = caption fallback khi không có VTT). Xem `apify/README.md`.
**Số lượng:** collector 476 thô → 457 cụm. raw.json 460 mục (thêm 3 TikTok-native): 358 ok · 12 caution · 90 drop (28 drop tay). **370 qua lọc.** Chấm tay 18 mục; mục chưa soát giới hạn fit và bridgeability ≤0,4; YT niche chỉ làm bằng chứng pattern. Drop tay: tội phạm / bắt giữ TikToker, chính trị / bầu cử / Trump, bệnh và nhãn y khoa (ADHD, tiểu đường, ung thư, đột quỵ, trầm cảm), bi kịch / tang lễ, đời tư showbiz, xổ số / vàng, rượu bia / cần sa, oatzempic / fibermaxxing / brain stacking (bão hoà), Olympia chuẩn mực.

Dữ liệu: `collect.json`, `collect.log`, `x-extra.json`, `x-raw/`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `apify/`.

## Top 10 (đã lọc)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | TikTok «Cách thoát khỏi trì hoãn, nằm một chỗ lướt điện thoại» (@nghemoi.official, 849,9k play / 7.267 share; comment top «giờ nghe hết cái video này tao cũng lười á») | 0.934 | 1.0 / 0.07 | [TikTok @nghemoi.official](https://www.tiktok.com/@nghemoi.official/video/7640877396073188629) | 4.9 (bằng chứng / hook phụ cho script dọn liền tay đang chờ chốt) | DARK |
| 2 | Adult gamers: cả ngày mong về mở game, tan làm chỉ còn ~47 phút Steam rồi ngủ gật (số từ tóm tắt X, chưa tự kiểm từng người) | 0.859 | 1.0 / 0.03 | [X News](https://x.com/i/trending/2118431101891027153) | 3.11 (đăng #16) | LIGHT |
| 3 | TikTok «ở nhà lâu ngày mất năng động» (@kiwilamdep, 168,9k, đăng 05/11; comment «ở nhà mà vẫn tích cực thì sao») | 0.745 | 1.0 / 0.03 | [TikTok @kiwilamdep](https://www.tiktok.com/@kiwilamdep/video/7704503079500139777) | 22.6 (đăng #23) | LIGHT |
| 4 | Infographic đi bộ: 5 phút nâng tâm trạng, ~11 phút/ngày giảm rủi ro (Mayo / Cambridge theo tóm tắt X, chưa tự kiểm bài gốc) | 0.431 | 1.0 / 0.07 | [X News](https://x.com/i/trending/2118294792505278510) | 22.6 (bằng chứng phụ) | LIGHT |
| 5 | Ưu tiên chăm mình hơn chiều lòng mọi người (people-pleasing) | 0.420 | 1.0 / 0.05 | [X News](https://x.com/i/trending/2118313919379038455) | 3.16 (ý tưởng mới / nói không) | — |
| 6 | Vibe coding: cảm giác làm được trong khi chẳng ship được gì | 0.363 | 1.0 / 0.17 | [X News](https://x.com/i/trending/2118413816937714108) | 4.7 (clip-03, góc ảo giác tiến độ — tránh AI-jobs chung) | DARK |
| 7 | Phim AI bối cảnh thời Tống «6 tỷ lượt xem» (số từ báo, chưa tự kiểm) | 0.289 | 1.0 / 0.15 | [VnExpress](https://vnexpress.net/phim-ai-boi-canh-thoi-tong-gay-sot-voi-6-ty-luot-xem-5141207.html) | 4.15 (bằng chứng phụ cạnh B-texthip-01) | — |
| 8 | TikTok «Một cách giúp giảm trì hoãn» (@amateurpsychology, 58,7k) | 0.262 | 1.0 / 0.1 | [TikTok @amateurpsychology](https://www.tiktok.com/@amateurpsychology/video/7693909106041703713) | 4.9 (pattern evidence) | — |
| 9 | Reviewer từng quyết không cho con xem TV/iPad rồi quay xe (caution: người có tên + trẻ em) | 0.260 | 1.0 / 0.05 | [Genk](https://genk.vn/reviewer-ngoc-vy-tung-quyet-khong-cho-con-xem-tv-ipad-cuoi-cung-quay-xe-khet-let-165261105160941521.chn) | 4.15 (chỉ góc tự nhận giới hạn app của người lớn) | — |
| 10 | «Ironies of Automation» 1983 vọng lại tranh luận AI coding (cognitive surrender) | 0.236 | 1.0 / 0.2 | [X News](https://x.com/i/trending/2118039608730779852) | 4.7 (bằng chứng phụ) | — |

Đã xem và bỏ khỏi top: UK quiet quitting (ngày 3, đã dùng cho 3.13); so sánh / buông so sánh (bão hoà); brain stacking (ngày 12); AI ở chỗ làm nói chung (Glasshand, corporate AI mandate, entry-level wipeout); CCCD khoe thẻ (ngày 3, clip-29 đã đủ hook); Vietlott / vàng / showbiz / bệnh / chính trị.

## TikTok signals
| keyword | nguồn | tín hiệu | brand-safe? | bridge |
|---|---|---|---|---|
| trì hoãn + lướt điện thoại | [Apify @nghemoi.official](https://www.tiktok.com/@nghemoi.official/video/7640877396073188629) | 849,9k / 7,2k share; comment «nghe xong cũng lười» | ok | B-trihoan-dt-01 → 4.9 |
| ở nhà lâu mất năng động | [Apify @kiwilamdep 05/11](https://www.tiktok.com/@kiwilamdep/video/7704503079500139777) | 168,9k / 2,2k share; mới | ok | B-onhalau-01 → đăng #23 |
| giới hạn thời gian app (iPhone Screen Time) | Apify search `gioi han thoi gian dien thoai` | nhiều mẹo shop / phụ huynh | ok (góc người lớn) | bằng chứng 4.15 |
| #phattrienbanthan | Apify hashtag | @hoaquynh0000 «còn trẻ để chọn đúng», @gonaox ghi nhớ (1,4M — góc học, chỉ pattern) | ok / caution học | — |
| #thoiquen nhạc cover | Apify hashtag | cover bài hát, bỏ | drop | — |
| #taptrung Ark Drops | Apify hashtag | quảng cáo thực phẩm, bỏ | drop | — |

## Learning
- Không thêm P-row. Tan làm hết pin khớp P10+P12. Ở nhà lâu khớp P10+P03. Trì hoãn+ĐT khớp P01+P10. P03/P10/P12 +1.
- Apify chạy lại lần đầu từ 22/10: tín hiệu TikTok-native trở lại. Query `het tri hoan` + `gioi han thoi gian dien thoai` ra đúng trụ 1–2; `#thoiquen` / `#taptrung` bị nhạc và ads — lần sau bỏ hoặc thay hashtag.
- Chủ đề «hết năng lượng sau giờ làm» lên từ hai phía: X News adult gamers + TikTok ở nhà lâu. Hợp trụ 3 (3.11) và trụ 4 (22.6), cả hai LIGHT — tốt cho chuỗi theme.
- 4.9 đang chờ chốt có thêm bằng chứng TikTok mạnh (849k); không cần stub mới nếu Hiệp đã nghiêng B-donlientay-01.
- Bão hoà nên tránh: bông hoa chưa nở (ngày 11), brain stacking (ngày 12), so sánh (ngày 8), AI ở chỗ làm nói chung, UK quiet quitting (ngày 3), CCCD (ngày 3).

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-gameenergy-01 | Adult gamers post-work crash | trên xe về vẫn nghĩ tối chơi một ván, về tới nhà mở máy rồi ngủ gật | 3.11 (Brooks & Lack 2006 — Deep Research xác nhận trước khi nêu tên) | "Cả mạng đang kể một chuyện giống nhau: cả ngày mong về mở game, tan làm thì chỉ còn đúng bốn mươi bảy phút Steam rồi ngủ gật trên ghế." (P10+P12) | empathy / data | đăng #16 (3.11) hook trend | LIGHT |
| B-onhalau-01 | Ở nhà lâu mất năng động | cuối tuần ở nhà từ sáng, định ra ngoài rồi lại mở điện thoại thêm một tiếng | 22.6 | "TikTok đang có clip hỏi vì sao người ở nhà lâu ngày lại dần mất đi sự năng động. Comment bên dưới toàn người gật: mình cũng đang vậy." (P10+P03) | empathy / contrarian | đăng #23 (22.6) hook trend | LIGHT |
| B-trihoan-dt-01 | Nằm lướt ĐT rồi trì hoãn | định làm một việc nhỏ, nằm xuống mở TikTok «một chút» | 4.9 | "Có clip gần tám trăm năm mươi nghìn lượt xem hỏi: cách thoát trì hoãn khi đang nằm một chỗ lướt điện thoại là gì?" (P01+P10) | empathy | 4.9 bằng chứng / hook phụ (script dọn liền tay đang chờ chốt) | DARK |

Cầu nối về trục kênh: trend chỉ là móc. B-gameenergy-01: về nhà đặt báo thức 10 phút trước app giải trí. B-onhalau-01: ra khỏi cửa đi bộ 10 phút, không mục tiêu. B-trihoan-dt-01: đứng dậy làm đúng một việc chín mươi giây đang để đó (callback clip-02).

## Differentiation
- **B-gameenergy-01**: Mọi người đang nói: người lớn hết pin sau giờ làm, tối muốn chơi mà chỉ kịp mở app ([X News](https://x.com/i/trending/2118431101891027153); số 47 phút từ tóm tắt, chưa tự kiểm). Góc của mình: không phải thiếu kỷ luật tối. Năng lượng cả ngày đã hết; 3.11 nói chợp khoảng mười phút lấy lại tỉnh táo tốt hơn cố «cày» tiếp. Voice nói rõ số 47 là lời kể trên mạng.
- **B-onhalau-01**: Mọi người đang nói: ở nhà lâu thì mất năng động, phải có lịch tập / ra quán ([TikTok @kiwilamdep](https://www.tiktok.com/@kiwilamdep/video/7704503079500139777)). Góc của mình: không cần kế hoạch lớn. 22.6 chỉ một việc — đi bộ. Tránh biến thành outdoor hustle (B-outdoor-01).

## Plan stubs
- `plans/plan-1-tan-lam-het-nang-luong-chop-muoi-phut.json`: ✔ validate 9 cảnh, 70,00s (stub-needs-approval). Trend nói thành lời ở b01 (L-084: thẻ chữ «tan làm hết pin · Adult Gamers · X News 05/11»). Ví dụ đời thường: xe về, sofa, gamepad, báo thức 10 phút. Tuần 3, không Omi.
- `plans/plan-2-o-nha-lau-mat-nang-dong-di-bo.json`: ✔ validate 9 cảnh, 70,00s (stub-needs-approval). Trend ở b01 (thẻ chữ «ở nhà lâu mất năng động · @kiwilamdep 05/11»). Ví dụ: cuối tuần ở nhà, điện thoại, dép, cửa. Tuần 4, không Omi.
- `check-rules.py --subjects` (ideas + 2 stub): PASS (L-087). `--evidence`: PASS. `--choppy` / `--flow` / `--repeat`: FAIL vì parser cần khung script «N. **[Nhãn]** lời» (giai đoạn OpenCreator), không đọc dialogue trong plan JSON — giống giới hạn công cụ, không phải lỗi nội dung stub. L-096: stub 1 chưa nêu đủ 3 phần dẫn chứng (Brooks & Lack) — Deep Research xác nhận trước khi viết script thật; số «47 phút» voice phải nói là lời kể trên mạng.
- Kịch bản thật do OpenCreator Studio viết sau khi Deep Research kiểm fact và Rule Reviewer duyệt.

## Script hooks (cần Hiệp duyệt)
1. "Cả mạng đang kể một chuyện giống nhau: cả ngày mong về mở game, tan làm thì chỉ còn đúng bốn mươi bảy phút Steam rồi ngủ gật trên ghế." (B-gameenergy-01, 3.11, đăng #16, LIGHT). Vì sao người lướt dừng lại: đúng cảm giác tối về hết pin.
2. "TikTok đang có clip hỏi vì sao người ở nhà lâu ngày lại dần mất đi sự năng động. Comment bên dưới toàn người gật: mình cũng đang vậy." (B-onhalau-01, 22.6, đăng #23, LIGHT). Vì sao dừng: tự nhận cuối tuần kẹt nhà.

## Trạng thái đang chờ
- clip-06 «bông hoa chưa nở» v1 và clip-05 v10 r10.2: đã ĐẠT review, vẫn chờ Hiệp chốt.
- 4.9 Dọn liền tay r3 ĐẠT, chờ chốt (+ hôm nay có bằng chứng TikTok 849k). 5.27: B-tietkiem-01 và B-thuongtet-01 (L-096/mức C).
- clip-29 (14.10): B-otp-01 + B-cccd-01.
- Đăng #26 (4.3): B-yeuviec-01. clip-20 (3.21): B-mongbantot-01. clip-08: B-thongbao-01. Ô #27: B-thang11-01, B-muathoigian-01.
- Đăng #10 (4.15): B-texthip-01. Đăng #12 (3.13): B-chunhat-01.
- Mới: đăng #16 (3.11) có B-gameenergy-01; đăng #23 (22.6) có B-onhalau-01.
- Apify: đã chạy lại được 06/11 (quota hồi).
- Commit 725d384…4014ab3 / b19afe9 / 9bf376d và hôm nay chưa push (Mac của Hiệp; News giữ bundle).

## Safety notes
- B-gameenergy-01: không nói nghiện game, không nhãn bệnh, số 47 phút phải nói là lời kể trên mạng. Không logo Steam.
- B-onhalau-01: không dùng góc làm đẹp / body của tài khoản nguồn; không chẩn đoán; không bảo ai «lười».
- B-trihoan-dt-01: không stub mới nếu 4.9 đã chốt; chỉ bằng chứng.
- Chính trị, tội phạm, bệnh, bi kịch, tâm linh, vàng, xổ số, rượu bia, đời tư người nổi tiếng: bỏ.
