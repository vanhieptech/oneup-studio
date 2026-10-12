#!/usr/bin/env python3
"""Comic strip renderer (rule-36 spirit). Source: <clip>/comic/spec.json -> <clip>/comic/strip.png (1080x1920).
Characters come from brand/characters/rig.py. Usage: python3 pipeline/comic/render.py content/clips/<clip-id>"""
import sys, json, pathlib, subprocess, html
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'brand/characters')); sys.path.insert(0, str(ROOT/'pipeline/storyboard'))
from rig import *
from render import chrome
PW, PH = 960, 330   # panel size
def scene(kind, expr):
    if kind == 'desk':
        return f'<g transform="translate(300,150) scale(0.62)">{hiep("q34", expr)}</g>' + desk(120, 640, 300) + laptop(250, 300, 200) + f'<rect x="470" y="262" width="90" height="38" fill="{PAPER}" stroke="{INK}" stroke-width="4"/><text x="515" y="288" text-anchor="middle" font-family="BVP" font-weight="700" font-size="18">TOEIC</text>'
    if kind == 'bed':
        return (f'<rect x="60" y="200" width="620" height="110" rx="24" fill="{SOFT}" stroke="{INK}" stroke-width="5"/><rect x="80" y="150" width="170" height="80" rx="30" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>'
                f'<g transform="translate(180,170) rotate(-80) scale(0.62)"><g filter="url(#hand)">{head("front", expr)}</g></g><path d="M220,240 C380,200 560,200 680,240" fill="none" stroke="{INK}" stroke-width="5"/>{phone(236,96,-35,False)}')
    if kind == 'desk-notebook':
        return f'<g transform="translate(790,120) scale(0.62)">{hiep("front", expr)}</g>' + desk(600, 950, 300) + notebook(700, 292, 150, 2)
    raise ValueError(kind)
def render(clip):
    clip = pathlib.Path(clip).resolve(); spec = json.load(open(clip/'comic/spec.json'))
    fonts = (ROOT/'brand/fonts').as_uri()+'/'
    css = "".join(f'@font-face{{font-family:BVP;src:url({fonts}BeVietnamPro-{n}.ttf);font-weight:{w}}}' for n, w in [('Regular',400),('Medium',500),('SemiBold',600),('Bold',700)])
    css += open(ROOT/'pipeline/storyboard/style.css').read().replace('$BG', PAPER).replace('$INK', INK).replace('$MUTED', MUTED).replace('$BORDER', '#E3E3E0')
    logo = (ROOT/'brand/logos/05-pair-plus.svg').read_text().split('?>')[-1].replace('<svg ', '<svg width="72" height="72" style="color:#111" ', 1)
    svg = ''
    for i, p in enumerate(spec['panels']):
        y0 = 260 + i*(PH+22)
        inner = scene(p['scene'], p['expr'])
        if p.get('omi'): o = p['omi']; inner += omi(o['x'], o['y'], o['size'], o['mood'])
        for b in p.get('bubbles', []): inner += bubble(b['x'], b['y'], b['w'], b['h'], tuple(b['tail']), b['who'], b['text'], 32)
        if p.get('narration'): inner += narration(0, 0, html.escape(p['narration']), font=22)
        svg += (f'<clipPath id="c{i}"><rect width="{PW}" height="{PH}" rx="6"/></clipPath><g transform="translate(60,{y0})">'
                f'<rect width="{PW}" height="{PH}" rx="6" fill="{PAPER}"/><g clip-path="url(#c{i})">{inner}</g>'
                f'<g filter="url(#hand)"><rect width="{PW}" height="{PH}" rx="6" fill="none" stroke="{INK}" stroke-width="6"/></g></g>')
    cap = spec['caption']; hl = cap['highlight']
    caps = " ".join(f"<b>{html.escape(w)}</b>" if i == hl else (f"<em>{html.escape(w)}</em>" if i < hl else html.escape(w)) for i, w in enumerate(cap['words']))
    doc = f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="top">{logo}<div>OneUp<span>.</span></div></div><div class="meta">clip-01 · comic · b01–b03</div>
<svg class="over" width="1080" height="1920"><defs>{FILTER()}</defs>{svg}</svg><div class="cap" style="top:1330px">{caps}</div>
<div class="rside"></div><div class="safe"><span>TikTok UI zone · keep clear</span></div></body></html>'''
    b = clip/'comic/.build'; b.mkdir(exist_ok=True); (b/'strip.html').write_text(doc)
    subprocess.run([chrome(), '--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars', '--window-size=1080,1920', '--virtual-time-budget=3000', f'--screenshot={clip}/comic/strip.png', (b/'strip.html').as_uri()], capture_output=True)
    print('rendered', clip/'comic/strip.png')
if __name__ == '__main__': render(sys.argv[1])
