#!/usr/bin/env python3
"""Multi-Video Pattern Synthesis: cross-compare ≥ 3 teardowns → weekly synthesis report + Gate 0 weights.

  pattern-synthesize.py [--trends-dir research/trends] [--min-teardowns 3]
                        [--out research/trends/weekly-synthesis.md]
                        [--weights-out research/trends/weekly-synthesis.json]
                        [--include-selftest] [--force]

Reads all `research/trends/*/teardowns/*.json` (excluding `selftest-*` unless `--include-selftest`),
cross-compares them across `direct_niche`, `cross_niche_craft`, and `anti_pattern` roles, and extracts:
  1. Top 5 winning hook mechanisms (weighted by outlier ratio / views / frequency).
  2. Top 3 smoothest transition patterns (from beat transitions & craft_transfer.sentence_rhythm).
  3. Cross-niche craft takeaways (metaphors, 3–5s pacing, interrupts/10s, anti-patterns to avoid).
  4. Priority weights (`arc_weights`, `hook_weights`) consumed automatically by `pipeline/scripts/gate0.py`.
"""
import collections
import datetime as dt
import json
import re
import statistics
import sys
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65

ROOT = P.ROOT
TRENDS = ROOT / "research/trends"
DEFAULT_OUT = TRENDS / "weekly-synthesis.md"
DEFAULT_WEIGHTS = TRENDS / "weekly-synthesis.json"
DEFAULT_MIN = 3


def _norm_key(s):
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def _clip_weight(td):
    """Compute evidence weight for one teardown from outlier ratio or views."""
    ap = td.get("apify") or {}
    fans = (ap.get("author") or {}).get("fans") or 0
    views = ap.get("play_count") or 0
    ratio = ap.get("outlier_ratio") or (round(views / fans, 2) if fans and views else None) or ap.get("outlier")
    if ratio and float(ratio) > 0:
        return round(min(float(ratio), 20.0), 2)
    if views and float(views) > 0:
        return round(min(1.0 + float(views) / 100_000.0, 10.0), 2)
    return 1.0


def _classify_transition(text):
    t = _norm_key(text)
    if not t:
        return None
    if any(k in t for k in ("jump cut", "cắt cứng", "hard cut", "tiêu đề", "số thứ tự", "thứ hai", "cuối cùng")):
        return "Jump cut + nhãn số/tiêu đề ngắn (đổi đạo cụ / tư thế)"
    if any(k in t for k in ("câu hỏi", "?", "hỏi", "tại sao", "vì sao")):
        return "Câu hỏi lửng mở vòng (Open Loop Question)"
    if any(k in t for k in ("nhưng", "khoan", "ngược", "lật", "hóa ra", "thật ra")):
        return "Từ nối bẻ lái / lật giả định («Nhưng mà khoan», «Hóa ra»)"
    if any(k in t for k in ("fade", "mờ tối", "ngắt nhịp", "dừng")):
        return "Ngắt nhịp tách khối sang phần kết / CTA"
    if any(k in t for k in ("ví dụ", "như mình", "thí nghiệm", "chứng minh", "zoom")):
        return "Đẩy thẳng từ nhận định sang ví dụ / bằng chứng vật lý"
    return "Chuyển cảnh trực tiếp theo mạch nhân quả"


def load_teardowns(trends_dir=TRENDS, include_selftest=False):
    """Load teardown JSON files under `<trends_dir>/*/teardowns/*.json`."""
    tdir = Path(trends_dir)
    if not tdir.exists():
        return []
    out = []
    for f in sorted(tdir.glob("*/teardowns/*.json")):
        if not include_selftest and f.stem.startswith("selftest"):
            continue
        try:
            doc = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        ap = doc.get("apify") or {}
        role = doc.get("role") or ap.get("role") or "direct_niche"
        out.append({
            "id": f.stem,
            "path": str(f.relative_to(ROOT)) if ROOT in f.resolve().parents else str(f),
            "date": (doc.get("_meta") or {}).get("date") or f.parent.parent.name,
            "role": role,
            "data": doc,
        })
    return out


def synthesize(teardowns):
    """Cross-compare teardowns and compute ranked hooks, transitions, craft insights, and Gate 0 weights."""
    hook_buckets = collections.defaultdict(lambda: {"count": 0, "weight": 0.0, "examples": [], "roles": set()})
    trans_buckets = collections.defaultdict(lambda: {"count": 0, "weight": 0.0, "examples": []})
    arc_weights = collections.defaultdict(float)
    craft_metaphors = []
    craft_pacing = []
    anti_notes = []
    interrupts_vals = []
    role_counts = collections.Counter()

    for item in teardowns:
        d = item["data"]
        role = item["role"]
        role_counts[role] += 1
        w = _clip_weight(d)
        cid = item["id"]
        meta = d.get("_meta") or {}
        arc_id = meta.get("arc")

        if role == "anti_pattern":
            hook_sp = (d.get("hook") or {}).get("spoken") or ""
            why = "; ".join(x.get("claim", "") for x in (d.get("why_it_works") or [])[:2] if isinstance(x, dict))
            anti_notes.append({"id": cid, "hook": hook_sp[:120], "note": why or "câu view / nội dung rỗng cần tránh"})
            continue

        # 1. Hook mechanism
        hk = d.get("hook") or {}
        arc = d.get("arc") or {}
        mech = (arc.get("hook_mechanism") or hk.get("mechanism") or "khác").strip()
        mech_key = mech.split("(")[0].strip().lower() or "khác"
        hb = hook_buckets[mech_key]
        hb["label"] = hb.get("label") or mech
        hb["count"] += 1
        hb["weight"] = round(hb["weight"] + w * (1.15 if role == "cross_niche_craft" else 1.0), 2)
        hb["roles"].add(role)
        ex_line = (hk.get("on_screen_text") or hk.get("spoken") or "").strip()[:100]
        hb["examples"].append({"id": cid, "role": role, "ratio_w": w, "snippet": ex_line})

        # 2. Transitions
        beats = d.get("beats") or d.get("spine") or []
        for b in beats:
            tr = (b.get("transition") or "").strip()
            cat = _classify_transition(tr)
            if cat:
                tb = trans_buckets[cat]
                tb["count"] += 1
                tb["weight"] = round(tb["weight"] + w * 0.5, 2)
                if len(tb["examples"]) < 3:
                    tb["examples"].append(f"`{cid}`: {tr[:90]}")

        # 3. Craft & pacing
        wp = d.get("winning_points") or {}
        if wp.get("interrupts_per_10s") is not None:
            try:
                interrupts_vals.append(float(wp["interrupts_per_10s"]))
            except (TypeError, ValueError):
                pass
        ct = d.get("craft_transfer") if isinstance(d.get("craft_transfer"), dict) else {}
        bm = wp.get("best_metaphor")
        met = ct.get("metaphor_transfer") or (bm.get("text") if isinstance(bm, dict) else (bm or ""))
        if met:
            craft_metaphors.append({"id": cid, "role": role, "text": str(met).strip()[:180]})
        if ct.get("pacing_3_5s"):
            craft_pacing.append({"id": cid, "role": role, "text": str(ct["pacing_3_5s"]).strip()[:180]})

        # 4. ARC weight for Gate 0
        if arc_id:
            arc_weights[arc_id] = round(arc_weights[arc_id] + w, 2)

    top_hooks = sorted(
        [
            {
                "key": k,
                "mechanism": v["label"],
                "count": v["count"],
                "weight": v["weight"],
                "roles": sorted(v["roles"]),
                "examples": v["examples"][:3],
            }
            for k, v in hook_buckets.items()
        ],
        key=lambda x: (-x["weight"], -x["count"], x["mechanism"]),
    )[:5]

    top_transitions = sorted(
        [
            {"pattern": k, "count": v["count"], "weight": v["weight"], "examples": v["examples"]}
            for k, v in trans_buckets.items()
        ],
        key=lambda x: (-x["weight"], -x["count"], x["pattern"]),
    )[:3]

    avg_int = round(statistics.mean(interrupts_vals), 2) if interrupts_vals else None
    return {
        "teardown_count": len(teardowns),
        "role_counts": dict(role_counts),
        "top_hooks": top_hooks,
        "top_transitions": top_transitions,
        "avg_interrupts_per_10s": avg_int,
        "craft_metaphors": craft_metaphors[:6],
        "craft_pacing": craft_pacing[:6],
        "anti_patterns": anti_notes[:5],
        "arc_weights": dict(sorted(arc_weights.items(), key=lambda kv: -kv[1])),
        "hook_weights": {h["key"]: h["weight"] for h in top_hooks},
    }


def render_markdown(res, date):
    lines = [
        "---",
        f'title: "Tổng hợp mẫu số chung đa video (Weekly Synthesis — {date})"',
        f"date: {date}",
        "id: trends.weekly-synthesis",
        "type: trend-digest",
        "status: active",
        f"updated: {date}",
        "tags: [trends, synthesis, weekly, arc, gate-0, cross-niche]",
        'source: "pipeline/scripts/pattern-synthesize.py (đối chiếu chéo các bản teardown)"',
        "---",
        f"# Tổng hợp đa video — {date}",
        "",
        f"Đối chiếu **{res['teardown_count']} bản teardown** "
        f"(`direct_niche`: {res['role_counts'].get('direct_niche', 0)}, "
        f"`cross_niche_craft`: {res['role_counts'].get('cross_niche_craft', 0)}, "
        f"`anti_pattern`: {res['role_counts'].get('anti_pattern', 0)}). "
        f"Trọng số ưu tiên tự động nạp vào `pipeline/scripts/gate0.py` qua `research/trends/weekly-synthesis.json`.",
        "",
        "## 1. Top 5 kiểu Hook đang thắng",
        "| # | Cơ chế Hook | Số clip | Trọng số | Nhóm kênh | Ví dụ đại diện |",
        "|---|---|---:|---:|---|---|",
    ]
    if res["top_hooks"]:
        for i, h in enumerate(res["top_hooks"], 1):
            ex = "; ".join(f"`{e['id']}` ({e['snippet'][:60]})" for e in h["examples"][:2])
            lines.append(f"| {i} | **{h['mechanism']}** | {h['count']} | {h['weight']:.2f} | {', '.join(h['roles'])} | {ex} |")
    else:
        lines.append("| — | chưa đủ dữ liệu | 0 | 0 | — | — |")

    lines += [
        "",
        "## 2. Top 3 cách chuyển ý mượt nhất",
        "| # | Kiểu chuyển ý | Lượt gặp | Trọng số | Minh họa |",
        "|---|---|---:|---:|---|",
    ]
    if res["top_transitions"]:
        for i, t in enumerate(res["top_transitions"], 1):
            lines.append(f"| {i} | {t['pattern']} | {t['count']} | {t['weight']:.2f} | {'; '.join(t['examples'][:2])} |")
    else:
        lines.append("| — | chưa đủ dữ liệu | 0 | 0 | — |")

    lines += ["", "## 3. Craft & Nhịp cắt học được (Direct + Cross-Niche)"]
    if res["avg_interrupts_per_10s"] is not None:
        lines.append(f"- Mật độ ngắt nhịp hình/âm thanh trung bình: **{res['avg_interrupts_per_10s']} lần / 10 giây**.")
    if res["craft_metaphors"]:
        lines.append("- **Ẩn dụ chuyển hóa khái niệm khó → đời thường:**")
        for m in res["craft_metaphors"]:
            lines.append(f"  - `{m['id']}` (`{m['role']}`): {m['text']}")
    if res["craft_pacing"]:
        lines.append("- **Kỹ thuật giữ nhịp 3–5s:**")
        for p in res["craft_pacing"]:
            lines.append(f"  - `{p['id']}` (`{p['role']}`): {p['text']}")
    if res["anti_patterns"]:
        lines += ["", "## 4. Anti-Pattern cần tránh"]
        for a in res["anti_patterns"]:
            lines.append(f"- `{a['id']}`: «{a['hook']}» — {a['note']}")

    lines += ["", "## 5. Trọng số ưu tiên nạp Gate 0 (`arc_weights`)"]
    if res["arc_weights"]:
        lines += ["| ARC | Trọng số ưu tiên |", "|---|---:|"]
        for aid, w in res["arc_weights"].items():
            lines.append(f"| `{aid}` | {w:.2f} |")
    else:
        lines.append("- Chưa có mã `ARC-NNN` gắn trong metadata teardown.")
    return "\n".join(lines) + "\n"


def run_synthesize(trends_dir=TRENDS, min_teardowns=DEFAULT_MIN, out_md=DEFAULT_OUT,
                   out_json=DEFAULT_WEIGHTS, include_selftest=False, force=False, date=None):
    date = date or dt.date.today().isoformat()
    tds = load_teardowns(trends_dir, include_selftest=include_selftest)
    if len(tds) < min_teardowns and not force:
        return {
            "ok": False,
            "skipped": True,
            "reason": f"chỉ có {len(tds)} bản teardown (cần ≥ {min_teardowns}; dùng --force để ép tổng hợp)",
            "teardown_count": len(tds),
        }
    res = synthesize(tds)
    res["date"] = date
    out_md_p = Path(out_md)
    out_json_p = Path(out_json)
    out_md_p.parent.mkdir(parents=True, exist_ok=True)
    out_json_p.parent.mkdir(parents=True, exist_ok=True)
    out_md_p.write_text(render_markdown(res, date), encoding="utf-8")
    out_json_p.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return {"ok": True, "skipped": False, "result": res, "out_md": out_md_p, "out_json": out_json_p}


def main():
    a = sys.argv[1:]
    if "-h" in a or "--help" in a:
        print(__doc__)
        return 0
    def opt(n, d=None):
        return a[a.index(n) + 1] if n in a else d
    res = run_synthesize(
        trends_dir=Path(opt("--trends-dir", str(TRENDS))),
        min_teardowns=int(opt("--min-teardowns", str(DEFAULT_MIN))),
        out_md=Path(opt("--out", str(DEFAULT_OUT))),
        out_json=Path(opt("--weights-out", str(DEFAULT_WEIGHTS))),
        include_selftest="--include-selftest" in a,
        force="--force" in a,
        date=opt("--date"),
    )
    if res["skipped"]:
        print(f"pattern-synthesize: bỏ qua — {res['reason']}")
        return 0
    r = res["result"]
    print(f"pattern-synthesize: đã tổng hợp {r['teardown_count']} teardown → {res['out_md']} (+ {res['out_json']})")
    if r["top_hooks"]:
        print("  Top hooks: " + ", ".join(f"{h['mechanism']} ({h['weight']:.2f})" for h in r["top_hooks"][:3]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
