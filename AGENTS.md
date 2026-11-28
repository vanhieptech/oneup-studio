---
title: "AGENTS.md: cách AI làm việc trong repo này"
date: 2026-10-12
source: "oneup-studio (soạn trong repo)"
id: agents
type: guide
status: active
updated: 2026-11-27
tags: [agents, retrieval, workflow]
---
# AGENTS.md: cách AI làm việc trong repo này
Repo chứa toàn bộ hệ thống nội dung TikTok **@hi.oneup** (OneUp, Hiệp). Đọc theo thứ tự: file này → `INDEX.md` (bản đồ mọi file, id) → nguồn chuẩn liên quan.

## Dual-channel
| Kênh | Thư mục | Luật / skill |
|---|---|---|
| **@hi.oneup** (comic + motion) | `content/clips/`, `skills/make-video/` | file này + `rules/video-rules.md` + DL-027 |
| **@vanhiep.tech** (talking-head + explainer overlay) | `channels/vanhiep-tech/` | **`channels/vanhiep-tech/AGENTS.md`** + `make-layer` + `make-capcut-draft` |

Khi user nói về `@vanhiep.tech`, CapCut A-roll, layer overlay/cutaway, hoặc `vht-YYYYMMDD-*`: **không** chạy `make-video` comic / không áp DL-027 shot-list ban — đọc AGENTS kênh trước.

## Nguồn chuẩn (không sao chép nội dung, chỉ trỏ tới)
| Cần gì | File chuẩn |
|---|---|
| **Tóm tắt nhanh đang hiệu lực (đọc trước)** | `rules/ACTIVE-CHECKLIST.md` (2 kênh, local Mac, đã bỏ luật cũ bị ghi đè) |
| Luật đầy đủ (id `rule-N` = mục N) | `rules/video-rules.md` |
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
| **Tìm kiếm (mặc định XERJ)** | `docs/conventions/search-xerj.md`: `xerj search --prefix work-oneup-studio "..."` (repo; prefix lấy từ `.xerj-prefix`) · `--prefix ref` (repo tham khảo, tra **trước khi viết code pipeline mới**) · index lại `pipeline/scripts/xerj-index.sh` · dự phòng `rg`/`git grep` |
| **Trình duyệt / service web (mặc định `/ego-browser`, DL-083)** | Luôn ưu tiên dùng skill `/ego-browser` (`ego-browser` CLI tại `~/.local/bin/ego-browser`, `EGO_BROWSER_BIN` trong `pipeline/paths.py`; chạy `ego-browser skill` trước khi thao tác) cho mọi tác vụ mở web, tương tác dịch vụ web, đăng nhập, lấy dữ liệu web cần trình duyệt, và QA/preview UI — không dùng built-in browser hay tự mở Playwright/Puppeteer |
| **Làm clip (bắt buộc, luật 48)** | `skills/make-video/SKILL.md` (v2.0) · khởi tạo `pipeline/scripts/ideate-clip.py` (`trend-match.py` + `script-arena.py`) · build `pipeline/scripts/build-final.py` · lint `pipeline/scripts/check-rules.py` + `audio-precheck.py` · bộ nhớ `golden-sync.py` · mẫu `content/archive/clip-01-implementation-intention/final/` |
| Skill | `skills/<id>/SKILL.md` (`make-video`, `social-poster` (link → nháp X/LinkedIn, không tự đăng), `motion-picks-per-script`, `trend-digest`, `script-polish`, `humanizer` (vendored MIT), `motionmaxxing` (symlink → `resources/refs/motionmaxxing/`, Apache-2.0 craft + measured eases; Remotion ports `video-engine/src/composition/motionmaxxing/`), `hyperframes/*` (vendored Apache-2.0, 21 skill HyperFrames chính thức, đọc trước mọi beat giải thích)) |

## Quy ước
- Prompt bot nội dung của Hiệp: `docs/prompts/content-bot-prompt.md` (reuse-first, front-matter, commit `<loại>: <mô tả>`); ánh xạ ở `docs/conventions/storage.md`.
- Mọi file `.md` (trừ SKILL.md và tài liệu brand gốc) có front-matter `id, type, status, updated, tags`. Khi tạo hoặc đổi tên file, chạy `python3 pipeline/scripts/build-index.py`.
- Id ổn định: `rule-N`, `DL-NNN`, `clip-NN`, `clip-NN.bNN` (beat), `trends-YYYY-MM-DD`, `skill.<id>`. Không đổi id đã dùng.
- Không đưa media vào git: file lớn ở `media/` (gitignored, `MANIFEST.json`), giữ trên Mac bằng `pipeline/scripts/media-sync.py`. Không vendor repo ngoài (xem `resources/refs/README.md`).

## Workflow
1. **Clip mới:** theo `skills/make-video/SKILL.md` v2.0 (`ideate-clip.py` bắt trend <72h → Gate 0 + Fact-lock → Đấu trường 3 kịch bản `script-arena.py` → `audio-precheck.py` + `check-rules.py --draft` → Reviewer Tournament Judge → Gate 1 → Chốt → render → `check-rules --final` → Gate 2 → `golden-sync.py` → DL).
2. **Có góp ý (rule-36):** thêm `DL-NNN` → sửa nguồn (`spec.json` / `script.md` / renderer), **không tạo lại từ đầu** → thêm một dòng vào `revisions` trong spec → render lại → tự xem lại 2 vòng (rule-34) → commit `...(DL-NNN)` → push.
3. **Góp ý lặp lại từ 2 lần:** nâng thành luật hoặc skill, ghi vào decision-log. Retro mỗi Chủ nhật.
4. **Hoàn thành mọi tác vụ (bắt buộc):** sau khi sửa xong code/tài liệu và chạy qua các cổng kiểm tra (`build-index.py`, `check-assets.py`, `pytest`), **luôn tự động `git add`, `git commit` (theo mẫu `<loại>: <mô tả>`) và `git push` lên `origin/main`** mà không chờ nhắc.

## Series format (DL-027)
Series @hi.oneup hiện tại **chỉ comic + motion graphics** (Remotion `video-engine/` + HyperFrames). Không shot list, không b-roll tự quay; Hiệp chỉ thu giọng. Không nhắc đăng (DL-028).

## Trend sync (rule-38, rule-47, rule-59: một nguồn duy nhất — local Mac)
Mọi asset của @hi.oneup chỉ nằm trong repo local này (gốc repo = `git rev-parse --show-toplevel`, DL-060, L-023). Không có box hay thư mục sync riêng.
1. Job hằng ngày chạy `skills/trend-digest` trực tiếp trong repo local. Ghi thẳng vào `research/trends/{YYYY-MM-DD/,ingest.md,patterns.md}` và `content/idea-bank.md`, rồi `git add research/trends content/idea-bank.md && git commit -m "trends: YYYY-MM-DD digest"`.
2. Media lớn (>2MB audio/video) để ở `media/` (gitignored, không có git-lfs), liệt kê trong `media/MANIFEST.json` (path, size, sha256) và kiểm bằng `python3 pipeline/scripts/media-sync.py verify`.
3. `python3 pipeline/scripts/check-assets.py` kiểm layout clip, front-matter, trùng nội dung, trùng ID (`DL-NNN`/`L-NNN`), và media mới >2MB.
4. Cài pre-commit hook local một lần: `bash pipeline/scripts/install-hooks.sh`.

## Đường dẫn máy
Không ghi cứng đường dẫn tuyệt đối của repo: mọi lệnh chạy từ gốc repo (`cd "$(git rev-parse --show-toplevel)"`), mọi đường dẫn trong tài liệu là tương đối với gốc repo. Checkout chính hiện ở Mac của Hiệp, nhưng repo có thể nằm ở thư mục khác (git worktree, máy khác). Toolchain ngoài repo: `$ONEUP_TOOLS_DIR` (mặc định `~/oneup-tools/`), tự nhận qua `pipeline/paths.py`; kiểm bằng `bash pipeline/scripts/env-check.sh`.

## Agent skills

### Issue tracker

Issues live in this repo's GitHub Issues (via `gh`). See `docs/agents/issue-tracker.md`.

### Domain docs

Single-context: root `GLOSSARY.md` + `docs/adr/`. See `docs/agents/domain.md`.

