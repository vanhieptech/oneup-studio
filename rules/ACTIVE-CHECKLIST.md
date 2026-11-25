---
title: "Active Checklist: Tóm tắt luật đang hiệu lực (2 kênh, local Mac)"
date: 2026-11-25
type: rules
tags: [rules, checklist, onboarding, active]
status: ready
source: "oneup-studio (chưng cất từ rules/video-rules.md, logs/decision-log.md, logs/lessons.md)"
id: rules-active-checklist
updated: 2026-11-25
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
- **Độ dài (`L-099`, thay rule-4/7/61 cũ):** strict **< 300s** tính cả end card/nghỉ/xfade; **120–180s** chỉ là mục tiêu/cảnh báo. Không quota từ cứng, không tăng tốc giọng để nhét.
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

## 4. Cổng kho & CI trước khi commit
- `python3 pipeline/scripts/check-assets.py` → phải **0 violations** (layout, front-matter, trùng file, trùng ID, media mới > 2 MB, `INDEX.md`).
- `python3 -m unittest discover -s tests && python3 -m unittest discover -s pipeline/tests`
- Khi sửa `video-engine/`: `cd video-engine && npm run typecheck && npm test`
- Bật hook tự kiểm local 1 lần: `bash pipeline/scripts/install-hooks.sh`
