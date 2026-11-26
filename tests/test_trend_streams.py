# trend-streams.py (26/11): three trend inputs — radar (Luồng 1), upstream scoring (Luồng 2), inbox + teardown queue (Luồng 3).
import importlib.util, json, os, tempfile, datetime as dt
from pathlib import Path
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = importlib.util.spec_from_file_location("trend_streams", os.path.join(R, "pipeline/scripts/trend-streams.py"))
ts = importlib.util.module_from_spec(s); s.loader.exec_module(ts)

CFG = {"min_ratio": 3.0, "growth": {"min_hours": 24, "max_hours": 72, "min_pct": 0.5, "min_abs": 100},
       "topics": {"productivity": ["thói quen", "trì hoãn"], "ai": ["chatgpt", "ai"]}}

def clip(vid, fans, views, caption, tags=(), comments=10, shares=5, author="kenh"):
    return {"url": f"https://www.tiktok.com/@{author}/video/{vid}", "caption": caption, "hashtags": list(tags),
            "author": {"name": author, "fans": fans}, "play_count": views, "comment_count": comments, "share_count": shares}

def write_day(root, day, clips):
    d = root / day / "apify"; d.mkdir(parents=True, exist_ok=True)
    (d / "clips.json").write_text(json.dumps({"measured_at": f"{day}T12:00:00", "clips": clips}), encoding="utf-8")

def test_ratio_outlier_in_niche_kept_off_niche_dropped():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        write_day(root, "2026-11-26", [clip(1, 1000, 7600, "Bỏ thói quen trì hoãn"), clip(2, 1000, 9000, "Nấu ăn ngon"),
                                       clip(3, 1000, 2000, "thói quen tốt")])
        rows = ts.radar("2026-11-26", CFG, root)
        assert [r["id"] for r in rows] == ["kenh-1"] and rows[0]["ratio_views_followers"] == 7.6 and rows[0]["topic_tags"] == ["productivity"]

def test_short_keyword_ai_needs_hashtag_or_uppercase():
    assert ts.topic_tags(clip(1, 1, 1, "ai cũng từng trì trệ"), {"ai": ["ai"]}) == []
    assert ts.topic_tags(clip(1, 1, 1, "Dùng AI để học"), {"ai": ["ai"]}) == ["ai"]
    assert ts.topic_tags(clip(1, 1, 1, "học", tags=["ai"]), {"ai": ["ai"]}) == ["ai"]

def test_growth_spike_between_snapshots():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        write_day(root, "2026-11-24", [clip(9, 100000, 50000, "trì hoãn", comments=200, shares=100)])
        write_day(root, "2026-11-26", [clip(9, 100000, 90000, "trì hoãn", comments=500, shares=200)])
        rows = ts.radar("2026-11-26", CFG, root)
        assert rows and rows[0]["reasons"] == ["growth spike"] and rows[0]["growth"]["delta"] == 400 and rows[0]["growth"]["hours"] == 48.0
        assert rows[0]["growth"]["save_counted"] is False

def test_upstream_scoring_and_missing():
    raw = {"items": [{"id": "a", "stream": "upstream", "shortlist": True, "pain": 4, "story": 5, "fit": {"hi_oneup": 2, "vanhiep_tech": 5}},
                     {"id": "b", "stream": "vn-tech", "shortlist": True, "pain": 3},
                     {"id": "c", "stream": "general", "shortlist": True}]}
    short, missing = ts.upstream(raw)
    assert [i["id"] for i in short] == ["a", "b"] and missing == ["b"]
    assert short[0]["upstream_score"] == 0.8 and short[0]["channel"] == "vanhiep_tech"

def test_inbox_ids_dedupe_and_mark_done():
    with tempfile.TemporaryDirectory() as d:
        d = Path(d); inbox = d / "inbox"; inbox.mkdir()
        (inbox / "links.txt").write_text("xem nè https://www.tiktok.com/@a/video/111?lang=vi\nhttps://www.tiktok.com/@b/video/222\n", encoding="utf-8")
        (inbox / "clip.mp4").write_bytes(b"fake-video")
        ingest = d / "ingest.md"; ingest.write_text("# ingest\n| x | [b](https://tiktok.com/@b/video/222/) |\n\n## Khác\n", encoding="utf-8")
        q = d / "queue.json"
        new, dup = ts.inbox("2026-11-26", inbox_dir=inbox, queue=q, ingest=ingest)
        assert [r["id"] for r in new] == ["trends-2026-11-26-01", "trends-2026-11-26-02"] and dup == 1
        again, dup2 = ts.inbox("2026-11-26", inbox_dir=inbox, queue=q, ingest=ingest)
        assert again == [] and dup2 == 3
        t = ingest.read_text(encoding="utf-8")
        assert ts.INBOX_HEAD in t and "trends-2026-11-26-01" in t and t.index(ts.INBOX_HEAD) > t.index("## Khác")  # new section at the end
        ingest.write_text(t + "\n## Sau\nx\n", encoding="utf-8"); (inbox / "more.url").write_text("https://youtu.be/zzz", encoding="utf-8")
        ts.inbox("2026-11-26", inbox_dir=inbox, queue=q, ingest=ingest)
        t = ingest.read_text(encoding="utf-8")
        assert t.index("trends-2026-11-26-03") < t.index("## Sau")  # rows go inside the Inbox section
        ts.mark_done("trends-2026-11-26-01", "research/trends/2026-11-26/teardowns/x.md", queue=q, ingest=ingest)
        assert json.loads(q.read_text())["items"][0]["status"] == "done"
        assert "| done | research/trends/2026-11-26/teardowns/x.md |" in ingest.read_text(encoding="utf-8")

def test_teardown_cmd_has_queue_id():
    assert "--queue-id trends-2026-11-26-01" in ts.teardown_cmd({"id": "trends-2026-11-26-01", "kind": "url", "source": "https://x"})
