---
id: repo-readme
type: readme
status: active
updated: 2026-10-12
tags: [overview]
---
# oneup-studio: hệ thống nội dung @hi.oneup
Agent: đọc `AGENTS.md` trước. Bản đồ file: `INDEX.md`.

Kênh TikTok https://www.tiktok.com/@hi.oneup: video productivity/motivation 55–60s, nội dung chuyển thể từ HowToLiveBetter (CC BY 4.0), dùng brand OneUp.

| Thư mục | Nội dung |
|---|---|
| `rules/` | `video-rules.md` (rules v2, chuẩn duy nhất) |
| `brand/` | tokens, index, MASTER.md, fonts (kèm license), logos, Omi, app icons, previews, prototype |
| `research/` | research engine, pipeline, motion |
| `content/` | `theme-map.md`, `idea-bank.md`, `clips/NN-slug/` (script, beat sheet, comic plan, caption, comp) |
| `templates/` | `hyperframes-base` (1080×1920, Be Vietnam Pro, GSAP local). Chạy `npm i` rồi `npm run render` |
| `skills/` | `motion-picks-per-script` |
| `refs/` | link tài liệu ngoài (awesome-ai-motion clone local, không commit) |
| `pipeline/` | `pipeline.md` + `scripts/` (placeholder) |
| `logs/` | `effects-log.md` |
| `assets/` | sfx (CC0, kèm SOURCES.md), stock, icon |
| `footage/` | `inbox/` nhận AirDrop giọng thu (file âm thanh không commit) |
| `renders/` | `ready/` gói sẵn đăng (file mp4 không commit) |

## Quy ước thư mục (luật 65)
Chi tiết: `docs/conventions/storage.md` · đường dẫn: `pipeline/paths.py` · chặn: `pipeline/scripts/check-assets.py`.
```
brand/            font, logo, màu, token (một bản duy nhất)
assets/           sfx/, voice-refs/ (giọng mẫu F5)
video-engine/src/ characters/ (rig, profile, biểu cảm), composition/ (props, layout, motion)
video-engine/public/voice/  voice take đã chọn (fonts/, brand/ là bản sinh, gitignored)
templates/        hyperframes-base
content/clips/<clip>/final/  script, spec, plan, timing, cover/, preview/, out/ (render, gitignored)
media/            file lớn (gitignored) + MANIFEST.json
pipeline/         scripts/, tts/, paths.py
research/ docs/ resources/  nghiên cứu, quy ước, quy trình (docs/workflow/per-video-pipeline.md)
logs/ rules/ skills/ tests/
```

