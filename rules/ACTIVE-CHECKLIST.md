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
- Trình duyệt / dịch vụ web (`DL-083`): **luôn mặc định dùng `/ego-browser`** (`~/.local/bin/ego-browser`, `EGO_BROWSER_BIN` trong `pipeline/paths.py`; chạy `ego-browser skill` để lấy hướng dẫn khớp phiên bản) cho mọi tác vụ web/service web, ưu tiên hơn built-in browser hoặc tự dựng Playwright/Puppeteer.
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

## 3b. Script (Content Engine v2.0, `DL-082`): Ideate → Multi-Script Arena → Emotional Wave → Reviewer (một nguồn: `docs/prompts/writer-hi-oneup.md`)
Thứ tự cố định, trùng 100% với `skills/make-video/SKILL.md` §2 và `gate0.py` (`DL-076`..`DL-082`). **Trước Chốt chỉ text** (script + bảng khung mạch + Hình/Caption EN/nhấn + gợi ý giọng F5 dạng chữ); spec/TTS/render là sau Chốt.
1. **Gate 0 — Khớp đảo chiều Hot Trend (`ideate-clip.py` / `trend-match.py`, F2 & F6):** chạy `python3 pipeline/scripts/ideate-clip.py --clip <clip-slug>` kiểm độ tươi Radar (< 48h) và lấy Top 3 cặp `(Trend tươi < 72h ↔ Bài học chưa làm)` theo *Agile Slot Swap* giữ `LIGHT/DARK ≤ 2` (hoặc *Pain-Wave Fallback* từ `audience-pain-bank.md`, không ép meme gượng). Nạp brief bằng `gate0.py --idea "<ý>" [--archetype M1..M5] [--arc auto|ARC-NNN]`. Chốt **1 câu hỏi trung tâm** (Single-Point Alignment) và khóa **Fact-lock** (số/từ CẤM). **Không** nhúng `style-pairs.md` hay bảng blacklist vào Pha 1.
1b. **Đấu trường Đa Kịch Bản (`script-arena.py`, F3 — khuyên dùng):** từ cùng 1 Fact-lock, chạy `script-arena.py prepare --idea "<ý>" --out-dir <clip>/archive/arena --archetypes M1,M2,M4` để 3 Pure-Voice Writers viết song song 3 phương pháp khác màu (`M1 Everyday Paradox` · `M2 5-Second Vulnerable Story` · `M3 Misconception Flip` · `M4 Self-Dialogue & Roleplay` · `M5 Micro-Experiment`) → `script-arena.py score` + Reviewer chế độ **Tournament Judge** chọn **Top 1 + 1 Á quân khác màu cảm xúc** trình Hiệp ở Gate 1.
2. **Gate 0.5 Hook Arena:** 4 góc (Pain-Mirror · Counter-Intuitive · In-Media-Res · Self-Mocking Story), đọc thành tiếng, Top 1. **Luật 3 Giây Rõ Nghĩa:** `b01` ≤ 20 âm tiết (1–2 câu cực ngắn); người lạ nghe 3 giây đầu hiểu ngay chủ đề và thấy chuyện của mình. Không chấm bằng `cadence-patterns.tsv` / `ai-blacklist.tsv`.
3. **Bảng khung mạch + Đường cong Cảm xúc 6 nhịp (`L-107`, `DL-082`):** mỗi beat 1 câu vai trò nhân quả kèm sắc thái cảm xúc (`Hook Spark → Vulnerability Dip bắt buộc ở nửa đầu → Curiosity → Aha Peak → Catharsis → Warm Peer CTA`).
4. **Độc thoại 2 Pha (`DL-079`, `DL-081`):** **Pha 1 (Pure Voice)** chỉ mở 4 đầu vào sạch, không mở bảng cấm, viết liền một hơi có ngữ khí mở lời trực diện, *Storytelling the Study*, *Climactic Order* (`18 → 254 ngày, hơn 8 tháng`), *Given–New Conceptual Flow* (cấm điệp từ cơ học *Anadiplosis*), và **CTA đối thoại thật** (đồng cảm «ai bị giống mình» + lắng nghe góc nhìn/cách vượt qua; cấm ép «comment 1 chữ» & cấm khảo sát xã giao sáo rỗng). **Pha 2 (Surgical Audit)** chỉ sửa vi phẫu chỗ chạm Fact-lock/ngân sách âm tiết, giữ nguyên hồn khẩu ngữ.
5. **Số bằng chữ số** trong nháp; cách đọc (`say`) chỉ khi dựng spec sau Chốt.
6. **Tách beat + `Hình:` / `EN:` / `{nhấn:}` (text).**
7. **Cổng tự kiểm Ngữ nghĩa tiếng Việt bản địa + Chống văn dịch + tự mâu thuẫn:** (a) người miền Nam có nói cụm này không · (b) ẩn dụ đúng vật lý/chủ ngữ không · (c) mốc thời gian/số giữa beat khớp không · (d) câu nào gượng/nhại chỉ để qua checker.
8. **Kiểm máy + Reviewer:** `check-rules.py --draft <draft.md>` (**0 ✖**) + `audio-precheck.py <draft.md>` (kiểm tốc độ 2.6–3.4 syl/s, hơi dài > 32, `HOOK_LONG`/`SLOW_ENTRY`/`BEAT_BLOAT`, cộng **`FLAT_CADENCE`**, **`MISSING_VULNERABILITY_DIP`** và **`VOICE_REF_MAP`** `thai-son-v2/serious/happy`); **bắt buộc** Reviewer độc lập khác model (`docs/prompts/reviewer-script.md`) rồi `check-rules.py --review <draft.md>` PASS trước khi trình Hiệp. Sau mỗi clip chạy `golden-sync.py sync-feedback --clip <clip>` nạp bài học vào `review-golden`.
- **Review 2 tầng:** Tầng 1 chặn cứng chỉ `H1` fact không nguồn hoặc chạm danh sách CẤM của `fact_lock` · `H2` ≥ 300s · `H3` sai format kênh / chê người xem · `H4` lỗi cấu trúc. Tầng 2 **Pairwise A/B** (hoặc **Tournament Judge** cho 3 bản đấu trường) với bản duyệt cùng kênh + chủ đề; xuất `HARD_FAILS / PAIRWISE (WIN|TIE|LOSE) / TOP_FIXES / CONFLICTS / VERDICT`. Verdict do `pipeline/review_tiers.py` tính lại.
- **3-Pass polish** (`skills/script-polish`): chỉ sau khi độc thoại đã có; không thêm câu chỉ để có «anchor», không nhồi liên từ, không nhại chữ.
- **Gate 2 Multimodal Video QA (`rule-34`, sau render):** `python3 pipeline/scripts/gate2-qa.py <clip>/` (skill `video-qa`) → `<clip>/final/gate2-qa-report.md`.

## 3c. Trend v5.1+ (`DL-082`, `DL-084`): Global EN + VN Radar v2 → 7-Block Viral DNA + Localization → Synthesis
- `pipeline/scripts/radar-fetch.py [--lang en|vi]` (yt-dlp local, **5 nhóm `role`** trong `pipeline/trends/radar.yaml`: **`global_niche_source`** — 11 kênh tiếng Anh chất lượng cao như Better Ideas, Matt D'Avella, Huberman Lab, Kurzgesagt, HealthyGamerGG, Psych2Go, Thomas Frank, Nathaniel Drew, Ali Abdaal, 3Blue1Brown, t3dotgg đi trước TikTok VN 3–6 tháng · `direct_niche` · `southern_story_voice` · `cross_niche_craft` · `anti_pattern`, gắn `format_compatibility` & `lang`; bổ sung `views_per_day` + `engagement_intensity` bắt kênh lớn khi `followers = 0`; trích Top Comments → `research/trends/<date>/audience-language.md`) → `trend-streams.py radar|upstream|inbox|queue`.
- `teardown.py … --queue-id …` → Viral DNA Card **7 khối** (`gemini-teardown.md` v2: có `emotional_arc`, `spoken_pivots`, `format_compatibility` và **`localization_vi`** chuyển bối cảnh Mỹ/Âu sang đời thường VN, chống văn dịch word-by-word; tự đẩy nỗi đau comment vào `resources/vn-spoken/audience-pain-bank.md`), gộp `ARC-NNN` và đẩy ý vào `content/idea-bank.md`. Video `.mp4` trong inbox chạy `learn-from-channel.py --file <mp4>` (bóc lời bằng `faster-whisper` local + kéo mẫu chuyển ý vào `gate0.py`).
- **Tổng hợp đa video & Khớp đảo chiều Song ngữ EN ↔ VN:** `pattern-synthesize.py` → `weekly-synthesis.json` + `trend-match.py` khớp cả Trend tiếng Anh lẫn tiếng Việt tươi (< 72h) × `theme-map.md` (gắn nhãn `EN→VN Localize` để Writer Việt hóa hoàn toàn).
- Khép vòng hiệu suất & bộ nhớ tự học: `python3 pipeline/arc_library.py sync-published` + `python3 pipeline/scripts/golden-sync.py sync-3d` (tính `win_rate` 3 chiều Archetype × Hook × CTA) + `golden-sync.py sync-feedback --clip <clip>`.

## 4. Cổng kho & CI trước khi commit
- `python3 pipeline/scripts/check-assets.py` → phải **0 violations** (layout, front-matter, trùng file, trùng ID, media mới > 2 MB, `INDEX.md`).
- `python3 -m pytest -q tests/` (hoặc `python3 -m unittest discover -s tests`) `&& python3 -m unittest discover -s pipeline/tests`
- Khi sửa `video-engine/`: `cd video-engine && npm run typecheck && npm test`
- Bật hook tự kiểm local 1 lần: `bash pipeline/scripts/install-hooks.sh`
