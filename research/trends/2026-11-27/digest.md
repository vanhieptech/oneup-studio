---
title: "Trend digest 2026-11-27"
source: "pipeline/scripts/trend-collect.py + radar-fetch.py + tinyfish_client.py + apify-run.py"
id: trends-2026-11-27
type: trend-digest
status: draft-needs-review
updated: 2026-11-27
tags: [trends, digest, daily]
date: 2026-11-27
collector: pipeline/scripts/trend-collect.py + radar-fetch.py + apify-run.py + tinyfish_client.py
skill: trend-digest v5.1.0
---
# Trend digest 2026-11-27 (thứ Sáu — Black Friday)

**Nguồn:** 30/39 collector ok. Lỗi: `kym-memes` (HTTP 403), `yt-niche-vn` / `yt-niche-en` (`JSONDecodeError`), 6 nguồn `tf-*` trong collector trống do `node` không có trong PATH mặc định (chạy riêng `tinyfish_client.py tiktok` với `PATH=/usr/local/bin` thu được **29** ứng viên; 1 query báo `Cannot reach agent.tinyfish.ai`). **X MCP:** `x: unavailable (no x MCP server configured)`.
**Apify TikTok:** chạy ok — **40 clip**, **28 subtitle**, **comments cho 3 clip**, 100% đủ 12 trường bắt buộc; chi phí **$0.1490 USD** (`apify/clips.json`).
**Multi-Channel Radar (`radar-fetch.py` + `trend-streams.py radar`):** 96 clip từ 10/13 kênh (lỗi `hoaquynh`, `spiderum` TikTok secondary user ID; `hieutv` Shorts HTTP 404) + 40 clip Apify → **27 outlier** trong `radar.json`, nạp **+25** vào `teardown-queue.json`.
**Số lượng:** collector 480 thô → 452 cụm. `raw.json` 457 mục (thêm 5 TikTok-native): **358 ok · 14 caution · 85 drop** (47 drop bộ lọc từ khoá + 38 hand-drop: chính trị, tai nạn/nổ khí gas, kiện tụng, sao/scandal, y khoa/GLP-1, NSFW). **372 qua lọc.**

Dữ liệu: `collect.json`, `radar.json`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `apify/`, `tinyfish/`, `teardowns/`.

## Luồng 1 — Outlier Radar (`radar.json`, 27 outlier — tiêu biểu đúng ngách)
| creator | view | outlier | chủ đề | góc khai thác | link |
|---|---|---|---|---|---|
| `@phamthuykieuhuong` | 1.700.000 | 38.99x (median) | hoc-tap, productivity | **Đã teardown → ARC-003**: bảng 6 số liệu phản khuôn mẫu (U30 học lại từ 0) → 4.12 | [TikTok](https://www.tiktok.com/@phamthuykieuhuong/video/7711338098323410196) |
| `@gonaox` | 1.900.000 | 12.69x (v/f) | tu-duy, hoc-tap | Mẹo ghi nhớ nhanh → đối chiếu bằng retrieval practice (23.14) | [TikTok](https://www.tiktok.com/@gonaox/video/7702426588662598920) |
| `@minggbest` | 796.400 | 106.33x (v/f) | hoc-tap | «Từ này nhìn quen lắm» = ảo giác thành thạo (recognition ≠ recall) → 23.14 (đăng #25) | [TikTok](https://www.tiktok.com/@minggbest/video/7696495062217248018) |
| `@phatbieulungtung` | 819.200 | 23.74x (v/f) | tu-duy | Đừng đổi vì người khác → so với chính mình 3 tháng trước (3.20) | [TikTok](https://www.tiktok.com/@phatbieulungtung/video/7702119001333189906) |
| `@carter.selfdev` | 474.700 | 9.44x (v/f) | productivity, tu-duy | «Để ngày mai rồi tính?» — trì hoãn bão hoà, chỉ làm bằng chứng phụ | [TikTok](https://www.tiktok.com/@carter.selfdev/video/7701501687999270164) |
| `@quocnguyenkieuvi` | 881.400 | 11.24x (median) | tu-duy | Listicle dài (7p20) → rút gọn thành 1 quy tắc có nguồn (22.9 / 3.16) | [TikTok](https://www.tiktok.com/@quocnguyenkieuvi/video/7705090431322787080) |
| `@tramdungtrithuc` | 323.200 | 4.32x (v/f) | tu-duy, hoc-tap | 5 kỹ năng giao tiếp → chọn 1 tình huống công sở cụ thể (4.5 / 3.16) | [TikTok](https://www.tiktok.com/@tramdungtrithuc/video/7710321816983620882) |
| `@giangoi` | 46.000 | 3.68x (median) | storytelling, tu-duy | `southern_story_voice`: học nhịp kể chuyện tự nhiên, tự giễu nhẹ | [YT Shorts](https://www.youtube.com/shorts/TCAnJIDO3Bg) |
| `@fireship` | 5.200.000 | 3.25x (median) | tech, storytelling | `cross_niche_craft`: nhịp cắt 2–3s, punchline cho `@vanhiep.tech` | [YT Shorts](https://www.youtube.com/shorts/aXcuz6fn8_w) |

*(Các row ngoài ngách: `lucasgmc4`, `dudu.edits46`, `meo_xinhhiuu`, `realnezzdapoet`, `tapchidanong21`, `honghan582`, `kinhthiendongdao.com` đã gắn `angle: "off-niche"`.)*

## Luồng 2 — Upstream Tech & VN-Tech (`trend-streams.py upstream --check` ✔)
| tin | luồng | pain | story | `@hi.oneup` | `@vanhiep.tech` | score | kênh |
|---|---|---:|---:|---:|---:|---:|---|
| Không chia sẻ OTP, không tải app lạ vẫn có nguy cơ mất tiền: Cảnh báo khẩn cho người dùng iPhone (DarkSword & Coruna nhắm iOS cũ) | vn-tech | 5 | 4 | 4 | 5 | **0.80** | `vanhiep_tech` |
| Nhiều trang web mất khách vì Google trả lời thay (AI Mode zero-click) | vn-tech | 4 | 4 | 3 | 5 | **0.64** | `vanhiep_tech` |
| RAM đắt đỏ, Microsoft quay sang «xử» chính ứng dụng của mình để tiết kiệm gần 900MB | vn-tech | 4 | 4 | 2 | 5 | **0.64** | `vanhiep_tech` |
| Sub-agent là gì? Khi nào nên dùng, chi phí, ưu và nhược điểm ra sao? (Tinhte) | vn-tech | 4 | 4 | 2 | 5 | **0.64** | `vanhiep_tech` |
| Study reveals how GTA 6’s release affected employee productivity in Latvia and worldwide | upstream | 4 | 5 | 4 | 3 | **0.64** | `hi_oneup` |
| Company Culture = Slack Emoji ÷ sqrt(Headcount) (HN + Lobsters) | upstream | 4 | 4 | 3 | 5 | **0.64** | `vanhiep_tech` |
| Hãng phần mềm lớn nhất châu Âu (SAP) có thể sa thải 10.000 người (tái cấu trúc AI) | vn-tech | 5 | 3 | 4 | 4 | **0.48** | `hi_oneup` |
| Gửi ngân hàng bao nhiêu tiền để không đi làm vẫn có 15 triệu/tháng? (caution) | vn-tech | 5 | 3 | 4 | 2 | **0.48** | `hi_oneup` |
| AI made self-hosting fun again (HN + Lobsters) | upstream | 3 | 4 | 2 | 5 | **0.48** | `vanhiep_tech` |
| Taking Email Back (Lobsters) | upstream | 4 | 3 | 4 | 4 | **0.384** | `hi_oneup` |
| The group chat where your AI talks behind your back (HN) | upstream | 3 | 4 | 2 | 4 | **0.384** | `vanhiep_tech` |
| From minimalist to maximalist: Ars staffers show off their home offices | upstream | 3 | 4 | 4 | 3 | **0.384** | `hi_oneup` |

## Luồng 3 — Mobile / Manual Inbox (`media/footage/inbox/`)
- `0 mới, 0 trùng` (hộp thư trống hôm nay).

## Viral DNA & ARC (teardown)
- **Hoàn thành (1):** `trends-2026-11-27-01` — `@phamthuykieuhuong` (1,7M view, 11s, 38.99x) → [`teardowns/trends-2026-11-27-01.md`](teardowns/trends-2026-11-27-01.md).
  - **ARC mới:** **`ARC-003`** — *Bảng số liệu phản khuôn mẫu chốt bằng tự tin* (tương phản thân phận U30 + bảng 6 con số cụ thể + 2 chi tiết tự giễu + mục tiêu đo được).
  - **Ý tưởng tự đẩy vào `content/idea-bank.md` (+2):** `@hi.oneup` (bẫy «trễ giờ cuộc đời» ở tuổi 25–30) & `@vanhiep.tech` (chuyển ngành / học lại lập trình tuổi U30 bằng bảng 5 con số thực tế).
  - **Nỗi đau đẩy vào `audience-pain-bank.md`:** nỗi sợ U30 đã quá muộn để học lại/đổi hướng; ngại ánh nhìn khi học chung nhóm nhỏ tuổi hơn.
- **Lỗi kỹ thuật (4 clip dài hơn trả response rỗng từ `agy-default`):** `trends-2026-11-27-05` (`@giangoi`), `trends-2026-11-27-19` (`@gonaox`), `trends-2026-11-27-20` (`@carter.selfdev`), `trends-2026-11-27-14` (`@minggbest`) — vẫn giữ trong `teardown-queue.json` để thử lại sau.

## Top 10 (đã lọc)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---:|---:|---|---|---|
| 1 | Người tiêu dùng bớt mặn mà với Black Friday (TP HCM: nhiều người chỉ mua vài món cần thiết vì quanh năm đã có sale ngày đôi) | 0.989 | 1.0 / 0.07 | [VnExpress 27/11](https://vnexpress.net/nguoi-tieu-dung-bot-man-ma-voi-black-friday-5149368.html) · [Genk deals](https://genk.vn/black-friday-san-deal-gia-dung-tu-panasonic-locklock-elmich-gia-tot-bat-ngo-nhieu-mon-con-165261127082941891.chn) | 5.1 (+5.23) đăng #28 | DARK |
| 2 | TikTok `@minggbest`: «Từ này nhìn quen lắm» (796,4k view, 901 cmt, 43,2k share, 106.33x) | 0.989 | 1.0 / 0.07 | [TikTok @minggbest](https://www.tiktok.com/@minggbest/video/7696495062217248018) | 23.14 đăng #25 (đời thường, không môn học) | DARK |
| 3 | TikTok `@gonaox`: «Ghi nhớ bất cứ thứ gì nhanh đến mức khó tin» (1,9M view, 818 cmt, 31k share, 12.69x) | 0.958 | 1.0 / 0.12 | [TikTok @gonaox](https://www.tiktok.com/@gonaox/video/7702426588662598920) | bằng chứng / củng cố #2 (23.14) | DARK |
| 4 | Không chia sẻ OTP, không tải app lạ vẫn có nguy cơ mất tiền: mã độc web DarkSword & Coruna nhắm iOS cũ (13.0–17.2.1 & 18.4–18.7) | 0.946 | 1.0 / 0.05 | [Genk 27/11](https://genk.vn/khong-chia-se-otp-khong-tai-app-la-van-co-nguy-co-mat-tien-canh-bao-khan-cho-nguoi-dung-iphone-165261127155807425.chn) | 14.10 / 14.6 đăng #29 (trụ 5) | DARK |
| 5 | GTA 6 ra mắt làm sụt năng suất nhân viên (bài khảo sát GNews US + `gta vi pc port` Google Trends US + The Verge + CafeBiz) | 0.894 | 1.0 / 0.05 | [GNews US](https://news.google.com/rss/articles/CBMiwgFBVV95cUxQVzRHOU5YVU9IaXUtMndpYVh1NVhfS1pTNmQ4UFRyRFJoRnhDUzV2akZ1bjktQjBnNHVxdExrZHRQX0hkRFJhU2w1bEtubzZPWEI4UnBUb0g0T0x3cV9weGR2UHRMU2RhcnhLQ3IzVTFuN3Qyd2RYTGplNzZ2NTlTVVdzZ1VmUWlweWpjTXBmM3R1cUtTS1hOc2hBN0RqeVppUGNJU2xINnZUZDFPbm12b3hWd09KdTRPUmNaN2lfQzFBQQ?oc=5) · [The Verge](https://www.theverge.com/entertainment/1043362/grand-theft-auto-6-ending) | 4.15 (+3.9) đăng #10 | LIGHT |
| 6 | TikTok `@phamthuykieuhuong`: U30 (28 tuổi) học lớp 11 GDTX (1,7M view, 1.173 cmt, 11,4k share, 38.99x) | 0.890 | 1.0 / 0.05 | [TikTok @phamthuykieuhuong](https://www.tiktok.com/@phamthuykieuhuong/video/7711338098323410196) | ARC-003 → 4.12 (caution người thật) | LIGHT |
| 7 | Nhiều trang web mất khách vì Google AI Mode trả lời thay (cs=2) | 0.713 | 1.0 / 0.12 | [VnExpress 27/11](https://vnexpress.net/nhieu-trang-web-mat-khach-vi-google-tra-loi-thay-5148929.html) | 23.16 / `@vanhiep.tech` | DARK |
| 8 | TikTok `@vutru_codai`: «Bạn có đang quá bận tâm đến ánh mắt người khác?» (173k view) | 0.713 | 1.0 / 0.10 | [TikTok @vutru_codai](https://www.tiktok.com/@vutru_codai/video/7709041076987858197) | củng cố 3.21 đăng #20 | LIGHT |
| 9 | Company Culture = Slack Emoji ÷ sqrt(Headcount) (cs=2) | 0.614 | 1.0 / 0.05 | [HN](https://lia.mg/posts/measuring-company-culture-with-slack-emoji/) · Lobsters | `@vanhiep.tech` (văn hoá team dev) | — |
| 10 | SAP (hãng phần mềm lớn nhất châu Âu) có thể sa thải 10.000 người khi tái cấu trúc AI (cs=2) | 0.582 | 1.0 / 0.23 | [VnExpress 27/11](https://vnexpress.net/hang-phan-mem-lon-nhat-chau-au-co-the-sa-thai-10-000-nguoi-5149433.html) | 5.27 quỹ dự phòng (củng cố B-thuongtet-01) | DARK |

## TikTok signals (Apify + Radar, 27/11/2026)
| keyword / nguồn | clip | xem / comment / share | hook / transcript snippet | sound | brand-safe? | bridge |
|---|---|---|---|---|---|---|
| hoc tap | [@minggbest](https://www.tiktok.com/@minggbest/video/7696495062217248018) · 59s | 796.400 / 901 / 43.200 | caption: «Trung bình văn mẫu của mấy đứa học tiếng Anh: Top 1: "Từ này nhìn quen lắm"» | gốc | ok | B-nhinquen-01 |
| radar direct_niche | [@phamthuykieuhuong](https://www.tiktok.com/@phamthuykieuhuong/video/7711338098323410196) · 11s | 1.700.000 / 1.173 / 11.400 | text: «U30 (28 tuổi) học lớp 11 GDTX: 65k/tháng, đi gần 60km/ngày, học hơn 10 tiếng/ngày…» | pop/synth-pop (không dùng) | caution (người thật) | B-u30batdau-01 (ARC-003) |
| hoc tap / ghi nho | [@gonaox](https://www.tiktok.com/@gonaox/video/7702426588662598920) · 168s | 1.900.000 / 818 / 31.000 | VTT: «ghi nhớ bất cứ thứ gì nhanh đến mức khó tin…» | gốc | ok | củng cố B-nhinquen-01 |
| tri hoan | [@carter.selfdev](https://www.tiktok.com/@carter.selfdev/video/7701501687999270164) · 108s | 474.700 / 276 / 19.600 | VTT: «để ngày mai rồi tính… điều đáng sợ nhất của trì hoãn…» | gốc | ok | bão hoà (chỉ bằng chứng) |
| tam ly | [@vutru_codai](https://www.tiktok.com/@vutru_codai/video/7709041076987858197) · 186s | 173.000 / 72 / 1.110 | VTT: «SAO tôi cứ thấy mình ngượng thế…» (bận tâm ánh mắt người khác) | gốc | ok | củng cố 3.21 (#20) |

## Learning
- **ARC-003 mới (`@phamthuykieuhuong`, 1,7M view, 11s):** bảng 6 số liệu tương phản danh tính + 2 chi tiết tự giễu + mục tiêu đo được cho thấy nhịp giữ chân rất mạnh mà không cần khẩu hiệu động lực.
- **Black Friday 27/11 không còn hiệu ứng "săn đơn lớn" như trước (VnExpress):** góc hay cho 5.1 là lật từ "bớt săn sale lớn" sang "tiền vẫn rò rỉ đều qua sale ngày đôi + gói tự trừ nhỏ".
- **Bão hoà nên tránh:** trì hoãn góc thẳng (`@carter.selfdev`, `sat=0.65`), AI lấy việc / cắt giảm nói chung (`SAP` chỉ nên dùng làm bằng chứng phụ cho quỹ dự phòng 5.27), listicle dạy học chung chung.
- **Patterns cập nhật:** không thêm P-row mới; tăng `seen` cho `P01`, `P03`, `P04`, `P05`, `P06`, `P10`, `P13`, `P15`, `F07`.

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-blackfriday-01 | Người tiêu dùng bớt mặn mà với Black Friday (VnExpress 27/11) | không chen mua Black Friday mà mở sao kê cuối tháng tiền vẫn mất vào mấy gói tự trừ + đơn sale ngày đôi | 5.1 (+5.23) | "Hôm nay Black Friday, báo đưa tin người tiêu dùng bớt mặn mà săn sale rồi. Nghe có vẻ năm nay mình giữ tiền giỏi hơn, đúng hông?" (P05+P03) | contrarian / empathy | đăng #28 (5.1) | DARK |
| B-gta6-01 | GTA 6 ra mắt làm sụt năng suất nhân viên (GNews US + Trends US + Verge) | bật game chơi 1 tiếng xả stress, câu «nốt nhiệm vụ này thôi» kéo thẳng tới 2h sáng | 4.15 (+3.9) | "GTA 6 vừa ra, cả mạng bàn chuyện dân văn phòng tụt năng suất. Mình hông bảo bạn bỏ game đâu, vì mình cũng mê mà." (P01+P15) | humor / empathy | đăng #10 (4.15) | LIGHT |
| B-nhinquen-01 | TikTok `@minggbest` «Từ này nhìn quen lắm» (796k) + `@gonaox` (1,9M) | đọc tài liệu công việc / sách kỹ năng thấy đoạn nào cũng «quen quen», tới lúc cần áp dụng thì đầu trống trơn | 23.14 | "Trên mạng đang rộ câu văn mẫu: «từ này nhìn quen lắm». Mà bạn có để ý không, lúc đọc tài liệu thấy quen là lúc não dễ lừa mình nhất?" (P01+P03) | contrarian / data | đăng #25 (23.14) | DARK |
| B-iosupdate-01 | Genk: không lộ OTP, không tải app lạ vẫn mất tiền vì mã độc web nhắm iOS cũ (DarkSword/Coruna) | thấy thông báo cập nhật hệ điều hành là bấm «để tối nay» cả tháng trời | 14.10 / 14.6 | "Không bấm link lạ, không đọc mã OTP cho ai mà điện thoại vẫn có thể bị xâm nhập chỉ vì lướt trúng trang web lỗi? Đừng để nút cập nhật hệ điều hành nằm chờ cả tháng nữa." (P04+P10) | data / contrarian | đăng #29 (14.10) hook thay thế | DARK |
| B-u30batdau-01 | TikTok `@phamthuykieuhuong` U30 học lớp 11 GDTX (1,7M, ARC-003) | gần 30 tuổi muốn học kỹ năng mới nhưng cứ ngại «trễ quá rồi» | 4.12 | "Gần 30 tuổi mới bắt đầu học lại từ con số 0, bạn nghĩ mình đang đi trễ hay đang cầm một lợi thế ngầm?" (P04+P15, ARC-003) | empathy / story | ý tưởng mới / callback clip-06 | LIGHT |
| B-aimode-01 | VnExpress: Nhiều trang web mất khách vì Google AI Mode trả lời thay | đọc xong 3 dòng AI tóm tắt tưởng mình nắm hết rồi, 10 phút sau kể lại thì không nhớ | 23.16 / 3.6 | "Google giờ trả lời thay luôn khỏi cần bấm vào trang web. Tiện thiệt, nhưng đọc ba dòng tóm tắt xong, mười phút sau bạn còn nhớ được gì?" (P03+P10) | contrarian | ý tưởng `@vanhiep.tech` + `@hi.oneup` | DARK |

## Differentiation
- **B-blackfriday-01.** Mọi người đang nói: người tiêu dùng tỉnh táo hơn, bớt mặn mà với Black Friday vì quanh năm đã có sale ngày đôi ([VnExpress 27/11](https://vnexpress.net/nguoi-tieu-dung-bot-man-ma-voi-black-friday-5149368.html)); báo tech thì đăng bài săn deal ([Genk 27/11](https://genk.vn/black-friday-san-deal-gia-dung-tu-panasonic-locklock-elmich-gia-tot-bat-ngo-nhieu-mon-con-165261127082941891.chn)). Góc của mình: không mua đợt lớn chưa chắc đã dư tiền hơn — tiền rò rỉ đều qua mấy khoản tự gia hạn và đơn nhỏ quanh năm (5.1). +1 tối nay: mở sao kê 30 ngày, tắt 1 khoản tự trừ đã quên.
- **B-gta6-01.** Mọi người đang nói: thống kê sụt năng suất vì GTA 6 ([GNews US](https://news.google.com/rss/articles/CBMiwgFBVV95cUxQVzRHOU5YVU9IaXUtMndpYVh1NVhfS1pTNmQ4UFRyRFJoRnhDUzV2akZ1bjktQjBnNHVxdExrZHRQX0hkRFJhU2w1bEtubzZPWEI4UnBUb0g0T0x3cV9weGR2UHRMU2RhcnhLQ3IzVTFuN3Qyd2RYTGplNzZ2NTlTVVdzZ1VmUWlweWpjTXBmM3R1cUtTS1hOc2hBN0RqeVppUGNJU2xINnZUZDFPbm12b3hWd09KdTRPUmNaN2lfQzFBQQ?oc=5)) hoặc review kết thúc game ([The Verge](https://www.theverge.com/entertainment/1043362/grand-theft-auto-6-ending)). Góc của mình: tự nhận mình cũng mê game (P15), không khuyên bỏ game; đặt giới hạn cứng giờ dừng TRƯỚC khi bấm Play (4.15) để chơi đã mà không vật vờ sáng hôm sau.

## Plan stubs
- `research/trends/2026-11-27/plans/plan-1-black-friday-sale-ngay-doi-ro-tien.json` — validate **✔** (9 scenes, 61.00s, DARK, `status: stub-needs-approval`).
- `research/trends/2026-11-27/plans/plan-2-gta6-gioi-han-cung-gio-choi.json` — validate **✔** (8 scenes, 53.00s, LIGHT, `status: stub-needs-approval`).

## Script hooks (cần duyệt)
1. (B-blackfriday-01, P05+P03) "Hôm nay Black Friday, báo đưa tin người tiêu dùng bớt mặn mà săn sale rồi. Nghe có vẻ năm nay mình giữ tiền giỏi hơn, đúng hông?"
2. (B-gta6-01, P01+P15) "GTA 6 vừa ra, cả mạng bàn chuyện dân văn phòng tụt năng suất. Mình hông bảo bạn bỏ game đâu, vì mình cũng mê mà."
3. (B-nhinquen-01, P01+P03) "Trên mạng đang rộ câu văn mẫu: «từ này nhìn quen lắm». Mà bạn có để ý không, lúc đọc tài liệu thấy quen là lúc não dễ lừa mình nhất?"
4. (B-iosupdate-01, P04+P10) "Không bấm link lạ, không đọc mã OTP cho ai mà điện thoại vẫn có thể bị xâm nhập chỉ vì lướt trúng trang web lỗi?"

## Safety notes
- **B-blackfriday-01:** không nêu tên thương hiệu/sàn TMĐT hay tên người được phỏng vấn trong bài VnExpress; bỏ quy định nền tảng Trung Quốc của mục 5.1.
- **B-gta6-01:** không trích số % sụt năng suất vào voice khi chưa tự kiểm bài gốc Baltic News Network; không dùng footage game.
- **B-nhinquen-01:** tuân thủ L-087 — chỉ mượn câu trend làm hook, chuyển ví dụ sang đọc sách kỹ năng / tài liệu công việc, không lấy môn học phổ thông.
- **B-u30batdau-01:** `caution` người thật — tuyệt đối không nêu tên/vẽ creator, chỉ học cấu trúc bảng số liệu `ARC-003`.
