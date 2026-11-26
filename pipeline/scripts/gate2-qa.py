#!/usr/bin/env python3
"""Gate 2 Multimodal Video QA wrapper (rule-34): inspect 720p MP4 + spec.json with Antigravity / Gemini CLI.

  gate2-qa.py <clip_dir_or_video> [--spec <spec.json>] [--video <720p.mp4>]
              [--engine auto|agy|gemini] [--model <model>] [--out <report.md>] [--dry-run]

Finds the newest 720p render of the clip (media/clips/<clip>/*720*.mp4, <clip>/final/out/*720*.mp4,
or media/channels/vanhiep-tech/<clip>/*720*.mp4), probes real duration via ffprobe (L-099 < 300s),
packages the video + spec.json + skills/video-qa/SKILL.md prompt, runs `agy -p` (or `gemini -p`
fallback, matching teardown.py), and writes `<clip>/final/gate2-qa-report.md` with repo front-matter.
"""
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65
from duration_policy import HARD_LIMIT_SECONDS, duration_status

SKILL_MD = P.ROOT / "skills/video-qa/SKILL.md"


def load_prompt(skill_path=SKILL_MD):
    t = Path(skill_path).read_text(encoding="utf-8")
    m = re.search(r"<<<PROMPT\n(.*?)\nPROMPT>>>", t, re.S)
    if not m:
        raise SystemExit(f"no <<<PROMPT … PROMPT>>> block in {skill_path}")
    return m.group(1)


def find_video(target, explicit_video=None):
    """Locate the newest 720p MP4 for a clip directory (or return explicit video path)."""
    if explicit_video:
        p = Path(explicit_video)
        return p if p.exists() else None
    t = Path(target)
    if t.is_file():
        return t
    slug = t.name
    search_dirs = [
        P.MEDIA_CLIPS / slug,
        t / "final/out",
        P.MEDIA / "channels/vanhiep-tech" / slug,
        t,
    ]
    cands_720, cands_any = [], []
    for d in search_dirs:
        if not d.exists():
            continue
        for f in d.glob("*.mp4"):
            if "720" in f.name.lower():
                cands_720.append(f)
            else:
                cands_any.append(f)
    if cands_720:
        return max(cands_720, key=lambda f: f.stat().st_mtime)
    if cands_any:
        return max(cands_any, key=lambda f: f.stat().st_mtime)
    return None


def find_spec(target, explicit_spec=None):
    if explicit_spec:
        p = Path(explicit_spec)
        return p if p.exists() else None
    t = Path(target)
    base = t.parent if t.is_file() else t
    for rel in ("final/spec.json", "spec.json", "capcut-spec.json", "final/capcut-spec.json"):
        p = base / rel
        if p.exists():
            return p
    return None


def probe_video(video_path):
    """Return {duration_s, width, height} via ffprobe (best-effort)."""
    try:
        r = subprocess.run(
            [P.FFPROBE_BIN, "-v", "error", "-select_streams", "v:0",
             "-show_entries", "stream=width,height:format=duration", "-of", "json", str(video_path)],
            capture_output=True, text=True, timeout=30,
        )
        d = json.loads(r.stdout or "{}")
        dur = float((d.get("format") or {}).get("duration") or 0)
        st = (d.get("streams") or [{}])[0]
        return {"duration_s": round(dur, 2), "width": st.get("width"), "height": st.get("height")}
    except Exception:
        return {"duration_s": None, "width": None, "height": None}


def detect_channel(target, spec_path):
    s = str(target) + " " + str(spec_path or "")
    return "vanhiep-tech" if ("vanhiep-tech" in s or "capcut-spec" in s or "vht-" in s) else "hi-oneup"


def build_prompt(video_path, spec_path, probe, channel):
    base = load_prompt()
    dur = probe.get("duration_s")
    dur_note = f"{dur}s" if dur is not None else "chưa đo được"
    if dur is not None and channel == "hi-oneup":
        st = duration_status(dur)
        dur_note += f" (L-099 < {int(HARD_LIMIT_SECONDS)}s: {st.upper()})"
    elif dur is not None and channel == "vanhiep-tech":
        dur_note += " (mục tiêu @vanhiep.tech: 45–90s)"

    parts = [
        base,
        "",
        "---",
        f"Kênh: @{channel.replace('-', '.')}",
        f"Độ phân giải đo từ ffprobe: {probe.get('width') or '?'}x{probe.get('height') or '?'} · Thời lượng thực tế: {dur_note}",
        f"File video 720p cần QA: @{os.path.abspath(video_path)}",
    ]
    if spec_path:
        parts.append(f"File spec đối chiếu: @{os.path.abspath(spec_path)}")
    else:
        parts.append("File spec đối chiếu: (không tìm thấy spec.json — chỉ QA trực tiếp trên video)")
    return "\n".join(parts)


def run_agy(prompt, add_dirs, model):
    if not P.AGY_BIN or not os.path.exists(P.AGY_BIN):
        raise SystemExit("agy CLI not found (AGY_BIN)")
    args = [P.AGY_BIN, "-p", prompt, "--output-format", "json", "--mode", "plan", "--print-timeout", "900s"]
    for d in dict.fromkeys(add_dirs):
        args += ["--add-dir", d]
    if model:
        args += ["--model", model]
    r = subprocess.run(args, capture_output=True, text=True, timeout=960, cwd=str(P.ROOT))
    try:
        out = json.loads(r.stdout.strip().splitlines()[-1])
    except (json.JSONDecodeError, IndexError):
        out = {"status": "ERROR", "error": (r.stderr or r.stdout).strip()[-500:]}
    if out.get("status") == "ERROR" or out.get("error"):
        print(f"agy error: {out.get('error')}", file=sys.stderr)
        sys.exit(3)
    return {
        "response": out.get("response", ""),
        "engine": "agy",
        "model": out.get("model") or model or "agy-default",
    }


def run_gemini(prompt, add_dirs, model):
    if not P.GEMINI_BIN:
        raise SystemExit("gemini CLI not found (GEMINI_BIN)")
    args = [P.GEMINI_BIN, "-p", prompt, "-o", "json", "--approval-mode", "plan"]
    for d in dict.fromkeys(add_dirs):
        args += ["--include-directories", d]
    if model:
        args += ["-m", model]
    env = dict(os.environ)
    key = P.tools_env("GEMINI_API_KEY")
    if key:
        env["GEMINI_API_KEY"] = key
    r = subprocess.run(args, capture_output=True, text=True, timeout=900, cwd=str(P.ROOT), env=env)
    try:
        out = json.loads(r.stdout)
    except json.JSONDecodeError:
        out = {"response": r.stdout, "error": {"message": r.stderr.strip()[:500]} if r.returncode else None}
    if out.get("error"):
        print(f"gemini error: {out['error'].get('message', out['error'])}", file=sys.stderr)
        sys.exit(3)
    return {"response": out.get("response", ""), "engine": "gemini", "model": model or "gemini-default"}


def run_engine(prompt, add_dirs, model, engine="auto"):
    if engine == "agy" or (engine == "auto" and P.AGY_BIN and os.path.exists(P.AGY_BIN)):
        return run_agy(prompt, add_dirs, model)
    return run_gemini(prompt, add_dirs, model)


def parse_qa_verdict(text, duration_s=None, channel="hi-oneup"):
    """Determine final Gate 2 QA verdict, enforcing deterministic L-099 (<300s) hard cap."""
    if duration_s is not None and channel == "hi-oneup" and duration_status(duration_s) == "error":
        return "NEEDS_FIX"
    m = re.findall(r"QA_VERDICT\s*:\s*(PASS|NEEDS_FIX)", text or "", re.I)
    return m[-1].upper() if m else "NEEDS_FIX"


def render_report(clip_name, video_path, spec_path, probe, channel, engine_out, date_str):
    dur = probe.get("duration_s")
    l099_fail = dur is not None and channel == "hi-oneup" and duration_status(dur) == "error"
    verdict = parse_qa_verdict(engine_out.get("response", ""), dur, channel)
    rel_vid = str(Path(video_path).resolve().relative_to(P.ROOT)) if P.ROOT in Path(video_path).resolve().parents else str(video_path)
    rel_spec = (str(Path(spec_path).resolve().relative_to(P.ROOT)) if spec_path and P.ROOT in Path(spec_path).resolve().parents else str(spec_path or "none"))
    safe_id = re.sub(r"[^a-z0-9-]+", "-", clip_name.lower()).strip("-") or "clip"

    lines = [
        "---",
        f'title: "Gate 2 Multimodal Video QA — {clip_name}"',
        f"date: {date_str}",
        f"id: gate2-qa.{safe_id}",
        "type: qa-report",
        "status: draft",
        f"updated: {date_str}",
        f"tags: [qa, gate-2, rule-34, {channel}]",
        f'source: "{rel_vid} · {rel_spec} · {engine_out.get("engine")} ({engine_out.get("model")})"',
        f"qa_verdict: {verdict}",
        "---",
        f"# Gate 2 Multimodal Video QA — `{clip_name}`",
        "",
        f"- **Video:** `{rel_vid}` ({probe.get('width') or '?'}×{probe.get('height') or '?'}, **{dur if dur is not None else '?'}s**)",
        f"- **Spec:** `{rel_spec}`",
        f"- **Engine:** `{engine_out.get('engine')}` · model `{engine_out.get('model')}`",
        f"- **L-099 duration check:** {'✖ FAIL (≥ 300s!)' if l099_fail else '✔ OK (< 300s)' if dur is not None else 'ℹ chưa đo'}",
        f"- **Final Verdict:** **{verdict}**",
        "",
        engine_out.get("response", "").strip(),
        "",
    ]
    return "\n".join(lines)


def resolve_out_path(target, explicit_out=None):
    if explicit_out:
        return Path(explicit_out)
    t = Path(target)
    if t.is_dir():
        if (t / "final").exists():
            return t / "final/gate2-qa-report.md"
        return t / "gate2-qa-report.md"
    return t.parent / "gate2-qa-report.md"


def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if a else 2
    def opt(n, d=None):
        return a[a.index(n) + 1] if n in a else d
    target = next((x for x in a if not x.startswith("-")), None)
    if not target:
        print(__doc__)
        return 2
    video = find_video(target, opt("--video"))
    if not video:
        print(f"✖ không tìm thấy file video 720p cho {target} (kiểm tra media/clips/ hoặc final/out/)", file=sys.stderr)
        return 2
    spec = find_spec(target, opt("--spec"))
    probe = probe_video(video)
    channel = detect_channel(target, spec)
    prompt = build_prompt(video, spec, probe, channel)
    out_path = resolve_out_path(target, opt("--out"))
    clip_name = Path(target).stem if Path(target).is_file() else Path(target).name

    if "--dry-run" in a:
        print(f"clip:    {clip_name} (@{channel.replace('-', '.')})")
        print(f"video:   {video} ({probe.get('width')}x{probe.get('height')}, {probe.get('duration_s')}s)")
        print(f"spec:    {spec or '(none)'}")
        print(f"out:     {out_path}")
        print(f"engine:  {opt('--engine', 'auto')} (agy={'ok' if P.AGY_BIN and os.path.exists(P.AGY_BIN) else 'missing'})")
        return 0

    add_dirs = [os.path.dirname(os.path.abspath(video))]
    if spec:
        add_dirs.append(os.path.dirname(os.path.abspath(spec)))
    engine_out = run_engine(prompt, add_dirs, opt("--model"), opt("--engine", "auto"))
    report = render_report(clip_name, video, spec, probe, channel, engine_out, dt.date.today().isoformat())
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report, encoding="utf-8")
    verdict = parse_qa_verdict(engine_out.get("response", ""), probe.get("duration_s"), channel)
    print(f"gate2-qa → {out_path} · {verdict} ({probe.get('duration_s')}s)")
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
