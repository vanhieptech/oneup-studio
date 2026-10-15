# Hệ thống sản xuất video 60s cho @hi.oneup: research & đề xuất
*Ngày 12/10/2026 (giờ VN). Nguồn: web, GitHub, tài liệu chính thức. Mục nào ghi [đã xác minh] là mình đã đọc nguồn hoặc chạy thử hôm nay. Mục ghi [cần kiểm lại] là mình viết theo hiểu biết sẵn có, chưa mở lại nguồn.*
*Tài liệu này không đổi bộ luật `/workspace/hi-oneup-video-rules.md`. Mọi lựa chọn đều nằm ở mục 8, chờ Hiệp quyết.*

---
## 1. Engine render (so sánh cho short giải thích 60s)

| Engine | Cách hoạt động | License | Bảo trì | Hợp với kênh? |
|---|---|---|---|---|
| **HyperFrames** (`heygen-com/hyperframes`) [đã xác minh, chạy thử] | Viết video bằng HTML/CSS/JS, đánh dấu bằng `data-start/data-duration`, rồi Chrome headless tua từng frame (beginFrame) và FFmpeg encode. Dùng được GSAP, Lottie, anime.js, WAAPI, Three.js. Có sẵn CLI `transcribe` (Whisper), `capture`, `lint`, `snapshot`, `beats`, `normalize-audio`, cùng agent skills (`init` tự cài skill) | **Apache 2.0**, không phí render | Rất tích cực (CLI 0.8.150 hôm nay) | **Rất hợp**: không cần build, agent viết HTML dễ, xuất được alpha (WebM, ProRes 4444 MOV) |
| **Remotion** [đã xác minh license] | Viết video bằng React, mỗi frame là một hàm của `useCurrentFrame()`, render bằng Chrome và FFmpeg | Source-available. **Miễn phí cho cá nhân, kể cả dùng thương mại, và cho công ty tối đa 3 người.** Từ 4 người trở lên phải mua license ($25/seat/tháng hoặc $0.01/render, tối thiểu $100/tháng). Nguồn: https://www.remotion.dev/docs/license/faq | Rất tích cực | Hợp. Hệ sinh thái lớn nhất (`@remotion/captions`, Studio, agent skills `npx skills add remotion-dev/skills`). Rủi ro: nếu team OneUp lên ≥4 người thì phải trả phí |
| Motion Canvas (motion-canvas.io) [cần kiểm lại] | Code TS dạng generator, có editor | MIT | Chậm lại | Mạnh về vẽ diagram, nhưng ít hợp với quy trình tự động |
| Revideo (redotvideo/revideo) [cần kiểm lại] | Fork của Motion Canvas, render headless qua API | MIT | Ít cập nhật gần đây | Phương án dự phòng |
| editly (mifi/editly) [cần kiểm lại] | Khai báo JSON5, chạy trên FFmpeg | MIT | Bảo trì thấp | Chỉ dùng để ghép b-roll đơn giản |
| FFmpeg thuần | filter_complex, drawtext, xfade | LGPL/GPL | Ổn định | Hợp cho bước cuối: ghép, chuẩn hoá âm, grain, encode |
| Manim CE (manim.community) [cần kiểm lại] | Python, animation toán học kiểu 3Blue1Brown | MIT | Tích cực | Hợp cho biểu đồ, đồ thị (ví dụ "ước lượng lệch gấp 2"). Render ra clip có alpha rồi chèn vào |
| Lottie: lottie-web / dotLottie (`@lottiefiles/dotlottie-web`) | Phát JSON animation từ After Effects/Figma | MIT | dotLottie tích cực, lottie-web ít cập nhật | Hợp cho icon động. HyperFrames có adapter sẵn |
| Rive | State machine, runtime miễn phí | Runtime MIT, editor có gói trả phí | Tích cực | Có thể dùng cho Omi động sau này. Không bắt buộc |
| **GSAP** [đã xác minh] | Timeline animation | "Standard No Charge" (Webflow, 30/4/2025): **miễn phí cả thương mại, gồm mọi plugin** (SplitText, MorphSVG, DrawSVG…). Cấm duy nhất: làm tool no-code cạnh tranh Webflow. https://gsap.com/community/standard-license/ | Tích cực | **Hợp nhất** cho chữ, SVG vẽ nét, morph. Là mặc định của HyperFrames |
| anime.js v4 | Animation JS nhẹ | MIT | Tích cực | Phương án thay GSAP |
| Framer Motion (nay là "Motion") | Animation cho React | MIT | Tích cực | Chạy theo thời gian thực, không theo frame, nên **không dùng để render** (trong Remotion phải dùng `interpolate/spring`) |

**Kết luận:** HyperFrames + GSAP làm engine chính. Manim chỉ dùng cho cảnh biểu đồ, FFmpeg cho ghép và hậu kỳ. Remotion là phương án thay thế nếu muốn hệ sinh thái React lớn hơn.

## 2. Kỹ thuật chụp web thành frame
- **Tua frame tất định:** đừng quay màn hình theo thời gian thực. Phải dừng thời gian lại, rồi với mỗi frame: seek timeline đến t = i/fps, chụp ảnh. HyperFrames gọi `window.__timelines[id].seek(t)`, Remotion đặt `frame` rồi chờ `delayRender` trả về.
- **Virtual time** (timesnap/timecut, [cần kiểm lại], ít bảo trì): ghi đè `Date`, `requestAnimationFrame`, `setTimeout`, `performance.now`. Dùng được với trang có sẵn mà không seek được, nhưng dễ vỡ.
- **CDP `Page.startScreencast`:** chạy theo thời gian thực, rớt frame, **không dùng để render**. **`HeadlessExperimental.beginFrame`:** chủ động điều khiển từng frame, tất định. HyperFrames dùng cách này ("beginframe capture" trong log chạy thử).
- **WebCodecs:** encode ngay trong trình duyệt (`VideoEncoder`), nhanh nhưng phụ thuộc codec của trình duyệt. Remotion có hướng render phía client. Chưa cần dùng.
- **Những lỗi hay gặp:**
  - Font: tự host file TTF và chờ `document.fonts.ready`, đừng dùng font hệ thống. Chạy thử đã chứng minh Be Vietnam Pro tự host lên đủ dấu.
  - Tính tất định: không dùng `Math.random()` không seed, CSS transition chạy theo thời gian thực hay video không seek được.
  - GPU: render headless dùng software GL nên shader chậm. Trên Mac thì bật GPU được.
  - Màu: ép sRGB / bt709 (`-colorspace bt709 -color_primaries bt709 -color_trc bt709`) để #111111 không bị lệch khi lên TikTok.
  - fps: TikTok chấp nhận 30 hoặc 60fps. 30fps nhẹ và trông "người quay" hơn.
  - Alpha cho overlay: xuất WebM VP9 alpha hoặc ProRes 4444 (`prores_ks -profile:v 4444 -pix_fmt yuva444p10le`), nền html/body phải để trong suốt.
  - Encode giao bài: H.264 High, yuv420p, CRF khoảng 18, AAC 48kHz.

## 3. Skill pack, agent skill, caption
- **HyperFrames skills** [đã xác minh]: `npx hyperframes skills`, `/hyperframes-core`. Lệnh `init` tự cài.
- **Remotion skills** [đã xác minh]: `npx skills add remotion-dev/skills` (`/remotion-best-practices`).
- **awesome-ai-motion** (MIT, đã có ở `/workspace/refs/awesome-ai-motion`) kèm skill `motion-picks-per-script` của mình: tiếp tục dùng để chọn motion theo từng beat.
- **GSAP llms-full.txt** (https://gsap.com/llms-full.txt): bộ hướng dẫn chính thức để agent viết GSAP đúng.
- **Caption và căn thời gian:**
  - **whisper.cpp** (MIT) chạy Metal trên Mac, model `large-v3` hoặc `large-v3-turbo`, nhận tiếng Việt tốt (`-l vi`), có timestamp từng từ (`-ml 1` / `--output-json-full`).
  - **WhisperX** (BSD-2): căn thời gian từng từ bằng wav2vec2. Có model căn tiếng Việt (`nguyenvulebinh/wav2vec2-base-vietnamese-250h`) [cần kiểm lại].
  - Lệnh `hyperframes transcribe` dùng Whisper.
  - Bất kể engine nào, cũng phải đi qua JSON caption, ví dụ dạng `Caption[]` của `@remotion/captions`.
- **Tiếng Việt thành caption tiếng Anh từng từ:**
  1. Lấy timestamp từng từ tiếng Việt.
  2. Chia thành cụm ý (phrase).
  3. Dịch mỗi cụm sang tiếng Anh (Hiệp duyệt bản dịch cùng lúc với script).
  4. Rải các từ tiếng Anh đều trong khoảng thời gian của cụm, có trọng số theo độ dài từ.
  5. Highlight từng từ theo thời gian đã rải.

  Đây là cách khả thi nhất, vì hai ngôn ngữ không khớp từng từ một.

## 4. Stock & tài sản (đều miễn phí, cần kiểm lại điều khoản trước khi đăng)
| Nguồn | License | API | Ghi chú |
|---|---|---|---|
| Pexels | Pexels License: dùng thương mại, không bắt buộc ghi nguồn, không bán lại nguyên bản | Có, cần key miễn phí | Nguồn chính |
| Pixabay | Pixabay Content License | Có, cần key | Lọc bỏ ảnh AI |
| Coverr | Free license | Có API | Ít clip |
| Mixkit (Envato) | Mixkit License (video/SFX dùng thương mại) | Không có API | Tải tay |
| Freesound | Tuỳ từng file: CC0 / CC-BY / CC-BY-NC | Có API | **Chỉ lấy CC0** để khỏi phải ghi nguồn. Tránh NC |
| Phosphor Icons | MIT | npm | Nét mảnh, đơn sắc, hợp brand |
| Lucide | ISC | npm | Phương án thay thế |
| unDraw | unDraw license (miễn phí, không ghi nguồn) | Không | Chỉ dùng nếu đổi màu nhấn về đơn sắc ink |
| Open Peeps | CC0 | Không | Nét vẽ tay đen trắng, **rất hợp** để chống "nhìn như AI" |
Đối chiếu brand: không emoji, đơn sắc, xanh lá chỉ cho khoảnh khắc "+1/xong". Phosphor, Open Peeps và đường SVG vẽ tay là hợp nhất.

## 5. Viết script cho clip giải thích 60s
Cấu trúc giữ người xem (khoảng 150–170 từ tiếng Việt cho 60s):
- **0–3s Hook:** câu ngược trực giác hoặc nỗi đau cụ thể, có hình ngay từ frame 0, không intro.
- **3–10s Vấn đề:** "vì sao bạn thất bại".
- **10–40s Giải thích + minh hoạ:** 3–4 beat, mỗi beat 5–8s, và ở mỗi beat đổi một thứ (góc máy, chèn diagram, zoom, đổi nền).
- **40–52s Bằng chứng / trước-sau:** con số, nghiên cứu (ví dụ "94 nghiên cứu").
- **52–60s Payoff + việc làm ngay hôm nay**, và câu cuối nối lại hook để video lặp tự nhiên. CTA nhẹ, không xin follow lộ liễu.

Các loại beat minh hoạ: sơ đồ nếu→thì (nét vẽ dần), so sánh trước/sau chia đôi màn, biểu đồ số liệu đếm lên, timeline, checklist tick dần, phép ẩn dụ bằng vật thật trên bàn (POV tay), quay màn hình app (từ tuần 3).

Tham khảo phong cách [cần kiểm lại]: Ali Abdaal (bằng chứng + framework đặt tên), Thomas Frank (giải thích kèm quay màn hình), Matt D'Avella (tối giản, nhịp chậm), Andrew Huberman clips (khoa học → protocol). TikTok giáo dục Việt Nam (#LearnOnTikTok, #hoccungtiktok): kiểu talking head nói nhanh kèm chữ to, "3 điều", "sai lầm khi…". Kênh có thể khác biệt nhờ minh hoạ tối giản đen trắng.

## 6. Checklist chống "nhìn như AI"
**Dấu hiệu hay gặp:**
- Giọng TTS đều đều.
- Stock quá bóng bẩy, người cười nhìn camera.
- Chữ động kiểu template bật lên đều đặn.
- Gradient phát sáng, neon, bố cục đối xứng hoàn hảo.
- Nhịp cắt đều tăm tắp.
- Script mở bằng "Bạn có biết…", liệt kê 3 ý chung chung.
- Ảnh AI (tay méo, chữ lỗi).

**Cách khắc phục:**
1. Giọng thật, giữ hơi thở và chỗ ngập ngừng tự nhiên, chỉ cắt khoảng lặng trên 0,6s.
2. Tối thiểu 50% hình tự quay (bàn, tay, điện thoại, cầm tay hơi rung). Stock tối đa 30%, chọn cảnh không nhìn camera, lọc ảnh AI.
3. Thêm yếu tố vẽ tay: đường SVG hơi run (rough.js, MIT), gạch chân vẽ tay, Open Peeps.
4. Nhịp thay đổi: có cảnh 1,5s, có cảnh 6s. Easing khác nhau, không dùng một kiểu fade cho mọi thứ.
5. Thêm grain phim nhẹ (`noise=alls=6:allf=t`) và vignette rất nhẹ. Không dùng glow.
6. Bố cục lệch, căn trái, khoảng trắng nhiều.
7. Quay màn hình thật của OneUp, có con trỏ hay ngón tay thật.
8. Tự sửa lỗi nhỏ ngay trên hình (gạch chữ rồi viết lại).
9. Câu chữ như người thật: ví dụ của chính Hiệp, ngôi thứ nhất, số liệu cụ thể.
10. Lúc QA, mỗi clip qua một lần "soi AI-look" theo danh sách này.

## 7. Pipeline đề xuất end-to-end
| Bước | Công cụ | Tự động / tay | Thời gian |
|---|---|---|---|
| 1. Ý tưởng | theme-map + HowToLiveBetter + idea bank | Agent | 2' |
| 2. Script VI + bản dịch EN + beat sheet nháp | Agent, theo template mục 5 | Agent | 5' |
| 3. Duyệt | Hiệp | Tay | 5–10' |
| 4. Thu giọng (iPhone) + quay b-roll theo shot list | Hiệp | Tay | 20–30' |
| 5. Chuyển file sang Mac | AirDrop vào `inbox/` | Tay | 1' |
| 6. Làm sạch âm: cắt khoảng lặng, loudnorm −14 LUFS | FFmpeg (`hyperframes normalize-audio`) | Tự động | 1' |
| 7. Transcribe + timestamp từng từ | whisper.cpp large-v3 (Metal) / WhisperX | Tự động | 1–2' |
| 8. Beat sheet có thời gian thật | Agent khớp script với timestamp | Tự động | 2' |
| 9. Chọn motion | skill motion-picks-per-script + effects-log | Tự động | 2' |
| 10. Lấy tài sản | Pexels/Pixabay API, Phosphor, SFX CC0 | Tự động | 2' |
| 11. Dựng composition | HyperFrames (HTML + GSAP), Manim cho biểu đồ | Agent | 10' |
| 12. Render | `hyperframes render` 1080×1920 30fps | Tự động | 1–3' |
| 13. QA | `hyperframes lint/snapshot`, contact sheet, kiểm safe-zone, dấu tiếng Việt, LUFS, checklist anti-AI | Tự động + Hiệp duyệt | 5' |
| 14. Đóng gói | caption post + hashtag + credit CC BY 4.0, ảnh cover, file `ready/` | Agent | 3' |
| 15. Đăng + chèn nhạc TikTok | Hiệp | Tay | 5' |
**Tổng thời gian:** khoảng 30–45' công tay của Hiệp mỗi clip (phần lớn là thu âm và quay), máy và agent chạy khoảng 20–30'.

**Cấu trúc thư mục đề xuất:**
```
hi-oneup/
  rules/ brand/ refs/ skills/
  templates/            # các cảnh HTML tái dùng: hook, diagram, before-after, checklist, data-count
  clips/NN-slug/
    script.md  beats.json  captions.vi.json  captions.en.json
    raw/ (voice.m4a, broll/*.mov)  assets/  comp/index.html
    out/ (draft.mp4, final.mp4, cover.png, contact-sheet.png)
    post.md   qa.md
  ready/      # file chờ đăng
```
**Stack thay thế:** Remotion + `@remotion/captions` + remotion skills thay HyperFrames (miễn phí cho cá nhân / ≤3 người).

## 8. Các quyết định Hiệp cần chọn (mình chưa quyết)
1. **Engine chính:** A) HyperFrames · B) Remotion · C) Kết hợp HyperFrames và Manim. *Đề xuất C: HyperFrames là lõi (Apache 2.0, không ràng buộc quy mô team, đã chạy thử được), Manim chỉ cho biểu đồ.*
2. **Độ dài chính xác:** A) 55–60s · B) 60–75s · C) 45–60s linh hoạt theo nội dung. *Đề xuất A, giữ tỉ lệ xem hết cao.*
3. **fps:** A) 30 · B) 60. *Đề xuất A: tự nhiên hơn, render nhanh hơn.*
4. **Tỉ lệ hình:** A) tự quay ≥50%, stock ≤30%, minh hoạ phần còn lại · B) chủ yếu minh hoạ, ít người · C) chủ yếu talking head. *Đề xuất A, chống AI-look tốt nhất.*
5. **Phong cách minh hoạ:** A) nét vẽ tay hơi run (rough.js / Open Peeps) · B) hình học sạch (Phosphor) · C) trộn cả hai. *Đề xuất C: diagram dùng nét tay, icon dùng Phosphor.*
6. **Chữ chính trên màn hình (ngoài caption EN):** A) chỉ tiếng Anh · B) tiếng Việt (Be Vietnam Pro) · C) song ngữ cho từ khoá. *Đề xuất A cho đồng bộ với caption EN, tránh rối.*
7. **Cách khớp caption EN:** A) rải theo cụm, Hiệp duyệt bản dịch cùng script · B) chỉ phụ đề cả câu, không highlight từng từ · C) caption tiếng Việt từng từ kèm câu dịch EN nhỏ. *Đề xuất A, đúng luật hiện tại.*
8. **Công cụ transcribe:** A) whisper.cpp (Metal) · B) WhisperX · C) `hyperframes transcribe`. *Đề xuất A, cần test độ chính xác tiếng Việt với giọng thật.*
9. **Grain / hậu kỳ:** A) grain nhẹ toàn clip · B) chỉ trên cảnh minh hoạ · C) không dùng. *Đề xuất A.*
10. **Nhịp đổi hình:** A) đổi hình mỗi 3–5s · B) mỗi 5–8s · C) theo nội dung, tối đa 8s. *Đề xuất C.*
11. **SFX:** A) không dùng · B) tiếng động nhẹ (click, tick, whoosh nhỏ) chỉ lấy CC0/Mixkit · C) nhiều SFX. *Đề xuất B. Lưu ý luật "không nhạc trong file" chỉ áp dụng cho nhạc, còn SFX thì Hiệp quyết.*
12. **Nguồn stock được phép:** A) chỉ Pexels · B) Pexels + Pixabay + Mixkit · C) cả Coverr. *Đề xuất B, có lọc ảnh AI.*
13. **Cấu trúc script mặc định:** A) Hook → Vấn đề → Giải thích → Bằng chứng → Việc làm ngay → nối lại hook · B) dạng "3 điều" · C) kể chuyện cá nhân trước rồi mới vào kiến thức. *Đề xuất A, xen B và C để tránh lặp.*
14. **CTA:** A) không CTA, chỉ lặp vòng · B) câu hỏi để kéo comment · C) nhắc OneUp (từ tuần 3). *Đề xuất B, và C khi đến lịch đưa app.*
15. **Mức tự động:** A) agent làm hết, Hiệp chỉ duyệt script + duyệt final · B) thêm một lần duyệt beat sheet / motion · C) Hiệp tự dựng một phần. *Đề xuất A, bước duyệt beat sheet để tuỳ chọn.*
16. **Nơi render:** A) Mac (như luật 12) · B) box ảo render nháp, Mac render final · C) chỉ box. *Đề xuất B: box nhanh cho nháp, Mac cho bản cuối. Cần Hiệp đồng ý vì khác luật 12.*
17. **Cách giao b-roll:** A) AirDrop vào thư mục `inbox` trên Mac · B) iCloud Drive / Google Drive · C) gửi qua chat. *Đề xuất A.*
18. **Shot list:** A) agent gửi danh sách cảnh cần quay kèm script · B) Hiệp quay tự do, agent chọn sau. *Đề xuất A.*
19. **Ảnh cover:** A) frame hook kèm chữ to · B) template cố định có logo · C) để TikTok tự chọn. *Đề xuất A.*
20. **Khung giờ đăng / số clip mỗi tuần với độ dài 60s:** A) giữ 3–4 clip/tuần · B) giảm còn 3 clip vì mỗi clip tốn công hơn. *Đề xuất B trong 2 tuần đầu, rồi đánh giá lại.*

## 9. Kết quả chạy thử trên box [đã xác minh]
- `npx hyperframes init hf-test --resolution=portrait` (CLI 0.8.150, Node 22) → `/workspace/hi-oneup/spike/hf-test/`
- Font Be Vietnam Pro Bold tự host, nền #111111, chữ #F7F7F5, GSAP fade-in. Lệnh `hyperframes render` chạy 3,1s → `/workspace/hi-oneup/spike/hf-test-3s.mp4` (1080×1920, 30fps, 3,0s, 104 KB). Frame mẫu: `/workspace/hi-oneup/spike/hf-frame.png`. Dấu tiếng Việt ("Nếu… thì… Kế hoạch ưu tiên") hiển thị đúng, không lẫn font khác.
- Ghi chú: template mặc định tải GSAP từ CDN, bản thật nên cài GSAP local để render offline. CLI có telemetry ẩn danh, tắt được bằng `hyperframes telemetry`.
