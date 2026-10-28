---
title: "AGENTS.md: cách AI làm việc trong repo này"
date: 2026-10-12
source: "oneup-studio (soạn trong repo)"
id: agents
type: guide
status: active
updated: 2026-10-28
tags: [agents, retrieval, workflow]
---
# AGENTS.md: cách AI làm việc trong repo này
Repo chứa toàn bộ hệ thống nội dung TikTok **@hi.oneup** (OneUp, Hiệp). Đọc theo thứ tự: file này → `INDEX.md` (bản đồ mọi file, id) → nguồn chuẩn liên quan.

## Nguồn chuẩn (không sao chép nội dung, chỉ trỏ tới)
| Cần gì | File chuẩn |
|---|---|
| Luật (id `rule-N` = mục N) | `rules/video-rules.md` |
| Lịch sử quyết định, góp ý (id `DL-NNN`) | `logs/decision-log.md`, **đọc trước mỗi clip** (rule-33) |
| Giọng nói của Hiệp | `content/voice-profile.md` (confirmed) · chuyện thật: `content/story-bank.md` |
| Brand (màu, font, logo, caption) | `brand/brand-tokens.json` (máy đọc), `brand/brand-index.md` (người đọc) |
| Thứ tự đăng + theme | `content/theme-map.md` |
| Cấu trúc repo, nơi lưu mọi file | **`docs/conventions/storage.md`** (nguồn duy nhất; README tóm tắt) |
| Một clip (id `clip-NN`) | đang làm `content/clips/clip-NN-<slug>/`, đã duyệt `content/archive/clip-NN-<slug>/` (luật 66): `final/` + `archive/` |
| Quy trình một video | `docs/workflow/per-video-pipeline.md` |
| Nhân vật (Hiệp, Omi) | `brand/characters/` (rig.py, sheets). Comic: `<clip>/comic/spec.json` → `pipeline/comic/render.py` |
| Video comic có chuyển động | `video-engine/` (README: setup, schema, lệnh `validate/plan/voice/render/frames`). Giọng nhân vật (F5-TTS: Hiệp "F5 · Thái Sơn", Omi "F5 · Mỹ Duyên", giọng mẫu `assets/voice-refs/`): `pipeline/scripts/voice-prosody.py` + `pipeline/tts/f5tts_gen.py` (rule-46, DL-035; giấy phép NC, Hiệp chấp nhận rủi ro). Ghép beat: `pipeline/scripts/join-beats.sh`. Mẫu tổng hợp: `content/samples/sample-full-w5/`. Profile nhân vật: `video-engine/src/characters/profiles/` |
| Storyboard | `storyboard/spec.json` là nguồn, PNG là kết quả render. Renderer: `pipeline/storyboard/render.py` |
| Trend | `research/trends/ingest.md` (thư viện sống) + `research/trends/YYYY-MM-DD/` |
| Quy trình | `pipeline/pipeline.md` |
| **Tìm kiếm (mặc định XERJ)** | `docs/conventions/search-xerj.md`: `xerj search --prefix oneup "..."` (repo) · `--prefix ref` (repo tham khảo, tra **trước khi viết code pipeline mới**) · index lại `pipeline/scripts/xerj-index.sh` · dự phòng `rg`/`git grep` |
| **Làm clip (bắt buộc, luật 48)** | `skills/make-video/SKILL.md` · build `pipeline/scripts/build-final.py` · lint `pipeline/scripts/check-rules.py` · mẫu `content/archive/clip-01-implementation-intention/final/` |
| Skill | `skills/<id>/SKILL.md` (`make-video`, `motion-picks-per-script`, `trend-digest`, `script-polish`, `humanizer` (vendored MIT), `hyperframes/*` (vendored Apache-2.0, 21 skill HyperFrames chính thức, đọc trước mọi beat giải thích)) |

## Quy ước
- Prompt bot nội dung của Hiệp: `docs/prompts/content-bot-prompt.md` (reuse-first, front-matter, commit `<loại>: <mô tả>`); ánh xạ ở `docs/conventions/storage.md`.
- Mọi file `.md` (trừ SKILL.md và tài liệu brand gốc) có front-matter `id, type, status, updated, tags`. Khi tạo hoặc đổi tên file, chạy `python3 pipeline/scripts/build-index.py`.
- Id ổn định: `rule-N`, `DL-NNN`, `clip-NN`, `clip-NN.bNN` (beat), `trends-YYYY-MM-DD`, `skill.<id>`. Không đổi id đã dùng.
- Không đưa media vào git: file lớn ở `media/` (gitignored, `MANIFEST.json`), giữ trên Mac bằng `pipeline/scripts/media-sync.py`. Không vendor repo ngoài (xem `resources/refs/README.md`).

## Workflow
1. **Clip mới:** theo `skills/make-video/SKILL.md` (intake → đọc nguồn → spec → humanizer → check-rules → gate 1 → render → check-rules --final → gate 2 → DL).
2. **Có góp ý (rule-36):** thêm `DL-NNN` → sửa nguồn (`spec.json` / `script.md` / renderer), **không tạo lại từ đầu** → thêm một dòng vào `revisions` trong spec → render lại → tự xem lại 2 vòng (rule-34) → commit `...(DL-NNN)` → push.
3. **Góp ý lặp lại từ 2 lần:** nâng thành luật hoặc skill, ghi vào decision-log. Retro mỗi Chủ nhật.

## Series format (DL-027)
Series @hi.oneup hiện tại **chỉ comic + motion graphics** (Remotion `video-engine/` + HyperFrames). Không shot list, không b-roll tự quay; Hiệp chỉ thu giọng. Không nhắc đăng (DL-028).

## Trend sync (rule-38, rule-47, rule-59: một nguồn duy nhất)
Mọi asset của @hi.oneup chỉ nằm trong repo này (DL-060, L-023). Không còn thư mục sync riêng.
1. Job hằng ngày chạy `skills/trend-digest` ngay trong `/workspace/oneup-studio` (box). Ghi thẳng vào `research/trends/{YYYY-MM-DD/,ingest.md,patterns.md}` và `content/idea-bank.md`, rồi `git add research/trends content/idea-bank.md && git commit -m "trends: YYYY-MM-DD digest"` (chỉ commit các path này).
2. Box không có quyền ghi GitHub: commit nằm trên box cho tới khi agent có Mac, rồi đẩy bằng bundle (`git bundle` → `split -b 9m` → CopyFromBox → trên Mac `git pull --ff-only <bundle> HEAD && git push origin main`).
3. Media lớn (>5MB audio/video) để ở `media/` (gitignored, không có git-lfs), liệt kê trong `media/MANIFEST.json` (path, size, sha256).
4. `python3 pipeline/scripts/check-assets.py` chặn khi còn file dự án nằm ngoài repo (`/workspace/oneup-studio-sync`, `/workspace/hi-oneup`, `/workspace/*.md` của dự án).
`/workspace/oneup-studio-sync` và `pipeline/scripts/sync-trends.sh` đã bỏ (deprecated).

## Đường dẫn máy
Repo trên Mac: `/Users/macbook/me/projects/oneup-studio` (machine I-Am-Focused). Bản clone trên box (nơi làm việc duy nhất, commit tại đây rồi đẩy qua Mac): `/workspace/oneup-studio`.
