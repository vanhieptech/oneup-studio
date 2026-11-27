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


# --- WS1 (27/11): ONEUP-CORE-ARC is the @hi.oneup default; approved-clip rhythm is loaded -------------------------
def test_hi_default_is_core_arc_with_60_90s_window():
    out = g.brief("xyzzy unmatched topic", "hi")
    assert "**ONEUP-CORE-ARC**" in out and "180–290 âm tiết" in out and "Đủ ý thì dừng" in out
    assert "gợi ý **65s**" in out
    assert "gợi ý **90s**" in g.brief("xyzzy", "hi", length=150)  # capped to the core window


def test_extended_lifts_core_window_to_120_180s():
    out = g.brief("xyzzy", "hi", length=150, extended=True)
    assert "gợi ý **150s**" in out and "--extended" in out


def test_explicit_arc_and_vht_do_not_use_core_arc():
    assert "**ARC-002**" in g.brief("xyzzy", "hi", arc_id="ARC-002")
    assert "ONEUP-CORE-ARC" not in g.brief("xyzzy", "vht")


def test_approved_structure_reads_all_five_approved_clips():
    st = g.approved_structure()
    assert set(st) == {"a-c01", "a-c02", "a-c03", "a-c04", "a-c05"} == set(g.APPROVED_DESC)
    assert st["a-c01"]["n"] == 12 and st["a-c04"]["n"] == 8      # first beat table only; b12 two lines merged
    assert all(st[k]["n"] >= 8 and 150 <= st[k]["total_syl"] <= 350 for k in st)
    out = g.brief("xyzzy", "hi")
    assert "Nhịp thực tế của 5 clip đã duyệt" in out
    for k in st: assert f"{k}:" in out
    assert "tự giễu + ví dụ đời thường" in out and "giọng miền Nam + miếng hài nhập vai" in out


def test_brief_loads_voice_reminder_story_bank_and_only_four_writing_inputs():
    out = g.brief("học TOEIC mai học", "hi")
    assert "voice-profile.md" in out and "«ấy / thế / nhé»" in out and "«hông / nha / nè»" in out
    assert "Story bank S-01" in out                       # dòng story-bank khớp từ khóa
    assert "Chỉ nạp 4 thứ" in out and "Fact-lock" in out and "Single-Point Alignment" in out
    assert "Không nạp `connectors.tsv`" in out


def test_pick_approved_returns_closest_two_or_three():
    picks = g.pick_approved("việc to ngợp chia nhỏ dọn phòng")
    assert picks[0] == "a-c03" and 2 <= len(picks) <= 3
    assert "a-c04" in g.pick_approved("học thuộc quên sạch sách tự kiểm")
