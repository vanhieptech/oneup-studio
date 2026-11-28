#!/usr/bin/env python3
"""VieNeu 4-block emotion voice for a locked clip spec.

  python3 pipeline/scripts/voice-vieneu.py \\
    --spec content/clips/<clip>/final/spec.json --prefix <prefix> \\
    [--precision fp32|int8] [--work DIR]

  python3 pipeline/scripts/voice-vieneu.py check-refs
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import unicodedata
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import paths as P
from tts.audio_utils import (
    SR_DEFAULT,
    audit_clip_l114,
    envelope_pcm,
    make_room_tone,
    master_voice_wav,
    measure_f0_hz,
    read_wav_mono_f32,
    validate_ref_consistency,
    write_wav_f32,
)
from tts import vieneu_gen as VG

BLOCK_TEMP = {"spark": 0.86, "dip": 0.80, "clear": 0.76, "warm": 0.86}
HIEP_REF_IDS = ("hiep-spark", "hiep-dip", "hiep-clear", "hiep-warm")
STT_MIN = 0.78
F0_MAX_ST = 2.5


def clean_text(s: str) -> str:
    """Prefer native EN–VI text: strip markdown + {nhấn:} markup, keep English tokens."""
    s = s or ""
    s = re.sub(r"\{nhấn:\s*([^}]+)\}", r"\1", s)
    s = re.sub(r"[*_`]+", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def spoken_prefer_text(line: dict) -> str:
    # Prefer `text` (may keep email/team/comment) over phonetic `say` crutches.
    raw = line.get("text") or line.get("say") or ""
    return clean_text(raw)


def iter_spec_lines(spec: dict):
    for part in spec.get("parts") or []:
        for sc in part.get("scenes") or []:
            lines = sc.get("lines") or []
            for li, line in enumerate(lines):
                lkey = sc["id"] + ("abcdef"[li] if len(lines) > 1 else "")
                yield lkey, sc, line


def emotion_block_for(lkey: str, sc: dict, line: dict) -> str:
    emo = (line.get("emotion") or "").lower()
    part = (sc.get("part") or "").lower()
    bid = sc.get("id") or lkey
    if part == "hook" or bid.startswith("b01"):
        return "spark"
    if emo in ("reflective", "sad", "vulnerable") or bid.startswith(("b02", "b03")):
        return "dip"
    if part == "evidence" or bid.startswith(("b04", "b05")):
        return "clear"
    if emo in ("warm", "happy") or bid.startswith(("b06", "b07")) or part in ("cta", "end"):
        return "warm"
    return "clear"


def group_emotion_blocks(spec: dict) -> list[dict]:
    """Group consecutive lines into 4 emotion blocks (spark→dip→clear→warm order preserved)."""
    order = ["spark", "dip", "clear", "warm"]
    buckets = {k: [] for k in order}
    for lkey, sc, line in iter_spec_lines(spec):
        b = emotion_block_for(lkey, sc, line)
        buckets[b].append({
            "key": lkey,
            "scene": sc,
            "line": line,
            "text": spoken_prefer_text(line),
            "cue": line.get("voice_cue") or line.get("cue"),
        })
    blocks = []
    for name in order:
        items = buckets[name]
        if not items:
            continue
        texts = []
        for it in items:
            t = it["text"]
            cue = it.get("cue")
            if cue and isinstance(cue, str) and cue.startswith("[") and cue not in t:
                t = f"{cue} {t}"
            texts.append(t)
        blocks.append({
            "name": name,
            "items": items,
            "text": " ".join(texts),
            "temperature": BLOCK_TEMP[name],
        })
    return blocks


def block_cache_hash(block_text: str, ref_id: str, precision: str, temperature: float, seed: int) -> str:
    payload = json.dumps(
        [block_text, ref_id, precision, round(temperature, 3), seed],
        ensure_ascii=False,
        separators=(",", ":"),
    )
    return hashlib.sha1(payload.encode()).hexdigest()[:16]


def resolve_ref_for_block(block_name: str, voice_refs: dict | None) -> tuple[str | None, str | None]:
    """Return (ref_audio_path or None, preset_voice or None, ref_id)."""
    vr = json.load(open(P.VOICE_REFS / "voice-refs.json", encoding="utf-8"))
    # custom hiep-* same-F0 set
    want = f"hiep-{block_name}"
    if want in vr and not want.startswith("_"):
        wav = P.VOICE_REFS / vr[want]["wav"]
        if wav.is_file():
            return str(wav), None, want
    # fallback: thai-son-v2 / thai-son as clone ref if present
    for fid in ("thai-son-v2", "thai-son"):
        if fid in vr:
            wav = P.VOICE_REFS / vr[fid]["wav"]
            if wav.is_file():
                return str(wav), None, fid
    # preset fallback
    return None, VG.DEFAULT_VOICE_HIEP, "preset:Thái Sơn"


def whisper_word_times(wav: Path) -> list[dict]:
    py = P.ASR_PYTHON
    script = r"""
import json, sys, os, subprocess, numpy as np
from faster_whisper import WhisperModel
path=sys.argv[1]
ff=os.environ.get("FFMPEG_BIN","ffmpeg")
raw=subprocess.run([ff,"-loglevel","error","-i",path,"-ac","1","-ar","16000","-f","f32le","-"],capture_output=True).stdout
audio=np.frombuffer(raw,dtype=np.float32)
m=WhisperModel(os.environ.get("ASR_MODEL","small"), device=os.environ.get("ASR_DEVICE","cpu"),
               compute_type=os.environ.get("ASR_COMPUTE","float32"))
segs,_=m.transcribe(audio, language="vi", word_timestamps=True)
words=[]
for s in segs:
  for w in (s.words or []):
    t=(w.word or "").strip()
    if t: words.append({"w":t,"start":float(w.start),"end":float(w.end)})
print(json.dumps(words, ensure_ascii=False))
"""
    env = os.environ.copy()
    env["FFMPEG_BIN"] = P.FFMPEG_BIN
    r = subprocess.run([py, "-c", script, str(wav)], capture_output=True, text=True, env=env)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-500:])
    return json.loads(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else "[]")


def norm_tok(s: str) -> list[str]:
    s = unicodedata.normalize("NFC", s or "")
    return re.findall(r"[\wÀ-ỹ]+", s.lower())


def split_block_by_alignment(pcm: np.ndarray, sr: int, words: list[dict], items: list[dict]) -> list[tuple[str, np.ndarray, float]]:
    """Split continuous block audio into per-line slices using word timestamps."""
    import difflib

    toks = []
    for w in words:
        nt = norm_tok(w["w"])
        if nt:
            toks.append({"tok": nt[0], "start": w["start"], "end": w["end"]})
    cursor = 0
    out = []
    for it in items:
        target = norm_tok(it["text"])
        if not target:
            out.append((it["key"], np.zeros(0, np.float32), 0.0))
            continue
        best = None
        for start_i in range(cursor, max(cursor + 1, len(toks))):
            max_len = min(len(toks) - start_i, max(len(target) + 2, int(len(target) * 2.2) + 2))
            for L in range(max(1, len(target) - 1), max_len + 1):
                window = [toks[start_i + j]["tok"] for j in range(L)]
                sc = difflib.SequenceMatcher(None, window, target).ratio()
                if best is None or sc > best["sim"]:
                    best = {
                        "sim": sc,
                        "start": toks[start_i]["start"],
                        "end": toks[start_i + L - 1]["end"],
                        "end_i": start_i + L,
                    }
            if best and best["sim"] >= 0.9:
                break
        if best is None:
            # equal split fallback
            n = len(pcm) // max(1, len(items))
            idx = items.index(it)
            a, b = idx * n, (idx + 1) * n if idx < len(items) - 1 else len(pcm)
            out.append((it["key"], pcm[a:b], 0.0))
            continue
        a = max(0, int(best["start"] * sr) - int(0.04 * sr))
        b = min(len(pcm), int(best["end"] * sr) + int(0.06 * sr))
        out.append((it["key"], pcm[a:b], round(best["sim"], 3)))
        cursor = best["end_i"]
    return out


def gen_block(tts_py: str, batch_path: Path) -> None:
    subprocess.run([tts_py, str(P.TTS / "vieneu_gen.py"), str(batch_path)], check=True)


def run_clip(spec_path: Path, prefix: str, precision: str, work: Path, max_reroll: int = 2) -> dict:
    spec = json.load(open(spec_path, encoding="utf-8"))
    blocks = group_emotion_blocks(spec)
    work.mkdir(parents=True, exist_ok=True)
    out_dir = P.VOICE_CACHE
    out_dir.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    meta_rows = []
    listen = []
    backbone = spec.get("backbone_repo")
    for block in blocks:
        seed = 7
        attempt = 0
        while True:
            attempt += 1
            ref_audio, preset, ref_id = resolve_ref_for_block(block["name"], spec.get("voice_refs"))
            ch = block_cache_hash(block["text"], ref_id, precision, block["temperature"], seed)
            raw_out = work / f"block-{block['name']}-{ch}.wav"
            batch = {
                "precision": precision,
                "backend": "onnx",
                "backbone_repo": backbone,
                "items": [{
                    "t": block["text"],
                    "out": str(raw_out),
                    "ref_audio": ref_audio,
                    "voice": None if ref_audio else preset,
                    "temperature": block["temperature"],
                    "seed": seed,
                    "denoise": True,
                    "cache_hash": ch,
                }],
            }
            bp = work / f"batch-{block['name']}.json"
            json.dump(batch, open(bp, "w"), ensure_ascii=False, indent=2)
            if not raw_out.is_file():
                print(f"gen block {block['name']} ({len(block['items'])} lines) seed={seed}", flush=True)
                gen_block(P.VIENEU_PYTHON, bp)
            pcm, sr = read_wav_mono_f32(raw_out, SR_DEFAULT)
            try:
                words = whisper_word_times(raw_out)
            except Exception as e:
                print(f"warn: whisper failed ({e}); equal-split fallback", flush=True)
                words = []
            slices = split_block_by_alignment(pcm, sr, words, block["items"]) if words else [
                (it["key"], pcm[i * len(pcm) // len(block["items"]) : (i + 1) * len(pcm) // len(block["items"])], 0.0)
                for i, it in enumerate(block["items"])
            ]
            block_rows = []
            for (lkey, seg, sim), it in zip(slices, block["items"]):
                raw_beat = work / f"{lkey}-raw.wav"
                write_wav_f32(raw_beat, seg, sr)
                dst = out_dir / f"{prefix}-{lkey}.wav"
                master_voice_wav(raw_beat, dst, sr=sr)
                mastered, _ = read_wav_mono_f32(dst, sr)
                f0 = measure_f0_hz(mastered, sr)
                payload = {
                    "duration": round(len(mastered) / sr, 3),
                    "envelope": envelope_pcm(mastered, sr),
                    "f0_hz": f0,
                    "engine": "vieneu-v3turbo-block",
                    "role": it["line"].get("speaker") or "Hiệp",
                    "stt": "",
                    "stt_sim": sim,
                    "intra_output_cuts": 0,
                    "emotion_block": block["name"],
                    "units": [{"text": it["text"], "take": f"block-{block['name']}", "sim": sim}],
                }
                json.dump(payload, open(dst.with_suffix(".json"), "w"), ensure_ascii=False)
                row = {"key": lkey, "f0_hz": f0, "duration": payload["duration"], "text": it["text"], "stt_sim": sim, "block": block["name"]}
                block_rows.append(row)
                if listen:
                    listen.append(make_room_tone(0.25, sr=sr, ref_wav=dst))
                listen.append(mastered)
            # L-114 / STT gate for this block
            audit = audit_clip_l114(block_rows)
            bad_stt = [r for r in block_rows if (r.get("stt_sim") or 0) < STT_MIN and words]
            need_reroll = (not audit["ok"] and audit["outliers"]) or bool(bad_stt)
            if need_reroll and attempt <= max_reroll:
                seed = seed + 17 * attempt
                print(f"reroll block {block['name']} attempt={attempt} seed={seed} outliers={audit['outliers']} bad_stt={len(bad_stt)}", flush=True)
                # bust cache
                if raw_out.is_file():
                    raw_out.unlink()
                continue
            meta_rows.extend(block_rows)
            if need_reroll:
                print(f"WARN block {block['name']} still fails L-114/STT after {attempt} tries", flush=True)
            break

    listen_path = work / "_listen_vieneu.wav"
    if listen:
        write_wav_f32(listen_path, np.concatenate(listen), SR_DEFAULT)
    audit = audit_clip_l114(meta_rows)
    elapsed = time.time() - t0
    total_dur = sum(r["duration"] for r in meta_rows) or 1.0
    report = {
        "elapsed_s": round(elapsed, 2),
        "audio_s": round(total_dur, 2),
        "rtf": round(elapsed / total_dur, 3),
        "precision": precision,
        "audit": audit,
        "listen": str(listen_path),
        "lines": meta_rows,
    }
    json.dump(report, open(work / "vieneu-report.json", "w"), ensure_ascii=False, indent=2)
    print(json.dumps({k: report[k] for k in ("elapsed_s", "audio_s", "rtf", "listen")}, indent=2))
    print("L-114", json.dumps({"ok": audit["ok"], "median_f0_hz": audit["median_f0_hz"], "avg_syl_per_s": audit["avg_syl_per_s"], "outliers": audit["outliers"]}, ensure_ascii=False))
    return report


def check_refs() -> int:
    vr = json.load(open(P.VOICE_REFS / "voice-refs.json", encoding="utf-8"))
    paths = []
    for rid in HIEP_REF_IDS:
        if rid not in vr:
            print(f"missing ref id {rid} in voice-refs.json (Phase-3 custom set)")
            continue
        paths.append(P.VOICE_REFS / vr[rid]["wav"])
    if len(paths) < 2:
        # also check thai-son-v2 alone
        if "thai-son-v2" in vr:
            p = P.VOICE_REFS / vr["thai-son-v2"]["wav"]
            print(f"check-refs: custom hiep-* set incomplete; measuring {p.name}")
            paths = [p]
        else:
            print("check-refs: no refs to measure")
            return 1
    res = validate_ref_consistency(paths, max_semitones=1.0)
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0 if res["ok"] else 2


def main(argv=None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    if argv and argv[0] == "check-refs":
        return check_refs()
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    ap.add_argument("--prefix", required=True)
    ap.add_argument("--precision", default="fp32", choices=["fp32", "int8"])
    ap.add_argument("--work", default="")
    args = ap.parse_args(argv)
    work = Path(args.work) if args.work else (P.VOICE_WORK_DIR / f"vieneu-{args.prefix}")
    run_clip(Path(args.spec), args.prefix, args.precision, work)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
