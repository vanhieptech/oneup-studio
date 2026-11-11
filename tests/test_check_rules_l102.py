"""L-102 --vague-hook tests (inline fixtures mirroring clip05 r17.4 / r18.2 / r18.3 hook concepts); no audio, image or render."""
import importlib.util
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CR = ROOT / "pipeline/scripts/check-rules.py"
spec = importlib.util.spec_from_file_location("check_rules_l102", CR)
cr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cr)

# r18.2-like: phrases hidden, the promise sits only in the «Câu nối» bridge (not in the hook) → ⚠ for every concept
R182 = """# concepts
## A — câu hỏi
1. Sao bạn đọc ghi chú tới mấy lần, mà hai hôm sau đầu bạn vẫn trống trơn?
2. Nhưng trong một thí nghiệm, người ta chỉ đổi cách ôn, mà kết quả đã khác.
3. Hai ngày sau, khi làm một việc khác thay cho lượt đọc lại, người ta nhớ đúng nhiều ý hơn.
- Câu nối: Việc khác đó là gì, phần tiếp theo có đủ số.

## B — nói ngược
1. Tài liệu bạn đọc lại cho chắc, vậy mà tuần sau vẫn thấy lạ hoắc.
2. Qua một tuần thì đọc lại thua một cách ôn khác.
3. Chỉ đọc lại thì người ta nhớ ít hơn khi làm cách kia.
- Câu nối: Cách ôn kia là gì, bạn nghe tiếp nhé.
"""
# r17.4-like: «> **S01**» lines, «một việc thay cho …» hidden, named only in the NEXT sentence → ⚠ (sentence needs the next one)
R174 = """## 1. Ba concept
### C1 — Nghịch lý
> **S01** Bạn nhớ lõm bõm chỉ sau hai hôm, dù đã đọc lại thêm một lượt.
> **S02** Khi tự viết ra không nhìn bài, trung bình người ta nhớ đúng nhiều ý hơn.
### C3 — Giấu tên việc
> **S01** Bài viết hôm kia, giờ bạn chỉ nhớ vài ý, dù đã đọc lại một lượt.
> **S02** Hai ngày sau, người ta nhớ đúng hơn khi làm một việc thay cho đọc lại, theo một thí nghiệm.
> **S03** Việc đó không phải đọc lại, mà là tự viết ra những gì còn nhớ.
## 7. Rủi ro
1. **C3:** cách khác vẫn còn giấu tên ở đây (ghi chú, không phải hook).
"""
# r18.3-like: C1 names the method, C2 hides it but promises inside the hook, A' names it → 0 ⚠, C2 ℹ MANUAL PENDING
R183 = """## C1 — nêu tên
1. Chủ nhật bạn đọc lại thêm một lượt, vậy mà thứ ba bạn chỉ nhớ cái tiêu đề.
2. Theo một thí nghiệm, nếu lượt thứ hai đó gấp bài lại và tự viết ra, thì hai ngày sau người ta nhớ nhiều ý hơn.
- Câu nối sang thân: Nhiều hơn bao nhiêu, bạn nghe tiếp nhé.

## C2 — có lời hứa
1. Chủ nhật bạn đọc lại thêm một lượt, vậy mà thứ ba bạn chỉ nhớ cái tiêu đề.
2. Theo một thí nghiệm, nếu lượt thứ hai đó không đọc mà làm một việc khác, thì hai ngày sau người ta nhớ nhiều ý hơn.
3. Việc đó là gì, và bạn làm nó ra sao, bạn nghe tiếp nhé.

## A' — nêu tên
1. Bạn có bao giờ đọc lại ghi chú thêm một lượt, mà hai hôm sau đầu vẫn trống trơn không?
2. Theo một thí nghiệm, nếu lượt đọc thêm đổi thành tự viết ra, thì người ta nhớ nhiều ý hơn.

## Ghi chú
- Chỉ là ghi chú, cách kia không tính.
"""


def run(md):
    cr.res.clear()
    cr.check_vague_hook(cr.l102_hooks(md), "t.md")
    return [(sym, msg) for sym, rule, msg in cr.res if rule == "L-102"]


class VagueHookTests(unittest.TestCase):
    def test_r182_like_warns_every_concept_bridge_promise_ignored(self):
        out = run(R182)
        self.assertEqual([s for s, _ in out], ["⚠", "⚠"])
        self.assertIn("«kết quả đã khác»", out[0][1]); self.assertIn("«việc khác»", out[0][1])
        self.assertIn("«cách ôn khác»", out[1][1]); self.assertIn("«cách kia»", out[1][1])

    def test_r174_like_warns_hidden_substitute_named_only_later(self):
        out = run(R174)
        self.assertEqual([s for s, _ in out], ["✔", "⚠"])
        self.assertIn("C3", out[1][1]); self.assertIn("một việc thay cho", out[1][1])

    def test_r183_like_no_warning_promise_is_manual_pending(self):
        out = run(R183)
        self.assertEqual([s for s, _ in out], ["✔", "ℹ", "✔"])
        self.assertIn("C2", out[1][1]); self.assertIn("MANUAL PENDING", out[1][1])
        self.assertFalse(any(s in ("⚠", "✖") for s, _ in out))

    def test_named_in_same_sentence_clears(self):
        md = "## C1 — x\n1. Có một cách khác là tự viết ra những gì còn nhớ.\n"
        self.assertEqual([s for s, _ in run(md)], ["✔"])

    def test_la_gi_is_not_a_name(self):
        md = "## C1 — x\n1. Có một cách khác là gì thì chưa ai nói.\n"
        self.assertEqual([s for s, _ in run(md)], ["⚠"])

    def test_diacritic_and_case_folding(self):
        md = "## C1 — x\n1. CÁCH KIA thì sao.\n"
        self.assertEqual([s for s, _ in run(md)], ["⚠"])

    def test_beat_draft_fallback_hook_only(self):
        md = "1. **[Hook]** Bạn làm cách kia mà vẫn quên.\n2. **[Thân]** Một việc khác ở thân bài không tính.\n"
        out = run(md)
        self.assertEqual([s for s, _ in out], ["⚠"])
        self.assertIn("hook", out[0][1])

    def test_no_hook_is_info_not_pass(self):
        out = run("# chỉ có tiêu đề\nkhông có câu hook\n")
        self.assertEqual([s for s, _ in out], ["ℹ"])

    def test_cli_warning_only_exit_zero(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "c.md"); open(p, "w", encoding="utf8").write(R182)
            r = subprocess.run([sys.executable, str(CR), "--vague-hook", p], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("2 warning(s)", r.stdout); self.assertIn("0 error(s)", r.stdout)


if __name__ == "__main__":
    unittest.main()
