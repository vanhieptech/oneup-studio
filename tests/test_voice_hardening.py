"""Regression tests for DL-087 / DL-088 / L-114 voice & build pipeline hardening."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class VoiceHardeningTests(unittest.TestCase):
    def test_voice_phrase_single_ref_and_6000h_speed_default(self):
        src = (ROOT / "pipeline/scripts/voice-phrase-f5.py").read_text(encoding="utf-8")
        m = re.search(r"REF_SLOTS\s*=\s*(\{[^}]+\})", src)
        self.assertTrue(m, "REF_SLOTS not found in voice-phrase-f5.py")
        slots = eval(m.group(1))
        self.assertEqual(set(slots.values()), {"thai-son-v2"})
        self.assertIn("STRETCHED_6000H_REFS", src)
        self.assertIn("1.12", src)
        self.assertTrue('"f0_hz":f0_hz' in src or '"f0_hz": f0_hz' in src)
        self.assertIn("make_room_tone", src)

    def test_build_final_auto_reuses_voice_prefix_stitched_files(self):
        src = (ROOT / "pipeline/scripts/build-final.py").read_text(encoding="utf-8")
        self.assertIn('vpre = spec.get("voice_prefix")', src)
        self.assertIn('cand = f"{vpre}-{lkey}"', src)
        self.assertIn("--voice-mode", src)

    def test_prosody_check_voice_has_work_dir_fallback(self):
        src = (ROOT / "pipeline/scripts/prosody-check.py").read_text(encoding="utf-8")
        self.assertIn('arg("--work") or str(P.VOICE_WORK_DIR', src)

    def test_check_rules_has_l114_f0_and_rate_checks(self):
        src = (ROOT / "pipeline/scripts/check-rules.py").read_text(encoding="utf-8")
        self.assertIn('"L-114"', src)
        self.assertIn("avg_rate < 3.8", src)
        self.assertIn("abs(12 * math.log2(v / med_f0)) > 2.5", src)

    def test_paths_expose_vieneu_voices_dir(self):
        sys_path_src = (ROOT / "pipeline/paths.py").read_text(encoding="utf-8")
        self.assertIn("VIENEU_VOICES_DIR", sys_path_src)
        self.assertIn("vieneu-venv", sys_path_src)


if __name__ == "__main__":
    unittest.main()
