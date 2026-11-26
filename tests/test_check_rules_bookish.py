# L-106 (Hiệp 26/11 «cả ai nói lý do nghe mới quê tuần .. thấy ngại»): --bookish flags written-register words (⚠ only).
import importlib.util, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec_ = importlib.util.spec_from_file_location("check_rules_bookish", os.path.join(R, "pipeline/scripts/check-rules.py"))
cr = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(cr)

def run(text):
    cr.res.clear(); cr.check_bookish_text("t", text)
    return [m for a, b, m in cr.res if b == "bookish"]

def test_l106_sentence_flagged():
    msgs = " ".join(run("Lý do nghe mới quê, tới tuần thứ ba vẫn thấy ngại. Cẩm nang ghi vậy."))
    assert "cẩm nang" in msgs and "thấy ngại" in msgs
def test_spoken_sentence_clean():
    assert run("Hôm đó mình bỏ luôn, tại vì mình tưởng lỡ một bữa là hỏng hết.") == []
def test_proper_names_not_flagged_as_rare():
    assert not any("lally" in m for m in run("Năm 2010 nhóm của Lally theo dõi chín mươi sáu người."))
def test_only_warnings():
    cr.res.clear(); cr.check_bookish_text("t", "Tuy nhiên do đó cẩm nang")
    assert {a for a, b, _ in cr.res} == {"⚠"}


import unittest as _ut
class _All(_ut.TestCase):
    pass
for _n, _f in list(globals().items()):
    if _n.startswith("test_") and callable(_f):
        setattr(_All, _n, (lambda f: lambda self: f())(_f))
if __name__ == "__main__":
    _ut.main()
