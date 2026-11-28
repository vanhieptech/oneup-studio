---
title: "make-video v3 benchmark — clip-08 preview / storyboard round-trip"
date: 2026-11-28
type: log
tags: [benchmark, make-video, dl-094, clip-08]
status: ready
source: "oneup-studio (Phase-2 make-video v3)"
id: runs-make-video-v3-benchmark-2026-11-28
updated: 2026-11-28
---
# make-video v3 benchmark (2026-11-28)

Clip: `content/clips/clip-08-dien-thoai-up-ban/` · machine: local Mac · `DL-094`.

## Storyboard size

| File | Lines |
|---|---|
| `templates/storyboard.yaml` (example) | 74 |
| `final/storyboard.yaml` (clip-08 decompile, 19 beats) | 278 |
| `final/spec.json` (clip-08) | 1417 |

Round-trip: `--decompile` → `storyboard.yaml` → `--merge-existing` compile → `check-rules.py` on temp clip dir **0 ✖** (PASS). Original `spec.json` kept; storyboard is the compact edit surface.

## `build-final.py --preview` (clip-08)

Output: `final/out/clip-08-final-preview-540p.mp4` (540×960, 24fps, CRF 28) + `final/contact-sheet.png`.

| Run | Wall time | Notes |
|---|---|---|
| Cold (no `.build-cache.json`, chunk miss) | **221.3 s** | Full Remotion chunk render at 0.5 scale; voice cache hit |
| Warm (no text change) | **8.4 s** | `cache hit: 19/19 beats`; remotion part cache hit; remux + contact sheet |
| Warm + 1 sentence tweak (`b03a`) | **52.5 s** | `cache hit: 18/19`, `rebuilt: [b03a]`; scene cache `13/14` chunk hit |

Target «preview < 30 s» met on **warm** path (Gate 2 iterate). Cold first paint still dominated by Remotion chunk encode; subsequent edits use beat-hash + scene cache.

## CLI

```bash
python3 pipeline/scripts/spec-compile.py --decompile <clip>/final/spec.json --out <clip>/final/storyboard.yaml
python3 pipeline/scripts/spec-compile.py --in <clip>/final/storyboard.yaml --out <clip>/final/spec.json --merge-existing
python3 pipeline/scripts/build-final.py <clip>/final/spec.json --preview
python3 pipeline/scripts/build-final.py <clip>/final/spec.json   # full after preview OK
```
