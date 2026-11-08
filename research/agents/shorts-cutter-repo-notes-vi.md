---
title: "Shorts Cutter — vận hành cắt video dài thành Shorts dọc cho @hi.oneup"
date: 2026-10-19
status: ready-for-first-input
source_repo: "https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator"
repo_path: "/workspace/AI-Youtube-Shorts-Generator"
id: shorts-cutter-readme-vi
type: guide
updated: 2026-10-19
tags: [shorts-cutter, hi.oneup, shorts, pipeline]
source: "https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator (MIT, commit 3d11f2e)"
---

# Shorts Cutter — Vận hành cho @hi.oneup

## 1. Mục đích & vai trò

Shorts Cutter là pipeline phụ trợ cho kênh **@hi.oneup** (Văn Hiệp Lê): lấy một video dài
(YouTube URL hoặc file MP4 local) → tự chọn đoạn nổi bật → cắt thành các Shorts dọc 9:16
có điểm viral, hook và lý do chọn đoạn, để Hiệp duyệt trước khi đăng.

- Đây **không** thay thế pipeline video chính của `oneup-studio` (comic + motion graphics,
  Remotion/HyperFrames). Shorts Cutter chỉ xử lý việc *tái sử dụng video dài có sẵn* thành Shorts.
- Trước mỗi clip, bắt buộc đọc `/workspace/oneup-studio/logs/lessons.md` (đã đọc 2026-10-19).
  Các lesson liên quan trực tiếp khi cắt Shorts:
  - **L-001**: tự soát ≥2 vòng, có contact sheet/frame kiểm tra trước khi gửi Hiệp.
  - **L-002**: chữ/phụ đề tiếng Việt dùng **Be Vietnam Pro** (có sẵn tại
    `/workspace/oneup-studio/brand/fonts/`), tránh font thiếu dấu.
  - **L-003**: phụ đề không chồng nhau, không che mặt/chủ thể.
  - **L-012**: chuẩn hoá loudness khoảng **−14 LUFS ±1, peak ≤ −0,5 dBFS** khi chốt bản đăng.
  - **L-021 / L-057 / L-058**: 3 giây đầu phải có hook rõ — nói thẳng pain point của người xem +
    một câu hỏi/câu punch, không mở đầu trung tính, dài dòng.
  - **L-053**: không dùng cụm chê năng lực người học/người xem.

## 2. Repo gốc — tóm tắt kỹ thuật (đã kiểm chứng trên box)

Repo: `/workspace/AI-Youtube-Shorts-Generator` — commit `3d11f2e` ("Update README with new video links", clone `--depth 1` ngày 2026-10-19).

### Pipeline 8 bước (`shorts_generator/pipeline.py`)

1. **Download** — API: MuAPI `/youtube-download`; Local: `yt-dlp` (URL) hoặc đọc thẳng file local/`file://`.
2. **Transcribe** — API: MuAPI `/openai-whisper` (Whisper cloud); Local: `faster-whisper` trên box
   (model mặc định `base`, CPU `int8` / CUDA `float16`, cache transcript thành `.srt` trong output dir).
3. **Phân loại nội dung** — LLM đoán content type (podcast/interview/tutorial/vlog…) + mật độ.
4. **Chunk video dài** — >30 phút (`LONG_VIDEO_THRESHOLD=1800s`) thì chia chunk 20 phút
   (`CHUNK_SIZE_SECONDS=1200s`), chồng lấp 60s.
5. **Chọn highlight (highlight detection)** — LLM chấm theo `VIRALITY_CRITERIA` trong
   `shorts_generator/highlights.py`: hook moments, emotional peaks, opinion bombs, revelation,
   conflict, quotable one-liners, story peaks, practical value. Mỗi ứng viên có
   `title, start_time, end_time, score 0–100, hook_sentence, virality_reason`.
   Sweet spot trong prompt: **45–90s** (20–44s cho one-liner, tối đa 180s khi cần trọn mạch chuyện).
6. **Dedupe** — hai đoạn chồng >50% thì giữ đoạn điểm cao hơn.
7. **Top-N** — lấy `--num-clips` đoạn cao nhất (mặc định 3).
8. **Cắt dọc 9:16** — API: MuAPI `/autocrop`; Local: `ffmpeg` cắt đoạn + OpenCV Haar cascade
   theo dõi mặt (làm mượt `smoothing=0.15`, cửa sổ dọc trượt ngang) rồi mux lại audio.

### Hai chế độ & API key bắt buộc

| | `--mode api` (mặc định) | `--mode local` |
|---|---|---|
| Download / Whisper / Crop | MuAPI (cloud) | yt-dlp / faster-whisper / ffmpeg+OpenCV (trên box) |
| LLM chọn highlight | MuAPI `gpt-5-mini` | OpenAI `gpt-4o-mini` **hoặc** Gemini `gemini-2.5-flash` |
| Key bắt buộc | `MUAPI_API_KEY` | `OPENAI_API_KEY` hoặc `GEMINI_API_KEY` |
| Output | URL hosted | file local `output/short_01.mp4`, `short_02.mp4`… |
| Chi phí | trả theo phút/clip cho MuAPI | trả theo token LLM; Whisper/cắt chạy free trên box |

Không có key nào thì **không chạy được bước highlight** ở cả hai chế độ. Hiện trên box **chưa có**
`MUAPI_API_KEY` / `OPENAI_API_KEY` / `GEMINI_API_KEY` nào (đã kiểm tra: không có `.env`, không có biến môi trường).

### Khoảng trống quan trọng so với nhu cầu @hi.oneup

- **Repo KHÔNG burn phụ đề vào video.** Local mode chỉ ghi cache `.srt` để tái dùng transcript;
  file Shorts xuất ra không có caption cháy. Muốn có phụ đề phải tự thêm bước hậu kỳ
  (vd `ffmpeg -vf subtitles=...` với font Be Vietnam Pro) — chưa làm, chờ Hiệp chốt style phụ đề.
- Prompt highlight viết cho nội dung tiếng Anh/viral quốc tế; video tiếng Việt cần kiểm tra thực tế
  độ chính xác của Whisper (`--language vi`) và có thể cần tinh chỉnh prompt — chưa kiểm chứng được
  vì chưa có video mẫu + key.
- Face tracking local chỉ là Haar cascade trượt ngang, không nhận diện nhiều người nói luân phiên,
  không crop dọc theo chiều dọc — đoạn có 2 người/bảng viết/slide dễ cắt mất chủ thể. Phải soát tay bằng frame.
- Chưa có bước chuẩn hoá loudness, hook text overlay frame 0, hay cover — các bước này thuộc checklist tay ở mục 4.

## 3. Quy trình đầu vào → đầu ra (khi chạy thật)

```
[1] Hiệp cấp: link/file video dài + xác nhận bản quyền (mục 4a) + số Shorts mong muốn
        ↓
[2] Shorts Cutter kiểm tra nguồn (ffprobe: thời lượng, độ phân giải, audio) — ghi vào báo cáo
        ↓
[3] Chạy pipeline (chế độ đã chốt + key đã cấp):
    python main.py "<URL hoặc đường dẫn file>" --mode local --num-clips <N> \
        --aspect-ratio 9:16 --language vi --output-json result.json
        ↓
[4] Nhận ứng viên: result.json (transcript + mọi highlight + top-N shorts)
        ↓
[5] (Nếu Hiệp chốt style) burn phụ đề + chuẩn hoá loudness bằng ffmpeg
        ↓
[6] CHECKLIST BẮT BUỘC mục 4 — bản quyền + chất lượng, tự soát ≥2 vòng (L-001)
        ↓
[7] Gửi Hiệp theo định dạng báo cáo mục 5. Chỉ đăng khi Hiệp duyệt. Không tự đăng.
```

Đầu ra mỗi Shorts: file MP4 dọc 9:16 (local: `short_NN.mp4`), kèm metadata trong `result.json`.

## 4. Checklist BẮT BUỘC trước khi trình Hiệp

Không đạt bất kỳ mục nào ở 4a thì **dừng, không cắt, hỏi lại Hiệp**. Không đạt 4b thì sửa/cắt lại, không gửi bản lỗi.

### 4a. Bản quyền nội dung nguồn — CHẶN CỨNG

- [ ] Video nguồn là **của Hiệp tự quay/sở hữu**, hoặc Hiệp xác nhận **được phép dùng/cắt lại/đăng lại** (ghi rõ ai cấp phép, phạm vi: đăng Shorts trên kênh nào, có monetize không).
- [ ] Nếu là video của **người thứ ba** (kể cả video YouTube công khai): **DỪNG — không tải, không cắt** — hỏi Hiệp về quyền sử dụng trước. "Công khai trên YouTube" ≠ "được phép cắt đăng lại".
- [ ] Kiểm tra thành phần bên trong video: nhạc nền, đoạn clip chèn, hình ảnh của bên khác — có yếu tố nào có bản quyền riêng không? Có thì ghi rõ trong báo cáo để Hiệp quyết (thay nhạc/cắt bỏ đoạn/giữ nguyên có dẫn nguồn).
- [ ] Ghi kết quả check bản quyền vào báo cáo giao Shorts (mục 5) — không có dòng này thì báo cáo chưa hoàn chỉnh.

### 4b. Chất lượng cắt — soát từng Shorts

- [ ] **Hook 3s đầu**: câu mở có dừng lướt được không? Ưu tiên pain point của người xem + punch/câu hỏi (L-057/L-058). Mở đầu trung tính/dài dòng → chọn lại điểm cắt hoặc loại đoạn.
- [ ] **Lời thoại rõ & trọn ý**: không cắt giữa câu/giữa ý; đầu–cuối đoạn nghe liền mạch; Whisper transcript khớp lời nói (soát đoạn nghi ngờ bằng tai, không tin 100% transcript).
- [ ] **Khung dọc 9:16**: mặt/chủ thể chính không bị cắt mất, không bị cửa sổ crop trượt lạc khi người nói di chuyển/đổi người nói; có bảng/slide thì chữ quan trọng còn đọc được.
- [ ] **Phụ đề** (khi đã burn): đúng chính tả tiếng Việt, khớp lời, một đoạn một ý tại một thời điểm, nằm vùng dưới an toàn, **không che mặt** (L-003), font Be Vietnam Pro (L-002).
- [ ] **Độ dài hợp lý**: ưu tiên 30–90s; <20s chỉ khi là one-liner trọn ý; >90s phải có lý do mạch chuyện.
- [ ] **Âm thanh**: nghe rõ, không rè/đứt, loudness hướng tới −14 LUFS ±1, peak ≤ −0,5 dBFS (L-012) ở bản chốt đăng.
- [ ] **Tự soát ≥2 vòng** (L-001): xem lại toàn bộ Shorts ít nhất 2 lần + trích frame đầu/giữa/cuối (contact sheet) kiểm tra crop & phụ đề trước khi gửi.

## 5. Định dạng báo cáo khi giao Shorts

Mỗi đợt giao, báo cáo theo mẫu sau (thiếu mục bản quyền/chất lượng là chưa xong):

```
SHORTS CUTTER — BÁO CÁO GIAO SHORTS
Nguồn: <tên/link/file video gốc> | Thời lượng gốc: <mm:ss>
Bản quyền: <của Hiệp tự sở hữu / được <ai> cho phép dùng, phạm vi … / ⚠️ chưa rõ — đã dừng>
Chế độ chạy: api (MuAPI) | local (Whisper <model> + LLM <provider/model>)

#1 <tên file Shorts, vd short_01.mp4>
   - Thời lượng: <s> | Đoạn gốc: <mm:ss → mm:ss>
   - Điểm viral (tool chấm): <0–100> | Hook: "<câu hook>"
   - Lý do chọn đoạn: <1 câu>
   - Check bản quyền: Đạt / vấn đề: <…>
   - Check chất lượng: hook 3s <Đạt/Chưa> · lời thoại <…> · khung dọc/mặt <…> ·
     phụ đề <…> · âm thanh <…> · đã tự soát <n> vòng
   - Ghi chú / điểm còn yếu: <…>

#2 … (tương tự)
Tổng: <N> Shorts đạt / <M> ứng viên bị loại (lý do ngắn)
Chờ Hiệp: duyệt đăng / sửa đoạn nào / bỏ đoạn nào
```

## 6. Thông tin còn cần từ Hiệp (hỏi trước lần chạy đầu tiên)

1. **Video dài đầu tiên**: link YouTube hoặc file MP4 + xác nhận bản quyền theo mục 4a.
2. **Số Shorts mong muốn** mỗi video (mặc định tool là 3).
3. **Style phụ đề**: có burn phụ đề không; nếu có — font (đề xuất Be Vietnam Pro theo brand),
   cỡ/màu/viền, vị trí, có highlight từ khoá không, phụ đề tiếng Việt hay song ngữ.
4. **Chế độ & API key**: dùng MuAPI (`MUAPI_API_KEY`, trả phí theo clip) hay local
   (cần `OPENAI_API_KEY` hoặc `GEMINI_API_KEY` cho bước highlight; Whisper/cắt chạy trên box).
   Shorts Cutter không tự tạo key, không chạy thử bằng key lạ.
5. (Tuỳ chọn) Kênh đích đăng Shorts (YouTube Shorts/TikTok/Reels) và có cần cover/tiêu đề/mô tả kèm theo không.

## 7. Trạng thái môi trường box (kiểm chứng 2026-10-19, giờ Asia/Saigon)

| Hạng mục | Kết quả |
|---|---|
| Python | 3.13.5 (`/usr/bin/python3`) — đạt yêu cầu ≥3.10 |
| ffmpeg / ffprobe | 7.1.5 — có sẵn |
| Ổ đĩa /workspace | 104G trống / 125G (18% đã dùng) — đủ cho video dài + output |
| RAM / CPU | 15 GiB RAM, 8 CPU — chạy faster-whisper CPU khả thi (model `base`/`small`) |
| Repo | đã clone tại `/workspace/AI-Youtube-Shorts-Generator`, commit `3d11f2e` |
| Venv smoke test | `.venv-smoke/` — chỉ cài core `requirements.txt` (requests, python-dotenv), **chưa** cài deps nặng của local mode (faster-whisper, opencv, yt-dlp, torch) |
| API keys | **chưa có** key nào (MuAPI/OpenAI/Gemini) — blocker chính |

### Smoke test đã chạy thật (không API key, không tốn phí)

- `python main.py --help` → in đúng usage/flags. ✅
- `from shorts_generator import generate_shorts` + test hàm `dedupe_highlights` thuần Python → import OK, dedupe hoạt động. ✅
- Chạy thử không key: dừng sạch với lỗi `MUAPI_API_KEY is not set` (đúng thiết kế, không crash lạ). ✅
- `ffmpeg -version` → 7.1.5. ✅
- **Chưa** test cắt video thật nào — chưa có video mẫu + chưa có key cho bước highlight. Không bịa kết quả.

### Lệnh chạy tham khảo (sau khi có key + video)

```bash
cd /workspace/AI-Youtube-Shorts-Generator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
# chỉ khi dùng local mode:
pip install -r requirements-local.txt

# Local mode với file của Hiệp (ưu tiên cho video tự sở hữu):
python main.py "/đường/dẫn/video.mp4" --mode local --num-clips 3 \
    --aspect-ratio 9:16 --language vi --output-json result.json
# → Shorts tại ./output/short_01.mp4 … (đổi qua LOCAL_OUTPUT_DIR trong .env)
```

