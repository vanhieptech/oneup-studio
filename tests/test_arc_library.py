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
