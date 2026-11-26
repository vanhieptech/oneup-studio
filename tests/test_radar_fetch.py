# radar-fetch.py: local yt-dlp TikTok outlier radar collector + median_views baseline + trend-streams merge.
import importlib.util, json, os, tempfile
from pathlib import Path

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s_rf = importlib.util.spec_from_file_location("radar_fetch", os.path.join(R, "pipeline/scripts/radar-fetch.py"))
rf = importlib.util.module_from_spec(s_rf); s_rf.loader.exec_module(rf)

s_ts = importlib.util.spec_from_file_location("trend_streams", os.path.join(R, "pipeline/scripts/trend-streams.py"))
ts = importlib.util.module_from_spec(s_ts); s_ts.loader.exec_module(ts)


CFG = {
    "min_ratio": 3.0,
    "recent_limit": 10,
    "growth": {"min_hours": 24, "max_hours": 72, "min_pct": 0.5, "min_abs": 100},
    "channels": [
        {"handle": "manghocls", "platform": "tiktok", "url": "https://www.tiktok.com/@manghocls", "followers": 10000, "niche": ["hoc-tap"], "niche_verified": True},
        {"handle": "nofans_ch", "platform": "tiktok", "url": "https://www.tiktok.com/@nofans_ch", "followers": 0, "niche": ["productivity"], "niche_verified": False},
    ],
    "topics": {"productivity": ["thói quen", "trì hoãn"], "hoc-tap": ["ôn thi", "nhớ lâu"]},
}


def fake_fetcher(url, limit):
    if "manghocls" in url:
        return [
            {"id": "101", "title": "Cách ôn thi nhớ lâu #hoctap", "view_count": 45000, "like_count": 2000, "comment_count": 120, "duration": 55, "timestamp": 1732500000},
            {"id": "102", "title": "Một ngày bình thường", "view_count": 8000, "like_count": 300, "comment_count": 10, "duration": 30},
            {"id": "103", "title": "Review bàn học", "view_count": 9000, "like_count": 310, "comment_count": 12, "duration": 40},
        ], ""
    return [
        # No followers configured → median views of 5 videos = 5000; vid 201 has 20000 (4.0x median) & niche keyword
        {"id": "201", "title": "Hết trì hoãn bằng thói quen 2 phút", "view_count": 20000, "comment_count": 90, "duration": 48},
        {"id": "202", "title": "Thói quen sáng", "view_count": 5000, "comment_count": 10, "duration": 40},
        {"id": "203", "title": "Thói quen tối", "view_count": 5000, "comment_count": 12, "duration": 35},
        {"id": "205", "title": "Thói quen trưa", "view_count": 4000, "comment_count": 8, "duration": 30},
        {"id": "204", "title": "Đi ăn phở", "view_count": 50000, "comment_count": 200, "duration": 25},  # off-niche, not niche_verified
    ], ""


def test_radar_fetch_computes_follower_and_median_ratios():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        cfg_p = root / "radar.yaml"
        cfg_p.write_text(json.dumps(CFG), encoding="utf-8")
        res = rf.run_fetch("2026-11-26", cfg_path=cfg_p, root=root, fetcher=fake_fetcher, enqueue=False)
        ids = [r["id"] for r in res["rows"]]
        assert "manghocls-101" in ids
        assert "nofans_ch-201" in ids
        assert "nofans_ch-204" not in ids  # off-niche dropped
        r1 = next(r for r in res["rows"] if r["id"] == "manghocls-101")
        r2 = next(r for r in res["rows"] if r["id"] == "nofans_ch-201")
        assert r1["ratio_views_followers"] == 4.5 and r1["outlier_ratio"] == 5.0
        assert r2["ratio_views_followers"] is None and r2["outlier_ratio"] == 4.0
        assert (root / "2026-11-26/radar-raw.json").exists()
        assert (root / "2026-11-26/radar.json").exists()


def test_trend_streams_reads_radar_raw_snapshot():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        cfg_p = root / "radar.yaml"
        cfg_p.write_text(json.dumps(CFG), encoding="utf-8")
        rf.run_fetch("2026-11-26", cfg_path=cfg_p, root=root, fetcher=fake_fetcher, enqueue=False)
        rows = ts.radar("2026-11-26", CFG, root=root)
        assert {r["id"] for r in rows} == {"manghocls-101", "nofans_ch-201"}
