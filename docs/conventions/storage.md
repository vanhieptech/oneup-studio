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
| Render clip | `content/clips/<clip>/final/out/` (gitignored), part render ở `video-engine/out/` | bản gửi Hiệp: 720p faststart < 10 MB |
| Media lớn (mp4 sample, footage) | `media/` (gitignored) + `media/MANIFEST.json` | `media/footage/inbox/` cho video quay |
| Test | `tests/` | |
| Script, tool | `pipeline/scripts/`, `pipeline/tts/`, `video-engine/src/` | |
| Research, trend | `research/` (`trends/<date>/`), `docs/research/`, `resources/` (từ điển, văn nói) | |
| Skill | bản chạy: `/home/box/agent-data/workflows/<skill>/`; bản mirror: `skills/<skill>/` (cập nhật cả hai) | |
| Log, bài học, quyết định | `logs/` (`lessons.md`, `decision-log.md`, `runs/`) | |
| Luật | `rules/video-rules.md` | |
| Quy trình | `docs/workflow/per-video-pipeline.md` | |

Thư mục gốc hợp lệ (`TOP_ALLOWED`): assets, brand, content, docs, logs, media, pipeline, research, resources, rules, skills, templates, tests, video-engine. Đã bỏ: `footage/` → `media/footage/`, `renders/` → `final/out/` của clip, `refs/` → `resources/refs/`, `samples/` → `content/samples/lab/`. `templates/` giữ vì là thư viện chung (scaffold HyperFrames, mẫu post-package).

Cấm: font/logo/giọng mẫu trong `content/`; hai file cùng nội dung (sha256) ngoài các vùng miễn trừ (skills vendored, voice cache, template `.tpl`, bản snapshot `/vN/`, `final/cover.png` theo L-020); thư mục cấp gốc ngoài danh sách `TOP_ALLOWED`.
