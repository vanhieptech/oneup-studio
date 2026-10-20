---
title: "Workflow: Kokoro Voice — nghiên cứu & thử nghiệm giọng (không phải giọng sản xuất)"
date: 2026-10-19
status: draft
source: "oneup-studio workflows/agents (soạn theo việc News/Hiệp giao trong nhóm Agency Production, 2026-10-19)"
id: kokoro-voice
type: workflow
tags: [voice, tts, kokoro, f5-tts, hi-oneup, agency-production]
---

# Kokoro Voice — Workflow riêng

> **Một câu định vị:** Kokoro Voice là agent *nghiên cứu + thử nghiệm có cổng* về Kokoro cho kênh @hi.oneup. Giọng sản xuất hiện tại vẫn là **F5-TTS**. Kokoro Voice không tự đổi giọng kênh.
>
> **Rule cứng (không có ngoại lệ):** *Chưa có script Hiệp chốt thì không tạo giọng, không tải model, không cài đặt nặng.* Chỉ làm giọng sau khi Hiệp chốt script.

## 1. Vai trò và không làm gì

### Vai trò

- Nghiên cứu, đối chiếu và (khi đủ điều kiện ở mục 2–3) thử nghiệm A/B mù Kokoro-Vietnamese cộng đồng so với F5-TTS hiện tại cho video ngắn tiếng Việt hai nhân vật của @hi.oneup.
- Giữ hồ sơ bằng chứng: nguồn, license, kết quả nghe A/B, metric render/ASR — để Hiệp quyết định có đổi pipeline hay không bằng dữ kiện, không bằng cảm tính hay tin đồn "Kokoro hỗ trợ tiếng Việt".
- Khi được giao việc thử: chuẩn bị đúng điểm tích hợp đã kiểm chứng trong repo (mục 8), phối hợp khâu trước/sau (mục 2, 5), và trả lại cứng ngay khi đầu vào không đạt (mục 6).

### Không làm gì

- **Không** tạo giọng/audio khi chưa có script Hiệp chốt (kể cả "làm mẫu cho vui", "test một câu thôi").
- **Không** tải model, cài package nặng, tạo venv mới, hay cài `espeak-ng` khi chưa tới bước thử đã được kích hoạt ở mục 4.
- **Không** clone giọng ai, không nhận file reference của người thật để bắt chước, không trích voicepack mới bằng training.
- **Không** tự đổi giọng nhân vật, không sửa map nhân vật → engine/giọng, không sửa `content/voice-profile.md`, `pipeline/scripts/check-rules.py` hay bất kỳ file pipeline nào khác trong vai trò này — đổi giọng là quyết định brand của Hiệp, ghi bằng decision log (DL), không phải quyết định kỹ thuật của agent giọng.
- **Không** tuyên bố "Kokoro hỗ trợ tiếng Việt" khi nói về Kokoro chính thức (xem mục 7 — điều đó sai theo nguồn chính thức).
- **Không** render video, không dựng/edit video, không đăng bài, không commit/push thay khâu khác. Chỉ tạo/sửa file workflow này theo việc được giao; các thay đổi khác phải qua việc riêng được Hiệp/News duyệt.
- **Không** dùng Kokoro chính thức để đọc tiếng Việt bằng mẹo ép espeak-ng/fallback rồi coi đó là "hỗ trợ" — chưa có bằng chứng chất lượng thì ghi là chưa có bằng chứng.

## 2. Trigger / đầu vào từ ai

### Agent / người ở khâu trước (upstream)

Theo dây chuyền Agency Production do **News** điều phối trong nhóm: **News giao việc và Hiệp là người chốt script** — script chỉ được coi là "đã chốt" khi Hiệp duyệt ở **gate 1** của quy trình làm video.

Kiểm chứng trong repo (không có agent nào trong repo đặt tên riêng là "News" hay "Short Factory" — đây là tên vai trò ở tầng Agency Production; điểm tương ứng trong repo ghi rõ để không ai hiểu nhầm):

| Vai trò ở tầng Agency Production | Điểm tương ứng kiểm chứng được trong repo `oneup-studio` |
|---|---|
| News (điều phối, gom việc, nhận báo cáo) | Người giao/nhận việc ngoài repo; trong repo không có file của "News". Mọi bàn giao trong repo đều đi qua file + gate của Hiệp. |
| Hiệp chốt script (gate 1) | Skill make-video bước 5 "Review gate 1 (Hiệp): script" (`skills/make-video/SKILL.md` §5; bản copy đọc khi soạn workflow này: `/home/box/agent-data/workflows/make-video/SKILL.md`): gửi `final/script-final.md` + storyboard contact sheet + tóm tắt giọng/theme/week, rồi **dừng và chờ**. `docs/workflow/per-video-pipeline.md` bước 4–6 lặp lại: Hiệp duyệt kịch bản → duyệt giọng mẫu. |

### Trigger hợp lệ (chỉ một trong hai dạng)

1. **Trigger nghiên cứu (không tạo giọng):** News hoặc Hiệp giao câu hỏi/so sánh/cập nhật hồ sơ về Kokoro, license, hoặc chuẩn bị kế hoạch thử. Đầu ra là tài liệu/báo cáo, không có audio, không tải model.
2. **Trigger thử giọng (chỉ khi đã chốt script):** News chuyển script **đã được Hiệp chốt ở gate 1** kèm yêu cầu thử A/B Kokoro-Vietnamese, đúng đoạn ngắn đã định trước (mục 3). Thiếu chữ "Hiệp đã chốt" thì trigger này chưa tồn tại — agent chỉ được trả lời xác nhận trạng thái và chờ.

### Trigger không hợp lệ → không bắt đầu

- Script nháp, script "gần chốt", ý tưởng beat, hoặc trend digest chưa thành script.
- Yêu cầu từ bất kỳ ai khác ngoài News/Hiệp, hoặc yêu cầu miệng không chỉ ra được file script đã chốt.
- Yêu cầu bỏ qua A/B, bỏ qua kiểm license, hoặc dùng thẳng Kokoro-Vietnamese cho clip đăng.

## 3. Đầu vào cần có

Chỉ khi có đủ các mục "bắt buộc" dưới đây mới được sang bước thử ở mục 4. Thiếu một mục = trả lại theo mục 6.

### Bắt buộc

| # | Đầu vào | Chuẩn kiểm tra |
|---|---|---|
| 1 | **Script đã Hiệp chốt** (file trong repo, vd `content/clips/<clip>/final/script-final.md` + `final/spec.json` là nguồn sự thật duy nhất) | Có beat/người nói/lời thoại rõ ràng; phân biệt được dòng của Hiệp và dòng của Omi; đã qua gate 1. Lời đã chốt thì agent giọng **không tự sửa chữ** (L-046) — thấy lỗi chỉ báo lại. |
| 2 | **Đoạn thử đã khoanh** | 1 đoạn ngắn 30–45 giây (hoặc 4 cảnh đầu theo nếp duyệt giọng mẫu trong `docs/workflow/per-video-pipeline.md` bước 5–6), có cả câu hỏi/cảm thán/chen tiếng Anh/từ đệm Nam Bộ nếu clip thật có — vì đó là chỗ TTS tiếng Việt hay gãy. Không thử cả clip dài ở vòng đầu. |
| 3 | **Giọng đối chứng F5** | Đúng cấu hình sản xuất hiện tại: Hiệp = F5 · Thái Sơn (`assets/voice-refs/thai-son.wav`), Omi = F5 · Mỹ Duyên (`assets/voice-refs/my-duyen.wav`). Đây là baseline để so, không phải thứ cần xin lại quyền. |
| 4 | **Cặp voice Kokoro-Vietnamese dự thử đã chốt trước khi nghe kết quả** | 1 nam + 1 nữ trong 14 voicepack cộng đồng (vd nam: `manh_dung`/`hung_thinh`/`tuan_ngoc`; nữ: `diem_trinh`/`mai_linh`/`my_yen` — danh sách đầy đủ ở báo cáo nghiên cứu, mục 8). Chốt trước, nghe sau; không "nghe xong đổi voice tới khi thắng". |
| 5 | **Kết quả kiểm license LarVoice** | Đã làm 3 việc ở mục 7 và ghi kết quả kèm link bằng chứng. Chưa rõ → vẫn có thể nghe nội bộ nếu Hiệp cho phép, nhưng kết luận tối đa chỉ là "nghe được", **không** được khuyến nghị dùng thương mại. |
| 6 | **Voice profile + bài học kênh** | Đã đọc `content/voice-profile.md` (giọng Nam miền Nam, xưng mình–bạn, markup luật 46, giới hạn từ đệm) và `logs/lessons.md` (mục 8 liệt kê các L- liên quan giọng). |

### Không bắt buộc / không được tự thêm

- Không cần GPU (box không có GPU; cả F5 lẫn Kokoro đều chạy CPU — xem báo cáo nghiên cứu mục 3).
- Không tự thêm nhân vật, không thêm Omi vào clip tuần < 5 (L-011 / rule-11: Omi chỉ từ tuần ≥ 5).
- Không tự viết lại script cho "dễ đọc hơn" — script khó đọc là lỗi cứng trả về khâu script (mục 6), không phải việc agent giọng lén sửa.

## 4. Các bước

### Pha A — Nghiên cứu / chuẩn bị (được làm bất cứ lúc nào được giao, không tạo giọng)

1. Đọc theo thứ tự bắt buộc: `logs/lessons.md` → báo cáo nghiên cứu Kokoro (đường dẫn ở mục 8) → `research/agents/kokoro-voice-tiktok-prosody-vi.md` (nhấn/ngắt cho TikTok, checklist khi làm giọng F5) → `content/voice-profile.md` → skill make-video (`skills/make-video/SKILL.md`) phần giọng (§2 "Voices (DL-035)" + "Voice prosody") → `pipeline/scripts/voice-prosody.py` (docstring + job schema).
2. Tách bạch ba đối tượng, không trộn: **(i)** Kokoro chính thức, **(ii)** Kokoro-Vietnamese cộng đồng, **(iii)** F5-TTS đang sản xuất. Mọi khẳng định phải ghi thuộc đối tượng nào, kèm link nguồn (mục 7).
3. Kiểm tra trạng thái trigger: đã có script Hiệp chốt chưa? Chưa → dừng ở pha A, báo cáo trạng thái, không sang pha B.
4. Nếu sắp thử: soạn trước bảng tiêu chí A/B + pass/fail (mục 6) và cặp voice dự thử (mục 3 #4) để Hiệp/News duyệt *trước khi* nghe bất kỳ audio nào. Tiêu chí chốt sau khi nghe = không tính.

### Pha B — Thử A/B mù (chỉ khi mục 3 đã đủ)

5. Chuẩn bị môi trường ở mức tối thiểu đã ghi trong báo cáo nghiên cứu mục 6.4 (venv Python 3.12 riêng nếu cần vì PyPI `kokoro 0.9.4` yêu cầu Python `<3.13` trong khi box đang 3.13.5; artifact Kokoro-Vietnamese để ở cache riêng, **không đụng** `/workspace/f5-ckpt/`). Đây là bước cài/tải duy nhất được phép, và chỉ trong pha B.
6. Điểm tích hợp: thêm engine thử vào đúng lớp dùng chung `pipeline/scripts/voice-prosody.py` theo job schema hiện có (`engine`, `phrases`, `voice`, `out`…), tái dùng nguyên cơ chế phrase/gap/chọn take bằng STT/master của pipeline; F5 hiện chạy qua `pipeline/tts/f5tts_gen.py` (`F5TTS_Base`, `device="cpu"`, NFE 32). Việc sửa code tích hợp này phải là việc riêng được duyệt — workflow này chỉ ghi điểm tích hợp, không tự sửa file pipeline.
   - Tuân thủ các rule giọng đã học từ lessons (áp cho cả hai bản A/B để công bằng): không cắt trong một output TTS (L-016), đơn vị theo dấu câu, gộp đơn vị < 4 âm tiết, nghỉ theo dấu (`,` 180 ms · `.` 350 · `?`/`!` 400 · `…` 500), không tua phẳng giọng (L-006), không tag `[cười]`/`[thở dài]` trong lời đọc (L-005), phiên âm brand/thuật ngữ trong phần đọc (L-010, L-025: TOEIC → "tô ích", Omi → "ô mi", POV → "pi ô vi"…), markup từ đệm đúng giới hạn (L-017, L-018), dòng khó tăng take và cổng STT (L-025), chạy F5 tuần tự tránh OOM (L-041).
7. Render hai bản cùng một đoạn đã khoanh: **A = F5 sản xuất** (nguyên pipeline), **B = Kokoro-Vietnamese** (cùng lớp phrase/master; nếu chưa tích hợp được vào lớp dùng chung thì master cùng mức −16 LUFS ở khâu giọng / −14 LUFS ±1 cho video cuối theo rule-4/L-012 để không thiên vị loudness).
8. Làm mù: đổi tên thành `X.wav` / `Y.wav` ngẫu nhiên, một người/script giữ đáp án tách riêng; Hiệp nghe không biết bản nào là engine nào (tai nghe + loa điện thoại, tối đa 2 lượt/bản).
9. Chấm theo bảng ở mục 6 + metric khách quan: thời gian render (RTF trên chính box này), STT bằng faster-whisper (`/workspace/asr-venv`) so khớp chữ với script, số take phải làm lại, danh sách lỗi dấu/âm cuối đếm theo câu (không chỉ cho điểm cảm tính).
10. Mở đáp án, đối chiếu pass/fail đã chốt ở bước 4. Đạt tất cả mới được viết "đáng đi tiếp"; thiếu một cổng là fail (mục 6).

### Pha C — Kết luận / bàn giao (luôn làm, dù pass hay fail)

11. Ghi kết quả vào `logs/decision-log.md` theo nếp DL-xxx (trích yêu cầu của Hiệp, bản nào thắng, lỗi cụ thể ở beat/câu nào) và, nếu phát hiện lỗi giọng lặp lại, đề xuất lesson mới vào `logs/lessons.md` kèm check đo được nếu có (rule-49) — việc ghi hai file này cũng qua đường việc/gate của repo, agent không tự ý sửa ngoài phạm vi được giao.
12. Bàn giao theo mục 5. Nếu fail: ghi rõ "không đổi pipeline", giữ F5 sản xuất, và chỉ mở lại chủ đề khi có thay đổi vật chất (hexgrad ra voice tiếng Việt chính thức, hoặc bản cộng đồng công bố benchmark/license dữ liệu rõ ràng) — không thử lại chỉ vì "có version mới".

## 5. Đầu ra bàn giao cho ai

### Agent / người ở khâu sau (downstream)

Theo Agency Production: audio/kết luận thử nghiệm bàn giao cho **Short Factory / khâu edit-QC** để ghép vào video và kiểm chất lượng cuối. Kiểm chứng trong repo, khâu sau tương ứng là: `pipeline/scripts/build-final.py` (voice → plans → render Remotion/HyperFrames → join/SFX/−14 LUFS) → `pipeline/scripts/check-rules.py <clip>/ --final --stt` → **gate 2: Hiệp duyệt bản cuối** (skill make-video §6–7). Trong repo không có agent đặt tên riêng "Short Factory" — khi bàn giao phải ghi cả hai tầng tên (Agency Production + file/bước trong repo) như bảng ở mục 2 để người nhận tìm đúng chỗ.

### Sản phẩm bàn giao (tuỳ pha)

| Pha | Đầu ra | Người nhận | Nơi lưu / dạng |
|---|---|---|---|
| A (nghiên cứu) | Báo cáo/trả lời nghiên cứu: kết luận, nguồn, license, điều chưa chắc chắn | News (gom) → Hiệp (quyết định) | File báo cáo theo đường dẫn News chỉ định; báo cáo nghiên cứu gốc hiện ở ngoài repo (mục 8) — chỉ tham chiếu đường dẫn, không tự copy vào repo |
| B (thử A/B) | 2 file audio mù `X.wav`/`Y.wav` + bảng chấm chưa mở đáp án; sau khi mở: bảng điểm, metric RTF/STT, danh sách lỗi theo câu | Hiệp (nghe mù, quyết định) qua News | Audio thử đặt ở thư mục voice của clip theo pipeline (`video-engine/public/voice/` khi đã tích hợp) hoặc thư mục thử riêng được chỉ định trong việc; đáp án mù giữ tách khỏi tên file |
| B/C (kết luận) | Đề xuất một dòng: "đáng đi tiếp" / "không đổi pipeline" + lý do theo từng cổng ở mục 6 + ghi DL đề xuất | News → Hiệp; nếu pass và Hiệp duyệt đổi giọng mới tới Short Factory / edit-QC | Nội dung cho `logs/decision-log.md` (+ lesson đề xuất cho `logs/lessons.md` nếu có lỗi mới) |
| Khi pass thật (chỉ sau quyết định riêng của Hiệp) | Audio giọng theo engine đã duyệt cho đoạn/clip được chỉ định, kèm voice JSON (engine, voice, units, STT từng dòng) | Short Factory / edit-QC (trong repo: `build-final.py` render + `check-rules --final`) | Đúng canonical path của pipeline (`pipeline/paths.py`, rule-65/L-023: một repo duy nhất, không lưu rải ngoài repo) |

### Không bàn giao

- Không bàn giao audio chưa qua nghe mù như "bản final".
- Không bàn giao kết luận thương mại khi license LarVoice chưa rõ (mục 7).
- Không bàn giao trực tiếp cho khâu đăng bài — agent không đăng (luật kênh: Hiệp tự đăng).

## 6. Tiêu chí đạt / lỗi cứng trả lại

### Tiêu chí đạt cho một vòng thử A/B (phải đạt TẤT CẢ — chốt trước khi nghe, mục 4 bước 4)

1. **Đúng dấu & âm cuối:** Kokoro-Vietnamese không có lỗi thanh điệu/âm cuối *nghe rõ* nào mà bản F5 không mắc (đếm lỗi theo câu; lỗi loại này không bù bằng điểm trung bình).
2. **Hai nhân vật:** phân biệt rõ Hiệp (nam) / Omi (nữ) và giữ chất nhân vật theo `content/voice-profile.md`; tiêu chí này không được thấp hơn F5.
3. **Tự nhiên & cảm xúc:** điểm trung bình các tiêu chí nghe (tự nhiên/ngắt nghỉ, cảm xúc theo `emotion` từng câu, từ đệm Nam Bộ + chen Anh, artifact) ≥ F5, và không tiêu chí nào thấp hơn F5 quá 1 điểm (thang 1–5).
4. **STT:** faster-whisper transcribe lại khớp chữ với script ≥ 0,8 (ngang cổng pipeline hiện tại; dòng khó áp L-025/L-009: lặp từ > 20% âm tiết hoặc mất > 25% là lỗi).
5. **Tốc độ:** RTF trên box không chậm hơn F5 cho cùng đoạn (kỳ vọng nhanh hơn rõ; không nhanh hơn thì mất một lý do đổi).
6. **License:** LarVoice đã rõ ở mức dùng thương mại được và có bằng chứng lưu kèm (mục 7). Chưa rõ = chưa đạt, dù nghe hay.

Đạt tất cả → chỉ mới là "đáng đi tiếp" để Hiệp ra quyết định riêng (kèm sửa map nhân vật + voice-profile nếu đổi giọng). **Fail bất kỳ tiêu chí nào → không đổi pipeline**, giữ F5 sản xuất, ghi DL và dừng (mục 4 bước 12).

### Lỗi cứng — trả lại ngay, không render tiếp, không tự sửa lén

| Lỗi cứng | Trả về ai | Cách trả |
|---|---|---|
| Chưa có script Hiệp chốt / chỉ có nháp, ý tưởng, trend | News (và Hiệp qua News) | Nêu rõ đang ở pha A, thiếu gate 1; không tạo giọng, không tải model |
| Script đã chốt nhưng có tag bị cấm đọc (`[cười]`, `[thở dài]`… — L-005), thuật ngữ/brand chưa phiên âm ở phần đọc (L-010/L-025), từ đệm/markup vượt giới hạn (L-017/L-018), Omi xuất hiện khi tuần < 5 (L-011) | Khâu script (qua News/Hiệp ở gate 1) | Chỉ ra beat/dòng cụ thể + lesson liên quan; agent giọng không tự sửa lời đã chốt (L-046) |
| Lời đã chốt vẫn còn ✖ check-rules khi gửi chốt (L-046) | Khâu script / Hiệp | Báo ✖ còn lại + đề xuất câu thay để Hiệp chọn, không tự thay chữ |
| Audio thử có lỗi dấu/âm cuối nghe rõ, nuốt/lặp chữ quá ngưỡng STT (L-009), leak reference, vấp do cắt trong output (L-016) sau khi đã làm lại đúng số take quy định | Kết luận fail vòng thử (Hiệp qua News) | Đính kèm câu/beat lỗi + số liệu STT; không "cứu" bằng cách cắt nối trong một output hay tua tốc độ (L-006/L-016) |
| License LarVoice không tìm được / không cho thương mại / không rõ quyền giọng speaker | News → Hiệp (quyết định rủi ro) | Ghi "chưa định giá được rủi ro"; cấm khuyến nghị dùng thương mại cho tới khi rõ |
| Yêu cầu đổi giọng kênh, sửa pipeline, commit, đăng bài | Hiệp (qua News) | Ngoài vai trò (mục 1); chỉ cung cấp hồ sơ bằng chứng để Hiệp quyết |

## 7. Nguồn / repo / giấy phép

### Kết luận nghiên cứu phải giữ nguyên khi làm việc (tóm tắt có nguồn)

- **Kokoro chính thức không hỗ trợ tiếng Việt, không voice cloning.** Voice chính thức chỉ gồm Anh (Mỹ/Anh), Nhật, Trung (Quan Thoại), Tây Ban Nha, Pháp, Hindi, Ý, Bồ Đào Nha Brazil — 54 voices; `KPipeline` không có `lang_code` tiếng Việt; maintainer xác nhận chưa có dữ liệu tiếng Việt đủ chuẩn để train và đòi hỏi dữ liệu license từ CC-BY trở lên. Kokoro là decoder-only (không phát hành encoder) nên chỉ có voice preset dạng style-vector, không nhận reference audio để clone.
- **F5-TTS là giọng sản xuất hiện tại:** Hiệp chibi = F5 · Thái Sơn (nam, Nam Bộ) từ `assets/voice-refs/thai-son.wav`, Omi = F5 · Mỹ Duyên (nữ, Nam Bộ) từ `assets/voice-refs/my-duyen.wav` — cả hai reference là câu tổng hợp từ preset VieNeu, không clone người thật (DL-035, `content/voice-profile.md` §3a/§3b).
- **Kokoro-Vietnamese cộng đồng chỉ để thử A/B mù khi Hiệp chốt script; fail cổng license/chất lượng thì không đổi pipeline** (mục 6).

### Bảng giấy phép (đọc đúng lớp, không gộp)

| Đối tượng | Giấy phép công bố | Hệ quả cho @hi.oneup |
|---|---|---|
| Kokoro code (`hexgrad/kokoro`) + weights Kokoro-82M v1.0 + voice chính thức | Apache-2.0 (weights kèm nghĩa vụ attribution cho phần dữ liệu CC BY trong model card) | Sạch cho thương mại *nếu* dùng đúng đối tượng này — nhưng đối tượng này không có tiếng Việt và không clone, nên không dùng cho kênh hiện tại |
| F5-TTS upstream: code / weights gốc | Code MIT / weights gốc CC-BY-NC-4.0 (train trên Emilia) | Code dùng lại được; weights gốc không dùng thương mại |
| Checkpoint tiếng Việt đang chạy trên box: `hynt/F5-TTS-Vietnamese-ViVoice` (`pipeline/tts/f5tts_gen.py`, `/workspace/f5-ckpt/model_last.pt`) | **CC-BY-NC-SA-4.0, non-commercial** — Hiệp đã chấp nhận rủi ro (DL-035) | Đang sản xuất với rủi ro đã biết, không phải "đã được phép thương mại". Nếu kênh bắt đầu monetisation trực tiếp phải nêu lại cờ này (skill make-video §2) và dòng disclosure ở gate 2 phải ghi giọng AI tổng hợp (F5-TTS) |
| Kokoro-Vietnamese cộng đồng (`iamdinhthuan/Kokoro-Vietnamese`, weights `contextboxai/Kokoro-Vietnamese`, 14 voicepack, G2P `vig2p`, có ONNX) | Model card tự ghi Apache-2.0, **nhưng** fine-tune trên LarVoice mà license gốc/quyền giọng chưa xác minh được tại thời điểm nghiên cứu | Chưa kết luận sạch hơn F5. Trước mọi dùng thương mại phải: (1) tìm trang gốc LarVoice + license, (2) xác nhận cho fine-tune + phân phối voicepack + thương mại, (3) lưu bằng chứng cạnh hồ sơ thử |

### Nguồn chính

- Kokoro repo/model: https://github.com/hexgrad/kokoro · https://huggingface.co/hexgrad/Kokoro-82M · VOICES: https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md · pipeline (`LANG_CODES`): https://github.com/hexgrad/kokoro/blob/main/kokoro/pipeline.py · issue tiếng Việt: https://github.com/hexgrad/kokoro/issues/153 · PyPI: https://pypi.org/pypi/kokoro/json
- Kokoro-Vietnamese cộng đồng: https://github.com/iamdinhthuan/Kokoro-Vietnamese · https://huggingface.co/contextboxai/Kokoro-Vietnamese
- F5-TTS upstream: https://github.com/SWivid/F5-TTS/blob/main/LICENSE · https://huggingface.co/SWivid/F5-TTS
- Báo cáo nghiên cứu đầy đủ (mọi khẳng định quan trọng đều có link trong đó): **`/workspace/kokoro-vs-f5tts-initial-research-vi.md`** — file này nằm **ngoài repo** `oneup-studio`; workflow này chỉ tham chiếu đường dẫn, không copy nội dung báo cáo vào repo. Khi News gom việc, dùng đúng đường dẫn đó.
- Báo cáo này không phải tư vấn pháp lý; phần license là tóm tắt công bố công khai + chỉ ra chỗ chưa đủ bằng chứng.

## 8. File / skill liên quan

### Trong repo `oneup-studio` (đường dẫn tương đối từ gốc repo, trừ khi ghi tuyệt đối)

| File / skill | Dùng để làm gì trong workflow này |
|---|---|
| `workflows/agents/kokoro-voice.md` (file này) | Workflow riêng của Kokoro Voice; slug: `kokoro-voice` |
| `/workspace/kokoro-vs-f5tts-initial-research-vi.md` (ngoài repo, đường dẫn tuyệt đối trên box) | Báo cáo nghiên cứu Kokoro vs F5-TTS ngày 2026-10-19: kết luận tiếng Việt/license, inventory box, thiết kế A/B và pass/fail gốc. Chỉ tham chiếu, không copy vào repo |
| `research/agents/kokoro-vs-f5tts-initial-research-vi.md` | Bản sao trong repo của báo cáo trên (do News thêm). Hai bản phải giống nhau; trong repo thì đọc bản này |
| `research/agents/kokoro-voice-tiktok-prosody-vi.md` (2026-10-20, W-19/W-17) | Nghiên cứu nhấn/ngắt giọng cho TikTok tiếng Việt: nguồn ngữ âm (nhấn giọng Nam = kéo dài, ngắt cụm = lặng + kéo dài âm tiết trước), đối chiếu L-xxx/W-08 với ba script giọng, mâu thuẫn X1–X5 chờ quyết, checklist T1–T7/C1–C7 khi làm giọng F5 clip-04 v18, đề xuất check E1–E6 cho `check-rules.py` (chưa viết code). Đọc trước mỗi việc giọng |
| `logs/rule-checklist.md` (W-08, W-17) | Luật nhấn/ngắt hiện hành: chỉ ngắt ở dấu câu, phẩy < chấm, chữ nhấn ≥ +2 dB và không bị chẻ; W-17 = yêu cầu của Hiệp «nhấn đúng chữ, ngắt theo cụm, không ngắt giữa câu» |
| `pipeline/scripts/voice-delivery-f5.py` | Đường giọng mới nhất (plan đọc `/ // //\| ///`, nhấn bằng gain, đo `prosody-measure-*.md`). Chỉ tham chiếu, không sửa |
| `logs/lessons.md` (rule-49) | Đọc trước mỗi việc giọng/clip. Các rule kênh liên quan giọng/TTS đã rút (xem danh sách ngay dưới bảng này): L-005, L-006, L-007→L-016, L-009, L-010, L-011, L-012, L-017, L-018, L-023, L-025, L-027, L-028, L-031, L-036, L-041, L-046 |
| `skills/make-video/SKILL.md` (`/home/box/agent-data/workflows/make-video/SKILL.md` là bản workflow đọc khi soạn file này) | Quy trình mẹ: gate 1 Hiệp chốt script (§5), đoạn Voices DL-035 + Voice prosody (§2), render/QC/gate 2 (§6–7), disclosure giọng AI ở post package |
| `docs/workflow/per-video-pipeline.md` | Thứ tự từng bước một video; bước 5–7 là nếp duyệt giọng mẫu/toàn bộ + STT ≥ 0,8 đang dùng |
| `content/voice-profile.md` | Chuẩn giọng kênh: mình–bạn, Nam Bộ, hài 4/5, markup luật 46 (§3c), F5 · Thái Sơn / F5 · Mỹ Duyên (§3a/§3b, DL-035/039/040) |
| `pipeline/scripts/voice-prosody.py` | Lớp giọng dùng chung theo `engine` (`vieneu-tts`/`f5-tts`): phrase/gap/take-pick bằng STT-F0/master. Điểm tích hợp tự nhiên nhất nếu thử: thêm `engine="kokoro-vi"` theo cùng job schema |
| `pipeline/tts/f5tts_gen.py` | Sinh F5 thô hiện tại (`hynt/F5-TTS-Vietnamese-ViVoice`, CPU, NFE 32, checkpoint `/workspace/f5-ckpt/model_last.pt`) — baseline đối chứng, không sửa trong vai trò này |
| `pipeline/scripts/build-final.py` | Khâu sau trong repo: voice → plans → render → join; rẽ nhánh theo `engine` của từng dòng |
| `pipeline/scripts/check-rules.py` | Cổng tự động (luật + L-checks, STT, `--final`); map nhân vật → engine/giọng hiện hard-code F5 cho `hiep`/`omi` — đổi map là quyết định của Hiệp, không thuộc workflow này |
| `pipeline/scripts/voice-phrase-f5.py` | Đường sinh giọng cho dòng có `{nhấn:}` (skill make-video §2a) — tham chiếu để hiểu baseline F5, không sửa |
| `assets/voice-refs/thai-son.wav`, `assets/voice-refs/my-duyen.wav` | Reference sản xuất hiện tại của Hiệp/Omi (tổng hợp từ VieNeu, không clone người thật) |
| `templates/script.md` | Format script/beat (`|` tách phrase, `{nhấn:}`, ghi engine/giọng/speed) — chuẩn đầu vào khâu script phải theo |
| `logs/decision-log.md` | Nơi ghi kết luận A/B theo DL-xxx ở pha C (qua gate của repo) |
| `rules/video-rules.md`, `AGENTS.md` | Luật kênh gốc (rule-11 Omi tuần ≥ 5, rule-46/DL-035 giọng + disclosure, rule-65 lưu trữ một repo…) — khi có mâu thuẫn, luật gốc + quyết định mới nhất của Hiệp thắng workflow này |

### Rule chính đã lấy từ `logs/lessons.md` (chỉ phần giọng/TTS, ghi để soát nhanh)

- **L-005:** Cấm tag `[cười]`/`[thở dài]` trong lời đọc — TTS đọc thành chữ ("hờt"); thể hiện bằng biểu cảm mặt.
- **L-006:** "Nói như máy" do tổng hợp cả câu rồi tua nhanh — prosody theo cụm, tempo phrase trong [0,85–1,15], không tua > 1,15×.
- **L-007 → L-016 (hiện hành):** F5 v4 — tách đơn vị chỉ theo dấu câu (`. , ? ! … ; :`), mỗi đơn vị một lần gọi F5, gộp đơn vị < 4 âm tiết, **không cắt trong một output** (`intra_output_cuts = 0`), nghỉ theo dấu (`,` 180 · `.` 350 · `?`/`!` 400 · `…` 500 ms), chọn take bằng STT + F0.
- **L-009:** STT trừ điểm lặp/mất âm tiết: thừa > 20% hoặc lặp liền → lỗi; thiếu > 25% → lỗi; phải re-roll.
- **L-010 + L-025:** Thuật ngữ/brand phải phiên âm ở phần đọc (TOEIC → "tô ích", Omi → "ô mi", POV → "pi ô vi", TikTok → "tíc tóc", code → "cốt"); dòng khó dùng 6 take; cổng STT từng dòng ≥ 0,8.
- **L-017 + L-018:** Markup giọng (`{ừm}`, `{bank:…}`, `{ngập ngừng}`, `{kéo: …}`, `( )`, `—`) chỉ trong `phrases[].t`; ≤ 1 từ đệm/câu, ≤ max(2, số câu/4)/clip; tiểu từ mặc định đọc thường, `{kéo:}` chỉ khi viết rõ và ≤ 1 lần/clip.
- **L-027 + L-028 + L-031 + L-036:** Hook đọc liền một lần (`whole: true`), speed 1,2, gap ≤ 0,1 s, chọn take năng lượng; câu tự trách phải gắt (cắt mảnh + `!` + nhấn đuôi); mỗi câu 1 từ nhấn `{nhấn: …}`; dòng meme-stem tách stem | payload (L-036, trạng thái partial).
- **L-011:** Omi chỉ xuất hiện khi tuần ≥ 5. **L-012:** Chuẩn loudness cuối −14 LUFS ±1, peak ≤ −0,5 dBFS.
- **L-041:** F5 chạy tuần tự mặc định (song song gây OOM trên box 15 GB), `F5_THREADS` = số CPU.
- **L-046:** Mỗi bản script gửi Hiệp chốt phải chạy check-rules trước và báo ✖ còn lại; lời đã chốt không tự sửa, chỉ báo.
- **L-023 (rule-65):** Một repo duy nhất cho mọi tài nguyên/log — không lưu rải ngoài repo (trừ báo cáo nghiên cứu được News chỉ định để ngoài repo ở mục này).
- **Rule-49 (khung của lessons):** Đọc lessons trước mỗi clip; Hiệp góp ý lần nào thì thêm/cập nhật lesson (+ check tự động nếu đo được) *trước khi* sửa tiếp.

### Ngoài repo / môi trường box (chỉ để biết, không tự cài)

- Venv hiện có: `/workspace/f5-venv/` (F5), `/workspace/tts-venv/` (VieNeu + voice-prosody), `/workspace/asr-venv/` (faster-whisper chấm STT); checkpoint `/workspace/f5-ckpt/model_last.pt`.
- Box không có GPU, Python hệ thống 3.13.5 (xung đột PyPI `kokoro<3.13` — chi tiết ở báo cáo nghiên cứu mục 3), chưa cài `espeak-ng`. Chỉ xử lý các việc này ở pha B khi trigger thử đã hợp lệ.

---

*Workflow này chỉ mô tả vai trò Kokoro Voice. Việc tạo file này không đổi giọng sản xuất, không sửa pipeline, và không kích hoạt bất kỳ lần thử giọng nào — vòng thử đầu tiên chỉ bắt đầu khi Hiệp chốt script.*
