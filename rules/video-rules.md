# @hi.oneup: Bộ luật sản xuất video (v2, 12/10/2026)

Kênh: https://www.tiktok.com/@hi.oneup · Repo: `oneup-studio` (đường dẫn trong file là đường dẫn tương đối tính từ gốc repo)
Bản này thay thế toàn bộ v1. Khi có mâu thuẫn, bản này là chuẩn.

## A. Định dạng
1. **Ngôn ngữ:** giọng nói tiếng Việt. Caption tiếng Anh highlight từng từ.
2. **Giọng:** giọng thật của Hiệp, thu bằng iPhone. Không dùng giọng AI. Giữ hơi thở tự nhiên, chỉ cắt khoảng lặng trên 0,6s.
3. **Lên hình:** có clip lộ mặt, có clip không lộ mặt.
4. **Độ dài:** 55–60s, 9:16, 1080×1920, 30fps, H.264 High yuv420p, màu bt709, âm thanh −14 LUFS.
5. **Phong cách (xoay vòng):** talking head · chữ trên b-roll tự quay · quay màn hình app OneUp kèm lồng tiếng · POV bàn làm việc / tay.
6. **Tỉ lệ hình:** tự quay ≥50%, stock ≤30%, phần còn lại là minh hoạ (diagram, khái niệm động, số liệu, trước/sau).

## B. Script & nội dung
7. **Cấu trúc mặc định:** Hook 0–3s → Vấn đề → Giải thích kèm minh hoạ (3–4 beat) → Bằng chứng / trước-sau → Việc làm ngay → câu cuối nối lại hook để clip lặp tự nhiên. Thỉnh thoảng xen dạng "3 điều" hoặc kể chuyện cá nhân để tránh lặp. Script khoảng 150–170 từ tiếng Việt.
8. **CTA:** câu hỏi kéo comment. Từ tuần 3 nhắc OneUp theo luật 11.
9. **Nhịp đổi hình:** theo nội dung, mỗi cảnh tối đa 8s. Không cắt đều tăm tắp.
10. **Chủ đề:** không giới hạn (bỏ các mục chỉ áp dụng cho luật / thủ tục Trung Quốc). Nguồn: HowToLiveBetter.
11. **Lịch đưa app:** tuần 1–2 không có app · tuần 3–4 có màn hình app ngắn · từ tuần 5 có Omi.
12. **Clip đầu tiên:** trụ 1 "Làm ít, xong nhiều", clip 1 (`content/clips/clip-01-implementation-intention/`).
13. **Ghi nguồn:** HowToLiveBetter (CC BY 4.0, kèm link giấy phép, ghi "đã chuyển thể") chỉ đặt trong caption bài đăng.

## C. Hình ảnh & brand
14. **Brand:**
    - Màu: ink `#111111`, paper `#F7F7F5`. Màu khác chỉ dùng khi mang nghĩa. Xanh lá chỉ cho khoảnh khắc "xong / +1".
    - Không emoji, không neon, không glow, không confetti.
    - Logo 05-pair-plus đặt nhỏ ở góc trên trái suốt clip. Mọi chữ nằm trong safe-zone TikTok.
    - Chi tiết: `brand/brand-index.md`, `brand/brand-tokens.json`.
15. **Font:** toàn bộ chữ trên màn hình (tiếng Anh và tiếng Việt) dùng Be Vietnam Pro (OFL, 400/500/600/700, `brand/fonts/`), font được nhúng sẵn, không dùng font hệ thống. Không trộn 2 font trong một dòng. DM Sans (font của app) chưa dùng cho video cho đến khi Hiệp đổi luật.
16. **Chữ chính trên màn hình:** chỉ tiếng Anh, khớp với caption.
17. **Theme:**
    - Mỗi clip là LIGHT (tích cực) hoặc DARK (mặt trái), xét theo hook. Không quá 2 clip cùng theme liên tiếp. Một clip chỉ một theme.
    - Bảng phân theme: `content/theme-map.md` (clip 1 = LIGHT).
18. **Minh hoạ:** diagram dùng nét vẽ tay (rough.js / Open Peeps), icon dùng Phosphor (đơn sắc).
19. **Motion:** chọn theo từng script, mỗi beat một hiệu ứng chính, lấy từ catalog awesome-ai-motion (637 effect, xem `refs/README.md`) bằng skill `skills/motion-picks-per-script/SKILL.md`. Ghi vào `logs/effects-log.md` để không lặp.
20. **Hậu kỳ:** grain phim nhẹ toàn clip. Bố cục lệch, căn trái. Theo checklist anti-AI-look (`research/production-system-research-vi.md` §6).

## D. Âm thanh & tài sản
21. **Nhạc:** không có nhạc trong file. Hiệp thêm nhạc từ TikTok Commercial Music Library lúc đăng.
22. **SFX:** được dùng tiếng động nhẹ (click, tick, whoosh nhỏ), chỉ lấy file CC0 (Freesound) hoặc Mixkit. Ghi nguồn từng file vào `assets/sfx/SOURCES.md`.
23. **Stock:** Pexels + Pixabay + Mixkit. Lọc bỏ ảnh AI, ưu tiên cảnh không nhìn vào camera.
24. **Chỉ dùng công cụ miễn phí:** không video AI, không giọng AI, nên không cần nhãn AI.

## E. Công cụ & pipeline
25. **Engine:**
    - HyperFrames (Apache 2.0) + GSAP cài local (không dùng CDN). Manim CE cho cảnh biểu đồ. FFmpeg để ghép và hậu kỳ.
    - Template: `templates/hyperframes-base/`.
    - Pipeline: `pipeline/pipeline.md`.
26. **Transcribe:** whisper.cpp large-v3 (Metal, `-l vi`) lấy timestamp từng từ. Caption tiếng Anh được rải theo từng cụm câu tiếng Việt. Bản dịch tiếng Anh được duyệt cùng script.
27. **Nơi render:** bản nháp render trên box ảo, bản final render trên Mac I-Am-Focused.
28. **Mức tự động:** agent làm toàn bộ, Hiệp duyệt 2 lần (script trước khi thu, final trước khi đăng). Duyệt beat sheet là tuỳ chọn.
29. **Quay:** agent gửi shot list cùng script. Hiệp AirDrop giọng và b-roll vào `footage/inbox/` trên Mac. File footage và render không commit lên git.
30. **Cover:** frame hook kèm chữ to.

## F. Lịch & đăng
31. **Tần suất:** 3 clip/tuần trong 2 tuần đầu, sau đó đánh giá lại (mục tiêu 3–4 clip/tuần).
32. **Đăng:** agent chuẩn bị gói sẵn đăng (mp4, caption, hashtag, credit, cover) trong `renders/ready/`, rồi nhắc Hiệp lúc 19:00 thứ Hai, Tư, Sáu, Chủ nhật. Hiệp tự đăng.

## G. Cải tiến liên tục
33. **Nhật ký quyết định** (`logs/decision-log.md`):
    - Ghi mọi câu hỏi, yêu cầu, góp ý sửa và quyết định của Hiệp, gồm ngày, tóm tắt yêu cầu (giữ nguyên ý), quyết định, luật / file bị ảnh hưởng.
    - Agent đọc lại log trước khi làm mỗi clip mới.
    - Góp ý lặp lại từ 2 lần trở lên thì nâng thành luật trong file này hoặc thành skill trong `skills/`, rồi ghi lại việc nâng đó.
    - Mỗi Chủ nhật có retro tuần trong cùng file: điều tốt, điều cần sửa, chỉ số, luật hay skill đã đổi.
34. **Chuẩn chất lượng:** mọi hình gửi Hiệp (preview, storyboard, frame, video) phải đạt mức "premium". Agent tự xem và sửa ít nhất 2 vòng trước khi gửi (sau góp ý "xấu quá" ngày 12/10/2026).
35. **Storyboard trước khi duyệt script:** mỗi clip có storyboard (1 frame 1080×1920 cho mỗi beat, kèm contact sheet) nằm trong `content/clips/NN-slug/storyboard/`, gửi cùng script để Hiệp duyệt.

## Changelog
- **v2.1, 12/10/2026:** thêm luật 33 (nhật ký quyết định + retro tuần), luật 34 (chuẩn chất lượng premium), luật 35 (storyboard trước khi duyệt script).
- **v2, 12/10/2026:**
  - Gộp 21 luật v1 với 20 quyết định đã duyệt.
  - Độ dài đổi từ 30–45s thành 55–60s.
  - Render đổi từ "chỉ Mac" thành nháp trên box, final trên Mac.
  - Tần suất trong 2 tuần đầu đổi từ 3–4 thành 3 clip/tuần.
  - Thêm: SFX CC0, cấu trúc script, CTA, tỉ lệ hình, nhịp, grain, minh hoạ, stock, engine, transcribe, shot list, cover.
  - Luật 7 cũ "cần asset" bỏ, vì đã có brand.
  - Đường dẫn đổi sang đường dẫn trong repo.
- **v1.3, 12/10/2026:** thêm luật theme LIGHT/DARK (luật 21 cũ).
- **v1.2, 12/10/2026:** font Be Vietnam Pro cho mọi chữ (luật 20 cũ).
- **v1.1, 12/10/2026:** motion chọn theo từng script (luật 19 cũ).
- **v1.0, 12/10/2026:** 18 quyết định đầu tiên.
