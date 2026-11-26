# Theme/Format-Matched Anchor Selection & feedback blind-spot injection in pipeline/scripts/review-eval.py.
import importlib.util
import os
import tempfile
from pathlib import Path

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location("review_eval", os.path.join(R, "pipeline/scripts/review-eval.py"))
reval = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reval)


def test_real_golden_set_matches_theme_and_format():
    all_ss = reval.samples()
    # clip-06 (habit story_metaphor) should match a-c03 (habit story_metaphor), NOT a-c05 (memory instructional_list)
    for sid in ("r-c06-v2", "r-c06-v3", "r-c06-v3r2", "r-c06-v3r3"):
        s = next(x for x in all_ss if x["id"] == sid)
        aid, aw, meta = reval.select_anchor_with_meta(all_ss, sid, sample=s)
        assert aid == "a-c03", f"{sid} matched {aid} ({meta}) instead of a-c03"
        assert aw and meta["theme"] == "habit_procrastination"
        assert meta["format"] == "story_metaphor"

    # a-c05 (memory_study) leave-one-out never picks itself; picks same-theme a-c04
    s_c05 = next(x for x in all_ss if x["id"] == "a-c05")
    aid_c05, _, meta_c05 = reval.select_anchor_with_meta(all_ss, "a-c05", sample=s_c05)
    assert aid_c05 != "a-c05" and aid_c05 == "a-c04" and meta_c05["anchor_theme"] == "memory_study"

    # a-c02 (habit_procrastination, instructional_list) matches same-theme high-craft habit anchor (a-c03)
    s_c02 = next(x for x in all_ss if x["id"] == "a-c02")
    aid_c02, _, _ = reval.select_anchor_with_meta(all_ss, "a-c02", sample=s_c02)
    assert aid_c02 != "a-c02" and aid_c02 == "a-c03"

    # clip-05 rejected drafts match a-c05 (memory_study + full spoken craft)
    s_r68 = next(x for x in all_ss if x["id"] == "r-c05-r68")
    aid_r68, _, meta_r68 = reval.select_anchor_with_meta(all_ss, "r-c05-r68", sample=s_r68)
    assert aid_r68 == "a-c05" and meta_r68["theme"] == "memory_study"


def test_channel_isolation_loads_from_approved_dir():
    with tempfile.TemporaryDirectory() as d:
        gdir = Path(d)
        (gdir / "approved").mkdir()
        (gdir / "approved/a-vht-01.md").write_text(
            "---\nchannel: @vanhiep.tech\nformat: story_metaphor\ntheme: tech_dev\n---\n"
            "1. **[b01]** JWT lưu trong localStorage rất dễ dính XSS khi deploy API.\n",
            encoding="utf-8",
        )
        (gdir / "approved/a-hi-01.md").write_text(
            "---\nchannel: @hi.oneup\nformat: story_metaphor\ntheme: habit_procrastination\n---\n"
            "1. **[b01]** Kế hoạch học của mình là mai học.\n",
            encoding="utf-8",
        )
        draft_vht = {"id": "r-vht-99", "verdict": "rejected", "channel": "@vanhiep.tech", "source": "channels/vanhiep-tech/clips/vht-1/script.md"}
        aid, aw, meta = reval.select_anchor_with_meta(
            [], "r-vht-99", sample=draft_vht,
            draft_words="1. **[b01]** Bug token API trong server docker bị lỗi.",
            golden_dir=gdir,
        )
        assert aid == "a-vht-01"
        assert meta["anchor_channel"] == "@vanhiep.tech"
        assert "JWT" in aw


def test_feedback_blindspots_loaded_from_repo():
    txt = reval.load_feedback_blindspots()
    assert "r-c06-v3r2" in txt and "r-c05-r4" in txt and "L-106" in txt
