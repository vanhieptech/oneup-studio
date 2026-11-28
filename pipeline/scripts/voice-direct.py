#!/usr/bin/env python3
"""Direct voice: raw 90s take → denoise → stumble drop → breath-keep → master → Remotion beats.

  python3 pipeline/scripts/voice-direct.py \\
    --raw <raw.wav|m4a> --spec content/clips/<clip>/final/spec.json \\
    --prefix <voice_prefix> [--denoise auto|vieneu|ffmpeg|none] \\
    [--max-pause 0.45] [--breath-keep 0.14] [--dry-run]
"""
from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import subprocess
import sys
import tempfile
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
    write_wav_f32,
)


def norm_tokens(s: str) -> list[str]:
    s = unicodedata.normalize("NFC", s or "")
    s = re.sub(r"\{nhấn:\s*([^}]+)\}", r"\1", s)
    s = re.sub(r"[*_`]+", "", s)
    return re.findall(r"[\wÀ-ỹ]+", s.lower())


def spoken_line(line: dict) -> str:
    return line.get("say") or re.sub(r"\{nhấn:\s*([^}]+)\}", r"\1", line.get("text") or "")


def iter_spec_lines(spec: dict):
    """Yield (lkey, scene, line) using same lettering as build-final / voice-phrase-f5."""
    for part in spec.get("parts") or []:
        for sc in part.get("scenes") or []:
            lines = sc.get("lines") or []
            for li, line in enumerate(lines):
                lkey = sc["id"] + ("abcdef"[li] if len(lines) > 1 else "")
                yield lkey, sc, line


def ffmpeg_to_mono48(src: Path, dst: Path) -> Path:
    dst.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        P.FFMPEG_BIN, "-y", "-hide_banner", "-loglevel", "error",
        "-i", str(src), "-ac", "1", "-ar", str(SR_DEFAULT),
        "-c:a", "pcm_s16le", str(dst),
    ]
    subprocess.run(cmd, check=True)
    return dst


def denoise_ffmpeg(src: Path, dst: Path) -> Path:
    cmd = [
        P.FFMPEG_BIN, "-y", "-hide_banner", "-loglevel", "error",
        "-i", str(src), "-af", "afftdn=nf=-25",
        "-ac", "1", "-ar", str(SR_DEFAULT), "-c:a", "pcm_s16le", str(dst),
    ]
    subprocess.run(cmd, check=True)
    return dst


def denoise_vieneu(src: Path, dst: Path) -> Path:
    py = P.VIENEU_PYTHON
    code = (
        "from vieneu import Vieneu; from pathlib import Path; "
        f"tts=Vieneu(backend='onnx'); tts.denoise({str(src)!r}, out_path={str(dst)!r})"
    )
    r = subprocess.run([py, "-c", code], capture_output=True, text=True)
    if r.returncode != 0 or not dst.is_file():
        raise RuntimeError(r.stderr[-400:] or "vieneu denoise failed")
    return dst


def maybe_denoise(src: Path, work: Path, mode: str) -> Path:
    dst = work / "denoised.wav"
    if mode == "none":
        return ffmpeg_to_mono48(src, dst) if src.suffix.lower() != ".wav" else src
    if mode in ("vieneu", "auto"):
        try:
            clean_in = work / "in48.wav"
            ffmpeg_to_mono48(src, clean_in)
            return denoise_vieneu(clean_in, dst)
        except Exception as e:
            if mode == "vieneu":
                raise
            print(f"warn: vieneu denoise unavailable ({e}); fallback ffmpeg afftdn", flush=True)
    clean_in = work / "in48.wav"
    ffmpeg_to_mono48(src, clean_in)
    return denoise_ffmpeg(clean_in, dst)


def whisper_words(wav: Path):
    """Word-level timestamps via faster-whisper (ASR_PYTHON)."""
    py = P.ASR_PYTHON
    script = r"""
import json, sys
from faster_whisper import WhisperModel
import numpy as np, subprocess, os
path = sys.argv[1]
ff = os.environ.get("FFMPEG_BIN", "ffmpeg")
raw = subprocess.run([ff,"-loglevel","error","-i",path,"-ac","1","-ar","16000","-f","f32le","-"], capture_output=True).stdout
audio = np.frombuffer(raw, dtype=np.float32)
m = WhisperModel(os.environ.get("ASR_MODEL","small"), device=os.environ.get("ASR_DEVICE","cpu"),
                 compute_type=os.environ.get("ASR_COMPUTE","float32"))
segs, _ = m.transcribe(audio, language="vi", word_timestamps=True)
words=[]
for s in segs:
  for w in (s.words or []):
    t=(w.word or "").strip()
    if t: words.append({"w": t, "start": float(w.start), "end": float(w.end)})
print(json.dumps(words, ensure_ascii=False))
"""
    env = os.environ.copy()
    env["FFMPEG_BIN"] = P.FFMPEG_BIN
    r = subprocess.run([py, "-c", script, str(wav)], capture_output=True, text=True, env=env)
    if r.returncode != 0:
        raise RuntimeError(f"whisper failed: {r.stderr[-500:]}")
    line = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else "[]"
    return json.loads(line)


def sim_tokens(a: list[str], b: list[str]) -> float:
    return difflib.SequenceMatcher(None, a, b).ratio()


def align_lines(words: list[dict], lines: list[tuple[str, dict]]) -> list[dict]:
    """Map each spec line to a [start,end) span; stumble auto-drop keeps last best match."""
    toks = [{"tok": norm_tokens(w["w"])[0] if norm_tokens(w["w"]) else "", **w} for w in words]
    toks = [t for t in toks if t["tok"]]
    cursor = 0
    spans = []
    for lkey, line in lines:
        target = norm_tokens(spoken_line(line))
        if not target:
            spans.append({"key": lkey, "start": 0.0, "end": 0.0, "sim": 0.0, "skipped": True})
            continue
        best = None
        # search windows starting at cursor..end
        for start_i in range(cursor, max(cursor + 1, len(toks) - len(target) + 1)):
            # allow overshoot for stumbles (up to 2.5x length)
            max_len = min(len(toks) - start_i, max(len(target) + 2, int(len(target) * 2.5) + 2))
            for L in range(max(1, len(target) - 1), max_len + 1):
                window = [toks[start_i + j]["tok"] for j in range(L)]
                sc = sim_tokens(window, target)
                # prefer later starts when scores close (stumble re-take)
                score = sc + 0.02 * (start_i - cursor) / max(1, len(toks))
                if best is None or score > best["score"]:
                    best = {
                        "score": score,
                        "sim": sc,
                        "start_i": start_i,
                        "end_i": start_i + L,
                        "start": float(toks[start_i]["start"]),
                        "end": float(toks[start_i + L - 1]["end"]),
                    }
            # early exit if excellent match found near cursor
            if best and best["sim"] >= 0.92 and best["start_i"] <= cursor + 3:
                break
        if best is None:
            spans.append({"key": lkey, "start": 0.0, "end": 0.0, "sim": 0.0, "skipped": True})
            continue
        spans.append({
            "key": lkey,
            "start": best["start"],
            "end": best["end"],
            "sim": round(best["sim"], 3),
            "skipped": False,
        })
        cursor = best["end_i"]
    return spans


def trim_pauses(
    pcm: np.ndarray,
    sr: int,
    start_s: float,
    end_s: float,
    max_pause: float,
    breath_keep: float,
    ref_wav: Path | None,
) -> np.ndarray:
    """Keep breath before onset; collapse dead air > max_pause to room tone."""
    a = max(0, int((start_s - breath_keep) * sr))
    b = min(len(pcm), int(end_s * sr))
    seg = pcm[a:b].copy()
    if len(seg) < int(0.05 * sr):
        return seg
    # energy gate
    hop = max(1, int(0.01 * sr))
    win = max(hop, int(0.02 * sr))
    thr = 0.012
    voiced = []
    for i in range(0, len(seg) - win, hop):
        fr = seg[i : i + win]
        voiced.append(float(np.sqrt(np.mean(fr * fr))) >= thr)
    # find runs of silence longer than max_pause (after initial breath)
    breath_n = int(breath_keep * sr)
    out = [seg[:breath_n]] if breath_n < len(seg) else [seg]
    i = breath_n
    while i < len(seg):
        # voiced region
        j = i
        while j < len(seg) and voiced[min(len(voiced) - 1, j // hop)]:
            j += hop
        out.append(seg[i:j])
        # silence
        k = j
        while k < len(seg) and not voiced[min(len(voiced) - 1, k // hop)]:
            k += hop
        sil = (k - j) / sr
        if sil > max_pause:
            out.append(make_room_tone(min(max_pause, 0.22), sr=sr, ref_wav=ref_wav))
        elif sil > 0:
            out.append(seg[j:k])
        i = k if k > i else i + hop
    return np.concatenate([x for x in out if len(x)]) if out else seg


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Raw take → mastered Remotion voice beats")
    ap.add_argument("--raw", required=True)
    ap.add_argument("--spec", required=True)
    ap.add_argument("--prefix", required=True)
    ap.add_argument("--denoise", default="auto", choices=["auto", "vieneu", "ffmpeg", "none"])
    ap.add_argument("--max-pause", type=float, default=0.45)
    ap.add_argument("--breath-keep", type=float, default=0.14)
    ap.add_argument("--work", default="")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    raw = Path(args.raw)
    spec_path = Path(args.spec)
    spec = json.load(open(spec_path, encoding="utf-8"))
    work = Path(args.work) if args.work else (P.VOICE_WORK_DIR / f"direct-{args.prefix}")
    work.mkdir(parents=True, exist_ok=True)
    out_dir = P.VOICE_CACHE
    out_dir.mkdir(parents=True, exist_ok=True)

    print("step1: normalize → 48k mono", flush=True)
    denoised = maybe_denoise(raw, work, args.denoise)
    print(f"step2: denoise done → {denoised}", flush=True)
    pcm, sr = read_wav_mono_f32(denoised, SR_DEFAULT)

    lines = [(k, line) for k, _sc, line in iter_spec_lines(spec)]
    print(f"step3: whisper align ({len(lines)} lines)", flush=True)
    words = whisper_words(denoised) if not args.dry_run else []
    if args.dry_run and not words:
        # synthetic spans for dry-run / unit tests
        t = 0.0
        spans = []
        for k, line in lines:
            dur = max(0.4, 0.18 * max(1, len(norm_tokens(spoken_line(line)))))
            spans.append({"key": k, "start": t, "end": t + dur, "sim": 1.0, "skipped": False})
            t += dur + 0.35
    else:
        spans = align_lines(words, lines)

    print("step4–5: cut / master / write beats", flush=True)
    meta_rows = []
    listen_segs = []
    for sp, (lkey, line) in zip(spans, lines):
        if sp.get("skipped"):
            print(f"  skip {lkey}: no align", flush=True)
            continue
        cut = trim_pauses(pcm, sr, sp["start"], sp["end"], args.max_pause, args.breath_keep, denoised)
        raw_beat = work / f"{lkey}-raw.wav"
        write_wav_f32(raw_beat, cut, sr)
        dst = out_dir / f"{args.prefix}-{lkey}.wav"
        master_voice_wav(raw_beat, dst, sr=sr)
        mastered, _ = read_wav_mono_f32(dst, sr)
        f0 = measure_f0_hz(mastered, sr)
        say = spoken_line(line)
        stt_sim = float(sp.get("sim") or 0.0)
        payload = {
            "duration": round(len(mastered) / sr, 3),
            "envelope": envelope_pcm(mastered, sr),
            "f0_hz": f0,
            "engine": "direct-voice-mastered",
            "role": line.get("speaker") or "Hiệp",
            "stt": "",
            "stt_sim": stt_sim,
            "intra_output_cuts": 0,
            "units": [{"text": say, "take": "direct", "sim": stt_sim}],
        }
        json.dump(payload, open(dst.with_suffix(".json"), "w", encoding="utf-8"), ensure_ascii=False)
        meta_rows.append({
            "key": lkey,
            "f0_hz": f0,
            "duration": payload["duration"],
            "text": say,
            "stt_sim": stt_sim,
        })
        if listen_segs:
            listen_segs.append(make_room_tone(0.28, sr=sr, ref_wav=denoised))
        listen_segs.append(mastered)
        print(f"  {lkey} dur={payload['duration']} f0={f0} sim={stt_sim}", flush=True)

    listen = work / "_listen_direct.wav"
    if listen_segs:
        write_wav_f32(listen, np.concatenate(listen_segs), sr)
    audit = audit_clip_l114(meta_rows)
    report = work / "l114-audit.json"
    json.dump({"audit": audit, "lines": meta_rows, "listen": str(listen)}, open(report, "w"), ensure_ascii=False, indent=2)
    print("step6: L-114 audit", flush=True)
    print(json.dumps({
        "ok": audit["ok"],
        "median_f0_hz": audit["median_f0_hz"],
        "avg_syl_per_s": audit["avg_syl_per_s"],
        "outliers": audit["outliers"],
        "listen": str(listen),
    }, ensure_ascii=False, indent=2))
    return 0 if audit["ok"] or args.dry_run else 0  # warn-only; do not hard-fail pipeline


# --- helpers exported for unit tests ---
def stumble_dedup_windows(candidates: list[dict], target: list[str]) -> dict:
    """Keep the last high-similarity window (stumble re-take)."""
    scored = []
    for c in candidates:
        scored.append({**c, "sim": sim_tokens(c.get("tokens") or [], target)})
    scored.sort(key=lambda x: (x["sim"], x.get("start", 0)))
    return scored[-1] if scored else {"sim": 0.0}


if __name__ == "__main__":
    raise SystemExit(main())
