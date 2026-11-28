#!/usr/bin/env python3
"""Shared voice audio helpers (Phase-1 voice engine): real room tone, studio mastering, F0/L-114 audit.

Paths come from pipeline.paths / env — never hardcode absolute machine paths into tracked callers.
"""
from __future__ import annotations

import math
import subprocess
import sys
from pathlib import Path
from typing import Optional, Sequence, Union

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import paths as P

SR_DEFAULT = 48000
ROOM_TONE_DB = -55.0
ROOM_XF_S = 0.015
L114_MAX_ST = 2.5
L114_MIN_SYL_S = 3.8
REF_MAX_ST = 1.0


def _ffmpeg() -> str:
    return P.FFMPEG_BIN


def read_wav_mono_f32(path: Union[str, Path], target_sr: int = SR_DEFAULT) -> tuple[np.ndarray, int]:
    """Load any ffmpeg-readable audio as mono float32 at target_sr."""
    path = str(path)
    cmd = [
        _ffmpeg(), "-hide_banner", "-loglevel", "error",
        "-i", path, "-ac", "1", "-ar", str(target_sr),
        "-f", "f32le", "-",
    ]
    r = subprocess.run(cmd, capture_output=True, check=False)
    if r.returncode != 0 or not r.stdout:
        raise RuntimeError(f"ffmpeg read failed for {path}: {r.stderr.decode(errors='replace')[:240]}")
    x = np.frombuffer(r.stdout, dtype=np.float32).copy()
    return x, target_sr


def write_wav_f32(path: Union[str, Path], pcm: np.ndarray, sr: int = SR_DEFAULT) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    pcm = np.asarray(pcm, dtype=np.float32).reshape(-1)
    peak = float(np.max(np.abs(pcm))) if len(pcm) else 0.0
    if peak > 1.0:
        pcm = pcm / peak
    # pcm_f32le via ffmpeg → 16-bit wav for Remotion compatibility
    cmd = [
        _ffmpeg(), "-y", "-hide_banner", "-loglevel", "error",
        "-f", "f32le", "-ar", str(sr), "-ac", "1", "-i", "-",
        "-c:a", "pcm_s16le", str(path),
    ]
    subprocess.run(cmd, input=pcm.tobytes(), check=True)


def rms_db(pcm: np.ndarray, eps: float = 1e-12) -> float:
    pcm = np.asarray(pcm, dtype=np.float32).reshape(-1)
    if not len(pcm):
        return -120.0
    r = float(np.sqrt(np.mean(pcm * pcm)) + eps)
    return 20.0 * math.log10(r)


def _pink_noise(n: int, rng: np.random.Generator) -> np.ndarray:
    """Simple Voss-McCartney-ish pink noise (warm room floor)."""
    white = rng.standard_normal(n).astype(np.float32)
    # 1/f filter in frequency domain
    spec = np.fft.rfft(white)
    freqs = np.fft.rfftfreq(n)
    freqs[0] = freqs[1] if len(freqs) > 1 else 1.0
    spec /= np.sqrt(freqs)
    pink = np.fft.irfft(spec, n=n).astype(np.float32)
    # soft band-pass (~80–6k) via moving average + subtract DC
    k = max(3, n // 8000)
    kernel = np.ones(k, dtype=np.float32) / k
    soft = np.convolve(pink, kernel, mode="same")
    soft -= float(np.mean(soft))
    return soft.astype(np.float32)


def _extract_quiet_segment(pcm: np.ndarray, sr: int, duration_s: float) -> Optional[np.ndarray]:
    """Pick the quietest window of `duration_s` from pcm (energy floor)."""
    need = max(1, int(duration_s * sr))
    if len(pcm) < need:
        return None
    hop = max(1, need // 4)
    best_i, best_e = 0, float("inf")
    for i in range(0, len(pcm) - need + 1, hop):
        seg = pcm[i : i + need]
        e = float(np.mean(seg * seg))
        if e < best_e:
            best_e, best_i = e, i
    seg = pcm[best_i : best_i + need].astype(np.float32)
    # Reject if the "quiet" window is still clearly speech
    if rms_db(seg) > -35.0:
        return None
    return seg


def _scale_to_db(pcm: np.ndarray, level_db: float) -> np.ndarray:
    cur = rms_db(pcm)
    gain = 10.0 ** ((level_db - cur) / 20.0)
    return (pcm * gain).astype(np.float32)


def _crossfade_edges(pcm: np.ndarray, sr: int, xf_s: float = ROOM_XF_S) -> np.ndarray:
    n = len(pcm)
    xf = min(n // 2, max(1, int(xf_s * sr)))
    if xf < 2:
        return pcm
    out = pcm.copy()
    ramp = np.linspace(0.0, 1.0, xf, dtype=np.float32)
    out[:xf] *= ramp
    out[-xf:] *= ramp[::-1]
    return out


def make_room_tone(
    duration_s: float,
    sr: int = SR_DEFAULT,
    level_db: float = ROOM_TONE_DB,
    ref_wav: Optional[Union[str, Path]] = None,
    seed: int = 7,
) -> np.ndarray:
    """Real room-tone bed (never digital silence). Prefer quiet extract from ref / assets/sfx/room-tone.wav."""
    n = max(1, int(round(float(duration_s) * sr)))
    if duration_s <= 0:
        return np.zeros(0, dtype=np.float32)

    candidates: list[Path] = []
    if ref_wav:
        candidates.append(Path(ref_wav))
    default_rt = P.SFX / "room-tone.wav"
    if default_rt.is_file():
        candidates.append(default_rt)

    for cand in candidates:
        if not cand.is_file():
            continue
        try:
            pcm, _ = read_wav_mono_f32(cand, sr)
        except Exception:
            continue
        seg = _extract_quiet_segment(pcm, sr, max(duration_s, 0.25))
        if seg is None and len(pcm) >= n:
            # loop a short quiet-ish tail
            tail = pcm[-min(len(pcm), int(0.4 * sr)) :]
            reps = int(math.ceil(n / max(1, len(tail))))
            seg = np.tile(tail, reps)[:n]
        if seg is None:
            continue
        if len(seg) < n:
            reps = int(math.ceil(n / len(seg)))
            seg = np.tile(seg, reps)[:n]
        else:
            seg = seg[:n]
        out = _scale_to_db(seg, level_db)
        return _crossfade_edges(out, sr)

    rng = np.random.default_rng(seed)
    pink = _pink_noise(n, rng)
    out = _scale_to_db(pink, level_db)
    return _crossfade_edges(out, sr)


def master_voice_wav(
    in_wav: Union[str, Path],
    out_wav: Union[str, Path],
    sr: int = SR_DEFAULT,
) -> Path:
    """TikTok-oriented studio chain → mono 48 kHz, −14 LUFS."""
    in_wav, out_wav = Path(in_wav), Path(out_wav)
    out_wav.parent.mkdir(parents=True, exist_ok=True)
    # highpass → warm EQ → presence → soft de-ess (high shelf cut) → light compressor → loudnorm
    af = (
        "highpass=f=80,"
        "equalizer=f=200:t=q:w=1.2:g=1.5,"
        "equalizer=f=3500:t=q:w=1.5:g=1.5,"
        "equalizer=f=7000:t=q:w=1.2:g=-2.5,"
        "acompressor=threshold=-18dB:ratio=2.5:attack=8:release=80:makeup=2,"
        "loudnorm=I=-14:TP=-1.5:LRA=7,"
        f"aformat=sample_fmts=s16:sample_rates={sr}:channel_layouts=mono"
    )
    cmd = [
        _ffmpeg(), "-y", "-hide_banner", "-loglevel", "error",
        "-i", str(in_wav), "-af", af, "-ac", "1", "-ar", str(sr),
        "-c:a", "pcm_s16le", str(out_wav),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"master_voice_wav failed: {r.stderr[:400]}")
    return out_wav


def measure_f0_hz(pcm_float: np.ndarray, sr: int = SR_DEFAULT) -> Optional[float]:
    """Median F0 via autocorrelation (same algorithm as voice-phrase-f5 stitch / L-114)."""
    y = np.asarray(pcm_float, dtype=np.float32).reshape(-1)
    if len(y) < int(0.05 * sr):
        return None
    hop, win = int(sr * 0.03), int(sr * 0.04)
    lo, hi = int(sr / 260), int(sr / 70)
    f0s: list[float] = []
    for i in range(0, len(y) - win, hop):
        fr = y[i : i + win]
        if float(np.sqrt(np.mean(fr * fr))) < 0.02:
            continue
        fr = fr - float(np.mean(fr))
        ac = np.correlate(fr, fr, mode="full")[win - 1 :]
        if hi < len(ac) and ac[0] > 1e-9:
            k = lo + int(np.argmax(ac[lo:hi]))
            if ac[k] > 0.45 * ac[0]:
                f0s.append(sr / k)
    if not f0s:
        return None
    return round(float(np.median(f0s)), 1)


def semitone_delta(a_hz: float, b_hz: float) -> float:
    if a_hz <= 0 or b_hz <= 0:
        return 0.0
    return 12.0 * math.log2(a_hz / b_hz)


def validate_ref_consistency(
    ref_paths: Sequence[Union[str, Path]],
    max_semitones: float = REF_MAX_ST,
) -> dict:
    """Measure F0 of each ref wav; fail if any pair differs by > max_semitones."""
    rows = []
    for p in ref_paths:
        p = Path(p)
        if not p.is_file():
            rows.append({"path": str(p), "f0_hz": None, "ok": False, "error": "missing"})
            continue
        pcm, sr = read_wav_mono_f32(p)
        f0 = measure_f0_hz(pcm, sr)
        rows.append({"path": str(p), "f0_hz": f0, "ok": f0 is not None})
    valid = [r for r in rows if r.get("f0_hz")]
    outliers = []
    if len(valid) >= 2:
        med = float(np.median([r["f0_hz"] for r in valid]))
        for r in valid:
            st = abs(semitone_delta(r["f0_hz"], med))
            r["delta_st"] = round(st, 2)
            if st > max_semitones:
                outliers.append({"path": r["path"], "f0_hz": r["f0_hz"], "delta_st": r["delta_st"]})
                r["ok"] = False
    ok = all(r.get("ok") for r in rows) and not outliers
    return {
        "ok": ok,
        "max_semitones": max_semitones,
        "refs": rows,
        "outliers": outliers,
    }


def _norm_tokens(s: str) -> list[str]:
    import re
    import unicodedata

    s = unicodedata.normalize("NFC", s or "")
    s = re.sub(r"\{nhấn:\s*([^}]+)\}", r"\1", s)
    s = re.sub(r"[*_`]+", "", s)
    return re.findall(r"[\wÀ-ỹ]+", s.lower())


def syllable_count(text: str) -> int:
    return len(_norm_tokens(text))


def audit_clip_l114(
    lines_meta: Sequence[dict],
    max_st: float = L114_MAX_ST,
    min_syl_s: float = L114_MIN_SYL_S,
) -> dict:
    """L-114 audit: F0 within ±max_st of clip median; speaking rate ≥ min_syl_s.

    Each item: {key, f0_hz?, duration?, text?|say?, syl_per_s?, stt_sim?}
    """
    f0_rows = [(m.get("key") or m.get("line"), m.get("f0_hz")) for m in lines_meta if m.get("f0_hz")]
    f0_rows = [(k, float(v)) for k, v in f0_rows if v]
    med = None
    outliers = []
    if len(f0_rows) >= 2:
        med = float(sorted(v for _, v in f0_rows)[len(f0_rows) // 2])
        for k, v in f0_rows:
            st = semitone_delta(v, med)
            if abs(st) > max_st:
                outliers.append({"key": k, "f0_hz": v, "delta_st": round(st, 2)})

    tot_syl = 0
    tot_dur = 0.0
    per_line = []
    for m in lines_meta:
        text = m.get("text") or m.get("say") or ""
        dur = float(m.get("duration") or m.get("dur") or 0.0)
        syl = int(m.get("syllables") or syllable_count(text))
        rate = (syl / dur) if dur > 0 else None
        if dur > 0 and syl > 0:
            tot_syl += syl
            tot_dur += dur
        st = None
        if med and m.get("f0_hz"):
            st = round(semitone_delta(float(m["f0_hz"]), med), 2)
        per_line.append({
            "key": m.get("key") or m.get("line"),
            "f0_hz": m.get("f0_hz"),
            "delta_st": st,
            "duration": dur or None,
            "syllables": syl,
            "syl_per_s": round(rate, 2) if rate else None,
            "stt_sim": m.get("stt_sim"),
        })

    avg_rate = (tot_syl / tot_dur) if tot_dur > 0 else None
    ok = (not outliers) and (avg_rate is None or avg_rate >= min_syl_s)
    return {
        "ok": ok,
        "median_f0_hz": round(med, 1) if med else None,
        "outliers": outliers,
        "avg_syl_per_s": round(avg_rate, 2) if avg_rate is not None else None,
        "min_syl_per_s": min_syl_s,
        "max_st": max_st,
        "lines": per_line,
    }


def envelope_pcm(pcm: np.ndarray, sr: int = SR_DEFAULT, fps: int = 30) -> list[float]:
    x = np.asarray(pcm, dtype=np.float32).reshape(-1)
    hop = sr / fps
    e = []
    i = 0
    while i * hop < len(x):
        seg = x[int(i * hop) : int((i + 1) * hop)]
        e.append(float(np.sqrt(np.mean(seg * seg))) if len(seg) else 0.0)
        i += 1
    if not e:
        return []
    pk = sorted(e)[int(len(e) * 0.95)]
    return [round(min(1.0, v / max(pk, 1e-4)), 3) for v in e]


def concat_with_room_tone(
    segments: Sequence[np.ndarray],
    gaps_s: Sequence[float],
    sr: int = SR_DEFAULT,
    ref_wav: Optional[Union[str, Path]] = None,
) -> np.ndarray:
    """Join segments with room-tone gaps (gaps_s length = len(segments)-1, or trailing)."""
    out: list[np.ndarray] = []
    for i, seg in enumerate(segments):
        out.append(np.asarray(seg, dtype=np.float32))
        if i < len(gaps_s):
            g = float(gaps_s[i])
            if g > 0:
                out.append(make_room_tone(g, sr=sr, ref_wav=ref_wav))
    if not out:
        return np.zeros(0, dtype=np.float32)
    return np.concatenate(out)
