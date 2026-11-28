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


SOCIAL_URLS = {
    "tiktok": lambda q: "https://www.tiktok.com/search?q=" + urllib.parse.quote(q),
    "x": lambda q: "https://x.com/search?q=" + urllib.parse.quote(q) + "&f=top",
    "threads": lambda q: "https://www.threads.net/search?q=" + urllib.parse.quote(q) + "&serp_type=default",
    "instagram": lambda q: "https://www.instagram.com/explore/tags/" + urllib.parse.quote(q.lstrip("#").replace(" ", "")) + "/",
    "youtube": lambda q: "https://www.youtube.com/results?search_query=" + urllib.parse.quote(q) + "&sp=EgIYAQ%253D%253D",
}


def crawl_social(platform, query, max_items=15, timeout=TIMEOUT):
    """DOM-only (zero screenshots, zero LLM vision tokens) extraction from logged-in TikTok/X/Threads/IG/YouTube in ego-browser."""
    plat = (platform or "").strip().lower()
    if plat not in SOCIAL_URLS or not query or not available():
        return []
    url = SOCIAL_URLS[plat](query.strip())
    payload = json.dumps({"url": url, "platform": plat, "limit": int(max_items)})
    script = f"""
const INPUT = {payload};
const task = await taskSpace("oneup-social-" + INPUT.platform + "-" + Date.now());
let items = [];
try {{
  const page = task.page("p1");
  try {{
    await page.goto(INPUT.url, {{ waitUntil: "domcontentloaded", timeout: 15000 }});
  }} catch (navErr) {{
    if (!String(navErr).includes("Timeout")) throw navErr;
  }}
  await new Promise((r) => setTimeout(r, 2500));
  items = await page.evaluate(({{ platform, limit }}) => {{
    const bodyTxt = (document.body?.innerText || "").slice(0, 600).toLowerCase();
    if (/verify you are human|captcha|cf-turnstile|recaptcha/.test(bodyTxt) && bodyTxt.length < 1000) {{
      return [{{ blocked: true, captcha: true, platform }}];
    }}
    const out = [];
    const seen = new Set();
    const pushItem = (title, href, author = "", metric = "") => {{
      const cleanT = (title || "").replace(/\\s+/g, " ").trim().slice(0, 220);
      if (!href || !href.startsWith("http") || seen.has(href) || cleanT.length < 6) return;
      seen.add(href);
      out.push({{ platform, title: cleanT, url: href, author, metric, source: "ego-browser" }});
    }};
    if (platform === "tiktok") {{
      for (const a of document.querySelectorAll('a[href*="/video/"]')) {{
        const card = a.closest('[data-e2e="search_top-item"], [class*="DivItemContainer"], div') || a;
        const m = a.href.match(/@([^/]+)\\/video/);
        pushItem(card.innerText || a.title || a.href, a.href, m ? m[1] : "");
        if (out.length >= limit) break;
      }}
    }} else if (platform === "x") {{
      for (const art of document.querySelectorAll('article[data-testid="tweet"]')) {{
        const a = art.querySelector('a[href*="/status/"]');
        const txt = art.querySelector('[data-testid="tweetText"]')?.innerText || art.innerText;
        const m = a?.href?.match(/x\\.com\\/([^/]+)\\/status/);
        pushItem(txt, a?.href || "", m ? m[1] : "");
        if (out.length >= limit) break;
      }}
    }} else if (platform === "threads") {{
      for (const a of document.querySelectorAll('a[href*="/post/"]')) {{
        const card = a.closest('div[data-pressable-container="true"], article, div') || a;
        const m = a.href.match(/@([^/]+)\\/post/);
        pushItem(card.innerText, a.href, m ? m[1] : "");
        if (out.length >= limit) break;
      }}
    }} else if (platform === "instagram") {{
      for (const a of document.querySelectorAll('a[href*="/reel/"], a[href*="/p/"]')) {{
        const img = a.querySelector("img");
        pushItem(img?.alt || a.innerText || a.href, a.href, "");
        if (out.length >= limit) break;
      }}
    }} else if (platform === "youtube") {{
      for (const a of document.querySelectorAll('a#video-title, a[href*="/shorts/"]')) {{
        pushItem(a.title || a.innerText, a.href, "");
        if (out.length >= limit) break;
      }}
    }}
    return out;
  }}, INPUT);
}} catch (e) {{
  items = [];
}} finally {{
  try {{ await task.finish({{ keep: [] }}); }} catch (_) {{}}
}}
console.log("{_MARKER}" + JSON.stringify(items));
"""
    data = _run_node(script, timeout=timeout)
    return data if isinstance(data, list) else []


def crawl_tiktok_comments(url, max_comments=15, timeout=TIMEOUT):
    """Extract anonymized top comments from a TikTok video via logged-in ego-browser (DOM-only, zero screenshots)."""
    if not url or not available():
        return []
    payload = json.dumps({"url": url, "limit": int(max_comments)})
    script = f"""
const INPUT = {payload};
const task = await taskSpace("oneup-tt-comments-" + Date.now());
let comments = [];
try {{
  const page = task.page("p1");
  try {{
    await page.goto(INPUT.url, {{ waitUntil: "domcontentloaded", timeout: 15000 }});
  }} catch (navErr) {{
    if (!String(navErr).includes("Timeout")) throw navErr;
  }}
  await new Promise((r) => setTimeout(r, 2500));
  comments = await page.evaluate((limit) => {{
    const out = [];
    const seen = new Set();
    const els = document.querySelectorAll('[data-e2e="comment-level-1"], p[data-e2e="comment-level-1"]');
    for (const el of els) {{
      const txt = (el.innerText || "").replace(/\\s+/g, " ").trim();
      if (txt.length < 8 || seen.has(txt.toLowerCase())) continue;
      seen.add(txt.toLowerCase());
      out.push({{ text: txt.slice(0, 280), likes: 0 }});
      if (out.length >= limit) break;
    }}
    return out;
  }}, INPUT.limit);
}} catch (e) {{
  comments = [];
}} finally {{
  try {{ await task.finish({{ keep: [] }}); }} catch (_) {{}}
}}
console.log("{_MARKER}" + JSON.stringify(comments));
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
    elif cmd == "social":
        if len(rest) < 2:
            print("Usage: ego_crawl.py social <tiktok|x|threads|instagram|youtube> \"<query>\" [--max 15]")
            return 2
        res = crawl_social(rest[0], " ".join(rest[1:]), max_items=int(opt("--max", 15)))
    elif cmd == "comments":
        res = crawl_tiktok_comments(rest[0] if rest else "", max_comments=int(opt("--max", 15)))
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
