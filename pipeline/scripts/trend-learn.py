#!/usr/bin/env python3
"""Trend learning helpers for skills/trend-digest (v2). Stdlib only, offline, deterministic.

  score <raw.json>                 add novelty/saturation/used flags to every item (in place) + print ranking
  stub  <ideas.json> <out_dir>     write video-engine plan stubs (one JSON per idea) for the top 1-2 ideas
  week  [YYYY-MM-DD]               print a 7-day roll-up (items, patterns, signals) for the Sunday synthesis

Repo root is inferred from this file's location. Trend dirs: research/trends/YYYY-MM-DD/raw.json.
"""
import json, re, sys, datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TRENDS = ROOT / "research" / "trends"

def norm(s):
    s = re.sub(r"[^\w\s]", " ", (s or "").lower())
    return " ".join(s.split())

def past_days(before):
    out = []
    for d in sorted(TRENDS.glob("20??-??-??")):
        if d.name < before and (d / "raw.json").exists():
            try: out.append((d.name, json.loads((d / "raw.json").read_text())))
            except Exception: pass
    return out

def used_bridge_ids():
    p = TRENDS / "ingest.md"
    ids = set()
    if p.exists():
        for line in p.read_text().splitlines():
            if line.startswith("|") and re.search(r"\|\s*(clip-\d\d|used)", line):
                ids.add(norm(line.split("|")[1]))
    return ids

def key(item):
    return norm(item.get("id") or item.get("text") or item.get("title"))

def score(path):
    p = Path(path); raw = json.loads(p.read_text())
    today = raw.get("date") or p.parent.name
    hist = past_days(today)
    d0 = dt.date.fromisoformat(today)
    used = used_bridge_ids()
    for it in raw.get("items", []):
        k = key(it); words = set(k.split())
        days = []
        for day, r in hist:
            for o in r.get("items", []):
                ok = key(o); ow = set(ok.split())
                if ok == k or (words and len(words & ow) / max(len(words | ow), 1) >= 0.6):
                    days.append(day); break
        last7 = [d for d in days if (d0 - dt.date.fromisoformat(d)).days <= 7]
        sat = it.get("saturation_signal")  # 0..1 set by agent from YT/X result counts, optional
        it["seen_days"] = len(days)
        it["novelty"] = round(1 / (1 + len(days)), 2)
        it["saturation"] = round(min(1.0, len(last7) / 4 + (sat or 0) * 0.5), 2)
        it["already_used"] = k in used
        num = lambda v: v if isinstance(v, (int, float)) else 0.5
        heat = num(it.get("heat_score")); fit = num(it.get("fit_score")); br = num(it.get("bridgeability"))
        it["rank_score"] = round(heat * fit * br * (0.5 + it["novelty"]) * (1 - 0.6 * it["saturation"]) * (0.3 if it["already_used"] else 1), 3)
    raw.setdefault("scoring", {})["method"] = "trend-learn.py v1: heat*fit*bridgeability*(0.5+novelty)*(1-0.6*saturation)*(0.3 if used)"
    p.write_text(json.dumps(raw, ensure_ascii=False, indent=1))
    for it in sorted(raw.get("items", []), key=lambda x: -x["rank_score"]):
        if it.get("safety", "ok") != "drop":
            print(f'{it["rank_score"]:.3f}  nov={it["novelty"]} sat={it["saturation"]} used={it["already_used"]}  {key(it)}')

def stub(ideas_path, out_dir):
    ideas = json.loads(Path(ideas_path).read_text())
    ideas = ideas.get("ideas", ideas) if isinstance(ideas, dict) else ideas
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    for i, idea in enumerate(ideas[:2], 1):
        beats = idea.get("beats") or [
            {"text": idea.get("hook_vi", "…"), "expression": "surprised", "action": "idle"},
            {"text": idea.get("moment_vi", "…"), "expression": "confused", "action": "idle"},
            {"text": idea.get("turn_vi", "…"), "expression": "happy", "action": "idle"}]
        scenes = []
        for j, b in enumerate(beats, 1):
            scenes.append({
                "id": f"s{j:02d}", "beat": f"{idea['id']}.b{j:02d}", "duration": b.get("duration", 4),
                "background": {"kind": b.get("background", "desk")},
                "camera": {"framing": "medium", "push": 0.04},
                "transition": {"type": "cut" if j == 1 else "fade"},
                "characters": [{"characterId": "hiep", "x": 0.4, "pose": b.get("pose", "standing"),
                                "action": b.get("action", "idle"), "expression": b.get("expression", "neutral")}],
                "dialogue": [{"speaker": "hiep", "text": b["text"], "start": 0.3, "end": b.get("duration", 4) - 0.3}],
                "caption": {"text": b.get("caption_en", idea.get("hook_en", "")) or "…", "start": 0.3, "end": b.get("duration", 4) - 0.3}})
        plan = {"version": 1, "id": f"trend-{idea['id']}", "title": f"[STUB] {idea.get('title', idea['id'])}",
                "meta": {"week": int(idea.get("week", 1)), "status": "stub-needs-approval",
                         "trend_id": idea.get("trend_id"), "bridge_id": idea.get("bridge_id"),
                         "lesson": idea.get("lesson"), "angle": idea.get("angle"), "pattern": idea.get("pattern"),
                         "differentiation": idea.get("differentiation")},
                "video": {"width": 1080, "height": 1920, "fps": 30, "theme": idea.get("theme", "light")},
                "scenes": scenes}
        f = out / f"plan-{i}-{idea['id']}.json"; f.write_text(json.dumps(plan, ensure_ascii=False, indent=1)); print(f)

def week(end=None):
    end = dt.date.fromisoformat(end) if end else dt.date.today()
    for day, r in past_days((end + dt.timedelta(days=1)).isoformat()):
        if (end - dt.date.fromisoformat(day)).days < 7:
            items = [i for i in r.get("items", []) if i.get("safety", "ok") != "drop"]
            pats = sorted({p for i in items for p in i.get("patterns", [])})
            print(f"{day}: {len(items)} items · patterns: {', '.join(pats) or '-'}")
            for i in sorted(items, key=lambda x: -x.get("rank_score", 0))[:3]:
                print(f"   {i.get('rank_score', '-')}  {key(i)}  signals={i.get('signals', {})}")

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    {"score": lambda: score(a[1]), "stub": lambda: stub(a[1], a[2]), "week": lambda: week(a[1] if len(a) > 1 else None)}[a[0]]()
