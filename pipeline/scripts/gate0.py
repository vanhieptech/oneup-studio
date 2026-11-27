#!/usr/bin/env python3
"""Gate 0 brief: load the 4 pieces before draft v1 (make-video §2.0 step 0, channels/vanhiep-tech/AGENTS.md).

  gate0.py --idea "<words from the idea>" [--channel hi|vht] [--arc ARC-NNN] [--tone story_warm|tech_sharp]
           [--memo media/voice-memos/x.txt] [--topic <research/explainers slug>]
           [--clip content/clips/clip-NN-*/] [--length 65] [--extended] [--out <draft.md>]

Pieces (printed as one Markdown block; --out writes/replaces the block between GATE0-BRIEF markers at the top of the draft):
  1. Idea: best-matching rows of content/idea-bank.md (main table + «Từ teardown (ARC)» ideas) + fact package
     (research/explainers/<topic>.md, best match by words when --topic is omitted).
  2. Story arc ARC-NNN (research/blueprints/index.json): skeleton + beat timing planned for the channel —
     @hi.oneup 60–180 s target (strict < 300 s, L-099; do not stretch a finished story) with an Open Loop + Micro-Payoff every 35–45 s;
     @vanhiep.tech 45–90 s with a layer cut every 3–5 s.
  3. Real details: the voice memo transcript (Voice-First Input, resources/vn-spoken/voice-first.md) or matching
     content/story-bank.md rows; spoken connectors (resources/vn-spoken/connectors.tsv) + AI blacklist size.
  4. Latest notes: resources/feedback.md (Hiệp's rejections, tier 1 list), the channel section of rules/ACTIVE-CHECKLIST.md,
     and <clip>/final/feedback.md when --clip is given.
@hi.oneup default (WS1, 27/11): without --arc/--tone the spine is ONEUP-CORE-ARC (Mạch 5 nhịp thực dụng: hook tình huống → bẻ thước đo + gài trend →
1 bằng chứng → 1 việc tối nay → CTA chia sẻ đồng hành, ~200–265 âm tiết ≈ 65–88 s, đủ ý thì dừng). --extended lifts the window to 120–180 s, only for a topic with real technical steps.
The brief also prints the 5 Hiệp-approved clips (a-c01…a-c05) with a one-line DNA each + measured beat structure, the 2–3 closest to the idea flagged, plus the matching story-bank rows and the voice-profile §2 reminder. Writing inputs are only: brief (Gate 0 + Fact-lock + trend) · voice-profile §2–3 · 2–3 closest approved · story-bank row + research/explainers/<topic>.md.
Read-only except --out. Never invents: a missing piece is printed as «chưa có» with where to get it.
"""
import json, math, re, sys, unicodedata
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65
import arc_library as ARC

ROOT = P.ROOT
BEGIN, END = "<!-- GATE0-BRIEF:BEGIN (pipeline/scripts/gate0.py) -->", "<!-- GATE0-BRIEF:END -->"
CH = {"hi": {"name": "@hi.oneup", "lo": 60, "hi": 180, "cap": 300, "default": 90},
      "vht": {"name": "@vanhiep.tech", "lo": 45, "hi": 90, "cap": 90, "default": 60}}
CORE_ARC_ID = "ONEUP-CORE-ARC"
CORE_WINDOW = (65, 88)       # seconds for the core arc unless --extended (khung gọn mặc định; đủ ý thì dừng, không ép dài, không bóp cụt chất kể chuyện)
EXTENDED_WINDOW = (120, 180)
APPROVED = {"a-c01": "content/archive/clip-01-implementation-intention/final/script-final.md",
            "a-c02": "content/archive/clip-02-procrastination-discomfort/final/script-final.md",
            "a-c03": "content/archive/clip-03-big-task-chunking/final/script-final.md",
            "a-c04": "content/archive/clip-04-gap-sach-tu-kiem/final/script-v18-LOCKED.md",
            "a-c05": "content/archive/clip-05-hoc-mot-dem/final/script-final.md"}
# DNA từng bản Hiệp đã duyệt: một dòng để chọn mẫu gần thể loại, không để chép câu. `kw` dùng để xếp hạng theo ý tưởng.
APPROVED_DESC = {
    "a-c01": ("tự giễu + ví dụ đời thường: «mai học» của chính Hiệp, kế hoạch nếu–thì cụ thể, trả lời tuần tự",
              "tự giễu thói quen ví dụ đời thường kế hoạch nếu thì học TOEIC mai học lời hứa"),
    "a-c02": ("khung «bản chất» + meme đời thường: hook thầy hỏi bản chất, 3 dấu hiệu, 1 con số Steel, gọi lại clip-01",
              "bản chất trì hoãn né cảm giác khó chịu lướt TikTok giải thích nguyên nhân dấu hiệu"),
    "a-c03": ("hook câu hỏi mở + chia nhỏ vật lý: việc to thành vài việc cầm được, hai nghiên cứu ngắn, ví dụ dọn phòng/ôn thi",
              "việc to chia nhỏ ngợp cuối tuần dọn phòng ôn thi ước lượng thời gian hook câu hỏi"),
    "a-c04": ("kể chuyện khép vòng: mở bằng chuyện học tối qua sáng quên, đi một mạch, chốt đúng nỗi đau mở đầu",
              "kể chuyện quên sạch học thuộc sách tự kiểm khép vòng nhớ ghi nhớ"),
    "a-c05": ("giọng miền Nam + miếng hài nhập vai: «hà / nè / hông», thí nghiệm có số rõ, câu rào giới hạn, cú hài ghi sổ đầu bài",
              "đọc lại nhớ tự viết thí nghiệm sinh viên giọng miền Nam miếng hài hông nè học một đêm"),
}
STOP = set("và của là có cho một những các được với không thì mà này đó để khi người bạn mình rồi lại cũng như nào gì vì nên".split())


def fold(s):
    s = unicodedata.normalize("NFD", (s or "").lower())
    return unicodedata.normalize("NFC", "".join(c for c in s if unicodedata.category(c) != "Mn")).replace("đ", "d")


def toks(s):
    return {w for w in re.findall(r"[a-z0-9]+", fold(s)) if len(w) > 1 and fold(w) not in {fold(x) for x in STOP}}


def overlap(q, text):
    a, b = toks(q), toks(text)
    return len(a & b) / max(len(a), 1)


def md_rows(path, min_cols=4):
    if not Path(path).exists(): return []
    out = []
    for l in Path(path).read_text(encoding="utf-8").splitlines():
        if l.startswith("|") and not re.match(r"^\|[-\s|:]+\|$", l):
            c = [x.strip() for x in l.strip("|").split("|")]
            if len(c) >= min_cols and c[0] not in ("Ý tưởng", "id", "| id"): out.append(c)
    return out



# ---------- approved-clip rhythm reference (WS1) ----------
def syllables(text):
    """Vietnamese writes one syllable per word token; numbers are written as they are read aloud."""
    clean = re.sub(r"\{[^}:]*:\s*([^}]*)\}", r"\1", (text or "").replace("**", ""))
    return len(re.findall(r"[0-9A-Za-zÀ-ỹđĐ]+", clean))


def _sent_count(text):
    return len([s for s in re.split(r"(?<=[.!?…])\s+", (text or "").strip()) if s.strip()])


def approved_beats(key, root=None):
    """Beats of an approved script as [{label, text, syl, sents}]. Hai khung: bảng beat có cột «Lời…» (a-c01/02/03/05) và «N. [Nhãn] lời» (a-c04)."""
    p = Path(root or ROOT) / APPROVED[key]
    if not p.exists():
        return []
    out, col = [], None
    for ln in p.read_text(encoding="utf-8").splitlines():
        if ln.startswith("## ") and out:
            break  # only the first beat list; later tables (effects, audit) reuse the same beat ids
        m = re.match(r"^\s*\d+\.\s*(?:\*\*)?\[([^\]]+)\](?:\*\*)?\s*(.+)$", ln)
        if m:
            label, text = m.group(1), m.group(2)
        elif ln.startswith("|"):
            c = [x.strip() for x in re.split(r"(?<!\\)\|", ln.strip().strip("|"))]
            if col is None:
                col = next((i for i, x in enumerate(c) if re.match(r"lời", x, re.I)), None)
                continue
            lab = c[0].split()[0] if c and c[0].split() else ""
            if col < len(c) and re.fullmatch(r"[be]\d{2}[a-z]?", lab) and c[col]:
                label, text = lab, c[col].replace("\\|", "|")
            elif len(c) >= 3 and re.fullmatch(r"[be]\d{2}", c[0]) and c[1] in ("remotion", "hyperframes"):
                label, text = c[0], c[2]  # a-c01 cũ: | bNN | engine | lời | caption |
            else:
                continue
        else:
            continue
        text = text.replace("**", "")
        if out and out[-1]["label"] == label:  # same beat spoken in two lines (b12)
            out[-1]["text"] += " " + text
            out[-1]["syl"] = syllables(out[-1]["text"]); out[-1]["sents"] = _sent_count(out[-1]["text"])
        else:
            out.append({"label": label, "text": text, "syl": syllables(text), "sents": _sent_count(text)})
    return out


def approved_structure(root=None):
    res = {}
    for k in APPROVED:
        bs = approved_beats(k, root)
        if bs:
            tot = sum(b["syl"] for b in bs)
            res[k] = {"beats": bs, "total_syl": tot, "n": len(bs), "avg_syl": round(tot / len(bs), 1),
                      "sents": sum(b["sents"] for b in bs)}
    return res


def reference_lines(root=None, picks=None):
    st = approved_structure(root)
    if not st:
        return ["- Nhịp tham chiếu clip đã duyệt: chưa đọc được file nào (`APPROVED` trong gate0.py)."]
    L = [f"- **Nhịp thực tế của {len(st)} clip đã duyệt** (đo từ file, không phải khuôn liệt kê): học độ dài beat + cách chuyển ý + giọng, không chép câu."]
    for k, s in st.items():
        star = " ← mẫu gần nhất, mở đọc" if picks and k in picks else ""
        L.append(f"  - {k}: {APPROVED_DESC[k][0]}{star}")
        L.append(f"    {s['n']} beat · {s['total_syl']} âm tiết · TB {s['avg_syl']} âm tiết/beat · {s['sents']} câu · beat: " +
                 ", ".join(f"{b['label']} {b['syl']}" for b in s["beats"]))
    return L


def pick_approved(q, n=3):
    """2–3 bản đã duyệt gần thể loại/ý tưởng nhất (xếp theo từ khóa DNA + lời beat đầu); luôn trả đủ n nếu có ≥ n bản."""
    scored = []
    for k in APPROVED:
        bs = approved_beats(k)
        first = " ".join(b["text"] for b in bs[:3])
        scored.append((overlap(q, APPROVED_DESC[k][1] + " " + APPROVED_DESC[k][0]) + 0.5 * overlap(q, first), k))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return [k for _, k in scored[:n]]


VOICE_REMINDER = [
    "- **Giọng Hiệp (`content/voice-profile.md` §2, bắt buộc):** miền Nam nhất quán, xưng mình–bạn; cấm trộn chữ Bắc «ấy / thế / nhé» cạnh «hông / nha / nè». Có chủ thể/ngữ khí trò chuyện ngay câu đầu (không mở bằng châm ngôn cụt chủ ngữ); đọc lên phải giống tin nhắn thoại gửi bạn thân.",
    "- **Kiến trúc 2 Pha chống Prompt Bloat (DL-079, `docs/prompts/writer-hi-oneup.md`):** **Pha 1 (Pure Voice)** học nhạc điệu từ 2–3 mẫu duyệt gần nhất, viết liền 1 hơi sống động trước (không mở bảng cấm). **Pha 2 (Surgical Audit)** mới kiểm Fact-lock, ngân sách âm tiết, tách Beat có đánh dấu `**nhấn**` mỗi câu — chỉ sửa vi phẫu từ vi phạm, cấm gọt phẳng khẩu ngữ.",
    "- **Ngân sách nguyên liệu (Anti-Stuffing Budget, DL-077..079):** không phải checklist điền đủ.",
    "  - **Đúng 1 nỗi đau đại chúng** · **Đúng 1 câu hỏi trung tâm** · **6–7 beat, ~200–265 âm tiết (~65–88s)** (`b01` ≤ 20 âm tiết rõ nghĩa trong 3s đầu, `b01+b02` ≤ 65, beat ≤ 45; `audio-precheck.py` cảnh báo `HOOK_LONG` / `SLOW_ENTRY` / `BEAT_BLOAT`).",
    "  - **Bằng chứng ≤ 35 âm tiết (Storytelling the Study + Climactic Order):** dẫn từ kỳ vọng sai → cú tỉnh ngộ (không nhảy kiểu Wikipedia), đặt **số nhỏ trước → số lớn gây bất ngờ cuối câu** (`18 → 254 ngày, hơn 8 tháng`), dịch nghĩa số lớn, bỏ cỡ mẫu/số tuần/món phụ khỏi lời đọc; rào giới hạn ≤ 1 vế ngắn; gia vị giọng chọn **tối đa 1–2 thứ** tự nhiên.",
    "  - **Đủ ý & Khép vòng + CTA chia sẻ đồng hành + Thought-Flow over Connector-Glue (DL-069, DL-080, DL-081):** giải tỏa nỗi lo ở Hook **ngay sau số liệu**, có 1 đổi thước đo + 1 hành động cụ thể; CTA phải **đồng cảm («ai bị giống mình») + lắng nghe góc nhìn/cách mỗi người vượt qua khúc dễ nản**, **cấm khảo sát xã giao sáo rỗng («bạn đang tập gì, được bao lâu») & cấm ép «comment 1 chữ»**; cấm mở câu rập khuôn `Tại / Mà / Vậy / Nghĩa là / Nên / Còn… thì sao`, cấm câu meta «dạo này có câu trend nói» hay cảnh giả «lướt trúng câu đang trend»; trend là xương sống ngay Hook hoặc xin ngoại lệ như `DL-069`.",
    "  - **Given–New Conceptual Flow + 4 hướng dẫn chuyện (`docs/research/storytelling-craft-guide.md`, DL-078/079):** chọn 1 hướng ở Gate 0 (`Misconception Reveal` · `Everyday Paradox` · `5-Second Moment` · `Self-Dialogue`); nối bằng tâm lý/tình huống ngầm (**CẤM điệp từ cuối–đầu cơ học Anadiplosis** kiểu `còn đó → Công còn đó`); Đề–Thuyết tự nhiên, 1 họ ẩn dụ duy nhất, không từ lệch nghĩa.",
    "- Chuyện thật từ `content/story-bank.md` (`[CẦN HIỆP XÁC NHẬN]` nếu chưa chốt), không bịa kết quả.",
]


# ---------- piece 1 ----------
def find_ideas(q, lib, n=3):
    rows = [{"kind": "idea-bank", "text": r[0], "cols": r} for r in md_rows(ROOT / "content/idea-bank.md") if not r[0].startswith("<")]
    rows = [r for r in rows if not any(r["text"] == x["idea"] for x in lib["ideas"])]
    rows += [{"kind": "arc-idea", "text": x["idea"], "idea": x} for x in lib["ideas"]]
    scored = sorted(((overlap(q, r["text"]), r) for r in rows), key=lambda x: -x[0])
    return [r for s, r in scored[:n] if s > 0]


def find_fact_package(q, topic=None):
    d = ROOT / "research/explainers"
    files = sorted(d.glob("*.md")) if d.exists() else []
    if topic:
        f = d / f"{topic}.md"
        return f if f.exists() else None
    best = max(files, key=lambda f: overlap(q, f.stem.replace("-", " ") + " " + f.read_text(encoding="utf-8")[:600]), default=None)
    return best if best and overlap(q, best.stem.replace("-", " ") + " " + best.read_text(encoding="utf-8")[:600]) > 0.3 else None


def fm_title(f):
    m = re.search(r'^title:\s*"?(.*?)"?\s*$', f.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else f.stem


# ---------- piece 2 ----------
HOOK_MAX = 8  # the opening beat keeps its own length (≤ 8 s); only the body stretches to the target


def _spans(arc, total):
    beats = arc.get("beats") or [{"role": f"bước {i + 1}"} for i in range(len(arc.get("skeleton", [])))]
    secs = [float(b.get("seconds") or 0) for b in beats]
    if not beats: return [], []
    hook = min(secs[0] or 5, HOOK_MAX); rest = secs[1:] if sum(secs[1:]) > 0 else [1.0] * (len(beats) - 1)
    body = total - hook; spans, t = [], 0.0
    for i, b in enumerate(beats):
        d = hook if i == 0 else (body * rest[i - 1] / sum(rest) if rest else 0)
        spans.append((t, t + d)); t += d
    return beats, spans


def plan_hi(arc, total):
    """Map ARC beats onto `total` seconds and place an Open Loop + Micro-Payoff every 35–45 s (target 40)."""
    beats, spans = _spans(arc, total); sk = arc.get("skeleton", [])
    rows = [{"from": round(a), "to": round(b), "role": x.get("role"), "skeleton": sk[i] if i < len(sk) else "", "function": x.get("function")}
            for i, (x, (a, b)) in enumerate(zip(beats, spans))]
    n = max(1, math.floor((total - 3) / 40))
    step = (total - 3) / (n + 1) if n else total
    step = min(45, max(35, step))
    loops = []
    k, at = 1, 3.0 + step
    while at < total - 10:
        loops.append({"at": round(at), "payoff": f"trả một phần lời hứa (micro-payoff {k})", "loop": f"mở câu hỏi mới kéo sang đoạn sau (open loop {k + 1})"})
        k += 1; at += step
    return rows, loops


def plan_vht(arc, total):
    beats, spans = _spans(arc, total); sk = arc.get("skeleton", [])
    return [{"from": round(a), "to": round(b), "role": x.get("role"), "skeleton": sk[i] if i < len(sk) else "",
             "layers": f"{max(1, math.floor((b - a) / 5))}–{max(1, math.ceil((b - a) / 3))}"} for i, (x, (a, b)) in enumerate(zip(beats, spans))]


# ---------- piece 3 / 4 ----------
def story_rows(q, n=2):
    rows = md_rows(ROOT / "content/story-bank.md", 4)
    scored = sorted(((overlap(q, " ".join(r[:4])), r) for r in rows if re.match(r"S-\d+", r[0])), key=lambda x: -x[0])
    return [r for s, r in scored[:n] if s > 0]


def tsv(path):
    if not Path(path).exists(): return []
    return [l.rstrip("\n").split("\t") for l in Path(path).read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]


def load_style_pairs(path=None):
    """Parse resources/vn-spoken/style-pairs.md table rows into dicts."""
    p = Path(path or (ROOT / "resources/vn-spoken/style-pairs.md"))
    out = []
    for r in md_rows(p, 6):
        if re.match(r"SP-\d+", r[0]):
            out.append({"id": r[0], "channel": r[1], "topics": r[2], "raw": r[3], "approved": r[4], "why": r[5],
                        "tone": r[6] if len(r) > 6 else ""})
    return out


def _has_warm_subject(text):
    pad = f" {(text or '').lower()} "
    return " mình " in pad or " bạn " in pad


def _choppy_approved(text):
    """Majority of sentences ≤ 6 words: the tight punch style story_warm must not learn."""
    sents = [s.strip() for s in re.split(r"[.!?]+", text or "") if s.strip()]
    if len(sents) < 2:
        return False
    shorts = sum(1 for s in sents if len(s.split()) <= 6)
    return shorts >= 2 and shorts * 2 >= len(sents)


def pick_style_pairs(q, ch="hi", n=3, path=None, tone=None):
    """Pick the n closest style-pairs for the topic and channel (preferring channel match + token overlap).

    tone=story_warm keeps warm narrative pairs that say «mình» or «bạn» and drops choppy punch lines.
    tone=tech_sharp keeps only pairs tagged tech_sharp. tone omitted keeps the old ranking.
    """
    pairs = load_style_pairs(path)
    if tone == "story_warm":
        pairs = [sp for sp in pairs if sp.get("tone") == "story_warm" and _has_warm_subject(sp["approved"]) and not _choppy_approved(sp["approved"])]
    elif tone == "tech_sharp":
        pairs = [sp for sp in pairs if sp.get("tone") == "tech_sharp"]
    if not pairs:
        return []
    ch_name = CH.get(ch, {}).get("name", "@hi.oneup")
    scored = []
    for idx, sp in enumerate(pairs):
        ch_bonus = 2.0 if ch_name in sp["channel"] else 0.0
        ov_topic = overlap(q, sp["topics"])
        ov_body = overlap(q, sp["raw"] + " " + sp["approved"] + " " + sp["why"])
        score = ch_bonus + 2.0 * ov_topic + ov_body
        scored.append((score, -idx, sp))
    scored.sort(key=lambda x: (-x[0], -x[1]))
    return [sp for _, _, sp in scored[:n]]


def load_weekly_synthesis(path=None):
    """Load optional priority weights generated by pipeline/scripts/pattern-synthesize.py."""
    p = Path(path or (ROOT / "research/trends/weekly-synthesis.json"))
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def pick_best_arc(arcs, synth=None):
    """Pick top ARC prioritizing win_rate, then weekly-synthesis weight, then wins/seen."""
    if not arcs:
        return None
    weights = (synth or {}).get("arc_weights") or {}
    if not weights:
        return ARC.best_arc(arcs)
    def key(a):
        wr = a.get("win_rate")
        if wr is None:
            wr = ARC._compute_win_rate(a.get("uses", 0), a.get("wins", 0))
        w = float(weights.get(a["id"], 0.0))
        return (wr if wr is not None else -1.0, w, a.get("wins", 0), a.get("seen", 0), -a.get("uses", 0))
    return max(arcs, key=key)


def checklist_section(ch):
    t = (ROOT / "rules/ACTIVE-CHECKLIST.md").read_text(encoding="utf-8") if (ROOT / "rules/ACTIVE-CHECKLIST.md").exists() else ""
    head = "## 2. Kênh `@hi.oneup`" if ch == "hi" else "## 3. Kênh `@vanhiep.tech`"
    if head not in t: return []
    sec = t.split(head, 1)[1].split("\n## ", 1)[0]
    return [l for l in sec.splitlines() if l.startswith("- ") and not l.rstrip().endswith(":**")][:6]


def feedback_rows():
    return [r for r in md_rows(ROOT / "resources/feedback.md", 4) if r[0].startswith("«")]


def brief(idea_q, ch="hi", arc_id=None, memo=None, topic=None, clip=None, length=None, tone=None, extended=False):
    lib = ARC.load(); c = CH[ch]; L = [BEGIN, f"## Gate 0 brief ({c['name']})", ""]
    # 1
    ideas = find_ideas(idea_q, lib)
    L += ["### 1. Ý tưởng đã chọn + fact package"]
    if ideas:
        for r in ideas:
            if r["kind"] == "arc-idea":
                x = r["idea"]; L.append(f"- [{x['arc']} · {ARC.CHANNELS[x['channel']]}] {x['idea']} — hook nháp: {x.get('hook') or '—'} (teardown `{x['teardown']}`)")
            else:
                L.append(f"- [idea-bank] {' | '.join(r['cols'][:6])}")
    else:
        L.append(f"- chưa có dòng nào khớp «{idea_q}» trong `content/idea-bank.md` → thêm ý vào idea-bank trước (trend-digest hoặc teardown Khối 6).")
    fp = find_fact_package(idea_q, topic)
    L.append(f"- Fact package: `{fp.relative_to(ROOT)}` — {fm_title(fp)}" if fp else "- Fact package: chưa có (`research/explainers/<chủ-đề>.md`); mọi số liệu cần claim → nguồn trước khi viết (H1).")
    # 2
    synth = load_weekly_synthesis()
    arc = ARC.get(arc_id) if arc_id else None
    if not arc and tone:
        tagged = [a for a in lib["arcs"] if a.get("tone") == tone]
        if len(tagged) == 1:
            arc = tagged[0]
        elif tagged:
            arc = pick_best_arc(tagged, synth)
    if not arc and ch == "hi" and not tone:  # @hi.oneup default spine (WS1): the core 5-beat arc, not a listicle teardown arc
        arc = next((a for a in lib["arcs"] if a["id"] == CORE_ARC_ID), None)
    if not arc:
        aid = next((r["idea"]["arc"] for r in ideas if r["kind"] == "arc-idea"), None)
        arc = ARC.get(aid) if aid else pick_best_arc(lib["arcs"], synth)
    L += ["", "### 2. Mạch cốt truyện"]
    if not arc:
        L.append("- chưa có ARC nào (`research/blueprints/index.json`): chạy teardown 1 clip outlier trước.")
    else:
        idea_len = next((r["idea"].get("length_s") for r in ideas if r["kind"] == "arc-idea" and r["idea"]["channel"] == ("hi_oneup" if ch == "hi" else "vanhiep_tech")), None)
        is_core = arc["id"] == CORE_ARC_ID and ch == "hi"
        if is_core:
            lo_s, hi_s = EXTENDED_WINDOW if extended else CORE_WINDOW
            total = int(length or (150 if extended else 65)); total = max(lo_s, min(total, hi_s))
        else:
            total = int(length or idea_len or c["default"]); total = max(c["lo"], min(total, c["hi"]))
        ev = ", ".join(f"{e.get('creator') or e.get('source')}" + (f" {e['ratio']}x" if e.get("ratio") else "") for e in arc.get("evidence", []))
        wr = arc.get("win_rate")
        wr_str = f"{wr:.0%} ({arc.get('wins', 0)}/{arc.get('uses', 0)})" if wr is not None else "chưa có"
        sw = (synth or {}).get("arc_weights", {}).get(arc["id"])
        sw_str = f" · trọng số synthesis: {sw:.2f}" if sw is not None else ""
        L.append(f"- **{arc['id']}** {arc.get('name') or ''} · cơ chế hook: {arc.get('hook_mechanism') or '—'} · bằng chứng: {ev or '—'} · đã dùng {arc.get('uses', 0)} lần · win_rate: {wr_str}{sw_str}")
        if synth and synth.get("top_hooks"):
            th = ", ".join(f"{h['mechanism']} ({h['weight']:.2f})" for h in synth["top_hooks"][:3])
            L.append(f"- Tổng hợp đa video (`research/trends/weekly-synthesis.md`): hook đang thắng — {th}")
        L += [f"  {i}. {s}" for i, s in enumerate(arc.get("skeleton", []), 1)]
        if ch == "hi" and is_core:
            ts = arc.get("target_syllables") or [200, 265]
            L.append(f"- Mạch chuẩn `{CORE_ARC_ID}`: **{ts[0]}–{ts[1]} âm tiết ≈ {CORE_WINDOW[0]}–{CORE_WINDOW[1]}s** đọc tự nhiên (2.7–3.3 âm tiết/s); các clip đã duyệt nằm ở ~190–310 âm tiết. Đủ ý thì dừng: không kéo dài, cũng không bóp cụt phần kể chuyện (chuyện thật, tự giễu, lời nội tâm là chất của kênh)"
                     + (f"; đang ở chế độ `--extended` {EXTENDED_WINDOW[0]}–{EXTENDED_WINDOW[1]}s vì chủ đề có nhiều bước kỹ thuật thật sự." if extended
                        else f"; chỉ mở rộng lên {EXTENDED_WINDOW[0]}–{EXTENDED_WINDOW[1]}s (`--extended`) khi chủ đề có nhiều bước kỹ thuật thật sự."))
            L.append("  Ngân sách âm tiết mỗi nhịp (gợi ý để cân đối, không phải trần cứng): " + " · ".join(f"{b['role']} {b['syllables'][0]}–{b['syllables'][1]}" for b in arc.get("beats", []) if b.get("syllables")) +
                     ". Một ví dụ xuyên suốt từ nhịp 1 tới nhịp 4. Không bịa chuyển cảnh, không câu tóm tắt bài học.")
        if ch == "hi":
            rows, loops = plan_hi(arc, total)
            L += ["", f"Nhịp cho {c['name']}: gợi ý **{total}s** khi chưa có lời ({'%d–%ds, mạch lõi' % (EXTENDED_WINDOW if extended else CORE_WINDOW) if is_core else '60–180s'}, hard cap < 300s gồm end card/nghỉ/chuyển cảnh, L-099). Câu chuyện đã đủ ý thì giữ độ dài đó, không kéo chữ. Story beat = comic, giải thích/bằng chứng = motion (DL-027).",
                  "| giây | vai trò | khung |", "|---|---|---|"]
            L += [f"| {r['from']}–{r['to']} | {r['role']} | {r['skeleton']} |" for r in rows]
            L += ["", "Open Loop & Micro-Payoff (mỗi 35–45s):"] + [f"- ~{x['at']}s: {x['payoff']} → {x['loop']}" for x in loops]
        else:
            rows = plan_vht(arc, total)
            L += ["", f"Nhịp cho {c['name']}: mục tiêu **{total}s** (45–90s), cắt layer `ov-*` / `cu-*` mỗi 3–5s, 1–2 `ov-dNN` bắt buộc.",
                  "| giây | vai trò | khung | số layer (3–5s/layer) |", "|---|---|---|---|"]
            L += [f"| {r['from']}–{r['to']} | {r['role']} | {r['skeleton']} | {r['layers']} |" for r in rows]
    # 3
    L += ["", "### 3. Chi tiết thật + giọng Hiệp"]
    if memo and Path(memo).exists():
        lines = [l.strip() for l in Path(memo).read_text(encoding="utf-8").splitlines() if l.strip()]
        L.append(f"- **Voice-First Input** `{memo}` ({len(lines)} đoạn): giữ ≥ 80% từ của Hiệp, chỉ đổi nhịp (`voice-memo.py keep <memo> <draft>`).")
        L += [f"  > {l}" for l in lines[:12]] + (["  > …"] if len(lines) > 12 else [])
    st = story_rows(idea_q)
    L += [f"- Story bank {r[0]}: {r[1]} ({r[2]})" for r in st] or ["- Story bank: không có dòng nào khớp từ khóa của ý này; dùng `[VÍ DỤ THẬT CỦA HIỆP: …]` hoặc xin Hiệp ghi âm 60–90s (Voice-First)."]
    if ch == "hi":
        L += VOICE_REMINDER
    picks = pick_approved(idea_q) if ch == "hi" else []
    L.append("- **Chỉ nạp 4 thứ khi viết nháp v1/v2:** (1) brief này (Gate 0 + Fact-lock + trend); (2) `content/voice-profile.md` §2–3; "
             + ("(3) 2–3 bản đã duyệt gần thể loại nhất: " + ", ".join(f"{k} `{APPROVED[k]}`" for k in picks) if picks else "(3) 2–3 bản đã duyệt cùng kênh")
             + "; (4) dòng `content/story-bank.md` khớp + `research/explainers/<topic>.md` nếu có. Không nạp `connectors.tsv`, `bookish.tsv`, `ai-blacklist.tsv`, `cadence-patterns.tsv`, style-pairs vào bước viết; các bảng đó chỉ cho `check-rules.py --audit` sau khi lời đã xong.")
    L.append("- **Fact-lock:** ghi danh sách số/kết luận được phép nói và danh sách CẤM (từ/số bị cấm, cơ chế não ngoài nguồn) trước khi viết; chạm vào danh sách cấm = H1. **Single-Point Alignment:** chọn 1 câu hỏi trung tâm; hook và bằng chứng là câu hỏi và câu trả lời của cùng câu đó.")
    if ch == "hi":
        L += reference_lines(picks=picks)
    if tone:
        L.append(f"- tone `{tone}`: học nhịp kể của a-c01 và a-c04, không lấy câu chặt chém.")
    # 4
    L += ["", "### 4. Lưu ý mới nhất"]
    fb = feedback_rows()
    L += [f"- Hiệp chê: {r[0]} → {r[1]} ({r[3]})" for r in fb[-6:]] or ["- `resources/feedback.md`: chưa có"]
    L.append("- Tầng 1 (chặn tuyệt đối): H1 fact không nguồn · H2 ≥ 300s · H3 sai brand/format kênh hoặc chê người xem · H4 lỗi cấu trúc. Tầng 2 so cặp Pairwise A/B với bản duyệt cùng chủ đề/format; khẩu ngữ tự nhiên không bị trừ.")
    L += [f"- {l[2:]}" for l in checklist_section(ch)]
    if clip:
        f = Path(clip) / "final/feedback.md"
        L += [f"- Góp ý clip: {r[2]} ({r[0]})" for r in md_rows(f, 4) if re.match(r"20\d\d-", r[0])] if f.exists() else [f"- `{f}`: chưa có góp ý"]
    L.append(END)
    return "\n".join(L) + "\n"


def write_into(draft, block):
    p = Path(draft); t = p.read_text(encoding="utf-8") if p.exists() else ""
    if BEGIN in t and END in t:
        t = t[: t.index(BEGIN)] + block.rstrip("\n") + t[t.index(END) + len(END):]
    elif t.startswith("---") and "\n---" in t[3:]:
        i = t.index("\n---", 3) + 4
        t = t[:i] + "\n\n" + block + t[i:]
    else:
        t = block + "\n" + t
    p.write_text(t, encoding="utf-8")


def main():
    a = sys.argv[1:]
    def opt(n, d=None): return a[a.index(n) + 1] if n in a else d
    if not opt("--idea"): print(__doc__); return 2
    ch = opt("--channel", "hi")
    if ch not in CH: print("--channel hi|vht"); return 2
    tone = opt("--tone")
    if tone and tone not in ("story_warm", "tech_sharp"):
        print("--tone story_warm|tech_sharp"); return 2
    b = brief(opt("--idea"), ch, opt("--arc"), opt("--memo"), opt("--topic"), opt("--clip"), opt("--length"), tone, "--extended" in a)
    if opt("--out"): write_into(opt("--out"), b); print(f"→ {opt('--out')}")
    else: print(b)
    return 0


if __name__ == "__main__":
    sys.exit(main())
