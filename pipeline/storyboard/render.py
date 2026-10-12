#!/usr/bin/env python3
"""Shared storyboard renderer (rule-36). Source of truth = <clip>/storyboard/spec.json.
Usage: python3 pipeline/storyboard/render.py content/clips/<clip-id> [spec-v3.json]   (needs google-chrome or Chrome.app, Pillow optional)
Edits on feedback: change spec.json (or this renderer for shared style), re-render, commit referencing decision-log id."""
import json, math, random, html, sys, os, subprocess, shutil, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
TOK = json.load(open(ROOT/'brand/brand-tokens.json'))
def chrome():
    for c in [os.environ.get('CHROME'), 'google-chrome', 'chromium', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome']:
        if c and (shutil.which(c) or os.path.exists(c)): return c
    sys.exit('Chrome not found; set CHROME=/path')
GREY, LGREY = "#9A9A97", "#B5B5B2"
class D:  # hand-drawn SVG primitives, deterministic per seed
    def __init__(s, seed, ink): s.R = random.Random(seed); s.ink = ink
    def line(s, x1, y1, x2, y2, w=4, c=None, j=2.2, passes=2):
        c = c or s.ink; R = s.R; o = ""
        for p in range(passes):
            mx = (x1+x2)/2+R.uniform(-j, j)*1.5; my = (y1+y2)/2+R.uniform(-j, j)*1.5
            o += f'<path d="M{x1+R.uniform(-j,j):.1f} {y1+R.uniform(-j,j):.1f} Q{mx:.1f} {my:.1f} {x2+R.uniform(-j,j):.1f} {y2+R.uniform(-j,j):.1f}" stroke="{c}" stroke-width="{w if p==0 else w*.6}" fill="none" stroke-linecap="round" opacity="{1 if p==0 else .55}"/>'
        return o
    def rect(s, x, y, W, H, w=4, c=None): return s.line(x,y,x+W,y,w,c)+s.line(x+W,y,x+W,y+H,w,c)+s.line(x+W,y+H,x,y+H,w,c)+s.line(x,y+H,x,y,w,c)
    def circle(s, cx, cy, r, w=4, c=None, passes=2):
        c = c or s.ink; o = ""
        for p in range(passes):
            st = s.R.uniform(0, 6.28); pts = []
            for i in range(31):
                a = st+i/28*2*math.pi; rr = r*(1+s.R.uniform(-.03, .03)); pts.append(f"{cx+rr*math.cos(a):.1f} {cy+rr*math.sin(a):.1f}")
            o += f'<path d="M{" L".join(pts)}" stroke="{c}" stroke-width="{w if p==0 else w*.6}" fill="none" stroke-linecap="round" opacity="{1 if p==0 else .5}"/>'
        return o
    def arrow(s, x1, y1, x2, y2, w=5, c=None):
        a = math.atan2(y2-y1, x2-x1); L = 26
        return s.line(x1,y1,x2,y2,w,c)+s.line(x2,y2,x2-L*math.cos(a-.45),y2-L*math.sin(a-.45),w,c,passes=1)+s.line(x2,y2,x2-L*math.cos(a+.45),y2-L*math.sin(a+.45),w,c,passes=1)
    def tick(s, x, y, c=None, w=7): return s.line(x,y,x+18,y+20,w,c,1.2)+s.line(x+18,y+20,x+52,y-26,w,c,1.2)
SKETCH = {  # placeholder silhouettes for live shots (coords in 900-wide box)
 'face': lambda d: d.circle(450,560,120,5,GREY)+d.line(250,900,330,760,5,GREY)+d.line(330,760,570,760,5,GREY)+d.line(570,760,650,900,5,GREY),
 'notebook': lambda d: d.rect(260,430,380,470,5,GREY)+d.line(450,430,450,900,4,GREY)+"".join(d.line(480,510+i*60,600,510+i*60,3,LGREY,passes=1) for i in range(5)),
 'hand': lambda d: d.rect(220,470,440,380,5,GREY)+d.line(330,640,560,620,4,LGREY)+d.line(560,620,690,470,7,GREY)+d.circle(700,455,26,5,GREY,1),
 'clock': lambda d: d.circle(450,640,180,6,GREY)+d.line(450,640,450,520,7,GREY)+d.line(450,640,530,640,7,GREY)+"".join(d.line(450+165*math.cos(a),640+165*math.sin(a),450+145*math.cos(a),640+145*math.sin(a),4,GREY,passes=1) for a in [i*math.pi/6 for i in range(12)]),
 'laptop': lambda d: d.rect(270,480,360,240,5,GREY)+d.line(200,760,700,760,6,GREY)+d.line(270,720,200,760,5,GREY)+d.line(630,720,700,760,5,GREY),
 'phone': lambda d: d.rect(330,380,240,440,6,GREY)+d.line(400,410,500,410,4,LGREY,passes=1)+d.circle(450,780,16,4,GREY,1)+d.line(180,880,720,880,5,LGREY),
 'strike': lambda d: d.rect(260,430,380,470,5,GREY)+d.line(300,560,600,560,3,LGREY,passes=1)+d.line(300,640,600,640,3,LGREY,passes=1)+d.line(290,642,610,630,6,GREY),
}
def svg_el(d, e, col):
    t = e['type']; c = col.get(e.get('color'), e.get('color')) if e.get('color') else None
    if t == 'strike': return d.line(*e['xy'], w=e.get('w', 8), c=c, j=2.5)
    if t == 'line': return d.line(*e['xy'], w=e.get('w', 4), c=c)
    if t == 'underline': x, y, w = e['xy']; return d.line(x, y, x+w, y+d.R.uniform(-4,4), 5, c, 1.5)
    if t == 'box': return d.rect(*e['xywh'], w=e.get('w', 6), c=c)
    if t == 'arrow': return d.arrow(*e['xy'], w=e.get('w', 5), c=c)
    if t == 'tick': return d.tick(*e['xy'], c=c)
    if t == 'glyph': x, y = e['xy']; return f'<text x="{x}" y="{y}" font-size="{e.get("size",120)}" font-family="BVP" font-weight="700" fill="{col["ink"]}" transform="rotate({e.get("rotate",0)} {x} {y})">{html.escape(e["text"])}</text>'
    if t == 'bar':  # value 0..1 progress bar with optional marks
        x, y, w = e['xyw']; o = f'<rect x="{x}" y="{y}" width="{w}" height="40" rx="20" fill="#ECECE9"/><rect x="{x}" y="{y}" width="{w*e["value"]:.0f}" height="40" rx="20" fill="{col["ink"]}"/>'
        return o+"".join(d.line(x+w*m, y-15, x+w*m, y+55, 3, col['muted'], 1) for m in e.get('marks', []))
    raise ValueError(f'unknown svg element {t}')
def css(fonts, col):
    ff = "".join(f'@font-face{{font-family:BVP;src:url({fonts}BeVietnamPro-{n}.ttf);font-weight:{w}}}' for n, w in [('Regular',400),('Medium',500),('SemiBold',600),('Bold',700)])
    return ff+open(pathlib.Path(__file__).parent/'style.css').read().replace('$BG', col['bg']).replace('$INK', col['ink']).replace('$MUTED', col['muted']).replace('$BORDER', col['border'])
def render(clip, spec_name='spec.json'):
    clip = pathlib.Path(clip).resolve(); src = clip/'storyboard'; spec = json.load(open(src/spec_name))
    sb = src/spec['out'] if spec.get('out') else src; sb.mkdir(exist_ok=True)
    theme = spec['theme'].lower(); col = dict(TOK['colors'][theme]); col['green'] = col['success']
    fonts = (ROOT/'brand/fonts').as_uri()+'/'; logo = (ROOT/spec.get('logo', 'brand/logos/05-pair-plus.svg')).read_text().split('?>')[-1]
    logo = logo.replace('<svg ', f'<svg width="72" height="72" style="color:{col["ink"]}" ', 1).replace('svg{color:#111111}', '')
    build = src/'.build'; build.mkdir(exist_ok=True); C = chrome()
    for b in spec['beats']:
        d = D(spec.get('seed', 7)*100+b['n'], col['ink'])
        cap = b['caption']; hl = cap['highlight']
        caps = " ".join(f"<b>{html.escape(w)}</b>" if i == hl else (f"<em>{html.escape(w)}</em>" if i < hl else html.escape(w)) for i, w in enumerate(cap['words']))
        live = ""
        if b.get('shot'):
            s = b['shot']; live = f'<div class="live" style="top:280px;height:820px"><svg class="sil" viewBox="0 0 900 820" width="900" height="820"><g transform="translate(90,50) scale(0.8)">{SKETCH[s["sketch"]](d)}</g></svg><div class="tag"><b>{s["id"]}</b> · {html.escape(s["label"])}<span>live shot · placeholder</span></div></div>'
        texts = "".join(f'<div class="{t["style"]}" style="top:{t["top"]}px;{t.get("css","")}">{t["html"]}</div>' for t in b.get('onscreen', []))
        svgs = "".join(svg_el(d, e, col) for e in b.get('draw', []))
        doc = f'''<!doctype html><html><head><meta charset="utf-8"><style>{css(fonts,col)}</style></head><body>
<div class="top">{logo}<div>OneUp<span>.</span></div></div><div class="meta">{b["n"]:02d} · {b["time"]} · {b["part"]}</div>
{live}{texts}<svg class="over" width="1080" height="1920">{svgs}</svg><div class="cap">{caps}</div>
<div class="rside"></div><div class="safe"><span>TikTok UI zone · keep clear</span></div></body></html>'''
        h = build/f'beat-{b["n"]:02d}.html'; h.write_text(doc)
        subprocess.run([C, '--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1', '--window-size=1080,1920', '--virtual-time-budget=3000', f'--screenshot={sb}/beat-{b["n"]:02d}.png', h.as_uri()], capture_output=True)
    # contact sheet 2x5
    cells = "".join(f'<div class="c"><img src="{(sb/f"beat-{b["n"]:02d}.png").as_uri()}"><div class="h"><b>{b["n"]:02d}</b><span>{b["time"]} · {b["part"]}</span></div><p>{html.escape(b["vi"])}</p></div>' for b in spec['beats'])
    sh = build/'sheet.html'; sh.write_text(f'<!doctype html><meta charset="utf-8"><style>{css(fonts,col)}{open(pathlib.Path(__file__).parent/"sheet.css").read()}</style><div class="sheet"><h1>{html.escape(spec["title"])}</h1><div class="sub">{html.escape(spec["subtitle"])}</div><div class="g">{cells}</div></div>')
    subprocess.run([C, '--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars', '--window-size=2400,2200', '--virtual-time-budget=4000', f'--screenshot={sb}/storyboard.png', sh.as_uri()], capture_output=True)
    print('rendered', len(spec['beats']), 'beats ->', sb)
if __name__ == '__main__': render(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'spec.json')  # optional variant spec, e.g. spec-v3.json (writes to spec['out'])
