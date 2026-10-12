"""Character rig v0.1 (code-drawn, brand ink/paper). Hiệp = stylized avatar, NOT his real face.
All functions return SVG fragments in local coords; head centre = (0,0), head radius 62."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[2]
INK, PAPER, MUTED, SOFT, GREEN = "#111111", "#F7F7F5", "#6B6B6B", "#ECECE9", "#1A7F4B"
S = f'stroke="{INK}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"'
def FILTER(id_='hand', scale=2.2, seed=3):
    return f'<filter id="{id_}"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="{seed}"/><feDisplacementMap in="SourceGraphic" scale="{scale}"/></filter>'
# ---------- Hiệp ----------
HAIR = {
 'front': "M-66,-2 C-70,-78 70,-82 66,-2 C60,-26 52,-30 44,-22 C36,-36 20,-38 8,-28 C-6,-40 -26,-36 -36,-24 C-46,-32 -60,-26 -66,-2Z",
 'q34':   "M-60,-4 C-66,-80 74,-84 70,4 C64,-22 56,-28 48,-20 C40,-36 24,-38 12,-28 C0,-38 -20,-34 -30,-22 C-40,-30 -54,-24 -60,-4Z",
 'side':  "M-62,8 C-70,-76 60,-86 64,-10 C56,-26 46,-30 38,-24 C30,-34 18,-34 10,-26 C-4,-28 -20,-18 -30,-4 C-40,-6 -50,0 -62,8Z",
}
FACE_DX = {'front': 0, 'q34': 16, 'side': 34}
def eyes(expr, dx=0, view='front'):
    L, R = (-22+dx, 6), (22+dx, 6)
    pts = [L, R] if view != 'side' else [(dx, 6)]
    o = ""
    for (x, y) in pts:
        if expr in ('neutral', 'procrastinating'):
            ox = 3 if expr == 'procrastinating' else 0
            o += f'<circle cx="{x+ox}" cy="{y+(3 if expr=="procrastinating" else 0)}" r="5.5" fill="{INK}"/>'
        elif expr == 'tired':
            o += f'<path d="M{x-9},{y} q9,6 18,0" fill="none" {S}/><path d="M{x-7},{y+12} q7,3 14,0" fill="none" stroke="{MUTED}" stroke-width="3" stroke-linecap="round"/>'
        elif expr == 'surprised':
            o += f'<circle cx="{x}" cy="{y}" r="9" fill="{PAPER}" {S}/><circle cx="{x}" cy="{y}" r="3.5" fill="{INK}"/>'
        elif expr == 'focused':
            o += f'<path d="M{x-7},{y} a7,7 0 0,0 14,0 Z" fill="{INK}"/><path d="M{x-10},{y-1} L{x+10},{y-1}" {S}/>'
        elif expr == 'proud':
            o += f'<path d="M{x-9},{y+3} q9,-11 18,0" fill="none" {S}/>'
    return o
def brows(expr, dx=0, view='front'):
    sides = [-1, 1] if view != 'side' else [1]
    o = ""
    for s in sides:
        x = (22*s + dx) if view != 'side' else dx
        if expr == 'surprised': o += f'<path d="M{x-10},-20 q10,-8 20,0" fill="none" {S}/>'
        elif expr == 'focused': o += f'<path d="M{x-10*s},-14 L{x+10*s},-8" {S}/>' if view != 'side' else f'<path d="M{x-10},-14 L{x+10},-9" {S}/>'
        elif expr == 'tired': o += f'<path d="M{x-10},-10 L{x+10},-12" {S} opacity=".8"/>'
        elif expr == 'proud': o += f'<path d="M{x-10},-15 q10,-5 20,0" fill="none" {S}/>'
        else: o += f'<path d="M{x-10},-12 q10,-3 20,0" fill="none" {S}/>'
    return o
def mouth(expr, dx=0):
    m = {'neutral': f'M{-10+dx},30 q10,6 20,0', 'tired': f'M{-9+dx},33 L{9+dx},32', 'procrastinating': f'M{-8+dx},31 q12,5 18,-3',
         'focused': f'M{-8+dx},32 L{8+dx},32', 'proud': f'M{-16+dx},26 q16,18 32,0'}
    if expr == 'surprised': return f'<ellipse cx="{dx}" cy="33" rx="7" ry="9" fill="{PAPER}" {S}/>'
    return f'<path d="{m[expr]}" fill="none" {S}/>'
def head(view='front', expr='neutral'):
    dx = FACE_DX[view]
    o = f'<circle cx="0" cy="0" r="62" fill="{PAPER}" {S}/>'
    if view == 'front': o += f'<path d="M-62,4 q-12,6 -2,20" fill="{PAPER}" {S}/><path d="M62,4 q12,6 2,20" fill="{PAPER}" {S}/>'
    elif view == 'q34': o += f'<path d="M-58,6 q-12,6 -2,20" fill="{PAPER}" {S}/>'
    else: o += f'<path d="M-10,0 q-14,4 -4,22 q8,2 10,-6" fill="{PAPER}" {S}/><path d="M60,8 l10,10 -8,4" fill="none" {S}/>'
    o += f'<path d="{HAIR[view]}" fill="{INK}"/>'
    if view == 'side':
        o += eyes(expr, 34, 'side') + brows(expr, 32, 'side') + mouth(expr, 30)
    else:
        o += eyes(expr, dx, view) + brows(expr, dx, view) + mouth(expr, dx)
        if expr == 'tired': o += f'<path d="M48,-30 q6,10 0,14 q-6,-4 0,-14Z" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>'
    return o
def body(view='front', arms='down'):
    w = {'front': 92, 'q34': 80, 'side': 46}[view]
    o = f'<path d="M-14,58 L-14,74 M14,58 L14,74" {S}/>'
    o += f'<path d="M{-w},300 L{-w},150 C{-w},100 {-w+34},84 0,82 C{w-34},84 {w},100 {w},150 L{w},300 Z" fill="{PAPER}" {S}/>'
    if view != 'side': o += f'<path d="M-22,84 q22,20 44,0" fill="none" {S}/>'  # crew neck
    if arms == 'down' and view != 'side':
        o += f'<path d="M{-w+30},128 L{-w+32},292 M{w-30},128 L{w-32},292" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
    if view == 'side':
        o += f'<path d="M6,128 L10,292" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
    return o
def hiep(view='front', expr='neutral', arms='down'):
    return f'<g filter="url(#hand)">{body(view, arms)}<g>{head(view, expr)}</g></g>'
# ---------- Omi ----------
def omi_svg(form='companion', mood='idle', size=96):
    s = (ROOT/f'brand/omi-exports/svg/{form}/{mood}.svg').read_text()
    s = s.split('?>')[-1]
    s = re.sub(r'<svg [^>]*viewBox="0 0 48 48"[^>]*>', f'<svg viewBox="0 0 48 48" width="{size}" height="{size}" overflow="visible">', s, count=1)
    return s
def omi(x, y, size=110, mood='idle', form='companion', float_=True):
    """Floating companion: no body/legs, soft shadow + 2 motion ticks."""
    o = f'<g transform="translate({x-size/2},{y-size/2})">{omi_svg(form, mood, size)}</g>'
    if float_:
        o = f'<ellipse cx="{x}" cy="{y+size*0.78}" rx="{size*0.28}" ry="{size*0.06}" fill="{INK}" opacity=".12"/>' + o
        o += f'<path d="M{x-size*0.62},{y+size*0.2} l-14,0 M{x-size*0.6},{y+size*0.34} l-9,0" stroke="{MUTED}" stroke-width="3" stroke-linecap="round"/>'
    return o
# ---------- props ----------
def laptop(x, y, w=220, open_=True):
    return (f'<g filter="url(#hand)"><path d="M{x},{y} l{w*0.12},{-w*0.62} l{w*0.76},0 l{w*0.12},{w*0.62} Z" fill="{PAPER}" {S}/>'
            f'<path d="M{x-20},{y} L{x+w+20},{y}" {S}/><circle cx="{x+w/2}" cy="{y-w*0.32}" r="7" fill="none" stroke="{INK}" stroke-width="3"/></g>')
def phone(x, y, a=0, glow=True):
    g = ''.join(f'<path d="M{x+20},{y-10} l{dx},{dy}" stroke="{MUTED}" stroke-width="3" stroke-linecap="round"/>' for dx, dy in [(-30,-34),(0,-44),(30,-34)]) if glow else ''
    return f'<g transform="rotate({a} {x+20} {y+36})">{g}<rect x="{x}" y="{y}" width="40" height="72" rx="8" fill="{PAPER}" {S}/><path d="M{x+14},{y+8} h12" stroke="{INK}" stroke-width="3" stroke-linecap="round"/></g>'
def notebook(x, y, w=200, lines=3, text=""):
    o = f'<g filter="url(#hand)"><path d="M{x},{y} l{w},-14 l14,{w*0.5} l{-w},14 Z" fill="#FFFFFF" {S}/>'
    o += ''.join(f'<path d="M{x+20},{y+30+i*24-i*2} l{w-50},-10" stroke="{MUTED}" stroke-width="3" stroke-linecap="round"/>' for i in range(lines))
    return o + '</g>'
def pen_hand(x, y):
    return f'<g filter="url(#hand)"><circle cx="{x}" cy="{y}" r="20" fill="{PAPER}" {S}/><path d="M{x+6},{y+8} l34,-60" stroke="{INK}" stroke-width="8" stroke-linecap="round"/></g>'
def desk(x1, x2, y):
    return f'<path d="M{x1},{y} L{x2},{y}" {S} stroke-width="6"/><path d="M{x1+30},{y} l0,140 M{x2-30},{y} l0,140" {S}/>'
def bubble(x, y, w, h, tail=(0, 40), who='hiep', html_text='', font=34):
    """who='hiep': hand-drawn white oval-rect + pointed tail. who='omi': soft rounded paper card + dotted tail (thought-dots)."""
    tx, ty = tail
    if who == 'omi':
        body_ = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="28" fill="#FFFFFF" stroke="{INK}" stroke-width="3"/>'
        t = ''.join(f'<circle cx="{x+30+tx*k}" cy="{y+h*0.7+ty*k}" r="{9-k*8}" fill="#FFFFFF" stroke="{INK}" stroke-width="3"/>' for k in (0.35, 0.8))
        badge = f'<rect x="{x+22}" y="{y-16}" width="74" height="32" rx="16" fill="{INK}"/><text x="{x+59}" y="{y+7}" text-anchor="middle" font-family="BVP" font-weight="700" font-size="20" fill="{PAPER}">Omi</text>'
        return body_ + t + badge + f'<foreignObject x="{x+28}" y="{y+22}" width="{w-56}" height="{h-36}"><div xmlns="http://www.w3.org/1999/xhtml" style="font:500 {font}px/1.25 BVP;color:{INK}">{html_text}</div></foreignObject>'
    p = f'M{x+40},{y} L{x+w-40},{y} Q{x+w},{y} {x+w},{y+40} L{x+w},{y+h-40} Q{x+w},{y+h} {x+w-40},{y+h} L{x+w*0.36},{y+h} L{x+w*0.3+tx},{y+h+ty} L{x+w*0.26},{y+h} L{x+40},{y+h} Q{x},{y+h} {x},{y+h-40} L{x},{y+40} Q{x},{y} {x+40},{y}Z'
    return (f'<g filter="url(#hand)"><path d="{p}" fill="#FFFFFF" {S} stroke-width="4"/></g>'
            f'<foreignObject x="{x+26}" y="{y+18}" width="{w-52}" height="{h-30}"><div xmlns="http://www.w3.org/1999/xhtml" style="font:600 {font}px/1.2 BVP;color:{INK}">{html_text}</div></foreignObject>')
def narration(x, y, text, w=None, font=26):
    w = w or (len(text)*font*0.7+48)
    return f'<rect x="{x}" y="{y}" width="{w}" height="{font+26}" fill="{INK}"/><text x="{x+22}" y="{y+font+6}" font-family="BVP" font-weight="600" font-size="{font}" fill="{PAPER}" letter-spacing=".04em">{text}</text>'
