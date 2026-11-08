---
title: "CapCut smoke — local Mac + CLI compile"
date: 2026-11-08
id: docs-vht-capcut-smoke
type: guide
status: active
updated: 2026-11-08
source: "channels/vanhiep-tech PLAN"
tags: [capcut, vanhiep-tech, local]
---
# CapCut smoke — local Mac + CLI compile

**Không** dùng cloud `/opt/cursor/artifacts`. Skill: `skills/make-capcut-draft/SKILL.md`.

## Repo Mac
`/Users/macbook/me/projects/oneup-studio`

## Media (absolute)
`/Users/macbook/me/projects/oneup-studio/media/channels/vanhiep-tech/vht-20261107-oauth-control-plane/`

| File | Track |
|---|---|
| `a-roll.mp4` | A-full (thật hoặc placeholder) |
| `a-roll-cutout.mov` | A-cutout (sau HF remove-background) |
| `cu-01.mp4` | Cutaway |
| `ov-hook.mov` / `ov-d01.mov` / `ov-l3.mov` / `ov-q.mov` | Overlay alpha |

## Path A — CLI compile (V1.1)
1. Đóng CapCut (hoặc compile ra `lab/out/` rồi import).
2. `npx capcut-cli doctor`
3. `npx capcut-cli compile channels/vanhiep-tech/clips/vht-20261107-oauth-control-plane/capcut-spec.json --check`
4. Vào store:
   ```bash
   npx capcut-cli compile channels/vanhiep-tech/clips/vht-20261107-oauth-control-plane/capcut-spec.json \
     --drafts "$HOME/Movies/CapCut/User Data/Projects/com.lveditor.draft" \
     --template auto
   ```
5. Mở CapCut → refine → thêm VO → export.
6. Fail → ghi `lab/capcut-cli-notes.md` → Path B.

## Path B — import tay (fallback)
1. Project 9:16 · A-roll local
2. Import 4× `.mov` Overlay + `cu-01` cutaway
3. Fail alpha → PLAN Revisions; tạm MP4 solid brand (không hồng)

## Cutout bake-off
Xem `make-capcut-draft` — HF `remove-background` vs CapCut `matting`; edge thắng.
