"""Unit tests for storyboard.yaml ↔ spec.json compiler (make-video v3 / DL-094)."""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load():
    path = ROOT / "pipeline/scripts/spec-compile.py"
    spec = importlib.util.spec_from_file_location("spec_compile", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


SC = _load()
TEMPLATE = ROOT / "templates/storyboard.yaml"


class SpecCompileTests(unittest.TestCase):
    def test_template_compiles_to_remotion_schema(self):
        sb = SC.load_yaml(TEMPLATE)
        spec = SC.compile_storyboard(sb)
        self.assertTrue(spec["id"].endswith("-final") or "clip" in spec["id"])
        self.assertIn("parts", spec)
        self.assertEqual(spec["parts"][0]["engine"], "remotion")
        scenes = spec["parts"][0]["scenes"]
        self.assertGreaterEqual(len(scenes), 3)
        self.assertIn("hook", spec)
        self.assertGreaterEqual(len(spec["hook"]["scenes"]), 1)
        self.assertEqual(spec["pacing"]["lead"], 0.06)
        self.assertEqual(spec["pacing"]["tail"], 0.15)
        self.assertGreaterEqual(len(spec["engagement"]), 3)
        for sc in scenes:
            self.assertIn("fx", sc)
            self.assertTrue(sc["fx"].get("visual"))
            self.assertIn("lines", sc)
            line = sc["lines"][0]
            self.assertIn("hl", line)
            self.assertIn("phrases", line)
            cast = sc.get("cast") or []
            for c in cast:
                x = float(c.get("x", 0.5))
                self.assertGreaterEqual(x, 0.35)
                self.assertLessEqual(x, 0.65)

    def test_hl_from_bold_markup(self):
        self.assertEqual(SC.hl_indices("Ai cũng **bảo**."), [2])
        self.assertEqual(SC.hl_indices("úp **máy** xuống"), [1])
        # L-004: EN caption indexes (not VI)
        self.assertEqual(SC.hl_for_line("Ai cũng **bảo**.", "Everyone says so.", "bảo"), [2])
        self.assertEqual(SC.hl_for_line("úp **máy** xuống", "Face-down means focus.", "máy"), [2])
        hl = SC.hl_for_line("mắt **liếc**", "Anyone else still glancing?", "liếc")
        en_w = "Anyone else still glancing?".split()
        self.assertTrue(hl)
        self.assertTrue(all(en_w[i].lower().strip(".,?!") not in SC._FUNC_EN for i in hl))

    def test_merge_existing_keeps_revisions(self):
        sb = SC.load_yaml(TEMPLATE)
        existing = {
            "revisions": [{"date": "2026-11-28", "dl": "DL-094", "note": "keep me"}],
            "fact_lock": ["Ward 2017"],
            "endcard": {"sources": "Ward 2017", "credit": "CC", "safety": "ok"},
        }
        spec = SC.compile_storyboard(sb, existing=existing)
        self.assertEqual(spec["revisions"][0]["dl"], "DL-094")
        self.assertEqual(spec["fact_lock"], ["Ward 2017"])
        self.assertEqual(spec["endcard"]["sources"], "Ward 2017")

    def test_round_trip_decompile(self):
        sb = SC.load_yaml(TEMPLATE)
        spec = SC.compile_storyboard(sb)
        back = SC.decompile_spec(spec)
        self.assertEqual(len(back["beats"]), len(sb["beats"]))
        self.assertEqual(back["beats"][0]["id"], sb["beats"][0]["id"])
        self.assertGreaterEqual(len(back["engagement"]), 3)
        # recompile after decompile still has hook + fx
        again = SC.compile_storyboard(back)
        self.assertIn("hook", again)
        self.assertTrue(again["parts"][0]["scenes"][0]["fx"]["visual"])

    def test_cli_merge_and_decompile(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            out_spec = td / "spec.json"
            # seed revisions file
            seed = SC.compile_storyboard(SC.load_yaml(TEMPLATE))
            seed["revisions"] = [{"date": "2026-11-01", "dl": "DL-001", "note": "seed"}]
            out_spec.write_text(json.dumps(seed), encoding="utf-8")
            rc = SC.main(["--in", str(TEMPLATE), "--out", str(out_spec), "--merge-existing"])
            self.assertEqual(rc, 0)
            merged = json.loads(out_spec.read_text(encoding="utf-8"))
            self.assertEqual(merged["revisions"][0]["dl"], "DL-001")
            yaml_out = td / "storyboard.yaml"
            rc2 = SC.main(["--decompile", str(out_spec), "--out", str(yaml_out)])
            self.assertEqual(rc2, 0)
            self.assertTrue(yaml_out.is_file())
            self.assertGreaterEqual(len(yaml_out.read_text(encoding="utf-8").splitlines()), 20)

    def test_engagement_under_three_fails(self):
        sb = SC.load_yaml(TEMPLATE)
        sb = dict(sb)
        sb["engagement"] = sb["engagement"][:2]
        with self.assertRaises(SystemExit):
            SC.compile_storyboard(sb)


if __name__ == "__main__":
    unittest.main()
