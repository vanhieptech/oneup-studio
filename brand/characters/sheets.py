#!/usr/bin/env python3
"""Render character model sheets -> brand/characters/*.png  (python3 brand/characters/sheets.py)"""
import sys, pathlib, subprocess
sys.path.insert(0, str(pathlib.Path(__file__).parent)); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]/'pipeline/storyboard'))
from rig import *
from render import chrome
HERE = pathlib.Path(__file__).parent; FONTS = (ROOT/'brand/fonts').as_uri()+'/'
CSS = "".join(f'@font-face{{font-family:BVP;src:url({FONTS}BeVietnamPro-{n}.ttf);font-weight:{w}}}' for n, w in [('Regular',400),('Medium',500),('SemiBold',600),('Bold',700)])
def page(w, h, title, sub, svg):
    return f'''<!doctype html><meta charset="utf-8"><style>{CSS}*{{margin:0}}body{{width:{w}px;height:{h}px;background:{PAPER};font-family:BVP;color:{INK}}}
.t{{position:absolute;left:80px;top:60px;font-size:52px;font-weight:700;letter-spacing:-.03em}}.s{{position:absolute;left:80px;top:130px;font-size:24px;color:{MUTED}}}
.l{{font:600 22px BVP;fill:{MUTED};letter-spacing:.06em;text-transform:uppercase}}</style>
<div class="t">{title}</div><div class="s">{sub}</div><svg width="{w}" height="{h}" style="position:absolute;left:0;top:0"><defs>{FILTER()}</defs>{svg}</svg>'''
def shot(name, w, h, html):
    f = HERE/f'.build/{name}.html'; f.parent.mkdir(exist_ok=True); f.write_text(html)
    subprocess.run([chrome(), '--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars', f'--window-size={w},{h}', '--virtual-time-budget=3000', f'--screenshot={HERE}/{name}.png', f.as_uri()], capture_output=True)
def lab(x, y, t): return f'<text class="l" x="{x}" y="{y}" text-anchor="middle">{t}</text>'
# 1. Hiệp turnaround + expressions
W, H = 2400, 1500
svg = lab(400, 250, 'Turnaround') 
for i, v in enumerate(['front', 'q34', 'side']):
    x = 220 + i*330; svg += f'<g transform="translate({x},420)">{hiep(v, "neutral")}</g>' + lab(x, 800, {'front':'front','q34':'3/4','side':'side'}[v])
svg += f'<path d="M80,860 L2320,860" stroke="#DCDCD8" stroke-width="2"/>' + lab(240, 920, 'Expressions')
for i, e in enumerate(['neutral', 'tired', 'procrastinating', 'surprised', 'focused', 'proud']):
    x = 230 + i*360; svg += f'<g transform="translate({x},1080) scale(1.25)"><g filter="url(#hand)">{head("front", e)}</g></g>' + lab(x, 1220, e)
    if e == 'procrastinating': svg += phone(x+60, 1110, 12, False)
svg += f'<g transform="translate(1260,180)"><text class="l" x="0" y="70">Size relation</text><g transform="translate(180,240)">{hiep("q34","neutral")}</g>{omi(420, 230, 110, "wave")}<path d="M420,300 L420,330" stroke="#DCDCD8" stroke-width="2" stroke-dasharray="6 6"/>'
svg += f'<text x="500" y="200" font-family="BVP" font-size="24" fill="{MUTED}">Omi ≈ 0.9× head</text><text x="500" y="232" font-family="BVP" font-size="24" fill="{MUTED}">floats at shoulder height</text><text x="500" y="264" font-family="BVP" font-size="24" fill="{MUTED}">never touches ground</text></g>'
svg += f'<text x="80" y="1420" font-family="BVP" font-size="22" fill="{MUTED}">Stylized avatar, not a likeness. Tune hair, glasses, clothing from Hiệp\'s description. Rig v0.1: brand/characters/rig.py</text>'
shot('hiep-model-sheet', W, H, page(W, H, 'Hiệp: model sheet v0.1', 'Protagonist · ink on paper · Be Vietnam Pro · code-drawn (brand/characters/rig.py)', svg))
# 2. key poses
svg = ''
# desk + laptop
svg += f'<g transform="translate(330,520)">{hiep("q34","focused")}</g>' + desk(120, 760, 760) + laptop(300, 760, 260) + lab(440, 980, 'At desk · laptop')
# bed + phone (lying): rotate figure
svg += f'<g transform="translate(1000,0)"><rect x="80" y="640" width="640" height="190" rx="30" fill="{SOFT}" stroke="{INK}" stroke-width="5"/><rect x="100" y="560" width="200" height="110" rx="40" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>'
svg += f'<g transform="translate(220,600) rotate(-80) scale(0.9)"><g filter="url(#hand)">{head("front","procrastinating")}</g></g><path d="M260,700 C420,640 600,640 700,700" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>{phone(300,540,-25)}</g>' + lab(1400, 980, 'In bed · phone (late)')
# writing in notebook
svg += f'<g transform="translate(2000,500)">{hiep("front","focused")}</g>' + desk(1780, 2240, 760) + notebook(1880, 750, 210) + pen_hand(2070, 730) + lab(2010, 980, 'Writing · notebook')
shot('hiep-poses', 2400, 1100, page(2400, 1100, 'Hiệp: key poses v0.1', 'At desk · in bed with phone · writing in notebook', svg))
# 3. Omi sheet
moods = ['idle','wave','think','quiet','listen','celebrate','sleep','proud','spark','blush','worry','cheer']
svg = lab(420, 250, 'Form: companion (assistant role)')
for i, m in enumerate(moods):
    x = 200 + (i % 6)*340; y = 400 + (i//6)*300
    svg += omi(x, y, 150, m, float_=False) + lab(x, y+130, m)
svg += f'<path d="M80,1000 L2320,1000" stroke="#DCDCD8" stroke-width="2"/>' + lab(420, 1060, 'Other forms (not used in comics)')
for i, f in enumerate(['seed','companion','guide','anchor']):
    svg += omi(220+i*220, 1180, 110, 'idle', f, float_=False) + lab(220+i*220, 1280, f)
svg += lab(1600, 1060, 'How Omi appears') + omi(1400, 1200, 110, 'spark')
svg += bubble(1500, 1110, 600, 150, (-40, 30), 'omi', 'Try one line: <b>IF</b> 9pm → <b>THEN</b> listening.', 30)
shot('omi-sheet', 2400, 1420, page(2400, 1420, 'Omi: character sheet', 'Existing brand SVGs (brand/omi-exports) · companion form · floating, no body · Omi bubble = soft card + dot tail + Omi tag', svg))
print('ok')
