#!/usr/bin/env python3
"""Closed-Loop Memory Sync (Content Engine v2.0, F5, DL-082).

Automates two learning loops so mistakes rejected once by Hiệp never recur:
  1. `sync-feedback`: parses `<clip>/final/feedback.md` and appends new rejected samples into
     `research/review-golden/index.json` (deduplicated by clip + version, updating `counts`).
  2. `sync-3d`: reads `content/published/` metrics and reports 3D `win_rate` across
     Storytelling Archetype (`M1..M5`) × Hook Mechanism × CTA Style, plus updates `research/blueprints/index.json` via `arc_library.sync_published`.

CLI:
  python3 pipeline/scripts/golden-sync.py sync-feedback --clip content/clips/clip-06-bong-hoa-chua-no [--dry-run]
  python3 pipeline/scripts/golden-sync.py sync-3d [--published-dir content/published] [--json]
"""
import datetime as dt
import json
import re
import sys
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65
import arc_library as ARC

ROOT = P.ROOT
GOLDEN_INDEX = ROOT / "research/review-golden/index.json"
STYLE_PAIRS = ROOT / "resources/vn-spoken/style-pairs.md"


def parse_feedback_md(path):
    """Parse `<clip>/final/feedback.md` table rows `| ngày | bản | góp ý | hành động |`."""
    p = Path(path)
    if not p.exists():
        return []
    rows = []
    for ln in p.read_text(encoding="utf-8").splitlines():
        if not ln.startswith("|") or re.match(r"^\|[-\s|:]+\|$", ln):
            continue
        c = [x.strip() for x in ln.strip("|").split("|")]
        if len(c) >= 4 and re.match(r"20\d\d-\d\d-\d\d", c[0]):
            rows.append({
                "date": c[0],
                "version": c[1],
                "quote": c[2],
                "action": c[3],
            })
    return rows


def _clip_code(clip_dir):
    m = re.search(r"(clip-\d+)", Path(clip_dir).name)
    return m.group(1) if m else Path(clip_dir).name


def _sample_id(clip_code, version):
    cnum = re.sub(r"^clip-0*", "c0", clip_code) if re.match(r"^clip-0\d$", clip_code) else clip_code.replace("clip-", "c")
    ver_slug = re.sub(r"[^a-z0-9]+", "-", (version or "v").lower()).strip("-")[:24]
    return f"r-{cnum}-{ver_slug}"


def recompute_counts(doc):
    samples = doc.get("samples") or []
    approved = sum(1 for s in samples if s.get("verdict") == "approved")
    rejected = sum(1 for s in samples if s.get("verdict") == "rejected")
    rej_found = sum(1 for s in samples if s.get("verdict") == "rejected" and s.get("found"))
    rej_miss = rejected - rej_found
    doc["counts"] = {
        "total": len(samples),
        "approved": approved,
        "rejected": rejected,
        "rejected_with_excerpt": rej_found,
        "rejected_not_found": rej_miss,
    }
    return doc


def sync_feedback(clip_dir, golden_path=None, dry_run=False):
    """Ingest rejection feedback rows from `<clip>/final/feedback.md` into `research/review-golden/index.json`."""
    cdir = Path(clip_dir)
    fb_path = cdir / "final/feedback.md"
    g_path = Path(golden_path or GOLDEN_INDEX)
    rows = parse_feedback_md(fb_path)
    if not rows:
        return {"added": 0, "skipped": 0, "total": 0, "ids": []}

    doc = json.loads(g_path.read_text(encoding="utf-8")) if g_path.exists() else {"id": "review-golden.index", "samples": []}
    samples = doc.setdefault("samples", [])
    existing_ids = {s.get("id") for s in samples}
    clip_code = _clip_code(cdir)
    added_ids = []
    skipped = 0

    for r in rows:
        # Only sync genuine rejections / critiques (skip pure 'Chốt' approval rows if any)
        if re.search(r"^\s*(?:chốt|ok|đạt)\s*$", r["quote"], re.I):
            skipped += 1
            continue
        sid = _sample_id(clip_code, r["version"])
        if sid in existing_ids:
            skipped += 1
            continue
        dl_m = re.search(r"\b(DL-\d+|L-\d+)\b", r["action"] + " " + r["quote"])
        rel_src = str(fb_path.resolve().relative_to(ROOT)) if ROOT in fb_path.resolve().parents else str(fb_path)
        samples.append({
            "id": sid,
            "verdict": "rejected",
            "clip": clip_code,
            "version": r["version"],
            "source": rel_src,
            "hiep_quote": r["quote"],
            "quote_kind": "verbatim",
            "lesson": r["action"],
            "lesson_id": dl_m.group(1) if dl_m else "",
            "excerpt_file": None,
            "found": False,
        })
        existing_ids.add(sid)
        added_ids.append(sid)

    doc["updated"] = dt.date.today().isoformat()
    recompute_counts(doc)
    if not dry_run and added_ids:
        g_path.parent.mkdir(parents=True, exist_ok=True)
        g_path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return {"added": len(added_ids), "skipped": skipped, "total": doc["counts"]["total"], "ids": added_ids}


def compute_3d_win_rates(published_dir=None, min_views=ARC.DEFAULT_MIN_VIEWS, min_completion=ARC.DEFAULT_MIN_COMPLETION):
    """Compute 3D win_rate across Archetype (M1..M5), Hook Mechanism, and CTA Style from content/published/*.json."""
    pdir = Path(published_dir or ARC.PUBLISHED)
    dims = {"archetype": {}, "hook_mechanism": {}, "cta_style": {}}
    if not pdir.exists():
        return {"records": 0, "dimensions": dims}

    records = []
    for f in sorted(pdir.glob("*.json")):
        try:
            doc = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        items = doc if isinstance(doc, list) else doc.get("clips") or doc.get("items") or [doc]
        for it in items:
            if isinstance(it, dict):
                records.append(it)

    for rec in records:
        win = ARC.is_win(
            {
                "views": ARC._parse_num(rec.get("views_7d") if rec.get("views_7d") is not None else rec.get("views")),
                "completion_pct": ARC._parse_pct(rec.get("completion_pct")),
                "saves": ARC._parse_num(rec.get("saves")),
                "shares": ARC._parse_num(rec.get("shares")),
            },
            min_views=min_views,
            min_completion=min_completion,
        )
        for dim in ("archetype", "hook_mechanism", "cta_style"):
            val = (rec.get(dim) or "").strip()
            if not val:
                continue
            st = dims[dim].setdefault(val, {"uses": 0, "wins": 0, "win_rate": None})
            st["uses"] += 1
            st["wins"] += 1 if win else 0
            st["win_rate"] = ARC._compute_win_rate(st["uses"], st["wins"])

    return {"records": len(records), "dimensions": dims}


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if a else 2
    def opt(n, d=None):
        return a[a.index(n) + 1] if n in a else d
    cmd = a[0]
    if cmd == "sync-feedback":
        clip = opt("--clip")
        if not clip:
            print("sync-feedback cần --clip <path>", file=sys.stderr)
            return 2
        res = sync_feedback(clip, golden_path=opt("--golden"), dry_run="--dry-run" in a)
        if "--json" in a:
            print(json.dumps(res, ensure_ascii=False, indent=1))
        else:
            print(f"golden-sync: +{res['added']} mẫu mới (bỏ qua {res['skipped']}) · tổng {res['total']} mẫu"
                  + (" (dry-run)" if "--dry-run" in a else ""))
            if res["ids"]:
                print("  IDs:", ", ".join(res["ids"]))
        return 0
    if cmd == "sync-3d":
        res = compute_3d_win_rates(published_dir=opt("--published-dir"))
        if "--json" in a:
            print(json.dumps(res, ensure_ascii=False, indent=1))
        else:
            print(f"golden-sync 3D win_rate ({res['records']} published JSON records):")
            for dim, tbl in res["dimensions"].items():
                print(f"  [{dim}]")
                for k, st in sorted(tbl.items(), key=lambda kv: -(kv[1]["win_rate"] or 0)):
                    wr = f"{st['win_rate']:.0%}" if st["win_rate"] is not None else "—"
                    print(f"    - {k}: {st['wins']}/{st['uses']} ({wr})")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
