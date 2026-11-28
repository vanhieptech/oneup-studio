#!/usr/bin/env python3
"""Local Multi-Channel Short-form Outlier Radar collector (Luồng 1, zero paid API).

  radar-fetch.py [--date YYYY-MM-DD] [--config pipeline/trends/radar.yaml]
                 [--limit 10] [--only handle1,handle2] [--role direct_niche,cross_niche_craft]
                 [--with-comments] [--no-enqueue] [--dry-run]

Supports 3 channel roles in `pipeline/trends/radar.yaml`:
  - `direct_niche`:      Same niche — learn ideas, structure, and keywords (`learn_scope: idea_and_craft`).
  - `cross_niche_craft`: Other high-retention niches (finance, storytelling, science, global/VN tech) —
                         learn hook, transitions, metaphor, and pacing ONLY (`learn_scope: craft_only`).
  - `anti_pattern`:      High-view hollow/clickbait channels — log errors to avoid (`learn_scope: avoid_only`).

Extracts Top Comments (when present in yt-dlp metadata or when `--with-comments` fetches per-outlier metadata)
and saves anonymized audience pain/phrasing into `research/trends/<date>/audience-language.md`.

Writes:
  - research/trends/<date>/radar-raw.json       (normalized clip snapshot for multi-day growth tracking)
  - research/trends/<date>/radar.json           (outlier rows in trend-streams.py schema + role/learn_scope)
  - research/trends/<date>/audience-language.md (when top comments are found)
and automatically calls `pipeline/scripts/trend-streams.py radar --date <date> --enqueue`
unless `--no-enqueue` or `--dry-run` is given.
"""
import datetime as dt
import importlib.util
import json
import re
import shutil
import statistics
import subprocess
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65

ROOT = P.ROOT
TRENDS = ROOT / "research/trends"
RADAR_CFG = ROOT / "pipeline/trends/radar.yaml"

VALID_ROLES = ("direct_niche", "global_niche_source", "southern_story_voice", "cross_niche_craft", "anti_pattern")
LEARN_SCOPE = {
    "direct_niche": "idea_and_craft",
    "global_niche_source": "idea_and_craft_localize",
    "southern_story_voice": "voice_cadence_only",
    "cross_niche_craft": "craft_only",
    "anti_pattern": "avoid_only",
}
DEFAULT_MIN_VIEWS_PER_DAY = 15000.0
DEFAULT_MIN_ENGAGEMENT_INTENSITY = 0.015
DEFAULT_MIN_ABS_VIEWS_FOR_VELOCITY = 50000
DEFAULT_TTL_HOURS = 6.0
DEFAULT_WORKERS = 6
SPIKE_VIEWS_PCT = 0.50
SPIKE_ENGAGEMENT_ABS = 100
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"


def _load_json(path, default):
    p = Path(path)
    if not p.exists():
        return default
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return default


def _save_json(path, data):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def fetch_youtube_rss(channel_id, etag=None, timeout=10):
    """Fast-path (~0.2s) YouTube Atom RSS check with ETag support. Returns (status, entries_or_none, new_etag)."""
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    headers = {"User-Agent": UA}
    if etag:
        headers["If-None-Match"] = etag
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read().decode("utf-8", "replace")
            new_etag = r.headers.get("ETag")
    except urllib.error.HTTPError as e:
        if e.code == 304:
            return "not_modified", None, etag
        return f"http_{e.code}", None, etag
    except Exception:
        return "error", None, etag
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return "parse_error", None, new_etag
    ids = []
    for entry in root.iter():
        if entry.tag.endswith("}videoId") or entry.tag == "videoId":
            if entry.text:
                ids.append(entry.text.strip())
    return "ok", ids, new_etag


def load_seen_index(root=TRENDS):
    return _load_json(Path(root) / "seen-index.json", {"updated": None, "videos": {}})


def apply_seen_dedupe(rows, root=TRENDS, include_seen=False, save=True):
    """Filter out unchanged already-seen videos using `seen-index.json`, keeping `new` and `spike` (+50% views or +100 comments/shares)."""
    idx = load_seen_index(root)
    videos = idx.setdefault("videos", {})
    now_iso = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    kept, skipped = [], []
    for r in rows:
        vid_key = r["id"]
        views = int(r.get("views") or 0)
        eng = int(r.get("comments") or 0) + int(r.get("shares") or 0)
        prev = videos.get(vid_key)
        if not prev:
            r["dedupe_status"] = "new"
            videos[vid_key] = {
                "first_seen": now_iso,
                "last_seen": now_iso,
                "views": views,
                "engagement": eng,
                "creator": r.get("creator"),
                "url": r.get("url"),
                "status": "new",
            }
            kept.append(r)
            continue
        prev_v = int(prev.get("views") or 0)
        prev_e = int(prev.get("engagement") or 0)
        view_growth = (views - prev_v) / max(prev_v, 1) if prev_v > 0 else 0.0
        eng_delta = eng - prev_e
        is_spike = (prev_v > 0 and view_growth >= SPIKE_VIEWS_PCT) or (eng_delta >= SPIKE_ENGAGEMENT_ABS)
        prev["last_seen"] = now_iso
        prev["views"] = max(prev_v, views)
        prev["engagement"] = max(prev_e, eng)
        if prev.get("status") == "done":
            r["dedupe_status"] = "done"
            skipped.append(r)
        elif is_spike:
            r["dedupe_status"] = "spike"
            r["reasons"] = list(r.get("reasons") or []) + [f"spike+{int(view_growth * 100)}%"]
            prev["status"] = "spike"
            kept.append(r)
        else:
            r["dedupe_status"] = "seen"
            prev["status"] = "seen"
            if include_seen:
                kept.append(r)
            else:
                skipped.append(r)
    idx["updated"] = now_iso
    if save:
        _save_json(Path(root) / "seen-index.json", idx)
    return kept, skipped


def _load_trend_streams():
    p = Path(__file__).resolve().parent / "trend-streams.py"
    sp = importlib.util.spec_from_file_location("trend_streams", str(p))
    mod = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(mod)
    return mod


def load_config(path=RADAR_CFG):
    lines = [l for l in Path(path).read_text(encoding="utf-8").splitlines() if not l.lstrip().startswith("#")]
    return json.loads("\n".join(lines))


def ytdlp_cmd():
    for cand in (shutil.which("yt-dlp"), "/opt/homebrew/bin/yt-dlp", "/usr/local/bin/yt-dlp"):
        if cand and Path(cand).exists():
            return [cand]
    return [sys.executable, "-m", "yt_dlp"]


def fetch_channel_entries(url, limit=10, timeout=90):
    """Run `yt-dlp --flat-playlist --dump-json --playlist-end <limit> <url>` and parse JSON lines."""
    cmd = [*ytdlp_cmd(), "--flat-playlist", "--dump-json", "--no-warnings", "--ignore-errors",
           "--playlist-end", str(limit), url]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    entries = []
    for line in (r.stdout or "").splitlines():
        line = line.strip()
        if not line or not line.startswith("{"):
            continue
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    err = "" if entries else (r.stderr or "").strip()[-240:]
    return entries, err


def fetch_video_comments(url, max_comments=10, timeout=60):
    """Fetch top comments for one outlier video via yt-dlp without downloading media."""
    cmd = [
        *ytdlp_cmd(), "--skip-download", "--dump-json", "--write-comments", "--no-warnings",
        "--extractor-args", f"youtube:max_comments={max_comments},all,0,0",
        url,
    ]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except Exception:
        return []
    for line in (r.stdout or "").splitlines():
        line = line.strip()
        if line.startswith("{"):
            try:
                doc = json.loads(line)
                return extract_top_comments(doc, limit=max_comments)
            except json.JSONDecodeError:
                continue
    return []


def extract_top_comments(entry, limit=5):
    """Extract top anonymized comments (text + likes) from yt-dlp metadata if present."""
    raw = entry.get("comments") or entry.get("top_comments") or []
    if not isinstance(raw, list):
        return []
    cleaned = []
    seen = set()
    for c in raw:
        if isinstance(c, str):
            text, likes = c.strip(), 0
        elif isinstance(c, dict):
            text = (c.get("text") or c.get("comment") or "").strip()
            likes = int(c.get("like_count") or c.get("likes") or 0)
        else:
            continue
        text = re.sub(r"\s+", " ", text)
        if len(text) < 8:
            continue
        key = text.lower()
        if key in seen:
            continue
        seen.add(key)
        cleaned.append({"text": text[:280], "likes": likes})
    cleaned.sort(key=lambda x: (-x["likes"], -len(x["text"])))
    return cleaned[:limit]


def extract_hashtags(text):
    return [m.group(1) for m in re.finditer(r"#([0-9A-Za-zÀ-ỹđ_]+)", text or "")]


def entry_to_clip(entry, ch_cfg, median_views):
    """Convert one yt-dlp JSON entry into the normalized clip schema shared with trend-streams.py."""
    handle = (ch_cfg.get("handle") or entry.get("uploader_id") or entry.get("channel") or entry.get("uploader") or "").lstrip("@")
    platform = ch_cfg.get("platform", "tiktok")
    role = ch_cfg.get("role") if ch_cfg.get("role") in VALID_ROLES else "direct_niche"
    vid = str(entry.get("id") or "")
    url = entry.get("webpage_url") or entry.get("url") or ""
    if url and not url.startswith("http") and platform == "tiktok" and handle:
        url = f"https://www.tiktok.com/@{handle}/video/{vid or url}"
    elif url and not url.startswith("http") and platform == "youtube" and vid:
        url = f"https://www.youtube.com/shorts/{vid}"
    elif not url and handle and vid:
        url = f"https://www.tiktok.com/@{handle}/video/{vid}" if platform == "tiktok" else f"https://www.youtube.com/shorts/{vid}"

    caption = (entry.get("description") or entry.get("title") or "").strip()
    views = int(entry.get("view_count") or 0)
    likes = int(entry.get("like_count") or 0) if entry.get("like_count") is not None else None
    comments = int(entry.get("comment_count") or 0) if entry.get("comment_count") is not None else 0
    shares = int(entry.get("repost_count") or entry.get("share_count") or 0)
    saves = entry.get("save_count", entry.get("collect_count"))
    fans = int(ch_cfg.get("followers") or entry.get("channel_follower_count") or 0)
    dur = entry.get("duration")
    ts = entry.get("timestamp")
    if ts:
        created = dt.datetime.fromtimestamp(int(ts), tz=dt.timezone.utc).isoformat()
    elif entry.get("upload_date") and len(str(entry["upload_date"])) == 8:
        ud = str(entry["upload_date"])
        created = f"{ud[:4]}-{ud[4:6]}-{ud[6:8]}"
    else:
        created = None

    outlier_ratio = round(views / median_views, 2) if median_views and median_views > 0 else None
    follower_ratio = round(views / fans, 2) if fans > 0 else None
    effective_ratio = follower_ratio if follower_ratio is not None else outlier_ratio
    basis = "views/followers" if follower_ratio is not None else ("views/median_views" if outlier_ratio is not None else None)
    top_comments = extract_top_comments(entry)
    engagement_intensity = round((comments * 3 + shares * 2) / views, 5) if views > 0 else None
    views_per_day = None
    if views > 0 and created:
        try:
            c_dt = dt.datetime.fromisoformat(created.replace("Z", "+00:00"))
            if c_dt.tzinfo is None:
                c_dt = c_dt.replace(tzinfo=dt.timezone.utc)
            age_days = max(0.25, (dt.datetime.now(dt.timezone.utc) - c_dt).total_seconds() / 86400.0)
            views_per_day = round(views / age_days, 1)
        except ValueError:
            views_per_day = None

    return {
        "raw_id": vid or url,
        "url": url,
        "platform": platform,
        "lang": ch_cfg.get("lang") or "vi",
        "role": role,
        "learn_scope": LEARN_SCOPE[role],
        "format_compatibility": ch_cfg.get("format_compatibility") or "story_metaphor",
        "craft_focus": list(ch_cfg.get("craft_focus") or []),
        "caption": caption,
        "hashtags": list(dict.fromkeys((entry.get("tags") or []) + extract_hashtags(caption))),
        "author": {"name": handle, "fans": fans},
        "play_count": views,
        "like_count": likes,
        "comment_count": comments,
        "share_count": shares,
        "save_count": saves,
        "top_comments": top_comments,
        "duration_s": round(float(dur), 1) if dur is not None else None,
        "create_time": created,
        "median_views": round(median_views, 1) if median_views else None,
        "outlier_ratio": outlier_ratio,
        "outlier": effective_ratio,
        "views_per_day": views_per_day,
        "engagement_intensity": engagement_intensity,
        "basis": basis,
        "channel_niche": ch_cfg.get("niche") or [],
        "niche_verified": bool(ch_cfg.get("niche_verified")),
        "source": "radar-fetch (yt-dlp)",
    }


def normalize_channel(ch_cfg, entries):
    """Compute channel median views across fetched entries and return normalized clip dicts."""
    view_counts = [int(e.get("view_count") or 0) for e in entries if (e.get("view_count") or 0) > 0]
    median_views = float(statistics.median(view_counts)) if view_counts else 0.0
    return [entry_to_clip(e, ch_cfg, median_views) for e in entries], median_views


def build_radar_rows(clips, cfg, date, ts_mod=None, root=TRENDS):
    """Filter clips into outlier radar rows matching trend-streams.py schema + channel role."""
    ts = ts_mod or _load_trend_streams()
    min_ratio = float(cfg.get("min_ratio", 3.0))
    min_vpd = float(cfg.get("min_views_per_day", DEFAULT_MIN_VIEWS_PER_DAY))
    min_eng = float(cfg.get("min_engagement_intensity", DEFAULT_MIN_ENGAGEMENT_INTENSITY))
    min_abs_v = int(cfg.get("min_abs_views_for_velocity", DEFAULT_MIN_ABS_VIEWS_FOR_VELOCITY))
    rows = []
    for c in clips:
        role = c.get("role") if c.get("role") in VALID_ROLES else "direct_niche"
        tags = ts.topic_tags(c, cfg.get("topics", {}))
        if not tags:
            if role == "cross_niche_craft":
                tags = list(c.get("channel_niche") or ["cross-niche-craft"])
            elif role == "global_niche_source":
                tags = list(c.get("channel_niche") or ["global-niche-source"])
            elif role == "southern_story_voice":
                tags = list(c.get("channel_niche") or ["southern-story-voice"])
            elif role == "anti_pattern":
                tags = list(c.get("channel_niche") or ["anti-pattern"])
            elif c.get("niche_verified") and c.get("channel_niche"):
                tags = list(c["channel_niche"])
        if not tags:
            continue
        fans = (c.get("author") or {}).get("fans") or 0
        views = c.get("play_count") or 0
        comments = c.get("comment_count") or 0
        ratio_f = round(views / fans, 2) if fans else None
        ratio_m = c.get("outlier_ratio")
        vpd = c.get("views_per_day")
        eng = c.get("engagement_intensity")
        reasons = []
        if ratio_f is not None and ratio_f >= min_ratio:
            reasons.append(f"ratio≥{min_ratio:.1f}")
        if ratio_m is not None and ratio_m >= min_ratio:
            reasons.append(f"median≥{min_ratio:.1f}x")
        # Fallback for big channels with followers=0 whose clips consistently hit high views (ratio_m ≈ 1.0–2.5x)
        if not reasons and fans == 0 and views >= min_abs_v:
            if vpd is not None and vpd >= min_vpd:
                reasons.append(f"velocity≥{int(min_vpd)}/d")
            if eng is not None and eng >= min_eng and comments >= 50:
                reasons.append(f"engagement≥{min_eng:.3f}")
            # YouTube Shorts --flat-playlist omits upload_date & comment_count: catch proven superstar/mega hits
            if not reasons and views >= int(cfg.get("min_megahit_views", 1000000)):
                reasons.append("megahit≥1M")
            elif not reasons and views >= 300000 and ratio_m is not None and ratio_m >= 1.5:
                reasons.append("superstar≥1.5x+300k")
        if not reasons:
            continue
        author = (c.get("author") or {}).get("name") or ""
        rows.append({
            "id": f"{author}-{ts.clip_id(c)}",
            "url": c.get("url"),
            "platform": c.get("platform", "tiktok"),
            "lang": c.get("lang", "vi"),
            "role": role,
            "learn_scope": c.get("learn_scope") or LEARN_SCOPE[role],
            "format_compatibility": c.get("format_compatibility") or "story_metaphor",
            "craft_focus": c.get("craft_focus") or [],
            "creator": author,
            "followers": fans,
            "views": views,
            "median_views": c.get("median_views"),
            "ratio_views_followers": ratio_f,
            "outlier_ratio": ratio_m,
            "views_per_day": vpd,
            "engagement_intensity": eng,
            "apify_outlier": c.get("outlier"),
            "apify_basis": c.get("basis"),
            "comments": comments,
            "top_comments": c.get("top_comments") or [],
            "shares": c.get("share_count"),
            "saves": c.get("save_count"),
            "created": c.get("create_time"),
            "duration_s": c.get("duration_s"),
            "topic_tags": tags,
            "growth": None,
            "reasons": reasons,
            "angle": "",
            "teardown": None,
        })
    rows.sort(key=lambda r: -(r["ratio_views_followers"] or r["outlier_ratio"] or 0))
    for r in rows:
        td = sorted(Path(root).glob(f"*/teardowns/{r['id']}.md"))
        if td:
            r["teardown"] = str(td[-1].relative_to(ROOT)) if ROOT in td[-1].parents else str(td[-1])
    return rows


def render_audience_language(date, clips):
    """Build `research/trends/<date>/audience-language.md` from anonymized top comments."""
    items = []
    for c in clips:
        tc = c.get("top_comments") or []
        if not tc:
            continue
        author = (c.get("author") or {}).get("name") or ""
        role = c.get("role", "direct_niche")
        url = c.get("url") or ""
        for cm in tc:
            items.append({
                "creator": author,
                "role": role,
                "url": url,
                "likes": int(cm.get("likes") or 0),
                "text": cm.get("text", "").replace("|", "/").strip(),
            })
    if not items:
        return None
    items.sort(key=lambda x: (-x["likes"], x["creator"]))
    lines = [
        "---",
        f'title: "Ngôn ngữ & nỗi đau khán giả thật ({date})"',
        f"date: {date}",
        f"id: trends-{date}-audience-language",
        "type: trend-digest",
        "status: active",
        f"updated: {date}",
        "tags: [trends, audience-language, comments, radar]",
        'source: "pipeline/scripts/radar-fetch.py (yt-dlp top comments, ẩn danh)"',
        "---",
        f"# Ngôn ngữ & nỗi đau khán giả thật — {date}",
        "",
        "Trích từ Top Comments của các video radar (ẩn danh tài khoản người bình luận). Dùng để khai thác câu cửa miệng và nỗi đau thật cho Gate 0 & Gate 0.5 Hook Arena.",
        "",
        "| kênh | role | like | câu comment / nỗi đau khán giả | video nguồn |",
        "|---|---|---:|---|---|",
    ]
    for it in items[:50]:
        lines.append(f"| @{it['creator']} | `{it['role']}` | {it['likes']} | «{it['text']}» | {it['url']} |")
    return "\n".join(lines) + "\n"


def run_fetch(date, cfg_path=RADAR_CFG, limit=None, only=None, roles=None, langs=None, root=TRENDS,
              fetcher=fetch_channel_entries, comment_fetcher=None, with_comments=False,
              enqueue=True, dry_run=False, workers=DEFAULT_WORKERS, ttl_hours=None,
              force=False, include_seen=False, use_ego=False):
    t0 = time.monotonic()
    cfg = load_config(cfg_path)
    lim = int(limit or cfg.get("recent_limit", 10))
    channels = cfg.get("channels") or []
    if only:
        want = {x.lstrip("@").lower() for x in only}
        channels = [c for c in channels if c.get("handle", "").lstrip("@").lower() in want]
    else:
        channels = [c for c in channels if c.get("enabled", True) and (c.get("url") or c.get("handle"))]
    if roles:
        want_r = {r.strip() for r in roles if r.strip()}
        channels = [c for c in channels if (c.get("role") or "direct_niche") in want_r]
    if langs:
        want_l = {l.strip().lower() for l in langs if l.strip()}
        channels = [c for c in channels if (c.get("lang") or "vi").lower() in want_l]

    # Default TTL cache enabled for real runs, disabled when a mock fetcher is injected in unit tests
    if ttl_hours is None:
        ttl_hours = 0.0 if (fetcher is not fetch_channel_entries or force) else DEFAULT_TTL_HOURS
    cache_path = Path(root) / ".cache/radar-cache.json"
    cache_doc = _load_json(cache_path, {"channels": {}}) if (ttl_hours > 0 and not force) else {"channels": {}}
    now_ts = time.time()

    def _fetch_one(idx, ch):
        handle = ch.get("handle") or ""
        url = ch.get("url") or f"https://www.tiktok.com/@{handle.lstrip('@')}"
        role = ch.get("role") if ch.get("role") in VALID_ROLES else "direct_niche"
        ckey = f"{ch.get('platform', 'tiktok')}:{handle.lower()}:{lim}"
        cached = (cache_doc.get("channels") or {}).get(ckey)
        if ttl_hours > 0 and not force and cached:
            age_h = (now_ts - float(cached.get("fetched_at") or 0)) / 3600.0
            if age_h <= ttl_hours and cached.get("entries") is not None:
                # Optional YouTube Atom RSS 304 fast-check if channel_id is cached
                cid = cached.get("channel_id") or ch.get("channel_id")
                rss_ok = True
                if ch.get("platform") == "youtube" and cid and age_h > 0.5:
                    st_rss, rss_ids, new_etag = fetch_youtube_rss(cid, etag=cached.get("etag"))
                    if st_rss == "ok" and rss_ids:
                        cached_ids = {str(e.get("id") or "") for e in cached["entries"]}
                        if any(rid not in cached_ids for rid in rss_ids[:3]):
                            rss_ok = False
                    if new_etag:
                        cached["etag"] = new_etag
                if rss_ok:
                    clips, med = normalize_channel(ch, cached["entries"])
                    return idx, clips, {
                        "handle": handle, "role": role, "platform": ch.get("platform", "tiktok"),
                        "url": url, "fetched": len(clips), "median_views": round(med, 1) if med else None,
                        "error": "", "cache_hit": True,
                    }, None
        try:
            entries, err = fetcher(url, lim)
        except Exception as e:
            entries, err = [], f"{type(e).__name__}: {e}"[:200]
        clips, med = normalize_channel(ch, entries)
        cid_found = next((e.get("channel_id") for e in entries if e.get("channel_id")), ch.get("channel_id"))
        new_cache_val = {"fetched_at": now_ts, "channel_id": cid_found, "entries": entries} if entries else None
        return idx, clips, {
            "handle": handle, "role": role, "platform": ch.get("platform", "tiktok"),
            "url": url, "fetched": len(clips), "median_views": round(med, 1) if med else None,
            "error": err, "cache_hit": False,
        }, (ckey, new_cache_val)

    results = []
    max_w = max(1, min(int(workers or DEFAULT_WORKERS), len(channels) or 1))
    if max_w == 1:
        for i, ch in enumerate(channels):
            results.append(_fetch_one(i, ch))
    else:
        with ThreadPoolExecutor(max_workers=max_w) as ex:
            futs = [ex.submit(_fetch_one, i, ch) for i, ch in enumerate(channels)]
            for fut in as_completed(futs):
                results.append(fut.result())
    results.sort(key=lambda x: x[0])

    all_clips, statuses = [], []
    cache_dirty = False
    for _, clips, st, c_upd in results:
        all_clips.extend(clips)
        statuses.append(st)
        if c_upd and c_upd[1] is not None:
            cache_doc.setdefault("channels", {})[c_upd[0]] = c_upd[1]
            cache_dirty = True
    if cache_dirty and not dry_run and fetcher is fetch_channel_entries:
        _save_json(cache_path, cache_doc)

    raw_rows = build_radar_rows(all_clips, cfg, date, root=root)
    rows, skipped_seen = apply_seen_dedupe(raw_rows, root=root, include_seen=include_seen, save=not dry_run)

    if with_comments and not dry_run:
        cf = comment_fetcher or fetch_video_comments
        ego_mod = None
        if use_ego:
            try:
                import ego_crawl as _ego
                if _ego.available():
                    ego_mod = _ego
            except Exception:
                ego_mod = None
        by_url = {c.get("url"): c for c in all_clips if c.get("url")}
        for r in rows[:10]:
            if r.get("url") and not r.get("top_comments"):
                tcs = cf(r["url"])
                if not tcs and ego_mod and r.get("platform") == "tiktok":
                    tcs = ego_mod.crawl_tiktok_comments(r["url"], max_comments=10)
                if tcs:
                    r["top_comments"] = tcs
                    if r["url"] in by_url:
                        by_url[r["url"]]["top_comments"] = tcs

    day_dir = Path(root) / date
    raw_path = day_dir / "radar-raw.json"
    out_path = day_dir / "radar.json"
    aud_path = day_dir / "audience-language.md"
    aud_md = render_audience_language(date, all_clips)
    elapsed_s = round(time.monotonic() - t0, 2)

    if not dry_run:
        day_dir.mkdir(parents=True, exist_ok=True)
        raw_doc = {
            "date": date,
            "measured_at": dt.datetime.now().isoformat(timespec="seconds"),
            "collector": "radar-fetch.py (yt-dlp parallel + rss + ttl-cache)",
            "elapsed_s": elapsed_s,
            "channels": statuses,
            "clips": all_clips,
        }
        raw_path.write_text(json.dumps(raw_doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        out_doc = {
            "date": date,
            "config": str(Path(cfg_path).relative_to(ROOT)) if ROOT in Path(cfg_path).resolve().parents else str(cfg_path),
            "collector": "radar-fetch.py (yt-dlp parallel + rss + ttl-cache)",
            "elapsed_s": elapsed_s,
            "skipped_seen": len(skipped_seen),
            "channels": statuses,
            "rows": rows,
        }
        out_path.write_text(json.dumps(out_doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        if aud_md:
            aud_path.write_text(aud_md, encoding="utf-8")
        if enqueue:
            ts_script = Path(__file__).resolve().parent / "trend-streams.py"
            subprocess.run([sys.executable, str(ts_script), "radar", "--date", date, "--enqueue"], check=False)

    return {
        "statuses": statuses,
        "clips": all_clips,
        "rows": rows,
        "skipped_seen": skipped_seen,
        "elapsed_s": elapsed_s,
        "raw_path": raw_path,
        "out_path": out_path,
        "audience_language_path": aud_path if aud_md else None,
    }


def main():
    a = sys.argv[1:]
    def opt(n, d=None):
        return a[a.index(n) + 1] if n in a else d
    if "-h" in a or "--help" in a:
        print(__doc__)
        return 0
    date = opt("--date", dt.date.today().isoformat())
    cfg_path = Path(opt("--config", str(RADAR_CFG)))
    limit = int(opt("--limit")) if opt("--limit") else None
    only = opt("--only").split(",") if opt("--only") else None
    roles = opt("--role").split(",") if opt("--role") else None
    langs = opt("--lang").split(",") if opt("--lang") else None
    workers = int(opt("--workers", str(DEFAULT_WORKERS)))
    ttl_hours = float(opt("--ttl-hours")) if opt("--ttl-hours") is not None else None
    force = "--force" in a
    include_seen = "--include-seen" in a
    use_ego = "--use-ego" in a
    with_comments = "--with-comments" in a
    dry_run = "--dry-run" in a
    enqueue = "--no-enqueue" not in a

    res = run_fetch(date, cfg_path=cfg_path, limit=limit, only=only, roles=roles, langs=langs,
                    with_comments=with_comments, enqueue=enqueue, dry_run=dry_run,
                    workers=workers, ttl_hours=ttl_hours, force=force,
                    include_seen=include_seen, use_ego=use_ego)
    for st in res["statuses"]:
        c_tag = " [CACHE]" if st.get("cache_hit") else ""
        tag = f"ok ({st['fetched']} clips, median={st['median_views']}){c_tag}" if st["fetched"] else f"empty/err: {st['error']}"
        print(f"  @{st['handle']:20} [{st['role']:19}] {tag}")
    extra = f" · audience-language → {res['audience_language_path']}" if res["audience_language_path"] else ""
    skip_s = f" · {len(res['skipped_seen'])} seen skipped" if res.get("skipped_seen") else ""
    print(f"radar-fetch: {len(res['clips'])} clips, {len(res['rows'])} new/spike outliers{skip_s} in {res['elapsed_s']}s → {res['out_path']}{extra}"
          + (" (dry-run)" if dry_run else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
