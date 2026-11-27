#!/usr/bin/env python3
"""Token-efficient native ego-browser (Ego Lite, DL-083) crawl & fallback module.

Used automatically when TinyFish search/fetch or stdlib HTTP/RSS fails (403, Cloudflare,
JS-rendered SPA, or "Site Maintenance"), or directly from CLI:

  ego_crawl.py fetch URL [URL ...] [--max-chars 3500] [--out file.json]
  ego_crawl.py search "query" [--domains a.com,b.com] [--max 10] [--out file.json]
  ego_crawl.py feed URL [--max 15] [--out file.json]

Design principles (studio-grade, zero token bloat):
- Runs in a single TaskSpace reusing Page `p1` across URLs, then closes via `task.finish({ keep: [] })`.
- Extracts compact structured JSON via `page.evaluate()` — never dumps raw HTML or full snapshots.
- Strips scripts/styles/nav/footer/ads and caps article text to `max_chars` (default 3500).
- Never bypasses CAPTCHAs or anti-bot walls: detects and marks `blocked: true, captcha: true`.
- Thread-safe via `_LOCK`; degrades gracefully (empty list + stderr warning) if Ego Lite is offline.
"""
import json, os, subprocess, sys, threading, urllib.parse

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65

TIMEOUT = 120
_LOCK = threading.Lock()
_MARKER = "__EGO_CRAWL_JSON__"


def available():
    if os.environ.get("ONEUP_DISABLE_EGO_FALLBACK") == "1":
        return False
    return bool(P.EGO_BROWSER_BIN and os.path.exists(P.EGO_BROWSER_BIN))


def _run_node(script, timeout=TIMEOUT):
    """Execute an ESM script via `ego-browser nodejs` and parse the JSON payload after _MARKER."""
    if not available():
        return None
    with _LOCK:
        try:
            r = subprocess.run(
                [P.EGO_BROWSER_BIN, "nodejs"],
                input=script,
                capture_output=True,
                text=True,
                timeout=timeout,
            )
        except (subprocess.TimeoutExpired, OSError) as e:
            print(f"warn: ego-browser crawl failed: {e}", file=sys.stderr)
            return None
    if r.returncode != 0:
        err = (r.stderr or r.stdout or "").strip().splitlines()
        tail = " | ".join(err[-3:])[:220]
        print(f"warn: ego-browser exit {r.returncode}: {tail}", file=sys.stderr)
        return None
    combined = (r.stdout or "") + "\n" + (r.stderr or "")
    for line in reversed(combined.splitlines()):
        if line.startswith(_MARKER):
            try:
                return json.loads(line[len(_MARKER):])
            except json.JSONDecodeError:
                return None
    return None


def fetch_urls(urls, max_chars=3500, timeout=TIMEOUT):
    """Fetch clean article text from one or more URLs using native ego-browser."""
    if not urls or not available():
        return []
    payload = json.dumps({"urls": list(urls), "maxChars": int(max_chars)})
    script = f"""
const INPUT = {payload};
const task = await taskSpace("oneup-crawl-fetch-" + Date.now());
const results = [];
try {{
  const page = task.page("p1");
  for (const url of INPUT.urls) {{
    try {{
      try {{
        await page.goto(url, {{ waitUntil: "domcontentloaded", timeout: 12000 }});
      }} catch (navErr) {{
        if (!String(navErr).includes("Timeout")) throw navErr;
      }}
      await new Promise((r) => setTimeout(r, 1200));
      const doc = await page.evaluate((maxChars) => {{
        const title = (document.title || "").trim();
        const bodyTextRaw = (document.body?.innerText || "").trim();
        const low = (title + " " + bodyTextRaw.slice(0, 600)).toLowerCase();
        const captcha = /verify you are human|just a moment|captcha|cf-turnstile|recaptcha|hcaptcha|access denied/.test(low)
          && bodyTextRaw.length < 1200;
        const maintenance = title === "Site Maintenance";
        if (captcha || maintenance) {{
          return {{ title, description: "", text: "", blocked: true, captcha, maintenance }};
        }}
        const metaDesc = document.querySelector('meta[name="description"], meta[property="og:description"]')?.content?.trim() || "";
        const root = document.querySelector("article, main, [role='main'], .fck_detail, .detail-content, .article-body") || document.body;
        const clone = root.cloneNode(true);
        clone.querySelectorAll("script,style,noscript,nav,footer,aside,iframe,svg,form,button,.ads,.advertisement,.related,.comment,.comments").forEach((el) => el.remove());
        const text = (clone.innerText || clone.textContent || "")
          .replace(/[ \\t]+/g, " ")
          .replace(/\\n{{3,}}/g, "\\n\\n")
          .trim()
          .slice(0, maxChars);
        return {{ title, description: metaDesc.slice(0, 300), text, blocked: false, captcha: false, maintenance: false }};
      }}, INPUT.maxChars);
      results.push({{ url, ...doc, source: "ego-browser" }});
    }} catch (e) {{
      results.push({{ url, title: "", description: "", text: "", blocked: true, error: String(e).slice(0, 180), source: "ego-browser" }});
    }}
  }}
}} finally {{
  try {{ await task.finish({{ keep: [] }}); }} catch (_) {{}}
}}
console.log("{_MARKER}" + JSON.stringify(results));
"""
    data = _run_node(script, timeout=max(timeout, 30 * len(urls)))
    return data if isinstance(data, list) else []


def search_web(query, domains=None, max_results=10, timeout=TIMEOUT):
    """Fallback web search via DuckDuckGo in native ego-browser, returning [{title, url, snippet, source}]."""
    if not query or not available():
        return []
    q = query.strip()
    if domains:
        doms = [d.strip() for d in domains.split(",") if d.strip()]
        if len(doms) == 1:
            q = f"site:{doms[0]} {q}"
        elif doms:
            q = "(" + " OR ".join(f"site:{d}" for d in doms) + ") " + q
    search_url = "https://duckduckgo.com/?q=" + urllib.parse.quote(q) + "&ia=web"
    payload = json.dumps({"url": search_url, "limit": int(max_results)})
    script = f"""
const INPUT = {payload};
const task = await taskSpace("oneup-crawl-search-" + Date.now());
let results = [];
try {{
  const page = task.page("p1");
  try {{
    await page.goto(INPUT.url, {{ waitUntil: "domcontentloaded", timeout: 12000 }});
  }} catch (navErr) {{
    if (!String(navErr).includes("Timeout")) throw navErr;
  }}
  await new Promise((r) => setTimeout(r, 1500));
  results = await page.evaluate((limit) => {{
    const out = [];
    const seen = new Set();
    const cards = document.querySelectorAll('article[data-testid="result"], .result, .nrn-react-div');
    for (const c of cards) {{
      const a = c.querySelector('a[data-testid="result-title-a"], a.result__a, h2 a');
      if (!a || !a.href || seen.has(a.href)) continue;
      seen.add(a.href);
      const title = (a.innerText || a.textContent || "").trim();
      const snEl = c.querySelector('[data-result="snippet"], .result__snippet, [data-testid="result-snippet"]');
      const snippet = (snEl?.innerText || "").trim().slice(0, 260);
      if (title) out.push({{ title, url: a.href, snippet, source: "ego-browser" }});
      if (out.length >= limit) break;
    }}
    return out;
  }}, INPUT.limit);
}} catch (e) {{
  results = [];
}} finally {{
  try {{ await task.finish({{ keep: [] }}); }} catch (_) {{}}
}}
console.log("{_MARKER}" + JSON.stringify(results));
"""
    data = _run_node(script, timeout=timeout)
    return data if isinstance(data, list) else []


def crawl_feed(url, max_items=15, timeout=TIMEOUT):
    """Extract headline links from a JS-rendered or Cloudflare-protected page as feed items."""
    if not url or not available():
        return []
    payload = json.dumps({"url": url, "limit": int(max_items)})
    script = f"""
const INPUT = {payload};
const task = await taskSpace("oneup-crawl-feed-" + Date.now());
let items = [];
try {{
  const page = task.page("p1");
  try {{
    await page.goto(INPUT.url, {{ waitUntil: "domcontentloaded", timeout: 12000 }});
  }} catch (navErr) {{
    if (!String(navErr).includes("Timeout")) throw navErr;
  }}
  await new Promise((r) => setTimeout(r, 1500));
  items = await page.evaluate((limit) => {{
    const low = ((document.title || "") + " " + (document.body?.innerText || "").slice(0, 400)).toLowerCase();
    if (/verify you are human|just a moment|captcha/.test(low) && (document.body?.innerText || "").length < 1200) {{
      return [];
    }}
    const out = [];
    const seen = new Set();
    const links = document.querySelectorAll("article a[href], h2 a[href], h3 a[href], main a[href]");
    for (const a of links) {{
      const href = a.href;
      const title = (a.innerText || a.textContent || "").replace(/\\s+/g, " ").trim();
      if (!href || !href.startsWith("http") || title.length < 18 || title.length > 220 || seen.has(href)) continue;
      seen.add(href);
      out.push({{ title, url: href, summary: "", source: "ego-browser" }});
      if (out.length >= limit) break;
    }}
    return out;
  }}, INPUT.limit);
}} catch (e) {{
  items = [];
}} finally {{
  try {{ await task.finish({{ keep: [] }}); }} catch (_) {{}}
}}
console.log("{_MARKER}" + JSON.stringify(items));
"""
    data = _run_node(script, timeout=timeout)
    return data if isinstance(data, list) else []


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        return 2
    cmd, rest = a[0], a[1:]
    def opt(name, default=None):
        if name in rest:
            i = rest.index(name); v = rest[i + 1]; del rest[i:i + 2]; return v
        return default
    outp = opt("--out")
    if cmd == "fetch":
        res = fetch_urls(rest, max_chars=int(opt("--max-chars", 3500)))
    elif cmd == "search":
        res = search_web(" ".join(rest), domains=opt("--domains"), max_results=int(opt("--max", 10)))
    elif cmd == "feed":
        res = crawl_feed(rest[0] if rest else "", max_items=int(opt("--max", 15)))
    else:
        print(__doc__)
        return 2
    txt = json.dumps(res, ensure_ascii=False, indent=1)
    if outp:
        os.makedirs(os.path.dirname(outp) or ".", exist_ok=True)
        open(outp, "w", encoding="utf-8").write(txt + "\n")
        print(f"{len(res)} item(s) → {outp}")
    else:
        print(txt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
