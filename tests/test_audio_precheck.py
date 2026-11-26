# audio-precheck.py: Vietnamese spoken rhythm QA before Gate 1 (speech rate, max unbroken sentence, repeated openers, hook audition).
import importlib.util, os, tempfile
from pathlib import Path

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = importlib.util.spec_from_file_location("audio_precheck", os.path.join(R, "pipeline/scripts/audio-precheck.py"))
ap = importlib.util.module_from_spec(s); s.loader.exec_module(ap)


GOOD_DRAFT = """---
title: "Nháp mẫu"
---
1. **[b01 · 0–7s]** Hồi tối qua, mình mở laptop lên tính làm cho xong việc, mà ngồi nửa tiếng chưa gõ nổi dòng nào.
2. **[b02 · 7–16s]** Vậy mà sáng nay, mình chỉ đổi đúng một bước nhỏ — là ngồi vô bàn trước khi mở điện thoại, tự nhiên làm trơn luôn á.
3. **[b03 · 16–24s]** Hóa ra bộ não tụi mình hông phải lười đâu, nó chỉ né cảm giác mơ hồ khi việc quá to thôi nha.
"""


def test_good_draft_passes_all_checks():
    beats = ap.parse_beats(GOOD_DRAFT)
    assert len(beats) == 3
    assert [b["duration_s"] for b in beats] == [7.0, 9.0, 8.0]
    res = ap.analyze_beats(beats)
    assert res["ok"] and res["warnings"] == []


def test_warns_too_fast_and_too_slow_beats():
    draft = (
        "1. **[b01 · 0–3s]** Hôm nay mình kể cho bạn nghe chuyện hồi tuần trước mình thức tới hai giờ sáng làm báo cáo mà sáng ra quên sạch hết trơn luôn.\n"
        "2. **[b02 · 3–13s]** Chậm quá trời luôn á.\n"
    )
    res = ap.analyze_beats(ap.parse_beats(draft))
    codes = {w["code"] for w in res["warnings"]}
    assert "RATE_FAST" in codes
    assert "RATE_SLOW" in codes


def test_warns_long_sentence_over_22_syllables_without_pause():
    draft = (
        "1. **[b01 · 0–9s]** Hôm qua mình ngồi trước màn hình máy tính cả buổi tối để cố gắng hoàn thành bài tập mà đầu óc cứ trống rỗng không nghĩ ra được chữ nào cả.\n"
    )
    res = ap.analyze_beats(ap.parse_beats(draft))
    assert any(w["code"] == "LONG_SENTENCE" for w in res["warnings"])


def test_long_sentence_with_short_clauses_passes():
    draft = (
        "1. **[b01 · 0–10s]** Hôm qua mình ngồi trước máy tính cả buổi tối, cố hoàn thành bài tập, mà đầu óc cứ trống rỗng — không nghĩ ra chữ nào.\n"
    )
    res = ap.analyze_beats(ap.parse_beats(draft))
    assert not any(w["code"] in ("LONG_SENTENCE", "LONG_CLAUSE") for w in res["warnings"])


def test_warns_consecutive_beat_opener_repetition():
    draft = (
        "1. **[b01 · 0–5s]** Nhưng mà chuyện này xảy ra hoài à, bạn thử để ý coi nha.\n"
        "2. **[b02 · 5–10s]** Nhưng mà tới lúc cần làm thiệt thì mình lại cầm điện thoại lên lướt.\n"
    )
    res = ap.analyze_beats(ap.parse_beats(draft))
    assert any(w["code"] == "REPEAT_OPENER" and w["beat"] == "b01→b02" for w in res["warnings"])


def test_audition_hook_dry_run_extracts_first_two_beats_and_targets_final_out():
    with tempfile.TemporaryDirectory() as d:
        clip = Path(d) / "content/clips/clip-99-test"
        (clip / "archive").mkdir(parents=True)
        (clip / "final").mkdir(parents=True)
        script = clip / "archive/script-v1-draft.md"
        script.write_text(GOOD_DRAFT, encoding="utf-8")
        beats = ap.parse_beats(GOOD_DRAFT)
        aud = ap.run_audition_hook(beats, script, dry_run=True)
        assert aud["dry_run"] is True
        assert aud["out"].endswith("clip-99-test/final/out/hook-audition.wav")
        assert "Hồi tối qua" in aud["text"] and "Vậy mà sáng nay" in aud["text"]
        assert "Hóa ra bộ não" not in aud["text"]
