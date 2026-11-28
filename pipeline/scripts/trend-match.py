#!/usr/bin/env python3
"""Reverse Hot-Trend Matcher (Content Engine v2.0, F2, DL-082).

Instead of picking a rigid sequential lesson from content/theme-map.md and forcing a stale trend onto it,
this script scans fresh trends (24–72h) from research/trends/ and matches them against unproduced lessons in
content/theme-map.md, content/idea-bank.md, and research/explainers/ using Emotional Bridge Matching.

Features:
  1. Freshness Gate (< 72h default, configurable via --max-age-hours).
  2. Agile Slot Swap: enforces theme-map.md Rule 4 (never > 2 consecutive LIGHT or DARK clips).
  3. Pain-Wave Fallback: when no fresh trend matches naturally, automatically falls back to
     resources/vn-spoken/audience-pain-bank.md (clean DL-069 exception, never fake trend bridges).

CLI:
  python3 pipeline/scripts/trend-match.py [--date YYYY-MM-DD] [--trend "<text>"]
      [--max-age-hours 72] [--recent-themes DARK,DARK] [--top 3] [--json]
"""
import datetime as dt
import json
import re
import sys
import unicodedata
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65

ROOT = P.ROOT
TRENDS_DIR = ROOT / "research/trends"
THEME_MAP = ROOT / "content/theme-map.md"
PAIN_BANK = ROOT / "resources/vn-spoken/audience-pain-bank.md"
EXPLAINERS_DIR = ROOT / "research/explainers"
IDEA_BANK = ROOT / "content/idea-bank.md"

DEFAULT_MAX_AGE_HOURS = 72.0
MIN_BRIDGE_SCORE = 0.12

STOP = set(
    "và của là có cho một những các được với không thì mà này đó để khi người bạn mình rồi lại cũng như nào gì vì nên "
    "cái việc đã sẽ đang hay hơn rất cả mới nữa luôn nha nè á hông vào ra lên về tới tại theo từ trong ngoài".split()
)

# Bilingual EN + VN Emotional & everyday bridge clusters: maps global English & VN trending metaphors/topics to core habit/psychology themes
BRIDGE_CLUSTERS = {
    "patience_habit": {
        "chua no", "bong hoa", "kien nhan", "21 ngay", "thoi quen", "bo cuoc", "nan", "cham", "mai mai", "doi", "ket qua",
        "21 days", "habit", "habits", "atomic habits", "consistency", "give up", "quit", "plateau", "compound", "routine",
    },
    "procrastination": {
        "tri hoan", "luoi", "mai hoc", "mai lam", "de sau", "deadline", "nuoc den chan", "so", "kho chiu", "ngai",
        "procrastinat", "lazy", "laziness", "avoidance", "discomfort", "perfectionism", "tomorrow", "put off", "delay",
    },
    "focus_distraction": {
        "dien thoai", "luot", "tiktok", "shorts", "reels", "mat tap trung", "thong bao", "da nhiem", "hop", "tin nhan", "ngat quang",
        "phone", "scroll", "doomscroll", "dopamine", "distract", "multitask", "attention", "notification", "focus", "deep work", "screen time",
    },
    "energy_sleep": {
        "ngu", "thuc khuya", "ca phe", "met", "buon ngu", "cuoi tuan", "thu hai", "kiet suc", "burnout", "ngoi nhieu", "di bo",
        "sleep", "caffeine", "coffee", "nap", "fatigue", "exhausted", "tired", "sedentary", "sitting", "walk", "circadian", "weekend",
    },
    "mindset_stress": {
        "overthinking", "so sanh", "ap luc", "lo au", "buon", "y chi", "can pin", "tu trach", "nghi nhieu", "chua lanh",
        "overthink", "compar", "anxiety", "willpower", "ego depletion", "stress", "breath", "sigh", "spotlight effect", "insecurity", "mood",
    },
    "learning_memory": {
        "hoc", "thi", "nho", "quen", "doc lai", "tu kiem", "hoc don", "mot dem", "on thi", "sach",
        "memory", "forget", "reread", "cram", "cramming", "retrieval", "active recall", "study", "exam", "learn", "remember",
    },
    "big_task_sunk": {
        "viec to", "chia nho", "ngop", "side project", "chi phi chim", "bo do", "ke hoach", "don phong",
        "overwhelm", "chunk", "break down", "sunk cost", "side project", "big task", "planning", "clean room",
    },
    "money_tech": {
        "gia han", "tien", "api", "bao mat", "phim tat", "ai", "lap trinh", "code",
        "subscription", "auto renew", "api key", "security", "shortcut", "shortcuts", "coding", "developer", "ai agent",
    },
}


def detect_lang(text, explicit_lang=None):
    """Detect whether a trend item is English (needs EN→VN cultural localization) or Vietnamese."""
    if explicit_lang in ("en", "vi"):
        return explicit_lang
    s = text or ""
    if re.search(r"[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]", s, re.I):
        return "vi"
    return "en"


def fold(s):
    s = unicodedata.normalize("NFD", (s or "").lower())
    return unicodedata.normalize("NFC", "".join(c for c in s if unicodedata.category(c) != "Mn")).replace("đ", "d")


def tokens(s):
    stop_f = {fold(x) for x in STOP}
    return {w for w in re.findall(r"[a-z0-9]+", fold(s)) if len(w) > 1 and w not in stop_f}


def cluster_tags(s):
    f = fold(s)
    hit = set()
    for name, kws in BRIDGE_CLUSTERS.items():
        if any(k in f for k in kws):
            hit.add(name)
    return hit


def bridge_score(trend_text, lesson_text):
    """Compute 0..1 emotional/semantic bridge score between a trend and a lesson."""
    ta, tb = tokens(trend_text), tokens(lesson_text)
    lex = len(ta & tb) / max(min(len(ta), len(tb)), 1) if ta and tb else 0.0
    ca, cb = cluster_tags(trend_text), cluster_tags(lesson_text)
    clu = len(ca & cb) / max(len(ca | cb), 1) if (ca or cb) else 0.0
    return round(0.45 * min(1.0, lex) + 0.55 * clu, 3), sorted(ca & cb)


def parse_theme_map(path=None):
    """Parse content/theme-map.md schedule table into structured lesson dicts."""
    p = Path(path or THEME_MAP)
    if not p.exists():
        return []
    rows = []
    in_table = False
    for ln in p.read_text(encoding="utf-8").splitlines():
        if ln.startswith("## Thứ tự đăng"):
            in_table = True
            continue
        if in_table and ln.startswith("## "):
            break
        if not in_table or not ln.startswith("|") or re.match(r"^\|[-\s|:]+\|$", ln):
            continue
        c = [x.strip() for x in ln.strip("|").split("|")]
        if len(c) < 8 or not re.fullmatch(r"\d+", c[0]):
            continue
        theme = "LIGHT" if "LIGHT" in c[7].upper() else ("DARK" if "DARK" in c[7].upper() else "")
        rows.append({
            "slot": int(c[0]),
            "plan_clip": c[1],
            "week": int(c[2]) if c[2].isdigit() else 0,
            "book_ref": c[3],
            "pillar": c[4],
            "topic": c[5],
            "tone_reason": c[6],
            "theme": theme,
        })
    return rows


def produced_clip_slots(root=None):
    """Detect clip numbers already present in content/archive/ and content/clips/."""
    base = Path(root or ROOT)
    done = set()
    for sub in ("content/archive", "content/clips"):
        d = base / sub
        if not d.exists():
            continue
        for p in d.iterdir():
            m = re.match(r"clip-(\d+)", p.name)
            if m:
                done.add(int(m.group(1)))
    return done


def required_theme(recent_themes):
    """Enforce theme-map.md Rule 4: if last 2 clips have the same theme, return the required opposite theme; else None."""
    clean = [t.strip().upper() for t in (recent_themes or []) if t and t.strip().upper() in ("LIGHT", "DARK")]
    if len(clean) >= 2 and clean[-1] == clean[-2]:
        return "LIGHT" if clean[-1] == "DARK" else "DARK"
    return None


def parse_pain_bank(path=None):
    """Parse resources/vn-spoken/audience-pain-bank.md rows for Pain-Wave Fallback."""
    p = Path(path or PAIN_BANK)
    if not p.exists():
        return []
    out = []
    for ln in p.read_text(encoding="utf-8").splitlines():
        if not ln.startswith("|") or re.match(r"^\|[-\s|:]+\|$", ln):
            continue
        c = [x.strip() for x in ln.strip("|").split("|")]
        if len(c) >= 5 and re.match(r"20\d\d-\d\d-\d\d", c[0]):
            out.append({
                "date": c[0],
                "source": c[1],
                "topics": c[2],
                "pain": c[3].strip("«»\"' "),
                "note": c[4],
            })
    return out


def _parse_date(s):
    if not s:
        return None
    m = re.search(r"(\d{4}-\d{2}-\d{2})", str(s))
    if not m:
        return None
    try:
        return dt.date.fromisoformat(m.group(1))
    except ValueError:
        return None


def load_fresh_trends(ref_date=None, max_age_hours=DEFAULT_MAX_AGE_HOURS, trends_dir=None):
    """Load fresh trend items (<= max_age_hours old) from research/trends/YYYY-MM-DD/radar.json & digest.md."""
    base = Path(trends_dir or TRENDS_DIR)
    ref = _parse_date(ref_date) or dt.date.today()
    max_days = max(1, int((max_age_hours + 23.99) // 24))
    items = []
    if not base.exists():
        return items
    for day_dir in sorted(base.iterdir(), reverse=True):
        if not day_dir.is_dir():
            continue
        d = _parse_date(day_dir.name)
        if not d:
            continue
        age_days = (ref - d).days
        if age_days < 0 or age_days > max_days:
            continue
        age_hours = round(age_days * 24.0, 1)
        radar_p = day_dir / "radar.json"
        if radar_p.exists():
            try:
                doc = json.loads(radar_p.read_text(encoding="utf-8"))
                for r in doc.get("rows") or []:
                    if r.get("role") == "anti_pattern":
                        continue
                    text = " ".join(filter(None, [
                        r.get("angle") or "",
                        " ".join(r.get("topic_tags") or []),
                        " ".join(c.get("text", "") for c in (r.get("top_comments") or [])[:2]),
                    ])).strip()
                    if not text:
                        text = f"@{r.get('creator', '')} outlier {r.get('id', '')}"
                    lang = detect_lang(text, r.get("lang"))
                    items.append({
                        "title": f"Radar @{r.get('creator', '?')} [{lang.upper()}]: {text[:90]}",
                        "text": text,
                        "lang": lang,
                        "role": r.get("role", "direct_niche"),
                        "source": str(radar_p.relative_to(ROOT)) if ROOT in radar_p.parents else str(radar_p),
                        "date": d.isoformat(),
                        "age_hours": age_hours,
                        "kind": "radar_outlier",
                    })
            except (json.JSONDecodeError, OSError):
                pass
        digest_p = day_dir / "digest.md"
        if digest_p.exists():
            for ln in digest_p.read_text(encoding="utf-8", errors="replace").splitlines():
                if ln.startswith(("- ", "* ")) and len(ln) > 20:
                    clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", ln[2:]).strip()
                    items.append({
                        "title": clean[:100],
                        "text": clean,
                        "source": str(digest_p.relative_to(ROOT)) if ROOT in digest_p.parents else str(digest_p),
                        "date": d.isoformat(),
                        "age_hours": age_hours,
                        "kind": "trend_digest",
                    })
    return items


def match_trends(
    ref_date=None,
    explicit_trends=None,
    max_age_hours=DEFAULT_MAX_AGE_HOURS,
    recent_themes=None,
    top_n=3,
    trends_dir=None,
    theme_map_path=None,
    pain_bank_path=None,
    root=None,
):
    """Match fresh trends against unproduced lessons with Agile Slot Swap + Pain-Wave Fallback."""
    lessons = parse_theme_map(theme_map_path)
    done = produced_clip_slots(root)
    unproduced = [l for l in lessons if l["slot"] not in done and l["topic"] and not l["topic"].startswith("(trống")]

    if recent_themes is None:
        # Infer last 2 produced themes from theme-map
        prod_rows = [l for l in lessons if l["slot"] in done]
        recent_themes = [r["theme"] for r in prod_rows[-2:]]
    req_theme = required_theme(recent_themes)

    if explicit_trends:
        trends = [
            {
                "title": t,
                "text": t,
                "lang": detect_lang(t),
                "source": "cli:--trend",
                "date": str(ref_date or dt.date.today()),
                "age_hours": 0.0,
                "kind": "explicit",
            }
            for t in explicit_trends if t and t.strip()
        ]
    else:
        trends = load_fresh_trends(ref_date=ref_date, max_age_hours=max_age_hours, trends_dir=trends_dir)

    candidates = []
    for tr in trends:
        tr_lang = detect_lang(tr.get("text", ""), tr.get("lang"))
        for ls in unproduced:
            if req_theme and ls["theme"] != req_theme:
                continue
            sc, clusters = bridge_score(tr["text"], f"{ls['pillar']} {ls['topic']} {ls['tone_reason']}")
            if sc < MIN_BRIDGE_SCORE:
                continue
            fresh_bonus = max(0.0, 0.15 * (1.0 - min(tr["age_hours"], max_age_hours) / max(max_age_hours, 1.0)))
            # Small quality bonus for global_niche_source English hits (3–6 months ahead of TikTok VN)
            global_bonus = 0.05 if tr.get("role") == "global_niche_source" else 0.0
            total = round(sc + fresh_bonus + global_bonus, 3)
            candidates.append({
                "score": total,
                "bridge_score": sc,
                "clusters": clusters,
                "trend": tr,
                "lang": tr_lang,
                "needs_localization": tr_lang == "en",
                "lesson": ls,
                "agile_swap": ls["slot"] != (unproduced[0]["slot"] if unproduced else ls["slot"]),
                "theme_rule_ok": True,
            })

    candidates.sort(key=lambda x: (-x["score"], x["lesson"]["slot"]))
    # Deduplicate by lesson slot so Top 3 offer distinct clip choices
    picked, seen_slots = [], set()
    for c in candidates:
        sl = c["lesson"]["slot"]
        if sl in seen_slots:
            continue
        seen_slots.add(sl)
        picked.append(c)
        if len(picked) >= top_n:
            break

    if picked:
        return {
            "mode": "hot_trend_match",
            "required_theme": req_theme,
            "recent_themes": list(recent_themes or []),
            "fresh_trends_count": len(trends),
            "matches": picked,
            "fallback_pains": [],
        }

    # Pain-Wave Fallback (DL-069 clean exception — no forced fake trend)
    pains = parse_pain_bank(pain_bank_path)
    fb_matches = []
    for p in pains:
        for ls in unproduced:
            if req_theme and ls["theme"] != req_theme:
                continue
            sc, clusters = bridge_score(f"{p['topics']} {p['pain']}", f"{ls['pillar']} {ls['topic']} {ls['tone_reason']}")
            fb_matches.append({
                "score": sc,
                "clusters": clusters,
                "pain": p,
                "lesson": ls,
                "agile_swap": ls["slot"] != (unproduced[0]["slot"] if unproduced else ls["slot"]),
                "theme_rule_ok": True,
            })
    fb_matches.sort(key=lambda x: (-x["score"], x["lesson"]["slot"]))
    fb_picked, seen_slots = [], set()
    for m in fb_matches:
        sl = m["lesson"]["slot"]
        if sl in seen_slots:
            continue
        seen_slots.add(sl)
        fb_picked.append(m)
        if len(fb_picked) >= top_n:
            break

    return {
        "mode": "pain_wave_fallback",
        "required_theme": req_theme,
        "recent_themes": list(recent_themes or []),
        "fresh_trends_count": len(trends),
        "matches": [],
        "fallback_pains": fb_picked,
    }


def format_report(res):
    lines = ["## Reverse Hot-Trend Match (`trend-match.py`, F2)", ""]
    req = res["required_theme"] or "LIGHT hoặc DARK đều hợp lệ"
    lines.append(f"- **Chế độ:** `{res['mode']}` · Trend tươi (< 72h): **{res['fresh_trends_count']}** · Ràng buộc theme kế tiếp (Rule 4 `LIGHT/DARK ≤ 2`): **{req}**")
    lines.append("")
    if res["mode"] == "hot_trend_match":
        lines.append("| # | Điểm | Slot (Theme) | Bài học khớp tự nhiên | Trend nóng (< 72h) | Cầu cảm xúc | Việt hóa / Swap |")
        lines.append("|---|---:|---|---|---|---|---|")
        for i, m in enumerate(res["matches"], 1):
            ls, tr = m["lesson"], m["trend"]
            clu = ", ".join(m["clusters"]) or "lexical"
            loc = "EN→VN Localize" if m.get("needs_localization") else "VN gốc"
            swap = "Đổi slot" if m["agile_swap"] else "Đúng thứ tự"
            lines.append(f"| {i} | {m['score']:.2f} | #{ls['slot']} ({ls['theme']}) | {ls['book_ref']} — {ls['topic']} | {tr['title']} ({tr['age_hours']:.0f}h) | {clu} | {loc} · {swap} |")
    else:
        lines.append("> Không có trend tươi (< 72h) nào khớp tự nhiên với trục kênh → kích hoạt **Pain-Wave Fallback (ngoại lệ sạch `DL-069`, không ép meme gượng)** từ `resources/vn-spoken/audience-pain-bank.md`.")
        lines.append("")
        lines.append("| # | Điểm | Slot (Theme) | Bài học | Nỗi đau khán giả thật (Pain Bank) | Cầu cảm xúc |")
        lines.append("|---|---:|---|---|---|---|")
        for i, m in enumerate(res["fallback_pains"], 1):
            ls, p = m["lesson"], m["pain"]
            clu = ", ".join(m["clusters"]) or "lexical"
            lines.append(f"| {i} | {m['score']:.2f} | #{ls['slot']} ({ls['theme']}) | {ls['book_ref']} — {ls['topic']} | «{p['pain']}» | {clu} |")
    return "\n".join(lines) + "\n"


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)
    if "-h" in a or "--help" in a:
        print(__doc__)
        return 0
    def opt(n, d=None):
        return a[a.index(n) + 1] if n in a else d

    ref_date = opt("--date", dt.date.today().isoformat())
    max_age = float(opt("--max-age-hours", str(DEFAULT_MAX_AGE_HOURS)))
    top_n = int(opt("--top", "3"))
    recent = opt("--recent-themes").split(",") if opt("--recent-themes") else None
    explicit = [a[i + 1] for i, x in enumerate(a) if x == "--trend" and i + 1 < len(a)] or None

    res = match_trends(
        ref_date=ref_date,
        explicit_trends=explicit,
        max_age_hours=max_age,
        recent_themes=recent,
        top_n=top_n,
    )
    if "--json" in a:
        print(json.dumps(res, ensure_ascii=False, indent=1))
    else:
        print(format_report(res))
    return 0


if __name__ == "__main__":
    sys.exit(main())
