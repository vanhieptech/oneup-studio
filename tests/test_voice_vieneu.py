"""Unit tests for voice-vieneu (4 emotion blocks, EN–VI text, cache hash, reroll gate)."""
from pathlib import Path
import importlib.util
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pipeline"))


def _load():
    path = ROOT / "pipeline/scripts/voice-vieneu.py"
    spec = importlib.util.spec_from_file_location("voice_vieneu", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


VV = _load()


class VoiceVieNeuTests(unittest.TestCase):
    def test_group_four_emotion_blocks(self):
        spec = {
            "parts": [{
                "scenes": [
                    {"id": "b01", "part": "hook", "lines": [{"text": "Hook spark.", "emotion": "neutral"}]},
                    {"id": "b02", "part": "story", "lines": [{"text": "Dip one.", "emotion": "reflective"}]},
                    {"id": "b04", "part": "evidence", "lines": [{"text": "Clear fact.", "emotion": "focused"}]},
                    {"id": "b07", "part": "cta", "lines": [{"text": "Warm ask.", "emotion": "warm"}]},
                ]
            }]
        }
        blocks = VV.group_emotion_blocks(spec)
        names = [b["name"] for b in blocks]
        self.assertEqual(names, ["spark", "dip", "clear", "warm"])
        self.assertIn("Hook spark", blocks[0]["text"])

    def test_prefer_text_keeps_english_tokens_not_say(self):
        line = {
            "text": "Mình check email với team rồi comment lại.",
            "say": "mình check i meo với tim rồi comment lại",
        }
        t = VV.spoken_prefer_text(line)
        self.assertIn("email", t)
        self.assertIn("team", t)
        self.assertNotIn("i meo", t)

    def test_block_cache_hash_stable_and_changes_on_text(self):
        a = VV.block_cache_hash("hello", "thai-son-v2", "fp32", 0.8, 7)
        b = VV.block_cache_hash("hello", "thai-son-v2", "fp32", 0.8, 7)
        c = VV.block_cache_hash("hello!", "thai-son-v2", "fp32", 0.8, 7)
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)

    def test_clean_text_strips_markup(self):
        self.assertEqual(VV.clean_text("Úp **máy** {nhấn: xuống} bàn"), "Úp máy xuống bàn")

    def test_vieneu_gen_mock_infer_kwargs(self):
        from tts import vieneu_gen as VG
        fake = mock.MagicMock()
        fake.infer.return_value = [0.0]
        with tempfile.TemporaryDirectory() as d:
            out = str(Path(d) / "out.wav")
            VG.synthesize_item(fake, {
                "t": "Xin chào team",
                "out": out,
                "voice": "Thái Sơn",
                "temperature": 0.86,
                "denoise": True,
            })
        kwargs = fake.infer.call_args.kwargs
        self.assertEqual(fake.infer.call_args.args[0], "Xin chào team")
        self.assertEqual(kwargs.get("voice"), "Thái Sơn")
        self.assertEqual(kwargs.get("temperature"), 0.86)
        fake.save.assert_called_once()


if __name__ == "__main__":
    unittest.main()
