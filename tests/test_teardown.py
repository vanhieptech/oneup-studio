# teardown.py (26/11/2026): parse Gemini output, measure cut accuracy on our own timing.json, render the template sections.
import importlib.util, json, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec_ = importlib.util.spec_from_file_location("teardown", os.path.join(R, "pipeline/scripts/teardown.py"))
td = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(td)

DATA = {"hook": {"spoken": "x", "mechanism": "tò mò"}, "pacing": {"interrupts": [{"t": "00:04", "what": "zoom", "kind": "quan sát"}]},
        "spine": [{"from": "00:00", "to": "00:04", "role": "dẫn dắt"}, {"from": "01:05", "to": "01:10", "role": "kết"}], "formula": ["a", "b", "c", "d"]}

def test_extract_json_from_fenced_text():
    assert td.extract_json("Đây:\n```json\n" + json.dumps(DATA) + "\n```")["hook"]["spoken"] == "x"

def test_prompt_block_loads():
    assert "Trả về DUY NHẤT một khối JSON" in td.load_prompt()

def test_cut_accuracy_uses_part_offsets():
    import tempfile, pathlib
    t = pathlib.Path(tempfile.mkdtemp()) / "timing.json"
    t.write_text(json.dumps({"parts": [{"_off": 0.0, "dur": 60, "scene_starts": [0.0, 4.3]}, {"_off": 60.0, "dur": 20, "scene_starts": [5.0]}]}))
    acc = td.cut_accuracy(DATA, str(t))
    assert acc["n"] == 3 and acc["within_1s"] == 3   # 00:04→4.3, 00:00→0, 01:05→65

def test_render_md_has_template_sections():
    md = td.render_md("c1", DATA, {"date": "2026-11-26", "video": "v.mp4", "cli": "0.71.1", "model": "m"})
    for h in ("## Khối 0", "## Khối 1 — Hook Mechanics", "## Khối 2 — Story Arc & Beat Map", "## Khối 3 — Winning Points",
              "## Khối 4 — Algorithmic Triggers", "## Khối 5 — Reusable Story Arc", "## Khối 6 — Dual-Channel Angle"): assert h in md

def test_normalize_maps_old_json():
    d = td.normalize(DATA)
    assert [b["role"] for b in d["beats"]] == ["dẫn dắt", "kết"] and d["beats"][0]["seconds"] == 4
    assert d["arc"]["skeleton"] == ["a", "b", "c", "d"] and d["winning_points"]["interrupts"][0]["t"] == "00:04"
    assert td.normalize(d) == d  # idempotent


import unittest as _ut
class _All(_ut.TestCase):
    pass
for _n, _f in list(globals().items()):
    if _n.startswith("test_") and callable(_f):
        setattr(_All, _n, (lambda f: lambda self: f())(_f))
if __name__ == "__main__":
    _ut.main()

class BlueprintAndCleanup(_ut.TestCase):
    def test_finish_upserts_arc_and_ideas_without_touching_repo(self):
        import tempfile, pathlib
        from unittest import mock
        d = pathlib.Path(tempfile.mkdtemp())
        (d / "patterns.md").write_text("# p\n", encoding="utf-8"); (d / "ideas.md").write_text("# i\n", encoding="utf-8")
        new = dict(DATA, arc={"name": "x", "skeleton": ["[a]", "[b]", "[c]", "[d]"]},
                   angles={"hi_oneup": {"idea": "ý comic", "hook": "h", "length_s": 150}, "vanhiep_tech": {"idea": "ý tech", "length_s": 60}})
        with mock.patch.object(td.ARC, "LIB", d / "index.json"), mock.patch.object(td.ARC, "PATTERNS", d / "patterns.md"), \
             mock.patch.object(td.ARC, "IDEAS", d / "ideas.md"), mock.patch.object(td, "find_clip", lambda s: None):
            meta = {"date": "2026-11-26", "video": "v.mp4", "cli": "agy", "model": "m", "source": "https://www.tiktok.com/@a/video/1"}
            td.finish("c1", new, meta, str(d / "td"))
            td.finish("c1", new, dict(meta), str(d / "td"))  # re-run: same evidence, no double count
        lib = json.loads((d / "index.json").read_text())
        self.assertEqual(lib["arcs"][0]["id"], "ARC-001"); self.assertEqual(lib["arcs"][0]["seen"], 1); self.assertEqual(len(lib["ideas"]), 2)
        self.assertIn("ARC-001", (d / "patterns.md").read_text()); self.assertIn("ý comic", (d / "ideas.md").read_text())
        self.assertIn("## Khối 5 — Reusable Story Arc (ARC-001)", (d / "td" / "c1.md").read_text())

    def test_downloaded_file_deleted_even_when_gemini_fails(self):
        import tempfile, sys as _sys
        from unittest import mock
        f = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False); f.close()
        def fail(*a, **k): raise SystemExit(3)
        with mock.patch.object(td, "download", lambda url: f.name), mock.patch.object(td, "run_engine", fail), \
             mock.patch.object(_sys, "argv", ["teardown.py", "--url", "https://www.tiktok.com/@a/video/1"]):
            with self.assertRaises(SystemExit): td.main()
        self.assertFalse(os.path.exists(f.name))
