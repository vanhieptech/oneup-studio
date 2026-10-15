---
id: storage
type: convention
status: active
updated: 2026-10-15
tags: [storage, rule-65, rule-66, source-of-truth]
---
# Quy ước lưu trữ (luật 65, L-034)

Một chỗ cho mỗi loại file. Đường dẫn khai báo tập trung trong `pipeline/paths.py`; mọi script sinh file phải import từ đó. `pipeline/scripts/check-assets.py` chặn (FAIL) khi sai.

| Loại | Nơi lưu (canonical) | Ghi chú |
|---|---|---|
| Font (Be Vietnam Pro, DM Sans) | `brand/fonts/` | Bản chép ở `video-engine/public/fonts/` và `<explainer>/fonts/` do `sync-shared.py` sinh, **gitignored** |
| Logo, màu, token brand | `brand/` (`logos/`, `brand-tokens.json`, `COLOR.md`) | `video-engine/public/brand/` + `<explainer>/logo.svg` là bản sinh |
| SFX dùng chung | `assets/sfx/` (nguồn ghi ở `SOURCES.md`) | SFX tổng hợp khi build nằm ở `final/out/sfx/` (gitignored) |
| Giọng mẫu F5 (reference) | `assets/voice-refs/` | profile nhân vật trỏ vào đây |
| Nhân vật, rig, biểu cảm | `video-engine/src/characters/` (`profiles/`, `rigs/`) | không vẽ nhân vật trong clip |
| Props, layout, motion | `video-engine/src/composition/` (`Props.tsx`, `layout.ts`, `transitions.ts`) | |
| Template HyperFrames | `templates/hyperframes-base/` | |
| Voice takes đã chọn | `video-engine/public/voice/` (key hash, hoặc `v<n>-<scene>`) | file `.json` kèm stt/stt_sim |
| Take thô, thử nghiệm giọng | ngoài repo (`/workspace/<job>/`) hoặc `media/` + `MANIFEST.json` | không commit take thô |
| Mỗi clip | `content/clips/<clip>/` chỉ có `final/` (bản hiện hành: `script-*.md`, `spec.json`, `plan-*.voiced.json`, `timing.json`, `cover/`, `preview/`, `out/`), `archive/` (nháp cũ, storyboard/comic cũ, bản box cũ) và `README.md` | check-assets chặn mọi thứ khác |
| Render clip | làm việc: `final/out/` (gitignored), part render `video-engine/out/`; **bản giữ lại**: `media/clips/<clip>/clip-NN-final.mp4` + `-720.mp4` (manifest) | bản gửi Hiệp: 720p faststart < 10 MB |
| Clip đã duyệt | `content/archive/<clip>/` (cùng layout, thêm `final/approved.json`) | luật 66 |
| Media lớn (mp4 sample, footage) | `media/` (gitignored) + `media/MANIFEST.json` | `media/footage/inbox/` cho video quay |
| Test | `tests/` | |
| Script, tool | `pipeline/scripts/`, `pipeline/tts/`, `video-engine/src/` | |
| Research, trend | `research/` (`trends/<date>/`), `docs/research/`, `resources/` (từ điển, văn nói) | |
| Skill | bản chạy: `/home/box/agent-data/workflows/<skill>/`; bản mirror: `skills/<skill>/` (cập nhật cả hai) | |
| Log, bài học, quyết định | `logs/` (`lessons.md`, `decision-log.md`, `runs/`) | |
| Luật | `rules/video-rules.md` | |
| Quy trình | `docs/workflow/per-video-pipeline.md` | |

Thư mục gốc hợp lệ (`TOP_ALLOWED`): GUIDE.md, assets, brand, content, docs, logs, media, pipeline, research, resources, rules, skills, templates, tests, video-engine. Đã bỏ: `footage/` → `media/footage/`, `renders/` → `final/out/` của clip, `refs/` → `resources/refs/`, `samples/` → `content/samples/lab/`. `templates/` giữ vì là thư viện chung (scaffold HyperFrames, mẫu post-package).

Cấm: font/logo/giọng mẫu trong `content/`; hai file cùng nội dung (sha256) ngoài các vùng miễn trừ (skills vendored, voice cache, template `.tpl`, bản snapshot `/vN/`, `final/cover.png` theo L-020); thư mục cấp gốc ngoài danh sách `TOP_ALLOWED`.

## Ánh xạ prompt bot nội dung (`docs/prompts/content-bot-prompt.md`)
Repo đã có guide nên giữ cấu trúc hiện tại; cấu trúc mặc định của prompt ánh xạ như sau.

| Prompt (mặc định) | Ở repo này | Ghi chú |
|---|---|---|
| `/GUIDE.md` | `GUIDE.md` (con trỏ ngắn) → file này | không chép nội dung |
| `/INDEX.md` | `INDEX.md` + `index.json` | sinh bằng `build-index.py`; `check-assets.py` FAIL nếu lỗi thời |
| `/research/trends/YYYY-MM-DD_<nguồn>.md` | `research/trends/<YYYY-MM-DD>/` (`digest.md`, `raw.json`, ghi chú theo chủ đề) | giữ thư mục theo ngày (rule-38) |
| `/research/references/` | `research/references/` (mới) | phân tích creator/hook/format; mẫu hook vẫn ở `research/trends/patterns.md` |
| `/scripts/YYYY-MM-DD_<slug>.md` | `content/clips/<clip>/final/script-final.md` (bản hiện hành), bản cũ `archive/script-vN.md` | không tạo `scripts/` |
| `/scripts/_templates/` | `templates/script.md` (mới), `templates/post-package.md` | |
| `/assets/` + metadata | `assets/` (`sfx/SOURCES.md`), `brand/`, media lớn `media/` + `MANIFEST.json`; tài liệu ngoài `resources/refs/README.md` | |
| `/prompts/` | `docs/prompts/` (mới) | prompt routine trend cũ vẫn ở `docs/plans/trend-routine-prompt-v*.md` (đề xuất gộp vào đây) |
| `/published/` | `content/published/README.md` (mới, log đăng) | clip đã duyệt vẫn `content/archive/` (luật 66) |
| `/archive/` | `content/archive/` (clip) + `archive/` trong mỗi clip | |

Front-matter bắt buộc cho `.md` nội dung (mọi file trừ `skills/`, `video-engine/`, `templates/hyperframes-base/`, `docs/legacy-box/`, `resources/refs/<clone>/`): `title, date, type, tags, status, source`. `status` của file mới trong `docs/prompts/`, `research/references/`, `content/published/`, `final/script-final.md`: `draft | ready | published`. Kiểm bằng `check-assets.py` (rule-65 FM). Commit: `<loại>: <mô tả>`.

## Vòng đời clip (luật 66)
`content/clips/<clip>/` (đang làm, được thiếu) → đủ gói đăng + Hiệp nói "duyệt" → `git mv` sang `content/archive/<clip>/`, ghi `final/approved.json`, video full + 720p ở `media/clips/<clip>/` + `MANIFEST.json`.

## File gitignored và nơi giữ trên Mac
Repo trên Mac: `/Users/macbook/me/projects/oneup-studio` (cùng đường dẫn tương đối như box `/workspace/oneup-studio`).

| Gitignored | Là gì | Trên Mac | Cách có |
|---|---|---|---|
| `media/**` (trừ MANIFEST/README) | video final full + 720p, sample mp4, footage thô | **phải có** | `pipeline/scripts/media-sync.py pack` (box) → CopyFromBox từng `part.NN` vào `.git/media-sync/` → `media-sync.py unpack` (Mac) → tự `verify` sha256 |
| `content/clips/**/final/out/`, `final/*.mp4` | render làm việc, mix, sfx sinh | sinh lại | `build-final.py`; bản giữ lại copy vào `media/clips/` |
| `video-engine/out/` | part render Remotion | sinh lại | `build-final.py` |
| `video-engine/public/fonts/`, `public/brand/`, `**/explainer/fonts/`, `**/explainer/logo.svg`, `templates/hyperframes-base/{fonts,logo.svg}` | bản chép thư viện chung | sinh lại | `sync-shared.py` (build-final tự chạy) |
| `node_modules/`, `.bundle-cache/` | thư viện npm, cache bundle | sinh lại | `npm ci` trong `video-engine/` |
| `video-engine/public/voice/_prosody-job.json` | file job tạm | không cần | — |
| `resources/refs/awesome-ai-motion/` | clone tài liệu ngoài | tuỳ chọn | `git clone` lại |
| `resources/refs/transitions.dev/` | clone tài liệu ngoài (Transitions.dev License, @8c92530) | tuỳ chọn | `git clone` lại; bản port nằm ở `video-engine/src/composition/transitions/` |
| `.env`, `__pycache__/`, `.DS_Store` | bí mật/cache | không chép | — |

Voice take (`video-engine/public/voice/*.wav|json`) **được commit** nên Mac có qua git. Chạy `python3 pipeline/scripts/media-sync.py verify` trên Mac sau mỗi lần sync; exit ≠ 0 = thiếu.

