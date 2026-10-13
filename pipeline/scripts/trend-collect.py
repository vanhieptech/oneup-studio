#!/usr/bin/env python3
"""Collect raw trend candidates from free public sources (stdlib only; yt-dlp optional).

  trend-collect.py [--date YYYY-MM-DD] [--out DIR] [--extra file.json ...] [--only id,id]

Reads pipeline/trends/sources.yaml (JSON-compatible YAML). Fetches in parallel with timeouts, records
per-source status, normalises to the raw.json item schema, clusters near-duplicates across sources
(cross_sources = quality signal), applies a keyword brand-safety pre-filter, writes OUT/collect.json.
--extra: JSON list of items gathered by the agent via MCP tools (X trends/news, web search) using the
same keys (source, title, url, cat, lang, rank, metric). X lives behind MCP so a script cannot call it.
No logins, no cookies.
"""
import json, re, sys, html, subprocess, datetime as dt, urllib.request, urllib.parse, unicodedata
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
DROP = r"chết|tử vong|thiệt mạng|tai nạn|án mạng|giết|cướp|ma túy|khởi tố|bắt giữ|xét xử|lừa đảo|bão|lũ|động đất|cháy|chiến tranh|tấn công|quân đội|đảng|quốc hội|chính phủ|bầu cử|tôn giáo|cờ bạc|cá độ|xổ số|vé số|jackpot|độc đắc|sex|tình dục|buôn người|xhamster|khiêu dâm|tô lâm|thủ tướng|chủ tịch nước|killed|dead|death|shooting|murder|war|attack|military|election|trump|senate|congress|lawsuit|court|arrest|hurricane|flood|earthquake|gambling|porn|israel|gaza|ukraine|russia|iran"
CAUTION = r"ca sĩ|diễn viên|hoa hậu|celebrity|singer|actor|tỷ phú|billionaire|giá vàng|crypto|bitcoin|stock"
CATS = [("tech/AI", r"\bai\b|trí tuệ nhân tạo|chatgpt|openai|gemini|claude|agent|robot|iphone|apple|google|lập trình|code|developer|startup"),
        ("niche", r"trì hoãn|thói quen|năng suất|kỷ luật|học tập|tự học|deadline|procrastinat|habit|productiv|discipline|focus|burnout|study|lock in"),
        ("work/career", r"công sở|nhân viên|sếp|lương|việc làm|tuyển dụng|office|career|salary|layoff|job|work"),
        ("sports", r"bóng đá|đội tuyển|v-league|world cup|nfl|nba|premier league|football|soccer|vs\.?\b"),
        ("entertainment", r"phim|mv|ca khúc|anime|concert|movie|film|album|netflix|series|game"),
        ("meme", r"meme|trend|viral|gen z|slang|câu nói|hot trend")]

def get(url, t=15, raw=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "vi,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=t) as r:
        b = r.read()
    return b if raw else b.decode("utf-8", "replace")

def clean(s): return html.unescape(re.sub(r"<[^>]+>", " ", s or "")).strip()
def norm(s):
    s = unicodedata.normalize("NFD", (s or "").lower()); s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return " ".join(re.sub(r"[^\w\s]", " ", s.replace("đ", "d")).split())
def slug(s): return "-".join(norm(s).split()[:8])[:60] or "item"

def parse_feed(text):
    root = ET.fromstring(text.encode() if isinstance(text, str) else text); out = []
    for it in root.iter():
        tag = it.tag.split("}")[-1]
        if tag not in ("item", "entry"): continue
        g = lambda n: next((c for c in it if c.tag.split("}")[-1] == n), None)
        link = g("link"); url = (link.text or link.get("href") or "") if link is not None else ""
        first = lambda *ns: next((x for x in (g(n) for n in ns) if x is not None), None)
        t = g("title"); d = first("description", "summary"); p = first("pubDate", "published", "updated")
        out.append({"title": clean(t.text if t is not None else ""), "url": url.strip(),
                    "summary": clean(d.text if d is not None else "")[:300], "date": (p.text or "").strip() if p is not None else ""})
    return out

def s_rss(s): return parse_feed(get(s["url"]))
def s_gnews(s):
    if s.get("q"): u = "https://news.google.com/rss/search?q=" + urllib.parse.quote(s["q"])
    else: u = "https://news.google.com/rss?"
    u += ("&" if "?" in u and not u.endswith("?") else "") + f"hl={s['hl']}&gl={s['gl']}&ceid={s['gl']}:{s['hl'].split('-')[0]}"
    return parse_feed(get(u))
def s_gtrends(s):
    txt = get(f"https://trends.google.com/trending/rss?geo={s['geo']}"); out = []
    for i, it in enumerate(parse_feed(txt)):
        out.append(it)
    traffic = re.findall(r"<ht:approx_traffic>([^<]+)</ht:approx_traffic>", txt)
    newsurl = re.findall(r"<ht:news_item_url>([^<]+)</ht:news_item_url>", txt)
    for i, it in enumerate(out):
        if i < len(traffic): it["metric"] = {"traffic": traffic[i]}
        if not it["url"].startswith("http") or "trends.google" in it["url"]:
            it["url"] = f"https://trends.google.com/trends/explore?geo={s['geo']}&q=" + urllib.parse.quote(it["title"])
    return out
def s_hn(s):
    d = json.loads(get("https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=30"))
    return [{"title": h["title"], "url": h.get("url") or f"https://news.ycombinator.com/item?id={h['objectID']}",
             "summary": "", "metric": {"points": h.get("points"), "comments": h.get("num_comments")}} for h in d["hits"]]
def s_wiki(s):
    y = dt.date.fromisoformat(s["_date"]) - dt.timedelta(days=1)
    d = json.loads(get(f"https://wikimedia.org/api/rest_v1/metrics/pageviews/top/{s['project']}/all-access/{y:%Y/%m/%d}"))
    out = []
    for a in d["items"][0]["articles"]:
        t = a["article"]
        if ":" in t or t in ("Main_Page", "Trang_Chính", "-") or t.startswith("Wikipedia"): continue
        out.append({"title": t.replace("_", " "), "url": f"https://{s['project']}.org/wiki/{urllib.parse.quote(t)}", "summary": "", "metric": {"pageviews": a["views"]}})
    return out
def s_bsky_trending(s):
    d = json.loads(get("https://public.api.bsky.app/xrpc/app.bsky.unspecced.getTrendingTopics"))
    return [{"title": t.get("displayName") or t["topic"], "url": "https://bsky.app" + t["link"], "summary": t.get("description", "")} for t in d.get("topics", [])]
def s_bsky_search(s):
    d = json.loads(get("https://api.bsky.app/xrpc/app.bsky.feed.searchPosts?sort=top&limit=25&q=" + urllib.parse.quote(s["q"])))
    out = []
    for p in d.get("posts", []):
        rk = p["uri"].split("/")[-1]
        out.append({"title": p["record"].get("text", "")[:140], "url": f"https://bsky.app/profile/{p['author']['handle']}/post/{rk}",
                    "summary": "", "metric": {"likes": p.get("likeCount"), "reposts": p.get("repostCount")}})
    return sorted(out, key=lambda x: -(x["metric"]["likes"] or 0))
def s_kworb(s):
    t = get(s["url"]); out = []
    for m in re.finditer(r'<td class="text mp"><div>(.*?)</div></td>', t):
        out.append({"title": clean(m.group(1)), "url": s["url"], "summary": ""})
    return out
def s_yt(s):
    r = subprocess.run([sys.executable, "-m", "yt_dlp", "--flat-playlist", "-J", f"ytsearch{s.get('max', 8)}:{s['q']}"], capture_output=True, text=True, timeout=60)
    d = json.loads(r.stdout)
    return [{"title": e.get("title", ""), "url": e.get("url") or f"https://www.youtube.com/watch?v={e['id']}", "summary": "",
             "metric": {"views": e.get("view_count")}} for e in d.get("entries", [])]

FN = {"rss": s_rss, "gnews": s_gnews, "gtrends": s_gtrends, "hn": s_hn, "wiki": s_wiki, "bsky_trending": s_bsky_trending,
      "bsky_search": s_bsky_search, "kworb": s_kworb, "yt": s_yt}

def run(s):
    t0 = dt.datetime.now()
    try:
        items = FN[s["type"]](s)[: s.get("max", 20)]
        st = "ok" if items else "empty"; err = ""
    except Exception as e:
        items, st, err = [], "error", f"{type(e).__name__}: {e}"[:200]
    for i, it in enumerate(items):
        it.update(source=s["id"], cat=s["cat"], lang=s["lang"], rank=i + 1)
    return {"source": s["id"], "type": s["type"], "status": st, "count": len(items), "error": err,
            "ms": int((dt.datetime.now() - t0).total_seconds() * 1000)}, items

def classify(text, default):
    n = text.lower()
    for c, rx in CATS:
        if re.search(rx, n): return c
    return default

FIT = {"niche": .9, "work/career": .75, "tech/AI": .7, "social": .7, "meme": .65, "viral": .6, "lifestyle": .55,
       "entertainment": .4, "celebrity": .35, "music": .35, "hot": .4, "sports": .3, "news": .3}
def auto_score(it):
    """Heuristic first-pass scores (agent overrides for the shortlist). heat: cross-source + rank + metrics."""
    s = it["signals"]; m = json.dumps(s["metrics"])
    nums = [int(re.sub(r"\D", "", x) or 0) for x in re.findall(r'"(?:traffic|points|views|likes|pageviews)": "?([\d,+]+)', m)]
    big = max(nums or [0])
    metric = min(1.0, (len(str(big)) - 2) / 5) if big else 0.2
    heat = 0.4 * min(1, (s["cross_sources"] - 1) / 2) + 0.3 * (1 - min(s["best_rank"], 20) / 20) + 0.3 * metric
    it["heat_score"] = round(min(1, heat + 0.1), 2)
    it["fit_score"] = FIT.get(it["category"], .4)
    it["bridgeability"] = round(min(1, it["fit_score"] + (0.1 if it["category"] in ("meme", "viral", "social") else 0)), 2)
    it["saturation_signal"] = 0.0
    it["patterns"] = []
    if all(x.startswith("yt-") for x in s["sources"]):  # evergreen niche videos = hook/saturation evidence, not news
        it["kind"] = "pattern-evidence"; it["saturation_signal"] = 0.8

def main():
    a = sys.argv[1:]; opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    date = opt("--date", dt.date.today().isoformat())
    out = Path(opt("--out", ROOT / "research" / "trends" / date)); out.mkdir(parents=True, exist_ok=True)
    cfg = json.loads("\n".join(l for l in (ROOT / "pipeline/trends/sources.yaml").read_text().splitlines() if not l.lstrip().startswith("#")))
    srcs = [dict(s, _date=date) for s in cfg["sources"]]
    if opt("--only"): srcs = [s for s in srcs if s["id"] in opt("--only").split(",")]
    with ThreadPoolExecutor(12) as ex: res = list(ex.map(run, srcs))
    status = [r[0] for r in res]; flat = [i for r in res for i in r[1]]
    extras = [a[i + 1] for i, x in enumerate(a) if x == "--extra"]
    for f in extras:
        ex_items = json.loads(Path(f).read_text()); flat += ex_items
        for src in sorted({i["source"] for i in ex_items}):
            status.append({"source": src, "type": "mcp/agent", "status": "ok", "count": sum(1 for i in ex_items if i["source"] == src), "error": "", "ms": 0})
    # cluster near-duplicates (token Jaccard >= 0.5 on normalised titles)
    clusters = []
    for it in flat:
        if not it.get("title"): continue
        w = set(norm(it["title"]).split()); hit = None
        for c in clusters:
            if w and len(w & c["_w"]) / max(len(w | c["_w"]), 1) >= 0.5: hit = c; break
        if hit: hit["members"].append(it); hit["_w"] |= w
        else: clusters.append({"_w": w, "members": [it]})
    items = []
    for c in clusters:
        m = c["members"][0]; text = m["title"] + " " + m.get("summary", "")
        nsrc = len({x["source"] for x in c["members"]}); best = min(x["rank"] for x in c["members"])
        safety = "drop" if re.search(DROP, text.lower()) else "caution" if re.search(CAUTION, text.lower()) else "ok"
        items.append({"id": slug(m["title"]), "kind": "news", "category": classify(text, m["cat"]), "lang": m["lang"],
                      "text": m["title"], "summary": m.get("summary", "")[:300],
                      "signals": {"sources": sorted({x["source"] for x in c["members"]}), "cross_sources": nsrc, "best_rank": best,
                                  "metrics": {x["source"]: x["metric"] for x in c["members"] if x.get("metric")}},
                      "evidence": [{"url": x["url"], "publisher": x["source"], "date": x.get("date") or date} for x in c["members"][:3]],
                      "safety": safety, "safety_reason": "auto keyword pre-filter; agent must confirm"})
    for it in items: auto_score(it)
    doc = {"date": date, "collected_at": dt.datetime.now().isoformat(timespec="seconds"), "collector": "trend-collect.py v1",
           "sources_tried": status, "raw_count": len(flat), "cluster_count": len(items),
           "by_safety": {k: sum(1 for i in items if i["safety"] == k) for k in ("ok", "caution", "drop")}, "items": items}
    (out / "collect.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1))
    for s in status: print(f"{s['status']:6} {s['count']:4}  {s['source']:22} {s['error']}")
    print(f"raw={len(flat)} clusters={len(items)} safety={doc['by_safety']} -> {out/'collect.json'}")

if __name__ == "__main__": main()
