#!/usr/bin/env python3
"""Multi-Script Tournament Arena Orchestrator (Content Engine v2.0, F3, DL-082).

Instead of writing 1 single draft and iterating serially for 13–21 rounds, generates 3 contrasting
Pure-Voice Writer briefs (from 1 shared Fact-lock) across different Storytelling Archetypes (M1..M5),
scores all 3 drafts through automated rhythm + emotional-arc checks, and prepares an Independent
Tournament Judge prompt to select Top 1 Recommended + 1 Contrasting Runner-up for Gate 1.

CLI:
  # 1. Prepare 3 contrasting Pure-Voice writer briefs from 1 Fact-lock
  python3 pipeline/scripts/script-arena.py prepare --idea "<ý tưởng>" --out-dir <clip>/archive/arena
      [--archetypes M1,M2,M4] [--topic <slug>] [--trend "<trend>"] [--fact-lock <path>]

  # 2. Score 3 completed drafts & emit Tournament Judge brief
  python3 pipeline/scripts/script-arena.py score --dir <clip>/archive/arena [--out <clip>/archive/arena/scorecard.md] [--json]
  python3 pipeline/scripts/script-arena.py score --drafts a.md,b.md,c.md [--json]
"""
import importlib.util
import json
import sys
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65

ROOT = P.ROOT
DEFAULT_ARCHETYPES = ("M1", "M2", "M6")
SOUL_ARCHETYPES = ("M2", "M6", "M7")


def _load_mod(name, rel_path):
    p = ROOT / rel_path
    sp = importlib.util.spec_from_file_location(name, str(p))
    mod = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(mod)
    return mod


def prepare_arena(
    idea,
    out_dir,
    archetypes=DEFAULT_ARCHETYPES,
    channel="hi",
    topic=None,
    trend=None,
    fact_lock_text=None,
    clip=None,
):
    """Generate 3 independent Pure-Voice Writer briefs (Pha 1, zero blacklist bloat) sharing 1 Fact-lock."""
    g0 = _load_mod("gate0", "pipeline/scripts/gate0.py")
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    picks = [a.strip().upper() for a in archetypes if a.strip().upper() in g0.ARCHETYPES]
    if not picks:
        picks = list(DEFAULT_ARCHETYPES)

    written = []
    for idx, ak in enumerate(picks):
        label = chr(ord("A") + idx)
        ad = g0.ARCHETYPES[ak]
        base_brief = g0.brief(idea, ch=channel, topic=topic, clip=clip, archetype=ak)
        lines = [
            "---",
            f'title: "Arena Writer {label} ({ak} — {ad["name"]})"',
            "date: 2026-11-28",
            f"id: arena.writer-{label.lower()}-{ak.lower()}",
            "type: draft",
            "status: draft",
            *(["mode: philosophy"] if ad.get("mode") == "philosophy" else []),
            "updated: 2026-11-28",
            f"tags: [arena, script-draft, {ak.lower()}]",
            "---",
            f"# Đấu trường Kịch bản — Writer {label} (`{ak}`: {ad['name']})",
            "",
            "> **LỆNH PHA 1 (PURE VOICE PASS — `DL-079`):** Đọc 2–3 clip duyệt gần nhất để thấm nhạc điệu miền Nam xưng mình–bạn, rồi viết liền 1 hơi sống động theo đúng phương pháp dưới đây. **Không mở bảng cấm từ trong lúc viết.** Sau khi viết xong mới sang Pha 2 kiểm Fact-lock & âm tiết (`200–265` âm tiết, `b01 ≤ 20`, mỗi beat `≤ 45`).",
            "",
            f"- **Phương pháp được khóa:** `{ak}` — {ad['name']} (*{ad['color']}*)",
            f"- **Cách mở Hook:** {ad['hook_style']}",
            f"- **Đường cong cảm xúc bắt buộc (`Emotional Wave`):** {ad['wave']}",
            f"- **Mẫu duyệt gợi ý nghe nhịp:** {', '.join(ad['ref_clips'])}",
        ]
        if trend:
            lines.append(f"- **Trend/Bối cảnh đang nóng (< 72h):** {trend} (dùng làm xương sống ẩn dụ ngay Hook, cấm câu meta «dạo này có câu trend nói»)")
        if fact_lock_text:
            lines += ["", "## Fact-lock dùng chung (tuyệt đối không vượt ngoài khối này — H1)", "", fact_lock_text.strip()]
        lines += ["", base_brief, "## Bản nháp của Writer " + label, "", "*(Viết 6–8 beat dạng `1. **[b01 · 0–6s]** ...` ở đây)*", ""]
        p = out / f"draft-{label}-{ak}.md"
        p.write_text("\n".join(lines), encoding="utf-8")
        written.append({"label": label, "archetype": ak, "name": ad["name"], "color": ad["color"], "path": str(p)})
    return written


def score_draft(path, ap=None, archive_hooks=None):
    """Run Audio-Back + Emotional Trajectory precheck on one arena draft."""
    ap = ap or _load_mod("audio_precheck", "pipeline/scripts/audio-precheck.py")
    p = Path(path)
    md = p.read_text(encoding="utf-8")
    beats = ap.parse_beats(md)
    if not beats:
        return {"path": str(p), "name": p.name, "beats_count": 0, "ok": False, "score": 0.0, "warnings": [{"code": "NO_BEATS", "message": "Chưa có lời thoại dạng beat"}]}
    res = ap.analyze_beats(beats, archive_hooks=archive_hooks)
    # Composite mechanical readiness score (0..100) to rank before Independent Tournament Judge
    score = 100.0
    for w in res["warnings"]:
        code = w["code"]
        if code in ("HOOK_LONG", "SLOW_ENTRY", "BEAT_BLOAT", "HOOK_ECHO"):
            score -= 15.0
        elif code in ("FLAT_CADENCE", "MISSING_VULNERABILITY_DIP"):
            score -= 12.0
        else:
            score -= 8.0
    tot = res["total_syllables"]
    if tot < 160 or tot > 310:
        score -= 10.0
    return {
        "path": str(p),
        "name": p.name,
        "beats_count": len(beats),
        "total_syllables": tot,
        "estimated_total_s": res["estimated_total_s"],
        "warning_codes": [w["code"] for w in res["warnings"]],
        "warnings": res["warnings"],
        "voice_ref_map": res.get("voice_ref_map", {}),
        "ok": res["ok"],
        "score": round(max(0.0, score), 1),
    }


def score_arena(draft_paths, archive_hooks=None):
    """Score all arena drafts and return ranked results + Tournament Judge brief."""
    ap = _load_mod("audio_precheck", "pipeline/scripts/audio-precheck.py")
    hooks = archive_hooks if archive_hooks is not None else ap.load_archive_hooks()
    results = [score_draft(p, ap=ap, archive_hooks=hooks) for p in draft_paths]
    results.sort(key=lambda r: (-r["score"], len(r.get("warnings", [])), r["name"]))
    top1 = results[0] if results else None
    runner_up = results[1] if len(results) > 1 else None
    return {"ranked": results, "top1": top1, "runner_up": runner_up}


def format_scorecard(res):
    lines = [
        "## Bảng Chấm Đấu Trường Đa Kịch Bản (`script-arena.py`, F3)",
        "",
        "| Hạng | Bản nháp | Beat | Âm tiết | Ước (s) | Điểm nhịp & cảm xúc | Cảnh báo |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for i, r in enumerate(res["ranked"], 1):
        wc = ", ".join(r.get("warning_codes") or []) or "✔ sạch"
        lines.append(f"| #{i} | `{r['name']}` | {r.get('beats_count', 0)} | {r.get('total_syllables', 0)} | {r.get('estimated_total_s', 0)}s | **{r['score']}** | {wc} |")
    lines += [
        "",
        "### Hướng dẫn Giám khảo Độc lập (`Tournament Judge`)",
        "1. Đọc song song các bản trên cùng 1 Anchor đã duyệt gần nhất (subagent đọc độc lập, không tự chấm).",
        "2. Loại ngay bản vi phạm Tầng 1 (`H1` bịa fact / `H3` sai chất kênh / giọng Bắc trộn Nam).",
        "3. Chọn ra **Top 1 Recommended** (tự nhiên nhất, sóng cảm xúc rõ nhất, CTA đồng cảm nhất) và **1 Á quân khác màu cảm xúc** (ví dụ Top 1 ấm áp chiêm nghiệm vs Á quân cà khịa bắt thóp) để trình Hiệp chọn nhanh tại Gate 1.",
    ]
    return "\n".join(lines) + "\n"


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if a else 2
    def opt(n, d=None):
        return a[a.index(n) + 1] if n in a else d
    cmd = a[0]
    if cmd == "prepare":
        idea = opt("--idea")
        out_dir = opt("--out-dir")
        if not idea or not out_dir:
            print("prepare cần --idea và --out-dir", file=sys.stderr)
            return 2
        archs = SOUL_ARCHETYPES if "--soul" in a else (opt("--archetypes").split(",") if opt("--archetypes") else DEFAULT_ARCHETYPES)
        fl_path = opt("--fact-lock")
        fl_txt = Path(fl_path).read_text(encoding="utf-8") if fl_path and Path(fl_path).exists() else None
        written = prepare_arena(
            idea=idea,
            out_dir=out_dir,
            archetypes=archs,
            channel=opt("--channel", "hi"),
            topic=opt("--topic"),
            trend=opt("--trend"),
            fact_lock_text=fl_txt,
            clip=opt("--clip"),
        )
        if "--json" in a:
            print(json.dumps(written, ensure_ascii=False, indent=1))
        else:
            print(f"script-arena prepare: đã tạo {len(written)} bản brief Pure-Voice tại {out_dir}")
            for w in written:
                print(f"  - Writer {w['label']} [{w['archetype']}] ({w['color']}) → {w['path']}")
        return 0
    if cmd == "score":
        drafts = []
        if opt("--drafts"):
            drafts = [Path(x.strip()) for x in opt("--drafts").split(",") if x.strip()]
        elif opt("--dir"):
            drafts = sorted(Path(opt("--dir")).glob("draft-*.md"))
        if not drafts:
            print("score cần --dir <arena_dir> hoặc --drafts a.md,b.md,c.md", file=sys.stderr)
            return 2
        res = score_arena(drafts)
        if "--json" in a:
            print(json.dumps(res, ensure_ascii=False, indent=1))
        else:
            md = format_scorecard(res)
            if opt("--out"):
                Path(opt("--out")).write_text(md, encoding="utf-8")
                print(f"→ {opt('--out')}")
            else:
                print(md)
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
