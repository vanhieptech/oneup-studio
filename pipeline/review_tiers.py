#!/usr/bin/env python3
"""Two-tier reviewer verdict: Tier 1 Hard-Gate (H1–H4) + Tier 2 Pairwise A/B (and legacy SCORE support).

Pairwise A/B block (preferred, replaces absolute ≥85 score threshold):

  HARD_FAILS: không | H1: <line>; H3: <line>
  PAIRWISE: WIN | TIE | LOSE (so với <anchor_id>)
  TOP_FIXES: tối đa 3 điểm sửa cụ thể nhất (ghi rõ beat/câu)
  CONFLICTS: không | <mục cần Hiệp quyết định>
  VERDICT: ĐẠT | CẦN SỬA

Legacy score block (DL-074, kept for backward compatibility with older review.md files):

  HARD_FAILS: không | H1: <line>; H3: <line>
  SCORE: A=18 B=13 C=17 D=14 E=14 F=9 G=4 TOTAL=89
  SOFT_WARNINGS: 3
  CONFLICTS: không | <text>
  VERDICT: ĐẠT | ĐẠT VỀ ĐIỂM — … | CHƯA ĐẠT — chặn|sửa nhỏ|sửa vừa|sửa lớn

`parse_block` reads either format, `is_hard_blocked` checks Tier 1 (H1–H4) as the sole hard gate, and
`tier_verdict` recomputes the verdict deterministically from the structured lines.
Used by review-eval.py and check-rules --review.
"""
import re

PASS_SCORE = 85
WEIGHTS = {"A": 20, "B": 15, "C": 20, "D": 15, "E": 15, "F": 10, "G": 5}
HARD_KINDS = ("H1", "H2", "H3", "H4")
PAIRWISE_VALUES = ("WIN", "TIE", "LOSE")
_NONE = {"", "không", "khong", "none", "-", "0", "không có", "n/a"}
_VERDICT_RE = re.compile(r"VERDICT\**\s*:\s*\**(ĐẠT VỀ ĐIỂM|CHƯA ĐẠT|CẦN SỬA|ĐẠT)", re.I)


def _line(text, label):
    hits = re.findall(rf"^[ \t]*\**{label}\**[ \t]*:[ \t]*(.*)$", text or "", re.M)
    return hits[-1].strip() if hits else None


def _extract_top_fixes(text):
    """Extract up to 3 concrete fixes from TOP_FIXES: inline (numbered or ; separated) or following bullet lines."""
    if not text:
        return []
    matches = list(re.finditer(r"^[ \t]*\**TOP_FIXES\**[ \t]*:[ \t]*(.*)$", text, re.M))
    if not matches:
        return []
    m = matches[-1]
    inline = m.group(1).strip()
    if inline and inline.lower().strip(" .") not in _NONE:
        # Prefer splitting on numbered markers (1. ... 2. ... 3. ...) so semicolons inside one fix stay intact
        if re.search(r"(?:^|\s)2[.)]\s", inline):
            items = [x.strip() for x in re.split(r"\s+(?=\d+[.)]\s)", inline) if x.strip()]
        elif ";" in inline:
            items = [x.strip() for x in inline.split(";") if x.strip()]
        else:
            items = [inline]
        return [re.sub(r"^\d+[.)]\s*", "", x).strip(" ;") for x in items if x.lower().strip(" .") not in _NONE][:3]
    # Otherwise look at indented / bulleted lines right after TOP_FIXES:
    tail = text[m.end():].splitlines()
    items = []
    for ln in tail:
        s = ln.strip()
        if not s:
            if items:
                break
            continue
        if re.match(r"^\**(?:HARD_FAILS|PAIRWISE|SCORE|SOFT_WARNINGS|CONFLICTS|VERDICT)\**\s*:", s):
            break
        bm = re.match(r"^(?:[-*•]|\d+[.)])\s+(.+)$", s)
        if bm:
            val = bm.group(1).strip()
            if val.lower().strip(" .") not in _NONE:
                items.append(val)
        else:
            break
    return items[:3]


def _parse_hard_fails(hard):
    """Parse HARD_FAILS line into (items, kinds). Strictly recognizes H1–H4."""
    if hard is None or hard.lower().strip(" .") in _NONE:
        return [], []
    raw = [x.strip() for x in re.split(r";\s*(?=H\d)", hard) if x.strip()]
    fails = [x for x in raw if x[:2].upper() in HARD_KINDS] or [hard]
    kinds = []
    for f in fails:
        km = re.match(r"^(H[1-4])\b", f.strip(), re.I)
        if km and km.group(1).upper() not in kinds:
            kinds.append(km.group(1).upper())
    return fails, kinds


def parse_block(text):
    """Parse either a Pairwise A/B block or a legacy SCORE block.

    Returns dict with keys:
      mode ('pairwise'|'score'), hard_fails, hard_kinds, pairwise ('WIN'|'TIE'|'LOSE'|None),
      anchor (str|None), top_fixes ([str]), score (int|None), parts ({A..G}), soft (int|None),
      conflicts (str|None), verdict_llm (str|None)
    or None when no structured block is present.
    """
    hard = _line(text, "HARD_FAILS")
    pw_l = _line(text, "PAIRWISE")
    score_l = _line(text, "SCORE")
    if hard is None and pw_l is None and score_l is None:
        return None

    fails, kinds = _parse_hard_fails(hard)

    # Pairwise A/B fields
    pairwise, anchor = None, None
    if pw_l is not None:
        pm = re.search(r"\b(WIN|TIE|LOSE)\b", pw_l, re.I)
        if pm:
            pairwise = pm.group(1).upper()
        am = re.search(r"(?:so với|vs\.?)\s+([a-zA-Z0-9._-]+)", pw_l, re.I)
        if am:
            anchor = am.group(1).strip("().,; ")
    top_fixes = _extract_top_fixes(text)

    # Legacy SCORE fields
    parts = {k: min(int(v), WEIGHTS[k]) for k, v in re.findall(r"\b([A-G])\s*=\s*(\d+)", score_l or "")}
    tot = re.search(r"TOTAL\s*=\s*(\d+)", score_l or "")
    total = int(tot.group(1)) if tot else (sum(parts.values()) if len(parts) == 7 else None)
    if parts and len(parts) == 7 and total is not None and abs(sum(parts.values()) - total) > 1:
        total = sum(parts.values())  # the parts are what was argued line by line; a mis-added TOTAL loses
    soft = _line(text, "SOFT_WARNINGS")
    sm = re.search(r"\d+", soft or "")

    conf = _line(text, "CONFLICTS")
    conf = None if conf is None or conf.lower().strip(" .") in _NONE else conf
    vl = [m.upper() for m in _VERDICT_RE.findall(text or "")]

    mode = "pairwise" if pw_l is not None else "score"
    return {
        "mode": mode,
        "hard_fails": fails,
        "hard_kinds": kinds,
        "pairwise": pairwise,
        "anchor": anchor,
        "top_fixes": top_fixes,
        "score": total,
        "parts": parts,
        "soft": int(sm.group()) if sm else None,
        "conflicts": conf,
        "verdict_llm": vl[-1] if vl else None,
    }


def is_hard_blocked(block):
    """Tier 1 hard gate (sole hard blocker): True iff any H1–H4 hard fail is present."""
    return bool(block and block.get("hard_fails"))


def tier_verdict(block):
    """Compute (label, detail) from the parsed block.

    - Tier 1 hard fail (H1–H4) always rejects: ('CẦN SỬA', 'chặn') in pairwise mode, ('CHƯA ĐẠT', 'chặn') in score mode.
    - Pairwise mode (Tier 2):
        WIN | TIE → ('ĐẠT', '') or ('ĐẠT VỀ ĐIỂM', conflicts)
        LOSE      → ('CẦN SỬA', 'thua cặp')
    - Legacy score mode (Tier 2):
        TOTAL ≥ 85 → ('ĐẠT', '') or ('ĐẠT VỀ ĐIỂM', conflicts)
        TOTAL < 85 → ('CHƯA ĐẠT', 'sửa nhỏ'|'sửa vừa'|'sửa lớn')
    """
    if not block:
        return None
    mode = block.get("mode", "score")
    if block["hard_fails"]:
        return ("CẦN SỬA", "chặn") if mode == "pairwise" else ("CHƯA ĐẠT", "chặn")
    if mode == "pairwise":
        pw = block.get("pairwise")
        if pw is None:
            return None
        if pw == "LOSE":
            return ("CẦN SỬA", "thua cặp")
        return ("ĐẠT VỀ ĐIỂM", block["conflicts"]) if block["conflicts"] else ("ĐẠT", "")
    s = block["score"]
    if s is None:
        return None
    if s >= PASS_SCORE:
        return ("ĐẠT VỀ ĐIỂM", block["conflicts"]) if block["conflicts"] else ("ĐẠT", "")
    return ("CHƯA ĐẠT", "sửa nhỏ" if s >= 75 else "sửa vừa" if s >= 60 else "sửa lớn")


def verdict_of(text):
    """Convenience: computed verdict label for a reviewer answer, falling back to the model's last VERDICT line."""
    b = parse_block(text)
    v = tier_verdict(b)
    if v:
        return v[0]
    hits = [m.upper() for m in _VERDICT_RE.findall(text or "")]
    return hits[-1] if hits else None
