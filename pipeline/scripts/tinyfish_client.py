#!/usr/bin/env python3
"""TinyFish CLI wrapper (free search + fetch) for the trend pipeline.

  tinyfish_client.py search "thói quen 21 ngày" [--lang vi] [--loc VN] [--domains a.com,b.com]
  tinyfish_client.py fetch URL [URL ...]
  tinyfish_client.py tiktok "thói quen" ["trì hoãn" ...] [--out research/trends/<date>/tinyfish/tiktok-candidates.json]

What works (tested 26/11/2026): search finds TikTok clips (link, caption snippet, date) with
--include-domains tiktok.com; fetch reads articles/papers. Fetch of TikTok video pages is blocked
("Site Maintenance"), so views/likes/subtitles/comments still come from Apify (apify-run.py).
Only the free Hobby search/fetch meters are used here; no agent/browser/dataset/monitor calls.
No binary → empty results + a warning on stderr, never a crash of the caller.
"""
import json, re, shutil, subprocess, sys, threading, time

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))  # ego_crawl

TIMEOUT = 90
_LOCK = threading.Lock()

def _env_with_node():
    env = dict(_o.environ)
    extra = []
    if P.TINYFISH_BIN:
        extra.append(_o.path.dirname(_o.path.abspath(P.TINYFISH_BIN)))
    for d in ("/opt/homebrew/bin", "/usr/local/bin"):
        if _o.path.isdir(d):
            extra.append(d)
    path_parts = [p for p in env.get("PATH", "").split(_o.pathsep) if p]
    for d in reversed(extra):
        if d and d not in path_parts:
            path_parts.insert(0, d)
    env["PATH"] = _o.pathsep.join(path_parts)
    return env

def _run(args, retries=2):
    if not P.TINYFISH_BIN or not _o.path.exists(P.TINYFISH_BIN):
        print(f"warn: tinyfish CLI not found (TINYFISH_BIN={P.TINYFISH_BIN!r}); skipping", file=sys.stderr)
        return None
    env = _env_with_node()
    with _LOCK:
        for attempt in range(1, retries + 1):
            try:
                r = subprocess.run([P.TINYFISH_BIN, *args], capture_output=True, text=True, timeout=TIMEOUT, env=env)
            except (subprocess.TimeoutExpired, OSError) as e:
                if attempt < retries:
                    time.sleep(1.5)
                    continue
                print(f"warn: tinyfish {args[:2]} failed: {e}", file=sys.stderr); return None
            if r.returncode:
                if attempt < retries and "fetch failed" in (r.stderr or ""):
                    time.sleep(2.0)
                    continue
                print(f"warn: tinyfish {args[:2]} exit {r.returncode}: {r.stderr.strip()[:200]}", file=sys.stderr); return None
            try:
                return json.loads(r.stdout)
            except json.JSONDecodeError:
                print(f"warn: tinyfish {args[:2]} returned non-JSON", file=sys.stderr); return None

def search(q, lang="vi", loc="VN", domains=None, page=0, ego_fallback=True):
    args = ["search", "query", q, "--language", lang, "--location", loc, "--page", str(page)]
    if domains: args += ["--include-domains", domains]
    d = _run(args)
    res = (d or {}).get("results", [])
    if not res and ego_fallback:
        try:
            import ego_crawl as EGO
            if EGO.available():
                res = EGO.search_web(q, domains=domains)
        except Exception as e:
            print(f"warn: ego_crawl search fallback error: {e}", file=sys.stderr)
    return res

def fetch(urls, ego_fallback=True):
    d = _run(["fetch", "content", "get", *urls])
    out = []
    by_url = {}
    for r in (d or {}).get("results", []):
        text = r.get("text") or r.get("content") or r.get("markdown") or ""
        blocked = (r.get("title") or "").strip() == "Site Maintenance" or len(text.strip()) < 160
        row = {**r, "blocked": blocked}
        out.append(row)
        if r.get("url"):
            by_url[r["url"]] = row
    if ego_fallback:
        need = [u for u in urls if u not in by_url or by_url[u].get("blocked")]
        if need:
            try:
                import ego_crawl as EGO
                if EGO.available():
                    fb = {r["url"]: r for r in EGO.fetch_urls(need) if r.get("url")}
                    merged = []
                    seen = set()
                    for row in out:
                        u = row.get("url")
                        if u in fb and not fb[u].get("blocked") and fb[u].get("text"):
                            merged.append(fb[u])
                        else:
                            merged.append(row)
                        if u: seen.add(u)
                    for u in need:
                        if u not in seen and u in fb:
                            merged.append(fb[u])
                    out = merged
            except Exception as e:
                print(f"warn: ego_crawl fetch fallback error: {e}", file=sys.stderr)
    return out

TIKTOK_RE = re.compile(r"tiktok\.com/@([^/?#]+)/video/(\d+)")

def tiktok_discover(queries, lang="vi", loc="VN"):
    """Find TikTok clip links for topic queries (free). Returns deduped candidates for Apify to measure."""
    seen, out = set(), []
    for q in queries:
        for r in search(q, lang, loc, domains="tiktok.com"):
            m = TIKTOK_RE.search(r.get("url", ""))
            if not m or m.group(2) in seen: continue
            seen.add(m.group(2))
            out.append({"url": f"https://www.tiktok.com/@{m.group(1)}/video/{m.group(2)}", "video_id": m.group(2),
                        "creator": m.group(1), "title": r.get("title", ""), "snippet": r.get("snippet", ""),
                        "date": r.get("date"), "query": q, "source": "tinyfish-search"})
    return out

def main():
    a = sys.argv[1:]
    if not a: print(__doc__); return 2
    cmd, rest = a[0], a[1:]
    def opt(name, default=None):
        if name in rest:
            i = rest.index(name); v = rest[i + 1]; del rest[i:i + 2]; return v
        return default
    lang, loc, domains, outp = opt("--lang", "vi"), opt("--loc", "VN"), opt("--domains"), opt("--out")
    if cmd == "search": res = search(" ".join(rest), lang, loc, domains)
    elif cmd == "fetch": res = fetch(rest)
    elif cmd == "tiktok": res = tiktok_discover(rest, lang, loc)
    else: print(__doc__); return 2
    txt = json.dumps(res, ensure_ascii=False, indent=1)
    if outp:
        _o.makedirs(_o.path.dirname(outp) or ".", exist_ok=True); open(outp, "w", encoding="utf-8").write(txt + "\n")
        print(f"{len(res)} item(s) → {outp}")
    else: print(txt)
    return 0

if __name__ == "__main__":
    sys.exit(main())
