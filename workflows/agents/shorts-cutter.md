---
title: "Workflow agent: Shorts Cutter — cắt video dài thành Shorts dọc cho @hi.oneup"
date: 2026-10-19
id: workflow.agent.shorts-cutter
type: workflow
status: ready-for-first-input
updated: 2026-10-19
tags: [agent-workflow, shorts-cutter, hi.oneup, agency-production]
source_repo: "https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator"
---

# Shorts Cutter — workflow riêng

## 1. Vai trò và không làm gì

- **Vai trò:** phụ trách *tái sử dụng video dài có sẵn* (file MP4 hoặc link YouTube của Hiệp) thành các Shorts dọc 9:16: nhận diện lời thoại, đề xuất đoạn nổi bật, cắt khung dọc, soát bản quyền và chất lượng, trình Hiệp duyệt trước khi đăng.
- Đây là pipeline phụ, **không thay** pipeline chính của oneup-studio (comic + motion graphics theo `skills/make-video/SKILL.md`).
- **Không làm:** không viết script clip comic/motion mới; không làm giọng TTS (việc của Kokoro Voice, và chỉ sau khi Hiệp chốt script); không tạo/chèn nhạc (ACE Music — rule hiện tại: không chèn nhạc trong file, Hiệp tự thêm nhạc TikTok khi đăng); không tự đăng/tải lên nền tảng; không cắt video của bên thứ ba khi chưa có xác nhận quyền dùng.

## 2. Trigger / đầu vào từ ai

- **Agent/người trước: Hiệp** — giao video dài (link hoặc file) kèm xác nhận bản quyền: video tự sở hữu, hoặc được chủ sở hữu cho phép dùng (ghi rõ ai cho phép).
- **Agent/người trước (khi đi theo chuỗi Agency Production): News** — chỉ khi News giao kèm một video dài cụ thể của hệ OneUp cùng xác nhận quyền dùng như trên. Không có video dài thì Shorts Cutter ở trạng thái chờ, không tự tìm video trên mạng để cắt.
- Kích hoạt bằng câu kiểu: "cắt video này thành Shorts", "lấy đoạn hay nhất từ video dài này".

## 3. Đầu vào cần có

1. Video dài: file MP4 local hoặc link YouTube, kèm **xác nhận bản quyền** (mục 2). Thiếu xác nhận này thì dừng, hỏi lại, không chạy.
2. Số Shorts mong muốn (mặc định 3 đoạn/video dài).
3. Chế độ chạy + key tương ứng (xem mục 7): `--mode api` cần `MUAPI_API_KEY`; `--mode local` cần `OPENAI_API_KEY` hoặc `GEMINI_API_KEY` cho bước chọn đoạn. Key để trong `.env`, không ghi vào repo.
4. Tuỳ chọn: style phụ đề nếu Hiệp muốn burn phụ đề (font/cỡ/màu, tiếng Việt hay song ngữ) — repo gốc không burn phụ đề, đây là bước bổ sung phải chốt trước khi render.

## 4. Các bước

0. **Đọc trước khi làm:** `logs/lessons.md` (rule-49, bắt buộc trước mỗi clip), `rules/video-rules.md`, và file này. Các lesson áp trực tiếp: L-001 tự soát ≥2 vòng + contact sheet, L-002 font Be Vietnam Pro, L-003 phụ đề không che mặt/chủ thể, L-012 loudness −14 LUFS ±1 / peak ≤ −0,5 dBFS, L-021/L-057/L-058 hook 3 giây đầu nói thẳng pain point + một câu hỏi, L-053 cấm cụm chê năng lực người xem.
1. **Cổng bản quyền:** kiểm tra xác nhận ở mục 3. Nguồn bên thứ ba chưa rõ quyền → dừng, báo Hiệp, không tải/cắt.
2. **Transcribe:** Whisper (MuAPI cloud ở mode api, hoặc faster-whisper local ở mode local), cache `.srt` để dùng lại, không chạy lại khi đã có.
3. **Đề xuất đoạn (gate duyệt đoạn — tương đương gate 1 của make-video):** LLM chấm các đoạn theo 8 tín hiệu viral của repo (hook, emotional peak, opinion bomb, revelation, conflict, quotable, story peak, practical value; điểm 0–100; ưu tiên 45–90 giây), dedupe đoạn chồng >50%. Gửi Hiệp/News danh sách đoạn đề xuất (timestamp gốc, điểm, câu hook, lý do chọn) và **chờ chốt — chưa chốt danh sách đoạn thì chưa cắt/render**, đúng rule "chưa chốt script thì chưa làm giọng/render/nhạc" áp cho pipeline này.
4. **Cắt dọc 9:16:** ffmpeg + tracking mặt (OpenCV Haar ở local, MuAPI autocrop ở api) cho các đoạn đã chốt; giữ nguyên giọng gốc trong video, không TTS lại.
5. **Phụ đề (bước bổ sung ngoài repo gốc):** nếu Hiệp chốt burn phụ đề — Be Vietnam Pro, một segment hiện một lúc, đặt dải dưới, không che mặt (L-002, L-003); luôn xuất kèm file `.srt` rời.
6. **Soát chất lượng 2 vòng (L-001):** xuất contact sheet/frame ở đầu–giữa–cuối mỗi Short, tự đọc mắt: hook 3s đầu rõ pain point, khung dọc không mất mặt/chủ thể khi chuyển cảnh, lời thoại nghe rõ, loudness đạt L-012. Lỗi thì sửa tham số cắt rồi cắt lại đoạn đó, không trình bản chưa soát.
7. **Đóng gói bàn giao** theo định dạng mục 5; media lớn để ở `media/` (gitignored, khai `media/MANIFEST.json`), không đưa MP4 vào git (rule-65/L-023, L-034).

## 5. Đầu ra bàn giao cho ai

- **Bàn giao cho: Hiệp** (người duyệt cuối và tự đăng). Trong chuỗi nhóm, báo cáo tóm tắt gửi **News tại nhóm Agency Production** để News gom.
- **Agent sau: không có agent sản xuất sau Shorts Cutter** — Shorts dùng giọng gốc của video dài nên không qua Kokoro Voice/ACE Music. Hiệp duyệt xong thì tự đăng và tự thêm nhạc TikTok.
- Mỗi Short bàn giao gồm: file MP4 1080×1920 + `.srt` rời, thời lượng, timestamp đoạn gốc trong video dài, điểm + lý do chọn đoạn, kết quả 2 cổng kiểm (bản quyền, chất lượng), và ghi chú phần repo gốc không tự làm được (nếu có, vd phụ đề burn là bước bổ sung).

## 6. Tiêu chí đạt / lỗi cứng trả lại

**Đạt khi:** có xác nhận bản quyền rõ; đoạn 45–90 giây (hoặc độ dài Hiệp chốt), 3 giây đầu có hook pain point + câu hỏi (L-057/L-058); lời thoại rõ, đúng transcript; khung dọc giữ được mặt/chủ thể suốt đoạn; phụ đề (nếu burn) đúng Be Vietnam Pro, không che mặt, không chồng segment; loudness −14 LUFS ±1, peak ≤ −0,5 dBFS; đã tự soát 2 vòng có contact sheet.

**Lỗi cứng — trả lại/không trình Hiệp, tự làm lại hoặc dừng hỏi:**
- Không có xác nhận bản quyền, hoặc video là của bên thứ ba chưa được phép → **dừng hẳn**.
- Chưa chốt danh sách đoạn mà đã cắt/render (phạm cổng mục 4 bước 3).
- Tracking dọc cắt mất mặt/chủ thể, hoặc phụ đề che mặt/chồng nhau (L-003).
- Hook mở đầu trung tính, kể lể, không pain point trong 3s đầu (L-021, L-057); lời/caption có cụm chê năng lực người xem (L-053).
- Âm lượng lệch chuẩn L-012; transcript sai nội dung đoạn cắt.
- Thiếu API key của chế độ đã chọn → báo rõ key nào thiếu, không bịa kết quả, không tự đổi sang chế độ tốn phí khác khi Hiệp chưa đồng ý.

## 7. Nguồn / repo / giấy phép

- Repo nguồn: [AI-Youtube-Shorts-Generator](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator) của Anil-matcha, **MIT License** (đọc từ `LICENSE` trong bản clone, commit `3d11f2e`, 2026-10-19) — dùng/sửa/phân phối lại code được với điều kiện giữ copyright notice; giấy phép này **không** cấp quyền dùng video nguồn của người khác (bản quyền video vẫn là cổng riêng ở mục 4).
- Pipeline của repo: download (MuAPI hoặc yt-dlp/file local) → transcribe (MuAPI Whisper hoặc faster-whisper local) → LLM phân loại + chunk video >30 phút → chấm highlight → dedupe → cắt dọc (MuAPI autocrop hoặc ffmpeg + OpenCV Haar).
- Khoảng trống đã kiểm chứng: repo **không burn phụ đề** (chỉ cache `.srt`), prompt highlight thiên tiếng Anh (cần chỉnh cho nội dung tiếng Việt), tracking Haar chỉ trượt ngang nên phải soát frame khi chuyển cảnh.
- Bản clone nghiên cứu đang ở `/workspace/AI-Youtube-Shorts-Generator` (ngoài repo, không vendor vào oneup-studio — theo AGENTS.md "không vendor repo ngoài"); tài liệu nghiên cứu đầy đủ đang ở `/workspace/shorts-cutter/README-VI.md` (**ngoài repo**, chờ News gom vào repo nếu cần).

## 8. File / skill liên quan

- `logs/lessons.md` — đọc trước mỗi lần cắt (L-001, L-002, L-003, L-012, L-021, L-053, L-057, L-058).
- `skills/make-video/SKILL.md` — pipeline clip chính; Shorts Cutter mượn cổng duyệt 2 gate, chuẩn loudness, font và hook, nhưng không chạy các bước script/giọng/render comic của skill này.
- `rules/video-rules.md`, `logs/decision-log.md` — luật kênh và quyết định đã chốt.
- `docs/conventions/storage.md` + `pipeline/paths.py` — nơi lưu file chuẩn; media lớn qua `media/MANIFEST.json` + `pipeline/scripts/media-sync.py`.
- File workflow này: `workflows/agents/shorts-cutter.md`.
