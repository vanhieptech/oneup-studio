# Two-tier reviewer verdict: Tier 1 Hard-Gate (H1–H4) + Tier 2 Pairwise A/B (and legacy SCORE support).
import importlib.util, os, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(R, "pipeline"))
import review_tiers as rt


def blk(h="không", parts="A=18 B=13 C=17 D=14 E=14 F=9 G=4", total=89, soft=5, conf="không", v="ĐẠT"):
    return f"…phân tích…\nHARD_FAILS: {h}\nSCORE: {parts} TOTAL={total}\nSOFT_WARNINGS: {soft}\nCONFLICTS: {conf}\nVERDICT: {v}\n"


def pw_blk(h="không", pw="TIE (so với a-c05)", fixes="1. b02: đổi từ nối; 2. b05: cắt bớt câu thừa", conf="không", v="ĐẠT"):
    return f"…so sánh 4 trục…\nHARD_FAILS: {h}\nPAIRWISE: {pw}\nTOP_FIXES: {fixes}\nCONFLICTS: {conf}\nVERDICT: {v}\n"


def test_pass_at_85():
    assert rt.verdict_of(blk(parts="A=17 B=13 C=17 D=13 E=13 F=8 G=4", total=85)) == "ĐẠT"


def test_soft_warnings_do_not_reject():
    assert rt.verdict_of(blk(soft=12, v="CHƯA ĐẠT")) == "ĐẠT"


def test_hard_fail_rejects():
    b = rt.parse_block(blk(h="H1: «gấp ba lần» không nguồn; H3: «đầu dở»"))
    assert len(b["hard_fails"]) == 2 and b["hard_kinds"] == ["H1", "H3"]
    assert rt.is_hard_blocked(b) and rt.tier_verdict(b) == ("CHƯA ĐẠT", "chặn")


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


# ---------- Pairwise A/B mode tests ----------
def test_pairwise_win_and_tie_pass():
    bw = rt.parse_block(pw_blk(pw="WIN (so với a-c05)", fixes="không"))
    assert bw["mode"] == "pairwise" and bw["pairwise"] == "WIN" and bw["anchor"] == "a-c05"
    assert not rt.is_hard_blocked(bw) and rt.tier_verdict(bw) == ("ĐẠT", "")

    bt = rt.parse_block(pw_blk(pw="TIE (so với a-c04)", v="CẦN SỬA"))
    assert rt.tier_verdict(bt) == ("ĐẠT", "")  # deterministic recomputation overrides strict LLM line
    assert bt["anchor"] == "a-c04" and len(bt["top_fixes"]) == 2


def test_pairwise_lose_gives_can_sua_without_hard_block():
    b = rt.parse_block(pw_blk(pw="LOSE (so với a-c05)", v="ĐẠT"))
    assert not rt.is_hard_blocked(b)
    assert rt.tier_verdict(b) == ("CẦN SỬA", "thua cặp")


def test_pairwise_hard_fail_blocks_even_on_win():
    b = rt.parse_block(pw_blk(h="H2: tổng ước 315s ≥ 300s", pw="WIN (so với a-c05)", v="ĐẠT"))
    assert rt.is_hard_blocked(b) and b["hard_kinds"] == ["H2"]
    assert rt.tier_verdict(b) == ("CẦN SỬA", "chặn")


def test_pairwise_multiline_top_fixes_capped_at_3():
    txt = (
        "HARD_FAILS: không\n"
        "PAIRWISE: LOSE (so với a-c05)\n"
        "TOP_FIXES:\n"
        "- b01: đổi câu mở đầu\n"
        "- b03: thêm nguồn tác giả\n"
        "- b06: rút gọn ví dụ\n"
        "- b08: sửa CTA\n"
        "CONFLICTS: không\n"
        "VERDICT: CẦN SỬA\n"
    )
    b = rt.parse_block(txt)
    assert len(b["top_fixes"]) == 3 and b["top_fixes"][0].startswith("b01:")


def test_pairwise_conflict_gives_dat_ve_diem():
    b = rt.parse_block(pw_blk(pw="WIN (so với a-c05)", conf="cần Hiệp chọn góc hook"))
    assert rt.tier_verdict(b) == ("ĐẠT VỀ ĐIỂM", "cần Hiệp chọn góc hook")


def test_eval_strips_markup_but_keeps_beat_labels():
    s = importlib.util.spec_from_file_location("review_eval", os.path.join(R, "pipeline/scripts/review-eval.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    out = m.strip_markup("1. **[b01]** Bạn học **tới khuya**, {nhấn: quên sạch} | rồi {ừm} sáng ra / trống trơn.")
    assert out == "1. **[b01]** Bạn học tới khuya, quên sạch rồi sáng ra trống trơn."


def test_eval_resolve_anchor_leave_one_out():
    s = importlib.util.spec_from_file_location("review_eval", os.path.join(R, "pipeline/scripts/review-eval.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    ss = m.samples()
    # Evaluating a rejected sample defaults to newest approved (a-c05)
    aid, w = m.resolve_anchor(ss, "r-c05-v2")
    assert aid == "a-c05" and w
    # Evaluating a-c05 itself must NOT leak a-c05; falls back to next approved (a-c04)
    aid2, w2 = m.resolve_anchor(ss, "a-c05", preferred_anchor="a-c05")
    assert aid2 == "a-c04" and w2
