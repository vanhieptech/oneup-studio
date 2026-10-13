"""Voice script markup (DL-039, L-017). Shared by voice-prosody.py, build-final.py, check-rules.py.

Markup inside a line's text / phrases[].t (never shown on screen; bubbles use `text`):
  {ừm} {ờ} {à} {ơ} {hừm} {ủa} {trời ơi} {thì là}  filler spoken INSIDE the next F5 unit ("ừm..." + clause,
                                                   merged by the ≥4-syllable rule → never cut out of an output)
  {bank:ừm}            filler from the cached per-character filler bank, inserted BETWEEN units with room tone
  {ngập ngừng}         hesitation inside a unit: F5 gets "..." without splitting the unit
  {kéo: nha}           lengthened particle, spelling from particle-styles.json for that character
  {nhỏ: …text…}        aside, quieter (−4 dB), own unit — same as "(…)"
Punctuation that also shapes delivery: , ; : . ? ! … — ( ) “ ” (pause per mark, see PAUSE).
"""
import json, os, re, unicodedata, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
FILLERS = {"ừm": "ừm...", "um": "ừm...", "ờ": "ờ...", "à": "à,", "ơ": "ơ...", "hừm": "hừm...", "hmm": "hừm...", "ủa": "ủa?", "trời ơi": "trời ơi!", "thì là": "thì là..."}
PARTICLES = ["nha", "á", "hông", "nè", "ha", "luôn", "ta", "đó", "hả", "nghen"]
PAUSE = {",": 0.18, ";": 0.26, ":": 0.28, ".": 0.35, "?": 0.42, "!": 0.38, "…": 0.52, "...": 0.52, "—": 0.12, "(": 0.20, ")": 0.20, "“": 0.15, "”": 0.15, '"': 0.15}
HES = "\u22ef"      # in-unit hesitation placeholder (not a split mark) → "..." for F5
ASIDE_DB = -4.0
MARK_RE = re.compile(r"\{([^{}]+)\}")
# filler density caps (voice-profile §3c): per line ≤ 1, per clip ≤ max(2, lines // 4)
MAX_FILLERS_LINE = 1

def styles():
    p = os.path.join(HERE, "particle-styles.json")
    return json.load(open(p)) if os.path.exists(p) else {}

def validate(text):
    """Returns list of problems for unknown/ill-formed markup."""
    bad = []
    for m in MARK_RE.finditer(text):
        k = m.group(1).strip(); kl = k.lower()
        if kl in FILLERS or kl == "ngập ngừng": continue
        if kl.startswith("bank:") and kl[5:].strip() in FILLERS: continue
        if kl.startswith("kéo:") and kl[4:].strip() in PARTICLES: continue
        if kl.startswith("nhỏ:") and kl[4:].strip(): continue
        bad.append(m.group(0))
    if text.count("{") != text.count("}"): bad.append("unbalanced braces")
    return bad

def count_fillers(text):
    return sum(1 for m in MARK_RE.finditer(text) if m.group(1).strip().lower() in FILLERS or m.group(1).strip().lower().startswith("bank:"))

def expand(text, character=None):
    """Markup → (F5 text with placeholders, bank list). Bank fillers become tokens §i§ (unit separators)."""
    st = styles().get(character or "", {}); bank = []
    def rep(m):
        k = m.group(1).strip(); kl = k.lower()
        if kl in FILLERS: return " " + FILLERS[kl] + " "
        if kl == "ngập ngừng": return HES + " "
        if kl.startswith("bank:"): bank.append(kl[5:].strip()); return f" §{len(bank) - 1}§ "
        if kl.startswith("kéo:"):
            p = kl[4:].strip(); return st.get(p, {}).get("long", p)
        if kl.startswith("nhỏ:"): return " (" + k[4:].strip() + ") "
        return m.group(0)
    t = MARK_RE.sub(rep, text)
    return re.sub(r"\s+", " ", t).strip(), bank

def auto_particles(unit, character):
    """Sentence-final particle → best spelling for this character (table 'auto'), only right before . ! ? …"""
    st = styles().get(character or "", {})
    def rep(m):
        p = m.group(1); s = st.get(p.lower(), {})
        return (s.get("auto") or p) + m.group(2)
    return re.sub(r"(?<!\w)(" + "|".join(PARTICLES) + r")(\s*(?:\.\.\.|[.!?…])+)\s*$", rep, unit, flags=re.I)

def spoken(text, character=None):
    """Plain spoken text (for STT comparison): markup expanded, placeholders removed."""
    t, _ = expand(text, character)
    return re.sub(r"§\d+§", " ", t).replace(HES, "...").strip()

def visible(text):
    """Caption/bubble-safe text: markup removed (fillers dropped, asides kept)."""
    t = MARK_RE.sub(lambda m: (m.group(1).split(":", 1)[1].strip() if m.group(1).lower().startswith(("kéo:", "nhỏ:")) else ""), text)
    return re.sub(r"\s+", " ", t).strip()

def bank_pick(character, filler, key, n):
    return int(hashlib.sha1(f"{character}|{filler}|{key}".encode()).hexdigest(), 16) % max(1, n)
