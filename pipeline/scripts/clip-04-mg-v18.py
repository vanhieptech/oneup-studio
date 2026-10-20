#!/usr/bin/env python3
"""clip-04 v18: HyperFrames motion-graphic plates for the evidence beats (rule-42).
Writes final/mg-b03/index.html and final/mg-b06/index.html (silent, text-free plates; captions,
study credits and the «+2 ngày» tag stay in the Remotion overlay layer on top). Timings come from the
same word clock as clip-04-spec-v18-scenes.py (Scene.W), so the plates stay sample-locked to the voice.
Render: cd final/mg-b03 && npx hyperframes@0.8.150 render -o ../../../../../video-engine/public/mg/c04v18-b03.mp4
Usage: python3 pipeline/scripts/clip-04-mg-v18.py"""
import importlib.util, json, os, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "../.."))
FD = os.path.join(REPO, "content/clips/clip-04-gap-sach-tu-kiem/final")
sp = importlib.util.spec_from_file_location("sc", os.path.join(HERE, "clip-04-spec-v18-scenes.py")); sc = importlib.util.module_from_spec(sp); sp.loader.exec_module(sc)
ICON = json.load(open(os.path.join(REPO, "brand/icons/phosphor-paths.json")))  # Phosphor core 2.1.1 (MIT), fill paths
INK, PAPER, SOFT, MUTED, ACC = "#111111", "#F7F7F5", "#E4E2DD", "#8A8A86", "#FF5A36"

def W(sid, lid, word, n=1): return sc.Scene(sid, sid[:3], "evidence", [lid], "paper").W(lid, word, n)
def dur(sid, lid): return sc.Scene(sid, sid[:3], "evidence", [lid], "paper").dur
def icon(name, size, fill=INK, stroke=None, sw=0, extra=""):
    st = f' stroke="{stroke}" stroke-width="{sw * 256 / size:.1f}" stroke-linejoin="round"' if stroke else ""
    return f'<g transform="translate({-size / 2} {-size / 2}) scale({size / 256:.4f})"><path d="{ICON[name]}" fill="{fill}"{st} {extra}/></g>'

def page(cid, total, svg, js):
    return f"""<!doctype html>
<html lang="vi" data-resolution="portrait">
<head>
<meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1920" />
<script src="node_modules/gsap/dist/gsap.min.js"></script>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: {PAPER}; }}
#root {{ width: 100%; height: 100%; position: relative; background: {PAPER}; }}
#stage {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; display: block; }}
</style>
</head>
<body>
<div id="root" data-composition-id="{cid}" data-start="0" data-duration="{total:.3f}" data-width="1080" data-height="1920">
<svg id="stage" class="clip" data-start="0" data-duration="{total:.3f}" data-track-index="0" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
<defs><pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="4" cy="4" r="2.4" fill="{INK}" opacity="0.10"/></pattern></defs>
<rect x="0" y="0" width="1080" height="1920" fill="{PAPER}"/>
<rect x="0" y="0" width="520" height="420" fill="url(#dots)"/>
{svg}
</svg>
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{js}
window.__timelines["{cid}"] = tl;
tl.seek(0);
</script>
</body>
</html>
"""

def window(x, y, w, h, pre):
    """moon/sun window; ids prefixed. Day = soft sky + sun up; night = ink sky + moon + stars."""
    stars = "".join(f'<circle cx="{x + w * a:.0f}" cy="{y + h * b:.0f}" r="6" fill="{PAPER}"/>' for a, b in [(0.18, 0.2), (0.62, 0.14), (0.8, 0.42), (0.42, 0.62)])
    return f"""<g id="{pre}win">
<rect x="{x + 10}" y="{y + 12}" width="{w}" height="{h}" rx="36" fill="{INK}"/>
<clipPath id="{pre}clip"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="36"/></clipPath>
<g clip-path="url(#{pre}clip)">
<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{INK}"/>
<rect id="{pre}day" x="{x}" y="{y}" width="{w}" height="{h}" fill="{SOFT}"/>
<g id="{pre}stars" opacity="0">{stars}</g>
<g id="{pre}moon" opacity="0"><g transform="translate({x + w * 0.3:.0f} {y + h * 0.36:.0f})">{icon("moon-fill", 104, PAPER)}</g></g>
<g id="{pre}sun"><g transform="translate({x + w * 0.3:.0f} {y + h * 0.38:.0f})"><g id="{pre}sunspin">{icon("sun-fill", 128, ACC, INK, 7)}</g></g></g>
</g>
<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="36" fill="none" stroke="{INK}" stroke-width="10"/>
<path d="M{x + w / 2},{y} V{y + h} M{x},{y + h / 2} H{x + w}" stroke="{INK}" stroke-width="8"/>
<rect x="{x - 18}" y="{y + h}" width="{w + 36}" height="20" rx="10" fill="{INK}"/>
</g>"""

def sky(pre, at, to, d=0.28, h=230):
    """tween the window to day/night at time `at`"""
    if to == "day":
        return (f'tl.to("#{pre}day", {{opacity: 1, duration: {d}, ease: "power1.out"}}, {at:.3f});\n'
                f'tl.fromTo("#{pre}sun", {{y: {h * 0.75:.0f}}}, {{y: 0, duration: {d}, ease: "back.out(1.6)", immediateRender: false}}, {at:.3f});\n'
                f'tl.to(["#{pre}moon", "#{pre}stars"], {{opacity: 0, duration: {d * 0.6:.2f}}}, {at:.3f});\n')
    return (f'tl.to("#{pre}day", {{opacity: 0, duration: {d}, ease: "power1.in"}}, {at:.3f});\n'
            f'tl.to("#{pre}sun", {{y: {h * 0.75:.0f}, duration: {d}, ease: "power2.in"}}, {at:.3f});\n'
            f'tl.to(["#{pre}moon", "#{pre}stars"], {{opacity: 1, duration: {d}}}, {at + d * 0.4:.3f});\n')

def bar(id_, x, w, base, fill, stroke=True):
    return f'<rect id="{id_}" x="{x}" y="{base}" width="{w}" height="0" rx="14" fill="{fill}"' + (f' stroke="{INK}" stroke-width="8"' if stroke else "") + "/>"

def grow(id_, base, h, at, d=0.5, ease="back.out(1.4)"):
    return f'tl.to("#{id_}", {{attr: {{y: {base - h}, height: {h}}}, duration: {d}, ease: "{ease}"}}, {at:.3f});\n'

def book(cx, cy, pre):
    """open book, spine + page edges, drawn (ink on paper)"""
    l = f'<path d="M{cx},{cy - 50} C{cx - 40},{cy - 70} {cx - 90},{cy - 70} {cx - 120},{cy - 58} V{cy + 62} C{cx - 90},{cy + 50} {cx - 40},{cy + 50} {cx},{cy + 70} Z" fill="{PAPER}" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/>'
    r = l.replace(f"{cx - 40}", f"{cx + 40}").replace(f"{cx - 90}", f"{cx + 90}").replace(f"{cx - 120}", f"{cx + 120}")
    edge = f'<path d="M{cx - 128},{cy - 48} V{cy + 76} C{cx - 90},{cy + 64} {cx - 40},{cy + 64} {cx},{cy + 82} C{cx + 40},{cy + 64} {cx + 90},{cy + 64} {cx + 128},{cy + 76} V{cy - 48}" fill="none" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/>'
    lines = "".join(f'<path d="M{cx + s * 24},{cy - 26 + i * 26} q{s * 36},-10 {s * 76},-2" stroke="{MUTED}" stroke-width="6" stroke-linecap="round" fill="none"/>' for s in (-1, 1) for i in range(4))
    lines = lines.replace("q-36", "q-36")
    return f'<g id="{pre}book"><g transform="translate(8 10)" opacity="1"><path d="M{cx - 128},{cy - 48} V{cy + 82} H{cx + 128} V{cy - 48}" fill="{INK}"/></g>{edge}{l}{r}<path d="M{cx},{cy - 50} V{cy + 70}" stroke="{INK}" stroke-width="8"/>{lines}</g>'

def sheet(cx, cy, pre, w=150, h=190):
    x, y = cx - w / 2, cy - h / 2
    rows = "".join(f'<path d="M{x + 22},{y + 40 + i * 30} H{x + w - 20}" stroke="{SOFT}" stroke-width="5"/>' for i in range(5))
    ink = "".join(f'<path id="{pre}r{i}" d="M{x + 24},{y + 38 + i * 30} q30,-8 {w * 0.55:.0f},0" stroke="{INK}" stroke-width="7" stroke-linecap="round" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>' for i in range(3))
    pen = f'<g transform="translate({cx + w / 2 + 20} {cy + h / 2 - 10}) rotate(30)"><g id="{pre}pen"><rect x="-12" y="-80" width="24" height="120" rx="8" fill="{INK}"/><path d="M-12,40 L0,66 L12,40 Z" fill="{INK}"/><rect x="-12" y="-80" width="24" height="18" rx="6" fill="{ACC}"/></g></g>'
    return f'<g id="{pre}sheet"><rect x="{x + 8}" y="{y + 10}" width="{w}" height="{h}" rx="10" fill="{INK}"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{PAPER}" stroke="{INK}" stroke-width="8"/>{rows}{ink}</g>{pen}'

def badge(name, size, plate=PAPER, fill=INK, r=52):
    return f'<circle cx="5" cy="6" r="{r}" fill="{INK}"/><circle r="{r}" fill="{plate}" stroke="{INK}" stroke-width="7"/>{icon(name, size, fill)}'

def tick(r=46):
    return f'<circle cx="5" cy="6" r="{r}" fill="{INK}"/><circle r="{r}" fill="{ACC}" stroke="{INK}" stroke-width="7"/>{icon("check-bold", r * 1.2, PAPER)}'

def pop(sel, at, d=0.35):
    return f'tl.fromTo("{sel}", {{scale: 0, opacity: 0, transformOrigin: "50% 50%"}}, {{scale: 1, opacity: 1, duration: {d}, ease: "back.out(2)"}}, {at:.3f});\n'

def b03():
    a, b, c = dur("b03a", "c06"), dur("b03b", "c07"), dur("b03c", "c08")
    tB, tC = a, a + b; total = a + b + c
    kiem, tot = tB + W("b03b", "c07", "kiểm"), tB + W("b03b", "c07", "tốt")
    hai, nhom, tu, nho = tC + W("b03c", "c08", "hai"), tC + W("b03c", "c08", "nhóm"), tC + W("b03c", "c08", "tự"), tC + W("b03c", "c08", "nhớ")
    rise1 = hai                    # 1st sunrise on «hai ngày sau»
    set1 = rise1 + 0.36            # sunset
    rise2 = set1 + 0.36            # 2nd sunrise = the «+2 ngày» moment; bars swap here
    BASE, LX, RX, BW = 980, 200, 680, 200
    L1, R1, L2, R2 = 280, 200, 160, 310  # after +2 ngày: re-read keeps ~57% (study: self-test clearly better, not "forgot all")
    svg = window(390, 170, 300, 230, "w") + book(300, 540, "b") + sheet(780, 540, "s")
    svg += f'<path id="div" d="M540,470 V{BASE}" stroke="{INK}" stroke-width="6" stroke-dasharray="18 16" opacity="0.55"/>'
    svg += bar("barL", LX, BW, BASE, SOFT) + bar("barR", RX, BW, BASE, INK, stroke=False)
    svg += f'<path id="base" d="M150,{BASE} H930" stroke="{INK}" stroke-width="10" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
    svg += f'<g id="thumbP" transform="translate({LX + BW / 2} {BASE - L1})"><g id="thumb" opacity="0">{badge("thumbs-up-fill", 62)}</g></g>'
    svg += f'<g id="tickP" transform="translate({RX + BW / 2} {BASE - R2})"><g id="tick" opacity="0">{tick()}</g></g>'
    js = ""
    js += 'tl.fromTo("#div", {opacity: 0}, {opacity: 0.55, duration: 0.3}, 0.05);\n'
    js += pop("#bbook", 0.15) + pop("#ssheet", 0.45)
    js += 'tl.to("#base", {attr: {"stroke-dashoffset": 0}, duration: 0.35, ease: "power2.out"}, 0.6);\n'
    js += "".join(f'tl.to("#sr{i}", {{attr: {{"stroke-dashoffset": 0}}, duration: 0.3}}, {0.75 + i * 0.3:.2f});\n' for i in range(3))
    js += 'tl.fromTo("#spen", {x: 0, y: 0}, {x: -40, y: -60, duration: 0.3, yoyo: true, repeat: 3, ease: "sine.inOut"}, 0.75);\n'
    js += f'tl.to("#wsunspin", {{rotation: 60, transformOrigin: "50% 50%", duration: {total:.2f}, ease: "none"}}, 0);\n'
    # phase B: tested at once → reread bar a bit taller, thumbs-up on it
    js += grow("barL", BASE, L1, kiem + 0.05, 0.6) + grow("barR", BASE, R1, kiem + 0.15, 0.6)
    js += pop("#thumb", tot)
    # phase C: night, sunrise 1, sunset, sunrise 2 (+2 ngày) → swap
    js += f'tl.set("#wday", {{opacity: 0}}, {tC:.3f});\ntl.set("#wsun", {{y: 172}}, {tC:.3f});\ntl.set(["#wmoon", "#wstars"], {{opacity: 1}}, {tC:.3f});\n'
    js += sky("w", rise1, "day") + sky("w", set1, "night", 0.24) + sky("w", rise2, "day")
    js += f'tl.to("#thumb", {{rotation: 180, transformOrigin: "50% 50%", duration: 0.4, ease: "back.out(1.6)"}}, {hai:.3f});\n'
    js += f'tl.to("#thumb circle:nth-child(2)", {{attr: {{fill: "{SOFT}"}}, duration: 0.3}}, {hai:.3f});\n'
    js += grow("barL", BASE, L2, rise2 + 0.05, 0.45, "power3.inOut") + grow("barR", BASE, R2, rise2 + 0.05, 0.55, "back.out(1.5)")
    js += f'tl.to("#thumbP", {{attr: {{transform: "translate({LX + BW / 2} {BASE - L2})"}}, duration: 0.45, ease: "power3.inOut"}}, {rise2 + 0.05:.3f});\n'
    js += pop("#tick", nho - 0.1)
    return "mg-b03", total, svg, js, {"rise1": rise1, "set1": set1, "rise2": rise2, "tC": tC, "total": total}

def b06():
    a, b = dur("b06a", "c13"), dur("b06b", "c14"); tB = a; total = a + b
    ngh = W("b06a", "c13", "nghiên")
    lop, kiem, diem, cao, muc = (tB + W("b06b", "c14", w) for w in ("lớp", "kiểm", "điểm", "cao", "mức"))
    BASE, LX, RX, BW, BH0 = 980, 200, 660, 220, 150
    LH, RH = 470, 380
    offs = [(-38, 6, -9), (30, 2, 7), (-14, -4, -4), (22, -8, 11), (-30, -12, 5), (10, -16, -8), (-20, -20, 3), (34, -24, -6),
            (-6, -28, 9), (18, -32, -3), (-26, -36, 6), (6, -40, -10), (28, -44, 4), (-16, -48, -5), (12, -52, 8), (-4, -56, -2)]
    sheets = ""; js = ""
    for i, (dx, dy, r) in enumerate(offs):
        sheets += (f'<g transform="translate({540 + dx} {820 + dy})"><g id="p{i}"><g id="pr{i}" transform="rotate({r})">'
                   f'<rect x="-155" y="-195" width="310" height="390" rx="12" fill="{PAPER}" stroke="{INK}" stroke-width="7"/>'
                   + "".join(f'<path d="M-110,{-130 + k * 50} H{110 - (k % 2) * 60}" stroke="{MUTED}" stroke-width="9" stroke-linecap="round"/>' for k in range(5)) + "</g></g></g>")
        js += f'tl.fromTo("#p{i}", {{y: -900, opacity: 1}}, {{y: 0, duration: 0.32, ease: "power3.in"}}, {0.1 + i * 0.12:.2f});\n'
    js += f'tl.to([{",".join(f"{chr(34)}#pr{i}{chr(34)}" for i in range(16))}], {{rotation: 0, transformOrigin: "50% 50%", duration: 0.3, ease: "back.out(2)"}}, {ngh:.3f});\n'
    js += f'tl.to("#pile", {{scale: 0.34, x: 0, y: -490, svgOrigin: "540 820", duration: 0.45, ease: "power3.inOut"}}, {tB - 0.05:.3f});\n'
    svg = f'<g id="pile">{sheets}</g>'
    svg += f'<path id="base" d="M150,{BASE} H930" stroke="{INK}" stroke-width="10" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
    svg += bar("barL", LX, BW, BASE, INK, stroke=False) + bar("barR", RX, BW, BASE, SOFT)
    svg += f'<g id="gL" transform="translate({LX + BW / 2} {BASE - 70})" opacity="0">{icon("users-three-fill", 120, PAPER)}</g>'
    svg += f'<g id="gR" transform="translate({RX + BW / 2} {BASE - 70})" opacity="0">{icon("users-three-fill", 120, INK)}</g>'
    svg += f'<g id="qP" transform="translate({LX + BW / 2} {BASE - BH0 - 70})"><g id="q" opacity="0"><circle cx="5" cy="6" r="52" fill="{INK}"/><circle r="52" fill="{PAPER}" stroke="{INK}" stroke-width="7"/><rect x="-22" y="-30" width="44" height="58" rx="6" fill="{PAPER}" stroke="{INK}" stroke-width="6"/><path d="M-12,-14 H12 M-12,0 H12 M-12,14 H4" stroke="{INK}" stroke-width="5" stroke-linecap="round"/><g transform="translate(38 34)">{tick(26)}</g></g></g>'
    hx, hy = LX + BW + 110, BASE - LH + 40
    svg += f'<g transform="translate({hx} {hy})"><g id="hand" opacity="0"><g transform="rotate(-90)">{icon("hand-pointing-fill", 150, INK, PAPER, 4)}</g></g></g>'
    svg += f'<path id="gap" d="M{LX + BW + 6},{BASE - RH} H{RX + BW}" stroke="{INK}" stroke-width="6" stroke-dasharray="16 12" opacity="0"/>'
    svg += f'<path id="br" d="M{LX + BW + 30},{BASE - LH + 4} h18 V{BASE - RH - 4} h-18" stroke="{ACC}" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0"/>'
    js += f'tl.to("#base", {{attr: {{"stroke-dashoffset": 0}}, duration: 0.3, ease: "power2.out"}}, {tB + 0.05:.3f});\n'
    js += grow("barL", BASE, BH0, lop - 0.1, 0.4) + grow("barR", BASE, BH0, lop, 0.4)
    js += f'tl.to(["#gL", "#gR"], {{opacity: 1, duration: 0.25}}, {lop + 0.1:.3f});\n'
    js += pop("#q", kiem)
    js += grow("barL", BASE, LH, diem, 0.6) + grow("barR", BASE, RH, diem + 0.08, 0.6)
    js += f'tl.to("#qP", {{attr: {{transform: "translate({LX + BW / 2} {BASE - LH - 70})"}}, duration: 0.6, ease: "back.out(1.4)"}}, {diem:.3f});\n'
    js += f'tl.fromTo("#hand", {{opacity: 0, x: 60}}, {{opacity: 1, x: 0, duration: 0.3, ease: "power2.out"}}, {cao + 0.1:.3f});\n'
    js += f'tl.to("#hand", {{x: -14, duration: 0.35, yoyo: true, repeat: {int((total - cao - 0.5) / 0.35)}, ease: "sine.inOut"}}, {cao + 0.45:.3f});\n'
    js += f'tl.to(["#gap", "#br"], {{opacity: 1, duration: 0.25}}, {muc:.3f});\n'
    js += f'tl.fromTo("#br", {{scaleY: 0, svgOrigin: "{LX + BW + 39} {BASE - (LH + RH) / 2}"}}, {{scaleY: 1, duration: 0.35, ease: "back.out(2)"}}, {muc:.3f});\n'
    return "mg-b06", total, svg, js, {"hand_tip": [hx - 65, hy], "barL_top": BASE - LH, "total": total}

def main():
    meta = {}
    for f in (b03, b06):
        cid, total, svg, js, m = f()
        d = os.path.join(FD, cid); os.makedirs(d, exist_ok=True)
        for fn in ("package.json", "hyperframes.json"): shutil.copy(os.path.join(FD, "explainer", fn), os.path.join(d, fn))
        json.dump({"id": cid, "name": cid, "createdAt": "2026-10-21T02:40:00.000Z"}, open(os.path.join(d, "meta.json"), "w"))
        if not os.path.exists(os.path.join(d, "node_modules")): shutil.copytree(os.path.join(FD, "explainer", "node_modules"), os.path.join(d, "node_modules"))
        open(os.path.join(d, "index.html"), "w").write(page(cid, total, svg, js))
        meta[cid] = {k: (round(v, 3) if isinstance(v, float) else v) for k, v in m.items()}
        print(cid, f"{total:.3f}s →", os.path.relpath(os.path.join(d, "index.html"), REPO))
    json.dump(meta, open(os.path.join(FD, "mg-v18.json"), "w"), indent=1)
    print(json.dumps(meta))
main()
