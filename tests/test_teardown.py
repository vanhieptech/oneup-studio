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
    for h in ("## 2. Hook", "## 3. Xương sống", "## 5. Nhịp", "## 11. Công thức khung"): assert h in md


import unittest as _ut
class _All(_ut.TestCase):
    pass
for _n, _f in list(globals().items()):
    if _n.startswith("test_") and callable(_f):
        setattr(_All, _n, (lambda f: lambda self: f())(_f))
if __name__ == "__main__":
    _ut.main()

class BlueprintAndCleanup(_ut.TestCase):
    def test_merge_blueprint_seen_and_new(self):
        import tempfile, pathlib
        p = pathlib.Path(tempfile.mkdtemp()) / "index.json"
        a = td.merge_blueprint(["kể chuyện hụt", "hỏi vì sao", "nghiên cứu trả lời", "cách làm nhỏ"], "u1", path=p)
        b = td.merge_blueprint(["kể chuyện hụt", "hỏi vì sao", "nghiên cứu trả lời", "cách làm nhỏ nhất"], "u2", path=p)
        c = td.merge_blueprint(["danh sách 5 mẹo", "mẹo bất ngờ cuối"], "u3", path=p)
        lib = json.loads(p.read_text())
        self.assertEqual(a, b); self.assertNotEqual(a, c)
        self.assertEqual(lib["modes"][0]["seen"], 2); self.assertEqual(lib["modes"][0]["sources"], ["u1", "u2"])

    def test_downloaded_file_deleted_even_when_gemini_fails(self):
        import tempfile, sys as _sys
        from unittest import mock
        f = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False); f.close()
        def fail(*a, **k): raise SystemExit(3)
        with mock.patch.object(td, "download", lambda url: f.name), mock.patch.object(td, "run_engine", fail), \
             mock.patch.object(_sys, "argv", ["teardown.py", "--url", "https://www.tiktok.com/@a/video/1"]):
            with self.assertRaises(SystemExit): td.main()
        self.assertFalse(os.path.exists(f.name))
