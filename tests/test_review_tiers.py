# DL-074: two-tier reviewer verdict (rubric §3b). Soft warnings never reject; hard fails always do.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pipeline"))
import review_tiers as rt

def blk(h="không", parts="A=18 B=13 C=17 D=14 E=14 F=9 G=4", total=89, soft=5, conf="không", v="ĐẠT"):
    return f"…phân tích…\nHARD_FAILS: {h}\nSCORE: {parts} TOTAL={total}\nSOFT_WARNINGS: {soft}\nCONFLICTS: {conf}\nVERDICT: {v}\n"

def test_pass_at_85():
    assert rt.verdict_of(blk(parts="A=17 B=13 C=17 D=13 E=13 F=8 G=4", total=85)) == "ĐẠT"

def test_soft_warnings_do_not_reject():
    assert rt.verdict_of(blk(soft=12, v="CHƯA ĐẠT")) == "ĐẠT"

def test_hard_fail_rejects():
    b = rt.parse_block(blk(h="H1: «gấp ba lần» không nguồn; H3: «đầu dở»"))
    assert len(b["hard_fails"]) == 2 and rt.tier_verdict(b) == ("CHƯA ĐẠT", "chặn")

def test_below_threshold_sizes():
    assert rt.tier_verdict(rt.parse_block(blk(parts="A=15 B=11 C=15 D=12 E=12 F=8 G=4", total=77))) == ("CHƯA ĐẠT", "sửa nhỏ")
    assert rt.tier_verdict(rt.parse_block(blk(parts="A=8 B=6 C=9 D=12 E=4 F=7 G=3", total=49)))[1] == "sửa lớn"

def test_misadded_total_uses_parts():
    assert rt.parse_block(blk(total=60))["score"] == 89

def test_conflict_gives_dat_ve_diem():
    assert rt.verdict_of(blk(conf="C-1 credit chờ Hiệp")) == "ĐẠT VỀ ĐIỂM"

def test_missing_block_falls_back_to_llm_line():
    assert rt.parse_block("VERDICT: CHƯA ĐẠT — lớn") is None
    assert rt.verdict_of("VERDICT: CHƯA ĐẠT — lớn") == "CHƯA ĐẠT"

def test_parts_capped_by_weight():
    assert rt.parse_block(blk(parts="A=25 B=13 C=17 D=14 E=14 F=9 G=4", total=96))["parts"]["A"] == 20

def test_eval_strips_markup_but_keeps_beat_labels():
    import importlib.util
    s = importlib.util.spec_from_file_location("review_eval", os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pipeline/scripts/review-eval.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    out = m.strip_markup("1. **[b01]** Bạn học **tới khuya**, {nhấn: quên sạch} | rồi {ừm} sáng ra / trống trơn.")
    assert out == "1. **[b01]** Bạn học tới khuya, quên sạch rồi sáng ra trống trơn."
