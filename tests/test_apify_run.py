# apify-run.py (26/11/2026): outlier score, budget guard, missing token, token never in output.
import importlib.util, io, json, os, tempfile, unittest, urllib.error, urllib.request
from unittest import mock
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec_ = importlib.util.spec_from_file_location("apify_run", os.path.join(R, "pipeline/scripts/apify-run.py"))
ar = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(ar)

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

    def test_http_error_hides_token(self):
        def boom(req, timeout=0): raise urllib.error.HTTPError(req.full_url, 400, "Bad", {}, io.BytesIO(b'{"error":"bad input"}'))
        with mock.patch.object(ar.P, "tools_env", lambda k: "tok_SECRET123"), mock.patch.object(urllib.request, "urlopen", boom):
            with self.assertRaises(SystemExit) as e: ar.http("GET", "https://api.apify.com/v2/x?y=1")
        self.assertNotIn("SECRET", str(e.exception)); self.assertIn("HTTP 400", str(e.exception))

if __name__ == "__main__":
    unittest.main()
