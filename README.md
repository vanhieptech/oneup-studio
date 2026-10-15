---
id: repo-readme
type: readme
status: active
updated: 2026-10-15
tags: [overview]
---
# oneup-studio: hệ thống nội dung @hi.oneup
Agent: đọc `AGENTS.md` trước. Bản đồ file: `INDEX.md`.

Kênh TikTok https://www.tiktok.com/@hi.oneup: video productivity/motivation 55–60s, nội dung chuyển thể từ HowToLiveBetter (CC BY 4.0), dùng brand OneUp.

Nguồn chuẩn về cấu trúc: **`docs/conventions/storage.md`** (luật 65, 66). Đường dẫn trong code: `pipeline/paths.py`. Kiểm: `pipeline/scripts/check-assets.py`. File này chỉ tóm tắt.

## Cấu trúc repo
```
AGENTS.md  INDEX.md(sinh)  README.md  index.json(sinh)
assets/            thư viện chung: sfx/ (CC0 + SOURCES.md), voice-refs/ (giọng mẫu F5)
brand/             font (fonts/), logo (logos/), màu + token, Omi, app icon, preview, MASTER.md
content/
  clips/<clip>/    clip ĐANG LÀM (được thiếu gói đăng)
  archive/<clip>/  clip ĐÃ DUYỆT (đủ gói đăng + final/approved.json)
  samples/         clip mẫu; samples/lab/ = thí nghiệm giọng, spike, audition
  theme-map.md idea-bank.md story-bank.md voice-profile.md
docs/              conventions/storage.md (cấu trúc), workflow/per-video-pipeline.md (quy trình), research/, plans/
logs/              lessons.md, decision-log.md, effects-log.md, runs/
media/             (gitignored) clips/<clip>/ video full + 720p, samples/, footage/inbox/ · MANIFEST.json (commit)
pipeline/          paths.py, scripts/ (build-final, check-rules, check-assets, sync-shared, media-sync…), tts/
research/          trends/<ngày>/, motion, production research
resources/         vn-dict/, vn-spoken/, refs/ (clone ngoài, gitignored)
rules/             video-rules.md (luật hiện hành)
skills/            mirror của skill (bản chạy: /home/box/agent-data/workflows/)
templates/         hyperframes-base (scaffold), post-package.md
tests/             test
video-engine/      Remotion: src/characters (rig, profile, biểu cảm), src/composition (props, layout, motion), public/voice (voice take, commit)
```

## Layout một clip
```
content/{clips|archive}/<clip>/
  README.md        (tuỳ chọn)
  final/           script-*.md, spec.json (nguồn sự thật), plan-*.voiced.json, timing.json, check-rules.txt,
                   post.md, post-checklist.md, cover/ + cover.png, preview/, explainer/, approved.json (khi lưu trữ),
                   out/ (gitignored: render làm việc, mix, sfx)
  archive/         nháp cũ, storyboard/comic cũ, bản trước
```
Chỉ `final/`, `archive/`, `README.md` được phép (check-assets chặn).

## Vòng đời clip (luật 66)
`content/clips/<clip>` → đủ tiêu đề, caption, hashtag, cover, video full + 720p (`media/clips/<clip>/`), `post.md` **và Hiệp nói "duyệt"** → `content/archive/<clip>` + `final/approved.json`. check-rules bỏ qua clip lưu trữ.

## Gitignored (vẫn phải giữ trên Mac)
`media/**` (video final, sample, footage) → chép sang Mac bằng `pipeline/scripts/media-sync.py`. Sinh lại được, không cần chép: `final/out/`, `video-engine/out/`, `node_modules/`, bản chép font/logo (`sync-shared.py`). Bảng đầy đủ: `docs/conventions/storage.md` §Gitignored.
