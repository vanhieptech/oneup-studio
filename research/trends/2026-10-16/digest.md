---
title: "Trend digest 2026-10-16"
source: "pipeline/scripts/trend-collect.py + X MCP extra + Apify TikTok-native"
id: trends-2026-10-16
type: trend-digest
status: draft-needs-review
updated: 2026-10-16
tags: [trends, digest, daily, apify]
date: 2026-10-16
collector: pipeline/scripts/trend-collect.py + X MCP + Apify clockworks/parseforge
skill: trend-digest v4
---
# Trend digest 2026-10-16

**Nguồn:** 34/36 collector (wiki-vi + wiki-en HTTP 404 — Wikimedia pageviews ngày trước chưa có lúc ~01:00 ICT). X MCP: trends VN 25 + worldwide 25 + 21 story X News → `x-extra.json` 71 mục. Apify TikTok-native: `clockworks/tiktok-scraper` run `GjDxjHOvo7LWub0CA` (40 raw → shortlist 9), comments `cQUZFOipRLSyacl6P` + `cYjVzTmCJDLGnzhVr` (120 comments), enrich `parseforge/tiktok-scraper` `SYCeL4YpNBeK1NNuP` (3 URL). Bỏ qua theo quy định: TikTok Creative Center / trends-scraper, Reddit, rsshub, lexis cookie actors, parseforge diacritic keywords.
**Số lượng:** collector 473 thô → 459 cụm; raw.json sau Apify = 468 mục (393 ok · 19 caution · 56 drop). Shortlist đọc tay: ~20 mục + 9 clip TikTok.
**Apify fields coverage:** 100% trên 12 trường bắt buộc (url, caption, author, play/like/share/comment, duration, music, hashtags, subtitle_or_transcript, top_comments) × 9 clip.
Dữ liệu: `collect.json`, `x-extra.json`, `apify/clips.json`, `raw.json`, `score.txt`, `ideas.json`, `plans/`.

## Top 10 (đã lọc, bỏ pattern-evidence bão hoà)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | Ngày càng nhiều người không còn đăng ảnh / cập nhật MXH | 1.030 | 1.0 / 0.07 | [Kenh14](https://kenh14.vn/vi-sao-ngay-cang-nhieu-nguoi-khong-con-dang-anh-hay-cap-nhat-thong-tin-tren-mang-xa-hoi-215261015192701748.chn) | 3.20 giới hạn xem đời người khác (lurk ≠ healed) | DARK |
| 2 | Công ty thu hẹp AI vì lỗi, chi phí, “AI slop” | 0.961 | 1.0 / 0.10 | [X News](https://x.com/i/trending/2110850870489252305) | 4.7 chia nhỏ task — “để AI làm hết” = dự án ma | DARK |
| 3 | StudyTok kiên trì học (TikTok @thnguyen.y 1,5M) | 0.957 | 1.0 / 0.07 | [TikTok](https://www.tiktok.com/@thnguyen.y/video/7663776976519384340) | 23.15 / pattern StudyTok (pattern evidence) | LIGHT |
| 4 | Áp lực “năng suất hoá” cả lúc ra ngoài trời | 0.913 | 1.0 / 0.05 | [Outside Mag via GNews](https://news.google.com/rss/articles/CBMikAFBVV95cUxPSWdnYllnOHdZZUJyS09xVUpJYnFlT3RtTy1WYWlqR2dGZnpydXIxbGhwbktUeWhzZjUzbHFvMEE3TGY1VW1KV2FJSFlpVkdXRDEwQzRqcWZYaHVYOHlXMkluMExsODhla2JlUEczdTBwdFFzSERmSXBVYVFCMDFyRHNyeGREb0dfNDcya21tQXA) | 22.6 buồn thì đi bộ — không phải outdoor hustle | LIGHT |
| 5 | Tips học tập / Pomodoro StudyTok (@dodai… 1,2M) | 0.838 | 1.0 / 0.07 | [TikTok](https://www.tiktok.com/@dodaihoccungvetaedu/video/7609936851717180692) | 4.12 / study habit list (P06 sat một phần) | LIGHT |
| 6 | Music + nghỉ = cách đối phó stress | 0.757 | 1.0 / 0.06 | [X News](https://x.com/i/trending/2109994700174512302) | 22.8 / 22.x thư giãn (không medical) | LIGHT |
| 7 | “Đừng đánh cược vào bản chất con người” + format bản chất (@hoaquynh 465k) | 0.750 | 1.0 / 0.12 | [TikTok](https://www.tiktok.com/@hoaquynh0000/video/7692007076716956946) | F06 / clip-02–03; dự án ma trong comment | DARK |
| 8 | McKinsey thử phỏng vấn avatar AI | 0.664 | 1.0 / 0.07 | [X News](https://x.com/i/trending/2110395763201388639) | 23.19 nghe–thích ứng (cùng họ hàng B-interview-01) | DARK |
| 9 | “Bạn không hề tuột lại” — ngừng soi đời người khác (@liminal 496k) | 0.660 | 1.0 / 0.05 | [TikTok](https://www.tiktok.com/@liminalspvce.io/video/7645271586156580116) | 3.20 + 4.12 (TikTok-native evidence cho #1) | LIGHT |
| 10 | 36% người lương ≥$300k vẫn sống tháng này sang tháng kia | 0.655 | 1.0 / 0.09 | [X News](https://x.com/i/trending/2109441779850260730) | 5.27 quỹ khẩn 3–6 tháng (caution: không mock) | DARK |

Đáng để ý (caution): [Gen Z điểm tựa khi tẩy chay / kiệt sức](https://news.google.com/rss/articles/CBMimgFBVV95cUxQSjFUV28wVEdwelI5SnpuMFBoRllzUjA3Z3lGSVBPbEl3UldYdVVsZmxTdEk4cW5ud2x6V01PemJSU1JIQlFFbUotejhDWFRiYXhZMm9xN1ZUVlVwZk1GSVowUlhjMm4tQjlCUndmTk9xNkQ5RGFfSHdUQm5fRDFwZnBHSnk3RC1ZaWtDTzBhdHd0WlkyTFlqOTVn) (Tiền Phong — empathy + 3.18, không trị liệu) · paycheck-to-paycheck $300k (không giễu) · celebrity Kenh14 (Hồng Đăng / Quỳnh Anh) — không dùng · [Đu trend lung tung quyền](https://news.google.com/rss/articles/CBMioAFBVV95cUxQc0p6ZFVaWEF2ZlpvOFhrSzN1NWVrTktaWUJDUFZIUkFTaWs4UkhQUDNIUGhlQThENnhGT2c1U3dwMXlLNldnT2dHOGRaWFNoRjBEaXM3ZktEZnhIZ3FrQWFCaFo1NkhxdnlpOHk4Q3dmWm1vSFVyVHV3RnFLZU1jOE90MjJ4Q3p5S0l0cGVmYnFEcnE3WHdZY0plTW5YbENi) (chấn thương — không promote). Sleep-struggle X News ngày 2 — hạ rank (đã stub năng lượng 15/10).

## Learning
- **Apify TikTok-native lần đầu vào digest hàng ngày:** clockworks hashtag+ASCII search + DOWNLOAD_SUBTITLES + comments shortlist + parseforge URL enrich → 100% fields. Format F06 “bản chất của…” vẫn sống (@giaimatrend giải mã + @hoaquynh nhái “bản chất con người”).
- **P03 / P11** mạnh với AI slop (thu hẹp AI ≠ “AI lấy việc”). **P06** StudyTok tips vẫn dày. Liminal transcript khớp 3.20 (“ngừng quan sát đời người khác”) — TikTok-native bridge cho Kenh14 #1.
- **Bão hoà, tránh góc thẳng:** trì hoãn không phải lười (YT + #trihoan TikTok, ngày 4) · 10k bước · productivity-tricks-adult · trần nhà · “AI lấy việc / AI tạo việc mới” tranh luận chung · sleep/5am/post-lunch (đã stub 15/10).
- Hôm nay stub **AI-slop→4.7 (clip-03)** + **không đăng vẫn lướt→3.20** — đổi trụ khỏi năng lượng ngủ của hôm qua; khác góc AI-jobs bão hoà.

## Bridges (khác biệt)
| id | Trend → khoảnh khắc | Bài học | Mọi người đang nói | Góc của mình | Hook VI (pattern) | Góc | Theme | Đích |
|---|---|---|---|---|---|---|---|---|
| B-aislop-01 | #2 → prompt một phát, sửa cả buổi | 4.7 | AI hype chết / công ty bỏ AI ([X](https://x.com/i/trending/2110850870489252305)) | Không kêu bỏ AI — “để AI làm hết” = task quá lớn / dự án ma; chia nhỏ phần người review được. Khác “AI lấy việc” | "Công ty đang thu hẹp AI vì lỗi và chi phí. Nghe quen hông?" (P11+P03) | contrarian / data | DARK | clip-03 |
| B-nopost-01 | #1 → story trống mà vẫn lướt feed | 3.20 | Bỏ đăng = detox / sống chậm ([Kenh14](https://kenh14.vn/vi-sao-ngay-cang-nhieu-nguoi-khong-con-dang-anh-hay-cap-nhat-thong-tin-tren-mang-xa-hoi-215261015192701748.chn)) | Không đăng ≠ hết so sánh nếu vẫn lướt đời người khác. Evidence TikTok: [@liminalspvce.io](https://www.tiktok.com/@liminalspvce.io/video/7645271586156580116). Khác B-scroll-01 (10 phút/app): hôm nay nhấn lurk ≠ healed. `[CẦN HIỆP XÁC NHẬN]` chuyện bỏ đăng | "Ngày càng nhiều người không còn đăng ảnh. Nghe healthy ghê." (P03+P06) | contrarian / empathy | DARK | ý tưởng mới |
| B-outdoor-01 | #4 → biến đi bộ thành “productive” | 22.6 | Ngoài trời cũng phải tối ưu / đóng goal | Buồn/stress thì đi bộ — không phải outdoor hustle | "Feed dạy bạn năng suất hoá cả lúc ra ngoài. Sách chỉ bảo: buồn thì đi bộ." (P03) | contrarian | LIGHT | ý tưởng mới |
| B-liminal-01 | #9 → sợ “tuột lại” so với người khác | 4.12 + 3.20 | Phải bắt kịp timeline người khác | Không có đường đua; thói quen tính theo tháng. Trùng evidence với B-nopost | "Bạn không hề tuột lại. Vì hông có đường đua nào cả." (P03) | empathy | LIGHT | ý tưởng mới / phụ B-nopost |
| B-paycheck-01 | #10 → lương cao vẫn hết tháng | 5.27 | Flex / giễu “nghèo giả” | Quỹ khẩn 3–6 tháng; lifestyle inflation — không mock. Caution | "Lương cao vẫn sống tháng này sang tháng kia. Sách hỏi: bạn có lớp đệm chưa?" (P04+P10) | data / empathy | DARK | ý tưởng mới |
| B-mckinsey-01 | #8 → luyện thuật toán, phỏng vấn hỏi lắng nghe | 23.19 | Sợ AI thay vòng phỏng vấn | Kỹ năng nghe–thích ứng vẫn là phần người; cùng họ B-interview-01 | "McKinsey thử phỏng vấn bằng avatar AI. Bạn đang luyện đúng thứ sẽ bị hỏi chưa?" (P04) | data | DARK | ý tưởng mới |
| B-banchat-02 | #7 F06 → điền “bản chất của dự án ma” | 4.7 / clip-02 | Nhại giảng Vật lí / meme điền khuyết | Giữ F06 cho clip-02 (đang production); dùng làm stem clip-03 “bản chất của việc để AI làm hết” | "(F06 stem) Vậy thì bản chất của việc để AI làm hết…" | humor | DARK | clip-02/03 callback |
| B-music-01 | #6 → bật nhạc / nằm khi stress | 22.8 | Coping playlist = đủ | Được; sách có thêm công cụ đo được (thở dài vòng). Không medical | "Feed bảo nhạc chữa stress. Được. Còn một công cụ có số liệu…" (P07→P03) | empathy / data | LIGHT | ý tưởng mới |

## Differentiation
Hai stub hôm nay tránh consensus hustle-sleep của 15/10 và tránh tranh luận “AI lấy việc”: (1) AI slop / thu hẹp AI → chia nhỏ task 4.7 cho **clip-03**; (2) bỏ đăng MXH ≠ hết so sánh → 3.20 với evidence TikTok liminal. Không Omi (tuần 1).

## Plan stubs (đều ✔ validate)
- `research/trends/2026-10-16/plans/plan-1-ai-slop-chia-nho-viec.json` (B-aislop-01, 8 cảnh, 43 giây, DARK, tuần 1). ✔ `npm run validate`.
- `research/trends/2026-10-16/plans/plan-2-khong-dang-van-luot.json` (B-nopost-01, 8 cảnh, 42 giây, DARK, tuần 1). ✔ `npm run validate`.
Cả hai `status: stub-needs-approval`. Plan-2 có beat chuyện thật `[CẦN HIỆP XÁC NHẬN]`. Không dùng Omi (tuần < 5).

## Script hooks (cần Hiệp duyệt)
1. "Công ty đang thu hẹp AI vì lỗi và chi phí. Nghe quen hông?" (B-aislop-01)
2. "Ngày càng nhiều người không còn đăng ảnh. Nghe healthy ghê." (B-nopost-01)
3. "Feed dạy bạn năng suất hoá cả lúc ra ngoài. Sách chỉ bảo: buồn thì đi bộ." (B-outdoor-01)
4. "Bạn không hề tuột lại. Vì hông có đường đua nào cả." (B-liminal-01)
5. "Lương cao vẫn sống tháng này sang tháng kia. Sách hỏi: bạn có lớp đệm chưa?" (B-paycheck-01) — caution

## TikTok signals
| keyword / trend | clip | views | comments | hook / transcript snip | sound | brand-safe? | bridge |
|---|---|---|---|---|---|---|---|
| #hoctap StudyTok | [@thnguyen.y](https://www.tiktok.com/@thnguyen.y/video/7663776976519384340) | 1.5M | 567 | kiên trì học / chia sẻ | original | ok | pattern StudyTok |
| bản chất con người | [@hoaquynh0000](https://www.tiktok.com/@hoaquynh0000/video/7692007076716956946) | 465k | 561 | “Đừng đánh cược vào bản chất…”; comment “Đồng nghiệp!! Sao tách đc” | original | ok | F06 + B-aislop stem |
| tư duy list | [@hoaquynh0000](https://www.tiktok.com/@hoaquynh0000/video/7680893073684958482) | 1.4M | 538 | “top Ba Tư duy…” VTT | original | ok | P06 |
| tips học / Pomodoro | [@dodaihoccungvetaedu](https://www.tiktok.com/@dodaihoccungvetaedu/video/7609936851717180692) | 1.2M | 462 | tips học; comment khen Pomodoro | original | ok | study habit |
| không tuột lại / ngừng soi đời người | [@liminalspvce.io](https://www.tiktok.com/@liminalspvce.io/video/7645271586156580116) | 496k | 266 | VTT: “ngừng việc quan sát cuộc sống của người khác… bạn không hề tuột lại” | original | ok | **B-nopost-01 / 3.20** |
| hết trì hoãn | [@nhile_n](https://www.tiktok.com/@nhile_n/video/7269745529582603526) | 740k | 265 | bí quyết trì hoãn (sat góc thẳng) | original | ok | pattern only — không top bridge |
| 7 thói quen học | [@gonaox](https://www.tiktok.com/@gonaox/video/7694997202954915079) | 332k | 151 | “7 thói quen học tập của học sinh giỏi nhất lớp” | original | ok | 4.12 / P06 sat một phần |
| giải mã “bản chất của dao động điều hoà” | [@giaimatrend.vn](https://www.tiktok.com/@giaimatrend.vn/video/7694889719036923154) | 72k | 33 | F06 origin explain; comment “v thì bản chất của lốp?” | original | ok | F06 / clip-02 |

## An toàn
Drop giữ nguyên keyword pre-filter. Caution: Gen Z tẩy chay/kiệt sức, paycheck $300k, celebrity gossip, lung tung quyền (chấn thương). Không promote medical claims từ caffeine–trẻ em. Không dùng góc AI-jobs chung (sat). Sample verify `au2F9eFcWhzuaXWnz` giữ trong folder; digest dùng run fresh `GjDxjHOvo7LWub0CA`.

## Đề xuất sửa công cụ (chờ Hiệp, không tự sửa)
- Wiki pageviews: auto lùi 1–2 ngày khi 404 (lặp lại từ 14–16/10).
- Normalize: khi VTT MCP trả kèm JSON wrapper `contentType`, strip trước khi ghi file (đã xử lý tay hôm nay).
