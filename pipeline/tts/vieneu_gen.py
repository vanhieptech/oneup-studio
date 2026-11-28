#!/usr/bin/env python3
"""VieNeu-TTS v3 Turbo backend (Apache-2.0, ONNX Runtime). Run with VIENEU_PYTHON:

  "$VIENEU_PYTHON" pipeline/tts/vieneu_gen.py batch.json

batch.json:
  {
    "precision": "fp32"|"int8",
    "backend": "onnx",
    "backbone_repo": optional LoRA/merged repo,
    "items": [
      {"t": "...", "out": "...wav", "voice": "Thái Sơn"|null,
       "ref_audio": "...wav"|null, "temperature": 0.80, "seed": 7,
       "denoise": true, "cache_hash": "..."}
    ]
  }

Voice resolution (priority):
  1. item.ref_audio (custom same-F0 clone)
  2. backbone_repo / item.backbone_repo (LoRA / merged — Phase 3 ready)
  3. preset voice name (default Thái Sơn for Hiệp, Mỹ Duyên for Omi)
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import paths as P

DEFAULT_VOICE_HIEP = "Thái Sơn"
DEFAULT_VOICE_OMI = "Mỹ Duyên"


def _is_cached(it: dict) -> bool:
    out = it["out"]
    if not os.path.exists(out):
        return False
    ch = it.get("cache_hash")
    if not ch:
        return True
    sig = out + ".sha256"
    return os.path.exists(sig) and open(sig, encoding="utf-8").read().strip() == ch


def build_tts(precision: str = "fp32", backend: str = "onnx", backbone_repo: str | None = None):
    from vieneu import Vieneu

    kwargs = {"mode": "v3turbo", "backend": backend, "precision": precision}
    if backbone_repo:
        kwargs["backbone_repo"] = backbone_repo
    return Vieneu(**kwargs)


def synthesize_item(tts, it: dict) -> None:
    text = it["t"]
    temp = float(it.get("temperature", 0.80))
    denoise = bool(it.get("denoise", True))
    ref_audio = it.get("ref_audio")
    voice = it.get("voice")
    # Prefer native EN–VI text; callers should pass clean text (no markdown / {nhấn:}).
    kwargs = {"temperature": temp, "denoise": denoise, "apply_watermark": False}
    if ref_audio:
        kwargs["ref_audio"] = ref_audio
    elif voice:
        kwargs["voice"] = voice
    else:
        kwargs["voice"] = DEFAULT_VOICE_HIEP
    # seed is accepted when engine supports it; ignore if not
    if "seed" in it:
        kwargs["seed"] = it["seed"]
    wav = tts.infer(text, **kwargs)
    out = Path(it["out"])
    out.parent.mkdir(parents=True, exist_ok=True)
    tts.save(wav, str(out))
    if it.get("cache_hash"):
        open(str(out) + ".sha256", "w", encoding="utf-8").write(it["cache_hash"] + "\n")
    print("ok", out.name, flush=True)


def main(path: str) -> None:
    b = json.load(open(path, encoding="utf-8"))
    todo = [it for it in b["items"] if not _is_cached(it)]
    if not todo:
        print(f"vieneu_gen: all {len(b['items'])} item(s) cached", flush=True)
        return
    precision = b.get("precision", "fp32")
    backend = b.get("backend", "onnx")
    backbone = b.get("backbone_repo") or os.environ.get("VIENEU_BACKBONE_REPO")
    # Phase-3 LoRA dir under $ONEUP_TOOLS_DIR/voices/hiep-oneup-v1/
    if not backbone:
        cand = P.TOOLS_DIR / "voices" / "hiep-oneup-v1"
        if cand.is_dir():
            backbone = str(cand)
    print(
        f"vieneu_gen: backend={backend} precision={precision} "
        f"backbone={backbone or 'default'} ({len(todo)}/{len(b['items'])} todo)",
        flush=True,
    )
    tts = build_tts(precision=precision, backend=backend, backbone_repo=backbone)
    for it in todo:
        # per-item backbone override not re-instantiated (Phase 3 will warm multiple)
        synthesize_item(tts, it)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: vieneu_gen.py batch.json")
    main(sys.argv[1])
