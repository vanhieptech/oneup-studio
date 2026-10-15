#!/usr/bin/env python3
"""Normalize Apify TikTok actor dataset items → required clip fields for trend-digest.

Usage:
  python3 pipeline/scripts/trend-apify-normalize.py \
    --actor clockworks/tiktok-scraper \
    --dataset path/to/items.json \
    [--comments path/to/comments.json] \
    [--vtt-dir path/to/vtt/] \
    --out research/trends/YYYY-MM-DD/apify/clips.json

Required output fields per clip:
  url, caption, author, play_count, like_count, share_count, comment_count,
  duration_s, music, hashtags[], subtitle_or_transcript, top_comments[],
  source_actor, raw_id
"""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

def _get(d, *keys, default=None):
    for k in keys:
        if isinstance(d, dict) and k in d and d[k] not in (None, ""):
            return d[k]
    return default

def _author(item):
    am = item.get("authorMeta") or {}
    if isinstance(am, dict) and am:
        name = am.get("name") or am.get("uniqueId") or am.get("nickName")
        nick = am.get("nickName") or am.get("name")
        return {"id": am.get("id"), "name": name, "nick": nick, "profile": am.get("profileUrl"), "fans": am.get("fans")}
    # flattened
    name = _get(item, "authorMeta.name", "author", "uniqueId", "authorName")
    return {"id": None, "name": name, "nick": _get(item, "authorMeta.nickName", "nickname"), "profile": None, "fans": _get(item, "authorMeta.fans")}

def _music(item):
    mm = item.get("musicMeta") or {}
    if isinstance(mm, dict) and mm:
        return {"id": mm.get("musicId"), "name": mm.get("musicName"), "author": mm.get("musicAuthor"), "original": mm.get("musicOriginal")}
    return {"id": None, "name": _get(item, "musicMeta.musicName", "musicName", "sound"), "author": _get(item, "musicMeta.musicAuthor"), "original": _get(item, "musicMeta.musicOriginal")}

def _hashtags(item):
    hs = item.get("hashtags") or []
    out = []
    if isinstance(hs, list):
        for h in hs:
            if isinstance(h, dict):
                n = h.get("name") or h.get("title")
                if n: out.append(n.lstrip("#"))
            elif isinstance(h, str):
                out.append(h.lstrip("#"))
    # from caption
    cap = _get(item, "text", "caption", "desc", default="") or ""
    for m in re.findall(r"#([\wÀ-ỹ]+)", cap, flags=re.UNICODE):
        if m not in out: out.append(m)
    sh = _get(item, "searchHashtag.name")
    if sh and sh not in out: out.insert(0, sh)
    return out

def _duration(item):
    vm = item.get("videoMeta") or {}
    if isinstance(vm, dict):
        d = vm.get("duration")
        if d is not None: return d
    return _get(item, "videoMeta.duration", "duration", "videoDuration")

def _subtitle(item, vtt_dir: Path | None):
    vm = item.get("videoMeta") or {}
    links = []
    if isinstance(vm, dict):
        if vm.get("transcriptionLink"):
            links.append(("transcription", vm["transcriptionLink"]))
        for s in (vm.get("subtitleLinks") or []) or []:
            if isinstance(s, dict):
                links.append((s.get("language") or s.get("source") or "sub", s.get("downloadLink") or s.get("tiktokLink") or s.get("url")))
            elif isinstance(s, str):
                links.append(("sub", s))
    # parseforge-style
    tr = _get(item, "transcript", "transcription", "subtitle", "captionsText")
    if tr:
        return {"kind": "transcript", "text": tr if isinstance(tr, str) else json.dumps(tr, ensure_ascii=False), "links": []}
    text = None
    if vtt_dir and vtt_dir.exists():
        vid = str(_get(item, "id", "videoId", default=""))
        for p in vtt_dir.glob("*"):
            if vid and vid in p.name:
                text = p.read_text(errors="replace")[:8000]
                return {"kind": "vtt", "text": text, "links": [str(p)], "file": p.name}
    caption = _get(item, "text", "caption", "desc", default="") or ""
    return {"kind": "caption_fallback", "text": caption, "links": [u for _, u in links if u]}

def _comments_for(url, comments_by_url, item):
    if url and url in comments_by_url:
        return comments_by_url[url][:20]
    # inline
    for key in ("comments", "topComments", "top_comments"):
        c = item.get(key)
        if isinstance(c, list) and c:
            out = []
            for x in c[:20]:
                if isinstance(x, dict):
                    out.append({"text": x.get("text") or x.get("comment") or "", "likes": x.get("diggCount") or x.get("likes") or 0, "author": x.get("uniqueId") or x.get("author")})
                else:
                    out.append({"text": str(x), "likes": 0, "author": None})
            return out
    return []

def normalize_item(item, actor: str, comments_by_url: dict, vtt_dir: Path | None):
    url = _get(item, "webVideoUrl", "url", "submittedVideoUrl", "videoUrl", "video_url")
    caption = _get(item, "text", "caption", "desc", default="") or ""
    sub = _subtitle(item, vtt_dir)
    return {
        "url": url,
        "caption": caption,
        "author": _author(item),
        "play_count": _get(item, "playCount", "play_count", "plays", default=0) or 0,
        "like_count": _get(item, "diggCount", "likeCount", "like_count", "likes", default=0) or 0,
        "share_count": _get(item, "shareCount", "share_count", "shares", default=0) or 0,
        "comment_count": _get(item, "commentCount", "comment_count", "commentsCount", default=0) or 0,
        "duration_s": _duration(item),
        "music": _music(item),
        "hashtags": _hashtags(item),
        "subtitle_or_transcript": sub,
        "top_comments": _comments_for(url, comments_by_url, item),
        "source_actor": actor,
        "raw_id": _get(item, "id", "videoId", "cid"),
        "create_time": _get(item, "createTimeISO", "createTime", "create_time"),
        "is_slideshow": bool(_get(item, "isSlideshow", "is_slideshow", default=False)),
    }

def load_comments(path: Path | None):
    by = {}
    if not path or not path.exists(): return by
    data = json.loads(path.read_text())
    items = data if isinstance(data, list) else data.get("items") or data.get("comments") or []
    for c in items:
        if not isinstance(c, dict): continue
        url = _get(c, "videoWebUrl", "submittedVideoUrl", "input", "url")
        if not url: continue
        by.setdefault(url, []).append({
            "text": c.get("text") or "",
            "likes": c.get("diggCount") or 0,
            "author": c.get("uniqueId") or c.get("uid"),
        })
    for url in by:
        by[url].sort(key=lambda x: -(x["likes"] or 0))
    return by

def field_coverage(clips):
    req = ["url","caption","author","play_count","like_count","share_count","comment_count","duration_s","music","hashtags","subtitle_or_transcript","top_comments"]
    cov = {k: 0 for k in req}
    for c in clips:
        for k in req:
            v = c.get(k)
            ok = False
            if k == "author": ok = bool((v or {}).get("name"))
            elif k == "music": ok = bool((v or {}).get("name"))
            elif k == "hashtags": ok = isinstance(v, list)  # empty ok but count present
            elif k == "subtitle_or_transcript": ok = bool((v or {}).get("text") or (v or {}).get("kind"))
            elif k == "top_comments": ok = isinstance(v, list)  # may be empty if comments actor not run
            elif k in ("play_count","like_count","share_count","comment_count"): ok = v is not None
            else: ok = v not in (None, "")
            if ok: cov[k] += 1
    n = max(len(clips), 1)
    return {k: {"present": v, "of": len(clips), "pct": round(100*v/n,1)} for k,v in cov.items()}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--actor", required=True)
    ap.add_argument("--dataset", required=True)
    ap.add_argument("--comments")
    ap.add_argument("--vtt-dir")
    ap.add_argument("--out", required=True)
    ap.add_argument("--run-id")
    args = ap.parse_args()
    raw = json.loads(Path(args.dataset).read_text())
    items = raw if isinstance(raw, list) else raw.get("items") or raw.get("data") or []
    comments = load_comments(Path(args.comments) if args.comments else None)
    vtt_dir = Path(args.vtt_dir) if args.vtt_dir else None
    clips = [normalize_item(it, args.actor, comments, vtt_dir) for it in items if isinstance(it, dict)]
    out = {
        "actor": args.actor,
        "run_id": args.run_id,
        "item_count": len(clips),
        "fields_coverage": field_coverage(clips),
        "clips": clips,
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(json.dumps({"wrote": args.out, "item_count": len(clips), "fields_coverage": out["fields_coverage"]}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
