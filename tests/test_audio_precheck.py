# audio-precheck.py: Vietnamese spoken rhythm QA before Gate 1 (speech rate, max unbroken sentence, repeated openers, hook audition).
import importlib.util, os, tempfile
from pathlib import Path

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = importlib.util.spec_from_file_location("audio_precheck", os.path.join(R, "pipeline/scripts/audio-precheck.py"))
ap = importlib.util.module_from_spec(s); s.loader.exec_module(ap)


GOOD_DRAFT = """---
title: "Nháp mẫu"
---
1. **[b01 · 0–7s]** Hồi tối qua mình mở laptop lên tính làm cho xong việc, mà ngồi nửa tiếng chưa gõ nổi dòng.
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


def test_narrative_breath_under_32_without_pause_is_ok():
    draft = (
        "1. **[b01 · 0–8s]** Hôm qua mình ngồi trước màn hình máy tính cả buổi tối để cố gắng hoàn thành bài tập mà đầu óc trống.\n"
    )
    res = ap.analyze_beats(ap.parse_beats(draft))
    assert not any(w["code"] in ("LONG_SENTENCE", "LONG_CLAUSE") for w in res["warnings"])


def test_warns_long_sentence_over_32_syllables_without_pause():
    draft = (
        "1. **[b01 · 0–12s]** Hôm qua mình ngồi trước màn hình máy tính cả buổi tối để cố gắng hoàn thành bài tập mà đầu óc cứ trống rỗng không nghĩ ra được một chữ nào hết trơn luôn.\n"
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


def test_warns_hook_echo_when_opening_matches_archive():
    hooks = [{
        "clip": "clip-02-procrastination-discomfort",
        "text": "Thì cái bản chất của việc trì hoãn là né cảm giác khó chịu.",
    }]
    draft = (
        "1. **[b01 · 0–6s]** Thì cái bản chất của việc chờ hoa nở là mình cứ nhìn chậu mỗi ngày.\n"
        "2. **[b02 · 6–12s]** Rồi một hôm đất nứt, mình mới thấy mầm.\n"
    )
    res = ap.analyze_beats(ap.parse_beats(draft), archive_hooks=hooks)
    assert any(w["code"] == "HOOK_ECHO" and "clip-02" in w["message"] for w in res["warnings"])


def test_distinct_hook_does_not_echo_archive():
    hooks = [{
        "clip": "clip-01-implementation-intention",
        "text": "Kế hoạch học TOEIC của mình là mai học.",
    }]
    res = ap.analyze_beats(ap.parse_beats(GOOD_DRAFT), archive_hooks=hooks)
    assert not any(w["code"] == "HOOK_ECHO" for w in res["warnings"])


def test_load_archive_hooks_reads_spoken_b01():
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        spec = Path(d) / "content/archive/clip-09-demo/final/spec.json"
        spec.parent.mkdir(parents=True)
        spec.write_text(
            '{"parts":[{"scenes":[{"id":"b01","part":"hook","lines":[{"text":"Tối qua mình nhổ nụ hoa rồi hối."}]}]}]}',
            encoding="utf-8",
        )
        hooks = ap.load_archive_hooks(d)
        assert hooks == [{"clip": "clip-09-demo", "text": "Tối qua mình nhổ nụ hoa rồi hối."}]


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


def _beats(*counts):
    """Dựng nháp có beat với số âm tiết cho trước (mỗi beat 1 câu có dấu phẩy)."""
    lines = []
    for i, n in enumerate(counts, 1):
        words = ["từ"] * (n - 1)
        lines.append(f"{i}. **[b{i:02d} · {(i-1)*5}–{i*5+5}s]** " + " ".join(words[:n // 2]) + ", " + " ".join(words[n // 2:]) + " nha.")
    return ap.parse_beats("\n".join(lines))


def _codes(res):
    return {w["code"] for w in res["warnings"]}


def test_hook_long_over_22_syllables_only():
    assert "HOOK_LONG" not in _codes(ap.analyze_beats(_beats(22, 20)))
    res = ap.analyze_beats(_beats(23, 20))
    assert "HOOK_LONG" in _codes(res)
    assert "HOOK_LONG" in {w["code"] for w in res["beats"][0]["warnings"]}


def test_slow_entry_over_65_syllables_for_b01_plus_b02():
    assert "SLOW_ENTRY" not in _codes(ap.analyze_beats(_beats(20, 45)))
    res = ap.analyze_beats(_beats(20, 46))
    assert "SLOW_ENTRY" in _codes(res)
    assert [w for w in res["warnings"] if w["code"] == "SLOW_ENTRY"][0]["beat"] == "b01+b02"


def test_beat_bloat_over_45_syllables_any_beat():
    assert "BEAT_BLOAT" not in _codes(ap.analyze_beats(_beats(15, 20, 45)))
    res = ap.analyze_beats(_beats(15, 20, 46))
    bloat = [w for w in res["warnings"] if w["code"] == "BEAT_BLOAT"]
    assert len(bloat) == 1 and bloat[0]["beat"] == "b03"


def test_clip06_v8_shape_triggers_all_three_warnings():
    # b01=39, b02=~30, b07=57 như clip-06 v8
    res = ap.analyze_beats(_beats(39, 30, 20, 20, 20, 20, 57))
    assert {"HOOK_LONG", "SLOW_ENTRY", "BEAT_BLOAT"} <= _codes(res)
    assert not res["ok"]
