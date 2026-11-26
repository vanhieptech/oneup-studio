# apify-run.py (26/11/2026): outlier score, budget guard, missing token, token never in output.
import importlib.util, json, os, pytest
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec_ = importlib.util.spec_from_file_location("apify_run", os.path.join(R, "pipeline/scripts/apify-run.py"))
ar = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(ar)

def test_outlier_author_median_and_fans():
    items = [{"id": i, "playCount": p, "authorMeta": {"name": "a", "fans": 100}} for i, p in ((1, 10), (2, 20), (3, 90))]
    items.append({"id": 4, "playCount": 500, "authorMeta": {"name": "b", "fans": 50}})
    s = ar.outlier_scores(items)
    assert s["3"] == {"outlier": 4.5, "basis": "author_median"} and s["4"] == {"outlier": 10.0, "basis": "fans"}

def test_missing_token(monkeypatch):
    monkeypatch.setattr(ar.P, "tools_env", lambda k: "")
    with pytest.raises(SystemExit) as e: ar.token()
    assert "APIFY_TOKEN missing" in str(e.value)

def test_budget_counts_existing_runs(tmp_path):
    c = tmp_path / "cost.json"
    ar.save_cost(c, {"actor": "x", "usd": 0.1}); ar.save_cost(c, {"actor": "y", "usd": 0.06})
    assert abs(ar.spent_today(c) - 0.16) < 1e-9 and json.loads(c.read_text())["total_usd"] == 0.16

def test_http_error_hides_token(monkeypatch):
    import urllib.request, urllib.error, io
    monkeypatch.setattr(ar.P, "tools_env", lambda k: "apify_api_SECRET123")
    def boom(req, timeout=0): raise urllib.error.HTTPError(req.full_url, 400, "Bad", {}, io.BytesIO(b'{"error":"bad input"}'))
    monkeypatch.setattr(urllib.request, "urlopen", boom)
    with pytest.raises(SystemExit) as e: ar.http("GET", "https://api.apify.com/v2/x?y=1")
    assert "SECRET" not in str(e.value) and "HTTP 400" in str(e.value)
