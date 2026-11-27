---
title: "Active Checklist: Tóm tắt luật đang hiệu lực (2 kênh, local Mac)"
date: 2026-11-25
type: rules
tags: [rules, checklist, onboarding, active]
status: ready
source: "oneup-studio (chưng cất từ rules/video-rules.md, logs/decision-log.md, logs/lessons.md)"
id: rules-active-checklist
updated: 2026-11-27
---
# Active Checklist — Tóm tắt nhanh cho agent (đọc trước khi làm)

Tài liệu gốc vẫn là `rules/video-rules.md`, `logs/decision-log.md`, `logs/lessons.md`. File này gom ngắn gọn **các quy tắc đang có hiệu lực** để tránh áp nhầm luật cũ đã bị ghi đè.

## 1. Môi trường local Mac
- Repo duy nhất: `/Users/macbook/work/oneup-studio` · Toolchain: `~/oneup-tools/` (tự nhận qua `pipeline/paths.py`, **không** dùng `/workspace/`).
- F5-TTS: mặc định chạy **Apple Silicon MPS** (`F5_DEVICE=auto`) với checkpoint **`f5-ckpt-6000h`** + `vocos-mel-24khz` (CC-BY-NC-SA, Hiệp chấp nhận rủi ro `DL-035`).
- HyperFrames: version chuẩn trong `pipeline/versions.json` (`0.9.94`).
- Media > 2 MB: để trong `media/` + `media/MANIFEST.json` (`python3 pipeline/scripts/media-sync.py verify`).
- Cấp số ID mới trước khi ghi log: `python3 pipeline/scripts/next-id.py` (không tự đoán `DL-NNN`/`L-NNN`).

## 2. Kênh `@hi.oneup` (Comic + Motion, `DL-027`)
- **Format:** 100% comic (Remotion `video-engine/`) + motion explainer (HyperFrames). Không quay mặt/b-roll, không nhạc nền (`rule-21`), không nhắc lịch đăng (`DL-028`), bắt buộc nhãn AI giọng (`rule-46`).
- **Độ dài (`L-099`, thay rule-4/7/61 cũ):** strict **< 300s** tính cả end card/nghỉ/xfade; mục tiêu **60–180s**. Clip cô đọng 60–119s không bị cảnh báo. Câu chuyện đã đủ ý thì dừng, không kéo chữ cho tới 120s. Không quota từ cứng, không tăng tốc giọng để nhét.
- **Tách cổng lời vs cổng hình (`L-098`):** **KHÔNG** sinh voice, ảnh, still preview hay render trước khi Hiệp **"Chốt"** đúng bản lời.
- **Nội dung & lời thoại:**
  - Kể chuyện tự nhiên giọng miền Nam như nói với bạn thân (`L-103`, `L-104`, `L-105`), không văn chương/báo cáo trong 2 câu đầu hook; không lấy môn học làm ví dụ (`L-087`); cấm cụm chê năng lực người học (`L-053`).
  - Có dẫn chứng thật (tác giả + năm/PMID/DOI) lồng vào chuyện (`L-088`, `L-096`), gắn trend/hook pattern từ `research/trends/` (`L-090`, `L-100`).
  - Mỗi câu 1 từ nhấn `{nhấn: …}` (`L-031`/`L-036`); EN caption chia chunk **≤ 8 từ** (`L-051`); câu hỏi kết bằng thanh huyền/nặng **không** ép nâng pitch (`L-082`); Whisper luôn `float32` (`L-079`); không phạt tốc độ > 5 âm tiết/s (`L-074`).
- **Render & QA:**
  - Chạy draft QA 1 lệnh: `python3 pipeline/scripts/check-rules.py --draft <script.md>`.
  - Render nháp nhanh: `python3 pipeline/scripts/build-final.py <spec.json> --draft` (`540×960`, scene cache tự động).
  - Bản final: `INTER_CRF = 10` cho beat trung gian, `CRF 20` bản cuối (`bt709`, `tv`), âm lượng tuyến tính **−14 LUFS** + `alimiter=0.78` (`DL-072`), `check-rules.py <clip> --final`.
  - Lưu trữ (`rule-66`): chỉ chuyển sang `content/archive/` khi đủ gói đăng + Hiệp nói `"duyệt"` + có `final/approved.json`.

## 3. Kênh `@vanhiep.tech` (Talking-head + CapCut layers)
- Đọc `channels/vanhiep-tech/AGENTS.md` + `PLAN.md` + `brand/frame.md` (không áp luật comic `@hi.oneup`).
- Màu One Dark chỉ dùng `var(--vht-*)` từ `brand/tokens.css`; cấm hồng/magenta; cấm `box-shadow`/`text-shadow`/`blur`/`backdrop-filter` trên `ov-*` (`DL-069`).
- `ov-*` xuất ProRes alpha `.mov` (`yuva*`); `cu-*` xuất `.mp4` nền đặc trên main track CapCut; `hard-scrim` (`opacity: 0.82`) ôm sát cluster với safe zone `T220 / B≥380 / L56 / R≥100`, `min-height ≥ 520` (`DL-070`, `DL-071`).
- Build + cache + kiểm alpha 1 lệnh:
  - `python3 channels/vanhiep-tech/scripts/build-layers.py channels/vanhiep-tech/clips/<clip-id>`
  - Hoặc chỉ kiểm QA: `python3 channels/vanhiep-tech/scripts/check-layer.py channels/vanhiep-tech/clips/<clip-id>`

## 3b. Script: Gate 0 → Hook Arena → Khung mạch → độc thoại → tự kiểm → Reviewer (một nguồn: `docs/prompts/writer-hi-oneup.md`)
Thứ tự cố định, trùng 100% với `skills/make-video/SKILL.md` §2 và `gate0.py` (DL-076). **Trước Chốt chỉ text** (script + bảng khung mạch + Hình/Caption EN/nhấn dạng chữ); spec/TTS/render là sau Chốt.
1. **Gate 0:** `python3 pipeline/scripts/gate0.py --idea "<ý>" [--channel vht] [--memo <transcript>] --out <draft.md>` in brief gồm: ý + fact package, mạch `ONEUP-CORE-ARC` (khung mặc định ~65–88s, đủ ý thì dừng; `--extended` 120–180s chỉ khi nhiều bước kỹ thuật thật), dòng `story-bank.md` khớp, nhắc `voice-profile.md` §2 (miền Nam nhất quán, cấm trộn «ấy/thế/nhé» với «hông/nha», gia vị tự giễu/lời nội tâm/từ EN/callback chỉ chọn 1–2 thứ thật tự nhiên; **Ngân sách nguyên liệu** chống nhồi), 5 bản đã duyệt `a-c01…a-c05` kèm DNA mỗi bản (2–3 bản gần nhất được gắn dấu), góp ý mới nhất. Chốt **1 câu hỏi trung tâm** (Single-Point Alignment: hook và bằng chứng là câu hỏi và câu trả lời của cùng câu đó) và khóa **Fact-lock** (số/từ CẤM, không bịa cơ chế ngoài nguồn). **Không** nhúng `style-pairs.md` hay bảng blacklist vào bước viết.
2. **Gate 0.5 Hook Arena:** 4 góc (Pain-Mirror · Counter-Intuitive · In-Media-Res · Self-Mocking Story), đọc thành tiếng, Top 1. **Luật 3 Giây Rõ Nghĩa:** `b01` ≤ 20 âm tiết (1–2 câu cực ngắn); người lạ nghe 3 giây đầu hiểu ngay chủ đề và thấy chuyện của mình. Trong Hook Arena, rõ nghĩa và trúng nỗi đau trong 3s luôn thắng việc tránh trùng dạng câu hỏi với clip trước. Không chấm bằng `cadence-patterns.tsv` / `ai-blacklist.tsv`.
3. **Bảng khung mạch (L-107) trước khi viết lời:** mỗi beat một câu vai trò, đọc ra mạch nhân quả liền, không nhảy cảnh, không tự mâu thuẫn mốc thời gian.
4. **Độc thoại một hơi như kể bạn thân miền Nam;** chỉ 4 đầu vào sạch: brief · `voice-profile.md` §2–3 · 2–3 bản duyệt gần nhất · story-bank + `research/explainers/<topic>.md`. Không mở `bookish/ai-blacklist/connectors.tsv`.
5. **Số bằng chữ số** trong nháp; cách đọc (`say`) chỉ khi dựng spec sau Chốt.
6. **Tách beat + `Hình:` / `EN:` / `{nhấn:}` (text).**
7. **Cổng tự kiểm Ngữ nghĩa tiếng Việt bản địa + Chống văn dịch + tự mâu thuẫn:** (a) người miền Nam có nói cụm này không · (b) ẩn dụ đúng vật lý/chủ ngữ không · (c) mốc thời gian/số giữa beat khớp không · (d) câu nào gượng/nhại chỉ để qua checker.
8. **Kiểm máy + Reviewer:** `check-rules.py --draft <draft.md>` (**0 ✖**; ✖ chỉ cho H1 `L-088`/`L-096` nguồn, H2 ước ≥ 300s, H3 `L-053`, H4 cấu trúc beat, `L-087`; mọi style `choppy/flow/link/repeat/clarity/bookish/ai-structure/connector-stuffing` chỉ ⚠, không hàn câu hay nhại chữ để xoá ⚠) + `audio-precheck.py`; **bắt buộc** Reviewer độc lập ở subagent khác model (`docs/prompts/reviewer-script.md`) rồi `check-rules.py --review <draft.md>` PASS (cần `final/feedback.md` đủ góp ý, `review.md` khớp `script_hash`) trước khi trình Hiệp.
- **Review 2 tầng:** Tầng 1 chặn cứng chỉ `H1` fact không nguồn hoặc chạm danh sách CẤM của `fact_lock` · `H2` ≥ 300s · `H3` sai format kênh / chê người xem · `H4` lỗi cấu trúc. Tầng 2 **Pairwise A/B** với bản duyệt cùng kênh + chủ đề, kèm các điểm mù (gồm điểm mù 5: sai ngữ nghĩa tiếng Việt / văn dịch / tự mâu thuẫn) và DNA kênh; xuất `HARD_FAILS / PAIRWISE (WIN|TIE|LOSE) / TOP_FIXES / CONFLICTS / VERDICT`. Verdict do `pipeline/review_tiers.py` tính lại.
- **3-Pass polish** (`skills/script-polish`): chỉ sau khi độc thoại đã có; không thêm câu chỉ để có «anchor», không nhồi liên từ, không nhại chữ.
- **Audio-Back QA:** `python3 pipeline/scripts/audio-precheck.py <draft.md>` kiểm nhịp nói (2.6–3.4 âm tiết/s); cảnh báo câu > 32 âm tiết không dấu ngắt, trùng mở đầu 2 beat liên tiếp, và `HOOK_LONG` (b01 > 22) · `SLOW_ENTRY` (b01+b02 > 65) · `BEAT_BLOAT` (beat > 45 âm tiết). **Luật Chống Nhồi Nhét:** 1 vấn đề · 1 câu hỏi · 1 ví dụ đại chúng (tập thể dục, đọc sách, dậy sớm, học tiếng Anh…, không chuyện ngách) · dẫn chứng ≤ 2 câu (≤ 35 âm tiết) · rào giới hạn ≤ 1 vế ngắn (clip-02 «Mới thấy đi chung thôi», clip-05 «Nhưng năm mấy chục cũng đâu phải nhớ hết»). 6–7 beat, ~200–265 âm tiết, `b01+b02` ≤ 65, không beat nào > 45. **Đủ ý & Khép vòng:** số lớn đã nêu phải dịch nghĩa cho người nghe (254 ngày → «hơn 8 tháng»); trend và nghiên cứu có câu dẫn mượt từ beat trước, không nhảy cóc; phần cách làm có 1 đổi thước đo + 1 hành động cụ thể rồi khép vòng về nỗi lo ở Hook; cụt ý < 60s là lỗi như nhồi nhét. Gia vị giọng Hiệp (tự giễu, lời nội tâm, từ EN, callback) chọn tối đa 1–2 thứ thật tự nhiên. Cấm tuyệt đối chuyển cảnh giả để chèn trend («đúng lúc đó mình lướt trúng câu đang trend…») và callback phi thực tế («đánh răng xong thì đăng đại một video»); trend nếu dùng là xương sống ngay Hook, gãy mạch thì xin ngoại lệ như DL-069.  `--audition-hook` khi Hiệp muốn nghe thử 20s đầu.
- **Gate 2 Multimodal Video QA (`rule-34`, sau render):** `python3 pipeline/scripts/gate2-qa.py <clip>/` (skill `video-qa`) → `<clip>/final/gate2-qa-report.md`.

## 3c. Trend v5+: Multi-Channel Radar → 7-Block Viral DNA → Synthesis + Feedback Loop
- `pipeline/scripts/radar-fetch.py` (yt-dlp local, 3 nhóm `role` trong `pipeline/trends/radar.yaml`: `direct_niche`, `cross_niche_craft`, `anti_pattern`; trích Top Comments → `research/trends/<date>/audience-language.md`) → `trend-streams.py radar|upstream|inbox|queue`.
- `teardown.py … --queue-id …` → Viral DNA Card **7 khối** (thêm Khối 7 Craft & Voice Transfer, tự đẩy nỗi đau comment vào `resources/vn-spoken/audience-pain-bank.md`), gộp `ARC-NNN` và đẩy ý vào `content/idea-bank.md`.
- **Tổng hợp đa video:** khi có ≥ 3 teardown mới, chạy `python3 pipeline/scripts/pattern-synthesize.py` → `research/trends/weekly-synthesis.md` + `weekly-synthesis.json` (tự động cập nhật trọng số ưu tiên cho `gate0.py`).
- Khép vòng hiệu suất sau đăng: `python3 pipeline/arc_library.py sync-published` đọc `content/published/` → cập nhật `uses`, `wins`, `win_rate` cho `ARC-NNN`.

## 4. Cổng kho & CI trước khi commit
- `python3 pipeline/scripts/check-assets.py` → phải **0 violations** (layout, front-matter, trùng file, trùng ID, media mới > 2 MB, `INDEX.md`).
- `python3 -m pytest -q tests/` (hoặc `python3 -m unittest discover -s tests`) `&& python3 -m unittest discover -s pipeline/tests`
- Khi sửa `video-engine/`: `cd video-engine && npm run typecheck && npm test`
- Bật hook tự kiểm local 1 lần: `bash pipeline/scripts/install-hooks.sh`
