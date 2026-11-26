#!/usr/bin/env python3
"""Gate 0 brief: load the 4 pieces before draft v1 (make-video §2.0 step 0, channels/vanhiep-tech/AGENTS.md).

  gate0.py --idea "<words from the idea>" [--channel hi|vht] [--arc ARC-NNN] [--memo media/voice-memos/x.txt]
           [--topic <research/explainers slug>] [--clip content/clips/clip-NN-*/] [--length 150] [--out <draft.md>]

Pieces (printed as one Markdown block; --out writes/replaces the block between GATE0-BRIEF markers at the top of the draft):
  1. Idea: best-matching rows of content/idea-bank.md (main table + «Từ teardown (ARC)» ideas) + fact package
     (research/explainers/<topic>.md, best match by words when --topic is omitted).
  2. Story arc ARC-NNN (research/blueprints/index.json): skeleton + beat timing planned for the channel —
     @hi.oneup 120–180 s target (strict < 300 s, L-099) with an Open Loop + Micro-Payoff every 35–45 s;
     @vanhiep.tech 45–90 s with a layer cut every 3–5 s.
  3. Real details: the voice memo transcript (Voice-First Input, resources/vn-spoken/voice-first.md) or matching
     content/story-bank.md rows; spoken connectors (resources/vn-spoken/connectors.tsv) + AI blacklist size.
  4. Latest notes: resources/feedback.md (Hiệp's rejections, tier 1 list), the channel section of rules/ACTIVE-CHECKLIST.md,
     and <clip>/final/feedback.md when --clip is given.
Read-only except --out. Never invents: a missing piece is printed as «chưa có» with where to get it.
"""
import json, math, re, sys, unicodedata
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65
import arc_library as ARC

ROOT = P.ROOT
BEGIN, END = "<!-- GATE0-BRIEF:BEGIN (pipeline/scripts/gate0.py) -->", "<!-- GATE0-BRIEF:END -->"
CH = {"hi": {"name": "@hi.oneup", "lo": 120, "hi": 180, "cap": 300, "default": 150},
      "vht": {"name": "@vanhiep.tech", "lo": 45, "hi": 90, "cap": 90, "default": 60}}
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


def checklist_section(ch):
    t = (ROOT / "rules/ACTIVE-CHECKLIST.md").read_text(encoding="utf-8") if (ROOT / "rules/ACTIVE-CHECKLIST.md").exists() else ""
    head = "## 2. Kênh `@hi.oneup`" if ch == "hi" else "## 3. Kênh `@vanhiep.tech`"
    if head not in t: return []
    sec = t.split(head, 1)[1].split("\n## ", 1)[0]
    return [l for l in sec.splitlines() if l.startswith("- ") and not l.rstrip().endswith(":**")][:6]


def feedback_rows():
    return [r for r in md_rows(ROOT / "resources/feedback.md", 4) if r[0].startswith("«")]


def brief(idea_q, ch="hi", arc_id=None, memo=None, topic=None, clip=None, length=None):
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
    arc = ARC.get(arc_id) if arc_id else None
    if not arc:
        aid = next((r["idea"]["arc"] for r in ideas if r["kind"] == "arc-idea"), None)
        arc = ARC.get(aid) if aid else ARC.best_arc(lib["arcs"])
    L += ["", "### 2. Mạch cốt truyện"]
    if not arc:
        L.append("- chưa có ARC nào (`research/blueprints/index.json`): chạy teardown 1 clip outlier trước.")
    else:
        idea_len = next((r["idea"].get("length_s") for r in ideas if r["kind"] == "arc-idea" and r["idea"]["channel"] == ("hi_oneup" if ch == "hi" else "vanhiep_tech")), None)
        total = int(length or idea_len or c["default"]); total = max(c["lo"], min(total, c["hi"]))
        ev = ", ".join(f"{e.get('creator') or e.get('source')}" + (f" {e['ratio']}x" if e.get("ratio") else "") for e in arc.get("evidence", []))
        wr = arc.get("win_rate")
        wr_str = f"{wr:.0%} ({arc.get('wins', 0)}/{arc.get('uses', 0)})" if wr is not None else "chưa có"
        L.append(f"- **{arc['id']}** {arc.get('name') or ''} · cơ chế hook: {arc.get('hook_mechanism') or '—'} · bằng chứng: {ev or '—'} · đã dùng {arc.get('uses', 0)} lần · win_rate: {wr_str}")
        L += [f"  {i}. {s}" for i, s in enumerate(arc.get("skeleton", []), 1)]
        if ch == "hi":
            rows, loops = plan_hi(arc, total)
            L += ["", f"Nhịp cho {c['name']}: mục tiêu **{total}s** (120–180s là mục tiêu, hard cap < 300s gồm end card/nghỉ/chuyển cảnh, L-099). Story beat = comic, giải thích/bằng chứng = motion (DL-027).",
                  "| giây | vai trò | khung |", "|---|---|---|"]
            L += [f"| {r['from']}–{r['to']} | {r['role']} | {r['skeleton']} |" for r in rows]
            L += ["", "Open Loop & Micro-Payoff (mỗi 35–45s):"] + [f"- ~{x['at']}s: {x['payoff']} → {x['loop']}" for x in loops]
        else:
            rows = plan_vht(arc, total)
            L += ["", f"Nhịp cho {c['name']}: mục tiêu **{total}s** (45–90s), cắt layer `ov-*` / `cu-*` mỗi 3–5s, 1–2 `ov-dNN` bắt buộc.",
                  "| giây | vai trò | khung | số layer (3–5s/layer) |", "|---|---|---|---|"]
            L += [f"| {r['from']}–{r['to']} | {r['role']} | {r['skeleton']} | {r['layers']} |" for r in rows]
    # 3
    L += ["", "### 3. Chi tiết thật + khẩu ngữ"]
    if memo and Path(memo).exists():
        lines = [l.strip() for l in Path(memo).read_text(encoding="utf-8").splitlines() if l.strip()]
        L.append(f"- **Voice-First Input** `{memo}` ({len(lines)} đoạn): giữ ≥ 80% từ của Hiệp, chỉ đổi nhịp (`voice-memo.py keep <memo> <draft>`).")
        L += [f"  > {l}" for l in lines[:12]] + (["  > …"] if len(lines) > 12 else [])
    else:
        st = story_rows(idea_q)
        L += [f"- Story bank {r[0]}: {r[1]} ({r[2]})" for r in st] or ["- Story bank: không có chuyện khớp; dùng `[VÍ DỤ THẬT CỦA HIỆP: …]` hoặc xin Hiệp ghi âm 60–90s (Voice-First)."]
    con = [r for r in tsv(ROOT / "resources/vn-spoken/connectors.tsv") if len(r) >= 4]
    con.sort(key=lambda r: {"H": 0, "PB": 1}.get(r[3], 2))
    L.append("- Từ nối văn nói (≤ 1 mỗi beat, không lặp): " + " · ".join(f"«{r[0]}» ({r[1]})" for r in con[:6]))
    L.append(f"- Cấm {len(tsv(ROOT / 'resources/vn-spoken/ai-blacklist.tsv'))} cụm mùi AI / văn dịch (`resources/vn-spoken/ai-blacklist.tsv`, `check-rules.py --bookish`).")
    # 4
    L += ["", "### 4. Lưu ý mới nhất"]
    fb = feedback_rows()
    L += [f"- Hiệp chê: {r[0]} → {r[1]} ({r[3]})" for r in fb[-6:]] or ["- `resources/feedback.md`: chưa có"]
    L.append("- Tầng 1 (chặn tuyệt đối): H1 fact không nguồn · H2 ≥ 300s · H3 sai brand/format kênh hoặc chê người xem · H4 lỗi cấu trúc. Còn lại chấm điểm, ≥ 85 là đạt; khẩu ngữ tự nhiên không bị trừ (rubric §3b).")
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
    b = brief(opt("--idea"), ch, opt("--arc"), opt("--memo"), opt("--topic"), opt("--clip"), opt("--length"))
    if opt("--out"): write_into(opt("--out"), b); print(f"→ {opt('--out')}")
    else: print(b)
    return 0


if __name__ == "__main__":
    sys.exit(main())
