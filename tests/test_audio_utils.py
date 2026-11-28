"""Offline unit tests for pipeline/tts/audio_utils.py (room tone, F0, L-114)."""
from pathlib import Path
import math
import struct
import sys
import tempfile
import unittest
import wave

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pipeline"))
from tts.audio_utils import (  # noqa: E402
    make_room_tone,
    measure_f0_hz,
    rms_db,
    validate_ref_consistency,
    audit_clip_l114,
)


def _write_tone_wav(path: Path, hz: float, sr: int = 48000, dur: float = 0.6):
    t = np.arange(int(sr * dur), dtype=np.float32) / sr
    y = (0.25 * np.sin(2 * math.pi * hz * t)).astype(np.float32)
    with wave.open(str(path), "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(struct.pack("<" + "h" * len(y), *[int(max(-1, min(1, v)) * 32767) for v in y]))


class AudioUtilsTests(unittest.TestCase):
    def test_make_room_tone_not_digital_silence(self):
        x = make_room_tone(0.5, sr=48000, level_db=-55.0, seed=3)
        self.assertEqual(len(x), 24000)
        self.assertGreater(float(np.max(np.abs(x))), 0.0)
        db = rms_db(x)
        self.assertGreaterEqual(db, -65.0)
        self.assertLessEqual(db, -45.0)

    def test_make_room_tone_zero_duration(self):
        self.assertEqual(len(make_room_tone(0.0)), 0)

    def test_validate_ref_consistency_detects_semitone_drift(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            a, b = d / "a.wav", d / "b.wav"
            _write_tone_wav(a, 120.0)
            _write_tone_wav(b, 140.0)
            res = validate_ref_consistency([a, b], max_semitones=1.0)
            self.assertFalse(res["ok"])
            self.assertTrue(res["outliers"])

    def test_validate_ref_consistency_same_pitch_ok(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            a, b = d / "a.wav", d / "b.wav"
            _write_tone_wav(a, 125.0)
            _write_tone_wav(b, 126.0)
            res = validate_ref_consistency([a, b], max_semitones=1.0)
            self.assertTrue(res["ok"])

    def test_audit_clip_l114_flags_outlier(self):
        lines = [
            {"key": "b01", "f0_hz": 120.0, "duration": 2.0, "text": "một hai ba bốn năm sáu bảy tám"},
            {"key": "b02", "f0_hz": 160.0, "duration": 2.0, "text": "một hai ba bốn năm sáu bảy tám"},
        ]
        r = audit_clip_l114(lines, max_st=2.5, min_syl_s=3.8)
        self.assertTrue(r["outliers"])
        self.assertFalse(r["ok"])

    def test_measure_f0_roughly_tracks_tone(self):
        sr = 48000
        t = np.arange(int(sr * 0.8), dtype=np.float32) / sr
        y = (0.3 * np.sin(2 * math.pi * 130.0 * t)).astype(np.float32)
        f0 = measure_f0_hz(y, sr)
        self.assertIsNotNone(f0)
        self.assertGreaterEqual(f0, 110.0)
        self.assertLessEqual(f0, 150.0)


if __name__ == "__main__":
    unittest.main()
