# apify-run.py (26/11/2026): outlier score, budget guard, missing token, token never in output.
import importlib.util, io, json, os, tempfile, unittest, urllib.error, urllib.request
from unittest import mock
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec_ = importlib.util.spec_from_file_location("apify_run", os.path.join(R, "pipeline/scripts/apify-run.py"))
ar = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(ar)
spec_c = importlib.util.spec_from_file_location("trend_collect", os.path.join(R, "pipeline/scripts/trend-collect.py"))
tc = importlib.util.module_from_spec(spec_c); spec_c.loader.exec_module(tc)

class ApifyRun(unittest.TestCase):
    def test_outlier_author_median_and_fans(self):
        items = [{"id": i, "playCount": p, "authorMeta": {"name": "a", "fans": 100}} for i, p in ((1, 10), (2, 20), (3, 90))]
        items.append({"id": 4, "playCount": 500, "authorMeta": {"name": "b", "fans": 50}})
        s = ar.outlier_scores(items)
        self.assertEqual(s["3"], {"outlier": 4.5, "basis": "author_median"})
        self.assertEqual(s["4"], {"outlier": 10.0, "basis": "fans"})

    def test_missing_token(self):
        with mock.patch.object(ar.P, "tools_env", lambda k: ""):
            with self.assertRaises(SystemExit) as e: ar.token()
        self.assertIn("APIFY_TOKEN missing", str(e.exception))

    def test_budget_counts_existing_runs(self):
        with tempfile.TemporaryDirectory() as d:
            c = ar.Path(d) / "cost.json"
            ar.save_cost(c, {"actor": "x", "usd": 0.1}); ar.save_cost(c, {"actor": "y", "usd": 0.06})
            self.assertAlmostEqual(ar.spent_today(c), 0.16)
            self.assertEqual(json.loads(c.read_text())["total_usd"], 0.16)

    def _cfg(self):
        return ar.load_cfg()

    def _candidates(self, root, date, urls):
        p = ar.Path(root) / "research" / "trends" / date / "tinyfish"
        p.mkdir(parents=True)
        path = p / "tiktok-candidates.json"
        path.write_text(json.dumps([{"url": u} for u in urls]))
        return path

    def test_bare_run_breaks_when_candidates_missing(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(SystemExit) as e:
                ar.resolve_tiktok_input(["--date", "2026-11-28"], "2026-11-28", self._cfg(), ar.Path(d))
        self.assertIn("BREAK trend-digest", str(e.exception))
        self.assertIn("hashtag", str(e.exception))

    def test_bare_run_breaks_when_candidates_exist(self):
        with tempfile.TemporaryDirectory() as d:
            self._candidates(d, "2026-11-28", ["https://www.tiktok.com/@a/video/1"])
            with self.assertRaises(SystemExit) as e:
                ar.resolve_tiktok_input(["--date", "2026-11-28"], "2026-11-28", self._cfg(), ar.Path(d))
        self.assertIn("BREAK trend-digest", str(e.exception))
        self.assertIn("--urls-from", str(e.exception))

    def test_max_urls_refuses_silent_cut(self):
        with tempfile.TemporaryDirectory() as d:
            path = self._candidates(d, "2026-11-28", [f"https://www.tiktok.com/@a/video/{i}" for i in range(3)])
            argv = ["--urls-from", str(path), "--max-urls", "1", "--allow-comment-sample"]
            with self.assertRaises(SystemExit) as e:
                ar.resolve_tiktok_input(argv, "2026-11-28", self._cfg(), ar.Path(d))
        self.assertIn("Không cắt im lặng", str(e.exception))

    def test_comment_sample_refuses_silent_top3(self):
        with tempfile.TemporaryDirectory() as d:
            path = self._candidates(d, "2026-11-28", [f"https://www.tiktok.com/@a/video/{i}" for i in range(4)])
            with self.assertRaises(SystemExit) as e:
                ar.resolve_tiktok_input(["--urls-from", str(path)], "2026-11-28", self._cfg(), ar.Path(d))
        self.assertIn("mẫu comment", str(e.exception))

    def test_urls_from_keeps_every_link(self):
        with tempfile.TemporaryDirectory() as d:
            path = self._candidates(d, "2026-11-28", [f"https://www.tiktok.com/@a/video/{i}" for i in range(4)])
            inp, mode = ar.resolve_tiktok_input(
                ["--urls-from", str(path), "--comments", "4"], "2026-11-28", self._cfg(), ar.Path(d))
        self.assertEqual(mode, "urls")
        self.assertEqual(len(inp["postURLs"]), 4)
        self.assertNotIn("hashtags", inp)
        self.assertNotIn("searchQueries", inp)

    def test_hashtag_basket_only_when_asked(self):
        with tempfile.TemporaryDirectory() as d:
            inp, mode = ar.resolve_tiktok_input(["--allow-hashtag-basket"], "2026-11-28", self._cfg(), ar.Path(d))
        self.assertEqual(mode, "hashtag-basket")
        self.assertIn("trihoan", inp["hashtags"])

    def test_http_error_hides_token(self):
        def boom(req, timeout=0): raise urllib.error.HTTPError(req.full_url, 400, "Bad", {}, io.BytesIO(b'{"error":"bad input"}'))
        with mock.patch.object(ar.P, "tools_env", lambda k: "tok_SECRET123"), mock.patch.object(urllib.request, "urlopen", boom):
            with self.assertRaises(SystemExit) as e: ar.http("GET", "https://api.apify.com/v2/x?y=1")
        self.assertNotIn("SECRET", str(e.exception)); self.assertIn("HTTP 400", str(e.exception))

class TrendCollectBreak(unittest.TestCase):
    def test_collect_without_x_file_breaks_before_fetch(self):
        with self.assertRaises(SystemExit) as e:
            tc.require_x_extra(["--date", "2026-11-28"], "2026-11-28")
        self.assertIn("BREAK trend-digest", str(e.exception))
        self.assertIn("--extra", str(e.exception))

    def test_allow_without_x_is_explicit(self):
        self.assertIsNone(tc.require_x_extra(["--allow-without-x"], "2026-11-28"))

if __name__ == "__main__":
    unittest.main()
