---
id: decision-log
type: log
status: living
updated: 2026-10-13
tags: [decisions, feedback]
---
# Nhật ký quyết định: @hi.oneup (luật 33)
Đọc lại trước mỗi clip mới. Góp ý lặp lại từ 2 lần → nâng thành luật hoặc skill.

| ID | Ngày | Yêu cầu / góp ý của Hiệp (tóm tắt) | Quyết định | Luật / file |
|---|---|---|---|---|
| DL-001 | 2026-10-12 | Trả lời 18 câu hỏi chuẩn hoá trước khi làm video đầu tiên | Chốt 18 luật v1 | rules/video-rules.md |
| DL-002 | 2026-10-12 | "Lưu lại và tuỳ nội dung script để chọn motion" | Motion chọn theo từng script bằng skill, ghi effects log | luật 19, skills/motion-picks-per-script, logs/effects-log.md |
| DL-003 | 2026-10-12 | Đọc thư mục brand để index design cho video | Lập brand index + tokens, logo 05-pair-plus | brand/brand-index.md, brand/brand-tokens.json |
| DL-004 | 2026-10-12 | Preview "xấu quá, kiểm tra lại, dùng đúng font" | Làm lại. Đặt chuẩn chất lượng premium, tự xem và sửa ≥2 vòng trước khi gửi | luật 34 |
| DL-005 | 2026-10-12 | Chữ tiếng Việt trên màn hình thì dùng font gì → "Be Vietnam Pro" | DM Sans thiếu dấu tiếng Việt chồng, nên dùng Be Vietnam Pro | luật 15 |
| DL-006 | 2026-10-12 | "Dùng font Poppins được không" | Không dùng: lệch brand và nghi thiếu dấu tiếng Việt. Hiệp chốt dùng Be Vietnam Pro cho mọi chữ | luật 15 |
| DL-007 | 2026-10-12 | Dark/light xen kẽ theo tone của series HowToLiveBetter | LIGHT = tích cực, DARK = mặt trái, tối đa 2 clip cùng theme liền nhau. 13 LIGHT / 17 DARK | luật 17, content/theme-map.md |
| DL-008 | 2026-10-12 | Video khoảng 1 phút, có giải thích và minh hoạ trực quan, nghiên cứu hệ thống chặt chẽ, hỏi trước khi quyết | Research production system, 20 câu hỏi quyết định | research/production-system-research-vi.md |
| DL-009 | 2026-10-12 | Duyệt cả 20 đề xuất | Rules v2 (55–60s, render nháp trên box + final trên Mac, 3 clip/tuần trong 2 tuần đầu, SFX CC0…) | rules/video-rules.md v2 |
| DL-010 | 2026-10-12 | Lưu toàn bộ dữ liệu vào repo oneup-studio | Dựng cấu trúc repo, commit | README.md |
| DL-011 | 2026-10-12 | Viết lại script clip 01 cho 55–60s | Script v2, chờ duyệt | content/clips/clip-01-implementation-intention/script.md |
| DL-012 | 2026-10-12 | Làm storyboard từng beat | Storyboard 10 frame + contact sheet. Thêm bước storyboard trước khi duyệt script | luật 35, pipeline/pipeline.md |
| DL-013 | 2026-10-12 | Ghi lại mọi quyết định để cải tiến liên tục | Tạo file này + retro tuần | luật 33 |
| DL-014 | 2026-10-12 | Tìm hiểu microsoft/skillopt | Đánh giá, chưa áp dụng (xem research/skillopt-eval-vi.md) | research/skillopt-eval-vi.md |
| DL-015 | 2026-10-12 | Storyboard phải là tài sản có phiên bản, khi góp ý thì sửa từ nguồn đã commit chứ không tạo lại. Repo thiết kế cho AI tra cứu (AGENTS.md, index, front-matter, id ổn định) | spec.json + renderer chung. AGENTS.md, INDEX.md / index.json, front-matter | rule-36, AGENTS.md, INDEX.md |
| DL-016 | 2026-10-12 | Hệ thống nghiên cứu trend hằng ngày (digest + ingest), skill trend-digest. Mỗi script phải dùng ≥1 cụm từ / tình huống đang phổ biến. Đồng bộ từ box sang repo | research/trends/, skill trend-digest, sync-trends.sh. Digest đầu tiên 2026-10-12 | rule-37, rule-38 |
| DL-017 | 2026-10-12 | Mở rộng trend sang mọi chủ đề nóng (VN + global), thêm bước bridge trend → bài học HowToLiveBetter, nhiều góc, lọc brand-safety | Viết lại skill trend-digest, thêm bảng Bridges trong ingest, chạy lại digest 2026-10-12, thêm vào idea-bank | rule-39, skills/trend-digest |
| DL-018 | 2026-10-12 | Đánh giá blader/humanizer, tạo voice profile, áp lên clip 01 thành bản v2.1 draft | Vendor humanizer (MIT) + skill script-polish + content/voice-profile.md + script-v2.1-draft.md | rule-40 |
| DL-019 | 2026-10-12 | Trả lời câu hỏi voice profile: bạn/mình, miền Nam + từ đệm, hài 4/5 (cà khịa, đá xéo, nhắc khéo, tinh tế), chen tiếng Anh, không có từ cấm, chuyện thật càng nhiều càng tốt, thích kể chuyện, không có ví dụ "dự án ma" riêng | voice-profile confirmed. Skill script-polish áp dụng. Tạo story-bank | content/voice-profile.md, skills/script-polish, content/story-bank.md |
| DL-020 | 2026-10-12 | Script phải kể chuyện trước, chỉ dùng chuyện thật. Viết clip 01 v3 draft + storyboard v3 | rule-41. script-v3-draft.md, spec-v3.json → storyboard/v3/ (spec v2 giữ nguyên) | rule-41, clip-01 |
| DL-021 | 2026-10-12 | Clip kể chuyện minh hoạ kiểu comic, Omi là trợ lý giúp Hiệp. Nghiên cứu công cụ, làm model sheet trước | research/comic-system-research-vi.md. Rig SVG + model sheet Hiệp v0.1, sheet Omi (companion), comic spec + renderer, strip clip-01 b01–b03. ⚠ Mâu thuẫn rule-11 (Omi từ tuần 5): đã báo, chưa đổi luật | brand/characters/, pipeline/comic/, content/clips/clip-01-*/comic/ |
| DL-022 | 2026-10-13 | Trả lời 6 câu hỏi nhân vật: cute/bo tròn/liquid; Omi từ tuần 5; Omi có giọng cảm xúc; comic chỉ cho beat kể chuyện, còn lại motion minh hoạ; cách điệu mạnh; cho AI image local để phác | Research hoạt hoạ (GSAP + SVG gooey + blob morph), rig v2 chibi, sheet + motion test 7s. Luật 42–44. Luật 11 giữ | rule-42, rule-43, rule-44, research/character-animation-research-vi.md, brand/characters/v2/ |
| DL-023 | 2026-10-13 | Giọng AI cảm xúc cho Omi (mâu thuẫn luật "không giọng AI") | Research TTS local tiếng Việt, đề xuất A/B/C (VieNeu-TTS Apache-2.0 đứng đầu). **Chưa đổi luật, chờ Hiệp chọn** | research/omi-voice-tts-research-vi.md |
| DL-024 | 2026-10-13 | Prompt hệ thống: dựng hệ thống tự động tạo video nhân vật comic (Remotion + React + TS, HyperFrames chỉ khi hợp lý, LLM tuỳ chọn, không AI ảnh/video, test + README) | `video-engine/`: schema zod + validator, profile Hiệp/Omi, rig SVG, state controller tất định, composition nhiều cảnh, planner rule-based + interface LLM OpenAI-compatible (fallback), CLI validate/plan/render/frames, 34 test. Mẫu clip-01 b01–b03 + debugging-story. Remotion license: miễn phí cho cá nhân/≤3 người. Sửa render.js bỏ phụ thuộc /tmp/pp | rule-45, video-engine/README.md |
| DL-025 | 2026-10-13 | Chọn giọng Omi: **A** (VieNeu-TTS). "Kiểm tra hoàn thiện rules đã có từ trước chưa" | Luật 46 (chỉ Omi có giọng AI, VieNeu local, preset "Kim Thanh", không clone, emotion theo câu, nhãn AI TikTok khi có giọng Omi). Audit 45 luật → rules v3.0: sửa luật 2, 5, 6 (tạm, chờ xác nhận), 7, 11, 16, 18, 24, 25+45, 26, 32, 42; sửa brand-index, pipeline, research TTS, voice-profile | rule-46, rules v3.0, logs/rules-audit-2026-10-13.md |
| DL-026 | 2026-10-13 | "Kết hợp toàn bộ và tạo 1 video sample một phân cảnh cho tôi xem" | Sample 15,5s tuần 5+: comic Hiệp + Omi (Omi có giọng, Hiệp chỉ bubble), caption EN highlight, xfade sang explainer HyperFrames If → Then. Thêm `npm run voice`, lip-sync theo envelope, audio trong render, logo trong composition, `join-beats.sh`, 7 test | content/samples/sample-full-w5/, video-engine/src/voice/, pipeline/tts/, pipeline/scripts/join-beats.sh |
| DL-027 | 2026-10-13 | "Không cần yêu cầu tự quay để sau hoặc series khác. Nên để comic cho đồng nhất sợ cảnh quay thật k tương thích video" | Series chỉ comic + motion graphics, bỏ ≥50% tự quay / "ít nhất 1 cảnh thật" / shot list / b-roll AirDrop; Hiệp chỉ thu giọng. Cảnh thật để giai đoạn sau / series khác | rule-3, 5, 6, 23, 29; pipeline.md, AGENTS.md, README.md |
| DL-028 | 2026-10-13 | "Khỏi nhắc" (lịch nhắc đăng) | Xoá routine nhắc đăng, Hiệp tự đăng | rule-32 |
| DL-029 | 2026-10-13 | "Cải tiến job ingest news trending học hỏi để làm nội dung nổi bật khác biệt nhưng vẫn đảm bảo tính hệ thống liền mạch" | Skill trend-digest v2: tín hiệu miễn phí, novelty/saturation + dedupe (`trend-learn.py`), thư viện hook `patterns.md`, bước khác biệt, plan stub JSON qua validator, tổng hợp tuần Chủ nhật. Routine prompt v2 (07:55 hằng ngày + Chủ nhật) chờ áp dụng | rule-47, rule-38, skills/trend-digest, research/trends/patterns.md, pipeline/scripts/trend-learn.py |
| DL-030 | 2026-10-13 | "Trước tiên hãy tạo 1 video hoàn chỉnh, giọng nhân vật vẫn dùng AI VieTTS giọng nam trầm ấm, Omi giọng nữ" | Hiệp chibi cũng dùng giọng AI preset: nghe thử 4 preset nam miền Nam (Thái Sơn, Minh Triết, Đức Trí, Adam), đo F0 + STT → chọn **Đức Trí** (F0 ≈ 91 Hz, trầm nhất, STT đúng), tempo 1.3× (Kim Thanh 1.12×). Validator/test cho phép audio với nhân vật có preset. Nhãn AI cho mọi clip có giọng AI. Clip 01 final demo 57,2s (week 5 vì có Omi, không đăng như tuần 1): `build-final.py`, caption theo từng câu, SFX tự tổng hợp, grain, −14 LUFS | rule-2, 24, 26, 29, 32, 45, 46; hiep.json; vieneu_tts.py; clip-01/final/ |
| DL-031 | 2026-10-13 | "Giờ mỗi lần làm video tôi cần yêu cầu như thế nào. Có skill nào đảm bảo rules consistent hết không, script generate tôi review như thế nào" | Skill `skills/make-video` (quy trình end-to-end, 2 gate duyệt, góp ý theo beat id, sửa spec), `pipeline/scripts/check-rules.py` (lint script + spec + plan + MP4 + post theo luật), luật 48 | rule-28, rule-48, skills/make-video |
## Góp ý lặp lại (theo dõi để nâng thành luật)
| Chủ đề | Số lần | Đã nâng? |
|---|---|---|
| Font / chất lượng hình ảnh | 3 (xấu quá, đúng font, Poppins) | Có, luật 15 và 34 |

## Retro tuần
### Tuần 1 (Chủ nhật 18/10/2026)
- Điều tốt:
- Điều cần sửa:
- Chỉ số (view, tỉ lệ xem hết, follow):
- Luật / skill đã đổi:
