# pattern-synthesize.py + gate0.py synthesis weights & style-pairs integration tests.
import importlib.util
import json
import os
import tempfile
from pathlib import Path
from unittest import mock

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_s_ps = importlib.util.spec_from_file_location("pattern_synthesize", os.path.join(R, "pipeline/scripts/pattern-synthesize.py"))
ps = importlib.util.module_from_spec(_s_ps)
_s_ps.loader.exec_module(ps)

_s_g0 = importlib.util.spec_from_file_location("gate0", os.path.join(R, "pipeline/scripts/gate0.py"))
g0 = importlib.util.module_from_spec(_s_g0)
_s_g0.loader.exec_module(g0)


def _write_td(td_dir, cid, doc):
    td_dir.mkdir(parents=True, exist_ok=True)
    (td_dir / f"{cid}.json").write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")


SAMPLE_TDS = [
    (
        "direct-1",
        {
            "role": "direct_niche",
            "_meta": {"date": "2026-11-26", "arc": "ARC-001"},
            "apify": {"play_count": 300000, "author": {"name": "c1", "fans": 50000}, "outlier_ratio": 6.0},
            "hook": {"spoken": "3 cách nhớ bài nhanh", "mechanism": "tò mò"},
            "beats": [
                {"role": "hook", "seconds": 4, "transition": "Jump cut kèm tiêu đề vàng"},
                {"role": "giải thích", "seconds": 20, "transition": "Nhưng mà khoan, lật giả định"},
            ],
            "winning_points": {"interrupts_per_10s": 2.4, "best_metaphor": {"text": "não như RAM đầy"}},
            "craft_transfer": {
                "metaphor_transfer": "ví trí nhớ ngắn hạn như tờ giấy nháp",
                "pacing_3_5s": "đổi đạo cụ mỗi 4 giây",
            },
        },
    ),
    (
        "cross-1",
        {
            "role": "cross_niche_craft",
            "_meta": {"date": "2026-11-26", "arc": "ARC-002"},
            "apify": {"play_count": 900000, "author": {"name": "veritasium", "fans": 0}, "outlier_ratio": 8.0},
            "hook": {"spoken": "Cái bạn tin về trí nhớ đang ngược hoàn toàn", "mechanism": "phản trực giác"},
            "beats": [
                {"role": "hook", "seconds": 3, "transition": "Câu hỏi lửng mở vòng: tại sao?"},
                {"role": "lật kèo", "seconds": 18, "transition": "Jump cut sang thí nghiệm thật"},
            ],
            "winning_points": {"interrupts_per_10s": 3.2},
            "craft_transfer": {
                "metaphor_transfer": "ví ma sát học tập như tạ tập gym",
                "pacing_3_5s": "cắt góc + zoom mỗi 3 giây",
            },
        },
    ),
    (
        "cross-2",
        {
            "role": "cross_niche_craft",
            "_meta": {"date": "2026-11-26", "arc": "ARC-002"},
            "apify": {"play_count": 500000, "author": {"name": "fireship", "fans": 0}, "outlier_ratio": 5.0},
            "hook": {"spoken": "Mọi người đang dùng JWT sai chỗ", "mechanism": "phản trực giác"},
            "beats": [
                {"role": "hook", "seconds": 3, "transition": "Jump cut kèm nhãn số thứ tự"},
                {"role": "kết", "seconds": 6, "transition": "Ngắt nhịp tách phần kết"},
            ],
            "winning_points": {"interrupts_per_10s": 3.8},
            "craft_transfer": {
                "metaphor_transfer": "localStorage như dán chìa khóa nhà ngoài cửa",
                "pacing_3_5s": "đổi diagram overlay mỗi 3 giây",
            },
        },
    ),
    (
        "anti-1",
        {
            "role": "anti_pattern",
            "_meta": {"date": "2026-11-26"},
            "apify": {"play_count": 400000, "author": {"name": "bait", "fans": 10000}, "outlier_ratio": 10.0},
            "hook": {"spoken": "Bí mật triệu đô không ai dám nói", "mechanism": "câu view"},
            "why_it_works": [{"claim": "hook giật gân nhưng thân bài rỗng"}],
        },
    ),
]


def test_skips_when_fewer_than_min_teardowns():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        _write_td(root / "2026-11-26/teardowns", "only-1", SAMPLE_TDS[0][1])
        res = ps.run_synthesize(trends_dir=root, min_teardowns=3, out_md=root / "w.md", out_json=root / "w.json")
        assert res["skipped"] is True and res["ok"] is False
        assert not (root / "w.md").exists()


def test_synthesizes_multi_role_teardowns_and_writes_outputs():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        td_dir = root / "2026-11-26/teardowns"
        for cid, doc in SAMPLE_TDS:
            _write_td(td_dir, cid, doc)
        res = ps.run_synthesize(
            trends_dir=root, min_teardowns=3, out_md=root / "weekly-synthesis.md",
            out_json=root / "weekly-synthesis.json", date="2026-11-26",
        )
        assert res["ok"] is True and res["skipped"] is False
        r = res["result"]
        assert r["teardown_count"] == 4
        assert r["role_counts"]["cross_niche_craft"] == 2
        assert r["role_counts"]["anti_pattern"] == 1
        # Cross-niche phản trực giác (2 clips, weighted 8*1.15 + 5*1.15 = 14.95) beats direct tò mò (6.0)
        assert r["top_hooks"][0]["key"] == "phản trực giác"
        assert len(r["top_transitions"]) >= 2
        assert r["arc_weights"]["ARC-002"] > r["arc_weights"]["ARC-001"]
        assert len(r["anti_patterns"]) == 1
        md = (root / "weekly-synthesis.md").read_text(encoding="utf-8")
        assert "id: trends.weekly-synthesis" in md
        assert "## 1. Top 5 kiểu Hook đang thắng" in md
        assert "## 4. Anti-Pattern cần tránh" in md


def test_gate0_uses_synthesis_weights_and_embeds_style_pairs():
    fake_lib = {
        "arcs": [
            {"id": "ARC-001", "name": "Cũ", "skeleton": ["[a]"], "beats": [{"role": "hook", "seconds": 5}], "seen": 2, "uses": 0, "wins": 0, "win_rate": None, "evidence": []},
            {"id": "ARC-002", "name": "Thắng tuần", "skeleton": ["[b]"], "beats": [{"role": "hook", "seconds": 4}], "seen": 2, "uses": 0, "wins": 0, "win_rate": None, "evidence": []},
        ],
        "ideas": [],
    }
    fake_synth = {
        "arc_weights": {"ARC-002": 13.0, "ARC-001": 4.0},
        "top_hooks": [{"mechanism": "phản trực giác", "weight": 14.95}],
    }
    with mock.patch.object(g0.ARC, "load", lambda *a, **k: fake_lib), \
         mock.patch.object(g0, "load_weekly_synthesis", lambda *a, **k: fake_synth):
        out = g0.brief("trì hoãn thói quen", "hi")
    assert "**ARC-002**" in out
    assert "Style Few-Shot" in out
    assert "SP-" in out
    assert "Tổng hợp đa video" in out
    # Tech channel should prioritize @vanhiep.tech style pair SP-14
    vht_pairs = g0.pick_style_pairs("bảo mật jwt api lập trình", "vht", n=3)
    assert vht_pairs and vht_pairs[0]["id"] == "SP-14"


def test_story_warm_skips_choppy_pairs_and_keeps_subject():
    pairs = g0.pick_style_pairs("thói quen nản giày chạy", "hi", n=3, tone="story_warm")
    assert [p["id"] for p in pairs] == ["SP-01", "SP-09", "SP-13"]
    for p in pairs:
        low = f" {p['approved'].lower()} "
        assert p["tone"] == "story_warm"
        assert " mình " in low or " bạn " in low


def test_tone_story_warm_picks_tagged_arc_not_heavier_listicle():
    fake_lib = {
        "arcs": [
            {"id": "ARC-001", "name": "Liệt kê", "tone": "tech_sharp", "skeleton": ["[a]"], "beats": [{"role": "hook", "seconds": 5}], "seen": 2, "uses": 0, "wins": 0, "win_rate": None, "evidence": []},
            {"id": "ARC-002", "name": "Đồng cảm", "tone": "story_warm", "skeleton": ["[b]"], "beats": [{"role": "dẫn dắt", "seconds": 18}], "seen": 0, "uses": 0, "wins": 0, "win_rate": None, "evidence": []},
        ],
        "ideas": [],
    }
    fake_synth = {"arc_weights": {"ARC-001": 20.0, "ARC-002": 0.1}, "top_hooks": []}
    with mock.patch.object(g0.ARC, "load", lambda *a, **k: fake_lib), \
         mock.patch.object(g0, "load_weekly_synthesis", lambda *a, **k: fake_synth):
        out = g0.brief("thói quen nản", "hi", tone="story_warm")
    assert "**ARC-002**" in out
    assert "SP-06" not in out
    assert "tone `story_warm`" in out
