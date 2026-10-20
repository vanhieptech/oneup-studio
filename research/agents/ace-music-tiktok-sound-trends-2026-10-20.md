---
title: "ACE Music: nhạc/âm thanh TikTok cho @hi.oneup — CML, trend niche học tập, bộ mood theo beat"
date: 2026-10-20
source: "Dữ liệu Apify có sẵn trong research/trends/2026-10-16..20 + tra web 20/10/2026 (Asia/Saigon)"
id: research.ace-music.tiktok-sound-trends
type: research
status: reference
updated: 2026-10-20
tags: [ace-music, tiktok, commercial-music-library, sound-note, hi.oneup]
---
# Nhạc/âm thanh TikTok cho @hi.oneup (20/10/2026)

Phạm vi: chỉ nghiên cứu. Không tải nhạc, không chèn gì vào video (rule-21), không commit.
Ký hiệu: **[FACT]** = có nguồn ghi kèm · **[ĐỀ XUẤT]** = ý kiến của ACE Music, chưa kiểm bằng dữ liệu · **[CHƯA XÁC MINH]** = có nguồn một phần nhưng thiếu bước kiểm quyết định.

## 0. Rule nội bộ đang áp dụng (đọc 20/10/2026)
- `rules/video-rules.md` luật 21: không có nhạc trong file; Hiệp thêm nhạc từ TikTok Commercial Music Library (CML) lúc đăng.
- Luật 53 mục 8 (gói đăng): "Âm thanh: thêm từ Commercial Music Library, mood gợi ý, mức âm lượng".
- `templates/post-package.md` mục 8: lo-fi / chill acoustic, không lời; giọng gốc 100%, nhạc 5–10%. Mục 9: "Nội dung thương mại / quảng cáo: OFF".
- `logs/lessons.md` (đến L-059…): không có lesson riêng về nhạc; L-059 yêu cầu bản trình script có cột sound/SFX từng beat (đó là SFX trong file, không phải nhạc).

## 1. TikTok Commercial Music Library — fact có nguồn
1. **[FACT]** CML là thư viện nhạc "pre-cleared", khoảng 1 triệu bài, miễn phí cho doanh nghiệp; doanh nghiệp không được dùng thư viện nhạc chung cho mục đích thương mại, kể cả bài đăng organic, duet/stitch, quảng cáo, branded content. Dùng "original sound" của người khác thì phải tự lo giấy phép. — https://ads.tiktok.com/help/article/commercial-music-library?lang=en
2. **[FACT]** Tài khoản Business: bấm Add Sound chỉ thấy "Commercial Sounds". Tài khoản cá nhân: thấy mọi âm thanh; muốn chọn CML thì bấm Sounds → chọn "Commercial Sounds" trong menu thả xuống. Trên web (Creative Center) lọc được theo khu vực, vị trí dùng (placement), theme, thể loại, mood, thời lượng; hiển thị tối đa 10.000 bài một lúc. — https://ads.tiktok.com/resources/help/article/how-to-use-the-commercial-music-library
3. **[FACT]** Music Terms: nhạc trong thư viện chung ("Sounds") chỉ cho mục đích cá nhân, phi thương mại; không dùng để gắn với hay quảng bá thương hiệu/doanh nghiệp. Commercial Sounds dành cho "Commercial User" — gồm cả **cá nhân** dùng nền tảng với mục đích thương mại — và được dùng để quảng bá thương hiệu. Commercial User không nên dùng Original Sound do người khác tải lên. Nhạc nói chung: không chỉnh sửa làm đổi bản chất bài có bản quyền, không dùng audio tách rời video. — https://www.tiktok.com/legal/page/global/music-terms-us/en
4. **[FACT]** Trợ giúp TikTok: khi đăng nội dung quảng bá thương hiệu/sản phẩm/dịch vụ, khuyến nghị chỉ dùng CML; nếu bật "content disclosure" mà dùng nhạc ngoài CML thì phải đồng ý "Music Usage Confirmation" (xác nhận không có nhạc bản quyền hoặc đã mua đủ license). — https://support.tiktok.com/en/business-and-creator/creator-and-business-accounts/commercial-use-of-music-on-tiktok
5. **[FACT]** Theo tổng hợp CML User Terms (Sume, đọc 28/09/2026): quyền thương mại chỉ trong TikTok, không được mang nhạc CML sang nền tảng khác (YouTube, Reels…); TikTok mất quyền một bài thì có thể gỡ hoặc tắt tiếng video dùng bài đó. — https://www.sume.com/blog/tiktok-commercial-music-library (nguồn thứ ba, tóm tắt điều khoản của TikTok)
6. **[FACT]** Creative Center tab Trends → Songs có ô "Approved for business use" để chỉ hiện âm thanh đã được duyệt dùng thương mại. — https://www.highsocial.com/resources/how-to-access-tiktok-commercial-music-library/ (nguồn thứ ba)

**Áp vào @hi.oneup — [ĐỀ XUẤT]:**
- Kênh hiện là tài khoản cá nhân, mục 9 gói đăng để "Nội dung thương mại: OFF". Dùng CML là lựa chọn an toàn hơn mức tối thiểu, đúng rule-21, và **bắt buộc** nếu sau này video quảng bá app/sản phẩm (theo #3, #4).
- Vì quyền CML chỉ trong TikTok (#5): khi đăng lại lên YouTube Shorts/Reels thì đăng bản **không nhạc** (đúng file gốc từ pipeline), không xuất lại bản TikTok đã có nhạc.
- Không dùng nhạc trend bản quyền hay "âm thanh gốc" của người khác, dù clip VN top đang dùng (xem mục 2).

## 2. Dữ liệu trend có sẵn trong repo (Apify, 16–20/10/2026)
Nguồn: `research/trends/2026-10-16..20/apify/raw-clockworks.json` (trường `musicMeta`) và `clips.json` (trường `music`). Ngày = ngày chạy actor (giờ VN), xem `run-meta.json`.

- **[FACT, dữ liệu nội bộ]** 209 clip đã scrape: 145 dùng âm thanh gốc (`musicOriginal: true`), 23 dùng nhạc/âm thanh không phải gốc, 41 không có trường này. Trong shortlist `clips.json` 5 ngày (32 clip), gần như tất cả là "âm thanh gốc / nhạc nền - <tên kênh>" — tức giọng nói của chính creator (có thể có nhạc chìm, không tách được từ metadata).
  → Clip VN top niche học tập/công sở thắng nhờ **lời nói**, không nhờ nhạc trend. Khớp hướng của kênh: nhạc chỉ là lớp nền 5–10%.
- Các track không phải âm thanh gốc gặp trong clip niche học tập/phát triển bản thân/công sở:

| Ngày data | Track (tên chính xác trong metadata) – tác giả | Clip | View | Ghi chú |
|---|---|---|---|---|
| 17/10 (cũng có trong 16/10 clips.json) | `vlog, chill out, calm daily life(1370843)` – SUNNY HOOD STUDIO | https://www.tiktok.com/@giaimatrend.vn/video/7694889719036923154 (giải mã trend câu giảng Vật lí 11) | 73,1K | Chill, nhẹ. Tên có số trong ngoặc — kiểu đặt tên của nhạc thư viện production. Toklytics: 495 video, 241,9M view tổng (https://toklytics.app/sound/7179679214566639618); kworb xếp #27 TikTok trending US, #15 AU (trang không ghi ngày, đọc 20/10/2026: https://kworb.net/charts/tiktok/us.html). **CML: [CHƯA XÁC MINH]** |
| 19/10 | `Vlog Video work Fashionable BGM(847726)` – Tsuyoshi_san | https://www.tiktok.com/@kieu06011993/video/7361063393723288840 ("Sống sót nơi công sở", #LearnOnTikTok) | 53,7K | BGM vlog công việc. **CML: [CHƯA XÁC MINH]** |
| 20/10 | `Coffee and Daydreams` – Tokyo.Beats & Tokyo.BeatsCreation | https://www.tiktok.com/@sam.siu.gap/video/7628203838675094802 (cafe học tập) | 89,6K | Lofi cafe. **CML: [CHƯA XÁC MINH]** |
| 18/10 | `Windy Hill` – 羽肿 | https://www.tiktok.com/@abbeytri/video/6972530116371025154 ("6 cách vượt qua lười biếng", đăng 2021) | 324K | Piano nhẹ, hay gặp trong clip động lực. Clip cũ; khả năng là nhạc phát hành thương mại → **không dùng nếu không thấy trong Commercial Sounds** |
| 18/10 | `Thay Đổi Bắt Đầu Từ Bên Trong` – Tiệm Sách Cũ | https://www.tiktok.com/@aphongnauan_88/video/7590644440314744072 | 34,2K | Không thuộc niche trực tiếp; chỉ tham khảo |

- Các track khác trong data (Savage, Messy, FREAKED OUT, Waiting for Love, As Long As You Love Me (Remix)…) là nhạc pop/remix bản quyền, phần lớn ở clip ngoài niche → **loại**.

## 3. Âm thanh lofi/study có nguồn trên web (20/10/2026)
- **[FACT]** `Calm Lofi/Cafe/Study/Vlog(1492712)` – Tana Music: Toklytics ghi 631 video, 19M view tổng, trung bình 30,2K view/video. — https://toklytics.app/sound/7291361232103294977
- **[FACT]** `Study Routine (Lofi)` – The Machinist Beats: Toklytics ghi 70 video, 2,8M view tổng, trung bình 39,6K. — https://toklytics.app/sound/7429837346730035201
- **[FACT]** `Cool Nights (Lofi)` – The Machinist Beats: Toklytics ghi 81 video, 2,5M view tổng. Danh sách video dùng có nhiều tài khoản thương hiệu (Dove, rhode…). — https://toklytics.app/sound/7430887976304674833
- **[CHƯA XÁC MINH]** cả ba có nằm trong CML khu vực Việt Nam hay không. Việc nhiều tài khoản thương hiệu dùng chỉ là dấu hiệu, không phải bằng chứng.
- **[FACT, ngoài niche]** BXH TikTok trending VN trên kworb (đọc 20/10/2026, trang không ghi ngày cập nhật) toàn nhạc V-pop/remix bản quyền (vd "Mật Ngọt - Nam Con Remix") — https://kworb.net/charts/tiktok/vn.html → không hợp và không an toàn cho kênh.

## 4. Bộ mood theo beat của format @hi.oneup — [ĐỀ XUẤT]
Quan trọng: TikTok chỉ gắn **một** track cho cả video (chọn được điểm bắt đầu). Nên bảng dưới là cách **chọn một track có đường năng lượng hợp với clip** + chọn điểm bắt đầu, không phải đổi nhạc theo beat. Nhạc luôn nằm dưới giọng: giọng 100%, nhạc 5–10% (rule kênh).

| Beat | Năng lượng muốn có | Loại nhạc | BPM gợi ý | Nhạc cụ | Mức âm lượng | Từ khoá tìm trong CML |
|---|---|---|---|---|---|---|
| Hook 0–3s | Mở gọn, không lấn lời đầu (lời ≤0,3s, luật 55) | Track vào ngay bằng pad/piano mỏng, không intro trống dài, không drop | 70–90 | Piano/Rhodes, pad, vinyl crackle | 5% (thấp nhất) | `lofi study`, `calm piano`, `chill vlog` |
| Nỗi đau / ví dụ | Chùng, hơi lửng | Lofi minor/7th chord, nhịp chậm | 70–85 | Rhodes, bass mềm, kick nhẹ | 5–8% | `lofi sad`, `melancholy piano`, `rainy lofi` |
| Giải thích / bằng chứng | Trung tính, rõ, không cảm xúc mạnh | Lofi/ambient đều nhịp, ít giai điệu | 75–90 | Pad, hi-hat nhẹ, pluck | 5–7% (lời dày chữ, số liệu) | `ambient study`, `focus`, `minimal lofi` |
| How-to | Đều tay, tiến lên | Lofi hip-hop / chill acoustic nhịp đều | 80–95 | Guitar mộc, Rhodes, shaker | 7–10% | `chill acoustic`, `daily routine`, `cafe lofi` |
| Kết quả / CTA | Ấm, sáng, nhẹ nhõm | Major key, sáng nhẹ | 80–95 | Ukulele/guitar, glockenspiel nhẹ | 8–10% | `warm acoustic`, `happy lofi`, `positive vlog` |

Theo theme (luật 17):
- **Light** (sáng, ban ngày): chill acoustic / "cafe lofi" major key, 85–95 BPM, guitar mộc + Rhodes. Từ khoá: `chill acoustic`, `cafe`, `vlog daily life`.
- **Dark** (tối, học khuya): lofi piano / ambient, 70–85 BPM, Rhodes + pad + vinyl crackle, ít percussion. Từ khoá: `lofi night`, `late night study`, `calm piano`.

Quy tắc chung [ĐỀ XUẤT]: không lời (instrumental), không drop/build lớn trong 60s đầu, không tiếng chuông/notification trùng SFX `tick`/`ding` của clip, tránh track có tiếng hát bè hoặc sample giọng nói (lẫn với giọng F5). Nghe thử ở 5–10% trên loa điện thoại: nếu còn nghe rõ giai điệu đè chữ thì hạ về 5%.

## 5. Chưa xác minh được / giới hạn
- **Không mở được CML trực tiếp:** trang Creative Center CML (`ads.tiktok.com/business/creativecenter/music/...`) qua WebFetch bị chuyển sang trang Symphony; trang `tiktok.com/music/...` trả về trang lỗi/khung rỗng từ box (không có dữ liệu bài). Rule kênh luật 57 cũng cấm dùng Creative Center làm nguồn trend. → Không xác nhận được bài nào ở mục 2–3 có trong CML khu vực VN.
- Toklytics/kworb là nguồn thứ ba; số liệu có thể khác TikTok thật; kworb không ghi ngày cập nhật trên trang.
- Không chạy actor Apify mới (chỉ đọc dữ liệu đã có), nên không có dữ liệu "Approved for business use".
- Cách kiểm cuối cùng (Hiệp làm lúc đăng, 1 phút): trong app → Thêm âm thanh → Sounds → **Commercial Sounds** → tìm tên bài. Có thì dùng; không có thì dùng từ khoá ở mục 4.
