---
title: "Danh mục skill cho mọi agent"
date: 2026-11-28
type: guide
tags: [agents, skills, grok, claude, cursor, antigravity]
status: ready
source: "oneup-studio (agent-native setup)"
id: agents.skills-index
updated: 2026-11-28
---
# Danh mục skill (một nguồn, mọi agent)

Nguồn duy nhất của mỗi skill là thư mục ghi ở cột **Nguồn** (có `SKILL.md`). `.agents/skills/` (Antigravity), `.claude/skills/` (Claude Code) và `.cursor/skills/` (Cursor) chỉ chứa **symlink tương đối** cùng tên trỏ về đây. Grok không đọc các thư mục đó: Grok dùng bảng này, mở `<Nguồn>/SKILL.md` khi tác vụ khớp cột «Khi nào dùng».

Thêm skill mới: tạo `<nguồn>/SKILL.md` (`name:` = tên thư mục) → thêm symlink cùng tên trong cả ba thư mục agent → thêm một dòng vào bảng này → chạy `bash pipeline/scripts/preflight.sh` (`tests/test_agent_setup.py` kiểm ba thư mục khớp nhau và khớp bảng này).

Mọi lệnh trong skill chạy từ gốc repo (`cd "$(git rev-parse --show-toplevel)"`). Kiểm toolchain: `bash pipeline/scripts/env-check.sh`.

## Skill riêng của @hi.oneup

| Skill | Nguồn | Khi nào dùng | Công cụ/CLI cần |
|---|---|---|---|
| `make-video` | `skills/make-video/` | Hiệp bảo làm clip @hi.oneup («Làm clip tiếp theo», «làm lại clip-NN», góp ý beat). Quy trình bắt buộc v3.0 (luật 48, `DL-094`): `--fast` / `--voice-mode` / `storyboard.yaml` → `spec-compile` → `--preview`. | `ideate-clip.py`, `script-arena.py`, `spec-compile.py`, `audio-precheck.py`, `check-rules.py`, `build-final.py` (`--preview`), `golden-sync.py`, `video-engine` (npm), VieNeu/F5/direct; Reviewer subagent khác model hoặc `review-eval.py` |
| `trend-digest` | `skills/trend-digest/` | Quét trend hằng ngày / tổng hợp Chủ nhật cho @hi.oneup. | `trend-collect.py`, `trend-streams.py`, `radar-fetch.py`, `apify-run.py` (`APIFY_TOKEN`), `tinyfish`, `ego-browser`; X qua MCP nếu agent có |
| `script-polish` | `skills/script-polish/` | Sau khi có kịch bản đã kiểm fact, trước khi gửi Hiệp duyệt: bỏ giọng AI, chuyển sang văn nói. | đọc `humanizer`, `content/voice-profile.md` |
| `humanizer` | `skills/humanizer/` | Sửa văn bản nghe như AI (vendored, MIT). | không |
| `motion-picks-per-script` | `skills/motion-picks-per-script/` | Kịch bản đã duyệt/nháp, cần chọn hiệu ứng chuyển động theo từng beat. | `resources/refs/awesome-ai-motion`, `transitions.dev`, `motionmaxxing` (clone local, gitignored) |
| `motionmaxxing` | `skills/motionmaxxing → resources/refs/motionmaxxing/` | Hướng dẫn craft motion graphics + ease đo sẵn (Apache-2.0). Symlink tới clone local: thiếu clone thì skill này không đọc được. | port Remotion ở `video-engine/src/composition/motionmaxxing/` |
| `social-poster` | `skills/social-poster/` | Hiệp gửi link và muốn nháp bài X/LinkedIn. Chỉ soạn nháp, không tự đăng. | `ego-browser` / fetch |
| `video-qa` | `skills/video-qa/` | Gate 2: QA video 720p đã render (luật 34). | `pipeline/scripts/gate2-qa.py` → `agy` (Antigravity CLI) hoặc `gemini` CLI |

## Skill kênh @vanhiep.tech (đọc `channels/vanhiep-tech/AGENTS.md` trước)

| Skill | Nguồn | Khi nào dùng | Công cụ/CLI cần |
|---|---|---|---|
| `make-layer` | `channels/vanhiep-tech/skills/make-layer/` | @vanhiep.tech: dựng và render layer overlay/cutaway HyperFrames. | HyperFrames CLI (Node ≥ 22), `brand-tokens.json` |
| `make-capcut-draft` | `channels/vanhiep-tech/skills/make-capcut-draft/` | @vanhiep.tech: tạo nháp CapCut Desktop từ layer đã render (local Mac). | `capcut-cli` (phiên bản ở `pipeline/versions.json`), CapCut Desktop |
| `shorts-cutter` | `channels/vanhiep-tech/skills/shorts-cutter/` | Cắt video dài (Hiệp có quyền) thành Shorts dọc. | faster-whisper qua `ASR_PYTHON`, `ffmpeg`, `yt-dlp` |

## HyperFrames (vendored Apache-2.0, 21 skill chính thức; bắt đầu từ `hyperframes`)

Dùng cho beat giải thích / motion graphics (luật 42). Cần HyperFrames CLI (phiên bản ở `pipeline/versions.json`) và Node ≥ 22. Mô tả gốc tiếng Anh, rút gọn câu đầu.

| Skill | Nguồn | Khi nào dùng |
|---|---|---|
| `embedded-captions` | `skills/hyperframes/embedded-captions/` | Add captions or subtitles to an existing single-subject talking-head video without editing the footage. |
| `faceless-explainer` | `skills/hyperframes/faceless-explainer/` | Turn arbitrary text — an article, notes, a topic, a brief — into a faceless explainer video: there is no site or footage to capture, so the visuals are invented per scene (typography, abstract graphics, diagrams, data-vi |
| `figma` | `skills/hyperframes/figma/` | Import Figma content into a HyperFrames composition — rendered assets, brand tokens, components, storyboard sections → reconstructed motion (frames read as states, not slides) (REST/CLI), connector-assisted motion when a |
| `general-video` | `skills/hyperframes/general-video/` | Author or edit a custom HyperFrames composition when no specialized workflow fits, or when BRIEF.md sets flow: companion. |
| `hyperframes` | `skills/hyperframes/hyperframes/` | Mandatory entry point: read this first for any request to make, create, edit, animate, or render a video, animation, or motion graphic, including a promo, explainer, captioned clip, title card, overlay, slideshow or inte |
| `hyperframes-animation` | `skills/hyperframes/hyperframes-animation/` | All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, AND the seven runtime adapters (GSAP default, plus Lottie, Three.js, Anime |
| `hyperframes-audio` | `skills/hyperframes/hyperframes-audio/` | Use when audio already placed in a HyperFrames composition needs to be mixed: fade-in/fade-out, crossfade, track gain or volume, volume automation, ducking, a music bed that fights a voiceover (voiceover carve), effects  |
| `hyperframes-cli` | `skills/hyperframes/hyperframes-cli/` | Use the HyperFrames CLI development loop: init, add, catalog, capture, lint, check, snapshot, compare, grade-compare, preview, play, present, beats, keyframes, single or batch render, publish, cloud, cloudrun, feedback,  |
| `hyperframes-core` | `skills/hyperframes/hyperframes-core/` | The HyperFrames composition contract — build one renderable project. |
| `hyperframes-creative` | `skills/hyperframes/hyperframes-creative/` | Non-animation creative direction for HyperFrames videos. |
| `hyperframes-keyframes` | `skills/hyperframes/hyperframes-keyframes/` | Use when a HyperFrames composition needs a punch-in, punch-out, zoom, reframe, Ken Burns treatment, camera move, visual match/whip handoff, or other seek-safe 2D/3D keyframes; also for GSAP, CSS keyframes, Anime.js, WAAP |
| `hyperframes-registry` | `skills/hyperframes/hyperframes-registry/` | Search, install, and wire registry blocks and components into HyperFrames compositions. |
| `hyperframes-studio` | `skills/hyperframes/hyperframes-studio/` | Use when working with a person on a HyperFrames project in Studio: first, whether their message asks for a change at all (questions, loose ideas and "don't change anything" get an answer and a plan, not an edit); for a n |
| `media-use` | `skills/hyperframes/media-use/` | Agent Media OS for a HyperFrames project. |
| `motion-graphics` | `skills/hyperframes/motion-graphics/` | A short, design-led motion graphic where motion is the message — kinetic typography, stat count-up, chart/data-viz hit, logo sting / brand lockup, lower-third / callout / social overlay, animated map (highlight regions,  |
| `music-to-video` | `skills/hyperframes/music-to-video/` | Turn a music track (an audio file, a video to pull audio from, or a track generated from a mood brief) into a beat-synced video — lyric video, slideshow, or kinetic promo. |
| `pr-to-video` | `skills/hyperframes/pr-to-video/` | Turn a GitHub pull request (a PR URL, owner/repo#N, or 'this PR' in a checked-out repo) into a code-change explainer video — changelog, feature reveal, fix, or refactor walkthrough built from the diff, commits, and files |
| `product-launch-video` | `skills/hyperframes/product-launch-video/` | Turn a product or marketing URL, pasted script, or brief into a product launch / promo video — SaaS promos, feature reveals, product demos, app and company launches. |
| `remotion-to-hyperframes` | `skills/hyperframes/remotion-to-hyperframes/` | Port an existing Remotion (React) composition''s source to HyperFrames HTML. |
| `slideshow` | `skills/hyperframes/slideshow/` | Author a HyperFrames slideshow — a presentation, pitch deck, or interactive deck with discrete slides, fragment reveals, branching, hotspot navigation, and built-in presenter mode with speaker notes; also converts an exi |
| `talking-head-recut` | `skills/hyperframes/talking-head-recut/` | Package an existing talking-head / interview / podcast video with timed, designed GRAPHIC OVERLAY cards — kinetic titles, lower-thirds, data callouts, quotes, side panels, picture-in-picture — synced to the transcript, o |
