# DL-076: --draft chỉ ✖ cho Tier-1 + nguồn/cấu trúc; mọi check phong cách chỉ ⚠. Parse nhiều khung beat. --review bắt buộc feedback.md.
import importlib.util, os, sys, tempfile, subprocess
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec_ = importlib.util.spec_from_file_location("check_rules_draft", os.path.join(R, "pipeline/scripts/check-rules.py"))
cr = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(cr)

CHOPPY = "# nháp\n\n" + "".join(f"{i}. **[b{i:02d}]** Mình chạy bộ. Mình mệt. Mình dừng.\n" for i in range(1, 5))
EVID_BAD = "# nháp\n\n1. **[Hook]** Nhiều nghiên cứu cho thấy ai cũng nản vào tuần hai.\n"

def _write(txt):
    d = tempfile.mkdtemp(); p = os.path.join(d, "script-v1-draft.md"); open(p, "w", encoding="utf-8").write(txt); return p

def test_choppy_is_warning_not_error():
    cr.res.clear(); cr.check_choppy_file(_write(CHOPPY))
    kinds = {a for a, b, _ in cr.res if b == "L-096"}
    assert "⚠" in kinds and "✖" not in kinds

def test_evidence_without_source_is_still_hard():
    cr.res.clear(); cr.check_evidence_file(_write(EVID_BAD))
    assert any(a == "✖" and b == "L-096" for a, b, _ in cr.res)

def test_soft_downgrades_errors_only_in_wrapped_call():
    cr.res.clear(); cr.err("X", "a"); cr.soft(lambda: cr.err("Y", "b")); cr.warn("Z", "c")
    assert [a for a, _, _ in cr.res] == ["✖", "⚠", "⚠"]

def test_structure_h4_blocks_when_no_beat():
    cr.res.clear(); assert cr.check_draft_structure(_write("# nháp\nkhông có beat nào\n")) is False
    assert cr.res[0][0] == "✖" and cr.res[0][1] == "H4"

def test_draft_cli_choppy_draft_passes_without_error():
    p = _write(CHOPPY)
    r = subprocess.run([sys.executable, os.path.join(R, "pipeline/scripts/check-rules.py"), "--draft", p], capture_output=True, text=True)
    assert "✖ L-096" not in r.stdout and "TUYỆT ĐỐI KHÔNG hàn câu" in r.stdout

def test_draft_beats_bold_plain_and_table():
    bold = "1. **[Hook]** Lời một.\n2. **[b02]** Lời hai.\n"
    plain = "1. [Hook] Lời một.\n2. [b02] Lời hai.\n"
    table = "## Kịch bản\n| Beat | Giây | Lời thoại | Hình |\n|---|---|---|---|\n| b01 Hook | 0–3 | Lời một. | x |\n| b02 | 3–6 | Lời hai. | y |\n"
    spine = "| Beat | Vai trò |\n|---|---|\n| b01 | chuyện |\n"
    assert [t for _, _, t in cr.draft_beats(bold)] == ["Lời một.", "Lời hai."]
    assert [t for _, _, t in cr.draft_beats(plain)] == ["Lời một.", "Lời hai."]
    assert [(l, t) for _, l, t in cr.draft_beats(table)] == [("b01", "Lời một."), ("b02", "Lời hai.")]
    assert cr.draft_beats(spine) == []          # bảng khung mạch không có cột «Lời» không bị đọc nhầm thành lời

def test_review_requires_feedback_file_in_draft_mode():
    d = tempfile.mkdtemp(); draft = "1. **[Hook]** Bạn có hay bỏ dở thói quen?\n"
    h = cr.draft_hash(draft)
    open(os.path.join(d, "review.md"), "w", encoding="utf-8").write(f"---\nverdict: ĐẠT\nscript_hash: {h}\n---\nbody\n")
    cr.res.clear(); cr.check_review(None, d, want=h, require_feedback=True)
    assert cr.res[0][0] == "✖" and "feedback.md" in cr.res[0][2]
    open(os.path.join(d, "feedback.md"), "w", encoding="utf-8").write("| thời gian | b | lời | xử lý |\n|---|---|---|---|\n| 2026-11-27 09:00 | v7 | «x» | y |\n")
    cr.res.clear(); cr.check_review(None, d, want=h, require_feedback=True)
    assert cr.res[0][0] == "✖" and "feedback_seen" in cr.res[0][2]
