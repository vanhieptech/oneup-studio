# tinyfish-monitors.py (26/11/2026): --plan makes no API call, --create refuses without explicit cost approval, --pull parses results.
import importlib.util, io, json, os, subprocess, types, unittest
from contextlib import redirect_stdout
from unittest import mock
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec_ = importlib.util.spec_from_file_location("tinyfish_monitors", os.path.join(R, "pipeline/scripts/tinyfish-monitors.py"))
tm = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(tm)

class Monitors(unittest.TestCase):
    def test_plan_makes_no_call(self):
        with mock.patch.object(subprocess, "run", side_effect=AssertionError("no API call in --plan")), redirect_stdout(io.StringIO()) as o:
            tm.plan()
        self.assertEqual(o.getvalue().count("monitor create"), 4)

    def test_create_refuses_without_flag(self):
        with mock.patch.object(subprocess, "run", side_effect=AssertionError("must not create")), redirect_stdout(io.StringIO()):
            self.assertEqual(tm.create(False), 1)

    def test_extract_results(self):
        m = {"name": "oneup-x", "last_run": {"results": [{"title": "t", "url": "https://www.tiktok.com/@a/video/1", "snippet": "s"}]}}
        r = tm.extract_results(m)
        self.assertEqual(r[0]["monitor"], "oneup-x"); self.assertEqual(r[0]["url"], "https://www.tiktok.com/@a/video/1")

    def test_monthly_cost(self):
        self.assertEqual(tm.monthly_cost(), 0.6)

if __name__ == "__main__":
    unittest.main()
