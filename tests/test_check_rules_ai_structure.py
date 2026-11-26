# Structural AI-Tells (⚠ ai-structure) in check-rules.py (--ai-structure / --draft / --bookish).
import importlib.util
import os
import tempfile
from pathlib import Path

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location("check_rules_ai_struct", os.path.join(R, "pipeline/scripts/check-rules.py"))
cr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cr)


def run_text(text):
    cr.res.clear()
    cr.check_ai_structure_text("b01", text)
    return list(cr.res)


def test_parallel_symmetry_khong_chi_ma_con_warns():
    rows = run_text("Cách này không chỉ giúp bạn tập trung hơn mà còn tăng động lực mỗi ngày.")
    assert any(sev == "⚠" and tag == "ai-structure" and "không chỉ" in msg for sev, tag, msg in rows)


def test_parallel_symmetry_vua_vua_giup_ban_warns():
    rows = run_text("Phương pháp này vừa tiết kiệm thời gian vừa giảm áp lực giúp bạn học hiệu quả hơn.")
    assert any(sev == "⚠" and tag == "ai-structure" and "vừa" in msg for sev, tag, msg in rows)


def test_preachy_book_summary_openers_warn():
    for sent in (
        "Bí quyết là bạn cần giữ tâm thế bình tĩnh trước mọi thử thách.",
        "Điều quan trọng nhất là kiên trì theo đuổi mục tiêu mỗi ngày.",
        "Chìa khóa nằm ở việc thay đổi tư duy từ bên trong.",
        "Thật ra thì, chìa khoá nằm ở sự kỷ luật của chính bạn.",
    ):
        rows = run_text(sent)
        assert any(sev == "⚠" and tag == "ai-structure" for sev, tag, _ in rows), f"missed: {sent}"


def test_low_concreteness_long_beat_warns():
    abstract_beat = (
        "Phát triển bản thân là một hành trình dài đòi hỏi sự kiên trì và tư duy đúng đắn từ mỗi cá nhân. "
        "Khi chúng ta hiểu rõ giá trị cốt lõi của mục tiêu, động lực nội tại sẽ dần hình thành để giúp tâm trí "
        "vượt qua cảm giác chán nản và duy trì hiệu suất bền vững lâu dài."
    )
    assert len(abstract_beat.split()) > 40
    rows = run_text(abstract_beat)
    assert any(sev == "⚠" and tag == "ai-structure" and "Sensory/Action Anchor" in msg for sev, tag, msg in rows)


def test_concrete_long_beat_with_action_number_or_time_is_clean():
    concrete_beat = (
        "Tối qua chín giờ mình ngồi vào bàn, gấp sách lại rồi lấy tờ giấy trắng tự viết ra ba ý chính nhớ được. "
        "Chỗ nào bí thì mình mới mở sách dò lại, khoanh tròn chỗ sót rồi sửa ngay tại chỗ cho khỏi quên."
    )
    assert len(concrete_beat.split()) > 40
    rows = run_text(concrete_beat)
    assert rows == []


def test_natural_southern_spoken_beat_is_clean():
    rows = run_text("Tối nào cũng vậy: code xong, mệt, rồi thôi, mai học. Hoá ra mình đâu thiếu động lực.")
    assert rows == []


def test_only_warnings_never_hard_error_in_file_mode():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "draft.md"
        p.write_text(
            "1. **[b01]** Điều quan trọng nhất là cách này không chỉ hay mà còn hiệu quả.\n"
            "2. **[b02]** Mình gấp sách lại lúc chín giờ tối rồi viết ba dòng.\n",
            encoding="utf-8",
        )
        cr.res.clear()
        n = cr.check_ai_structure_file(str(p))
        assert n >= 2
        assert all(sev == "⚠" and tag == "ai-structure" for sev, tag, _ in cr.res)
