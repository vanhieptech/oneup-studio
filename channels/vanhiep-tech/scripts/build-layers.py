#!/usr/bin/env python3
"""1-command local Mac build + cache + QA for @vanhiep.tech HyperFrames layers.

Pipeline per layer:
  1. sync-shared.py (fonts + brand/tokens.css)
  2. Content-hash check (*.sha256 beside rendered .mov/.mp4 in media/channels/vanhiep-tech/<clip>/)
  3. On cache miss (or --no-cache): npx --yes hyperframes@<HF_VER> check && render (--format mov for ov-*, mp4 for cu-*)
  4. Automated QA gate via channels/vanhiep-tech/scripts/check-layer.py

Usage:
  python3 channels/vanhiep-tech/scripts/build-layers.py channels/vanhiep-tech/clips/vht-20261107-oauth-control-plane
  python3 channels/vanhiep-tech/scripts/build-layers.py <clip-dir> --layer ov-d01 [--no-cache] [--check-only]
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "pipeline"))
import paths as P  # noqa: E402

SKIP_DIRS = {"node_modules", ".hyperframes", "fonts", ".git", "__pycache__"}


def layer_hash(layer_dir: Path) -> str:
    h = hashlib.sha256()
    h.update(P.HYPERFRAMES_VERSION.encode())
    for root, dirs, files in os.walk(layer_dir):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for fn in sorted(files):
            if fn.endswith((".sha256", ".log")):
                continue
            p = Path(root) / fn
            h.update(p.relative_to(layer_dir).as_posix().encode())
            h.update(p.read_bytes())
    return h.hexdigest()[:16]


def resolve_output(layer_dir: Path) -> tuple[Path, str]:
    fmt = "mov" if layer_dir.name.startswith("ov-") else "mp4"
    pkg = layer_dir / "package.json"
    if pkg.is_file():
        try:
            cmd = json.loads(pkg.read_text(encoding="utf-8")).get("scripts", {}).get("render", "")
            m = re.search(r"-o\s+(\S+\.(?:mov|mp4))\b", cmd)
            if m:
                return (layer_dir / m.group(1)).resolve(), fmt
        except Exception:
            pass
    clip_id = layer_dir.parent.parent.name
    return ROOT / "media" / "channels" / "vanhiep-tech" / clip_id / f"{layer_dir.name}.{fmt}", fmt


def run_env() -> dict[str, str]:
    ff_dir = os.path.dirname(P.FFMPEG_BIN) if os.path.isabs(P.FFMPEG_BIN) else ""
    extra = ":".join(x for x in (P.NODE_BIN, ff_dir) if x)
    return dict(os.environ, PATH=(extra + ":" if extra else "") + os.environ.get("PATH", ""))


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print("Usage: build-layers.py <clip-dir> [--layer <id>] [--no-cache] [--check-only]")
        return 2
    clip_dir = Path(args[0]).resolve()
    only = args[args.index("--layer") + 1].split(",") if "--layer" in args else None
    no_cache = "--no-cache" in args
    check_only = "--check-only" in args

    layers_root = clip_dir / "layers"
    if not layers_root.is_dir():
        sys.stderr.write(f"No layers/ directory in {clip_dir}\n")
        return 1

    layers = sorted(d for d in layers_root.iterdir() if d.is_dir() and (d / "index.html").is_file())
    if only:
        layers = [d for d in layers if d.name in only]
    if not layers:
        sys.stderr.write("No matching layers found.\n")
        return 1

    # 1. Sync fonts + brand tokens.css
    subprocess.run([sys.executable, str(ROOT / "pipeline/scripts/sync-shared.py"), *[str(d) for d in layers]], check=True)

    env = run_env()
    hf = f"hyperframes@{P.HYPERFRAMES_VERSION}"
    for ld in layers:
        out_path, fmt = resolve_output(ld)
        sig_path = Path(str(out_path) + ".sha256")
        key = layer_hash(ld)
        if not no_cache and out_path.is_file() and sig_path.is_file() and sig_path.read_text().strip() == key:
            print(f"[cache hit] {ld.name} -> {out_path.relative_to(ROOT)} ({key[:8]})")
            continue
        if check_only:
            print(f"[check] {ld.name} ({hf})")
            subprocess.run(["npx", "--yes", hf, "check"], cwd=ld, env=env, check=True)
            continue
        out_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"[build] {ld.name} ({hf}, --format {fmt}) -> {out_path.relative_to(ROOT)}")
        subprocess.run(["npx", "--yes", hf, "check"], cwd=ld, env=env, check=True)
        subprocess.run(["npx", "--yes", hf, "render", "--format", fmt, "-o", str(out_path), "."], cwd=ld, env=env, check=True)
        sig_path.write_text(key + "\n", encoding="utf-8")

    # 2. Run automated alpha/CSS QA gate on ov-* layers
    ov_layers = [str(d) for d in layers if d.name.startswith("ov-")]
    if ov_layers and not check_only:
        subprocess.run([sys.executable, str(ROOT / "channels/vanhiep-tech/scripts/check-layer.py"), *ov_layers], check=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
