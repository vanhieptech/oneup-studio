"""L-099 boundary and timeline-scope tests; no audio, image or render is created."""
import importlib.util
import sys
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check_rules_l099", ROOT / "pipeline/scripts/check-rules.py")
cr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cr)
from duration_policy import duration_status, estimated_total


class DurationPolicyTests(unittest.TestCase):
    def setUp(self):
        cr.res.clear()

    def check(self, seconds, symbol, estimated=False):
        cr.check_duration_total(seconds, "test timeline", estimated=estimated)
        self.assertEqual(cr.res[-1][0], symbol)
        self.assertIn("INCLUDING end card, pauses and transitions", cr.res[-1][2])
        return cr.res[-1][2]

    def test_299_0_passes(self):
        self.check(299.0, "⚠")

    def test_299_9_passes(self):
        self.check(299.9, "⚠")

    def test_300_0_fails(self):
        self.check(300.0, "✖")

    def test_300_1_fails(self):
        self.check(300.1, "✖")

    def test_119_warns_not_fails(self):
        self.check(119, "⚠")

    def test_181_warns_not_fails(self):
        self.check(181, "⚠")

    def test_250_warns_not_fails(self):
        self.check(250, "⚠")

    def test_150_clean(self):
        self.check(150, "✔")

    def test_target_boundaries_inclusive(self):
        self.check(120, "✔")
        self.check(180, "✔")

    def test_end_card_pushes_over_limit(self):
        self.assertEqual(duration_status(298), "warning")
        self.assertEqual(duration_status(estimated_total(298 * 2.9, 2)), "error")

    def test_estimate_includes_extra_pauses_and_transitions(self):
        self.assertAlmostEqual(estimated_total(290, 2, 3, 4), 109)

    def test_cached_total_already_includes_end_card(self):
        cr.check_spec_duration({"endcard": {"duration": 2}}, {"total": 299.9})
        self.assertEqual(cr.res[0][0], "⚠")  # NOT 301.9: never add end card twice
        cr.res.clear()
        cr.check_spec_duration({"endcard": {"duration": 2}}, {"total": 300})
        self.assertEqual(cr.res[0][0], "✖")

    def test_legacy_targets_cannot_override_limit_or_minimum(self):
        old = {"length_target": [55, 60], "word_target": [140, 175], "length_exception": "approved old exception"}
        cr.check_spec_duration(old, {"total": 150})
        self.assertEqual(cr.res[0][0], "✔")
        cr.res.clear()
        cr.check_spec_duration(old, {"total": 300})
        self.assertEqual(cr.res[0][0], "✖")
        cr.res.clear()
        cr.check_spec_duration(old, {"total": 40})
        self.assertEqual(cr.res[0][0], "⚠")

    def test_estimate_not_presented_as_measurement(self):
        msg = self.check(150, "✔", estimated=True)
        self.assertIn("ƯỚC/estimate", msg)
        self.assertNotIn("measured", msg)
        msg = self.check(150, "✔")
        self.assertIn("measured after Chốt", msg)

    def test_no_timing_uses_natural_reading_plus_endcard(self):
        script = {"endcard": {"duration": 2}, "estimated_pauses_s": 3,
                  "estimated_transitions_s": 4,
                  "parts": [{"scenes": [{"lines": [{"text": "từ " * 290}]}]}]}
        cr.check_spec_duration(script)
        self.assertEqual(cr.res[0][0], "⚠")
        self.assertIn("109.000s", cr.res[0][2])
        self.assertIn("ƯỚC/estimate", cr.res[0][2])

    def test_missing_endcard_cannot_claim_complete_estimate(self):
        cr.check_spec_duration({"parts": []})
        self.assertEqual(cr.res[0][0], "⚠")
        self.assertIn("estimate incomplete", cr.res[0][2])

    def test_only_obsolete_voice_duration_flag_retired(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / "script-test-delivery.md").write_text("delivery plan")
            measure = p / "measure.json"
            measure.write_text(json.dumps({"total_s": 61, "flags": [
                "tổng giọng 61.00s > 58s (dư 3.00s)",
                "s01: STT khớp 0.5 (<0.8)"]}))
            cr.check_prosody_file(str(measure), d)
            flagged = [msg for symbol, _, msg in cr.res if symbol == "✖"]
            self.assertEqual(len(flagged), 1)
            self.assertIn("STT", flagged[0])
            self.assertNotIn("58s", flagged[0])

    def test_no_rounding_loophole(self):
        self.check(299.9999, "⚠")
        self.check(300.00001, "✖")

    def test_invalid_values_fail(self):
        for value in [float("nan"), float("inf"), -1]:
            self.assertEqual(duration_status(value), "error")


if __name__ == "__main__":
    unittest.main()
