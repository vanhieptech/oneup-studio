# DL-074: resources/vn-spoken/ai-blacklist.tsv → ⚠ ai-tell in check-rules --bookish (start-only phrases only at sentence start).
import importlib.util, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = importlib.util.spec_from_file_location("check_rules_ai", os.path.join(R, "pipeline/scripts/check-rules.py"))
cr = importlib.util.module_from_spec(s); s.loader.exec_module(cr)

def tags(text):
    cr.res.clear(); cr.check_ai_blacklist_text("b01", text)
    return [b for _, b, _ in cr.res]

def test_any_position_phrase_warns():
    assert tags("Mình nói thật, trong thế giới ngày nay ai cũng bận.") == ["ai-tell"]

def test_start_only_phrase_at_start_warns():
    assert tags("Mình thử rồi. Tuy nhiên nó hông chạy.") == ["ai-tell"]

def test_start_only_phrase_mid_sentence_ok():
    assert tags("Mình thử, tuy nhiên nó hông chạy.") == []

def test_spoken_connectors_never_flagged():
    assert tags("Thật ra thì mình né. Nhưng mà khoan, nghe quen không? Nói thẳng ra là sợ dở.") == []

def test_markup_stripped():
    assert tags("{nhấn: Bạn có biết} mình dời bao lâu?") == ["ai-tell"]
