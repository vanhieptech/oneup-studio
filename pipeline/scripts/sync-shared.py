#!/usr/bin/env python3
"""rule-65 / L-034: shared library → derived runtime copies (gitignored). Never edit the copies.
Canonical sources (single copy in git):
  brand/fonts/*            → video-engine/public/fonts/, <explainer>/fonts/ (BVP ttf only)
  brand/logos/05-pair-plus.svg → video-engine/public/brand/{logo,pair-plus}.svg, <explainer>/logo.svg
Explainer dirs = any folder under content/ or templates/ containing index.html.tpl or hyperframes.json.
Usage: sync-shared.py [explainer_dir ...]   (no args: all)"""
import shutil, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
FONTS = ROOT / "brand/fonts"; LOGO = ROOT / "brand/logos/05-pair-plus.svg"
def cp(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if not dst.exists() or dst.read_bytes() != src.read_bytes(): shutil.copyfile(src, dst)
def sync_engine():
    for f in FONTS.iterdir():
        if f.suffix in (".ttf", ".txt"): cp(f, ROOT / "video-engine/public/fonts" / f.name)
    for n in ("logo.svg", "pair-plus.svg"): cp(LOGO, ROOT / "video-engine/public/brand" / n)
def sync_explainer(d):
    d = Path(d)
    for w in ("Bold", "SemiBold", "Regular"): cp(FONTS / f"BeVietnamPro-{w}.ttf", d / "fonts" / f"BeVietnamPro-{w}.ttf")
    cp(LOGO, d / "logo.svg")
def explainers():
    out = set()
    for base in ("content", "templates"):
        for p in (ROOT / base).rglob("hyperframes.json"):
            if "node_modules" not in p.parts: out.add(p.parent)
    return sorted(out)
if __name__ == "__main__":
    sync_engine()
    for d in (sys.argv[1:] or explainers()): sync_explainer(d)
    print("sync-shared: ok")
