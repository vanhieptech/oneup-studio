---
title: "clip-05 r15.2 text-only archive and check audit"
date: 2026-11-08
type: archive-audit
tags: [clip-05, r15.2, text-only, storage]
status: draft
source: "News exact byte copies, unchanged check-rules.py and duration_policy.py; source-owner reports attributed only"
---
# clip-05 r15.2 — archive and text-only checks

Audit performed 2026-11-08T21:52:41.315487+07:00 (Asia/Saigon). No Chốt inferred from agent messages. Human review = **CHƯA KIỂM**. This is NOT full production PASS.

## Canonical inventory
- Frozen draft: `content/clips/clip-05-hoc-mot-dem/archive/r15/clip05-r15.2-full-draft-2026-11-08.md`.
- Manifest: `content/clips/clip-05-hoc-mot-dem/archive/r15/clip05-r15.2-hash-manifest-2026-11-08.json`. Source mtimes preserved with `cp -p`; separate verification timestamps recorded. Originals remain in place.
- Lineage: `archive/r14/` → `archive/concept-reset/` → `archive/r15/`. r14.3 stopped: supplied blocker + counts only; no full r14.3 script found, not invented. Reset B and round2 E concept/review files preserved.
- 58 original text/JSON files archived unchanged; generated adapters/check outputs kept separately under `archive/r15/checks-2026-11-08/`.
- Three source locks independently compared with expected commits and newly fetched origin/main bytes; all identical. See `clip05-r15.2-source-lock-verification-2026-11-08.json`.

## Exact SHA verification
File SHA `87885dd3f4e0b1d847e7971c0476878f85691e3178b55ff7cbae6f6a096f7dc2`; spoken SHA `3a6f280daede0ea30db9d095643deb7f77868981ea22b804991b3b425cf7a78e`: both independently reproduced. Extraction: bytes after entire `<!-- SPOKEN_START -->` line and LF through before closing marker, retaining final LF. No strip/normalization. 439 whitespace units, 9 paragraphs/beats, 21 sentences in source index. New adapter's 9 spoken strings equal all 9 frozen payload paragraphs exactly.

Deep report hash `6a72bbd77fc6f191f6d05f8384eea7ead158822e0757b3744c71c681405bfcf2` matched. Its original mtime 08/11/2026 14:36:04.393667 Asia/Saigon is NOT verification time. Deep's 21:50 Asia/Saigon re-verification is an agent claim, not a new act by News.

Social report hash `d6c27b8092929e2b91ef414a3be1f59ee7fd6f96800ff9acca1c7f10f06bf70f` matched; supersedes pending-report status. Social claims “ĐẠT nguồn Social trong phạm vi hẹp”: only S05, its caption, storyboard b02. NOT overall PASS. Social's live evidence remains historical 08/11/2026 14:20:51 Asia/Saigon pinned `a32f51f558ff144a8448f6a00eeb900e2ad23542`, not a fresh live check. No current hotness, participant-pain, memory or efficacy claim added. Mac **CHƯA KIỂM**.

## Safe pre-Chốt checks
All commands below run from `/workspace/oneup-studio`. Only documented draft-file flags used, not full clip/spec mode. See JSON for counts, exit codes and exact flags.

| flag | checks | errors | warnings | exit |
|---|---:|---:|---:|---:|
| --subjects | 1 | 0 | 0 | 0 |
| --l088 | 7 | 0 | 0 | 0 |
| --trend | 6 | 1 | 0 | 1 |
| --flow | 6 | 0 | 1 | 0 |
| --clarity | 5 | 0 | 2 | 0 |
| --link | 2 | 0 | 1 | 0 |
| --repeat | 4 | 0 | 1 | 0 |
| --evidence | 2 | 0 | 0 | 0 |
| --choppy | 2 | 0 | 0 | 0 |
| --fresh | 3 | 0 | 0 | 0 |

### Exact commands
```sh
python3 pipeline/scripts/check-rules.py --subjects content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/clip-05-r15.2-trend-adapter.md --out content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/subjects-output.txt
python3 pipeline/scripts/check-rules.py --l088 content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/clip-05-r15.2-trend-adapter.md --out content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/l088-output.txt
python3 pipeline/scripts/check-rules.py --trend content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/clip-05-r15.2-trend-adapter.md --out content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/trend-output.txt
python3 pipeline/scripts/check-rules.py --flow content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/clip-05-r15.2-trend-adapter.md --out content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/flow-output.txt
python3 pipeline/scripts/check-rules.py --clarity content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/clip-05-r15.2-trend-adapter.md --out content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/clarity-output.txt
python3 pipeline/scripts/check-rules.py --link content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/clip-05-r15.2-trend-adapter.md --out content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/link-output.txt
python3 pipeline/scripts/check-rules.py --repeat content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/clip-05-r15.2-trend-adapter.md --out content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/repeat-output.txt
python3 pipeline/scripts/check-rules.py --evidence content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/clip-05-r15.2-trend-adapter.md --out content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/evidence-output.txt
python3 pipeline/scripts/check-rules.py --choppy content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/clip-05-r15.2-trend-adapter.md --out content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/choppy-output.txt
python3 pipeline/scripts/check-rules.py --fresh content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/clip-05-r15.2-trend-adapter.md --against content/clips/clip-05-hoc-mot-dem/archive/r11/opencreator-clip05-script-r11.4-draft-2026-11-07.md content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/clip-05-r12-actual-spoken-adapter.md content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/clip-05-r14.2-actual-spoken-adapter.md --out content/clips/clip-05-hoc-mot-dem/archive/r15/checks-2026-11-08/fresh-output.txt
```

### Warnings and unresolved fields
- **--trend FAIL (1 error)**: frozen draft supplies no P/F hook-pattern identifier. New adapter deliberately records `hook_pattern: UNMAPPED_PENDING_SCRIPT_OWNER`, rather than inventing an unrelated active pattern to pass. Script owner / Reviewer needs to supply supported mapping; no spoken rewrite requested. Trend ID, b02 trend placement, actual spoken phrase and example path checks passed mechanically. Example path only documents press lifestyle context, not channel-viewer pain or efficacy.
- --flow: b03/b08 opening not automatically linked.
- --clarity: hook question precedes concrete scenario; 28-unit S05, 32-unit S17 and 26-unit S18 flagged. S17/S18 consecutive long payoff sentences need actual human listening.
- --link: S03→S04 and S05→S06 (2/20 adjacent pairs).
- --repeat: “trong thí nghiệm” ×5, “sau một tuần” ×2, “một tuần tự” ×2, “tuần tự viết” ×2, “hơn ở mốc” ×2, “kể sau vài” ×2, “sau vài ngày” ×3, “cho tỷ lệ” ×3.
- --fresh: all THREE prior actual texts compared. r11.4 directly parses 7 beats/150 units. r12 and r14.2 full reports do NOT directly parse (0); exact SPOKEN-block paragraph adapters parse 7/142 and 9/501 respectively. No silent skipping. Scores (hook, chain): r11.4 0.060606/0.071284; r12 0.111111/0.082692; r14.2 0.256410/0.340830; all <0.5. Parse evidence retains source hashes and paths.
- Checker `--out` is plain text, not JSON. Initial orchestration failed JSON decoding after successful subjects check; corrected output extension and reran all flags. Checker code unchanged.

## Duration estimate — ƯỚC ONLY
Reproduced `pipeline.duration_policy.estimated_total(439, endcard_seconds=14, pause_seconds=11.7, transition_seconds=4)` and `duration_status(total)`: **181.079310s** at default descriptive 2.9 units/s. Sensitivity at 2.5 units/s: **205.30s**. Both exceed 120–180s target → WARNING only; both estimates <300s. Do not speed reading to force target. No actual audio or duration certified.

## Not checked / not produced
Human read-aloud, stranger hook test, one-listen comprehension, actual timing, full spec/clip checker, production images/assets/adapters/media, TTS/voice, static previews, render, publish: **CHƯA KIỂM / NOT RUN**. No spec generation or build-final/stage plans. Existing final files not touched. Mac not accessed/synced; no push.

## Storage and source control
Archive frozen files have incomplete/absent frontmatter in some originals. Preserving exact bytes takes precedence over backfill: storage check failures are reported, not fixed by altering originals. No checker suppression or exemptions added. INDEX generated normally. Protected Reviewer logs stashed around initial rebase from 8ff76986 onto freshly fetched a32f51f; patch before/after matched. Only this stream's explicit paths may be committed.

### Observed storage results
`python3 pipeline/scripts/check-assets.py --list` baseline: rule-59 PASS (0 external), rule-65 **390 violations**, exit 1. After archive: rule-59 PASS (0 external), rule-65 **419 violations**, exit 1. Delta: **30 new frontmatter violations from exact original copies**, minus 1 stale INDEX issue resolved. No new layout/duplicate violations. See storage-delta.json and raw before/after outputs. Frozen files intentionally not backfilled. An earlier baseline command was interrupted by parent steering; no completed result was claimed from that attempt.

`python3 pipeline/scripts/build-index.py`: 418 docs / 66 rules / 7 clips. `python3 pipeline/scripts/build-index.py --check`: exit 0, INDEX up to date. Generator also discovered seven pre-existing ignored snapshot/reference docs absent from former index; these are index entries only, not files copied, changed or committed from those workstreams.

`git diff --cached --check`: exit 2, one whitespace warning in the exact original `archive/r14/clip-05-r14.1-checker-input.md:41` (blank line at EOF). Preserved original bytes rather than normalizing. Generated audit/checker code not changed to hide this.
