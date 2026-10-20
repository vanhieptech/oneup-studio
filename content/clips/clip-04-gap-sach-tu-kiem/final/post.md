---
title: "Bộ final đăng clip-04 v18 «Gấp sách tự kiểm» (TikTok · Threads · Instagram Reels · YouTube Shorts)"
date: 2026-10-20
source: "oneup-studio (Social Poster soạn trong repo) · lời khoá final/script-v18-LOCKED.md · HowToLiveBetter phần 23 mục 14"
id: clip-04.post
type: post-package
template: post-package v1 (rule-53, DL-045) + bản đa nền tảng (W-20)
status: bộ final v18, Rule Reviewer đã soát phần chữ (23c82a7), chờ --final + Hiệp duyệt
updated: 2026-10-21
video: "final/clip-04-v18-tiktok.mp4 (TikTok) · final/clip-04-v18-reels.mp4 (Reels, YouTube Shorts, Threads)"
cover: "final/cover.png (1080×1920) · final/cover-1080x1350.png (IG feed, Threads) — FLUX b7d1bba, Rule Reviewer duyệt"
hashtags: ["#hoctap", "#hoctienganh", "#tuvungtienganh", "#studytok", "#studymethod"]
tags: [clip-04, post, tiktok, threads, instagram, youtube-shorts, w-20, final]
---
# Bộ final đăng clip-04 v18 «Gấp sách tự kiểm»

> **Bộ final, chưa đăng.** Không đăng, không lên lịch, không đăng nhập tài khoản nào. Hiệp tự đăng tay sau khi Rule Reviewer soát đạt và Hiệp duyệt.
> Lời bám đúng `final/script-v18-LOCKED.md` (Hiệp «Oke duyệt», L-078). Claim chỉ lấy từ script khoá + `final/script-v18-table.md` (mục Claim → nguồn) + `final/fact-package-redo-2026-10-19.md` + HowToLiveBetter phần 23 mục 14.
> Bộ xu hướng `research/tiktok-trend-pack-study-2026-10-20.md` **chưa có trong repo** lúc soạn (20/10/2026, 23:2x giờ VN) → **chưa áp bộ xu hướng**. Hashtag lấy từ hệ thẻ đã dùng ở clip-01..04 + `final/trend-signals.md` (Apify 17/10/2026).

Mục 1–12 là gói TikTok theo `templates/post-package.md` (giữ đúng tên mục để check rule-53 đọc được). Mục 13–15 là bản Threads, Instagram Reels, YouTube Shorts. Mục 16 là thumbnail. Mục 17 là tự soát.

## 1. File video
```
TikTok:          content/clips/clip-04-gap-sach-tu-kiem/final/clip-04-v18-tiktok.mp4 · 48,90s · 1080×1920 (9:16) · 30fps · H.264 High + AAC LC 48 kHz mono · −14,2 LUFS · peak −0,9 dBFS · 26,6 MB
Instagram Reels: content/clips/clip-04-gap-sach-tu-kiem/final/clip-04-v18-reels.mp4 · 48,90s · 1080×1920 · 30fps · H.264 High + AAC LC 48 kHz mono · −14,2 LUFS · peak −0,9 dBFS · 27,0 MB (phụ đề đặt cao, tránh vùng UI Reels)
YouTube Shorts:  clip-04-v18-reels.mp4 (cùng file với Reels)
Threads:         clip-04-v18-reels.mp4 (cùng file với Reels)
Bản xem nhanh:   clip-04-v18-light.mp4 · 48,90s · 540×960 · 30fps · −14,7 LUFS · 1,75 MB — chỉ để xem, không đăng
```
- Số đo bằng ffprobe + ebur128 trên box (21/10/2026, 03:3x giờ VN). `final/out/clip-04-final.mp4` trùng md5 với `clip-04-v18-tiktok.mp4` (ee514a7b…).
- File nào cũng **không có nhạc** (luật 21), nên cả hai bản đều là «file sạch». Nhạc CML chỉ thêm trong app TikTok. Shorts và Threads dùng bản reels vì phụ đề nằm cao hơn và hai bản cùng nội dung. Phụ đề chỉ được đặt tránh UI của Reels, **chưa đo riêng** vùng UI của Shorts.
- Bản tiktok/reels không có trong git (chỉ bản light đã commit). Hiệp lấy file trên Mac ở cùng đường dẫn.
- Không file nào có logo TikTok (render gốc, không phải bản tải về từ TikTok).

## 2. Chữ trên cover (≤ 40 ký tự)
```
HỌC THUỘC TỐI QUA? SÁNG QUÊN SẠCH!
```
**Đã render phương án A** (FLUX, commit b7d1bba, Rule Reviewer duyệt). Chữ đọc trên ảnh `final/cover.png`: tag `#04 HỌC ĐÚNG CÁCH` · hàng 1 `HỌC THUỘC TỐI QUA?` (chữ thường, không gạch, strike −1) · hàng 2 `SÁNG QUÊN SẠCH!` (pill đen) · logo `OneUp.` · chibi buồn có dấu «!!». Theme LIGHT, khớp video. B và C không render.

Ba phương án ban đầu (đều ≤ 40 ký tự, render bằng template A `Cover.tsx`, không lấy frame video — luật 54, L-020):
- **A (đã render, 34 ký tự):** `HỌC THUỘC TỐI QUA?` → `SÁNG QUÊN SẠCH!` (pill). Khớp hook b01. Props trong `final/spec.json → cover` = `final/cover/cover-a.props.json` (theme light, strike −1).
- **B (21 ký tự):** `TỐI THUỘC,` → `SÁNG QUÊN?` — đề xuất của FLUX Visual trong `final/visual-plan-v18.md`.
- **C (35 ký tự):** `GẤP SÁCH LẠI,` → `CÒN VIẾT ĐƯỢC MẤY TỪ?` — nối thẳng với CTA b08; không dùng bản «~~ĐỌC LẠI~~ → GẤP SÁCH» vì gạch chữ «đọc lại» dễ hiểu thành «đọc lại vô dụng» (claim bị chặn trong fact package).

Tiêu đề (dùng chung, dòng đầu caption TikTok/Reels/YouTube): **Học thuộc tối qua, sáng dậy quên sạch.** (câu khẳng định, để mỗi bản chỉ có 1 câu hỏi ở CTA)
Frame cover: **0s** (trường bắt buộc của rule-53, không phải frame video: ảnh bìa là `final/cover.png` tải lên riêng từ template A; trên mọi nền tảng không chọn frame video làm ảnh bìa, luật 54).

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
Thử gấp sách lại, bạn viết được mấy từ? Comment con số thật của bạn nha.
```
Thêm «Thử» ở đầu câu (21/10/2026) theo L-073: câu nói với người xem không mở bằng cụm động từ trơ «Gấp sách lại,».

## 7. Giờ đăng đề xuất (giờ VN)
```
Mặc định 19:00 (giờ VN), theo gợi ý luật 32 (thứ Hai/Tư/Sáu, kênh mới chưa có Analytics). Hiệp tự đăng tay, không lên lịch tự động. Ngày cụ thể do Hiệp xếp theo theme-map.
```

## 8. Âm thanh
```
Thêm 1 track từ TikTok Commercial Music Library (Sounds → Commercial Sounds). Mood: chill acoustic / cafe lofi sáng, major key, guitar mộc + Rhodes, không lời, 85–95 BPM, không drop, không giọng hát. Âm lượng: giọng gốc 100%, nhạc 5% (tối đa 8%). Bắt đầu track ở đoạn mở mỏng (guitar/piano), tránh intro trống. Trong file không có nhạc (luật 21); SFX + ambience đã mix sẵn.
Ưu tiên tìm tên: "vlog, chill out, calm daily life(1370843)" – SUNNY HOOD STUDIO · "Coffee and Daydreams" – Tokyo.Beats · "Calm Lofi/Cafe/Study/Vlog(1492712)" – Tana Music. Không thấy trong Commercial Sounds thì tìm: chill acoustic / cafe lofi / vlog daily life.
```

- Nguồn: `final/sound-note-v18.md` mục 1 (ACE Music, bản theme light, commit 913ccdc, 21/10/2026). Bản v18 render theme light (`spec.json`, f1cd4fd), nên ưu tiên lần lượt là `vlog, chill out, calm daily life(1370843)` (SUNNY HOOD STUDIO), `Coffee and Daydreams` (Tokyo.Beats), rồi `Calm Lofi/Cafe/Study/Vlog(1492712)` (Tana Music).
- **Chưa xác minh** bài nào có trong Commercial Music Library ở VN. Hiệp kiểm trong app: Sounds → Commercial Sounds → gõ tên; có trong đó mới dùng.
- Quyền nhạc CML **chỉ áp dụng trong TikTok**. Reels, YouTube Shorts và Threads đăng `clip-04-v18-reels.mp4`, không thêm nhạc.
- **Kiểm file (21/10/2026):** check-rules `rule-21 no music` ✔. Trong file có 29 hit SFX (swish 9, tick 4, pen 4, pop 4, snap 3, rise 3, ding 2, theo `final/timing.json → sfx_mix`) + 1 lớp `ambience` chạy suốt clip; `rule-50`: 8/8 chuyển cảnh có SFX. Đo tay: đoạn 42,3–43,2s giọng im hẳn (−91 dB trong voice track) nhưng file mp4 vẫn có tiếng (trung bình −57 dB, đỉnh −32 dB, có swish ở 43,15s); end card 47,8–48,8s trung bình −63 dB (ambience); không có đoạn lặng hẳn < −70 dB nào ≥ 0,3s.

## 9. Checklist cài đặt khi đăng
```
[ ] Bật "Nội dung do AI tạo" (AI-generated content): ON
[ ] Dòng công bố trong caption: "Giọng trong video là giọng AI tổng hợp (F5-TTS)."
[ ] Cho phép bình luận: ON · Duet: ON · Stitch: ON
[ ] Ai có thể xem: Mọi người (Everyone)
[ ] Vị trí: không gắn
[ ] Nội dung thương mại / quảng cáo: OFF (giọng F5 CC-BY-NC-SA, DL-035)
[ ] Thêm vào danh sách phát (playlist): "Học đúng cách"
[ ] Ảnh bìa: final/cover.png (1080×1920, template A, «Tải ảnh bìa lên», không chọn frame video)
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
Giọng nhân vật trong video là giọng AI tổng hợp (F5-TTS). Hình: nhân vật và cảnh vẽ bằng code (video-engine + 2 tấm motion HyperFrames b03/b06), không dùng ảnh/video AI.
```
- Kiểm 21/10/2026: check-rules `rule-46` ✔ (Hiệp = F5 · Thái Sơn); `rule-42` ✔ tấm b03/b06 là HyperFrames. Phần «không ảnh/video AI» dựa trên spec + check-rules, mình không kiểm nguồn từng hình.
- Frame tự trích (1,5s · 18s · 40,4s · 48,5s ở cả 2 bản): end card có câu an toàn, nguồn «Roediger & Karpicke 2006 · Yang et al. 2021» và credit đủ chữ, link `https://chuanman2707.github.io/HowToLiveBetter/`. End card để dấu nháy cong ‘…’, caption để nháy thẳng '…' (không đổi nghĩa). Chữ và phụ đề nằm trong khung, không chạm mép. Bản reels: phụ đề lên khoảng giữa màn hình (y ≈ 45–55%), bản tiktok để phụ đề ở khoảng 78–88%. Không bản nào có logo TikTok, chỉ có logo OneUp ở góc trên trái.
- Bật nhãn AI trên cả 4 nền tảng (TikTok mục 9, Reels mục 14, YouTube mục 15, Threads mục 13).

## 13. Threads (bài text kèm video, ngắn)
```
Học thuộc tối qua, sáng dậy quên sạch.

Một thí nghiệm năm 2006 thấy, nếu kiểm tra ngay thì nhóm đọc lại làm tốt hơn. Nhưng hai ngày sau, nhóm tự kiểm tra nhớ hơn hẳn.

Cách thử: học mười từ, gấp sách viết lại, chỗ nào bí mới mở sách.

Bạn thử gấp sách lại thì viết được mấy từ?

Thông tin tham khảo, không thay thế tư vấn chuyên gia
Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/
```
- Đính kèm `final/clip-04-v18-reels.mp4`. Ảnh bìa: `final/cover-1080x1350.png` (4:5), tải lên riêng. App Threads có cho đặt ảnh bìa riêng cho video hay không thì mình chưa xác minh; **nếu không tải ảnh riêng được thì chờ Hiệp quyết** (rule-54). Chủ đề (topic) gợi ý chọn trong app: «Học tập» (1 topic tag, rule-53b). Không hashtag trong thân bài.
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
- Video: `final/clip-04-v18-reels.mp4` (không logo TikTok, không nhạc).
- Ảnh bìa Reels: `final/cover.png` (1080×1920), tải lên riêng. Ô lưới hồ sơ / feed 4:5: `final/cover-1080x1350.png`. Bản này cắt y 265–1615 từ cover, vẫn còn đủ tag `#04 HỌC ĐÚNG CÁCH`, hai hàng hero, logo và nhân vật (chỉ mất một chút bóng dưới chân). Nếu app chỉ cho kéo khung cắt trên ảnh 9:16 thì kéo sao cho khớp bản 1350.
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
- Video: `final/clip-04-v18-reels.mp4`. Ảnh bìa: `final/cover.png`, tải lên riêng. Mình chưa xác minh app YouTube có cho tải ảnh bìa riêng cho Shorts hay không; **nếu không tải ảnh riêng được thì chờ Hiệp quyết** (rule-54).
- Playlist: «Học đúng cách».

## 16. Thumbnail
```
TikTok · Reels · YouTube Shorts: content/clips/clip-04-gap-sach-tu-kiem/final/cover.png        1080×1920 · md5 8d13787f… = final/cover/cover-a.png (render template A Cover.tsx, props cover-a.props.json)
IG feed/lưới hồ sơ · Threads:   content/clips/clip-04-gap-sach-tu-kiem/final/cover-1080x1350.png 1080×1350 · cắt 4:5 từ cover.png (y 265–1615)
```
- Nguồn: FLUX Visual, commit b7d1bba (21/10/2026, 03:37 giờ VN), Rule Reviewer đã duyệt. Render từ template A, không lấy frame video (luật 54, L-020). check-rules lượt trước của News (trước b7d1bba): `rule-54` ✔, `L-020` ✔.
- Chữ trên ảnh (đọc trực tiếp từ file): `#04 HỌC ĐÚNG CÁCH` · `HỌC THUỘC TỐI QUA?` · `SÁNG QUÊN SẠCH!` · `OneUp.`. Đúng phương án A ở mục 2, đủ dấu tiếng Việt.
- Bản 1080×1350: không mất chữ nào. Tag, hai hàng hero và logo nằm trọn trong khung, nhân vật chỉ mất phần bóng dưới chân.
- Theme LIGHT, khớp video v18.

## 17. Tự soát (Social Poster, bộ final 21/10/2026; Rule Reviewer đã soát phần chữ 23c82a7)
Quyết định Rule Reviewer đã chốt (20/10/2026): C-1 giữ credit nguyên văn trong caption, dòng «đã chuyển thể» + link giấy phép ở mục 10 và cuối mô tả YouTube; YouTube bật nhãn altered/synthetic; câu công bố giọng AI trung tính; rule-53b (hashtag theo nền tảng, commit 680d4b6). Cover A: Rule Reviewer duyệt (b7d1bba).

### Tiêu chí Rule Reviewer sẽ soát (tự kiểm trước)
| # | Tiêu chí | Kết quả |
|---|---|---|
| T1 | Tiêu đề ≤ 70 ký tự | Đạt. YouTube 59/70 (chỉ từ khoá, không hashtag). Dòng tiêu đề chung TikTok/Reels «Học thuộc tối qua, sáng dậy quên sạch.» 38 ký tự |
| T2 | Hashtag đúng rule-53b | Đạt. TikTok 5 thẻ (trong 3–5; rule-53b khuyên 3–4 thẻ ngách, Rule Reviewer đã cho giữ 5 cho clip-04), `#hoctienganh` dùng được vì clip lấy ví dụ 30 từ tiếng Anh. Reels 5/5, không #reels. YouTube 3 thẻ ở cuối mô tả (`#Shorts #hoctap #hoctienganh`), tiêu đề 0 thẻ. Threads 0 hashtag trong thân bài, 1 topic «Học tập», 452/500 ký tự |
| T3 | Credit CC BY 4.0 nguyên văn + câu an toàn ở cả 4 bản | Đạt. Script so chuỗi nguyên văn trong code block mục 3, 13, 14, 15 (mô tả): 4/4 có credit, 4/4 có câu an toàn. End card trong video cũng có cả hai câu (xem frame 48,5s) |
| T4 | Không câu nào ám chỉ tác giả xác nhận/bảo trợ | Đạt. Không có chữ «xác nhận / bảo trợ / ủng hộ / chứng thực / tài trợ / endorse» trong 4 bản. Credit chỉ ghi «Nội dung dựa trên…» |
| T5 | Chữ cover + caption chỉ nói điều script v18 đã nói | Đạt, đối chiếu từng câu với `final/script-v18-LOCKED.md`: hook ← câu 1 (đổi «?» thành «.»); «Cách thử: học hết phần nào, gấp sách tự viết lại phần đó, chỗ nào bí mới mở sách» ← câu 5; CTA ← câu 8; Threads «Một thí nghiệm năm 2006…nhớ hơn hẳn» ← câu 3 (bỏ chữ «lại» theo Rule Reviewer); Threads «học mười từ» ← câu 5 «mỗi phần mười từ» (voice plan v18 còn đúng «mười từ»); YouTube câu Yang ← câu 6 (giữ «222», «ở mức vừa»); tiêu đề YouTube «thử gấp sách tự kiểm» ← tên mục HTB 23.14. Cover `HỌC THUỘC TỐI QUA? / SÁNG QUÊN SẠCH!` ← câu 1. Ngoài năm của nguồn, ID PubMed, 222 và «mười từ», không có số nào khác; không %; không hứa kết quả |
| T6 | Bản 1080×1350 không mất chữ | Đạt. Đã xem ảnh: tag `#04 HỌC ĐÚNG CÁCH`, 2 hàng hero và logo `OneUp.` còn đủ; chỉ mất bóng dưới chân nhân vật |

### Các mục khác
| # | Kiểm | Kết quả |
|---|---|---|
| 1 | Mỗi bản 1 CTA, 1 câu hỏi | Đạt. Đếm «?»: TikTok 1 · Threads 1 · Reels 1 · YouTube tiêu đề 0 + mô tả 1 |
| 2 | Văn nói, xưng «bạn», không từ hiếm, không chê năng lực (P-07) | Đạt. Bình luận ghim thêm «Thử» ở đầu câu theo L-073 (sửa 21/10, Rule Reviewer soát lại giúp) |
| 3 | Không lên lịch / đăng tự động | Đạt. Hiệp tự đăng tay |
| 4 | Video thật (ffprobe) | 48,90s · 1080×1920 · 30fps · H.264 High · AAC 48 kHz mono · −14,2 LUFS · peak −0,9 dBFS (tiktok + reels) |
| 5 | Không nhạc, có SFX + ambience (luật 21/50) | Đạt (mục 8) |
| 6 | End card credit, vùng an toàn, Reels không logo TikTok | Đạt (mục 12) |
| 7 | Cover từ template A, không frame video (luật 54, L-020) | Đạt (mục 16) |

### Độ dài thật (đếm bằng script, 21/10/2026)
| Bản | Độ dài | Giới hạn |
|---|---|---|
| TikTok caption (mục 3) | 529 ký tự | 2200 |
| Threads (mục 13) | 452 ký tự | 500 |
| Reels caption (mục 14) | 538 ký tự | 2200 |
| YouTube tiêu đề / mô tả (mục 15) | 59 / 854 ký tự | 100 (OneUp ≤ 70) / 5000 |
| Video | 48,90s, cả 3 file | L-080: độ dài theo nội dung |

### Còn mở, cần Rule Reviewer hoặc Hiệp quyết
- **Shorts/Threads dùng bản reels:** phụ đề chỉ được đặt tránh UI của Reels, chưa đo riêng UI Shorts. App Threads/YouTube có cho tải ảnh bìa riêng hay không thì mình chưa xác minh; nếu không tải ảnh riêng được thì chờ Hiệp quyết (rule-54, Rule Reviewer chuyển Hiệp).
- **CML ở VN:** chưa xác minh bài nào có sẵn, Hiệp kiểm trong app.
