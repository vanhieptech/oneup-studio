#!/usr/bin/env python3
"""rule-52 (DL-044): print the per-beat effects table from final/spec.json for script-final.md (gate 1).
usage: python3 pipeline/scripts/fx-table.py <clip>/final/spec.json [--write]   (--write replaces the '## Bảng hiệu ứng' section)"""
import json, os, re, sys
specp = sys.argv[1]; s = json.load(open(specp)); ts = s.get("transition_sfx", {})
rows = ["## Bảng hiệu ứng (rule-52, duyệt ở gate 1 trước khi render)",
        f"Transition SFX mặc định: chuyển phần = `{ts.get('part', '?')}`, chuyển scene/section = `{ts.get('scene', '?')}`; lớp nền `ambience` suốt clip (rule-50).", "",
        "| Beat | Engine | Hiệu ứng / ẩn dụ hình ảnh | Gắn với chữ | SFX nhấn → chữ | Chuyển cảnh vào (+SFX) |", "|---|---|---|---|---|---|"]
first = True
for p in s["parts"]:
    items = p.get("scenes", p.get("sections", []))
    for i, x in enumerate(items):
        fx = x.get("fx", {}); acc = [f"`{h['sfx']}` → “{h.get('word', '?')}”" for h in x.get("hits", []) if h.get("sfx")] + [f"`{y['name']}` → “{y.get('word', '?')}”" for y in x.get("sfx", [])]
        if first: tr = "mở đầu"
        elif i == 0: tr = f"{prev_fx or 'fade'} (`{ts.get('part', '?')}`)"
        else: tr = f"{x.get('transition', 'push')} (`{ts.get('scene', '?')}`)"
        rows.append(f"| {x['id']} | {('hyperframes plate ' + x['mg']) if x.get('mg') else p['engine']} | {fx.get('visual', '**THIẾU**')} | “{fx.get('word', '?')}” | {'; '.join(acc) or '—'} | {tr} |"); first = False
    prev_fx = p.get("transitionOut")
table = "\n".join(rows) + "\n"
if "--write" in sys.argv:
    sf = os.path.join(os.path.dirname(specp), "script-final.md"); t = open(sf).read()
    t = re.sub(r"## Bảng hiệu ứng.*?(?=\n## |\Z)", table.rstrip("\n") + "\n", t, flags=re.S) if "## Bảng hiệu ứng" in t else t.replace("\n## Motion picks", "\n" + table + "\n## Motion picks", 1)
    open(sf, "w").write(t)
print(table)
