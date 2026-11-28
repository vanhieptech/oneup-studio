#!/usr/bin/env python3
"""Auto-Channel Discovery (Content Engine v2.1, DL-085, Zero-Token).

Scans collected trend snapshots (`research/trends/*/collect.json` & `radar-raw.json`) and optional
live YouTube keyword search (`--live`) for high-performing creators NOT yet tracked in
`pipeline/trends/radar.yaml`. Ranks candidates and writes `research/trends/suggested-channels.md`
with 1-line `radar.yaml` JSON snippets ready for Hiệp to approve.

CLI:
  python3 pipeline/scripts/channel-discover.py [--days 14] [--min-views 50000] [--live] [--top 10] [--json]
"""
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65

ROOT = P.ROOT
TRENDS_DIR = ROOT / "research/trends"
RADAR_CFG = ROOT / "pipeline/trends/radar.yaml"
OUT_MD = TRENDS_DIR / "suggested-channels.md"


def load_tracked_handles(cfg_path=RADAR_CFG):
    lines = [l for l in Path(cfg_path).read_text(encoding="utf-8").splitlines() if not l.lstrip().startswith("#")]
    cfg = json.loads("\n".join(lines))
    handles = {str(c.get("handle") or "").lstrip("@").lower() for c in cfg.get("channels") or []}
    return handles, cfg


def _extract_handle(url, fallback=""):
    m = re.search(r"(?:tiktok\.com|youtube\.com|x\.com|threads\.net)/@?([A-Za-z0-9._-]+)", url or "", re.I)
    if m and m.group(1).lower() not in ("watch", "results", "shorts", "search", "explore", "video"):
        return m.group(1).lstrip("@")
    return (fallback or "").lstrip("@").strip()


def _detect_lang(text):
    if re.search(r"[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]", text or "", re.I):
        return "vi"
    return "en"


def live_youtube_discover(keywords, per_kw=6, timeout=45):
    """Run zero-token yt-dlp flat-playlist search on English/VN keywords to discover new creators."""
    ytdlp = shutil.which("yt-dlp") or "/opt/homebrew/bin/yt-dlp"
    cmd_base = [ytdlp] if Path(ytdlp).exists() else [sys.executable, "-m", "yt_dlp"]
    found = []
    for kw in keywords[:4]:
        try:
            r = subprocess.run(
                [*cmd_base, "--flat-playlist", "-J", "--no-warnings", f"ytsearch{per_kw}:{kw}"],
                capture_output=True, text=True, timeout=timeout,
            )
            if r.returncode != 0 or not r.stdout.strip():
                continue
            doc = json.loads(r.stdout)
            for e in doc.get("entries") or []:
                uid = (e.get("uploader_id") or "").lstrip("@").strip()
                cname = (e.get("channel") or e.get("uploader") or "").strip()
                curl = (e.get("channel_url") or "").rstrip("/")
                handle = uid or re.sub(r"\s+", "", cname) or curl.rsplit("/", 1)[-1].lstrip("@")
                found.append({
                    "handle": handle,
                    "channel_name": cname or handle,
                    "platform": "youtube",
                    "url": f"https://www.youtube.com/@{uid}/shorts" if uid else (curl or f"https://www.youtube.com/@{handle}/shorts"),
                    "title": e.get("title") or "",
                    "views": int(e.get("view_count") or 0),
                    "lang": _detect_lang(e.get("title") or kw),
                    "keyword": kw,
                })
        except Exception:
            continue
    return found


def discover_channels(
    trends_dir=TRENDS_DIR,
    cfg_path=RADAR_CFG,
    days=14,
    min_views=50000,
    live=False,
    top_n=10,
    extra_items=None,
):
    tracked, cfg = load_tracked_handles(cfg_path)
    base = Path(trends_dir)
    cutoff = dt.date.today() - dt.timedelta(days=days)
    raw_items = list(extra_items or [])

    if base.exists():
        for day_dir in sorted(base.iterdir(), reverse=True):
            if not day_dir.is_dir() or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", day_dir.name):
                continue
            try:
                d = dt.date.fromisoformat(day_dir.name)
            except ValueError:
                continue
            if d < cutoff:
                continue
            col_p = day_dir / "collect.json"
            if col_p.exists():
                try:
                    doc = json.loads(col_p.read_text(encoding="utf-8"))
                    for it in doc.get("items") or []:
                        url = it.get("url") or ""
                        if not any(dom in url for dom in ("youtube.com", "youtu.be", "tiktok.com")):
                            continue
                        handle = _extract_handle(url, it.get("creator") or "")
                        views = int((it.get("signals") or {}).get("metrics", {}).get("views") or 0)
                        plat = "tiktok" if "tiktok.com" in url else "youtube"
                        raw_items.append({
                            "handle": handle,
                            "platform": plat,
                            "url": f"https://www.tiktok.com/@{handle}" if plat == "tiktok" else f"https://www.youtube.com/@{handle}/shorts",
                            "title": it.get("text") or it.get("title") or "",
                            "views": views,
                            "lang": it.get("lang") or _detect_lang(it.get("text") or ""),
                        })
                except (json.JSONDecodeError, OSError):
                    pass

    if live:
        kws = [k for k in (cfg.get("keywords") or []) if _detect_lang(k) == "en"] or (cfg.get("keywords") or [])
        raw_items.extend(live_youtube_discover(kws))

    by_ch = {}
    for it in raw_items:
        h = (it.get("handle") or "").lstrip("@").strip()
        if not h or h.lower() in tracked or len(h) < 2:
            continue
        k = h.lower()
        st = by_ch.setdefault(k, {
            "handle": h,
            "platform": it.get("platform", "youtube"),
            "lang": it.get("lang", "en"),
            "url": it.get("url") or f"https://www.youtube.com/@{h}/shorts",
            "hits": 0,
            "max_views": 0,
            "total_views": 0,
            "samples": [],
        })
        v = int(it.get("views") or 0)
        st["hits"] += 1
        st["max_views"] = max(st["max_views"], v)
        st["total_views"] += v
        if it.get("title") and len(st["samples"]) < 2:
            st["samples"].append(it["title"][:90])

    candidates = []
    for st in by_ch.values():
        if st["max_views"] < min_views and st["hits"] < 2:
            continue
        role = "global_niche_source" if st["lang"] == "en" else "direct_niche"
        score = round(st["hits"] * 25.0 + min(100.0, st["max_views"] / 10000.0), 1)
        snippet = {
            "handle": st["handle"],
            "platform": st["platform"],
            "lang": st["lang"],
            "role": role,
            "format_compatibility": "story_metaphor",
            "url": st["url"],
            "followers": 0,
            "niche": ["productivity", "tu-duy"],
            "niche_verified": True,
        }
        candidates.append({**st, "suggested_role": role, "score": score, "radar_snippet": snippet})

    candidates.sort(key=lambda x: (-x["score"], -x["max_views"], x["handle"]))
    return candidates[:top_n]


def render_markdown(candidates, date_str=None):
    today = date_str or dt.date.today().isoformat()
    lines = [
        "---",
        f'title: "Đề xuất kênh mới nên theo dõi ({today})"',
        f"date: {today}",
        "id: trends-suggested-channels",
        "type: trend-digest",
        "status: active",
        f"updated: {today}",
        "tags: [trends, discovery, radar, global-channels]",
        'source: "pipeline/scripts/channel-discover.py (zero-token auto-discovery)"',
        "---",
        f"# Đề xuất Kênh Mới Nên Theo Dõi ({today})",
        "",
        "Các kênh ngoài `pipeline/trends/radar.yaml` có video đạt lượt xem cao hoặc lặp lại nhiều lần trong kết quả quét gần đây. Hiệp duyệt dòng nào thì dán snippet JSON vào `radar.yaml`.",
        "",
    ]
    if not candidates:
        lines.append("- Chưa có kênh mới nào vượt ngưỡng đề xuất trong cửa sổ quét hiện tại.")
        return "\n".join(lines) + "\n"
    lines += [
        "| Kênh | Nền tảng | Ngôn ngữ | Vai trò gợi ý | Hits | Max Views | Video mẫu |",
        "|---|---|---|---|---:|---:|---|",
    ]
    for c in candidates:
        samp = "; ".join(c["samples"]).replace("|", "/")
        lines.append(f"| `@{c['handle']}` | {c['platform']} | `{c['lang']}` | `{c['suggested_role']}` | {c['hits']} | {c['max_views']:,} | {samp} |")
    lines += ["", "## Snippet sẵn dán vào `pipeline/trends/radar.yaml`", "", "```json"]
    for c in candidates[:5]:
        lines.append(json.dumps(c["radar_snippet"], ensure_ascii=False) + ",")
    lines.append("```")
    return "\n".join(lines) + "\n"


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)
    if "-h" in a or "--help" in a:
        print(__doc__)
        return 0
    def opt(n, d=None):
        return a[a.index(n) + 1] if n in a else d

    cands = discover_channels(
        days=int(opt("--days", "14")),
        min_views=int(opt("--min-views", "50000")),
        live="--live" in a,
        top_n=int(opt("--top", "10")),
    )
    if "--json" in a:
        print(json.dumps(cands, ensure_ascii=False, indent=1))
        return 0
    md = render_markdown(cands)
    out = Path(opt("--out", str(OUT_MD)))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")
    print(f"channel-discover: {len(cands)} kênh đề xuất → {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
