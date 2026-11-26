# gate0.py (26/11): the 4-piece Gate 0 brief — timing plans per channel and draft insertion.
import importlib.util, os, tempfile
from pathlib import Path
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = importlib.util.spec_from_file_location("gate0", os.path.join(R, "pipeline/scripts/gate0.py"))
g = importlib.util.module_from_spec(s); s.loader.exec_module(g)

ARC = {"id": "ARC-T", "skeleton": ["[hook]", "[vấn đề]", "[lật kèo]", "[áp dụng]", "[kết]"],
       "beats": [{"role": "hook", "seconds": 4}, {"role": "câu hỏi", "seconds": 20}, {"role": "lật kèo", "seconds": 12},
                 {"role": "áp dụng", "seconds": 16}, {"role": "kết", "seconds": 6}]}

def test_hi_plan_keeps_hook_short_and_loops_every_35_45s():
    rows, loops = g.plan_hi(ARC, 150)
    assert rows[0]["to"] <= 8 and rows[-1]["to"] == 150
    gaps = [b["at"] - a["at"] for a, b in zip(loops, loops[1:])]
    assert loops and all(35 <= x <= 45 for x in gaps) and 35 <= loops[0]["at"] - 3 <= 45

def test_vht_plan_layer_counts_follow_3_5s():
    rows = g.plan_vht(ARC, 60)
    assert rows[-1]["to"] == 60
    lo, hi = map(int, rows[1]["layers"].split("–"))
    d = rows[1]["to"] - rows[1]["from"]
    assert lo == max(1, d // 5) and hi >= d // 3

def test_brief_has_four_pieces_and_never_invents():
    b = g.brief("xyzzy qwertz plugh", "hi")
    for h in ("### 1.", "### 2.", "### 3.", "### 4."): assert h in b
    assert "chưa có dòng nào khớp" in b

def test_write_into_replaces_block_after_front_matter():
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / "draft.md"; f.write_text("---\ntitle: x\n---\n# Nháp\n", encoding="utf-8")
        g.write_into(f, f"{g.BEGIN}\nA\n{g.END}\n"); g.write_into(f, f"{g.BEGIN}\nB\n{g.END}\n")
        t = f.read_text(encoding="utf-8")
        assert t.startswith("---\ntitle: x\n---") and t.count(g.BEGIN) == 1 and "\nB\n" in t and "# Nháp" in t


def test_brief_prioritizes_highest_win_rate_arc_when_arc_omitted():
    from unittest import mock
    fake_lib = {
        "arcs": [
            {"id": "ARC-001", "name": "Cũ", "skeleton": ["[a]"], "beats": [{"role": "hook", "seconds": 5}], "seen": 5, "uses": 4, "wins": 1, "win_rate": 0.25, "evidence": []},
            {"id": "ARC-002", "name": "Thắng cao", "skeleton": ["[b]"], "beats": [{"role": "hook", "seconds": 5}], "seen": 1, "uses": 3, "wins": 3, "win_rate": 1.0, "evidence": []},
        ],
        "ideas": [],
    }
    with mock.patch.object(g.ARC, "load", lambda *a, **k: fake_lib):
        out = g.brief("xyzzy unmatched topic", "hi")
    assert "**ARC-002**" in out and "win_rate: 100% (3/3)" in out
