# arc_library (26/11): ARC-NNN story arcs — upsert by similarity, evidence keyed by source, generated views, SM migration.
import json, os, sys, tempfile
from pathlib import Path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pipeline"))
import arc_library as A

ARC1 = {"name": "lời hứa số lượng", "skeleton": ["[Lời hứa số lượng + chuẩn đáng tin]", "[Từ chuyển nhịp] rồi cắt vào ý 1",
                                                 "[Tên giải pháp] → [cơ chế] → [con số]", "[Câu hỏi mở] kéo bình luận"],
        "beats": [{"role": "hook"}, {"role": "dẫn dắt"}, {"role": "giải thích"}, {"role": "kết"}]}
ARC2 = {"name": "chuyện hụt", "skeleton": ["[Khoảnh khắc thất bại cá nhân]", "[Câu hỏi vì sao]", "[Nghiên cứu lật kèo]", "[Việc nhỏ làm ngay]"],
        "beats": [{"role": "hook"}, {"role": "câu hỏi"}, {"role": "lật kèo"}, {"role": "áp dụng"}]}

def tmp():
    d = Path(tempfile.mkdtemp()); return d / "index.json"

def test_new_then_same_arc_adds_evidence():
    p = tmp()
    a, new_a = A.upsert_arc(ARC1, {"source": "u1", "creator": "manghocls", "ratio": 7.64}, p)
    b, new_b = A.upsert_arc(dict(ARC1, skeleton=ARC1["skeleton"][:3] + ["[Câu hỏi mở cuối] kéo bình luận"]), {"source": "u2", "ratio": 4.1}, p)
    c, new_c = A.upsert_arc(ARC2, {"source": "u3"}, p)
    assert (a, new_a, b, new_b) == ("ARC-001", True, "ARC-001", False) and (c, new_c) == ("ARC-002", True)
    assert A.load(p)["arcs"][0]["seen"] == 2

def test_same_source_not_double_counted():
    p = tmp()
    A.upsert_arc(ARC1, {"source": "u1"}, p); A.upsert_arc(ARC1, {"source": "u1", "ratio": 7.6}, p)
    arc = A.load(p)["arcs"][0]
    assert arc["seen"] == 1 and arc["evidence"][0]["ratio"] == 7.6

def test_migrates_script_modes():
    p = tmp(); p.write_text(json.dumps({"modes": [{"id": "SM01", "formula": ARC1["skeleton"], "seen": 1, "uses": 0, "wins": 0, "sources": ["u1"]}]}))
    lib = A.load(p)
    assert lib["arcs"][0]["id"] == "ARC-001" and lib["arcs"][0]["legacy_id"] == "SM01" and "modes" not in lib

def test_rendered_views_replace_block_in_place():
    d = Path(tempfile.mkdtemp()); p = d / "index.json"; pat = d / "patterns.md"; ide = d / "ideas.md"
    pat.write_text("# P\n\n## Learnings log\nx\n", encoding="utf-8"); ide.write_text("# I\n", encoding="utf-8")
    A.upsert_arc(ARC1, {"source": "u1", "creator": "manghocls", "ratio": 7.64, "teardown": "research/trends/2026-11-26/teardowns/m.md"}, p)
    A.push_ideas("ARC-001", {"hi_oneup": {"idea": "comic về dời việc", "length_s": 150}}, "research/trends/2026-11-26/teardowns/m.md", "2026-11-26", p)
    A.render_patterns(p, pat); A.render_patterns(p, pat); A.render_ideas(p, ide)
    t = pat.read_text(encoding="utf-8")
    assert t.count(A.ARC_BEGIN) == 1 and "manghocls 7.64x" in t and "ARC-001" in t
    assert "comic về dời việc" in ide.read_text(encoding="utf-8") and "@hi.oneup" in ide.read_text(encoding="utf-8")

def test_reteardown_same_source_refreshes_not_forks():
    p = tmp(); p.write_text(json.dumps({"modes": [{"id": "SM01", "formula": ["prose step one", "prose step two"], "seen": 1, "uses": 0, "wins": 0, "sources": ["u1"]}]}))
    a, new = A.upsert_arc(ARC1, {"source": "u1", "ratio": 7.64}, p)
    lib = A.load(p)
    assert (a, new, len(lib["arcs"])) == ("ARC-001", False, 1) and lib["arcs"][0]["skeleton"] == ARC1["skeleton"] and lib["arcs"][0]["legacy_id"] == "SM01"


def test_sync_published_updates_uses_wins_win_rate_and_patterns():
    d = Path(tempfile.mkdtemp())
    idx = d / "index.json"
    pat = d / "patterns.md"
    pub = d / "published"
    pub.mkdir()
    pat.write_text("# Patterns\n", encoding="utf-8")
    A.upsert_arc(ARC1, {"source": "u1", "creator": "manghocls", "ratio": 7.64}, idx)
    A.upsert_arc(ARC2, {"source": "u2", "creator": "other", "ratio": 4.2}, idx)

    (pub / "README.md").write_text(
        "# Published\n\n"
        "| Ngày giờ (VN) | Clip | Link TikTok | Caption | Views 24h | Views 7d | Giữ chân 3s | Xem hết % | Share | Save | ARC | Mã hook | Ghi chú |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|\n"
        "| 2026-11-20 | clip-01 | https://t/1 | c1 | 8.000 | 45.000 | 68% | 38% | 400 | 900 | ARC-001 | P01 | tốt |\n"
        "| 2026-11-22 | clip-02 | https://t/2 | c2 | 2.000 | 4.500 | 40% | 15% | 10 | 20 | ARC-001 | P03 | yếu |\n"
        "| 2026-11-24 | clip-03 | https://t/3 | c3 | 12k | 62k | 72% | 41% | 800 | 1200 | ARC-002 | P06 | đỉnh |\n"
        "| 2026-11-25 | clip-04 | https://t/4 | c4 | | | | | | | ARC-002 | P06 | chưa có số |\n",
        encoding="utf-8",
    )

    res = A.sync_published(published_dir=pub, path=idx, patterns=pat)
    assert res["records"] == 4
    lib = A.load(idx)
    a1 = next(x for x in lib["arcs"] if x["id"] == "ARC-001")
    a2 = next(x for x in lib["arcs"] if x["id"] == "ARC-002")
    # ARC-001: 2 uses, 1 win (clip-01 beats median/target; clip-02 fails) → 50%
    assert a1["uses"] == 2 and a1["wins"] == 1 and a1["win_rate"] == 0.5
    # ARC-002: 2 uses, 1 win (clip-03 wins; clip-04 has empty metrics → NOT a win) → 50%
    assert a2["uses"] == 2 and a2["wins"] == 1 and a2["win_rate"] == 0.5
    # Rendered patterns.md includes win_rate column and 50%
    ptxt = pat.read_text(encoding="utf-8")
    assert "| win_rate |" in ptxt and "| 50% |" in ptxt


def test_best_arc_prioritizes_highest_win_rate():
    arcs = [
        {"id": "ARC-001", "seen": 5, "uses": 4, "wins": 1, "win_rate": 0.25},
        {"id": "ARC-002", "seen": 1, "uses": 2, "wins": 2, "win_rate": 1.0},
        {"id": "ARC-003", "seen": 9, "uses": 0, "wins": 0, "win_rate": None},
    ]
    assert A.best_arc(arcs)["id"] == "ARC-002"
