---
title: "Caption + hashtag dễ lên xu hướng theo nền tảng (TikTok, Reels, Shorts, Threads) — Social Poster"
date: 2026-10-20
source: "Social Poster: Apify (4 run, 20/10/2026 23:21–23:27 ICT), x.get_trends_by_woeid, trang trợ giúp/newsroom chính thức, báo công nghệ"
id: research.social-poster.caption-hashtag-2026-10-20
type: research
status: draft
updated: 2026-10-20
tags: [social, caption, hashtag, tiktok, instagram, youtube-shorts, threads, rule-53, W-20, W-19]
---
# Caption + hashtag theo nền tảng: nghiên cứu ngày 20/10/2026 (Social Poster)

Phạm vi: ngách học tập, năng suất và phát triển bản thân, ưu tiên khán giả Việt Nam. File này dùng làm đầu vào cho gói đăng (rule-53, W-20). File không đổi rule nào. Chỗ nào khác rule thì ghi ở §6 để Rule Reviewer và Hiệp quyết.

**Không chép lại nội dung đã có, chỉ trỏ tới:**
- Cách nền tảng đề xuất video (tín hiệu xem, chia sẻ): `research/platform-recommendation-facts-2026-10-20.md`.
- Hook/format: `research/trends/patterns.md`. Hashtag đã ghi trước đây: `research/trends/ingest.md` §Hashtags.
- Tín hiệu TikTok của clip-04: `content/clips/clip-04-gap-sach-tu-kiem/final/trend-signals.md`.
- Bộ xu hướng TikTok của Social Research: `research/tiktok-trend-pack-study-2026-10-20.md`. **Lúc viết file này (23:30 ICT) file đó chưa có.** Khi có thì phần TikTok ưu tiên số của bộ đó, file này chỉ bổ sung phần caption/hashtag.

Dữ liệu thô nằm ở `research/agents/data/social-poster-trends-2026-10-20/` (`run-meta.json` + 4 file dataset). Mọi số view/like trong file này là **số thô do scraper trả về lúc thu (20/10/2026 ~23:21 ICT)**. Đây là mẫu nhỏ (30/24/24/17 bài), chỉ cho thấy khuynh hướng, không đủ để kết luận "đang là trend".

Quy ước nhãn: **[CT]** là nguồn chính thức của nền tảng. **[BC]** là báo chí hoặc blog dẫn lại lời nền tảng. **[DL]** là dữ liệu Apify của file này. **[KN]** là kinh nghiệm creator hoặc suy luận, chưa có bằng chứng chính thức.

---

## 1. Dữ liệu đã thu

| Nền tảng | Actor / công cụ | Input | Số bài | Ước chi phí (giá FREE) |
|---|---|---|---:|---:|
| TikTok | `clockworks/tiktok-scraper` run `ZjK5AyEIbn4zPDGu7` | #hoctap #studytok #phattrienbanthan #hoctienganh + search "meo hoc bai nho lau", "cach hoc thuoc nhanh"; 5/trang | 30 | ≈ $0,11 |
| Instagram Reels | `apify/instagram-hashtag-scraper` run `aSVxUBYfin9YUNzLF` | #hoctap #phattrienbanthan #studygram #hoctienganh; reels; 6/thẻ | 24 | ≈ $0,06 |
| YouTube Shorts | `streamers/youtube-scraper` run `hJqK4fwPr74nPIvmv` | search "mẹo học bài nhớ lâu", "cách học thuộc nhanh", "phát triển bản thân"; 8 Shorts/từ khoá | 24 | ≈ $0,10 |
| Threads | `scraping_solutions/threads-search-scraper` run `Kd2HaljaXJ8girANh` | keyword "cách học", top, tối đa 20 | 17 (tính phí 20) | ≈ $0,04 |
| X | `x.get_trends_by_woeid` woeid 23424984 (VN) | 30 trend | 30 | 0 (quota X) |

Tổng ước tính khoảng **$0,31** (≈ 0,12 CU). MCP không trả số USD thật, nên đây là số ước theo bảng giá FREE tier của từng actor. Không dùng các actor bị cấm trong rule-57 / `pipeline/trends/apify.yaml`.

**X:** trend X Việt Nam lúc 23:23 ICT toàn là fandom Thái, crypto và "Thứ Ba", không có gì về học tập/năng suất nên không dùng. Threads không có API trend công khai nên phần Threads dựa vào bài top theo từ khoá.

---

## 2. TikTok

### 2.1 Quy tắc chính thức hiện hành
- **[CT] Hashtag: "Less is more. Use 2-3 for context and discovery."** Nguồn: TikTok for Good, *Technical best practices*, https://www.tiktok.com/for-good/technical-best-practices/ (đọc 20/10/2026). Lời khuyên 2–3 thẻ của Creator Academy được Zolyp dẫn lại [BC]: https://www.zolyp.com/blog/tiktok-captions-and-hashtags (Zolyp ghi kiểm 14/10/2026).
- **[CT] #FYP / #ForYou "won't necessarily improve your chances"**. Nên dùng chỗ trong caption để thêm ngữ cảnh cùng hashtag liên quan. Nguồn: TikTok Newsroom, *5 tips for TikTok creators*, https://newsroom.tiktok.com/en-us/5-tips-for-tiktok-creators (đọc 20/10/2026).
- **[CT] Caption, âm thanh và hashtag là "thông tin video" mà TikTok dùng để đề xuất.** Chi tiết xem `research/platform-recommendation-facts-2026-10-20.md`.
- **Độ dài caption:** trợ giúp chính thức của TikTok không công bố giới hạn trong app. API Direct Post giới hạn **2.200 UTF-16 runes**, hashtag tính chung vào đó [BC, dẫn tài liệu developer]: https://kodahq.app/en/reference/tiktok-caption-and-hashtag-limits. Giới hạn trong app được báo là 4.000 ký tự [BC]. **[DL]** bài @camreadwonder có caption 2.917 ký tự, cho thấy app nhận dài hơn 2.200: https://www.tiktok.com/@camreadwonder/video/7614813783201975573. Rule-53 đặt ≤ 2.200, vẫn an toàn cho cả hai đường.
- **[CT] Nhãn AI:** bật "AI-generated content" khi video có âm thanh AI nghe như thật. Đã ghi trong rule-46 (support.tiktok.com, kiểm 13/10/2026), không nhắc lại ở đây.
- **[BC] Từ khoá tìm kiếm:** đặt từ khoá trong caption, chữ trên màn hình và lời nói. Theo Zolyp dẫn TikTok Support, ở trang tìm kiếm mức khớp giữa từ khoá và nội dung bài được tính nặng nhất. Nguồn: Sprout Social https://sproutsocial.com/insights/tiktok-seo/ và Zolyp ở trên. Phần này chưa mở được trang support gốc, coi như [BC].

### 2.2 Mẫu caption đang chạy trong ngách (VN) [DL]
| Kiểu | Ví dụ thật | Số thô lúc thu |
|---|---|---|
| **Từ khoá tìm kiếm làm câu đầu** ("cách/mẹo + học thuộc/nhớ lâu") | "Cách giúp bạn học thuộc nhanh trong 5 phút" + #LearnOnTikTok #hoccungtiktok #hocthuocnhanh… https://www.tiktok.com/@biquyetdodaihoc/video/7431067111763561736 | 1,1M view, 10.415 lưu (đăng 29/10/2024) |
| | "Cách nhớ kiến thức lâu" https://www.tiktok.com/@nhunconuong/video/7095558725313760538 | 2,2M view (2022, bài cũ) |
| **Một câu "đúng tim đen"** (relatable) | "Học 1 đêm mới hiểu sao kiến thức được dạy trong 1 kỳ" https://www.tiktok.com/@ng__phanh/video/7532553338664045831 | 1,1M view, 55,3k share (số lấy từ `research/trends/2026-10-20/apify/clips.json`) |
| **Nhận ra muộn** (hindsight + emoji) | "4 năm đại học, vẫn đống đề cương đó mà giờ mới biết dùng kiểu này 💀" https://www.tiktok.com/@hoc.di.roi.biet/video/7695270625660652820 | 390,7k view (cùng file). Có thẻ quảng cáo #astraai #4153, tức quảng cáo ngầm |
| **Câu hỏi kéo comment** ở cuối caption | "Còn tư duy nào nữa không mn? Comment đề học hỏi nào?" https://www.tiktok.com/@hoaquynh0000/video/7680893073684958482 | 1,5M view, 19k share |

Rút ra [KN]: caption thắng trong mẫu đều **ngắn, 1–2 câu**. Câu đầu hoặc là từ khoá tìm kiếm ("cách học thuộc nhanh") hoặc là một câu nỗi đau ai cũng gặp, sau đó tới hashtag. Caption dài kiểu bài viết có tồn tại (@camreadwonder) nhưng hiếm. Khuynh hướng này khớp với ý của Rule Reviewer: caption ngắn, mỗi ý nói một lần.

### 2.3 Hashtag [DL]
Mỗi bài trong mẫu 30 bài có trung vị **5 thẻ** (2–14). Thẻ xuất hiện nhiều nhất: #learnontiktok 9/30, #studytok 8/30, #phattrienbanthan 5/30, #viral 5/30, #xuhuongtiktok 4/30, #fyp 3/30.
Bộ đếm view của trang hashtag do actor trả về (cả đời, thu 20/10/2026): **#studytok 100 tỷ** (có thể là số làm tròn hoặc chặn trần), **#phattrienbanthan 21,9 tỷ**, **#hoctienganh 13 tỷ**, **#hoctap 5,5 tỷ**. Số đã có từ trước trong ingest.md (18/10): #kyluatbanthan 1,2 tỷ, #sinhvien 18,4 tỷ.

| Nhóm | Đề xuất | Bằng chứng / lưu ý |
|---|---|---|
| Rộng (giáo dục) | `#learnontiktok` | Thẻ phổ biến nhất trong mẫu VN (9/30). Chưa có nguồn chính thức nói TikTok "đẩy" thẻ này, nên không khẳng định điều đó |
| Ngách VN | `#hoctap`, `#onthi`, `#hocthuocnhanh` | #hoctap 5,5 tỷ. #onthi có @ng__phanh 1,1M. #hocthuocnhanh đi kèm bài 1,1M của @biquyetdodaihoc |
| Ngách VN (rộng hơn) | `#phattrienbanthan` | 21,9 tỷ, nhưng mẫu lẫn nhiều tâm linh/tài chính (@toiyeudaophatv, @kesanmoi.rf). Chỉ dùng khi clip về thói quen hoặc kỷ luật |
| Theo chủ đề clip | `#hoctienganh` **chỉ khi** clip nói về tiếng Anh | 2/5 bài top của #hoctienganh trong mẫu là nhạc thiếu nhi (@kahu99, @kids.english.ever), nên lệch khán giả |
| EN | `#studytok`, `#studytips` | #studytok: bài top trong mẫu là tiếng Anh/Hà Lan năm 2021, tệp VN thấp. Chỉ dùng làm thẻ thứ 5 nếu cần |

**Nên tránh:** #fyp #foryou #viral #xuhuong #xuhuongtiktok #trending (đã cấm trong rule-53, TikTok cũng nói không giúp được). Thẻ quảng cáo hoặc số (#astraai, #4153, #4201). Thẻ thương hiệu người khác (#biquyetdodaihoc, #edutaco…). Thẻ lệch ngách (#manifestation, #luathapdan, #chualanhtamhon, #taichinh).

### 2.4 Template TikTok cho OneUp (theo rule-53, W-14, C-1)
```
{Hook 1 câu: nỗi đau nói thẳng + câu hỏi; có từ khoá tìm kiếm, vd "học thuộc", "nhớ lâu"}
{1 câu ý chính: cách làm, nói một lần}
{CTA duy nhất: thử thách comment 1 chữ (rule-56); không xin like/follow}
{tuỳ chọn: 1 dòng nguồn nghiên cứu, vd "Nghiên cứu: Yang 2021 (tổng hợp 222 nghiên cứu)" — chỉ số đã khoá}
Giọng trong video là giọng AI tổng hợp (F5-TTS).
Thông tin tham khảo, không thay thế tư vấn chuyên gia
Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/
#learnontiktok #hoctap #{ngách theo chủ đề} {≤ 2 thẻ nữa}
```
"Đã chuyển thể" và link giấy phép đặt ở chỗ Rule Reviewer đã chốt cho clip-04 (C-1). Không viết "tác giả ủng hộ / hợp tác / chính chủ". Không thêm số nào ngoài fact lock.

---

## 3. Instagram Reels

### 3.1 Quy tắc hiện hành
- **[BC dẫn lời IG] Tối đa 5 hashtag mỗi post/reel**, áp dần từ 18/12/2025. Instagram nói: "using fewer (up to 5) more targeted hashtags, rather than many generic ones, can improve both your content's performance and people's experience". Mosseri nói hashtag giúp tìm kiếm nhưng "don't increase your reach". Nguồn: Social Media Today 18/12/2025 https://www.socialmediatoday.com/news/instagram-implements-new-limits-on-hashtag-use/808309/, The Verge https://www.theverge.com/news/847739/instagram-hashtag-spam-limit, Indian Express 21/12/2025. Indian Express dẫn @creators: thẻ chung chung như #reels, #explore "may negatively impact" hiệu quả bài.
- **[DL] Xác nhận gián tiếp:** cả 14/14 reel đăng từ 2026 trong mẫu có ≤ 5 thẻ. Reel đăng trước 2026 có tới 14–19 thẻ.
- **[BC dẫn Instagram Help] Nhãn AI:** bắt buộc với video giống thật hoặc **âm thanh AI nghe như thật**, "a reel with a realistic AI voiceover" là ví dụ cần nhãn. Bật bằng nút "Add AI label" trước khi chia sẻ (chỉ trong app). Nguồn: Zolyp 15/10/2026 dẫn *Instagram Help Centre: Label AI content on Instagram* https://www.zolyp.com/blog/how-to-label-ai-content-on-instagram. **Chưa xác nhận từ nguồn gốc** (help.instagram.com trả 403).
- **Caption tối đa 2.200 ký tự.** Trong tab Reels chỉ hiện khoảng 55–60 ký tự trước nút "more" [BC: https://bundle.social/blog/instagram-character-limits-guide].
- Tín hiệu đề xuất (lượt gửi bạn bè, thời gian xem): xem `research/platform-recommendation-facts-2026-10-20.md`.

### 3.2 Mẫu caption [DL]
| Kiểu | Ví dụ | Số thô |
|---|---|---|
| Câu lợi ích viết HOA từ khoá | "Hãy xem những BỘ PHIM sau nếu muốn TĂNG TRÌNH TIẾNG ANH" + 5 thẻ https://www.instagram.com/p/Db7_fAtztfU/ | 200,5k play, **1.527 share** (12/08/2026) |
| Caption dạng list dài (1.265 ký tự) | "1. Đừng than vãn quá nhiều về cuộc sống…" https://www.instagram.com/p/DWVJ4sICTpD/ | 174,4k play, 364 share |
| CTA "comment từ khoá" | "COMMENT "NANGSUAT" ĐỂ NHẬN TEMPLATE MIỄN PHÍ" + #phattrienbanthan #productivity https://www.instagram.com/p/DIWII2LvwVM/ | 25,6k play, 47 comment |
| Relatable ngắn | "literally me 😆" #studygram… https://www.instagram.com/p/DerlanWyu5u/ | 19,6k play, 292 share (19/10/2026) |

Rút ra [KN]: ở Reels, nút **share** đáng để ý (khớp với lời Mosseri về lượt gửi). Câu đầu nên nói rõ người xem được gì vì chỉ ~55 ký tự hiện ra. Kiểu "comment 1 chữ" chạy được và trùng với rule-56. Lưu ý: link trong caption IG thường không bấm được. Đây là quan sát trong app, chưa có trang chính thức; Hiệp kiểm lại khi đăng.

### 3.3 Hashtag
| Nhóm | Đề xuất | Bằng chứng |
|---|---|---|
| Ngách VN | `#hoctap`, `#phattrienbanthan` | 6/24 mỗi thẻ. #phattrienbanthan lẫn MMO/kinh doanh online (@spiderguy.co, @thanhvaxuan) |
| EN học tập | `#studytips`, `#studygram` | #studygram 8/24 nhưng phần lớn là tài khoản nước ngoài (US/BR) |
| Theo chủ đề | `#hoctienganh` chỉ khi clip về tiếng Anh | 7/24 |
**Tránh:** #reels #explore #explorepage #instagram #fyp #viral #xuhuong (Instagram nói thẻ chung chung có thể làm giảm hiệu quả). Không vượt 5 thẻ.

### 3.4 Template Reels
```
{Câu 1 ≤ ~55 ký tự: nỗi đau/lợi ích + từ khoá}
{1 câu ý chính}
{CTA duy nhất — vd comment 1 chữ; không thêm CTA "gửi cho bạn" (W-14)}
Giọng trong video là giọng AI tổng hợp (F5-TTS).
Thông tin tham khảo, không thay thế tư vấn chuyên gia
Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/
#hoctap #studytips #{ngách} (3–5, tối đa 5)
```
Bật "Add AI label" vì giọng F5 là giọng AI nghe như thật. Xuất file sạch, không dính watermark TikTok (xem platform-recommendation-facts).

---

## 4. YouTube Shorts

### 4.1 Quy tắc chính thức [CT]
- **Hashtag:** đặt trong tiêu đề hoặc mô tả. Trong các thẻ ở mô tả, **tối đa 3 thẻ** được hiện cạnh tiêu đề. **Quá 60 thẻ thì YouTube bỏ qua toàn bộ hashtag** của video, và gắn quá nhiều có thể bị gỡ khỏi tìm kiếm. Thẻ không liên quan bị tính là metadata gây hiểu lầm. Nguồn: https://support.google.com/youtube/answer/6390658 (đọc 20/10/2026).
- **Tiêu đề tối đa 100 ký tự, mô tả 5.000 ký tự**: https://support.google.com/youtube/answer/57404.
- **Nhãn AI ("AI use" trong YouTube Studio):** bắt buộc với nội dung AI **trông như thật**. Nội dung không thật, như hoạt hình hay nhân vật hoạt hình, thì không bắt buộc. Nhãn cho audio AI không phải nhạc hoặc nội dung hoạt hình nằm ở mô tả mở rộng. "Disclosing AI content alone won't limit a video's audience". Nguồn: https://support.google.com/youtube/answer/14328491. Rule Reviewer đã quyết bật nhãn để thống nhất với TikTok/Reels, và theo YouTube thì bật nhãn không làm giảm lượt tiếp cận.
- Tín hiệu xếp hạng Shorts: xem `research/platform-recommendation-facts-2026-10-20.md`. **[BC]** Theo Social Media Today, YouTube (Todd Sherman) nói hashtag trên Shorts không bắt buộc, chỉ có ích khi gắn với sự kiện hoặc chủ đề: https://www.socialmediatoday.com/news/youtube-advice-for-shorts-creators-hashtags-algorithm/691835/.

### 4.2 Mẫu tiêu đề/mô tả [DL]
- Top 10 Shorts trong mẫu có tiêu đề dài 31–96 ký tự (trung vị 56). Từ khoá đứng đầu tiêu đề. 15/24 có "#" trong tiêu đề, phần lớn là tag tên kênh. 5/24 có #shorts. 6/24 **không có mô tả**.
- "Phương Pháp Học Ghi Nhớ Kỳ Lạ Nhưng Cực Kỳ Hiệu Quả" (không mô tả): https://www.youtube.com/shorts/SpnllmoE-k8, **2,82M view** (25/08/2026).
- "Dạy bạn cách nhanh chóng tăng cường trí nhớ #metrithuc": https://www.youtube.com/shorts/JI_g0Xyy6vI, 1,13M view.
- "Cách để nhớ hết những gì đã đọc": https://www.youtube.com/shorts/DFcytHxScW4, 855k (2021).
- **Kênh hoạt hình gần format OneUp nhất**, Beauty Toon: "Mẹo Ôn Thi Hiệu Quả ! #beautytoon #hoathinhvuinhon" https://www.youtube.com/shorts/7LJVykytjxk (374,5k). Mô tả mở bằng câu hỏi nỗi đau: "Bạn lo lắng vì thi cử sắp đến mà ôn tập chưa hiệu quả? 📚". Kênh này có 3 Shorts 272k–375k trong mẫu.
- Đối thủ cùng chủ đề tự kiểm, mới đăng 20/10: "Phương Pháp Học Tập BRAIN DUMP… #studytips #hoctap #hocgioi" https://www.youtube.com/shorts/Vw43BjgOPFw (1 view lúc thu). Đây chỉ là tín hiệu chủ đề, không phải bằng chứng hiệu quả.

### 4.3 Hashtag
Ba thẻ hiện cạnh tiêu đề: `#hoctap #studytips #{ngách}`. Có thể thêm `#phattrienbanthan` trong mô tả. Mẫu YouTube cho thấy hashtag ít quan trọng. Từ khoá trong tiêu đề ("cách học thuộc", "nhớ lâu") mới là thứ được dùng nhiều.

### 4.4 Template Shorts
```
Tiêu đề (≤ 100, khuyến nghị ~40–60): {Từ khoá + lợi ích/nỗi đau}, vd "{Cách ...} — {nỗi đau ngắn}?"
Mô tả:
{Câu nỗi đau + câu hỏi}
{1 câu ý chính}
{CTA duy nhất}
{Nguồn nghiên cứu + link PubMed (được phép ở YouTube theo quyết định của Rule Reviewer)}
Giọng trong video là giọng AI tổng hợp (F5-TTS).
Thông tin tham khảo, không thay thế tư vấn chuyên gia
Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/
{Dòng "đã chuyển thể" + link giấy phép CC BY 4.0 (C-1)}
#hoctap #studytips #{ngách}
Studio: AI use = Yes.
```

---

## 5. Threads

### 5.1 Quy tắc [CT qua tài liệu Meta, dẫn lại]
- **Một topic tag mỗi bài**, dài 1–50 ký tự, được có dấu cách, dấu # không bắt buộc. Thêm bằng "Tag" hoặc gõ #. Hashtag thứ hai trở đi chỉ là chữ thường [BC dẫn Threads Help]: https://www.zolyp.com/blog/how-to-use-topic-tags-on-threads. Bản API ghi "Only one topic tag is allowed per post" [BC dẫn developer docs]: https://adaptlypost.com/blog/threads-api-500-character-limit-topic-tag. **Chưa xác nhận từ nguồn gốc** (developers.facebook.com trả 403).
- **Text tối đa 500 ký tự.** Hashtag viết trong text cũng tính vào giới hạn này (nguồn như trên).
- **[CT] "Trending" (tóm tắt chủ đề nóng) có ở Việt Nam từ 05/2026.** Connor Hayes (trưởng Threads) viết: "now live in Japan, Vietnam, Taiwan, and Brazil": https://www.threads.com/@conno_r/post/DX7RQFskeSO. SMT cũng đưa tin: https://www.socialmediatoday.com/news/threads-expands-trending-topic-summaries-to-more-regions/819276/.
- **Nhãn AI:** Threads có nút "Add AI label" trong composer [BC]: https://www.zolyp.com/blog/how-to-label-ai-content-on-threads. Mosseri: thẻ trên Threads nhắm "communities … less on engagement hacking" (dẫn qua The Verge, link ở §3.1).

### 5.2 Mẫu bài trong ngách [DL, keyword "cách học", top]
| Kiểu | Ví dụ | Số thô |
|---|---|---|
| Một nhận định, viết HOA | "ĐOẠN QUAN TRỌNG NHẤT TRONG VIỆC HỌC CHÍNH LÀ HỌC CÁCH HỌC…" (153 ký tự) https://www.threads.com/@kirbybabyangel.ng/post/DaANK57D1VQ | 14.596 like, 2.322 repost (25/06/2026) |
| Tự thú hài, 1 câu + video | "Kể từ hồi đi làm thì tao thực sự đã xả stress bằng cách học bài 🙂" https://www.threads.com/@__kieuyenngoc___/post/DemQRF9Eybg | 11.708 like (17/10/2026) |
| Chuyện đời ngắn | "Kiếp nạn khi làm gia sư / Chỉ học sinh cách học và bị đuổi 😭" https://www.threads.com/@thanhtrucdayne/post/Dd-zUkzDycx | 11.593 like |
| List "vấn đề → cách gỡ" | "Cách xử lý nhanh các vấn đề khi học: Trì hoãn → …" https://www.threads.com/@donutdayy/post/DQHLJ19iePS | 1.916 like, 401 repost |
| Cùng chủ đề tự kiểm | "…'Muốn nhớ lâu, phải tự hỏi lại não mình.'" https://www.threads.com/@donutdayy/post/DQocnsuiaPO | 210 like |
| Số không nguồn (KHÔNG bắt chước) | "90% MỌI NGƯỜI ĐANG HỌC TỪ VỰNG SAI CÁCH!" https://www.threads.com/@vuong_hochanh/post/DA8sFd5S757 | 4.366 like (2024) |

Rút ra [KN]: trên Threads, bài top là **chữ ngắn (58–153 ký tự), ngôi thứ nhất, giọng bạn bè**. Video chỉ đi kèm. 0/17 bài có hashtag trong text (topic tag là trường riêng, scraper không lấy được). Bài hỏi cộng đồng ("ai share cho t cách học…") kéo được nhiều comment.

### 5.3 Topic tag
Chọn **một** topic, ưu tiên tag gần cộng đồng: `Học tập` hoặc `cách học` (có dấu cách được). Chưa kiểm được số người theo dõi mỗi topic vì không có API công khai. Hiệp nên gõ thử trong composer xem Threads gợi ý gì, rồi chọn tag có bài cùng chủ đề.

### 5.4 Template Threads (≤ 500 ký tự kể cả footer)
Footer bắt buộc chiếm khoảng 220 ký tự (dòng AI 48 + câu an toàn 52 + credit 118 + xuống dòng), nên thân bài còn **≤ ~270 ký tự**.
```
{1–2 câu ngôi "mình", kể nỗi đau cụ thể (giữ nhãn minh hoạ nếu là ví dụ)}
{1 câu cách làm}
{1 câu hỏi duy nhất ở cuối (CTA)}
Giọng trong video là giọng AI tổng hợp (F5-TTS).
Thông tin tham khảo, không thay thế tư vấn chuyên gia
Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/
Topic: {1 tag}
```

---

## 6. Chỗ khác rule, cần Rule Reviewer / Hiệp quyết (chưa đổi rule nào)
1. **Số hashtag TikTok:** rule-53 cho 3–5 thẻ. TikTok khuyên 2–3 [CT]. Mẫu VN có trung vị 5 [DL]. Hai bên trùng ở mức **3 thẻ**. Đề xuất: giữ rule, nhưng mặc định nghiêng về 3–4 thẻ. Cần quyết có hạ trần xuống 4 hay không.
2. **Threads chỉ cho 1 topic tag.** Mục 4 của rule-53 (3–5 thẻ) và W-20 ("hashtag" cho từng nền tảng) chưa có ngoại lệ cho Threads. Cần ghi rõ: Threads = 1 topic tag.
3. **Instagram trần cứng 5 thẻ:** khớp với rule-53 (≤ 5). Chỉ cần ghi chú là IG chặn trên 5.
4. **YouTube:** rule-53 viết cho TikTok, chưa nói thẻ đặt ở tiêu đề hay mô tả. Đề xuất: 3 thẻ ở cuối mô tả (hiện cạnh tiêu đề), tiêu đề chỉ chứa từ khoá. Nhãn AI của YouTube không bắt buộc với nhân vật hoạt hình, nhưng Rule Reviewer đã quyết bật. Không xung đột, chỉ ghi lại lý do.
5. **Threads 500 ký tự:** footer bắt buộc (AI + an toàn + credit nguyên văn) chiếm ~220 ký tự. Không xung đột, nhưng thân bài phải ≤ ~270 ký tự.
6. **TikTok for Good khuyên "Ditch branding… end cards".** Luật của OneUp bắt buộc thẻ cuối có credit CC BY. Đây là lời khuyên cho tổ chức phi lợi nhuận, không phải luật nền tảng. Đề xuất giữ thẻ cuối và chỉ ghi nhận rủi ro.
7. **Template cũ `templates/post-package.md`** (clip-01) ghi "#learnontiktok: TikTok đẩy cho nội dung giáo dục" mà không có nguồn. Lượt này không tìm thấy nguồn chính thức nào xác nhận. Đề xuất bỏ câu đó trong các gói sau (không sửa template ở lượt này).

## 7. Việc tiếp theo
- Khi `research/tiktok-trend-pack-study-2026-10-20.md` của Social Research có, đối chiếu lại bảng hashtag §2.3 và chỉ trỏ tới file đó.
- Sau 14 ngày có Analytics của kênh: so thẻ/caption theo lượt xem của chính kênh, cập nhật file này (rule-47).
- Chưa kiểm được: trang gốc Instagram/Threads Help và Meta developer docs (403 khi fetch). Các mục [BC dẫn] từ Meta ghi là «chưa xác nhận từ nguồn gốc»; nhờ Deep Research kiểm lại khi cần để nâng lên [CT].
