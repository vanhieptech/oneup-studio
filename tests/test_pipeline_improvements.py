"""Regression tests for pipeline improvements (scene chunking, shared respell, next-id, check-layer)."""
import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pipeline"))


def _load(rel: str, name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestPipelineImprovements(unittest.TestCase):
    def test_split_scene_chunks_preserves_non_cut_transitions(self):
        bf = _load("pipeline/scripts/build-final.py", "build_final_mod")
        plan = {
            "scenes": [
                {"id": "b01", "transition": {"type": "mmx-crash-in", "duration": 0.4}},
                {"id": "b01a", "transition": {"type": "cut", "duration": 0}},
                {"id": "b09e", "transition": {"type": "cut", "duration": 0}},
                {"id": "b09f", "transition": {"type": "tdev-shake", "duration": 0.4}},
                {"id": "b10a", "transition": {"type": "mmx-whip", "duration": 0.4}},
                {"id": "b10b", "transition": {"type": "cut", "duration": 0}},
            ]
        }
        chunks = bf._split_scene_chunks(plan)
        ids = [[s["id"] for s in ch] for ch in chunks]
        self.assertEqual(ids, [["b01"], ["b01a"], ["b09e", "b09f", "b10a"], ["b10b"]])

    def test_shared_respell_table(self):
        from tts import respell as RS
        self.assertEqual(RS.respell_word("Dunlosky"), "Đun lốt ki")
        self.assertEqual(RS.respell_word("airport"), "e pọt")
        self.assertEqual(RS.unrespell("Đun lốt ki và e pọt"), "Dunlosky và airport")
        self.assertIn("tiktok", RS.STT_ALIAS_MAP)

    def test_next_id_reads_table_and_headings(self):
        ni = _load("pipeline/scripts/next-id.py", "next_id_mod")
        self.assertGreaterEqual(ni.max_id("DL"), 73)
        self.assertGreaterEqual(ni.max_id("L"), 105)

    def test_check_layer_hard_scrim_alpha(self):
        cl = _load("channels/vanhiep-tech/scripts/check-layer.py", "check_layer_mod")
        html_scrim = '<div id="scrim" data-backdrop="hard-scrim"></div><style>#scrim{opacity:0.82;}</style>'
        self.assertEqual(cl.detect_hard_scrim_alpha(html_scrim), 209)
        self.assertIsNone(cl.detect_hard_scrim_alpha('<div id="main"></div>'))


if __name__ == "__main__":
    unittest.main()
