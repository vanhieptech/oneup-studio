---
id: index
type: index
status: generated
tags: [index, retrieval]
---
# INDEX (generated, do not hand-edit; run `python3 pipeline/scripts/build-index.py`)

## Docs
| id | type | status | path | title |
|---|---|---|---|---|
| agents | guide | active | `AGENTS.md` | AGENTS.md: cách AI làm việc trong repo này |
| index | index | generated | `INDEX.md` | INDEX (generated, do not hand-edit; run `python3 pipeline/scripts/build-index.py`) |
| repo-readme | readme | active | `README.md` | oneup-studio: hệ thống nội dung @hi.oneup |
| sfx-sources | log | living | `assets/sfx/SOURCES.md` | Nguồn SFX (chỉ dùng CC0 hoặc Mixkit, theo luật 22) |
| brand-index | brand | active | `brand/brand-index.md` | @hi.oneup — Brand index cho video |
| characters | brand | prototype | `brand/characters/README.md` | Characters (prototype v0.1) |
| clip-01.beat-sheet | beat-sheet | draft | `content/clips/clip-01-implementation-intention/beat-sheet.md` | Clip 01: Beat sheet v2 (55–60s, LIGHT), khớp với script.md |
| clip-01.script-v2.1-draft | script | draft | `content/clips/clip-01-implementation-intention/script-v2.1-draft.md` | Clip 01: script v2.1 DRAFT (humanizer + voice profile), đặt cạnh v2 |
| clip-01.script-v3-draft | script | draft | `content/clips/clip-01-implementation-intention/script-v3-draft.md` | Clip 01: script v3 DRAFT (kể chuyện, giọng Hiệp), đặt cạnh v2 và v2.1 |
| clip-01.script | script | awaiting-approval | `content/clips/clip-01-implementation-intention/script.md` | @hi.oneup: Clip 01 script v2 (55–60s), chờ Hiệp duyệt |
| clip-01.shot-list | shot-list | draft | `content/clips/clip-01-implementation-intention/shot-list.md` | Clip 01: Shot list v2 (LIGHT, 55–60s), khớp với script.md |
| idea-bank | plan | active | `content/idea-bank.md` | Idea bank |
| story-bank | plan | needs-confirmation | `content/story-bank.md` | Story bank: chuyện thật của Hiệp (rule-41) |
| theme-map | plan | active | `content/theme-map.md` | Theme map — @hi.oneup (LIGHT / DARK theo tone) |
| voice-profile | profile | confirmed | `content/voice-profile.md` | Voice profile: Hiệp (@hi.oneup) |
| decision-log | log | living | `logs/decision-log.md` | Nhật ký quyết định: @hi.oneup (luật 33) |
| effects-log | log | living | `logs/effects-log.md` | Effects log |
| pipeline | workflow | active | `pipeline/pipeline.md` | Pipeline sản xuất 1 clip (theo rules v2) |
| refs | reference | active | `refs/README.md` | Tài liệu tham khảo (link ngoài, không đưa mã nguồn vào repo) |
| research.comic-system | research | reference | `research/comic-system-research-vi.md` | Nghiên cứu: hệ thống minh hoạ comic cho clip kể chuyện (Hiệp + Omi) |
| research.motion-layer | research | reference | `research/motion-layer.md` | @hi.oneup motion layer, based on gongnyang/awesome-ai-motion |
| research.video-gen | research | reference | `research/oneup-video-gen-research-vi.md` | Nghiên cứu: tự động hoá video ngắn productivity/motivation cho TikTok @hi.oneup |
| research.production-system | research | reference | `research/production-system-research-vi.md` | Hệ thống sản xuất video 60s cho @hi.oneup: research & đề xuất |
| research.skillopt | research | reference | `research/skillopt-eval-vi.md` | Đánh giá microsoft/skillopt (12/10/2026) |
| trends-2026-10-12 | trend-digest | done | `research/trends/2026-10-12/digest.md` | Trend digest: 2026-10-12 (chạy lại theo chế độ rộng, 23:30 giờ VN) |
| trends-ingest | trend-library | living | `research/trends/ingest.md` | Trend ingest: thư viện sống (rule-37, rule-39) |
| rules | rules | active | `rules/video-rules.md` | @hi.oneup: Bộ luật sản xuất video (v2, 12/10/2026) |
| skill.humanizer | skill | active | `skills/humanizer/SKILL.md` | humanizer |
| skill.humanizer.upstream | vendor-note | active | `skills/humanizer/UPSTREAM.md` | Humanizer (vendored, MIT) |
| skill.motion-picks-per-script | skill | active | `skills/motion-picks-per-script/SKILL.md` | Motion picks per script |
| skill.script-polish | skill | active | `skills/script-polish/SKILL.md` | Script polish (VI voice) |
| skill.trend-digest | skill | active | `skills/trend-digest/SKILL.md` | Trend digest |

## Rules (source: `rules/video-rules.md`)
| id | title |
|---|---|
| rule-1 | Ngôn ngữ |
| rule-2 | Giọng |
| rule-3 | Lên hình |
| rule-4 | Độ dài |
| rule-5 | Phong cách (xoay vòng) |
| rule-6 | Tỉ lệ hình |
| rule-7 | Cấu trúc mặc định |
| rule-8 | CTA |
| rule-9 | Nhịp đổi hình |
| rule-10 | Chủ đề |
| rule-11 | Lịch đưa app |
| rule-12 | Clip đầu tiên |
| rule-13 | Ghi nguồn |
| rule-14 | Brand |
| rule-15 | Font |
| rule-16 | Chữ chính trên màn hình |
| rule-17 | Theme |
| rule-18 | Minh hoạ |
| rule-19 | Motion |
| rule-20 | Hậu kỳ |
| rule-21 | Nhạc |
| rule-22 | SFX |
| rule-23 | Stock |
| rule-24 | Chỉ dùng công cụ miễn phí |
| rule-25 | Engine |
| rule-26 | Transcribe |
| rule-27 | Nơi render |
| rule-28 | Mức tự động |
| rule-29 | Quay |
| rule-30 | Cover |
| rule-31 | Tần suất |
| rule-32 | Đăng |
| rule-33 | Nhật ký quyết định |
| rule-34 | Chuẩn chất lượng |
| rule-35 | Storyboard trước khi duyệt script |
| rule-36 | Storyboard là tài sản có phiên bản |
| rule-37 | Script phải dùng trend |
| rule-38 | Trend digest hằng ngày |
| rule-39 | Bridge từ trend sang bài học |
| rule-40 | Polish script (humanizer + voice) |
| rule-41 | Kể chuyện trước |

## Clips
| id | theme | path | files |
|---|---|---|---|
| clip-01 | LIGHT | `content/clips/clip-01-implementation-intention` | beat-sheet.md, comic, script-v2.1-draft.md, script-v3-draft.md, script.md, shot-list.md, storyboard |

## Assets & tools
| id | path | description |
|---|---|---|
| asset.fonts | `brand/fonts/` | Be Vietnam Pro (video), DM Sans (app) + OFL licenses |
| asset.logos | `brand/logos/` | Logo SVG/PNG; hero = 05-pair-plus.svg |
| asset.omi | `brand/omi-exports/` | Omi mascot SVG/PNG, 4 styles x 12 moods |
| asset.app-icons | `brand/app-icon-exports/` | App icons light/dark |
| asset.tokens | `brand/brand-tokens.json` | Colors/fonts/caption/logo tokens (machine-readable) |
| asset.sfx | `assets/sfx/` | CC0/Mixkit SFX + SOURCES.md |
| asset.template | `templates/hyperframes-base/` | HyperFrames 1080x1920 scaffold, local GSAP |
| asset.characters | `brand/characters/` | Hiệp rig + model sheets, Omi sheet (prototype v0.1) |
| tool.comic | `pipeline/comic/render.py` | Comic strip renderer (comic/spec.json -> strip.png) |
| tool.storyboard | `pipeline/storyboard/render.py` | Shared storyboard renderer (spec.json -> PNGs + contact sheet) |
| tool.sync-trends | `pipeline/scripts/sync-trends.sh` | Box -> repo trend sync, commit, push |
| tool.build-index | `pipeline/scripts/build-index.py` | Regenerates this index |
| data.trends | `research/trends/` | Daily digests YYYY-MM-DD/{digest.md,raw.json} + ingest.md |
| dir.footage | `footage/inbox/` | AirDrop inbox (media gitignored) |
| dir.renders | `renders/ready/` | Ready-to-post packages (media gitignored) |
