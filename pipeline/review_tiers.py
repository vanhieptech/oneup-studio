#!/usr/bin/env python3
"""Two-tier reviewer verdict (DL-074, logs/rule-scoring-rubric.md §3b).

The reviewer (docs/prompts/reviewer-script.md) ends its answer with a 5-line block:

  HARD_FAILS: không | H1: <line>; H3: <line>
  SCORE: A=18 B=13 C=17 D=14 E=14 F=9 G=4 TOTAL=89
  SOFT_WARNINGS: 3
  CONFLICTS: không | <text>
  VERDICT: ĐẠT | ĐẠT VỀ ĐIỂM — … | CHƯA ĐẠT — chặn|sửa nhỏ|sửa vừa|sửa lớn

`parse_block` reads it, `tier_verdict` recomputes the verdict from the hard fails + score only, so soft warnings can
never reject a script and a model cannot "lean strict" past the numbers. Used by review-eval.py and check-rules --review.
"""
import re

PASS_SCORE = 85
WEIGHTS = {"A": 20, "B": 15, "C": 20, "D": 15, "E": 15, "F": 10, "G": 5}
HARD_KINDS = ("H1", "H2", "H3", "H4")
_NONE = {"", "không", "khong", "none", "-", "0", "không có"}


def _line(text, label):
    hits = re.findall(rf"^\s*\**{label}\**\s*:\s*(.*)$", text or "", re.M)
    return hits[-1].strip() if hits else None


def parse_block(text):
    """Return {hard_fails: [..], score: int|None, parts: {A..G}, soft: int|None, conflicts: str|None, verdict_llm: str|None}
    or None when the block is missing (no SCORE and no HARD_FAILS line)."""
    hard, score_l = _line(text, "HARD_FAILS"), _line(text, "SCORE")
    if hard is None and score_l is None: return None
    fails = []
    if hard is not None and hard.lower().strip(" .") not in _NONE:
        fails = [x.strip() for x in re.split(r";\s*(?=H\d)", hard) if x.strip()]
        fails = [x for x in fails if x[:2] in HARD_KINDS] or [hard]
    parts = {k: min(int(v), WEIGHTS[k]) for k, v in re.findall(r"\b([A-G])\s*=\s*(\d+)", score_l or "")}
    tot = re.search(r"TOTAL\s*=\s*(\d+)", score_l or "")
    total = int(tot.group(1)) if tot else (sum(parts.values()) if len(parts) == 7 else None)
    if parts and len(parts) == 7 and total is not None and abs(sum(parts.values()) - total) > 1:
        total = sum(parts.values())  # the parts are what was argued line by line; a mis-added TOTAL loses
    soft = _line(text, "SOFT_WARNINGS")
    sm = re.search(r"\d+", soft or "")
    conf = _line(text, "CONFLICTS")
    conf = None if conf is None or conf.lower().strip(" .") in _NONE else conf
    vl = re.findall(r"VERDICT:\s*(ĐẠT VỀ ĐIỂM|CHƯA ĐẠT|ĐẠT)", text or "")
    return {"hard_fails": fails, "score": total, "parts": parts, "soft": int(sm.group()) if sm else None,
            "conflicts": conf, "verdict_llm": vl[-1] if vl else None}


def tier_verdict(block):
    """(label, size) from the block: hard fail → CHƯA ĐẠT/chặn; else by TOTAL. None when the score is missing."""
    if not block: return None
    if block["hard_fails"]: return ("CHƯA ĐẠT", "chặn")
    s = block["score"]
    if s is None: return None
    if s >= PASS_SCORE: return ("ĐẠT VỀ ĐIỂM", block["conflicts"]) if block["conflicts"] else ("ĐẠT", "")
    return ("CHƯA ĐẠT", "sửa nhỏ" if s >= 75 else "sửa vừa" if s >= 60 else "sửa lớn")


def verdict_of(text):
    """Convenience: computed verdict label for a reviewer answer, falling back to the model's own last VERDICT line."""
    b = parse_block(text)
    v = tier_verdict(b)
    if v: return v[0]
    hits = re.findall(r"VERDICT:\s*(ĐẠT VỀ ĐIỂM|CHƯA ĐẠT|ĐẠT)", text or "")
    return hits[-1] if hits else None
