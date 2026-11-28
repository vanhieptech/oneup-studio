---
title: "Trend digest 2026-11-28"
source: "pipeline/scripts/trend-collect.py + radar-fetch.py + tinyfish_client.py + apify-run.py"
id: trends-2026-11-28
type: trend-digest
status: draft-needs-review
updated: 2026-11-28
tags: [trends, digest, daily]
date: 2026-11-28
collector: pipeline/scripts/trend-collect.py + radar-fetch.py + apify-run.py + tinyfish_client.py
skill: trend-digest v5.2.0
---
# Trend digest 2026-11-28 (thứ Bảy)

**Nguồn (chiều, `trend-collect.py` + `x-extra.json`):** 53/53 ok. 617 thô → 587 cụm. An toàn tự động: 521 ok · 12 caution · 54 drop. Sáng cùng ngày collector là 51/52 vì `gnews-us-tiktoktrend` HTTP 429; chiều nguồn đó trả 10 mục. `raw.json` giữ bản chấm tay buổi sáng (582 mục, 491 qua lọc) vì cụm chiều chưa chấm lại từng dòng.
**X:** `search_news` có 3 story trong `x-extra.json` (Focus Mode 01/11, hối hận video ngắn 01/11, lấy lại sự tập trung 20/11). `get_trends_by_woeid` 23424984 lỗi `Client Forbidden` / `user-not-enrolled` / Pay-per-use, `https://console.x.com`. Đã gọi lại một lần, cùng lỗi. Không ghi `x: unavailable`.
**TinyFish → Apify:** 25 link trong `tinyfish/tiktok-candidates.json` đo đủ (`--urls-from`, `--comments 25`). 25 clip, 15 subtitle, comment cho cả 25, 12 trường đủ 96–100%. Chi phí đo này $0.0935 (scraper) + $0.38 (304 comment). Cộng giỏ sáng, **hôm nay $0.6775**, vượt trần `apify.yaml` $0.50. Giỏ hashtag sáng (40 clip, 26 VTT, comment 3 clip, $0.204) chuyển sang `apify-basket/`.
**Ego-browser:** search TikTok 4 cụm (`nghiện điện thoại`, `dẹp điện thoại`, `điện thoại úp bàn`, `tập trung làm việc`) trả 0 thẻ. Trang search mở bằng Ego Lite 0.6.3.17 rồi hiện `Something went wrong`.
**Radar chiều (`radar-fetch.py --use-ego --with-comments`):** cache ấm, 175 clip, **0 outlier mới**, 38 clip đã thấy. Lần chạy ghi đè `radar.json` thành bảng mỏng nên hoàn lại bản sáng **30 outlier**. Inbox: 0 file mới.

Dữ liệu: `collect.json`, `radar.json`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `apify/`, `tinyfish/`, `teardowns/`.

## Luồng 1 — Outlier Radar (`radar.json`, 30 outlier — tiêu biểu đúng ngách)
| creator | view | outlier | chủ đề | góc khai thác | link |
|---|---|---|---|---|---|
| `@thomasfrank` | 857.000 | median≥3.0x | hoc-tap, productivity | **Đã teardown → ARC-003**: gọi tên sức ỳ (`hit resistance`) → đảo mục tiêu Output sang Input (4.7 / 4.9) | [YT Shorts](https://www.youtube.com/shorts/7Co-TmrLiYk) |
| `@healthygamergg` | 487.000 | median≥3.0x | tu-duy, productivity | **Đã teardown → ARC-003**: GTA VI «chores simulator» → nghịch lý chăm làm việc giả lập trên app hơn ngoài đời (4.9 / 3.14) | [YT Shorts](https://www.youtube.com/shorts/PlswZxxapn4) |
| `@tramdungtrithuc` | 1.100.000 | 14.59x (v/f) | tu-duy, hoc-tap | Bị nói kháy công sở → 3.17 / 3.23 hạ nhiệt thay vì bật lại theo cơn nóng | [TikTok](https://www.tiktok.com/@tramdungtrithuc/video/7710946714219236626) |
| `@dangde.suyngam` | 1.100.000 | 30.47x (v/f) | tu-duy | Lập kế hoạch tích luỹ lúc còn kiếm được tiền → củng cố quỹ dự phòng 5.27 | [TikTok](https://www.tiktok.com/@dangde.suyngam/video/7707949451339402503) |
| `@parentlab3` | 502.700 | 13.93x (v/f) | hoc-tap, ai | Quy tắc «3 lần nhớ» → đối chiếu retrieval practice 23.14 (đời thường, L-087) | [TikTok](https://www.tiktok.com/@parentlab3/video/7684183085755190548) |
| `@thnguyen.y` | 1.700.000 | 122.3x (v/f) | hoc-tap | Hành trình kiên trì từ số 0 → bằng chứng phụ 4.12 (caution người thật) | [TikTok](https://www.tiktok.com/@thnguyen.y/video/7663776976519384340) |
| `@ngocanhh0565` | 216.300 | 217.61x (v/f) | productivity, hoc-tap | Tự giễu dồn sức sai chỗ → áp sang công việc/dự án (L-087) | [TikTok](https://www.tiktok.com/@ngocanhh0565/video/7707619983878065429) |
| `@johnnyharris` | 148.000 | median≥3.0x | storytelling, khoa-hoc | `cross_niche_craft`: nhịp dẫn chuyện bản đồ & mở vòng lặp câu chuyện | [YT Shorts](https://www.youtube.com/shorts/TAV5Prbponw) |
| `@fireship` | 5.200.000 | median≥3.0x | tech, storytelling | `cross_niche_craft`: nhịp cắt 2–3s, ẩn dụ tech cho `@vanhiep.tech` | [YT Shorts](https://www.youtube.com/shorts/aXcuz6fn8_w) |

*(Các row ngoài ngách như `anaiscastillo109`, `realnezzdapoet` đã gắn `angle: "off-niche"`; các clip cũ của `phamthuykieuhuong`, `manghocls` giữ ghi chú đã teardown.)*

## Luồng 2 — Upstream Tech & VN-Tech (`trend-streams.py upstream --check` ✔)
| tin | luồng | pain | story | `@hi.oneup` | `@vanhiep.tech` | score | kênh |
|---|---|---:|---:|---:|---:|---:|---|
| Thần đồng Terence Tao kêu gọi chuyển sang 'toán học 2.0' vì AI (caution tên GS) | vn-tech | 4 | 5 | 4 | 5 | **0.80** | `vanhiep_tech` |
| I deleted three productivity apps this week. (Reddit r/productivity) | upstream | 5 | 4 | 5 | 3 | **0.80** | `hi_oneup` |
| Credit card skimming scripts using WebRTC found on popular shopping sites (HN) | upstream | 5 | 4 | 4 | 5 | **0.80** | `vanhiep_tech` |
| Convex skills send the user's app idea to a remote server without telling them (HN) | upstream | 5 | 4 | 3 | 5 | **0.80** | `vanhiep_tech` |
| Whatever happened to programming? "Today, I mostly paste libraries..." (Reddit) | upstream | 4 | 4 | 2 | 5 | **0.64** | `vanhiep_tech` |
| You ever have a super-productive start to the week... (Reddit r/productivity) | upstream | 4 | 4 | 4 | 3 | **0.512** | `hi_oneup` |
| Why optimistic updates are corrosive (Lobsters) | upstream | 3 | 4 | 1 | 5 | **0.48** | `vanhiep_tech` |
| How iFood scales coding agents across 15,000 repositories (OpenAI) | upstream | 3 | 4 | 2 | 5 | **0.48** | `vanhiep_tech` |
| Copilot code review billing will default to the organization (GitHub) | upstream | 4 | 3 | 2 | 4 | **0.384** | `vanhiep_tech` |
| GPT 6.2 Astra Solves a Historical Mystery (HN) | upstream | 3 | 4 | 2 | 4 | **0.384** | `vanhiep_tech` |
| Nvidia 'yêu cầu đối tác dừng chuyển chip đến bốn nước Đông Nam Á' (caution) | vn-tech | 3 | 3 | 1 | 4 | **0.288** | `vanhiep_tech` |
| Apple chiếm 57% thị phần smartphone Mỹ khi khủng hoảng chip nhớ bóp Android giá rẻ | vn-tech | 3 | 3 | 2 | 4 | **0.288** | `vanhiep_tech` |
| Curb impacts of AI on programming to maintain EU sovereignty (Lobsters) | upstream | 3 | 3 | 2 | 4 | **0.288** | `vanhiep_tech` |

## Luồng 3 — Mobile / Manual Inbox (`media/footage/inbox/`)
- `0 mới, 0 trùng` (hộp thư trống hôm nay).

## Viral DNA & ARC (teardown)
- **Hoàn thành (2):**
  1. `trends-2026-11-28-04` — `@thomasfrank` (857k view, EN `global_niche_source`) → [`teardowns/trends-2026-11-28-04.md`](teardowns/trends-2026-11-28-04.md). Gọi tên sức ỳ (`hit resistance`) + cặp đối lập `Output-based → Input-based` + đồng hồ Pomodoro vật lý (`external motivator`).
  2. `trends-2026-11-28-01` — `@healthygamergg` (487k view, EN `global_niche_source`) → [`teardowns/trends-2026-11-28-01.md`](teardowns/trends-2026-11-28-01.md). Dùng GTA VI («chores simulator») lật định nghĩa mộng tưởng: tại sao nhiều người chăm làm việc nhà/tập gym trong game hơn ngoài đời.
- **ARC cập nhật:** **`ARC-003`** tăng thêm +2 bằng chứng (tổng 4 bằng chứng trong `research/trends/patterns.md`).
- **Ý tưởng tự đẩy vào `content/idea-bank.md` (+4):**
  - `@hi.oneup`: (1) đổi mục tiêu «phải xong» sang «có mặt 10 phút» kèm đồng hồ hẹn giờ; (2) nghịch lý chăm bấm hoàn thành thói quen cho nhân vật ảo trên app hơn làm thật ngoài đời.
  - `@vanhiep.tech`: (1) tách backlog/refactor lớn từ Output sang Input Timebox 25 phút; (2) hội chứng *Productivity Simulator* — dev tốn 4 tiếng config dotfiles/AI agent thay vì 10 phút làm xong việc.

## Top 10 (đã lọc)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---:|---:|---|---|---|
| 1 | TikTok `@tramdungtrithuc`: «Bị nói kháy đừng giải thích, hãy lặp lại và hỏi ngược» (1,1M view, 549 cmt, 6,7k share, 14.59x) | 1.067 | 1.0 / 0.04 | [TikTok @tramdungtrithuc](https://www.tiktok.com/@tramdungtrithuc/video/7710946714219236626) | 3.17 (+3.23) hạ nhiệt cơn nóng | DARK |
| 2 | Nghệ thuật quyến rũ của những người không có nhu cầu làm hài lòng thiên hạ (cs=2) | 1.066 | 1.0 / 0.04 | [Kenh14 28/11](https://kenh14.vn/nghe-thuat-quyen-ru-cua-nhung-nguoi-khong-co-nhu-cau-lam-hai-long-thien-ha-21526112807494151.chn) | 3.21 (+3.16) đăng #20 | LIGHT |
| 3 | GS Terence Tao kêu gọi chuyển sang «toán học 2.0» vì AI — chỉ công nhận khi tự giải thích được thứ AI viết (VnExpress + Google Trends VN 500+) | 1.014 | 1.0 / 0.05 | [VnExpress 28/11](https://vnexpress.net/than-dong-terence-tao-keu-goi-chuyen-sang-toan-hoc-2-0-vi-ai-5149544.html) | 23.14 đăng #25 (caution tên GS) | DARK |
| 4 | Reddit r/productivity: «I deleted three productivity apps this week» (xoá habit tracker, to-do, time blocking) | 0.994 | 1.0 / 0.03 | [Reddit](https://www.reddit.com/r/productivity/comments/1ukgb64/i_deleted_three_productivity_apps_this_week/) | 4.8 (+4.1) ô #27 | LIGHT |
| 5 | Muốn tự do phải có tiền, nhưng kiếm tiền phải đánh đổi sức khoẻ: Nghịch lý khi làm người lớn | 0.984 | 1.0 / 0.06 | [Kenh14 27/11](https://kenh14.vn/muon-tu-do-phai-co-tien-nhung-kiem-tien-phai-danh-doi-suc-khoe-nghich-ly-khi-lam-nguoi-lon-215261127222051053.chn) | 3.13 đăng #12 | DARK |
| 6 | TikTok `@parentlab3`: «Học mãi không vào, thử quy tắc 3 lần nhớ này» (502,7k view, 8,6k share, 13.93x) | 0.891 | 1.0 / 0.11 | [TikTok @parentlab3](https://www.tiktok.com/@parentlab3/video/7684183085755190548) | củng cố 23.14 / 23.15 (L-087) | DARK |
| 7 | TikTok `@dangde.suyngam`: «Hãy luôn học cách lập kế hoạch trước» lúc còn kiếm được tiền (1,1M view, 15,1k share, 30.47x) | 0.856 | 1.0 / 0.10 | [TikTok @dangde.suyngam](https://www.tiktok.com/@dangde.suyngam/video/7707949451339402503) | củng cố 5.27 quỹ dự phòng (caution) | DARK |
| 8 | Convex skills send the user's app idea to a remote server without telling them (HN) | 0.842 | 1.0 / 0.03 | [GitHub Issue](https://github.com/convex/convex-backend-skill/issues/64) | 14.10 đăng #29 / `@vanhiep.tech` | DARK |
| 9 | Credit card skimming scripts using WebRTC found on popular shopping sites (HN) | 0.754 | 1.0 / 0.03 | [InfoHawk](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) | 14.10 / 14.6 + `@vanhiep.tech` | DARK |
| 10 | TikTok `@thnguyen.y`: từ người không biết gì kiên trì học ngoại ngữ (1,7M view, 602 cmt, 122.3x) | 0.730 | 1.0 / 0.12 | [TikTok @thnguyen.y](https://www.tiktok.com/@thnguyen.y/video/7663776976519384340) | bằng chứng phụ 4.12 (caution) | LIGHT |

## TikTok signals (28/11/2026)

Giỏ sáng nằm ở `apify-basket/` (hashtag, không phải 25 link TinyFish). Bảng này là lớp view cao đúng ngách từ giỏ đó.

| keyword / nguồn | clip | xem / comment / share | hook / transcript snippet | sound | brand-safe? | bridge |
|---|---|---|---|---|---|---|
| tu duy / giao tiep | [@tramdungtrithuc](https://www.tiktok.com/@tramdungtrithuc/video/7710946714219236626) · 408s | 1.100.000 / 549 / 6.746 | VTT: «khi bị người khác xúc phạm mà không kịp phản ứng…» | gốc | ok | B-noikhay-01 |
| hoc tap | [@parentlab3](https://www.tiktok.com/@parentlab3/video/7684183085755190548) · 49s | 502.700 / 107 / 8.663 | VTT: «học mãi không vào thử quy tắc ba lần nhớ này…» | gốc | ok | củng cố 23.14 / B-toan20-01 |
| lap ke hoach | [@dangde.suyngam](https://www.tiktok.com/@dangde.suyngam/video/7707949451339402503) · 36s | 1.100.000 / 542 / 15.100 | caption: «Hãy luôn học cách lập kế hoạch trước» (VTT tiếng Trung: không phải năm nào cũng kiếm được tiền) | gốc | caution (tiền) | củng cố 5.27 |
| kien tri | [@thnguyen.y](https://www.tiktok.com/@thnguyen.y/video/7663776976519384340) · 66s | 1.700.000 / 602 / 8.882 | VTT: «từ một người không biết gì về tiếng Trung…» | gốc | caution (người thật) | bằng chứng 4.12 |
| tap trung | [@ngocanhh0565](https://www.tiktok.com/@ngocanhh0565/video/7707619983878065429) · 33s | 216.300 / 46 / 9.559 | caption: «bỏ các môn khác để tập trung 1 môn… cái xg điểm thấp tất» | gốc | ok | bằng chứng tự giễu (L-087) |

### 25 link TinyFish vừa đo (chiều)

Query `thoi quen` / `tri hoan` / `tap trung` / `quan ly thoi gian` kéo nhiều clip lệch từ khoá (cơm gà, Lăng Bác, trượt tuyết, hiến tóc). Xếp theo comment rồi view, chỉ giữ dòng đụng thói quen / tập trung / trì hoãn. Âm thanh đều là nhạc gốc trên clip.

| keyword | clip | xem / comment / share | hook / comment | brand-safe? | bridge |
|---|---|---|---|---|---|
| quản lý thời gian | [@tuthanvuonlen](https://www.tiktok.com/@tuthanvuonlen/video/7397788075708976402) · 135s | 617.200 / 171 / 2.653 | «Quy tắc 1-3-5». Comment: «xem xong cuối cùng quên, không thèm làm» | ok | người xem nhận ra mẹo rồi không làm — gần 3.1 / 4.x, không phải mẹo mới |
| trì hoãn | [@misslamdep19_01](https://www.tiktok.com/@misslamdep19_01/video/7553199316848971026) · 49s | 202.900 / 12 / 406 | «Cách để chữa sự trì hoãn» | ok | list chữa trì hoãn, bão hoà, comment không nói nỗi đau |
| mất tập trung | [@khanhvyccf](https://www.tiktok.com/@khanhvyccf/video/7572561134096633095) · 76s | 146.800 / 66 / 423 | «Nếu mất tập trung thì hay thử làm mấy việc này». Comment nhiều về mặt, không về việc | caution (người nổi tiếng) | list mẹo, không lấy làm góc |
| thói quen | [@thuyvinavi1602](https://www.tiktok.com/@thuyvinavi1602/video/7712066361492655380) · 249s | 90.900 / 42 / 1.349 | «7 thói quen giúp cuộc sống phất». Comment: «bạn nói nhanh quá» | ok | list 7 điều, bão hoà |
| tập trung bàn học | [@tranquocphuc.taovang](https://www.tiktok.com/@tranquocphuc.taovang/video/7538353920767397128) · 145s | 37.700 / 51 / 711 | «vì sao con không tập trung khi ngồi vào bàn học» | caution (L-087, học sinh) | không đưa ví dụ môn học vào lời thoại |

View cao nhưng lệch chủ đề, không bắc cầu: [@kaethykitchen](https://www.tiktok.com/@kaethykitchen/video/7474207141423811846) 1.800.000 view (cơm gà), [@sepannhan](https://www.tiktok.com/@sepannhan/video/7589154041150622983) 901.200 view / 2.157 comment (hài giận nhau).

## Learning
- **2 teardown EN củng cố `ARC-003`:** cả `@thomasfrank` (857k) và `@healthygamergg` (487k) đều đi theo cấu trúc gọi tên nỗi đau bằng một nhãn gọn / ví dụ phản trực giác → lật khung khái niệm → chốt bằng câu ngắn sắc không cần nhạc nền dày.
- **Đề xuất kênh mới (`suggested-channels.md`):** `@TED`, `@TEDEd`, `@JustinSung` (10,3M view về đọc nhớ lâu), `@TEDx`, `@easywayactually1` — Hiệp duyệt dòng nào thì dán vào `radar.yaml`.
- **Bão hoà nên tránh:** trì hoãn góc thẳng (`@carter.selfdev`, `@nhile_n`, YT niche `sat=0.40+`), học dồn 1 đêm (`@b.ch.phng.thi0` đã có `B-hoc1dem-01`), AI lấy việc nói chung.
- **Patterns cập nhật:** không thêm P-row mới; tăng `seen` cho `P01`, `P03`, `P04`, `P06`, `P08`, `P10`, `P12`, `P13`, `P15`, `F04`.

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-hailong-01 | Kenh14 (cs=2): Nghệ thuật quyến rũ của những người không có nhu cầu làm hài lòng thiên hạ | nhận lời mời lúc đã hết pin, ngồi gõ tin nhắn từ chối 10 phút với 3 lý do dài ngoằng vì sợ bị giận | 3.21 (+3.16) | "Bài báo đang hot hôm nay nói về khí chất của mấy người hông cần làm hài lòng thiên hạ. Mà nói thiệt, nhiều khi mình sợ từ chối hông phải vì hiền, mà vì tưởng ai cũng đang soi mình á." (P03+P10) | contrarian / empathy | đăng #20 (3.21) | LIGHT |
| B-toan20-01 | VnExpress + Trends VN: GS Terence Tao kêu gọi chuyển sang «toán học 2.0» vì AI | dán tài liệu 20 trang vô AI tóm tắt 5 gạch đầu dòng thấy mượt, vô họp bị hỏi ngược thì đứng hình | 23.14 | "GS Terence Tao vừa cảnh báo: giờ đầy bài nghiên cứu do AI viết mà chính người gửi cũng hông hiểu bên trong nói gì. Nghe xa xôi hả? Mà lần gần nhất bạn nhờ AI tóm tắt tài liệu rồi gửi sếp, bạn có giải thích lại được hông?" (P03+P10) | data / contrarian | đăng #25 (23.14) | DARK |
| B-xoa3app-01 | Reddit r/productivity: «I deleted three productivity apps this week» | cài đủ habit tracker, to-do, time blocking mà cuối tuần vẫn chưa mở việc chính | 4.8 (+4.1) | "Có người vừa lên mạng kể: tuần này tôi xoá sạch ba cái app năng suất. Nghe ngược đời hen, mà cài thêm app thứ tư có làm bạn bắt đầu sớm hơn hông?" (P15+P03) | humor / contrarian | ô #27 (LIGHT trống) | LIGHT |
| B-tienvasuckhoe-01 | Kenh14: Muốn tự do phải có tiền, nhưng kiếm tiền phải đánh đổi sức khoẻ | chạy deadline tới 1–2h sáng để mong dư tiền hơn, sáng hôm sau vật vờ làm không ra việc | 3.13 | "Nghịch lý ai cũng than: có tiền thì không có thời gian, có thời gian thì lo chuyện tiền. Mà bạn có biết sau một ngưỡng giờ làm, càng cố thức khuya càng ít ra việc hơn không?" (P10+P03) | contrarian / data | đăng #12 (3.13) | DARK |
| B-noikhay-01 | TikTok `@tramdungtrithuc`: «Bị nói kháy đừng giải thích, hãy lặp lại và hỏi ngược» (1,1M, 14.59x) | bị nói kháy trong cuộc họp/nhóm chat, tim đập nhanh muốn bật lại liền hoặc về nhà nghĩ cả tối | 3.17 (+3.23) | "Trên TikTok có clip hơn một triệu lượt xem dạy cách đáp trả khi bị nói kháy. Mà trước khi nghĩ câu phản pháo thật sắc, bạn có để ý cơn nóng đang lấy mất bao nhiêu tiếng tối nay của mình hông?" (P03+P10) | empathy / contrarian | ý tưởng mới 3.17 | DARK |
| B-skimmer-01 | HN: Convex skills gửi ý tưởng app lên server ngoài + WebRTC credit card skimmer mùa Black Friday | cài skill/extension AI lạ hoặc nhập thẻ mua deal nhanh mà không kiểm tra nguồn | 14.10 / 14.6 | "Mùa sale cuối năm và thời đại cài skill AI chỉ bằng một dòng lệnh: dữ liệu của bạn có thể đi ra ngoài mà màn hình chẳng hiện cảnh báo nào." (P04+P10) | data / contrarian | đăng #29 (14.10) + `@vanhiep.tech` | DARK |

## Differentiation
- **B-hailong-01.** Mọi người đang nói: khen khí chất lạnh lùng, bất cần của các ngôi sao không cần chiều lòng thiên hạ ([Kenh14 28/11](https://kenh14.vn/nghe-thuat-quyen-ru-cua-nhung-nguoi-khong-co-nhu-cau-lam-hai-long-thien-ha-21526112807494151.chn)). Góc của mình: hông cần đóng vai lạnh lùng (bỏ hết ví dụ người nổi tiếng) — vấn đề thật là hiệu ứng ánh đèn sân khấu khiến mình tưởng cả phòng đang chấm điểm câu từ chối của mình (3.21). +1 tối nay: từ chối một lời mời không hợp bằng đúng 1 câu gọn, lịch sự, không viết cả đoạn văn biện minh.
- **B-toan20-01.** Mọi người đang nói: AI giải toán giỏi quá, lo ngại sinh viên/chuyên gia bị thay thế ([VnExpress 28/11](https://vnexpress.net/than-dong-terence-tao-keu-goi-chuyen-sang-toan-hoc-2-0-vi-ai-5149544.html)). Góc của mình: lời nhắc thực dụng nhất của GS Terence Tao là *chỉ công nhận khi người gửi tự giải thích được thứ AI viết*. Đọc 5 gạch đầu dòng AI tóm tắt thấy mượt rất dễ dính ảo giác đã hiểu — gấp màn hình lại 30 giây, tự nói lại 3 ý chính bằng lời của mình (23.14).

## Plan stubs
- `research/trends/2026-11-28/plans/plan-1-khong-can-lam-hai-long-thien-ha.json` — validate **✔** (8 scenes, 56.00s, LIGHT, `status: stub-needs-approval`).
- `research/trends/2026-11-28/plans/plan-2-terence-tao-toan-hoc-2-0-giai-thich-lai.json` — validate **✔** (8 scenes, 56.00s, DARK, `status: stub-needs-approval`).

## Script hooks (cần duyệt)
1. (B-hailong-01, P03+P10) "Bài báo đang hot hôm nay nói về khí chất của mấy người hông cần làm hài lòng thiên hạ. Mà nói thiệt, nhiều khi mình sợ từ chối hông phải vì hiền, mà vì tưởng ai cũng đang soi mình á."
2. (B-toan20-01, P03+P10) "GS Terence Tao vừa cảnh báo: giờ đầy bài nghiên cứu do AI viết mà chính người gửi cũng hông hiểu bên trong nói gì. Nghe xa xôi hả? Mà lần gần nhất bạn nhờ AI tóm tắt tài liệu rồi gửi sếp, bạn có giải thích lại được hông?"
3. (B-xoa3app-01, P15+P03) "Có người vừa lên mạng kể: tuần này tôi xoá sạch ba cái app năng suất. Nghe ngược đời hen, mà cài thêm app thứ tư có làm bạn bắt đầu sớm hơn hông?"
4. (B-tienvasuckhoe-01, P10+P03) "Nghịch lý ai cũng than: có tiền thì không có thời gian, có thời gian thì lo chuyện tiền. Mà bạn có biết sau một ngưỡng giờ làm, càng cố thức khuya càng ít ra việc hơn không?"
5. (B-noikhay-01, P03+P10) "Trên TikTok có clip hơn một triệu lượt xem dạy cách đáp trả khi bị nói kháy. Mà trước khi nghĩ câu phản pháo thật sắc, bạn có để ý cơn nóng đang lấy mất bao nhiêu tiếng tối nay của mình hông?"

## Safety notes
- **B-hailong-01:** bỏ toàn bộ tên và ví dụ người nổi tiếng nước ngoài (Rihanna, Frank Ocean, Anna Wintour) trong bài Kenh14; giữ thuần góc tâm lý hiệu ứng ánh đèn sân khấu (3.21).
- **B-toan20-01:** `caution` tên nhà khoa học — chỉ trích phát biểu học thuật trung tính của GS Terence Tao, không vẽ chân dung người thật, không đưa số liệu khảo sát MIT chưa tự kiểm vào voice; tuân thủ L-087 (ví dụ đọc tài liệu công việc, không lấy môn học phổ thông).
- **B-tienvasuckhoe-01:** bỏ toàn bộ phần lão hoá sớm / bệnh lý trong bài Kenh14; chỉ nói về ngưỡng giờ làm giảm hiệu suất (3.13).
- **B-noikhay-01:** không chép câu thoại hay vẽ hình creator `@tramdungtrithuc`; giữ góc tự điều chỉnh cảm xúc (3.17 / 3.23).
- **B-skimmer-01:** không quy kết hay công kích nhà cung cấp cụ thể; tập trung vào thói quen kiểm tra quyền truy cập của skill/công cụ AI và bảo vệ thẻ thanh toán (14.10).
- **Apify 28/11:** tổng $0.6775, vượt trần ngày $0.50 vì comment 25 clip × 20 comment ($0.38). Lần sau giữ `--comments` đúng số link skill yêu cầu nhưng hạ `commentsPerPost` trước khi chạy, hoặc xin trần mới.
- **TinyFish chiều:** `@khanhvyccf` là người nổi tiếng, chỉ caution. `@tranquocphuc.taovang` là bàn học của con, L-087, không đưa vào lời thoại.
- **Chi phí Apify 28/11:** $0.6775, vượt trần ngày $0.50 vì comment 25 clip × 20 comment/clip ($0.38). Lần sau giữ `--comments` bằng số link đúng chủ đề, không kéo cả file ứng viên khi TinyFish trả clip lệch từ khoá.
- **@khanhvyccf:** caution người nổi tiếng. **@tranquocphuc.taovang:** caution L-087, không đưa ví dụ bàn học học sinh vào lời thoại.
