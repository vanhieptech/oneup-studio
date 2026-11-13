---
name: make-capcut-draft
description: >-
  Scaffold a CapCut Desktop draft for @vanhiep.tech via capcut-cli compile
  (local Mac). Dual A-roll (full + cutout), place ov-*/cu-* by script markers.
  Desktop remains final export. Use after make-layer renders exist.
version: "1.0.0"
metadata:
  author: OneUp Studio
  tags:
    - capcut
    - vanhiep-tech
    - draft
    - a-roll
---
# Make CapCut draft (@vanhiep.tech)

## Purpose
Scaffold a CapCut Desktop draft for @vanhiep.tech from rendered ov-*/cu-* layers via local `capcut-cli compile`.


Not comic `make-video`. Read `channels/vanhiep-tech/AGENTS.md` + `PLAN.md` + this skill.

## Preconditions (local Mac)
- Repo: the Mac checkout of `oneup-studio`
- Layers rendered: `media/channels/vanhiep-tech/<clip-id>/{ov-*.mov,cu-*.mp4}`
- **Overlays passed `make-layer` alpha gate** (yuva + corners clear + soft-alpha &lt; 3%). Do not compile foggy overlays — fix HTML (strip soft shadows) first (DL-069).
- **Backdrop (DL-070):** prefer `hard-scrim` baked opaque in `ov-*.mov`. Optional CapCut `a-roll-blur`: mask A-roll to scrim bbox → Blur — never bake `filter:blur` into overlay.
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
**Scope = A-roll talking-head only.** Never run `remove-background` / CapCut matting on `ov-*.mov` to “clean” overlay fog — that is a soft-shadow authoring bug (DL-069 / `make-layer`).

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
| `cu-*` | `cu-*.mp4` on **same main track** as A (no gap — CapCut magnetic main collapses holes) | — |

## Banned
- Cloud `/opt/cursor/artifacts` as CapCut source
- Relying on CLI `render` / `export` for final delivery
- VO/Whisper as compile requirement V1.1
- Deep effects on A-roll in V1.1 (HF motion stays on `ov-*`/`cu-*` only)
- Compiling overlays that fail soft-alpha &lt; 3% gate
- Putting `cu-*` on a parallel track (main-track gap → CapCut collapses timeline)
- Using A-roll cutout tools to “fix” overlay halo

## Limitations
- Local Mac only; Desktop remains final export.
- Requires make-layer alpha gate pass before compile.
- VO/captions are not compiled — add by hand in CapCut.

## Troubleshooting
| Error / symptom | Cause | Fix |
|---|---|---|
| Foggy overlay in CapCut | Soft alpha / shadows in HTML | Fix layer HTML; re-render; re-run alpha gate |
| capcut-cli doctor fail | CLI/Desktop path drift | Fix install; re-run doctor |
| Wrong a-roll window | Marker / a_roll mismatch | Align script markers with layer table |
