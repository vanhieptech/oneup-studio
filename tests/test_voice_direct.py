"""Unit tests for voice-direct (stumble dedup, breath-keep, json schema)."""
from pathlib import Path
import importlib.util
import json
import sys
import tempfile
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pipeline"))


def _load_voice_direct():
    path = ROOT / "pipeline/scripts/voice-direct.py"
    spec = importlib.util.spec_from_file_location("voice_direct", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


VD = _load_voice_direct()


class VoiceDirectTests(unittest.TestCase):
    def test_stumble_dedup_keeps_last_best_match(self):
        target = ["úp", "máy", "xuống"]
        cands = [
            {"tokens": ["úp", "máy"], "start": 0.0},
            {"tokens": ["úp", "máy", "xuống"], "start": 1.2},
            {"tokens": ["úp", "máy", "xuống", "bàn"], "start": 2.5},
        ]
        best = VD.stumble_dedup_windows(cands, target)
        self.assertEqual(best["start"], 1.2)
        self.assertGreaterEqual(best["sim"], 0.9)

    def test_align_lines_prefers_later_retake(self):
        words = [
            {"w": "úp", "start": 0.0, "end": 0.2},
            {"w": "máy", "start": 0.2, "end": 0.4},
            {"w": "ủa", "start": 0.5, "end": 0.6},
            {"w": "úp", "start": 1.0, "end": 1.2},
            {"w": "máy", "start": 1.2, "end": 1.4},
            {"w": "xuống", "start": 1.4, "end": 1.7},
        ]
        lines = [("b01", {"text": "Úp máy xuống", "say": "úp máy xuống"})]
        spans = VD.align_lines(words, lines)
        self.assertEqual(len(spans), 1)
        self.assertGreaterEqual(spans[0]["start"], 0.9)
        self.assertGreaterEqual(spans[0]["sim"], 0.8)

    def test_trim_pauses_collapses_dead_air(self):
        sr = 48000
        breath = np.zeros(int(0.2 * sr), np.float32)
        tone = (0.2 * np.sin(2 * np.pi * 140 * np.arange(int(0.3 * sr)) / sr)).astype(np.float32)
        dead = np.zeros(int(1.0 * sr), np.float32)
        tone2 = (0.2 * np.sin(2 * np.pi * 140 * np.arange(int(0.2 * sr)) / sr)).astype(np.float32)
        pcm = np.concatenate([breath, tone, dead, tone2])
        out = VD.trim_pauses(pcm, sr, start_s=0.2, end_s=len(pcm) / sr, max_pause=0.45, breath_keep=0.14, ref_wav=None)
        self.assertLess(len(out) / sr, 1.2)

    def test_json_schema_fields(self):
        from tts.audio_utils import write_wav_f32, measure_f0_hz, envelope_pcm
        with tempfile.TemporaryDirectory() as d:
            wav = Path(d) / "c08v1-b01.wav"
            x = (0.2 * np.sin(2 * np.pi * 130 * np.arange(48000) / 48000)).astype(np.float32)
            write_wav_f32(wav, x, 48000)
            payload = {
                "duration": round(len(x) / 48000, 3),
                "envelope": envelope_pcm(x, 48000),
                "f0_hz": measure_f0_hz(x, 48000),
                "engine": "direct-voice-mastered",
                "role": "Hiệp",
                "stt": "",
                "stt_sim": 0.91,
                "intra_output_cuts": 0,
                "units": [{"text": "test", "take": "direct", "sim": 0.91}],
            }
            jp = wav.with_suffix(".json")
            json.dump(payload, open(jp, "w"))
            m = json.load(open(jp))
            for k in ("duration", "envelope", "f0_hz", "engine", "role", "stt", "stt_sim", "intra_output_cuts", "units"):
                self.assertIn(k, m)
            self.assertEqual(m["engine"], "direct-voice-mastered")
            self.assertIsNotNone(m["f0_hz"])


if __name__ == "__main__":
    unittest.main()
