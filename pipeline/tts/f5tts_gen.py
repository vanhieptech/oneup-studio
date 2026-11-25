#!/usr/bin/env python3
"""F5-TTS Vietnamese batch synthesis (DL-035). Run with the local F5 venv:
  ~/oneup-tools/f5-venv/bin/python pipeline/tts/f5tts_gen.py batch.json
batch = {"ref": "assets/voice-refs/thai-son.wav", "ref_text": "…", "items": [{"t": "…", "seed": 7, "speed": 1.0, "out": "/tmp/x.wav"}]}
Model: hynt/F5-TTS-Vietnamese-ViVoice / f5-ckpt-6000h (CC-BY-NC-SA-4.0, NON-COMMERCIAL; risk accepted by Hiệp, DL-035).
Reference clips are neutral sentences synthesized by VieNeu presets (no real person cloned).
Text is lower-cased (the checkpoint is trained on lower-case ViVoice). Raw output only: trimming,
leakage removal, take picking and prosody are done by pipeline/scripts/voice-prosody.py.
"""
import json, os, sys
from pathlib import Path
import torch, soundfile as sf

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import paths as P

torch.set_num_threads(int(os.environ.get("F5_THREADS", os.cpu_count() or 4)))
from f5_tts.api import F5TTS

CK = P.F5_CKPT_DIR
VOC = P.F5_VOCODER_DIR or None
NFE = int(os.environ.get("F5_NFE", "32"))


def resolve_device() -> str:
    req = os.environ.get("F5_DEVICE", "auto").strip().lower()
    if req in ("cpu", "mps", "cuda"):
        return req
    if torch.cuda.is_available():
        return "cuda"
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def _is_cached(it: dict) -> bool:
    out = it["out"]
    if not os.path.exists(out):
        return False
    ch = it.get("cache_hash")
    if not ch:
        return True
    sig = out + ".sha256"
    return os.path.exists(sig) and open(sig, encoding="utf-8").read().strip() == ch


def main(path):
    b = json.load(open(path, encoding="utf-8"))
    todo = [it for it in b["items"] if not _is_cached(it)]
    if not todo:
        print(f"f5tts_gen: all {len(b['items'])} item(s) cached, skipping model load", flush=True)
        return
    dev = resolve_device()
    print(f"f5tts_gen: device={dev} ckpt={CK} vocoder={VOC or 'hf-hub'} nfe={NFE} ({len(todo)}/{len(b['items'])} todo)", flush=True)
    m = F5TTS(
        model="F5TTS_Base",
        ckpt_file=f"{CK}/model_last.pt",
        vocab_file=f"{CK}/vocab.txt",
        device=dev,
        vocoder_local_path=VOC,
    )
    for it in todo:
        ref_file = it.get("ref") or b["ref"]
        ref_text = (it.get("ref_text") or b["ref_text"]).lower()
        w, sr, _ = m.infer(
            ref_file=ref_file,
            ref_text=ref_text,
            gen_text=it["t"].lower(),
            nfe_step=NFE,
            speed=it.get("speed", 1.0),
            seed=it.get("seed", 7),
            remove_silence=False,
            show_info=lambda *a: None,
        )
        sf.write(it["out"], w, sr)
        if it.get("cache_hash"):
            open(it["out"] + ".sha256", "w", encoding="utf-8").write(it["cache_hash"] + "\n")
        print("ok", os.path.basename(it["out"]), round(len(w) / sr, 2), flush=True)


if __name__ == "__main__":
    main(sys.argv[1])
