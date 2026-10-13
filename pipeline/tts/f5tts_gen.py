#!/usr/bin/env python3
"""F5-TTS Vietnamese batch synthesis (DL-035). Run with the F5 venv:
  /workspace/f5-venv/bin/python pipeline/tts/f5tts_gen.py batch.json
batch = {"ref": "pipeline/tts/f5-refs/thai-son.wav", "ref_text": "…", "items": [{"t": "…", "seed": 7, "speed": 1.0, "out": "/tmp/x.wav"}]}
Model: hynt/F5-TTS-Vietnamese-ViVoice (CC-BY-NC-SA-4.0, NON-COMMERCIAL; risk accepted by Hiệp, DL-035).
Reference clips are neutral sentences synthesized by VieNeu presets (no real person cloned).
Text is lower-cased (the checkpoint is trained on lower-case ViVoice). Raw output only: trimming,
leakage removal, take picking and prosody are done by pipeline/scripts/voice-prosody.py.
"""
import json, os, sys
import torch, soundfile as sf
torch.set_num_threads(int(os.environ.get("F5_THREADS", os.cpu_count() or 4)))
from f5_tts.api import F5TTS
CK = os.environ.get("F5_CKPT_DIR", "/workspace/f5-ckpt")
NFE = int(os.environ.get("F5_NFE", "32"))

def main(path):
    b = json.load(open(path))
    m = F5TTS(model="F5TTS_Base", ckpt_file=f"{CK}/model_last.pt", vocab_file=f"{CK}/vocab.txt", device="cpu")
    for it in b["items"]:
        if os.path.exists(it["out"]): continue
        w, sr, _ = m.infer(ref_file=b["ref"], ref_text=b["ref_text"].lower(), gen_text=it["t"].lower(), nfe_step=NFE,
                           speed=it.get("speed", 1.0), seed=it.get("seed", 7), remove_silence=False, show_info=lambda *a: None)
        sf.write(it["out"], w, sr); print("ok", os.path.basename(it["out"]), round(len(w) / sr, 2), flush=True)

if __name__ == "__main__":
    main(sys.argv[1])
