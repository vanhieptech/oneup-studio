import json,html
B=json.load(open('beats.json'))
F="../../../../../brand/fonts/"
cells="".join(f'''<div class="c"><img src="../beat-{b["n"]:02d}.png"><div class="h"><b>{b["n"]:02d}</b><span>{b["t"]} · {b["part"]}</span></div><p>{html.escape(b["vi"])}</p></div>''' for b in B)
open('sheet.html','w').write(f'''<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:BVP;src:url({F}BeVietnamPro-Regular.ttf);font-weight:400}}@font-face{{font-family:BVP;src:url({F}BeVietnamPro-Bold.ttf);font-weight:700}}@font-face{{font-family:BVP;src:url({F}BeVietnamPro-Medium.ttf);font-weight:500}}
*{{margin:0;box-sizing:border-box}}body{{width:2400px;background:#F7F7F5;font-family:BVP;color:#111;padding:80px}}
h1{{font-size:56px;letter-spacing:-.03em}}.sub{{color:#6B6B6B;font-size:26px;margin:12px 0 56px}}
.g{{display:grid;grid-template-columns:repeat(5,1fr);gap:48px 40px}}.c img{{width:100%;border-radius:20px;border:2px solid #E3E3E0;display:block}}
.h{{display:flex;gap:14px;align-items:baseline;margin:20px 0 8px}}.h b{{font-size:34px}}.h span{{color:#6B6B6B;font-size:22px;font-weight:500;text-transform:uppercase;letter-spacing:.05em}}
p{{font-size:24px;line-height:1.45}}</style>
<h1>Clip 01 · Implementation intention — Storyboard</h1><div class="sub">@hi.oneup · script v2 · 55–60s · LIGHT · placeholders = live shots Hiệp quay (S1–S7)</div><div class="g">{cells}</div>''')
