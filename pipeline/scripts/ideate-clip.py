#!/usr/bin/env python3
"""One-Command Pre-Gate1 Orchestrator (Content Engine v2.0, F6, DL-082).

Unifies the pre-Gate1 research & multi-script preparation flow for @hi.oneup and @vanhiep.tech:
  1. Checks Radar/Trend freshness in research/trends/ (warns if newest snapshot > 48h old).
  2. Runs Reverse Hot-Trend Matching (`trend-match.py`, F2) to surface Top 3 natural
     `(Fresh Trend < 72h ↔ Unproduced Lesson)` pairs (or Pain-Wave Fallback) respecting LIGHT/DARK ≤ 2.
  3. When `--idea` is given (after Hiệp picks 1 pair at Gate 0), prepares the 3-Writer
     Multi-Script Tournament Arena (`script-arena.py prepare`, F3) with 3 contrasting Archetypes (`M1,M2,M4`).

CLI:
  # Phase 0: Check trend freshness + get Top 3 natural pairs for Gate 0 selection
  python3 pipeline/scripts/ideate-clip.py --clip clip-07 [--date YYYY-MM-DD] [--trend "<trend>"]

  # Phase 1: After choosing an idea, spawn 3 contrasting Pure-Voice Writer briefs into <clip>/archive/arena/
  python3 pipeline/scripts/ideate-clip.py --clip clip-07 --idea "<chủ đề>" [--archetypes M1,M2,M4]
      [--topic <slug>] [--trend "<trend>"] [--fact-lock <path>] [--out-dir <dir>]
"""
import datetime as dt
import importlib.util
import json
import re
import sys
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65

ROOT = P.ROOT
TRENDS_DIR = ROOT / "research/trends"
STALE_HOURS = 48.0


def _load_mod(name, rel_path):
    p = ROOT / rel_path
    sp = importlib.util.spec_from_file_location(name, str(p))
    mod = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(mod)
    return mod


def check_radar_freshness(ref_date=None, trends_dir=None, stale_hours=STALE_HOURS):
    """Return freshness dict for the newest YYYY-MM-DD folder in research/trends/."""
    base = Path(trends_dir or TRENDS_DIR)
    ref = dt.date.fromisoformat(ref_date) if ref_date else dt.date.today()
    latest = None
    if base.exists():
        for d in sorted(base.iterdir(), reverse=True):
            if d.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", d.name):
                try:
                    latest = dt.date.fromisoformat(d.name)
                    break
                except ValueError:
                    continue
    if not latest:
        return {"latest_date": None, "age_hours": None, "stale": True, "hint": "Chưa có snapshot trend nào → chạy `python3 pipeline/scripts/radar-fetch.py` trước."}
    age_h = round(max(0, (ref - latest).days) * 24.0, 1)
    stale = age_h > stale_hours
    hint = f"Snapshot mới nhất `{latest.isoformat()}` (~{age_h:.0f}h > {int(stale_hours)}h) → nên chạy `python3 pipeline/scripts/radar-fetch.py` để bắt trend tươi." if stale else f"Dữ liệu trend tươi (`{latest.isoformat()}`, ~{age_h:.0f}h)."
    return {"latest_date": latest.isoformat(), "age_hours": age_h, "stale": stale, "hint": hint}


def run_ideate(
    clip_slug,
    ref_date=None,
    idea=None,
    archetypes=("M1", "M2", "M4"),
    channel="hi",
    topic=None,
    trend=None,
    fact_lock=None,
    out_dir=None,
    trends_dir=None,
):
    tm = _load_mod("trend_match", "pipeline/scripts/trend-match.py")
    sa = _load_mod("script_arena", "pipeline/scripts/script-arena.py")

    freshness = check_radar_freshness(ref_date=ref_date, trends_dir=trends_dir)
    match_res = tm.match_trends(
        ref_date=ref_date,
        explicit_trends=[trend] if trend else None,
        trends_dir=trends_dir,
    )

    arena_written = []
    if idea:
        dest = Path(out_dir) if out_dir else (ROOT / "content/clips" / clip_slug / "archive/arena")
        fl_txt = Path(fact_lock).read_text(encoding="utf-8") if fact_lock and Path(fact_lock).exists() else None
        arena_written = sa.prepare_arena(
            idea=idea,
            out_dir=dest,
            archetypes=archetypes,
            channel=channel,
            topic=topic,
            trend=trend,
            fact_lock_text=fl_txt,
        )

    return {
        "clip": clip_slug,
        "freshness": freshness,
        "trend_match": match_res,
        "arena_briefs": arena_written,
    }


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if a else 2
    def opt(n, d=None):
        return a[a.index(n) + 1] if n in a else d

    clip_slug = opt("--clip", "clip-next")
    ref_date = opt("--date", dt.date.today().isoformat())
    idea = opt("--idea")
    archs = ("M2", "M6", "M7") if "--soul" in a else (tuple(opt("--archetypes").split(",")) if opt("--archetypes") else ("M1", "M2", "M6"))

    res = run_ideate(
        clip_slug=clip_slug,
        ref_date=ref_date,
        idea=idea,
        archetypes=archs,
        channel=opt("--channel", "hi"),
        topic=opt("--topic"),
        trend=opt("--trend"),
        fact_lock=opt("--fact-lock"),
        out_dir=opt("--out-dir"),
    )
    if "--json" in a:
        print(json.dumps(res, ensure_ascii=False, indent=1))
        return 0

    tm = _load_mod("trend_match", "pipeline/scripts/trend-match.py")
    print(f"# Ideate Pre-Gate1: {clip_slug}\n")
    print(f"- **Độ tươi Radar:** {'⚠ ' if res['freshness']['stale'] else '✔ '}{res['freshness']['hint']}\n")
    print(tm.format_report(res["trend_match"]))
    if res["arena_briefs"]:
        print(f"## Đấu trường Đa Kịch Bản đã khởi tạo ({len(res['arena_briefs'])} Writers)\n")
        for w in res["arena_briefs"]:
            print(f"- Writer **{w['label']}** (`{w['archetype']}` · *{w['color']}*): `{w['path']}`")
    else:
        print("→ Chọn 1 cặp ở bảng trên rồi chạy lại với `--idea \"<chủ đề>\"` để mở Đấu trường 3 Kịch bản Song song.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
