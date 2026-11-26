#!/usr/bin/env python3
"""Apify TikTok run for the local Mac (replaces the box MCP `user-Apify`, 26/11/2026).

  apify-run.py [--date YYYY-MM-DD] [--urls-from research/trends/<date>/tinyfish/tiktok-candidates.json]
               [--max-urls 10] [--comments 3] [--cap-usd 0.15] [--dry-run]

Flow: candidate links (TinyFish discovery, free) → clockworks/tiktok-scraper measures them (play/like/share/comment,
author fans, music, subtitles) — or, with no candidates, the keyword/hashtag input in pipeline/trends/apify.yaml →
VTT subtitles downloaded → clockworks/tiktok-comments-scraper on the top `--comments` clips by outlier score →
pipeline/scripts/trend-apify-normalize.py → research/trends/<date>/apify/clips.json (+ `outlier` per clip) and cost.json.

Token: APIFY_TOKEN from the environment or ~/oneup-tools/env.sh (pipeline/paths.py tools_env). Sent only in the
Authorization header to api.apify.com; never printed, logged or written into the repo.
Budget: stops before a run when today's cost.json total ≥ --cap-usd; each run also gets maxTotalChargeUsd.
"""
import datetime as dt, json, os, statistics, subprocess, sys, urllib.error, urllib.parse, urllib.request
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65

API = "https://api.apify.com/v2"
CFG = P.ROOT / "pipeline/trends/apify.yaml"

def load_cfg():
    return json.loads("\n".join(l for l in CFG.read_text().splitlines() if not l.lstrip().startswith("#")))

def token():
    t = P.tools_env("APIFY_TOKEN")
    if not t: raise SystemExit("APIFY_TOKEN missing: add `export APIFY_TOKEN=…` to ~/oneup-tools/env.sh (outside git, chmod 600)")
    return t

def http(method, url, body=None, timeout=420, raw=False):
    req = urllib.request.Request(url, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": f"Bearer {token()}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
    except urllib.error.HTTPError as e:  # show Apify's reason (never the token)
        raise SystemExit(f"apify {method} {url.split('?')[0]} → HTTP {e.code}: {e.read().decode(errors='replace')[:300]}")
    return data if raw else json.loads(data)

def run_actor(actor, inp, cap_usd, wait=300):
    """Start a run, wait for it, return (items, run_info). maxTotalChargeUsd caps pay-per-event actors."""
    # Apify rejects maxTotalChargeUsd < 0.50; our real cap is the daily check in main() plus tiny inputs (≤10 links).
    q = urllib.parse.urlencode({"waitForFinish": wait, "maxTotalChargeUsd": f"{max(cap_usd, 0.50):.2f}"})
    run = http("POST", f"{API}/acts/{actor.replace('/', '~')}/runs?{q}", inp)["data"]
    for _ in range(6):  # waitForFinish is capped server-side; poll a little longer if still running
        if run.get("status") not in ("READY", "RUNNING"): break
        run = http("GET", f"{API}/actor-runs/{run['id']}?waitForFinish=60")["data"]
    items = http("GET", f"{API}/datasets/{run['defaultDatasetId']}/items?clean=true&format=json") if run.get("defaultDatasetId") else []
    info = {"actor": actor, "run_id": run.get("id"), "status": run.get("status"), "usd": float(run.get("usageTotalUsd") or 0), "items": len(items)}
    return items, info

def spent_today(cost_path):
    if not cost_path.exists(): return 0.0
    return sum(r.get("usd", 0) for r in json.loads(cost_path.read_text()).get("runs", []))

def save_cost(cost_path, info):
    d = json.loads(cost_path.read_text()) if cost_path.exists() else {"runs": []}
    d["runs"].append({**info, "at": dt.datetime.now().isoformat(timespec="seconds")})
    d["total_usd"] = round(sum(r.get("usd", 0) for r in d["runs"]), 4)
    cost_path.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n")

def download_vtts(items, vtt_dir):
    """Vietnamese (else first) subtitle per clip → vtt_dir/<id>-<lang>.vtt (normalizer matches by id in the file name)."""
    n = 0
    for it in items:
        links = ((it.get("videoMeta") or {}).get("subtitleLinks") or [])
        if not links: continue
        pick = next((l for l in links if str(l.get("language", "")).lower().startswith("vie")), links[0])
        url = pick.get("downloadLink") or pick.get("tiktokLink")
        if not url: continue
        try:
            data = http("GET", url, raw=True, timeout=60) if "api.apify.com" in url else urllib.request.urlopen(url, timeout=60).read()
        except Exception as e:  # subtitle missing is normal (slideshows, muted clips): caption fallback in the normalizer
            print(f"warn: subtitle {it.get('id')}: {type(e).__name__}", file=sys.stderr); continue
        vtt_dir.mkdir(parents=True, exist_ok=True)
        (vtt_dir / f"{it.get('id')}-{pick.get('language', 'sub')}.vtt").write_bytes(data); n += 1
    return n

def outlier_scores(items):
    """play ÷ median play of the same author in this batch when the author has ≥3 clips here, else play ÷ fans."""
    by = {}
    for it in items: by.setdefault((it.get("authorMeta") or {}).get("name"), []).append(it.get("playCount") or 0)
    out = {}
    for it in items:
        play = it.get("playCount") or 0; plays = by.get((it.get("authorMeta") or {}).get("name"), [])
        fans = (it.get("authorMeta") or {}).get("fans") or 0
        if len(plays) >= 3 and statistics.median(plays) > 0: out[str(it.get("id"))] = {"outlier": round(play / statistics.median(plays), 2), "basis": "author_median"}
        elif fans > 0: out[str(it.get("id"))] = {"outlier": round(play / fans, 2), "basis": "fans"}
        else: out[str(it.get("id"))] = {"outlier": None, "basis": "unknown"}
    return out

def main():
    a = sys.argv[1:]
    def opt(n, d=None): return a[a.index(n) + 1] if n in a else d
    date = opt("--date", dt.date.today().isoformat())
    outd = P.ROOT / f"research/trends/{date}/apify"; outd.mkdir(parents=True, exist_ok=True)
    cost_path = outd / "cost.json"; cfg = load_cfg()
    cap = float(opt("--cap-usd", min(0.15, cfg["budget"].get("daily_usd_cap", 0.15))))
    urls = []
    if opt("--urls-from"):
        urls = [c["url"] for c in json.loads(Path(opt("--urls-from")).read_text()) if c.get("url")][: int(opt("--max-urls", 10))]
    base = dict(cfg["actors"]["clockworks_search"]["default_input"])
    inp = ({**{k: v for k, v in base.items() if k not in ("hashtags", "searchQueries", "searchSection", "resultsPerPage")}, "postURLs": urls}
           if urls else base)
    if "--dry-run" in a:
        print(json.dumps({"date": date, "cap_usd": cap, "spent_today": spent_today(cost_path), "input": inp}, ensure_ascii=False, indent=1)); return 0
    if spent_today(cost_path) >= cap: raise SystemExit(f"daily cap reached ({spent_today(cost_path):.3f} ≥ {cap} USD)")
    items, info = run_actor("clockworks/tiktok-scraper", inp, cap - spent_today(cost_path)); save_cost(cost_path, info)
    (outd / "dataset.json").write_text(json.dumps(items, ensure_ascii=False, indent=1) + "\n")
    nv = download_vtts(items, outd / "vtt")
    scores = outlier_scores(items)
    k = int(opt("--comments", 3))
    top = sorted(items, key=lambda it: -(scores.get(str(it.get("id")), {}).get("outlier") or 0))[:k]
    cpath = outd / "comments.json"
    if top and spent_today(cost_path) < cap:
        cinp = {**cfg["actors"]["clockworks_comments"]["default_input"], "postURLs": [t.get("webVideoUrl") for t in top if t.get("webVideoUrl")]}
        citems, cinfo = run_actor("clockworks/tiktok-comments-scraper", cinp, cap - spent_today(cost_path)); save_cost(cost_path, cinfo)
        cpath.write_text(json.dumps(citems, ensure_ascii=False, indent=1) + "\n")
    norm = [sys.executable, str(P.ROOT / "pipeline/scripts/trend-apify-normalize.py"), "--actor", "clockworks/tiktok-scraper",
            "--dataset", str(outd / "dataset.json"), "--vtt-dir", str(outd / "vtt"), "--out", str(outd / "clips.json")]
    if cpath.exists(): norm += ["--comments", str(cpath)]
    subprocess.run(norm, check=True)
    clips = json.loads((outd / "clips.json").read_text())
    rows = clips if isinstance(clips, list) else clips.get("clips", [])
    for r in rows: r.update(scores.get(str(r.get("raw_id")), {}))
    (outd / "clips.json").write_text(json.dumps(clips, ensure_ascii=False, indent=1) + "\n")
    print(f"apify: {len(items)} clip(s), {nv} subtitle(s), comments for {len(top)}; cost today {spent_today(cost_path):.4f} USD → {outd}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
