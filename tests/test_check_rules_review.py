# make-video §4b gate: final/review.md must carry verdict ĐẠT for the current spoken words (draft or spec) and answer every Hiệp note.
import importlib.util, os, tempfile
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec_ = importlib.util.spec_from_file_location("check_rules_review", os.path.join(R, "pipeline/scripts/check-rules.py"))
cr = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(cr)

SPEC = {"parts": [{"scenes": [{"lines": [{"text": "Bạn có hay **bỏ dở** thói quen?", "en": "Do you quit habits?"}]}], "sections": []}]}
DRAFT = "# nháp\n\n1. **[Hook]** Bạn có hay {nhấn: bỏ dở} thói quen?\n"

def run(review=None, spec=SPEC, want=None, feedback=None):
    cr.res.clear()
    with tempfile.TemporaryDirectory() as d:
        if review is not None: open(os.path.join(d, "review.md"), "w", encoding="utf-8").write(review)
        if feedback is not None: open(os.path.join(d, "feedback.md"), "w", encoding="utf-8").write(feedback)
        cr.check_review(spec, d, want=want)
    return [(a, b) for a, b, _ in cr.res]

def fm(verdict, h=None, score=88, extra=""):
    return f"---\ntitle: \"review\"\nverdict: {verdict}\nscore: {score}\nscript_hash: {h or cr.script_hash(SPEC)}\n{extra}---\nbody\n"

FB = "| thời gian | bản | lời Hiệp | đã xử lý |\n|---|---|---|---|\n| 2026-11-26 06:47 | 4b16165 | «xàm» | b02 |\n| 2026-11-26 06:55 | 8df074e | «rời rạc» | khung mạch |\n"

def test_missing_blocks(): assert run() == [("✖", "review")]
def test_dat_passes(): assert run(fm("ĐẠT — trình gate 1")) == [("✔", "review")]
def test_chua_dat_blocks(): assert run(fm("CHƯA ĐẠT — sửa nhỏ", score=80)) == [("✖", "review")]
def test_dat_ve_diem_warns(): assert run(fm("ĐẠT VỀ ĐIỂM — chờ Hiệp quyết C-1")) == [("⚠", "review")]
def test_stale_hash_blocks(): assert run(fm("ĐẠT", h="000000000000")) == [("✖", "review")]
def test_bad_verdict_blocks(): assert run(fm("ok")) == [("✖", "review")]
def test_hash_tracks_wording():
    changed = {"parts": [{"scenes": [{"lines": [{"text": "Bạn có hay bỏ dở thói quen không?"}]}], "sections": []}]}
    assert cr.script_hash(changed) != cr.script_hash(SPEC)
def test_draft_and_spec_same_hash_ignoring_markup():
    assert cr.draft_hash(DRAFT) == cr.script_hash(SPEC)
def test_hash_keeps_tones():
    a = {"parts": [{"scenes": [{"lines": [{"text": "ma"}]}], "sections": []}]}
    b = {"parts": [{"scenes": [{"lines": [{"text": "má"}]}], "sections": []}]}
    assert cr.script_hash(a) != cr.script_hash(b)
def test_hash_with_label_text_accepted():
    assert run(fm("ĐẠT", h=f"\"draft-{cr.script_hash(SPEC)} (ghi chú)\"")) == [("✔", "review")]
def test_review_on_draft_hash():
    assert run(fm("ĐẠT", h=cr.draft_hash(DRAFT)), spec=None, want=cr.draft_hash(DRAFT)) == [("✔", "review")]
def test_feedback_unseen_blocks():
    assert run(fm("ĐẠT", extra="feedback_seen: 1\n"), feedback=FB) == [("✖", "review")]
def test_feedback_missing_field_blocks():
    assert run(fm("ĐẠT"), feedback=FB) == [("✖", "review")]
def test_feedback_all_seen_passes():
    assert run(fm("ĐẠT", extra="feedback_seen: 2\n"), feedback=FB) == [("✔", "review")]


import unittest as _ut
class _All(_ut.TestCase):
    pass
for _n, _f in list(globals().items()):
    if _n.startswith("test_") and callable(_f):
        setattr(_All, _n, (lambda f: lambda self: f())(_f))
if __name__ == "__main__":
    _ut.main()

class Gate0Warning(_ut.TestCase):
    def test_missing_gate0_warns_on_review_mode(self):
        import subprocess, sys, tempfile, pathlib
        d = pathlib.Path(tempfile.mkdtemp()) / "content" / "clips" / "clip-99-x"
        (d / "archive").mkdir(parents=True); (d / "final").mkdir()
        draft = d / "archive" / "script-v1-draft.md"; draft.write_text(DRAFT, encoding="utf-8")
        (d / "final" / "review.md").write_text(fm("ĐẠT", h=cr.draft_hash(DRAFT)), encoding="utf-8")
        out = subprocess.run([sys.executable, os.path.join(R, "pipeline/scripts/check-rules.py"), "--review", str(draft)], capture_output=True, text=True).stdout
        self.assertIn("gate0", out)
        draft.write_text("## Gate 0\n- A\n\n" + DRAFT, encoding="utf-8")
        out = subprocess.run([sys.executable, os.path.join(R, "pipeline/scripts/check-rules.py"), "--review", str(draft)], capture_output=True, text=True).stdout
        self.assertNotIn("gate0", out)


class TwoTierBlock(_ut.TestCase):
    """DL-074: the body's HARD_FAILS/SCORE block recomputes the verdict; front-matter must agree."""
    BLOCK = "HARD_FAILS: {h}\nSCORE: A=18 B=13 C=17 D=14 E=14 F=9 G=4 TOTAL={t}\nSOFT_WARNINGS: 4\nCONFLICTS: không\nVERDICT: {v}\n"

    def _fm(self, verdict, body):
        return f"---\ntitle: \"review\"\nverdict: {verdict}\nscore: 89\nscript_hash: {cr.script_hash(SPEC)}\n---\n{body}"

    def test_block_agrees_passes(self):
        self.assertEqual(run(self._fm("ĐẠT", self.BLOCK.format(h="không", t=89, v="ĐẠT"))), [("✔", "review")])

    def test_strict_model_overruled_by_numbers(self):
        # model said CHƯA ĐẠT while score ≥85 and no hard fail: front-matter CHƯA ĐẠT disagrees with the tier verdict
        self.assertEqual(run(self._fm("CHƯA ĐẠT — sửa nhỏ", self.BLOCK.format(h="không", t=89, v="CHƯA ĐẠT"))), [("✖", "review")])

    def test_hard_fail_blocks_even_high_score(self):
        self.assertEqual(run(self._fm("ĐẠT", self.BLOCK.format(h="H1: «nhớ gấp 3 lần» không có nguồn", t=92, v="ĐẠT"))), [("✖", "review")])


class PairwiseHardGateBlock(_ut.TestCase):
    """Tier 1 (H1–H4) is the sole hard blocker in pairwise mode; LOSE without H1–H4 warns instead of hard-blocking."""
    PW = "HARD_FAILS: {h}\nPAIRWISE: {pw} (so với a-c05)\nTOP_FIXES: 1. b01: rút ngắn hook\nCONFLICTS: {c}\nVERDICT: {v}\n"

    def _fm(self, verdict, body):
        return f"---\ntitle: \"review\"\nverdict: {verdict}\nscript_hash: {cr.script_hash(SPEC)}\n---\n{body}"

    def test_pairwise_tie_passes(self):
        self.assertEqual(run(self._fm("ĐẠT", self.PW.format(h="không", pw="TIE", c="không", v="ĐẠT"))), [("✔", "review")])

    def test_pairwise_lose_without_hard_fail_warns_only(self):
        # Sole hard gate is H1–H4; LOSE without hard fails emits warning with TOP_FIXES
        self.assertEqual(run(self._fm("CẦN SỬA", self.PW.format(h="không", pw="LOSE", c="không", v="CẦN SỬA"))), [("⚠", "review")])

    def test_pairwise_hard_fail_blocks_hard(self):
        self.assertEqual(run(self._fm("CẦN SỬA", self.PW.format(h="H3: chê người xem «não kém»", pw="WIN", c="không", v="CẦN SỬA"))), [("✖", "review")])

    def test_pairwise_frontmatter_disagreement_blocks(self):
        self.assertEqual(run(self._fm("ĐẠT", self.PW.format(h="H1: không nguồn", pw="WIN", c="không", v="ĐẠT"))), [("✖", "review")])
