---
title: "Nghiên cứu short-video-factory đối chiếu oneup-studio"
date: 2026-10-19
status: research-only
source: "https://github.com/YILS-LIN/short-video-factory + /workspace/oneup-studio"
tags: [short-factory, oneup-studio, research]
type: research
id: research.short-factory
---

# Nghiên cứu short-video-factory (YILS-LIN) đối chiếu pipeline oneup-studio

> Phạm vi: chỉ đọc web (README/LICENSE/package.json/CHANGELOG/cây file GitHub API) và đọc file trên box ngày 19/10/2026 (Asia/Saigon). **Không cài, không chạy code của short-video-factory, không render, không sửa pipeline oneup-studio.** Mọi con số về hiệu năng của repo kia đều là lời giới thiệu của chính repo, chưa kiểm chứng bằng chạy thử — không dùng làm bằng chứng.

## 1. short-video-factory là gì

- Định vị: app desktop Electron đa nền tảng, "một cú bấm" sinh video marketing/nội dung chung: LLM viết văn bản → EdgeTTS đọc → tự trộn đoạn video trong thư mục素材 → phụ đề/hiệu ứng → FFmpeg xuất file, kèm chế độ chạy hàng loạt theo preset.
- Cấu trúc (cây `main` trên GitHub): `src/` (Vue 3: `lib/llm/*`, `effect-engine/` render phụ đề bằng Pixi, `views/Home` gồm TextGenerate/TtsControl/VideoRender/VideoManage), `electron/` (`lib/edge-tts.ts`, `ffmpeg/index.ts`, `effect-engine/subtitle-render-service.ts`, `sqlite/`, `tts/`), `tests/` (vitest: llm/tts/render/metadata), `locales/` zh-CN + en.
- Phụ thuộc chính (`package.json` v1.3.0): Electron 22, Vue 3 + Vite 7, Node ≥22.17, pnpm ≥10.12.4, `ffmpeg-static`, `better-sqlite3`, `pixi.js` 8.17, `subtitle` 4.2.2-alpha, AI SDK (`@ai-sdk/openai`, `@ai-sdk/anthropic`, `@ai-sdk/openai-compatible`). **Không thấy phụ thuộc GPU/CUDA trong package.json**; render dựa vào FFmpeg tĩnh + CPU (suy ra từ stack, chưa chạy thử).
- API bên ngoài: (a) LLM qua API tương thích OpenAI/Anthropic — cần API key, dữ liệu kịch bản rời máy; (b) EdgeTTS — dịch vụ giọng của Microsoft qua thư viện edge-tts, không phải API chính thức có cam kết ổn định: CHANGELOG v1.3.0 ghi phải "sửa lỗi EdgeTTS 403 do thay đổi xác thực", v1.2.0 cũng ghi sửa lỗi tổng hợp EdgeTTS.
- Tính năng theo README/CHANGELOG (bằng chứng văn bản, chưa chạy): viết văn bản đa giao thức + kiểm soát đa dạng văn bản (v1.3.0), EdgeTTS (TTS duy nhất; roadmap "thêm API giọng nói" còn bỏ ngỏ `[ ]`), trộn đoạn ngẫu nhiên từ thư mục素材, cân bằng âm lượng BGM/giọng, hàng loạt tự động, **engine render phụ đề mới + xuất SRT kèm video (v1.3.0)**, xuất chẩn đoán lỗi kèm phiên bản app (v1.3.0), dò metadata素材 có cache cho thư mục lớn (v1.2.2).
- Prompt mẫu (`src/lib/llm/prompts.ts`): yêu cầu "không bịa thông số sản phẩm/giá/dữ liệu", chỉ xuất văn bản đọc, không Markdown/emoji/chỉ dẫn cảnh. Tốt ở mức nguyên tắc, nhưng **không có** fact-lock theo nguồn, không cấu trúc hook–bằng chứng–CTA của OneUp, không cột hình/caption EN, không cổng duyệt người.

## 2. oneup-studio trên box — CÓ tìm thấy

- Có tại `/workspace/oneup-studio` (bản clone trên box; bản Mac ở `/Users/macbook/me/projects/oneup-studio` theo AGENTS.md). Đã đọc: `README.md`, `AGENTS.md`, `logs/lessons.md` (L-001…L-058, cập nhật 19/10/2026), `pipeline/scripts/check-rules.py` (file nằm trong `pipeline/scripts/`, không ở gốc repo), `pipeline/pipeline.md`, `rules/video-rules.md`, `content/voice-profile.md`, và `/home/box/agent-data/workflows/make-video/SKILL.md` (25 KB, workflow bắt buộc rule-48).
- Cấu trúc chính: `spec.json` là nguồn sự thật duy nhất của clip; video-engine Remotion (React/TS, nhân vật chibi Hiệp/Omi, layoutCheck chống va chạm, Cover template) + HyperFrames cho beat giải thích; `pipeline/scripts/build-final.py` (voice → plans → render → ghép), `check-rules.py`/`check-assets.py` làm cổng QC; brand Be Vietnam Pro, ink `#111111`/paper `#F7F7F5`/accent `#FF5A36`; lưu trữ theo luật 65/66 (`content/clips/` → `content/archive/` + `approved.json` khi Hiệp nói "duyệt").

## 3. Đối chiếu 7 khâu

| Khâu | short-video-factory | oneup-studio hiện tại | Cái nào tốt hơn + bằng chứng |
|---|---|---|---|
| 1. Script | LLM một prompt chung cho marketing/nội dung chung; có kiểm soát đa dạng + chống trùng (`src/lib/llm/diversity.ts`, `similarity.ts`, `copywriting-history`). Prompt cấm bịa số (prompts.ts) nhưng không bám một nguồn fact nào. | Script = `spec.json` + `script-final.md` theo template: hook pain-point + câu hỏi (L-057/L-058), throughline, fact-lock từ HowToLiveBetter, bảng Beat/Giây/Người nói/Lời/Hình+caption EN, `{nhấn:}`, fx table duyệt ở gate 1 (rule-52, SKILL.md bước 2/5). check-rules chặn rule-55/58/60/61/62/64. | **OneUp tốt hơn hẳn cho kênh này**: bám nguồn CC BY, văn nói miền Nam, chống lặp ý (L-054). Repo kia chỉ hơn ở ý tưởng đo độ tương tự văn bản giữa các bản sinh (xem Nên lấy #2). |
| 2. TTS | EdgeTTS duy nhất (README roadmap xác nhận chưa có API giọng khác). Không prosody theo cụm, không chọn take bằng STT/F0, không giọng nhân vật cố định; lịch sử lỗi 403 (CHANGELOG v1.3.0/v1.2.0). | F5-TTS local, Hiệp chibi = "F5 · Thái Sơn", Omi = "F5 · Mỹ Duyên" (luật 46/DL-035, giọng mẫu tổng hợp VieNeu, không clone người thật). F5 v4: tách đơn vị theo dấu câu, cấm cắt trong một output F5 (L-016), 3 seed, chọn take bằng STT + F0, markup `{nhấn:}/{kéo:}`, kiểm leak giọng mẫu (SKILL.md bước 2). | **OneUp tốt hơn**: giọng nhân vật nhất quán, kiểm chất lượng tự động, chạy local. EdgeTTS chỉ đáng xét làm giọng nghe thử nháp — không thay F5. Lưu ý rủi ro sẵn có: checkpoint F5 giấy phép CC-BY-NC-SA, Hiệp đã chấp nhận (DL-035) và phải bật nhãn AI khi đăng. |
| 3. Edit/Render | Electron + Pixi render phụ đề/hiệu ứng, FFmpeg trộn đoạn video **ngẫu nhiên** từ thư mục素材, hàng loạt không người trông. Không nhân vật brand, không layout chống che mặt/caption. | Remotion comic chibi + HyperFrames motion graphics; vật/hành động/tỉ lệ kể nghĩa thay vì vẽ chữ (L-050 đã duyệt); layoutCheck chặn bong bóng che prop/mặt và prop chui vào dải caption (L-033/L-038); still duyệt bằng mắt trước render; contact-sheet soát ≥2 vòng (rule-34). | **OneUp tốt hơn** về brand và độ kiểm soát từng beat. Cách trộn ngẫu nhiên của repo kia xung đột trực tiếp L-033/L-050 và luật "không stock người thật, không AI trong hình final" (luật 24/44). |
| 4. Subtitle | v1.3.0: engine render phụ đề riêng, bật/tắt hiển thị, **xuất SRT kèm video**; `src/effect-engine/shared/subtitle-srt.ts` coi SRT là "định dạng trung gian chuẩn, không绑定 TTS, tái dùng cho ASR/lời bài hát/nhập phụ đề ngoài". Đã sửa lỗi dính chữ phụ đề phi-Trung (v1.2.0). | Caption EN theo phrase (chunk ≤8 từ, L-051), highlight đúng từ khoá (L-004), không chồng thời gian (L-003), bong bóng VI theo phrase; timing từ audio thật + STT. Chưa thấy xuất SRT sidecar trong quy trình chuẩn (SKILL.md/check-rules không nhắc SRT). | **Hoà, mỗi bên mạnh một nửa**: OneUp mạnh về caption brand + đồng bộ giọng; repo kia hơn ở **SRT sidecar chuẩn hoá** — phần nên lấy duy nhất ở khâu này (Nên lấy #1). |
| 5. BGM | Có trộn BGM trong file + cân bằng âm lượng BGM/giọng (v1.2.0); CHANGELOG v1.2.1 ghi từng có lỗi chuẩn hoá âm lượng làm cụt giọng khi thêm BGM. | **Luật 21: không nhạc trong file**; Hiệp tự thêm nhạc TikTok Commercial Music Library khi đăng (5–10% theo post package). Chỉ có SFX CC0 có nguồn + ambience brown-noise rất nhỏ suốt clip (rule-50), check-rules gặp `"music"`/`bgm` trong spec là ✖ (rule-21). | **OneUp đúng rule kênh; repo kia xung đột rule.** Không lấy tính năng trộn BGM. Nếu đổi rule mới xét lại — cần Hiệp chốt. |
| 6. QC / check-rules | Có test vitest cho code (llm/tts/render) và "audio validation" cho TTS (v1.3.0), xuất chẩn đoán lỗi. Không thấy cổng QC nội dung: không kiểm fact theo nguồn, credit, độ dài, hook, nhãn AI, gói đăng. | `check-rules.py` chặn ✖ trước gate 1 và `--final`: 55–60s (dài hơn chỉ cảnh báo DL-067), −14 LUFS ±1/peak ≤ −0,5 dBFS, 1080×1920, font Be Vietnam Pro local không CDN, STT từng dòng, L-001…L-05x từ lessons.md, credit CC BY 4.0 + "đã chuyển thể", nhãn AI F5-TTS, cover từ template, post.md 12 mục. Mỗi góp ý của Hiệp thành lesson + check (rule-49). | **OneUp tốt hơn vượt trội.** Repo kia chỉ gợi ý thêm lớp xuất chẩn đoán kỹ thuật (Nên lấy #3), không thay được QC nội dung. |
| 7. Output | Xuất video từ app desktop, chạy hàng loạt theo preset, SRT kèm; không gói đăng (caption/hashtag/cover template/credit), không cổng duyệt người, không lưu trữ phiên bản theo clip. | Một clip = MP4 full + bản 720p ở `media/clips/<clip>/`, cover template A, `post.md` + `post-checklist.md`, gate 2 Hiệp duyệt final, chỉ lưu archive khi Hiệp nói "duyệt" (luật 66). Agent không tự đăng; Hiệp tự đăng + thêm nhạc TikTok. | **OneUp tốt hơn và an toàn hơn.** Chế độ "tự chạy hàng loạt" của repo kia phá vỡ rule cứng gate 1/gate 2 — không lấy. |

## 4. Nên lấy (tối đa 5 — chỉ lấy ý tưởng, viết lại sạch, không chép code AGPL)

1. **Xuất SRT sidecar kèm mỗi clip** (từ engine phụ đề v1.3.0 + `subtitle-srt.ts`): sinh `.srt` từ timing/caption đã có, để Hiệp có phụ đề rời khi đăng/kiểm tra, không thay caption brand cháy trong hình.
2. **Đo độ tương tự script giữa các clip** (ý tưởng từ `diversity.ts`/`similarity.ts`/`copywriting-history`): bổ sung cho audit lặp ý thủ công (L-054) bằng cảnh báo khi hook/câu chốt trùng cao với clip trước — chỉ cảnh báo ở gate 1, không tự viết lại lời đã chốt.
3. **Gói chẩn đoán khi build lỗi** (v1.3.0: diagnostic export + lỗi kèm phiên bản): `build-final.py` khi fail thì xuất một file log gọn (bước lỗi, phiên bản engine, spec id) để gửi/soát, giảm vòng debug.
4. **Cache metadata素材 + xử lý file素材 không đọc được** (v1.2.2/v1.3.0): dò thời lượng/định dạng素材 một lần có cache và báo file hỏng sớm ở bước plans, thay vì fail giữa render.
5. **Cấu hình LLM viết script đa giao thức + thông số đa dạng** (v1.3.0): nếu sau này cần thêm nhà cung cấp LLM cho bước *soạn nháp*, dùng cấu hình provider/sampling tách riêng — vẫn phải qua fact-lock, humanizer và gate 1 như hiện tại.

## 5. Không nên lấy

- **Thay F5-TTS bằng EdgeTTS**: mất giọng Thái Sơn/Mỹ Duyên đã chốt, mất prosody/STT/F0, phụ thuộc dịch vụ không chính thức từng 403.
- **Trộn đoạn video ngẫu nhiên từ thư mục素材**: phá brand comic chibi, L-033/L-050, luật không stock người thật/không AI trong hình final; rủi ro bản quyền素材 (README repo ghi素材 mẫu "lấy từ mạng, chỉ để demo").
- **Trộn BGM trong file**: trái luật 21; Hiệp tự thêm nhạc TikTok khi đăng.
- **Chế độ một cú bấm / hàng loạt không cổng duyệt**: trái rule cứng — không render khi chưa chốt script (gate 1), không xuất final khi chưa qua gate 2.
- **Dựng thêm app Electron GUI** song song Remotion/HyperFrames: thêm một stack phải bảo trì, không giải quyết khâu nào OneUp đang yếu.
- **Tin các khẩu hiệu hiệu năng trên trang giới thiệu của repo** ("30 giây ra một video, ngày 100 video, chạy 24×7"): chưa kiểm chứng, không chạy thử theo đúng phạm vi việc này.

## 6. Rủi ro / giấy phép

- **AGPL-3.0** (file LICENSE của repo): copyleft mạnh — chép/sửa code rồi phân phối hoặc cho dùng qua mạng có thể kéo theo nghĩa vụ công bố mã nguồn phái sinh. Vì vậy báo cáo này chỉ đề xuất **lấy ý tưởng và tự viết lại**; muốn fork/dùng code thật phải có quyết định riêng của Hiệp (và soát pháp lý nếu kênh thương mại hoá).
- **EdgeTTS**: dịch vụ phía Microsoft không có cam kết API; CHANGELOG cho thấy đã gãy vì thay đổi xác thực (403). Dùng làm giọng chính = rủi ro gãy pipeline bất cứ lúc nào, chưa kể điều khoản sử dụng giọng.
- **LLM qua API ngoài**: API key, chi phí, và nội dung nháp rời máy — trái với thế mạnh "chạy local" hiện tại của F5/Remotion; prompt chung của repo không có fact-lock nên nguy cơ bịa số/nguồn nếu dùng thẳng cho nội dung HowToLiveBetter (bản thân nội dung nguồn là CC BY 4.0, vẫn phải credit + ghi "đã chuyển thể" theo luật 13).
- **Rủi ro sẵn có không đổi**: checkpoint F5-TTS tiếng Việt CC-BY-NC-SA (DL-035, Hiệp đã chấp nhận) và nghĩa vụ bật nhãn "AI-generated content" trên TikTok cho mọi clip có giọng AI — đổi hay không đổi công cụ đều phải giữ.
- **Chưa kiểm chứng kỹ thuật**: toàn bộ nhận định về repo kia dựa trên tài liệu/cây code công khai; chưa cài/chạy nên chưa biết chất lượng giọng tiếng Việt của EdgeTTS trong app, tốc độ render thật, hay độ ổn định bản Linux.

## 7. Điểm cần Hiệp chốt (trước bất kỳ thử nghiệm nào)

1. Có muốn thêm **SRT sidecar** vào gói xuất clip không (Nên lấy #1)?
2. Có muốn bổ sung **cảnh báo trùng lặp script** vào check-rules ở gate 1 không (Nên lấy #2)?
3. Có muốn **gói chẩn đoán build lỗi** cho `build-final.py` không (Nên lấy #3)? Hai mục #4/#5 chỉ làm khi Hiệp thấy cần.
4. EdgeTTS: **không thử** / chỉ nghe thử một câu nháp so với F5 / bỏ hẳn khỏi danh sách?
5. Chủ trương giấy phép: **chỉ lấy ý tưởng, không dùng code AGPL** — đúng ý Hiệp không, hay muốn thử fork tách riêng ngoài pipeline?
6. Khẳng định lại rule hiện hành: **không nhạc trong file** và **không render khi chưa chốt script** vẫn giữ nguyên (báo cáo này mặc định giữ cả hai).

## Nguồn đã đọc

- Repo: github.com/YILS-LIN/short-video-factory — README.md, LICENSE (AGPL-3.0), package.json v1.3.0, CHANGELOG.md (v1.0.0–v1.3.0, 16/10/2026), `src/lib/llm/prompts.ts`, `src/effect-engine/shared/subtitle-srt.ts`, cây file qua GitHub API, trang short-video-factory.yils.blog.
- Box: `/workspace/oneup-studio/{README.md, AGENTS.md, logs/lessons.md, pipeline/pipeline.md, pipeline/scripts/check-rules.py, rules/video-rules.md, content/voice-profile.md}`, `/home/box/agent-data/workflows/make-video/SKILL.md`.
