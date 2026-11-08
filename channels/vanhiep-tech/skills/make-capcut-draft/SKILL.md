---
name: make-capcut-draft
description: >-
  Scaffold a CapCut Desktop draft for @vanhiep.tech via capcut-cli compile
  (local Mac). Dual A-roll (full + cutout), place ov-*/cu-* by script markers.
  Desktop remains final export. Use after make-layer renders exist.
---
# Make CapCut draft (@vanhiep.tech)

Not comic `make-video`. Read `channels/vanhiep-tech/AGENTS.md` + `PLAN.md` + this skill.

## Preconditions (local Mac)
- Repo: `/Users/macbook/me/projects/oneup-studio`
- Layers rendered: `media/channels/vanhiep-tech/<clip-id>/{ov-*.mov,cu-*.mp4}`
- A-roll (gitignored media):
  - `media/channels/vanhiep-tech/<clip-id>/a-roll.mp4` (full)
  - `media/channels/vanhiep-tech/<clip-id>/a-roll-cutout.mov` (HF remove-background; after bake-off)
- `npx capcut-cli doctor` OK
- CapCut Desktop installed; drafts under `~/Movies/CapCut/User Data/Projects/com.lveditor.draft`

## Script schema
Layer table columns: `Id | Vai trò | Canvas | Output | a_roll`
- `a_roll`: `full` (default) | `cutout`
- Marker shorthand: `[mm:ss ov-d01 cutout]` → same as `a_roll: cutout`
- `cu-*`: cutaway — main track plays cutaway media; A-roll off that window
- VO/caption: **not** in compile (add by hand in CapCut)

## Cutout bake-off (once per camera setup)
1. **A — HyperFrames** (default candidate):
   ```bash
   npx hyperframes remove-background media/.../a-roll.mp4 \
     -o media/.../a-roll-cutout.mov --quality best
   ```
2. **B — CapCut matting flag** (experiment):
   - `compile` or `add-video` A-roll → `capcut matting <project> <segment-id>`
   - Open CapCut; app computes matte
3. Win on **edge quality** (hair/shoulders, 10–15s talk). Record time as secondary in `channels/vanhiep-tech/lab/capcut-cli-notes.md`.
4. Winner path becomes default in this skill + PLAN revision.

## Compile steps
1. Write `clips/<clip-id>/capcut-spec.json` (see pilot sample).
2. Validate:
   ```bash
   npx capcut-cli compile clips/<clip-id>/capcut-spec.json --check
   npx capcut-cli compile clips/<clip-id>/capcut-spec.json --plan
   ```
3. Build into CapCut store (`--template auto`):
   ```bash
   npx capcut-cli compile clips/<clip-id>/capcut-spec.json \
     --drafts "$HOME/Movies/CapCut/User Data/Projects/com.lveditor.draft" \
     --template auto
   ```
4. Open CapCut → refine → export. Add VO by hand.
5. On failure: fallback `docs/capcut-smoke.md` manual import; append error to `lab/capcut-cli-notes.md`.

## Track rules (machine)
| Marker | Main / A track | Overlay track |
|---|---|---|
| `ov-*` + `a_roll:full` | `a-roll.mp4` | `ov-*.mov` |
| `ov-*` + `a_roll:cutout` | `a-roll-cutout.mov` (+ brand plate under if needed) | `ov-*.mov` |
| `cu-*` | `cu-*.mp4` replaces A for duration | — |

## Banned
- Cloud `/opt/cursor/artifacts` as CapCut source
- Relying on CLI `render` / `export` for final delivery
- VO/Whisper as compile requirement V1.1
- Deep effects on A-roll in V1.1 (HF motion stays on `ov-*`/`cu-*` only)
