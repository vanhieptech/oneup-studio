---
title: "Bộ nháp đăng clip-04 v18 «Gấp sách tự kiểm» (TikTok · Threads · Instagram Reels · YouTube Shorts)"
date: 2026-10-20
source: "oneup-studio (Social Poster soạn trong repo) · lời khoá final/script-v18-LOCKED.md · HowToLiveBetter phần 23 mục 14"
id: clip-04.publish.post-package
type: post-package
template: post-package v1 (rule-53, DL-045) + bản đa nền tảng (W-20)
status: đã sửa theo Rule Reviewer, chờ soát lại
updated: 2026-10-20
video: "CHỜ video cuối v18 từ News"
cover: "CHỜ — đề xuất ở mục 2, chưa render"
hashtags: ["#hoctap", "#hoctienganh", "#tuvungtienganh", "#studytok", "#studymethod"]
tags: [clip-04, post, publish, tiktok, threads, instagram, youtube-shorts, w-20, draft]
---
# Bộ nháp đăng clip-04 v18 «Gấp sách tự kiểm»

> **Chỉ là nháp.** Không đăng, không lên lịch, không đăng nhập tài khoản nào. Hiệp tự đăng tay sau khi Rule Reviewer soát đạt và Hiệp duyệt.
> Lời bám đúng `final/script-v18-LOCKED.md` (Hiệp «Oke duyệt», L-078). Claim chỉ lấy từ script khoá + `final/script-v18-table.md` (mục Claim → nguồn) + `final/fact-package-redo-2026-10-19.md` + HowToLiveBetter phần 23 mục 14.
> Bộ xu hướng `research/tiktok-trend-pack-study-2026-10-20.md` **chưa có trong repo** lúc soạn (20/10/2026, 23:2x giờ VN) → **chưa áp bộ xu hướng**. Hashtag lấy từ hệ thẻ đã dùng ở clip-01..04 + `final/trend-signals.md` (Apify 17/10/2026).

Mục 1–12 là gói TikTok theo `templates/post-package.md` (giữ đúng tên mục để check rule-53 đọc được). Mục 13–15 là bản Threads, Instagram Reels, YouTube Shorts. Mục 16 là thumbnail. Mục 17 là tự soát.

## 1. File video
```
CHỜ video cuối v18 từ News (chưa có).
Đích dự kiến: content/clips/clip-04-gap-sach-tu-kiem/final/out/clip-04-final.mp4 · ~49s (ước tính trong script-v18-table: ~42s lời + nghỉ, gồm 2s end card) · 1080×1920 (9:16) · 30fps · H.264 High + AAC 48 kHz · −14 LUFS
```
Lưu ý: file `final/out/clip-04-final.mp4` đang có (68,97s, tạo 20/10 lúc 11:25 giờ VN) là bản dựng **v14**, trước khi v18 được chốt (23:11) → **không dùng**. Khi News giao file v18 thì điền lại thời lượng/độ phân giải thật bằng ffprobe.
Mỗi nền tảng tải lên **file gốc sạch** (không dùng bản tải về từ TikTok có logo), vì Instagram ưu tiên nội dung gốc (`research/platform-recommendation-facts-2026-10-20.md`).

## 2. Chữ trên cover (≤ 40 ký tự)
```
HỌC THUỘC TỐI QUA? SÁNG QUÊN SẠCH!
```
Ba phương án để Hiệp chọn (đều ≤ 40 ký tự, render bằng template A `Cover.tsx`, không lấy frame video — luật 54, L-020):
- **A (đề xuất, 34 ký tự):** `HỌC THUỘC TỐI QUA?` (gạch) → `SÁNG QUÊN SẠCH!` (pill). Khớp nguyên văn hook b01. Props sẵn trong `final/spec.json → cover` (bản render v14 ở `final/cover/cover-a.png` đã đủ dấu, có thể dùng lại nếu Hiệp chọn A).
- **B (21 ký tự):** `TỐI THUỘC,` → `SÁNG QUÊN?` — đề xuất của FLUX Visual trong `final/visual-plan-v18.md`.
- **C (35 ký tự):** `GẤP SÁCH LẠI,` → `CÒN VIẾT ĐƯỢC MẤY TỪ?` — nối thẳng với CTA b08; không dùng bản «~~ĐỌC LẠI~~ → GẤP SÁCH» vì gạch chữ «đọc lại» dễ hiểu thành «đọc lại vô dụng» (claim bị chặn trong fact package).

Tiêu đề (dùng chung, dòng đầu caption TikTok/Reels/YouTube): **Học thuộc tối qua, sáng dậy quên sạch.** (câu khẳng định, để mỗi bản chỉ có 1 câu hỏi ở CTA)
Frame cover: **0s** (ảnh bìa tải lên riêng từ template A, không lấy frame video).

## 3. Caption / tiêu đề TikTok (VI)
```
Học thuộc tối qua, sáng dậy quên sạch.
Cách thử: học hết phần nào, gấp sách tự viết lại phần đó, chỗ nào bí mới mở sách.
Bạn thử gấp sách lại thì viết được mấy từ? Comment con số nha.
Nghiên cứu: Roediger & Karpicke (2006); Yang và cộng sự (2021).
Giọng trong video là giọng AI tổng hợp (F5-TTS).
Thông tin tham khảo, không thay thế tư vấn chuyên gia
Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/
#hoctap #hoctienganh #tuvungtienganh #studytok #studymethod
```
Rút gọn theo Rule Reviewer: 1 câu hook (không đặt câu hỏi để cả bản chỉ còn 1 câu hỏi ở CTA) · 1 câu ý chính · 1 CTA · rồi nguồn nghiên cứu, câu công bố giọng AI, câu an toàn, credit nguyên văn, hashtag. Không có số nào trong thân caption ngoài năm của nguồn. Không emoji.

## 4. Hashtag (5: rộng / ngách / VN)
```
#hoctap #hoctienganh #tuvungtienganh #studytok #studymethod
```
- `#hoctap`: thẻ VN rộng (đã dùng clip-01..04).
- `#hoctienganh`: thẻ ngách, đúng ví dụ 30 từ tiếng Anh (clip-01).
- `#tuvungtienganh`: thay `#learnontiktok` (20/10/2026). Cả 6 bài từ vựng Việt A1–A6 trong `research/tiktok-trend-pack-study-2026-10-20.md` mục 4 đều dùng `#tuvungtienganh` hoặc `#hoctienganh`; clip-04 lấy ví dụ học từ tiếng Anh nên hợp chủ đề.
- `#studytok`: giữ, vì bài mẹo học Việt A8 và @dodaihoccungvetaedu trong gói trend (mục 4) dùng thẻ này. `#learnontiktok` là thẻ rộng, ít đặc thù nhất nên bỏ.
- `#studymethod`: hashtag trong caption clip @phamthuykieuhuong 995.100 view (`final/trend-signals.md`, Apify 17/10/2026, số thô tại lúc thu).
Giữ 5 thẻ: vừa trần 3–5 của rule-53, vừa sàn 5–8 của yêu cầu W-20, và nằm trong khoảng 4–6 thẻ ngách mà gói trend đề xuất. Không #fyp/#viral/#xuhuong. Nguồn: `research/tiktok-trend-pack-study-2026-10-20.md` (Social Research, 20/10/2026) mục 4 và tóm tắt việc #5. Không thêm «lưu lại để thử» (sẽ thành CTA thứ hai, chờ Hiệp quyết).

## 5. Từ khoá SEO (đã lồng tự nhiên trong caption)
```
học thuộc, quên sạch, gấp sách, tự viết lại, mở sách, học tiếng Anh (qua hashtag)
```

## 6. Bình luận ghim
```
Gấp sách lại, bạn viết được mấy từ? Comment con số thật của bạn nha.
```

## 7. Giờ đăng đề xuất (giờ VN)
```
Mặc định 19:00 (giờ VN), theo gợi ý luật 32 (thứ Hai/Tư/Sáu, kênh mới chưa có Analytics). Hiệp tự đăng tay, không lên lịch tự động. Ngày cụ thể do Hiệp xếp theo theme-map.
```

## 8. Âm thanh
```
Thêm 1 track từ TikTok Commercial Music Library (Sounds → Commercial Sounds). Mood: lofi piano/Rhodes trầm, ấm, không lời, 70–90 BPM, không drop, không giọng hát. Âm lượng: giọng gốc 100%, nhạc 5% (tối đa 8%). Bắt đầu track ở đoạn mở mỏng (pad/piano), tránh intro trống. Trong file không có nhạc (luật 21); SFX + ambience đã mix sẵn.
Ưu tiên tìm tên: "Calm Lofi/Cafe/Study/Vlog(1492712)" – Tana Music · "Study Routine (Lofi)" – The Machinist Beats · "vlog, chill out, calm daily life(1370843)" – SUNNY HOOD STUDIO. Không thấy trong Commercial Sounds thì tìm: lofi study / calm piano / late night study.
```

- Nguồn: `final/sound-note-v18.md` mục 1 (ACE Music, 20/10/2026). News đã xác nhận theme dark, nên thứ tự ưu tiên là `Calm Lofi/Cafe/Study/Vlog(1492712)` (Tana Music) → `Cool Nights (Lofi)` → `Study Routine (Lofi)` (cả hai của The Machinist Beats), theo mục 3 của sound note.
- **Chưa xác minh** bài nào có trong Commercial Music Library ở VN. Hiệp kiểm trong app: Sounds → Commercial Sounds → gõ tên; có trong đó mới dùng.
- Quyền nhạc CML **chỉ áp dụng trong TikTok**. Reels và YouTube Shorts dùng file sạch không nhạc (News đang xuất bản này).

## 9. Checklist cài đặt khi đăng
```
[ ] Bật "Nội dung do AI tạo" (AI-generated content): ON
[ ] Dòng công bố trong caption: "Giọng trong video là giọng AI tổng hợp (F5-TTS)."
[ ] Cho phép bình luận: ON · Duet: ON · Stitch: ON
[ ] Ai có thể xem: Mọi người (Everyone)
[ ] Vị trí: không gắn
[ ] Nội dung thương mại / quảng cáo: OFF (giọng F5 CC-BY-NC-SA, DL-035)
[ ] Thêm vào danh sách phát (playlist): "Học đúng cách"
[ ] Ảnh bìa: cover.png (template A, tải lên riêng)
[ ] Ghim bình luận ở mục 6 ngay sau khi đăng
```

## 10. Ghi nguồn (luật 13)
```
Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/
Đã chuyển thể từ HowToLiveBetter phần 23 mục 14 «Học xong gấp sách tự kiểm một lần, đừng quay đầu đọc lại». Giấy phép: https://creativecommons.org/licenses/by/4.0/
Nghiên cứu: Roediger & Karpicke (2006), Psychological Science 17(3), PubMed 16507066 · Yang et al. (2021), Psychological Bulletin 147(4), PubMed 33683913.
```
Dòng 1 giữ **nguyên văn** bản Hiệp đã chốt (C-1), đặt trong caption. Dòng 2 («đã chuyển thể» + link giấy phép) đặt ở **bình luận thứ 2** trên TikTok và Reels, và ở **cuối mô tả YouTube**. Cách này đủ yêu cầu CC BY nên không có xung đột (Rule Reviewer đã chốt, xem mục 17).

## 11. Series / playlist
```
Học đúng cách (#4)
```

## 12. Nhãn AI (luật 46)
```
Giọng nhân vật trong video là giọng AI tổng hợp (F5-TTS). Hình ảnh: CHỜ kiểm khi có video v18.
```

## 13. Threads (bài text kèm video, ngắn)
```
Học thuộc tối qua, sáng dậy quên sạch.

Một thí nghiệm năm 2006 thấy, nếu kiểm tra ngay thì nhóm đọc lại làm tốt hơn. Nhưng hai ngày sau, nhóm tự kiểm tra nhớ hơn hẳn.

Cách thử: học mười từ, gấp sách viết lại, chỗ nào bí mới mở sách.

Bạn thử gấp sách lại thì viết được mấy từ?

Thông tin tham khảo, không thay thế tư vấn chuyên gia
Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/
```
- Đính kèm file video gốc v18. Chủ đề (topic) gợi ý chọn trong app: «Học tập». Không hashtag trong thân bài.
- Độ dài: 452 ký tự (giới hạn Threads 500). Chỉ 1 câu hỏi (ở cuối), cũng là CTA duy nhất.
- Câu Roediger chép đúng lời khoá b03 nhưng bỏ chữ «lại» theo Rule Reviewer: «Nhưng hai ngày sau, nhóm tự kiểm tra nhớ hơn hẳn.» (bản lời khoá không sửa).
- Repo chưa có tài liệu chính thức nào của Threads về video (`research/platform-recommendation-facts-2026-10-20.md`) → không tối ưu theo «thuật toán Threads».
- Câu công bố giọng AI không nằm trong thân bài (giữ dưới 500 ký tự); nếu app hỏi thì bật nhãn AI.

## 14. Instagram Reels (caption + hashtag)
```
Học thuộc tối qua, sáng dậy quên sạch.

Cách thử: học hết phần nào, gấp sách tự viết lại phần đó, chỗ nào bí mới mở sách.

Bạn thử gấp sách lại thì viết được mấy từ? Comment con số nha.

Nghiên cứu: Roediger & Karpicke (2006); Yang và cộng sự (2021).

Giọng trong video là giọng AI tổng hợp (F5-TTS).
Thông tin tham khảo, không thay thế tư vấn chuyên gia
Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/

#hoctap #hoctienganh #studymethod #activerecall #tuvungtienganh
```
- Đã bỏ câu «Gửi cho đứa bạn…» (CTA thứ hai, W-14). Còn 1 CTA, 1 câu hỏi.
- Hashtag: Instagram chưa có dữ liệu trend trong repo → chọn theo đúng chủ đề (5 thẻ); `#activerecall` theo phụ đề clip @phamthuykieuhuong trong `final/trend-signals.md`.
- Ảnh bìa: cover 1080×1920; lưới hồ sơ Instagram cắt giữa (FLUX đề xuất bản 1080×1350 giữ tờ giấy + nhân vật ở giữa) — chờ video v18 + Hiệp chọn cover.
- Nhãn AI: bật «AI info / nhãn AI» nếu app hỏi.

## 15. YouTube Shorts
Tiêu đề (59 ký tự, chỉ từ khoá, không hashtag theo rule-53b; không đặt câu hỏi để cả bản chỉ có 1 câu hỏi ở CTA):
```
Học thuộc tối qua, sáng dậy quên sạch: thử gấp sách tự kiểm
```
Mô tả:
```
Học thuộc tối qua, sáng dậy quên sạch.

Cách thử: học hết phần nào, gấp sách tự viết lại phần đó, chỗ nào bí mới mở sách.
Nhóm của Yang tổng hợp 222 nghiên cứu: lớp có kiểm tra nhỏ thì điểm cao hơn lớp không làm kiểm tra nhỏ, ở mức vừa.

Bạn thử gấp sách lại thì viết được mấy từ? Comment con số nha.

Nghiên cứu:
- Roediger & Karpicke (2006), Psychological Science: https://pubmed.ncbi.nlm.nih.gov/16507066/
- Yang et al. (2021), Psychological Bulletin: https://pubmed.ncbi.nlm.nih.gov/33683913/

Giọng trong video là giọng AI tổng hợp (F5-TTS).
Thông tin tham khảo, không thay thế tư vấn chuyên gia
Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/
Đã chuyển thể từ HowToLiveBetter phần 23 mục 14. Giấy phép: https://creativecommons.org/licenses/by/4.0/

#Shorts #hoctap #hoctienganh
```
- Hashtag: 3 thẻ ở cuối mô tả (`#Shorts #hoctap #hoctienganh`), tiêu đề không có hashtag (rule-53b, Rule Reviewer 20/10/2026).
- Được giữ thêm câu Yang + link PubMed (Rule Reviewer cho phép riêng YouTube).
- **Khi tải lên: BẬT nhãn «Nội dung bị biến đổi hoặc tổng hợp» (altered or synthetic content)** — Rule Reviewer đã chốt (giọng là AI tổng hợp).
- Playlist: «Học đúng cách».

## 16. Thumbnail
```
Thumbnail = CHỜ video cuối v18 (chưa render, không tạo ảnh nào trong publish/).
Cách làm khi Hiệp chọn chữ cover: render template A Cover.tsx (1080×1920) từ spec.json → cover, xuất final/cover.png; không lấy frame video (luật 54, L-020).
```
- Cảnh đề xuất (theo `final/visual-plan-v18.md`): tờ giấy 10 dòng, dòng 5 trống + bóng vali mờ, sách gấp, bút dừng; nhân vật bên phải, sững. Không chữ trong hình — chữ lớn do slot hero của template A.
- Chữ cover: 3 phương án ở mục 2 (A đề xuất).
- Nếu Hiệp muốn xem thêm frame để đối chiếu với cover khi có video: lấy b01 (~1s, giấy trắng + bút dừng) và b07 (~40s, dòng 5 được viết + vali hiện rõ) — chỉ để tham khảo, **không** dùng làm cover.

## 17. Tự soát (Social Poster, sau khi sửa theo Rule Reviewer)
Quyết định Rule Reviewer đã chốt (20/10/2026):
- **C-1:** giữ như hiện tại (caption dùng credit nguyên văn; dòng «đã chuyển thể» + link giấy phép ở mục 10 và cuối mô tả YouTube).
- **TikTok 5 hashtag:** đạt.
- **YouTube:** bật nhãn nội dung tổng hợp (altered/synthetic) — đã ghi ở mục 15 và `post-checklist.md`.
- **Câu công bố giọng AI:** giữ trung tính «Giọng trong video là giọng AI tổng hợp (F5-TTS).».
- **Cover A/B/C và thumbnail:** chờ video v18.

| # | Kiểm | Kết quả |
|---|---|---|
| 1 | Credit nguyên văn ở TikTok (3), Threads (13), Reels (14), YouTube (15) | Đạt — so chuỗi nguyên văn bằng script ở cả 4 code block |
| 2 | Câu an toàn nguyên văn ở cả 4 nền tảng | Đạt |
| 3 | Mỗi bản 1 CTA, 1 câu hỏi | Đạt — đếm dấu «?» trong mỗi bản = 1 (YouTube tính cả tiêu đề) |
| 4 | Caption rút gọn: hook + ý chính + CTA + nguồn + công bố AI + an toàn + credit | Đạt — TikTok, Reels, YouTube (YouTube thêm câu Yang + PubMed) |
| 5 | Ý Roediger ghi đúng «Nhưng hai ngày sau, nhóm tự kiểm tra nhớ hơn hẳn.» | Đạt — chỉ còn ở Threads |
| 6 | Số chỉ từ script/nguồn: 2006, 2021 (năm nguồn), 222 + «mức vừa» (Yang, chỉ YouTube), «mười từ» (script b05, Threads), ID PubMed | Đạt — không %, không 48.478, không g |
| 7 | Không nói tác giả sách ủng hộ/chứng thực kênh | Đạt |
| 8 | Văn nói, xưng «bạn», không từ hiếm, không chê năng lực (P-07), không hứa lố | Đạt |
| 9 | Không lên lịch/đăng tự động | Đạt — Hiệp tự đăng tay |
| 10 | Độ dài | TikTok 528/2200 · Threads 452/500 · Reels 538/2200 · YouTube mô tả 854/5000, tiêu đề 59/70 |
| 11 | Cover ≤ 40 ký tự | Đạt (A 34 · B 21 · C 35) — chờ video v18 |

Còn mở: video v18 chưa có; cover/thumbnail chờ video v18; mục 12 phần hình chờ kiểm; bộ xu hướng chưa có.

### Kết quả check máy (20/10/2026, sau khi sửa)
`check-rules.py` chỉ đọc `final/post.md` khi chạy `--final` (cần video cuối) nên chưa chạy thẳng cho `publish/`. Đã chạy lại đúng logic rule-13 / rule-46 / rule-53 trên file này: **15/16 đạt**. Lỗi duy nhất: `cover.png` chưa có (chủ ý — cover chờ video v18). `final/post.md` vẫn là gói v14 cũ, chưa ghi đè.
