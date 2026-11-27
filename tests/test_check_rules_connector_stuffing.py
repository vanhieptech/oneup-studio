# ⚠ connector-stuffing (WS2, 27/11): chuỗi câu mở bằng liên từ nối nhau, hoặc > 25% câu mở bằng liên từ.
import importlib.util
import os
import tempfile
from pathlib import Path

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location("check_rules_cs", os.path.join(R, "pipeline/scripts/check-rules.py"))
cr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cr)


def run(sents):
    cr.res.clear()
    n = cr.check_connector_stuffing_text("t", sents)
    return n, [m for sev, tag, m in cr.res if sev == "⚠" and tag == "connector-stuffing"]


def test_two_consecutive_openers_warn():
    n, w = run(["Mình mua giày.", "Nên mình xỏ vào.", "Nhưng mà cân không nhích.", "Hôm sau mình đi tiếp.", "Bạn thử chưa?"])
    assert n >= 1 and any("2 câu liên tiếp" in m for m in w)


def test_each_listed_connector_counts():
    for c in ("Nên", "Nhưng mà", "Thành ra", "Vì vậy", "Do đó", "Mà", "Rồi", "Thế là"):
        n, w = run([f"{c} mình đi.", f"{c} mình về.", "Hết.", "Xong.", "Ngủ.", "Dậy."])
        assert any("2 câu liên tiếp" in m for m in w), c


def test_density_over_25_percent_warns_even_when_not_adjacent():
    n, w = run(["Mình mua giày.", "Nên mình xỏ vào.", "Cân không nhích.", "Rồi mình nản.", "Bạn có vậy không?"])
    assert any("quá 25%" in m for m in w) and not any("liên tiếp" in m for m in w)


def test_one_connector_in_twelve_sentences_is_clean():
    sents = ["Câu một."] * 5 + ["Nhưng mà câu sáu."] + ["Câu bảy."] * 6
    assert run(sents) == (0, [])


def test_connector_inside_sentence_is_not_an_opener():
    assert run(["Mình mua giày nhưng mà chưa chạy.", "Cân không nhích, rồi mình nản.", "Hôm sau đi tiếp."]) == (0, [])


def test_file_flattens_sentences_across_beats_and_draft_gate_runs_it():
    md = ("1. **[Hook]** Mình mua giày. Nên mình xỏ vào.\n2. **[But]** Nhưng mà cân không nhích.\n"
          "3. **[CTA]** Bạn thử chưa?\n")
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "draft.md"; p.write_text(md, encoding="utf-8")
        cr.res.clear(); cr.check_connector_stuffing_file(str(p))
        assert any(tag == "connector-stuffing" and sev == "⚠" for sev, tag, _ in cr.res)


def test_approved_scripts_are_not_flagged():
    for rel in ("content/archive/clip-04-gap-sach-tu-kiem/final/script-v18-LOCKED.md",
                "content/archive/clip-01-implementation-intention/final/script-final.md"):
        cr.res.clear(); cr.check_connector_stuffing_file(os.path.join(R, rel))
        assert not [1 for sev, tag, _ in cr.res if sev == "⚠"], rel
