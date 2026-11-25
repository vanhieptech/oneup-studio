#!/usr/bin/env python3
"""Automated QA gate for @vanhiep.tech overlay layers (DL-069, DL-070).

Checks each ov-* layer in a clip dir (or given layer dirs):
  1. Banned CSS in HTML/CSS: box-shadow, text-shadow, filter:blur, drop-shadow, backdrop-filter
  2. Rendered ProRes .mov has alpha pixel format (yuva*)
  3. Mid-frame 4 corners are fully transparent (alpha == 0)
  4. Soft-alpha budget: non-scrim semi-transparent pixels (0 < a < 250) < 3.0%
     (Uniform hard-scrim plate opacity, e.g. 0.82 -> alpha ~209 +- 6, is allowed per DL-070.)

Usage:
  python3 channels/vanhiep-tech/scripts/check-layer.py channels/vanhiep-tech/clips/vht-20261107-oauth-control-plane
  python3 channels/vanhiep-tech/scripts/check-layer.py .../layers/ov-d01 .../layers/ov-hook
"""
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "pipeline"))
import paths as P  # noqa: E402

BANNED_CSS = re.compile(
    r"(box-shadow|text-shadow|filter\s*:\s*[^;{}]*blur|drop-shadow|backdrop-filter)",
    re.I,
)
STRIP_COMMENTS = re.compile(r"<!--.*?-->|/\*.*?\*/", re.S)


def resolve_mov(layer_dir: Path) -> Path | None:
    pkg = layer_dir / "package.json"
    if pkg.is_file():
        try:
            render_cmd = json.loads(pkg.read_text(encoding="utf-8")).get("scripts", {}).get("render", "")
            m = re.search(r"-o\s+(\S+\.mov)\b", render_cmd)
            if m:
                cand = (layer_dir / m.group(1)).resolve()
                if cand.is_file():
                    return cand
        except Exception:
            pass
    clip_id = layer_dir.parent.parent.name if layer_dir.parent.name == "layers" else ""
    if clip_id:
        cand = ROOT / "media" / "channels" / "vanhiep-tech" / clip_id / f"{layer_dir.name}.mov"
        if cand.is_file():
            return cand
    return None


def detect_hard_scrim_alpha(html: str) -> int | None:
    if 'data-backdrop="hard-scrim"' not in html and "backdrop: hard-scrim" not in html:
        return None
    m = re.search(r"#scrim[^{]*\{[^}]*opacity\s*:\s*([0-9.]+)", html, re.S)
    op = float(m.group(1)) if m else 0.82
    return round(op * 255)


def check_one(layer_dir: Path) -> tuple[bool, str]:
    name = layer_dir.name
    errs: list[str] = []

    html_path = layer_dir / "index.html"
    if not html_path.is_file():
        return False, f"✖ {name}: missing index.html"
    raw_html = html_path.read_text(encoding="utf-8", errors="ignore")
    scrim_alpha = detect_hard_scrim_alpha(raw_html)

    # 1. Banned CSS in HTML + local CSS files (excluding shared tokens.css comments)
    for src_path in sorted(list(layer_dir.glob("*.html")) + list(layer_dir.glob("*.css"))):
        cleaned = STRIP_COMMENTS.sub("", src_path.read_text(encoding="utf-8", errors="ignore"))
        hits = sorted({m.group(1).lower() for m in BANNED_CSS.finditer(cleaned)})
        if hits:
            errs.append(f"banned CSS in {src_path.name}: {', '.join(hits)}")

    # 2. Check rendered MOV
    mov = resolve_mov(layer_dir)
    if mov is None:
        errs.append("rendered .mov not found (render with --format mov first)")
        return False, f"✖ {name}: " + "; ".join(errs)

    probe = subprocess.run(
        [
            P.FFPROBE_BIN,
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=pix_fmt,width,height:format=duration",
            "-of",
            "json",
            str(mov),
        ],
        capture_output=True,
        text=True,
    )
    if probe.returncode != 0:
        return False, f"✖ {name}: ffprobe failed on {mov.name}: {probe.stderr.strip()}"

    info = json.loads(probe.stdout or "{}")
    stream = (info.get("streams") or [{}])[0]
    pix_fmt = stream.get("pix_fmt", "")
    dur = float((info.get("format") or {}).get("duration") or 3.0)
    if "yuva" not in pix_fmt and "rgba" not in pix_fmt and "argb" not in pix_fmt:
        errs.append(f"pix_fmt={pix_fmt!r} has no alpha (expected yuva*)")

    # 3 & 4. Extract mid-frame and inspect RGBA pixels
    ss = min(1.5, max(0.2, dur * 0.5))
    try:
        from PIL import Image
    except ImportError:
        return False, f"✖ {name}: Pillow (PIL) is required to inspect alpha frames"

    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tf:
        png_path = tf.name
    try:
        r = subprocess.run(
            [P.FFMPEG_BIN, "-y", "-loglevel", "error", "-ss", f"{ss:.2f}", "-i", str(mov), "-frames:v", "1", png_path],
            capture_output=True,
            text=True,
        )
        if r.returncode != 0 or not os.path.exists(png_path):
            errs.append(f"ffmpeg frame extract failed: {r.stderr.strip()}")
            return False, f"✖ {name}: " + "; ".join(errs)

        im = Image.open(png_path).convert("RGBA")
        w, h = im.size
        corners = [im.getpixel((0, 0))[3], im.getpixel((w - 1, 0))[3], im.getpixel((0, h - 1))[3], im.getpixel((w - 1, h - 1))[3]]
        if any(c != 0 for c in corners):
            errs.append(f"corners not transparent: alpha={corners}")

        px = im.load()
        raw_semi = 0
        non_scrim_semi = 0
        tot = 0
        for y in range(0, h, 2):
            for x in range(0, w, 2):
                a = px[x, y][3]
                tot += 1
                if 0 < a < 250:
                    raw_semi += 1
                    if scrim_alpha is not None and abs(a - scrim_alpha) <= 6:
                        continue
                    non_scrim_semi += 1

        raw_pct = 100.0 * raw_semi / max(1, tot)
        ns_pct = 100.0 * non_scrim_semi / max(1, tot)
        if ns_pct >= 3.0:
            errs.append(f"non-scrim semi-alpha={ns_pct:.2f}% >= 3.0% (soft fog/halo)")
    finally:
        if os.path.exists(png_path):
            os.remove(png_path)

    scrim_note = f"hard-scrim(a≈{scrim_alpha}, raw={raw_pct:.1f}%)" if scrim_alpha is not None else "no-scrim"
    if errs:
        return False, f"✖ {name} ({pix_fmt}, {scrim_note}, non_scrim_semi={ns_pct:.2f}%): " + "; ".join(errs)
    return True, f"✔ {name} ({pix_fmt}, {w}x{h}, corners=0, {scrim_note}, non_scrim_semi={ns_pct:.2f}%)"


def collect_layers(args: list[str]) -> list[Path]:
    layers: list[Path] = []
    for a in args:
        p = Path(a).resolve()
        if (p / "layers").is_dir():
            layers.extend(sorted(d for d in (p / "layers").iterdir() if d.is_dir() and d.name.startswith("ov-")))
        elif p.is_dir() and p.name.startswith("ov-"):
            layers.append(p)
        elif p.is_dir():
            layers.extend(sorted(d for d in p.iterdir() if d.is_dir() and d.name.startswith("ov-")))
    return layers


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: check-layer.py <clip-dir | layer-dir ...>")
        return 2
    layers = collect_layers(sys.argv[1:])
    if not layers:
        print("No ov-* layers found.")
        return 1
    fails = 0
    for ld in layers:
        ok, msg = check_one(ld)
        print(msg)
        if not ok:
            fails += 1
    print(f"\n{len(layers)} overlay layer(s) checked · {fails} failed → {'FAIL' if fails else 'PASS'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
