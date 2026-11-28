#!/usr/bin/env python3
"""Apify TikTok measure for the local Mac (replaces the box MCP `user-Apify`, 26/11/2026).

  apify-run.py --date YYYY-MM-DD --urls-from research/trends/<date>/tinyfish/tiktok-candidates.json
               [--max-urls N] [--allow-truncate] [--comments N] [--allow-comment-sample]
               [--allow-hashtag-basket] [--comments-only] [--cap-usd 0.15] [--dry-run]

Native path: every URL in the TinyFish file is sent as postURLs. The hashtag/searchQueries block in
pipeline/trends/apify.yaml is not a fallback. Missing file, empty file, a bare run while candidates
exist, or a --max-urls that would drop links exits with `BREAK trend-digest` before any paid call.
Comment pull defaults to 3; measuring more links than that also breaks unless --comments N or
--allow-comment-sample is set. --allow-hashtag-basket is the only switch onto the yaml basket, and
only after Hiệp says so in that run.

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

def break_digest(reason, nxt):
    """Stop the run. The text is the alert Hiệp must see. Do not catch this and continue."""
    raise SystemExit(f"BREAK trend-digest\n{reason}\nNext: {nxt}")

def load_candidate_urls(path):
    """None when the file is absent. A list (possibly empty) when it exists."""
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    rows = data if isinstance(data, list) else (data.get("items") or data.get("candidates") or data.get("results") or [])
    return [r["url"] for r in rows if isinstance(r, dict) and r.get("url")]

def resolve_tiktok_input(argv, date, cfg, root):
    """Pick the Apify input. Breaks before a paid call when the native TinyFish path would be skipped."""
    def opt(n, d=None):
        return argv[argv.index(n) + 1] if n in argv else d
    base = dict(cfg["actors"]["clockworks_search"]["default_input"])
    rel = f"research/trends/{date}/tinyfish/tiktok-candidates.json"
    measure = f"python3 pipeline/scripts/apify-run.py --date {date} --urls-from {rel}"
    discover = f"python3 pipeline/scripts/tinyfish_client.py tiktok \"<topic>\" --out {rel}"
    if "--allow-hashtag-basket" in argv:
        return base, "hashtag-basket"
    src = Path(opt("--urls-from")) if opt("--urls-from") else (root / rel)
    urls = load_candidate_urls(src)
    shown = opt("--urls-from") or rel
    if urls is None:
        break_digest(f"Thiếu file ứng viên TinyFish ({shown}). Không chuyển sang giỏ hashtag trong pipeline/trends/apify.yaml.", discover)
    if not urls:
        break_digest(f"File ứng viên TinyFish rỗng ({shown}). Không chuyển sang giỏ hashtag.", discover)
    if "--urls-from" not in argv:
        break_digest(f"{len(urls)} link TinyFish tại {rel} chưa được đưa vào Apify. Không đo bằng hashtag mặc định.", measure)
    cap_n = opt("--max-urls")
    if cap_n is not None and len(urls) > int(cap_n) and "--allow-truncate" not in argv:
        dropped = len(urls) - int(cap_n)
        break_digest(f"{len(urls)} link trong {rel}, --max-urls {cap_n} sẽ bỏ {dropped} link. Không cắt im lặng.", f"{measure} --max-urls {len(urls)}")
    if cap_n is not None and "--allow-truncate" in argv:
        urls = urls[:int(cap_n)]
    comment_n = int(opt("--comments", "3"))
    if len(urls) > comment_n and "--allow-comment-sample" not in argv:
        break_digest(
            f"Sắp đo {len(urls)} link nhưng comment mặc định chỉ {comment_n} clip. Không lấy mẫu comment im lặng.",
            f"{measure} --comments {len(urls)}   hoặc thêm --allow-comment-sample khi Hiệp nói rõ là giữ {comment_n} comment",
        )
    kept = {k: v for k, v in base.items() if k not in ("hashtags", "searchQueries", "searchSection", "resultsPerPage")}
    return {**kept, "postURLs": urls}, "urls"

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

def finish_clips(items, outd, scores, comments_path):
    norm = [sys.executable, str(P.ROOT / "pipeline/scripts/trend-apify-normalize.py"), "--actor", "clockworks/tiktok-scraper",
            "--dataset", str(outd / "dataset.json"), "--vtt-dir", str(outd / "vtt"), "--out", str(outd / "clips.json")]
    if comments_path.exists():
        norm += ["--comments", str(comments_path)]
    subprocess.run(norm, check=True)
    clips = json.loads((outd / "clips.json").read_text())
    rows = clips if isinstance(clips, list) else clips.get("clips", [])
    for r in rows:
        r.update(scores.get(str(r.get("raw_id")), {}))
    (outd / "clips.json").write_text(json.dumps(clips, ensure_ascii=False, indent=1) + "\n")

def pull_comments(items, scores, outd, cost_path, cap, cfg, comment_n):
    """Paid comment step. Breaks when the cap would skip it after the dataset is already on disk."""
    top = sorted(items, key=lambda it: -(scores.get(str(it.get("id")), {}).get("outlier") or 0))[:comment_n]
    cpath = outd / "comments.json"
    if not top:
        return cpath, 0
    if spent_today(cost_path) >= cap:
        break_digest(
            f"Đã lưu {len(items)} clip tại {outd / 'dataset.json'} nhưng trần tiền chặn comment. Chưa xong lớp TikTok.",
            f"python3 pipeline/scripts/apify-run.py --date {outd.parent.name} --comments-only --cap-usd {cap}",
        )
    cinp = {**cfg["actors"]["clockworks_comments"]["default_input"], "postURLs": [t.get("webVideoUrl") for t in top if t.get("webVideoUrl")]}
    citems, cinfo = run_actor("clockworks/tiktok-comments-scraper", cinp, cap - spent_today(cost_path))
    save_cost(cost_path, cinfo)
    cpath.write_text(json.dumps(citems, ensure_ascii=False, indent=1) + "\n")
    return cpath, len(top)

def main():
    a = sys.argv[1:]
    def opt(n, d=None): return a[a.index(n) + 1] if n in a else d
    date = opt("--date", dt.date.today().isoformat())
    outd = P.ROOT / f"research/trends/{date}/apify"
    cost_path = outd / "cost.json"; cfg = load_cfg()
    cap = float(opt("--cap-usd", min(0.15, cfg["budget"].get("daily_usd_cap", 0.15))))
    comment_n = int(opt("--comments", "3"))
    if "--comments-only" in a:
        dataset = outd / "dataset.json"
        if not dataset.exists():
            break_digest(f"Không có {dataset} để kéo comment. Không chạy lại scraper.", f"python3 pipeline/scripts/apify-run.py --date {date} --urls-from research/trends/{date}/tinyfish/tiktok-candidates.json")
        items = json.loads(dataset.read_text())
        scores = outlier_scores(items)
        cpath, ntop = pull_comments(items, scores, outd, cost_path, cap, cfg, comment_n)
        finish_clips(items, outd, scores, cpath)
        print(f"apify: comments-only, {len(items)} clip(s), comments for {ntop}; cost today {spent_today(cost_path):.4f} USD → {outd}")
        return 0
    inp, _mode = resolve_tiktok_input(a, date, cfg, P.ROOT)
    if "--dry-run" in a:
        print(json.dumps({"date": date, "cap_usd": cap, "spent_today": spent_today(cost_path), "input": inp}, ensure_ascii=False, indent=1)); return 0
    outd.mkdir(parents=True, exist_ok=True)
    if spent_today(cost_path) >= cap: raise SystemExit(f"daily cap reached ({spent_today(cost_path):.3f} ≥ {cap} USD)")
    items, info = run_actor("clockworks/tiktok-scraper", inp, cap - spent_today(cost_path)); save_cost(cost_path, info)
    (outd / "dataset.json").write_text(json.dumps(items, ensure_ascii=False, indent=1) + "\n")
    if not items:
        break_digest("Apify trả 0 clip. Không điền tín hiệu TikTok bằng giỏ hashtag hay proxy YouTube.", f"python3 pipeline/scripts/apify-run.py --date {date} --urls-from research/trends/{date}/tinyfish/tiktok-candidates.json")
    nv = download_vtts(items, outd / "vtt")
    scores = outlier_scores(items)
    cpath, ntop = pull_comments(items, scores, outd, cost_path, cap, cfg, comment_n)
    finish_clips(items, outd, scores, cpath)
    print(f"apify: {len(items)} clip(s), {nv} subtitle(s), comments for {ntop}; cost today {spent_today(cost_path):.4f} USD → {outd}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
