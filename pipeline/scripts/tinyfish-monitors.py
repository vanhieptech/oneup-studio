#!/usr/bin/env python3
"""TinyFish search monitors for the daily trend job (0.005 USD per run; NOT created without Hiệp's OK).

  tinyfish-monitors.py --plan                      # print the create commands + estimated monthly cost (no API call)
  tinyfish-monitors.py --list                      # tinyfish monitor list
  tinyfish-monitors.py --create --yes-i-approved-cost   # create the monitors below (billed; refuses without the flag)
  tinyfish-monitors.py --pull [--date YYYY-MM-DD]  # latest results of monitors named oneup-* → research/trends/<date>/tinyfish/monitors.json

Monitors run once a day at 07:00 Asia/Ho_Chi_Minh, 10 results, last 24 h. TikTok queries use site:tiktok.com because
monitors have no domain option; they only find links (TikTok pages block fetch) — apify-run.py measures them.
"""
import datetime as dt, json, os, subprocess, sys

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65

SCHEDULE = "CRON_TZ=Asia/Ho_Chi_Minh 0 7 * * *"
PRICE_PER_RUN = 0.005
MONITORS = [
    {"name": "oneup-tiktok-thoiquen", "query": "site:tiktok.com thói quen", "purpose": "@hi.oneup trend: TikTok clips về thói quen"},
    {"name": "oneup-tiktok-trihoan", "query": "site:tiktok.com trì hoãn", "purpose": "@hi.oneup trend: TikTok clips về trì hoãn"},
    {"name": "oneup-tiktok-hocnho", "query": "site:tiktok.com mẹo học nhớ lâu", "purpose": "@hi.oneup trend: TikTok clips về học nhớ"},
    {"name": "oneup-web-niche-vi", "query": "thói quen trì hoãn kỷ luật bản thân gen Z", "purpose": "@hi.oneup trend: web/báo tiếng Việt cùng ngách"},
]

def create_args(m):
    return ["monitor", "create", "--query", m["query"], "--schedule", SCHEDULE, "--name", m["name"], "--purpose", m["purpose"],
            "--result-limit", "10", "--recency-minutes", "1440"]

def monthly_cost():
    return round(len(MONITORS) * 30 * PRICE_PER_RUN, 2)

def tf(args):
    if not P.TINYFISH_BIN or not os.path.exists(P.TINYFISH_BIN):
        print(f"warn: tinyfish CLI not found (TINYFISH_BIN={P.TINYFISH_BIN!r})", file=sys.stderr); return None
    r = subprocess.run([P.TINYFISH_BIN, *args], capture_output=True, text=True, timeout=120)
    if r.returncode:
        print(f"warn: tinyfish {args[:2]} exit {r.returncode}: {r.stderr.strip()[:200]}", file=sys.stderr); return None
    try: return json.loads(r.stdout)
    except json.JSONDecodeError: return {"raw": r.stdout}

def plan():
    for m in MONITORS:
        print("tinyfish " + " ".join(f'"{x}"' if " " in x else x for x in create_args(m)))
    print(f"# {len(MONITORS)} monitors × 30 runs × {PRICE_PER_RUN} USD ≈ {monthly_cost()} USD/month")

def create(approved):
    if not approved:
        print("refused: creating monitors is billed (≈ %s USD/month). Re-run with --yes-i-approved-cost after Hiệp agrees." % monthly_cost())
        return 1
    existing = {m.get("name") for m in ((tf(["monitor", "list"]) or {}).get("monitors") or [])}
    for m in MONITORS:
        if m["name"] in existing: print(f"skip (exists): {m['name']}"); continue
        print(json.dumps(tf(create_args(m)), ensure_ascii=False)[:300])
    return 0

def extract_results(monitor):
    """Normalise a monitor's latest run into [{title,url,snippet,date,monitor}] whatever the exact field names are."""
    run = monitor.get("last_run") or monitor.get("latest_run") or monitor.get("last_result") or monitor
    res = run.get("results") or (run.get("result") or {}).get("results") or []
    return [{"title": r.get("title", ""), "url": r.get("url", ""), "snippet": r.get("snippet", ""), "date": r.get("date"),
             "monitor": monitor.get("name")} for r in res if isinstance(r, dict)]

def pull(date):
    mons = [m for m in ((tf(["monitor", "list"]) or {}).get("monitors") or []) if str(m.get("name", "")).startswith("oneup-")]
    items = []
    for m in mons:
        full = tf(["monitor", "get", m.get("id") or m.get("monitor_id")]) or m
        items += extract_results(full)
    out = P.ROOT / f"research/trends/{date}/tinyfish/monitors.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(items, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(items)} item(s) from {len(mons)} monitor(s) → {out}")
    return 0

def main():
    a = sys.argv[1:]
    if "--plan" in a: plan(); return 0
    if "--list" in a: print(json.dumps(tf(["monitor", "list"]), ensure_ascii=False, indent=1)); return 0
    if "--create" in a: return create("--yes-i-approved-cost" in a)
    if "--pull" in a: return pull(a[a.index("--date") + 1] if "--date" in a else dt.date.today().isoformat())
    print(__doc__); return 2

if __name__ == "__main__":
    sys.exit(main())
