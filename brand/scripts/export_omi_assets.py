#!/usr/bin/env python3
"""Export all Omi form × mood SVGs and PNGs from the locked design language.

Source of truth: design-system/oneup/pages/omi-bond.md + omi-emotion.md
Visual logic mirrors prototype/oneup-journey (circle face + ornaments).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import cairosvg
except ImportError:
    print("Install cairosvg: pip install cairosvg", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]  # brand/
OUT = ROOT / "omi-exports"
ASSETS = ROOT.parents[2] / "OneUp" / "Resources" / "Assets.xcassets"

FORMS = ("seed", "companion", "guide", "anchor")
MOODS = (
    "idle",
    "wave",
    "think",
    "quiet",
    "listen",
    "celebrate",
    "sleep",
    "proud",
    "spark",
    "blush",
    "worry",
    "cheer",
)

# App imageset names (PascalCase). "suggest" kept for legacy OmiPose.
APP_MOOD_MAP = {
    "idle": "OmiIdle",
    "suggest": "OmiSuggest",  # alias of think
    "think": "OmiThink",
    "quiet": "OmiQuiet",
    "celebrate": "OmiCelebrate",
    "wave": "OmiWave",
    "listen": "OmiListen",
    "sleep": "OmiSleep",
    "proud": "OmiProud",
    "spark": "OmiSpark",
    "blush": "OmiBlush",
    "worry": "OmiWorry",
    "cheer": "OmiCheer",
}

PNG_SIZES = (48, 96, 144, 256)


def eyes(mood: str, ink: str) -> str:
    dot = f'<circle cx="17" cy="22" r="1.85" fill="{ink}"/><circle cx="31" cy="22" r="1.85" fill="{ink}"/>'
    closed = f'<path d="M14.5 22c1.2-1.4 3.2-1.4 4.4 0M29 22c1.2-1.4 3.2-1.4 4.4 0" fill="none" stroke="{ink}" stroke-width="2" stroke-linecap="round"/>'
    sleep = f'<path d="M14.5 22.5h5M28.5 22.5h5" stroke="{ink}" stroke-width="1.85" stroke-linecap="round"/>'
    worry = f"""<path d="M14 20.2c1.3-1.3 3.4-1.3 4.5 0M29.5 20.2c1.3-1.3 3.4-1.3 4.5 0" fill="none" stroke="{ink}" stroke-width="1.5" stroke-linecap="round"/>
        <circle cx="17" cy="23" r="1.55" fill="{ink}"/><circle cx="31" cy="23" r="1.55" fill="{ink}"/>"""
    # No white highlights — assets are template-tinted.
    listen = f'<circle cx="17" cy="22" r="2.05" fill="{ink}"/><circle cx="31" cy="22" r="2.05" fill="{ink}"/>'
    if mood in ("celebrate", "cheer", "proud"):
        return closed
    if mood == "sleep":
        return sleep
    if mood == "worry":
        return worry
    if mood in ("listen", "spark"):
        return listen
    return dot


def mouth(mood: str, ink: str) -> str:
    d = "M17.5 29.5c2.2 2.4 6.8 2.4 9 0"
    if mood in ("celebrate", "cheer"):
        d = "M15.5 29c3.2 4.4 9.8 4.4 13 0"
    elif mood in ("proud", "blush"):
        d = "M16.5 29.8c2.6 2.9 8 2.9 10.6 0"
    elif mood in ("quiet", "sleep"):
        d = "M19 31h10"
    elif mood == "worry":
        d = "M18.5 31.2c1.6-1.1 5-1.1 6.6 0"
    elif mood == "wave":
        d = "M16.5 29.2c2.6 2.6 8 2.6 10.6 0"
    elif mood == "listen":
        d = "M18.5 30.5h11"
    elif mood == "spark":
        d = "M17.2 29.5c2.4 2.8 7.2 2.8 9.6 0"
    return f'<path d="{d}" fill="none" stroke="{ink}" stroke-width="1.85" stroke-linecap="round"/>'


def body(form: str, ink: str) -> str:
    face = f'<circle cx="24" cy="24" r="15.5" fill="none" stroke="{ink}" stroke-width="1.85"/>'
    if form == "seed":
        return face
    if form == "companion":
        return f"""{face}
          <path d="M5.5 18.5c1.2-2.8 3.4-3.6 4.6-2.2" fill="none" stroke="{ink}" stroke-width="1.5" stroke-linecap="round" opacity=".7"/>
          <path d="M42.5 18.5c-1.2-2.8-3.4-3.6-4.6-2.2" fill="none" stroke="{ink}" stroke-width="1.5" stroke-linecap="round" opacity=".7"/>
          <circle cx="7.2" cy="22.5" r="1.2" fill="{ink}" opacity=".45"/>
          <circle cx="40.8" cy="22.5" r="1.2" fill="{ink}" opacity=".45"/>"""
    if form == "guide":
        return f"""<circle cx="24" cy="24" r="18.2" fill="none" stroke="{ink}" stroke-width="1.15" opacity=".28"/>
          {face}
          <path d="M16 6.5c2.4-1.6 5.4-2.4 8-2.4s5.6.8 8 2.4" fill="none" stroke="{ink}" stroke-width="1.5" stroke-linecap="round"/>
          <circle cx="24" cy="4.2" r="1.7" fill="{ink}"/>
          <circle cx="18.2" cy="6.2" r="1.1" fill="{ink}" opacity=".55"/>
          <circle cx="29.8" cy="6.2" r="1.1" fill="{ink}" opacity=".55"/>"""
    return f"""<circle cx="24" cy="24" r="21" fill="none" stroke="{ink}" stroke-width="1" opacity=".22"/>
        <circle cx="24" cy="24" r="18.4" fill="none" stroke="{ink}" stroke-width="1.25" opacity=".4"/>
        {face}
        <path d="M24 2.2l1.1 2.2 2.4.4-1.7 1.7.4 2.4L24 7.6l-2.2 1.3.4-2.4-1.7-1.7 2.4-.4Z" fill="{ink}"/>
        <path d="M8.5 10.5l.7 1.4 1.5.3-1.1 1.1.3 1.5-1.4-.7-1.4.7.3-1.5-1.1-1.1 1.5-.3Z" fill="{ink}" opacity=".7"/>
        <path d="M39.5 10.5l.7 1.4 1.5.3-1.1 1.1.3 1.5-1.4-.7-1.4.7.3-1.5-1.1-1.1 1.5-.3Z" fill="{ink}" opacity=".7"/>
        <circle cx="24" cy="43.2" r="1.35" fill="{ink}" opacity=".5"/>
        <circle cx="5.8" cy="24" r="1.1" fill="{ink}" opacity=".35"/>
        <circle cx="42.2" cy="24" r="1.1" fill="{ink}" opacity=".35"/>"""


def extras(mood: str, form: str, ink: str) -> str:
    parts: list[str] = []
    form_id = {"seed": 1, "companion": 2, "guide": 3, "anchor": 4}[form]
    if mood == "blush" or mood in ("celebrate", "cheer"):
        cheek_op = "0.55" if form_id >= 2 else ("0.35" if mood == "blush" else "0")
    else:
        cheek_op = "0.22" if form_id >= 2 else "0"
    if float(cheek_op) > 0:
        parts.append(
            f'<ellipse cx="11.5" cy="27.5" rx="3.2" ry="2" fill="{ink}" opacity="{cheek_op}"/>'
            f'<ellipse cx="36.5" cy="27.5" rx="3.2" ry="2" fill="{ink}" opacity="{cheek_op}"/>'
        )
    if mood == "think":
        parts.append(
            f"""<circle cx="37.5" cy="10.5" r="2.1" fill="{ink}"/>
            <circle cx="41.2" cy="6.8" r="1.5" fill="{ink}"/>
            <circle cx="43.5" cy="3.6" r="1" fill="{ink}"/>"""
        )
        parts.append(
            f'<path d="M13.5 17.2c1.5-1 4-1 5.4 0M29 17.2c1.5-1 4-1 5.4 0" fill="none" stroke="{ink}" stroke-width="1.35" stroke-linecap="round" opacity=".55"/>'
        )
    if mood in ("celebrate", "cheer", "spark"):
        parts.append(
            f"""<g>
            <path d="M7 9l1.15 2.3 2.35.4-1.7 1.65.4 2.35L7 14.5l-2.2 1.2.4-2.35-1.7-1.65 2.35-.4Z" fill="{ink}"/>
            <path d="M40 7.5l.95 1.9 1.95.35-1.4 1.35.35 1.95L40 12l-1.85 1.05.35-1.95-1.4-1.35 1.95-.35Z" fill="{ink}"/>
            <path d="M41 29.5l.7 1.4 1.45.25-1.05 1 .25 1.45L41 32.5l-1.35.8.25-1.45-1.05-1 1.45-.25Z" fill="{ink}"/>
            </g>"""
        )
    if mood == "wave":
        parts.append(
            f'<path d="M38.5 15.5c2.2-3.2 5.2-2.4 4.8 1.3-.25 2-1.85 2.8-3.3 2" fill="none" stroke="{ink}" stroke-width="1.75" stroke-linecap="round"/>'
        )
    if mood == "sleep":
        parts.append(
            f"""<text x="35" y="11" font-size="8" font-weight="700" fill="{ink}" opacity=".5" font-family="system-ui,sans-serif">z</text>
            <text x="39.5" y="6.5" font-size="6" font-weight="700" fill="{ink}" opacity=".35" font-family="system-ui,sans-serif">z</text>"""
        )
    return "\n".join(parts)


def svg_markup(form: str, mood: str, *, ink: str = "#111111") -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48" role="img" aria-label="Omi {form} {mood}">
  {body(form, ink)}
  {eyes(mood, ink)}
  {mouth(mood, ink)}
  {extras(mood, form, ink)}
</svg>
"""


def write_imageset(name: str, png_1x: Path, png_2x: Path, png_3x: Path) -> None:
    folder = ASSETS / f"{name}.imageset"
    folder.mkdir(parents=True, exist_ok=True)
    for src, dest in (
        (png_1x, folder / f"{name}.png"),
        (png_2x, folder / f"{name}@2x.png"),
        (png_3x, folder / f"{name}@3x.png"),
    ):
        dest.write_bytes(src.read_bytes())
    contents = {
        "images": [
            {"filename": f"{name}.png", "idiom": "universal", "scale": "1x"},
            {"filename": f"{name}@2x.png", "idiom": "universal", "scale": "2x"},
            {"filename": f"{name}@3x.png", "idiom": "universal", "scale": "3x"},
        ],
        "info": {"author": "xcode", "version": 1},
        "properties": {"template-rendering-intent": "template"},
    }
    (folder / "Contents.json").write_text(json.dumps(contents, indent=2) + "\n", encoding="utf-8")


def build_showcase(svg_root: Path) -> None:
    cards = []
    for form in FORMS:
        row = []
        for mood in MOODS:
            rel = f"svg/{form}/{mood}.svg"
            row.append(
                f'<figure><img src="{rel}" width="72" height="72" alt="{form} {mood}"/>'
                f"<figcaption>{mood}</figcaption></figure>"
            )
        cards.append(f'<section><h2>{form}</h2><div class="grid">{"".join(row)}</div></section>')
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>OneUp — Omi asset export</title>
  <style>
    :root {{ --bg:#F7F7F5; --ink:#111; --muted:#6B6B6B; --border:#E8E8E6; }}
    body {{ margin:0; font-family: ui-sans-serif, system-ui, sans-serif; background:var(--bg); color:var(--ink); }}
    .wrap {{ max-width: 960px; margin: 0 auto; padding: 40px 20px 80px; }}
    h1 {{ font-size: 1.6rem; margin: 0 0 8px; }}
    p {{ color: var(--muted); margin: 0 0 28px; }}
    h2 {{ font-size: 0.85rem; letter-spacing: .08em; text-transform: uppercase; margin: 28px 0 12px; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(88px, 1fr)); gap: 12px; }}
    figure {{ margin:0; background:#fff; border:1px solid var(--border); border-radius:14px; padding:14px 8px; text-align:center; }}
    figcaption {{ font-size: 11px; color: var(--muted); margin-top: 8px; }}
    img {{ display:block; margin:0 auto; }}
  </style>
</head>
<body>
  <div class="wrap">
    <h1>Omi exports</h1>
    <p>4 forms × 12 moods · SVG + PNG · ink template assets</p>
    {"".join(cards)}
  </div>
</body>
</html>
"""
    (OUT / "index.html").write_text(html, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Export all Omi assets")
    parser.add_argument("--skip-app", action="store_true", help="Do not update Xcode imagesets")
    parser.add_argument("--form", choices=FORMS, help="Export a single form only")
    args = parser.parse_args()

    forms = (args.form,) if args.form else FORMS
    svg_root = OUT / "svg"
    png_root = OUT / "png"
    OUT.mkdir(parents=True, exist_ok=True)

    count_svg = 0
    count_png = 0

    for form in forms:
        for mood in MOODS:
            svg_dir = svg_root / form
            svg_dir.mkdir(parents=True, exist_ok=True)
            svg_path = svg_dir / f"{mood}.svg"
            markup = svg_markup(form, mood)
            svg_path.write_text(markup, encoding="utf-8")
            count_svg += 1

            png_dir = png_root / form / mood
            png_dir.mkdir(parents=True, exist_ok=True)
            for size in PNG_SIZES:
                out_png = png_dir / f"{mood}-{size}.png"
                cairosvg.svg2png(
                    bytestring=markup.encode("utf-8"),
                    write_to=str(out_png),
                    output_width=size,
                    output_height=size,
                )
                count_png += 1

    build_showcase(svg_root)

    readme = f"""# Omi asset exports

Generated by `brand/scripts/export_omi_assets.py`.

## Matrix

- **Forms:** {", ".join(FORMS)}
- **Moods:** {", ".join(MOODS)}
- **Total:** {len(FORMS) * len(MOODS)} SVGs · PNGs at {", ".join(str(s) for s in PNG_SIZES)}px

## Layout

```
omi-exports/
  index.html          # visual grid
  svg/{{form}}/{{mood}}.svg
  png/{{form}}/{{mood}}/{{mood}}-{{size}}.png
```

## App imagesets

Seed-form PNGs (48 / 96 / 144) sync into `AppIcon`-adjacent Omi* imagesets as **template** (tint with `Color.ou.ink`).

Form ornaments for Companion+ stay in this export tree until SwiftUI draws forms live.
"""
    (OUT / "README.md").write_text(readme, encoding="utf-8")

    if not args.skip_app:
        # Always sync seed form into xcassets (default companion look until Bond forms ship in UI).
        seed_png = png_root / "seed"
        for mood_key, imageset in APP_MOOD_MAP.items():
            src_mood = "think" if mood_key == "suggest" else mood_key
            base = seed_png / src_mood
            write_imageset(
                imageset,
                base / f"{src_mood}-48.png",
                base / f"{src_mood}-96.png",
                base / f"{src_mood}-144.png",
            )
        print(f"Updated {len(APP_MOOD_MAP)} imagesets under {ASSETS}")

    print(f"Exported {count_svg} SVGs + {count_png} PNGs → {OUT}")
    print(f"Showcase: {OUT / 'index.html'}")


if __name__ == "__main__":
    main()
