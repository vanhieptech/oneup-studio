#!/usr/bin/env python3
"""Rule 58 helper: list 2–3 syllable compounds in a line that exist in Viet74K, flag vague words, suggest sharper ones.
usage: vn-words.py "<câu tiếng Việt>"   |   vn-words.py --spec <spec.json>"""
import json, os, re, sys
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = set(w.strip().lower() for w in open(os.path.join(R, "resources/vn-dict/Viet74K.txt"), encoding="utf8"))
TH = {}
for l in open(os.path.join(R, "resources/vn-dict/thesaurus.md"), encoding="utf8"):
    m = re.match(r"\| ([^|]+) \| ([^|]+) \|$", l.strip())
    if m and not m.group(1).startswith(("Nhạt", "---")): TH[m.group(1).strip()] = m.group(2).strip()
def scan(t):
    ws = re.sub(r"[^\w\s]", " ", re.sub(r"\{[^}]*\}", "", t.lower())).split()
    comp = [" ".join(ws[i:i + n]) for n in (3, 2) for i in range(len(ws) - n + 1) if " ".join(ws[i:i + n]) in D]
    sug = [f"{k} → {v}" for k, v in TH.items() if any(x.strip() and x.strip().split(" (")[0] in t.lower() for x in k.split("/"))]
    return comp, sug
if __name__ == "__main__":
    lines = [sys.argv[1]] if sys.argv[1] != "--spec" else [l["text"] for p in json.load(open(sys.argv[2]))["parts"] for x in p.get("scenes", p.get("sections", [])) for l in x["lines"]]
    for t in lines:
        c, s = scan(t); print(f"• {t}\n   từ ghép trong từ điển: {', '.join(c) or '—'}" + (f"\n   gợi ý: {' · '.join(s)}" if s else ""))
