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
import json, re, subprocess, sys

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65

TIMEOUT = 90

def _run(args):
    if not P.TINYFISH_BIN or not _o.path.exists(P.TINYFISH_BIN):
        print(f"warn: tinyfish CLI not found (TINYFISH_BIN={P.TINYFISH_BIN!r}); skipping", file=sys.stderr)
        return None
    try:
        r = subprocess.run([P.TINYFISH_BIN, *args], capture_output=True, text=True, timeout=TIMEOUT)
    except (subprocess.TimeoutExpired, OSError) as e:
        print(f"warn: tinyfish {args[:2]} failed: {e}", file=sys.stderr); return None
    if r.returncode:
        print(f"warn: tinyfish {args[:2]} exit {r.returncode}: {r.stderr.strip()[:200]}", file=sys.stderr); return None
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        print(f"warn: tinyfish {args[:2]} returned non-JSON", file=sys.stderr); return None

def search(q, lang="vi", loc="VN", domains=None, page=0):
    args = ["search", "query", q, "--language", lang, "--location", loc, "--page", str(page)]
    if domains: args += ["--include-domains", domains]
    d = _run(args)
    return (d or {}).get("results", [])

def fetch(urls):
    d = _run(["fetch", "content", "get", *urls])
    out = []
    for r in (d or {}).get("results", []):
        blocked = (r.get("title") or "").strip() == "Site Maintenance"
        out.append({**r, "blocked": blocked})
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
