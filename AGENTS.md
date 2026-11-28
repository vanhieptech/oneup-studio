---
title: "AGENTS.md: cách AI làm việc trong repo này"
date: 2026-10-12
source: "oneup-studio (soạn trong repo)"
id: agents
type: guide
status: active
updated: 2026-11-28
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
| **Làm clip (bắt buộc, luật 48)** | `skills/make-video/SKILL.md` (v3.0, `DL-094`) · khởi tạo `ideate-clip.py` (`trend-match.py` + `script-arena.py`; `--fast` bỏ arena) · sau Chốt: `storyboard.yaml` → `spec-compile.py` → `build-final.py --preview` rồi full · lint `check-rules.py` + `audio-precheck.py` · `golden-sync.py` · mẫu `templates/storyboard.yaml` + `content/archive/clip-01-…/final/` |
| Skill | `skills/<id>/SKILL.md` (`make-video`, `social-poster` (link → nháp X/LinkedIn, không tự đăng), `motion-picks-per-script`, `trend-digest`, `script-polish`, `humanizer` (vendored MIT), `motionmaxxing` (symlink → `resources/refs/motionmaxxing/`, Apache-2.0 craft + measured eases; Remotion ports `video-engine/src/composition/motionmaxxing/`), `hyperframes/*` (vendored Apache-2.0, 21 skill HyperFrames chính thức, đọc trước mọi beat giải thích)) |

## Quy ước
- Prompt bot nội dung của Hiệp: `docs/prompts/content-bot-prompt.md` (reuse-first, front-matter, commit `<loại>: <mô tả>`); ánh xạ ở `docs/conventions/storage.md`.
- Mọi file `.md` (trừ SKILL.md và tài liệu brand gốc) có front-matter `id, type, status, updated, tags`. Khi tạo hoặc đổi tên file, chạy `python3 pipeline/scripts/build-index.py`.
- Id ổn định: `rule-N`, `DL-NNN`, `clip-NN`, `clip-NN.bNN` (beat), `trends-YYYY-MM-DD`, `skill.<id>`. Không đổi id đã dùng.
- Không đưa media vào git: file lớn ở `media/` (gitignored, `MANIFEST.json`), giữ trên Mac bằng `pipeline/scripts/media-sync.py`. Không vendor repo ngoài (xem `resources/refs/README.md`).

## Workflow
1. **Clip mới:** theo `skills/make-video/SKILL.md` v3.0 (`ideate-clip.py` bắt trend <72h → Gate 0 + Fact-lock → Đấu trường 3 kịch bản `script-arena.py` trừ `--fast` → `audio-precheck.py` + `check-rules.py --draft` → Reviewer → Gate 1 → Chốt → `storyboard.yaml` → `spec-compile.py` → `build-final.py --preview` → Gate 2 QA preview → full render → `check-rules --final` → `golden-sync.py` → DL).
2. **Có góp ý (rule-36):** thêm `DL-NNN` → sửa nguồn (`spec.json` / `script.md` / renderer), **không tạo lại từ đầu** → thêm một dòng vào `revisions` trong spec → render lại → tự xem lại 2 vòng (rule-34) → commit `...(DL-NNN)` → push.
3. **Góp ý lặp lại từ 2 lần:** nâng thành luật hoặc skill, ghi vào decision-log. Retro mỗi Chủ nhật.
4. **Hoàn thành mọi tác vụ (bắt buộc):** sau khi sửa xong code/tài liệu, chạy `python3 pipeline/scripts/build-index.py` rồi cổng kiểm tra chung `bash pipeline/scripts/preflight.sh` (check-assets + unittest + video-engine typecheck/vitest; cùng nội dung với pre-commit hook), rồi **tự động `git add`, `git commit` (theo mẫu `<loại>: <mô tả>`) và `git push` lên `origin/main`** mà không chờ nhắc. **Ngoại lệ Grok (OneUp bot):** Grok commit bình thường nhưng **chỉ push khi Hiệp yêu cầu** (áp dụng cả bước push ở mục 2).

## Series format (DL-027)
Series @hi.oneup hiện tại **chỉ comic + motion graphics** (Remotion `video-engine/` + HyperFrames). Không shot list, không b-roll tự quay; Hiệp chỉ thu giọng. Không nhắc đăng (DL-028).

## Trend sync (rule-38, rule-47, rule-59: một nguồn duy nhất — local Mac)
Mọi asset của @hi.oneup chỉ nằm trong repo local này (gốc repo = `git rev-parse --show-toplevel`, DL-060, L-023). Không có box hay thư mục sync riêng.
1. Job hằng ngày chạy `skills/trend-digest` trực tiếp trong repo local. Ghi thẳng vào `research/trends/{YYYY-MM-DD/,ingest.md,patterns.md}` và `content/idea-bank.md`, rồi `git add research/trends content/idea-bank.md && git commit -m "trends: YYYY-MM-DD digest"`.
2. Media lớn (>2MB audio/video) để ở `media/` (gitignored, không có git-lfs), liệt kê trong `media/MANIFEST.json` (path, size, sha256) và kiểm bằng `python3 pipeline/scripts/media-sync.py verify`.
3. `python3 pipeline/scripts/check-assets.py` kiểm layout clip, front-matter, trùng nội dung, trùng ID (`DL-NNN`/`L-NNN`), và media mới >2MB.
4. Cài pre-commit hook local một lần: `bash pipeline/scripts/install-hooks.sh` (hook chỉ gọi `pipeline/scripts/preflight.sh --staged`). Agent không có hook thì chạy tay `bash pipeline/scripts/preflight.sh` trước khi commit.

## Đường dẫn máy
Không ghi cứng đường dẫn tuyệt đối của repo: mọi lệnh chạy từ gốc repo (`cd "$(git rev-parse --show-toplevel)"`), mọi đường dẫn trong tài liệu là tương đối với gốc repo. Checkout chính hiện ở Mac của Hiệp, nhưng repo có thể nằm ở thư mục khác (git worktree, máy khác). Toolchain ngoài repo: `$ONEUP_TOOLS_DIR` (mặc định `~/oneup-tools/`), tự nhận qua `pipeline/paths.py`; kiểm bằng `bash pipeline/scripts/env-check.sh`.

## Agent skills

### Issue tracker

Issues live in this repo's GitHub Issues (via `gh`). See `docs/agents/issue-tracker.md`.

### Domain docs

Single-context: root `GLOSSARY.md` + `docs/adr/` **chưa tồn tại** (tạo khi thật sự cần, xem `docs/agents/domain.md`: thiếu thì bỏ qua, không báo). Hiện thuật ngữ và quyết định nằm ở `rules/video-rules.md` (`rule-N`), `logs/decision-log.md` (`DL-NNN`), `logs/lessons.md` (`L-NNN`).

## Agent setup (Claude Code · Antigravity · Cursor · Grok): một nguồn duy nhất
Mọi agent đọc cùng một bộ luật; file riêng của từng agent chỉ là lớp mỏng trỏ về đây, không chép nội dung.

| Agent | Điểm vào | Skill (đều là symlink tới nguồn) | Cổng kiểm tra |
|---|---|---|---|
| Grok (OneUp bot) | `AGENTS.md` (file này) | đọc `docs/agents/skills-index.md` → `SKILL.md` | chạy tay `preflight.sh` (không có hook) |
| Claude Code | `CLAUDE.md` (`@AGENTS.md`) | `.claude/skills/` | pre-commit hook → `preflight.sh` |
| Antigravity | `AGENTS.md`, `GEMINI.md` | `.agents/skills/` | pre-commit hook → `preflight.sh` |
| Cursor | `AGENTS.md`, `.cursor/rules/oneup.mdc` | `.cursor/skills/` | pre-commit hook → `preflight.sh` |

- **Nguồn skill:** `skills/<id>/`, `skills/hyperframes/<id>/`, `channels/vanhiep-tech/skills/<id>/`. Danh mục: `docs/agents/skills-index.md`. Thêm skill mới → thêm symlink cùng tên trong **cả ba** `.agents/skills`, `.claude/skills`, `.cursor/skills` + một dòng trong skills-index (`tests/test_agent_setup.py` chặn khi lệch).
- **Gốc repo, không đường dẫn tuyệt đối:** mọi lệnh chạy từ `"$(git rev-parse --show-toplevel)"`; code Python lấy đường dẫn từ `pipeline/paths.py`, shell dùng `git rev-parse`. Không ghi `/Users/...`, `/home/...`, `/workspace...`, `/opt/cursor...`, đường dẫn tmp hay workspace riêng của agent vào file tracked (test chặn).
- **Không làm trên bản sao của agent:** chỉ làm trong checkout local trên Mac của Hiệp. Không clone/sync sang sandbox, box `/workspace` hay thư mục artifact của agent.
- **Nhiều agent cùng lúc:** nếu checkout chính đang có agent khác sửa (vd Antigravity làm clip), làm việc ở worktree riêng: `git worktree add ../oneup-studio-<việc> -b <nhánh> origin/main`, không stash/checkout đè lên thay đổi của agent khác.

### Quy tắc riêng cho Grok (không có hook, chạy qua remote shell)
1. Đầu phiên: `cd "$(git rev-parse --show-toplevel)"` rồi `bash pipeline/scripts/env-check.sh` (shell không tương tác nên không có nvm/venv; `paths.py` tự tìm). Secret chỉ báo set/missing, không in giá trị.
2. Trước mọi commit: `python3 pipeline/scripts/build-index.py` (nếu thêm/đổi tên `.md`) rồi `bash pipeline/scripts/preflight.sh`. Lỗi có sẵn trước thay đổi của mình thì ghi rõ trong báo cáo, không giấu.
3. **Push chỉ khi Hiệp yêu cầu** (ngoại lệ của Workflow 2 và 4). Không force-push, không sửa lịch sử đã push.
4. Hook toàn cục của Claude (`~/.claude/hooks`: `tools-ready.sh` bật XERJ, các guard gsd…) **không** chạy với Grok. Muốn tìm bằng XERJ: `xerj-ensure`, `export XERJ_API_KEY="$(cat ~/xerj-data/admin.key)"`, rồi `xerj search --prefix work-oneup-studio "..."`; không được thì dùng `rg`/`git grep`.
5. Trình duyệt (DL-083): dùng `ego-browser` CLI qua shell (`EGO_BROWSER_BIN`, chạy `ego-browser skill` trước). Chỉ dùng trình duyệt riêng của Grok khi ego-browser không làm được, và ghi lại.
6. Bước cần subagent (Reviewer khác model, `make-video` §4b): dùng subagent của Grok hoặc `pipeline/scripts/review-eval.py --engine claude|agy|cursor`. Bước cần Antigravity/Gemini (`video-qa`, `teardown.py`, `gate2-qa.py`) gọi `agy` CLI qua shell.
7. Bước dùng MCP (X trong `trend-digest`): dùng tool X của Grok nếu có; không có thì bỏ qua và ghi chú trong digest.

