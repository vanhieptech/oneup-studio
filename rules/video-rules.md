---
id: rules
type: rules
status: active
updated: 2026-10-13
version: 3.8
tags: [rules, source-of-truth]
---
# @hi.oneup: Bộ luật sản xuất video (v3.8, 14/10/2026)

Kênh: https://www.tiktok.com/@hi.oneup · Repo: `oneup-studio` (đường dẫn trong file là đường dẫn tương đối tính từ gốc repo)
Bản này thay thế v2.x (đã audit toàn bộ 45 luật ngày 13/10/2026, xem `logs/rules-audit-2026-10-13.md`). Khi có mâu thuẫn, bản này là chuẩn. Luật đánh số cao hơn **không** tự động ghi đè luật thấp hơn: mỗi luật đã được sửa để không còn mâu thuẫn.

## A. Định dạng
1. **Ngôn ngữ:** giọng nói tiếng Việt. Caption tiếng Anh highlight từng từ.
2. **Giọng (DL-035):** cả hai nhân vật dùng **giọng AI F5-TTS** theo luật 46: nhân vật chibi **Hiệp** = "F5 · Thái Sơn" (nam, miền Nam), **Omi** = "F5 · Mỹ Duyên" (nữ, miền Nam). Giọng mẫu (reference) là câu tổng hợp bằng preset VieNeu, không clone giọng thật của ai (kể cả Hiệp). Hiệp vẫn có thể tự thu giọng thật cho một clip (thì clip đó không dùng giọng AI cho Hiệp); khi đó giữ hơi thở tự nhiên, chỉ cắt khoảng lặng trên 0,6s.
3. **Lên hình:** series này **chỉ dùng comic + motion graphics**, không quay mặt/cảnh thật (DL-027). Hiệp lên hình bằng nhân vật chibi (luật 43).
4. **Độ dài:** 55–60s, 9:16, 1080×1920, 30fps, H.264 High yuv420p, màu bt709, âm thanh −14 LUFS.
5. **Phong cách (xoay vòng trong khuôn comic):** beat kể chuyện comic (Remotion, luật 42) · beat giải thích motion graphics (HyperFrames) · màn hình app OneUp dựng lại bằng vector/mockup trong motion beat (từ tuần 3). Không talking head, không b-roll tự quay trong series này.
6. **Tỉ lệ hình:** 100% hình dựng (comic + motion graphics) để đồng nhất. **Không** yêu cầu cảnh tự quay, không trộn cảnh quay thật (DL-027). Cảnh quay thật để dành cho giai đoạn sau hoặc series khác (sẽ có bộ luật riêng).

## B. Script & nội dung
7. **Cấu trúc:** mặc định là mạch kể chuyện của luật 41. Khi không có chuyện thật phù hợp thì dùng dạng giải thích: Hook 0–3s → Vấn đề → Giải thích kèm minh hoạ (3–4 beat) → Bằng chứng / trước-sau → Việc làm ngay. Dạng nào cũng có câu cuối nối lại hook để clip lặp tự nhiên. Thỉnh thoảng xen dạng "3 điều". Script khoảng 150–170 từ tiếng Việt (cho 55–60s, luật 4).
8. **CTA:** câu hỏi kéo comment. Từ tuần 3 nhắc OneUp theo luật 11.
9. **Nhịp đổi hình:** theo nội dung, mỗi cảnh tối đa 8s. Không cắt đều tăm tắp.
10. **Chủ đề:** không giới hạn (bỏ các mục chỉ áp dụng cho luật / thủ tục Trung Quốc). Nguồn: HowToLiveBetter.
11. **Lịch đưa app:** tuần 1–2 không có app · tuần 3–4 có màn hình app ngắn · từ tuần 5 có Omi (nhân vật comic + giọng luật 46). Validator `video-engine` chặn Omi khi `meta.week < 5`. Bản mẫu nội bộ phải ghi `week ≥ 5` và không đăng.
12. **Clip đầu tiên:** trụ 1 "Làm ít, xong nhiều", clip 1 (`content/clips/clip-01-implementation-intention/`).
13. **Ghi nguồn:** HowToLiveBetter (CC BY 4.0, kèm link giấy phép, ghi "đã chuyển thể") chỉ đặt trong caption bài đăng.

## C. Hình ảnh & brand
14. **Brand:**
    - Màu: ink `#111111`, paper `#F7F7F5`. Màu khác chỉ dùng khi mang nghĩa. Xanh lá chỉ cho khoảnh khắc "xong / +1".
    - Không emoji, không neon, không glow, không confetti.
    - Logo 05-pair-plus đặt nhỏ ở góc trên trái suốt clip. Mọi chữ nằm trong safe-zone TikTok.
    - Chi tiết: `brand/brand-index.md`, `brand/brand-tokens.json`.
15. **Font:** toàn bộ chữ trên màn hình (tiếng Anh và tiếng Việt) dùng Be Vietnam Pro (OFL, 400/500/600/700, `brand/fonts/`), font được nhúng sẵn, không dùng font hệ thống. Không trộn 2 font trong một dòng. DM Sans (font của app) chưa dùng cho video cho đến khi Hiệp đổi luật.
16. **Chữ chính trên màn hình:** caption và tiêu đề chỉ tiếng Anh, khớp với lời nói, highlight từ khoá. Ngoại lệ: bubble thoại và hộp dẫn chuyện trong beat comic là lời nhân vật nên viết tiếng Việt (giọng luật 41).
17. **Theme:**
    - Mỗi clip là LIGHT (tích cực) hoặc DARK (mặt trái), xét theo hook. Không quá 2 clip cùng theme liên tiếp. Một clip chỉ một theme.
    - Bảng phân theme: `content/theme-map.md` (clip 1 = LIGHT).
18. **Minh hoạ:** diagram dùng nét vẽ tay (rough.js), icon dùng Phosphor (đơn sắc). Người/nhân vật chỉ dùng rig Hiệp/Omi (luật 43), không dùng Open Peeps cho nhân vật chính.
19. **Motion:** chọn theo từng script, mỗi beat một hiệu ứng chính, lấy từ catalog awesome-ai-motion (637 effect, xem `refs/README.md`) bằng skill `skills/motion-picks-per-script/SKILL.md`. Ghi vào `logs/effects-log.md` để không lặp.
20. **Hậu kỳ:** grain phim nhẹ toàn clip. Bố cục lệch, căn trái. Theo checklist anti-AI-look (`research/production-system-research-vi.md` §6).

## D. Âm thanh & tài sản
21. **Nhạc:** không có nhạc trong file. Hiệp thêm nhạc từ TikTok Commercial Music Library lúc đăng.
22. **SFX:** được dùng tiếng động nhẹ (click, tick, whoosh nhỏ), chỉ lấy file CC0 (Freesound) hoặc Mixkit. Ghi nguồn từng file vào `assets/sfx/SOURCES.md`.
23. **Stock:** series comic không dùng stock video/ảnh người thật. Nếu cần texture/icon thì Pexels/Pixabay/Mixkit/Phosphor, lọc bỏ ảnh AI, không quá 10% thời lượng.
24. **Chỉ dùng công cụ miễn phí, không AI trong hình final:** không video AI, không ảnh AI trong video (luật 44). Giọng AI chỉ cho nhân vật có `voice` trong profile (Hiệp chibi, Omi; luật 46). Ngoại lệ đã được Hiệp chấp nhận: checkpoint F5-TTS tiếng Việt có giấy phép không thương mại (DL-035). **Mọi clip có giọng AI (gần như mọi clip) phải gắn nhãn AI** theo luật 46. Chỉ clip hoàn toàn không có giọng AI mới không bật nhãn.

## E. Công cụ & pipeline
25. **Engine (vai trò cố định):**
    - Beat kể chuyện / comic: **Remotion** trong `video-engine/` (chi tiết luật 45).
    - Beat giải thích / motion graphics: **HyperFrames** (Apache 2.0, cần Node ≥ 22) + GSAP cài local (không CDN), template `templates/hyperframes-base/`. Manim CE cho cảnh biểu đồ.
    - Giọng nhân vật (Hiệp, Omi): F5-TTS local qua `pipeline/scripts/voice-prosody.py` (luật 46, DL-035); VieNeu-TTS chỉ còn để tạo giọng mẫu và làm phương án dự phòng. Clip final: `pipeline/scripts/build-final.py <final/spec.json>` (TTS → plan → render → ghép), kiểm bằng `pipeline/scripts/check-rules.py` và `pipeline/tts/stt_check.py`.
    - Ghép và hậu kỳ: FFmpeg, `pipeline/scripts/join-beats.sh` (xfade giữa beat, chuẩn −14 LUFS). Mỗi engine render file riêng, không trộn trong một lần render.
    - Pipeline: `pipeline/pipeline.md`.
26. **Transcribe:** câu TTS (Hiệp, Omi) lấy thời lượng + envelope từ file TTS, kiểm lại bằng ASR (`pipeline/tts/stt_check.py`, faster-whisper). Nếu Hiệp tự thu giọng thật: whisper.cpp large-v3 (Metal, `-l vi`) lấy timestamp từng từ. Caption tiếng Anh được rải theo từng cụm câu tiếng Việt. Bản dịch tiếng Anh được duyệt cùng script.
27. **Nơi render:** bản nháp render trên box ảo, bản final render trên Mac I-Am-Focused.
28. **Mức tự động:** agent làm toàn bộ theo skill `skills/make-video/SKILL.md`, Hiệp duyệt 2 lần (gate 1: script + beat table + storyboard; gate 2: MP4 final + post.md). Góp ý theo id beat (`b03: …`), agent sửa spec, không làm lại từ đầu.
29. **Thu giọng:** mặc định không cần (giọng AI preset, DL-030). Nếu Hiệp muốn tự thu: thu bằng iPhone, AirDrop vào `footage/inbox/` trên Mac. File âm thanh và render không commit lên git.
30. **Cover:** frame hook kèm chữ to.

## F. Lịch & đăng
31. **Tần suất:** 3 clip/tuần trong 2 tuần đầu, sau đó đánh giá lại (mục tiêu 3–4 clip/tuần).
32. **Đăng:** agent chuẩn bị gói sẵn đăng (mp4, caption, hashtag, credit, cover, và dòng nhãn AI khi có giọng AI) trong `renders/ready/`. **Không có nhắc đăng** (routine nhắc đã xoá, DL-028): Hiệp tự đăng theo lịch của mình, gợi ý thứ Hai, Tư, Sáu trong 2 tuần đầu.

## G. Cải tiến liên tục
33. **Nhật ký quyết định** (`logs/decision-log.md`):
    - Ghi mọi câu hỏi, yêu cầu, góp ý sửa và quyết định của Hiệp, gồm ngày, tóm tắt yêu cầu (giữ nguyên ý), quyết định, luật / file bị ảnh hưởng.
    - Agent đọc lại log trước khi làm mỗi clip mới.
    - Góp ý lặp lại từ 2 lần trở lên thì nâng thành luật trong file này hoặc thành skill trong `skills/`, rồi ghi lại việc nâng đó.
    - Mỗi Chủ nhật có retro tuần trong cùng file: điều tốt, điều cần sửa, chỉ số, luật hay skill đã đổi.
34. **Chuẩn chất lượng:** mọi hình gửi Hiệp (preview, storyboard, frame, video) phải đạt mức "premium". Agent tự xem và sửa ít nhất 2 vòng trước khi gửi (sau góp ý "xấu quá" ngày 12/10/2026).
35. **Storyboard trước khi duyệt script:** mỗi clip có storyboard (1 frame 1080×1920 cho mỗi beat, kèm contact sheet) nằm trong `content/clips/NN-slug/storyboard/`, gửi cùng script để Hiệp duyệt.

36. **Storyboard là tài sản có phiên bản:**
    - Nguồn chuẩn là `content/clips/<clip>/storyboard/spec.json`, render bằng renderer chung `pipeline/storyboard/render.py`.
    - Khi có góp ý: sửa spec (hoặc renderer / style nếu là thay đổi chung), không tạo lại từ đầu. Thêm một dòng vào `revisions` trong spec, render lại, rồi commit với message dẫn mã decision log (`... (DL-0xx)`).
37. **Script phải dùng trend:**
    - Trước khi viết script, đọc `research/trends/ingest.md` và digest mới nhất.
    - Mỗi script có ít nhất 1 cụm từ hoặc tình huống đang phổ biến, gần gũi với khán giả (ghi id trend trong script), nhưng fact vẫn giữ đúng HowToLiveBetter và nguồn trích dẫn.
    - Không sao chép nội dung của người khác.
38. **Trend digest hằng ngày (v2, học hỏi, luật 47):**
    - Chạy theo `skills/trend-digest/SKILL.md`, chỉ dùng nguồn miễn phí, công khai, có trích link.
    - Job chạy tự động ghi vào box `/workspace/oneup-studio-sync/research/trends/`. Agent đồng bộ vào repo bằng `pipeline/scripts/sync-trends.sh` mỗi khi có quyền truy cập Mac (xem AGENTS.md).

39. **Bridge từ trend sang bài học:**
    - Khi lên ý tưởng hook, dùng mọi trend nóng (không chỉ trend ngách) qua bảng Bridges (trend → khoảnh khắc → bài học HowToLiveBetter phần.mục → hook VI → góc → clip).
    - Thay đổi góc giữa các clip: humor, contrarian, empathy, data, story.
    - Qua bộ lọc brand-safety: không chính trị, không bi kịch hay bạo lực, không chế giễu ai, không cổ vũ cờ bạc. Trend về người nổi tiếng hay tiền bạc thì phải có Hiệp duyệt.
    - Không dùng hình, âm thanh của sự kiện. Fact bài học lấy đúng theo sách, số liệu chỉ có ở Trung Quốc thì phải tìm số liệu tương đương ở VN.
40. **Polish script (humanizer + voice):**
    - Sau khi kiểm fact và trước khi gửi duyệt, chạy skill `skills/script-polish` (dùng `skills/humanizer`, MIT, cùng `content/voice-profile.md`).
    - Khoá fact: số liệu, nghiên cứu, trích dẫn giữ nguyên. Không bịa chuyện cá nhân, dùng placeholder `[VÍ DỤ THẬT CỦA HIỆP]`.
    - Lưu thành `script-vX.Y-draft.md` cạnh bản đã duyệt, không ghi đè.

41. **Kể chuyện trước:**
    - Script mặc định theo mạch chuyện cá nhân: tình huống → vật lộn → bước ngoặt → bài học (HowToLiveBetter, fact giữ nguyên) → mời gọi.
    - Chuyện **chỉ được là chuyện thật của Hiệp**, lấy từ `content/story-bank.md`. Chi tiết chưa xác nhận thì ghi `[CẦN HIỆP XÁC NHẬN]` và phải được xác nhận trước khi thu. Không bao giờ bịa chuyện hay kết quả.
    - Giọng theo `content/voice-profile.md` (đã xác nhận): mình/bạn, miền Nam, hài 4/5 tinh tế, chen 1–3 từ tiếng Anh.

42. **Loại beat quyết định kiểu hình:**
    - Beat kể chuyện → **comic** (nhân vật Hiệp/Omi, panel, bubble), nhân vật luôn có chuyển động (idle thở, chớp mắt, squash-stretch, follow-through).
    - Beat dẫn chứng / giải thích / kiến thức → **motion graphics minh hoạ** (số liệu, sơ đồ, icon), không vẽ comic.
    - Omi chỉ xuất hiện từ tuần 5 (luật 11).
43. **Cách điệu mạnh:** chibi đầu to, khối tròn, không góc nhọn, biểu cảm và đạo cụ phóng đại để người xem hiểu ngữ cảnh ngay và thấy vui. Vẫn giữ brand ink/paper 90/8/2 và Be Vietnam Pro. Rig nguồn: `pipeline/characters-v2/`.
44. **AI image local chỉ để phác ý tưởng:** được dùng model tạo ảnh chạy local để sketch/ideation. Không đưa ảnh AI vào video final; hình final phải vẽ lại bằng rig/vector.
45. **Engine video comic (`video-engine/`, vai trò xem luật 25):**
    - Beat kể chuyện render bằng `video-engine/` (Remotion + React + TS): nguồn chuẩn là JSON scene plan (`content/clips/<clip>/comic/plan.json`; bản đầu của clip-01 đang ở `video-engine/examples/clip-01-story.json`) hoặc script text theo `src/scenes/textFormat.ts`, validate trước khi render (`npm run validate`).
    - Nhân vật chỉ vẽ bằng rig SVG trong `video-engine/src/characters/` theo character profile. Không AI ảnh/video trong render. LLM chỉ là tuỳ chọn để lập plan, kết quả phải qua validator.
    - Có giọng: `npm run voice <plan.json>` → `plan.voiced.json` (audio + envelope), hoặc clip final qua `build-final.py`. Miệng **cả Hiệp và Omi** chạy theo envelope audio thật (DL-030).
    - Logo 05-pair-plus (luật 14) và Be Vietnam Pro (luật 15) có sẵn trong composition.
    - Sau mỗi render: `npm run frames` rồi tự soát contact sheet (luật 34) trước khi gửi Hiệp.

46. **Giọng AI nhân vật (F5-TTS, DL-035):**
    - Chỉ nhân vật có `voice` trong profile mới có giọng AI: **Hiệp chibi** = **"F5 · Thái Sơn"** (nam, miền Nam; nghe thử 8 giọng, chọn số 6), **Omi** = **"F5 · Mỹ Duyên"** (nữ, miền Nam; số 6). Hiệp chọn 13/10/2026 (DL-035), thay Đức Trí / Kim Thanh (DL-030). Khai báo ở `video-engine/src/characters/profiles/{hiep,omi}.json` → `voice` (`engine: f5-tts`, `ref`, `refText`). Engine: F5-TTS + checkpoint `hynt/F5-TTS-Vietnamese-ViVoice`, chạy **local** trên CPU (`/workspace/f5-venv`, `pipeline/tts/f5tts_gen.py`), không gọi API. Đổi giọng/giọng mẫu phải ghi DL.
    - ⚠ **Giấy phép:** checkpoint là **CC-BY-NC-SA-4.0 (không thương mại)**. Kênh có quảng bá app OneUp nên dùng trong clip đăng là **rủi ro vi phạm giấy phép**; Hiệp đã xác nhận chấp nhận rủi ro này (13/10/2026, DL-035). Nếu bị khiếu nại hoặc kênh bắt đầu kiếm tiền trực tiếp thì quay về VieNeu (Apache-2.0, `engine: vieneu-tts`, profile còn ghi `previous`) và ghi DL.
    - **Giọng mẫu (reference):** chỉ dùng câu trung tính do preset VieNeu tổng hợp (`pipeline/tts/f5-refs/`, câu "Hôm nay trời Sài Gòn mát mẻ…"). **Cấm clone giọng người thật** (kể cả Hiệp), cấm `ref_audio` lấy từ bản thu người thật.
    - **Prosody:** mọi câu đi qua `voice-prosody.py` theo từng cụm hơi (`phrases`: khoảng nghỉ, nhấn = chậm + lên giọng + to hơn), với F5 (DL-038, L-016): **không bao giờ cắt bên trong một output F5**. Tách câu theo dấu câu (. , ? ! … ; :) thành đơn vị câu/mệnh đề (gộp đơn vị < 4 âm tiết), mỗi đơn vị một lần gọi F5 riêng, 3 seed cố định cho mỗi nhân vật (speed 1.0, NFE 32), chọn take bằng STT trừ lặp/mất âm tiết + khớp F0 với các đơn vị khác; chỉ gọt lặng đầu/cuối (−50 dB, đệm 40 ms, fade 15 ms); nối bằng khoảng nghỉ theo dấu câu (phẩy 180 ms, chấm 350, ?/! 400, … 500) có room tone. Muốn ngắt/nhấn thì sửa dấu câu, không cắt audio. Nhấn nhá thêm bằng markup giọng (từ đệm, ngập ngừng, kéo tiểu từ, câu chen, ngắt ngang; bảng ở `content/voice-profile.md` §3c, DL-039), tối đa 1 từ đệm/câu và max(2, số câu ÷ 4)/clip (check L-017). Thời gian beat/caption theo audio; tự cắt phần **rò giọng mẫu** (chữ của câu mẫu lọt vào đầu take) bằng timestamp từng từ của faster-whisper. Câu không có `phrases` được tính là một cụm. Lời theo voice profile: gọi người xem là "bạn", miền Nam, nha/á/hông, cà khịa nhẹ, 1–3 từ tiếng Anh. Không dùng tag [cười]/[thở dài].
    - Audio cache theo hash (engine + giọng + giọng mẫu + cụm), chuẩn loudness rồi ghép −14 LUFS. Không nhạc (luật 21). Kiểm bằng ffprobe (có track audio) và ASR (đúng chữ) trước khi gửi Hiệp.
    - **Nhãn AI trên TikTok:** TikTok bắt buộc gắn nhãn cho nội dung AI có hình, **âm thanh** hoặc video trông/nghe như thật (Community Guidelines, mục Edited Media & AIGC). Giọng nhân vật là giọng tổng hợp nghe như người thật → **mọi clip có giọng AI** (Hiệp và/hoặc Omi): **bật nút "AI-generated content"** khi đăng, và ghi trong caption: "Giọng của Hiệp (nhân vật) và Omi trong video là giọng AI tổng hợp (F5-TTS)." (chỉ nêu nhân vật thật sự nói). Clip không có giọng AI thì không bật (gắn nhãn sai cho nội dung không AI cũng vi phạm điều khoản). Nguồn: support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content (kiểm 13/10/2026).
    - Mọi câu phải qua STT (`pipeline/tts/stt_check.py`); câu nghe sai thì sửa cách viết (`say`, vd. TOEIC → "tô ích") hoặc tăng `take` trong spec để đọc lại.
    - Nếu TTS lỗi: không giả giọng; dùng placeholder có ghi rõ "[PLACEHOLDER – chưa có giọng]" và báo Hiệp.

47. **Trend job biết học (DL-029):**
    - Mỗi ngày: chấm `novelty`/`saturation`, khử trùng với digest cũ và bridge đã dùng (`pipeline/scripts/trend-learn.py score`), ghi tín hiệu miễn phí (Google Trends traffic, view YouTube qua yt-dlp, X public), mổ xẻ dạng hook đang chạy vào `research/trends/patterns.md` (chỉ lưu khuôn trừu tượng, không chép).
    - Mỗi bridge có dòng **khác biệt**: "mọi người đang nói" vs "góc của mình" (chuyện thật của Hiệp, cú cà khịa của Omi, fact sách mà số đông bỏ qua, hoặc góc ngược). Góc trùng số đông thì loại.
    - Top 1–2 ý tưởng có **plan stub** JSON theo schema `video-engine` (`trend-learn.py stub`) và phải qua `npm run validate`. Stub luôn `stub-needs-approval`, chuyện chưa xác nhận để placeholder (luật 41).
    - Chủ nhật: tổng hợp tuần `research/trends/weekly/YYYY-Www.md` + cập nhật uses/wins của pattern theo số liệu Hiệp báo (không bịa số). Đề xuất đổi luật thì hỏi Hiệp trước.
    - Vẫn giữ: nguồn miễn phí, lọc brand-safety (luật 39), không đăng/gửi gì.

48. **Một quy trình duy nhất cho mọi clip (DL-031):**
    - Mọi clip làm theo `skills/make-video/SKILL.md`: intake → đọc nguồn chuẩn → script → humanizer → `check-rules` → **gate 1** (script.md + beat table + storyboard) → render → `check-rules --final` + soát frame + STT → **gate 2** (MP4 + post.md) → ghi DL.
    - `pipeline/scripts/check-rules.py` là cổng tự động: lỗi (✖) thì không gửi Hiệp duyệt và không render final.
    - Hiệp yêu cầu bằng "Làm clip tiếp theo" / "Làm clip về <chủ đề/trend>"; góp ý theo id beat ("b03: đổi câu …"). Agent sửa `final/spec.json` (hoặc template), tăng `revisions`, build lại; không viết lại từ đầu.
49. **Cổng bài học, tự học từ lỗi (lessons gate):**
    - `logs/lessons.md` ghi mọi lỗi đã gặp (id `L-NNN`, ngày, triệu chứng theo lời Hiệp, nguyên nhân gốc, cách sửa, cách phát hiện, tên check tự động, trạng thái). Đọc file này **trước mỗi clip**.
    - Mỗi lần Hiệp góp ý/chê ("vấp", "xấu", "đọc sai"…): **trước khi sửa** thêm hoặc cập nhật lesson, và nếu đo được thì thêm check `L-NNN` vào `pipeline/scripts/check-rules.py`. Check ✖ chặn gửi duyệt (luật 48) như mọi luật khác. Lỗi chưa đo được thì ghi `manual` kèm cách soát tay.
    - Không xoá lesson; khi đổi cách sửa thì cập nhật dòng và ghi DL.

50. **Mỗi lần chuyển cảnh đều có SFX, luôn có lớp nền ambience (DL-042):**
    - Chuyển phần (xfade A→E→B) dùng `whoosh-soft`. Chuyển scene/section bên trong một phần dùng `swish`. SFX bắt đầu sớm hơn điểm cắt khoảng 0.12s để chồng qua vết cắt, âm lượng nhỏ, nằm dưới giọng.
    - Lớp nền `ambience` (brown noise rất nhỏ) chạy suốt clip, để khoảng lặng giữa các cảnh không bị "chết". Vẫn không có nhạc (luật 21).
    - Chỉ dùng SFX tự tổng hợp, CC0 hoặc Mixkit, có ghi trong `assets/sfx/SOURCES.md` (luật 22).
    - Kiểm tra bằng `check-rules` (rule-50): mọi transition trong `timing.json` phải có SFX nằm trong khoảng ±0.3s, và phải có `ambience`.

51. **Motion phải gắn với nội dung; mỗi điểm animation trọng tâm có SFX nhấn (DL-043):**
    - Mỗi beat/section có ít nhất một ẩn dụ hình ảnh gắn với đúng chữ đang nói, ví dụ: câu nếu–thì ráp như mảnh ghép, pin đầy/cạn, laptop gập lại, lịch lật trang, số đếm lên, con dấu ✕. Không dùng chung một hiệu ứng cho mọi section (tránh lặp; chọn theo skill motion-picks-per-script). Chỉ animate transform/opacity, chữ nằm trong safe area.
    - Điểm nhấn được đánh dấu trong spec bằng `hits: [{id, f, sfx}]` (section) hoặc `sfx` (scene). Template dùng `H(id, hit)` nên hình và tiếng rơi đúng cùng một thời điểm.
    - SFX nhấn gồm pop, ding, tick, click, snap, pen, stamp, rise. Tự tổng hợp (luật 22), nhỏ hơn giọng khoảng 12–16 dB, chỉ đặt ở điểm nhấn chứ không phải mọi chuyển động nhỏ, tối đa 3 cái mỗi section.
    - check-rules (rule-51): mỗi section explainer có ≥ 1 hit gắn SFX; SFX phải có trong SOURCES.md; không có 2 SFX nhấn cách nhau dưới 0.25s.

## Changelog
- **v3.8, 14/10/2026:** luật 51, motion gắn với nội dung + SFX nhấn ở điểm animation trọng tâm (DL-043).
- **v3.7, 14/10/2026:** luật 50, chuyển cảnh nào cũng có SFX và luôn có lớp nền ambience (DL-042).
- **v3.6, 14/10/2026:** markup giọng tự nhiên (từ đệm, kho từ đệm theo nhân vật, ngập ngừng, kéo tiểu từ, pause từng dấu, câu chen), bảng tiểu từ đo bằng STT + F0, giới hạn tần suất từ đệm (luật 46; DL-039, L-017).
- **v3.5, 13/10/2026:** F5 sinh theo đơn vị câu/mệnh đề tách bằng dấu câu, cấm cắt bên trong output F5 (luật 46; DL-038, L-016).
- **v3.4, 13/10/2026:** luật 49 (cổng bài học `logs/lessons.md` + check `L-NNN`); F5 v3 chống "vấp": 1 take tự nhiên mỗi câu, chỉ cắt ở lặng thật (luật 46; DL-036, DL-037).
- **v3.3, 13/10/2026:** giọng nhân vật chuyển sang F5-TTS (Hiệp "F5 · Thái Sơn", Omi "F5 · Mỹ Duyên", giọng mẫu tổng hợp từ VieNeu); Hiệp chấp nhận rủi ro giấy phép CC-BY-NC-SA của checkpoint; dòng nhãn AI ghi "(F5-TTS)" (luật 2, 24, 25, 46; DL-035).
- **v3.2, 13/10/2026:** giọng AI preset cho cả Hiệp chibi ("Đức Trí") và Omi ("Kim Thanh"); nhãn AI cho mọi clip có giọng AI (luật 2, 24, 26, 29, 32, 45, 46; DL-030). Luật 48: skill `make-video` + `check-rules.py` là quy trình bắt buộc (luật 28; DL-031).
- **v3.1, 13/10/2026:** series chỉ comic + motion, bỏ yêu cầu tự quay (luật 3, 5, 6, 23, 29; DL-027). Bỏ nhắc đăng (luật 32; DL-028). Luật 47 trend job học hỏi, luật 38 trỏ sang skill v2 (DL-029).
- **v3.0, 13/10/2026:** audit toàn bộ 45 luật (DL-025, DL-026, `logs/rules-audit-2026-10-13.md`). Luật 46 mới (giọng AI Omi, VieNeu-TTS, nhãn AI TikTok). Sửa luật 2, 24 (không còn "cấm mọi giọng AI"), 25 + 45 (vai trò Remotion/HyperFrames/ffmpeg, bỏ trùng), 5, 6, 7, 11, 16, 18, 26, 32 (lịch nhắc khớp 3 clip/tuần), 42 (bỏ trùng luật 11). Sửa lỗi dính dòng changelog.
- **v2.6, 13/10/2026:** luật 45 (engine video comic `video-engine/`: Remotion cho beat kể chuyện, HyperFrames cho beat giải thích, plan JSON có validate) (DL-024).
- **v2.5, 13/10/2026:** luật 42 (comic cho beat kể chuyện, motion graphics cho beat giải thích), luật 43 (cách điệu mạnh, chibi), luật 44 (AI image local chỉ để phác). Giọng AI cho Omi: chưa đổi, chờ quyết (research/omi-voice-tts-research-vi.md).
- **v2.4, 12/10/2026:** luật 41 (kể chuyện trước, chỉ chuyện thật, voice profile đã xác nhận).
- **v2.3, 12/10/2026:** luật 39 (bridge trend → bài học, lọc brand-safety), luật 40 (polish script bằng humanizer + voice profile).
- **v2.2, 12/10/2026:** thêm luật 36 (storyboard theo spec + renderer chung, sửa thay vì tạo lại), luật 37 (script phải đọc trend ingest, có ≥1 cụm từ đang phổ biến), luật 38 (trend digest hằng ngày + sync). Thêm front-matter và id ổn định cho tài liệu.
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
