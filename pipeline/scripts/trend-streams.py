#!/usr/bin/env python3
"""Three trend input streams for skills/trend-digest (v5). Stdlib only, offline, deterministic.

  trend-streams.py radar    [--date D] [--enqueue]        Luồng 1: TikTok Outlier Radar → research/trends/D/radar.json
  trend-streams.py upstream [--date D] [--check] [--top N] Luồng 2: score upstream/vn-tech news in research/trends/D/raw.json
  trend-streams.py inbox    [--date D] [--dry-run]         Luồng 3: media/footage/inbox/ links + files → teardown queue
  trend-streams.py queue    [--all]                        print the teardown queue with the exact teardown.py command

Radar: niche match (pipeline/trends/radar.yaml topics) AND (views ÷ follower ≥ min_ratio OR comment/share[/save] spike
between two snapshots 24–72h apart). Metadata kept: link, creator, follower, views, ratio, apify outlier + basis, topic tags,
growth, angle (empty: the agent writes the exploitation angle). --enqueue adds radar hits to the teardown queue.
Upstream: each shortlisted item needs `pain` (1–5, touches a mass pain), `story` (1–5, can be told as a story / visual metaphor)
and `fit` {"hi_oneup": 1–5, "vanhiep_tech": 1–5}. upstream_score = pain·story·max(fit)/125; `channel` = the better fit.
--check exits 1 when a shortlisted upstream item lacks a score (the digest must not ship unscored upstream news).
Inbox: URLs in *.txt/*.url/*.md and video files in media/footage/inbox/ get id trends-D-NN unless already in
research/trends/ingest.md or the queue (URL normalised; files by sha256). Rows go to research/trends/teardown-queue.json and
the «Inbox (Luồng 3)» table in ingest.md. Inbox files are never moved or deleted.
"""
import datetime as dt, hashlib, json, re, sys, unicodedata
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65

ROOT = P.ROOT
TRENDS = ROOT / "research/trends"
INBOX = ROOT / "media/footage/inbox"
QUEUE = TRENDS / "teardown-queue.json"
INGEST = TRENDS / "ingest.md"
RADAR_CFG = ROOT / "pipeline/trends/radar.yaml"
VIDEO = {".mp4", ".mov", ".webm", ".m4v", ".mkv"}
TEXT = {".txt", ".url", ".md", ".webloc"}
URL_RE = re.compile(r"https?://[^\s<>\"')\]]+")
INBOX_HEAD = "## Inbox (Luồng 3)"


def load_jsonish(p):
    return json.loads("\n".join(l for l in Path(p).read_text(encoding="utf-8").splitlines() if not l.lstrip().startswith("#")))


def fold(s):
    s = unicodedata.normalize("NFD", (s or "").lower())
    return unicodedata.normalize("NFC", "".join(c for c in s if unicodedata.category(c) != "Mn")).replace("đ", "d")


# ---------- Luồng 1: radar ----------
def topic_tags(clip, topics):
    """Topic groups a clip matches. Keywords ≤ 3 letters («ai») are ambiguous in Vietnamese («ai» = who, «it» ≈ «ít»):
    they match only an exact hashtag or the UPPERCASE form in the caption."""
    cap = clip.get("caption") or ""; tags = {fold(h) for h in (clip.get("hashtags") or [])}
    toks = " " + " ".join(re.findall(r"[a-z0-9]+", fold(cap + " " + " ".join(tags)))) + " "
    out = []
    for tag, kws in topics.items():
        for k in kws:
            kf = " ".join(re.findall(r"[a-z0-9]+", fold(k)))
            hit = (fold(k) in tags or re.search(rf"\b{re.escape(k.upper())}\b", cap)) if len(kf) <= 3 else f" {kf} " in toks or kf.replace(" ", "") in tags
            if hit: out.append(tag); break
    return out


def engagement(c):
    save = c.get("save_count", c.get("collect_count"))
    return (c.get("comment_count") or 0) + (c.get("share_count") or 0) + (save or 0), save


def clip_id(c):
    m = re.search(r"/video/(\d+)", c.get("url") or "")
    return m.group(1) if m else str(c.get("raw_id") or c.get("url"))


def snapshots(date, root=TRENDS):
    """[(datetime, clips)] from research/trends/<day>/apify/clips.json up to `date` (newest last)."""
    out = []
    for d in sorted(root.glob("20??-??-??")):
        f = d / "apify/clips.json"
        if d.name <= date and f.exists():
            try:
                doc = json.loads(f.read_text(encoding="utf-8"))
                ts = dt.datetime.fromtimestamp(f.stat().st_mtime) if d.name == date else dt.datetime.fromisoformat(d.name + "T12:00:00")
                clips = doc if isinstance(doc, list) else doc.get("clips", [])
                if isinstance(doc, dict) and doc.get("measured_at"): ts = dt.datetime.fromisoformat(doc["measured_at"])
                out.append((ts, clips))
            except (json.JSONDecodeError, ValueError):
                pass
    return out


def growth(cid, now_clip, now_ts, snaps, g):
    """Spike between the current measure and the oldest snapshot 24–72h before it (same clip)."""
    best = None
    for ts, clips in snaps:
        hours = (now_ts - ts).total_seconds() / 3600
        if g["min_hours"] <= hours <= g["max_hours"]:
            prev = next((c for c in clips if clip_id(c) == cid), None)
            if prev and (best is None or hours > best[0]): best = (hours, prev)
    if not best: return None
    e_now, save = engagement(now_clip); e_prev, _ = engagement(best[1])
    d = e_now - e_prev; pct = d / max(e_prev, 1)
    return {"hours": round(best[0], 1), "engagement_prev": e_prev, "engagement_now": e_now, "delta": d, "pct": round(pct, 2),
            "save_counted": save is not None, "spike": pct >= g["min_pct"] and d >= g["min_abs"]}


def radar(date, cfg=None, root=TRENDS):
    cfg = cfg or load_jsonish(RADAR_CFG)
    snaps = snapshots(date, root)
    if not snaps or snaps[-1][1] is None: return []
    cur = root / date / "apify/clips.json"
    if not cur.exists(): return []
    now_ts, clips = snaps[-1]
    rows = []
    for c in clips:
        tags = topic_tags(c, cfg["topics"])
        if not tags: continue
        fans = (c.get("author") or {}).get("fans") or 0; views = c.get("play_count") or 0
        ratio = round(views / fans, 2) if fans else None
        gr = growth(clip_id(c), c, now_ts, snaps[:-1], cfg["growth"])
        reasons = (["ratio≥%.1f" % cfg["min_ratio"]] if ratio is not None and ratio >= cfg["min_ratio"] else []) + (["growth spike"] if gr and gr["spike"] else [])
        if not reasons: continue
        author = (c.get("author") or {}).get("name") or ""
        rows.append({"id": f"{author}-{clip_id(c)}", "url": c.get("url"), "creator": author, "followers": fans, "views": views,
                     "ratio_views_followers": ratio, "apify_outlier": c.get("outlier"), "apify_basis": c.get("basis"),
                     "comments": c.get("comment_count"), "shares": c.get("share_count"), "saves": c.get("save_count", c.get("collect_count")),
                     "created": c.get("create_time"), "duration_s": c.get("duration_s"), "topic_tags": tags, "growth": gr,
                     "reasons": reasons, "angle": "", "teardown": None})
    rows.sort(key=lambda r: -(r["ratio_views_followers"] or 0))
    for r in rows:
        td = sorted(root.glob(f"*/teardowns/{r['id']}.md"))
        if td: r["teardown"] = str(td[-1].relative_to(ROOT)) if ROOT in td[-1].parents else str(td[-1])
    return rows


# ---------- Luồng 2: upstream scoring ----------
def score_upstream(it):
    p, s, f = it.get("pain"), it.get("story"), it.get("fit") or {}
    fits = {k: v for k, v in f.items() if isinstance(v, (int, float))}
    if not (isinstance(p, (int, float)) and isinstance(s, (int, float)) and fits): return None
    ch = max(fits, key=fits.get)
    it["upstream_score"] = round(p * s * fits[ch] / 125, 3); it["channel"] = ch
    return it["upstream_score"]


def upstream(raw, top=None):
    items = [i for i in raw.get("items", []) if i.get("stream") in ("upstream", "vn-tech")]
    short = [i for i in items if i.get("shortlist")] or sorted(items, key=lambda i: -(i.get("rank_score") or i.get("heat_score") or 0))[: top or 10]
    missing = [i["id"] for i in short if score_upstream(i) is None]
    return short, missing


# ---------- Luồng 3: inbox + queue ----------
def norm_url(u):
    u = u.strip().rstrip(".,;)")
    u = re.sub(r"[?#].*$", "", u)
    return u.rstrip("/").replace("://www.", "://").replace("://m.", "://").lower()


def load_queue(p=QUEUE):
    return json.loads(Path(p).read_text(encoding="utf-8")) if Path(p).exists() else {"items": []}


def save_queue(q, p=QUEUE):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    Path(p).write_text(json.dumps(q, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()


def next_id(q, date):
    n = [int(m.group(1)) for x in q["items"] if (m := re.match(rf"trends-{date}-(\d+)$", x["id"]))]
    return f"trends-{date}-{(max(n) + 1) if n else 1:02d}"


def known_urls(q, ingest_text):
    return {norm_url(u) for u in URL_RE.findall(ingest_text)} | {norm_url(x["source"]) for x in q["items"] if x["kind"] == "url"}


def enqueue(q, date, kind, source, origin, ingest_text, sha=None, meta=None):
    """Add one item unless it is already known. Returns the new row or None (duplicate)."""
    if kind == "url" and norm_url(source) in known_urls(q, ingest_text): return None
    if kind == "file" and any(x.get("sha256") == sha for x in q["items"]): return None
    row = {"id": next_id(q, date), "added": date, "kind": kind, "source": source, "origin": origin, "status": "queued", "teardown": None}
    if sha: row["sha256"] = sha
    if meta: row["meta"] = meta
    q["items"].append(row)
    return row


def scan_inbox(inbox=INBOX):
    urls, files = [], []
    if not Path(inbox).exists(): return urls, files
    for f in sorted(Path(inbox).rglob("*")):
        if not f.is_file() or f.name.startswith("."): continue
        if f.suffix.lower() in VIDEO: files.append(f)
        elif f.suffix.lower() in TEXT:
            urls += [(u.rstrip(".,;)"), f) for u in URL_RE.findall(f.read_text(encoding="utf-8", errors="ignore"))]
    return urls, files


def ingest_rows(rows, ingest=INGEST):
    t = Path(ingest).read_text(encoding="utf-8") if Path(ingest).exists() else ""
    if INBOX_HEAD not in t:
        t = t.rstrip("\n") + f"\n\n{INBOX_HEAD}\nLink hoặc file Hiệp ném vào `media/footage/inbox/`, gắn id bằng `pipeline/scripts/trend-streams.py inbox`; hàng đợi teardown ở `research/trends/teardown-queue.json`.\n\n| id | nguồn | thêm ngày | gốc | trạng thái | teardown |\n|---|---|---|---|---|---|\n"
    add = "".join(f"| {r['id']} | {r['source'] if r['kind'] == 'url' else Path(r['source']).name} | {r['added']} | {r['origin']} | {r['status']} | |\n" for r in rows)
    head, _, tail = t.partition(INBOX_HEAD)
    nxt = re.search(r"\n## ", tail)
    sec, rest = (tail[: nxt.start() + 1], tail[nxt.start() + 1:]) if nxt else (tail, "")
    Path(ingest).write_text(head + INBOX_HEAD + sec.rstrip("\n") + "\n" + add + ("\n" + rest if rest else ""), encoding="utf-8")


def inbox(date, dry=False, inbox_dir=INBOX, queue=QUEUE, ingest=INGEST):
    q = load_queue(queue); it = Path(ingest).read_text(encoding="utf-8") if Path(ingest).exists() else ""
    urls, files = scan_inbox(inbox_dir); new, dup = [], 0
    for u, f in urls:
        r = enqueue(q, date, "url", u, f"inbox:{f.name}", it)
        (new.append(r) if r else None); dup += r is None
    for f in files:
        r = enqueue(q, date, "file", str(f.relative_to(ROOT)) if ROOT in f.parents else str(f), "inbox", it, sha=sha256(f))
        (new.append(r) if r else None); dup += r is None
    if new and not dry:
        save_queue(q, queue); ingest_rows(new, ingest)
    return new, dup


def teardown_cmd(r):
    src = f"--url '{r['source']}'" if r["kind"] == "url" else f"'{r['source']}'"
    return f"python3 pipeline/scripts/teardown.py {src} --id {r['id']} --queue-id {r['id']}"


def mark_done(qid, teardown_path, queue=QUEUE, ingest=INGEST):
    q = load_queue(queue)
    for x in q["items"]:
        if x["id"] == qid:
            x["status"], x["teardown"] = "done", teardown_path
    save_queue(q, queue)
    if Path(ingest).exists():
        t = Path(ingest).read_text(encoding="utf-8")
        t = re.sub(rf"^(\| {re.escape(qid)} \|.*\|) queued \| \|$", lambda m: f"{m.group(1)} done | {teardown_path} |", t, flags=re.M)
        Path(ingest).write_text(t, encoding="utf-8")


def main():
    a = sys.argv[1:]
    if not a: print(__doc__); return 2
    def opt(n, d=None): return a[a.index(n) + 1] if n in a else d
    date = opt("--date", dt.date.today().isoformat()); cmd = a[0]
    if cmd == "radar":
        rows = radar(date)
        out = TRENDS / date / "radar.json"; out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps({"date": date, "config": str(RADAR_CFG.relative_to(ROOT)), "rows": rows}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("| creator | follower | view | view/follower | tăng 24–72h | chủ đề | lý do | link |\n|---|---|---|---|---|---|---|---|")
        for r in rows:
            g = r["growth"]; gs = f"+{g['delta']} ({g['pct']:.0%}, {g['hours']}h)" if g else "chưa có snapshot"
            print(f"| {r['creator']} | {r['followers']} | {r['views']} | {r['ratio_views_followers']}x | {gs} | {', '.join(r['topic_tags'])} | {', '.join(r['reasons'])} | {r['url']} |")
        print(f"→ {out} ({len(rows)} outlier)")
        if "--enqueue" in a:
            q = load_queue(); it = INGEST.read_text(encoding="utf-8") if INGEST.exists() else ""
            new = [x for x in (enqueue(q, date, "url", r["url"], f"radar:{r['ratio_views_followers']}x", it,
                                       meta={"radar_id": r["id"], "ratio": r["ratio_views_followers"], "topics": r["topic_tags"]}) for r in rows if not r["teardown"]) if x]
            if new: save_queue(q); ingest_rows(new)
            print(f"queue +{len(new)}")
        return 0
    if cmd == "upstream":
        rp = TRENDS / date / "raw.json"
        if not rp.exists(): print(f"missing {rp}"); return 2
        raw = json.loads(rp.read_text(encoding="utf-8"))
        short, missing = upstream(raw, int(opt("--top", "10")))
        rp.write_text(json.dumps(raw, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("| tin | luồng | nỗi đau | kể chuyện | hợp @hi.oneup | hợp @vanhiep.tech | điểm | kênh |\n|---|---|---|---|---|---|---|---|")
        for i in sorted(short, key=lambda i: -(i.get("upstream_score") or 0)):
            f = i.get("fit") or {}
            print(f"| {i.get('text', '')[:70]} | {i.get('stream')} | {i.get('pain', '–')} | {i.get('story', '–')} | {f.get('hi_oneup', '–')} | {f.get('vanhiep_tech', '–')} | {i.get('upstream_score', '–')} | {i.get('channel', '–')} |")
        if missing: print(f"✖ thiếu điểm pain/story/fit: {', '.join(missing)}")
        return 1 if (missing and "--check" in a) else 0
    if cmd == "inbox":
        new, dup = inbox(date, "--dry-run" in a)
        for r in new: print(f"+ {r['id']} {r['kind']} {r['source']}\n    {teardown_cmd(r)}")
        print(f"inbox: {len(new)} mới, {dup} trùng (đã có trong ingest.md / hàng đợi){' — dry run, chưa ghi' if '--dry-run' in a else ''}")
        return 0
    if cmd == "queue":
        for r in load_queue()["items"]:
            if "--all" in a or r["status"] == "queued":
                print(f"{r['id']:22} {r['status']:7} {r['origin']:24} {r['source']}" + (f"\n    {teardown_cmd(r)}" if r["status"] == "queued" else f" → {r['teardown']}"))
        return 0
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main())
