import sys
F="file:///workspace/hi-oneup/brand/fonts/"
T={"dark":dict(bg="#111111",ink="#F7F7F5",muted="#A3A3A0",surface="28,28,26",line="#2E2E2C",glow="255,255,250",glowA=".10",plateA=".78"),
   "light":dict(bg="#F7F7F5",ink="#111111",muted="#6B6B6B",surface="255,255,255",line="#E8E8E6",glow="0,0,0",glowA=".045",plateA=".86")}
LOGO='<svg viewBox="0 0 100 100" fill="none"><path d="M73 19A38 38 0 1 0 84 31" stroke="currentColor" stroke-width="4" stroke-linecap="round"/><circle cx="30" cy="52" r="5" fill="currentColor"/><circle cx="70" cy="52" r="5" fill="currentColor"/><g stroke="currentColor" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M35 52h30"/><path d="M50 30v44"/><path d="M38 41l12-11"/></g></svg>'
words=["then","I","write","one","line."]; cur=2
def cap():
    out=[]
    for i,w in enumerate(words):
        c="past" if i<cur else ("cur" if i==cur else "next")
        out.append(f'<span class="w {c}">{w}</span>')
    return " ".join(out)
for name,t in T.items():
    html=f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:OU;src:url('{F}BeVietnamPro-Regular.ttf');font-weight:400}}
@font-face{{font-family:OU;src:url('{F}BeVietnamPro-Medium.ttf');font-weight:500}}
@font-face{{font-family:OU;src:url('{F}BeVietnamPro-SemiBold.ttf');font-weight:600}}
@font-face{{font-family:OU;src:url('{F}BeVietnamPro-Bold.ttf');font-weight:700}}
*{{margin:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;overflow:hidden;position:relative;background:{t['bg']};color:{t['ink']};font-family:OU;-webkit-font-smoothing:antialiased}}
.bg{{position:absolute;inset:0;background:
 radial-gradient(900px 700px at 78% 30%, rgba({t['glow']},{t['glowA']}), transparent 70%),
 radial-gradient(1200px 900px at 10% 95%, rgba({t['glow']},{float(t['glowA'])*0.6}), transparent 70%)}}
.scene i{{position:absolute;filter:blur(60px)}}
.grain{{position:absolute;inset:0;opacity:.07;mix-blend-mode:overlay}}
.head{{position:absolute;left:72px;top:236px;display:flex;align-items:center;gap:18px}}
.head svg{{width:60px;height:60px;color:{t['ink']}}}
.wm{{font-weight:700;font-size:44px;letter-spacing:-.03em}} .wm span{{opacity:.35}}
.tag{{position:absolute;right:140px;top:252px;font-size:26px;font-weight:600;letter-spacing:.14em;color:{t['muted']}}}
.hero{{position:absolute;left:72px;right:140px;top:560px}}
.eyebrow{{font-size:28px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:{t['muted']};margin-bottom:28px}}
h1{{font-size:104px;font-weight:700;letter-spacing:-.035em;line-height:1.02}}
h1 em{{font-style:normal;color:{t['muted']}}}
.sub{{margin-top:36px;font-size:36px;line-height:1.45;color:{t['muted']};max-width:760px}}
.plate{{position:absolute;left:56px;right:140px;bottom:420px;padding:48px 52px 44px;border-radius:40px;
 background:rgba({t['surface']},{t['plateA']});backdrop-filter:blur(30px);border:1.5px solid {t['line']}}}
.cap{{font-size:76px;font-weight:600;line-height:1.15;letter-spacing:-.02em}}
.w.past{{color:{t['ink']}}} .w.next{{color:{t['muted']};opacity:.55}}
.w.cur{{color:{t['ink']};font-weight:700;text-decoration:underline;text-decoration-thickness:6px;text-underline-offset:14px}}
.meta{{margin-top:40px;padding-top:28px;border-top:1.5px solid {t['line']};display:flex;justify-content:space-between;font-size:26px;font-weight:500;color:{t['muted']}}}
.bar{{height:6px;border-radius:3px;background:{t['line']};margin-top:22px;overflow:hidden}} .bar i{{display:block;height:100%;width:48%;background:{t['ink']}}}
</style></head><body>
<div class="bg"></div><div class="scene">
<i style="left:560px;top:1080px;width:520px;height:340px;border-radius:24px;transform:rotate(-8deg);background:rgba({t['glow']},{float(t['glowA'])*1.1})"></i>
<i style="left:-80px;top:1260px;width:300px;height:300px;border-radius:50%;background:rgba({t['glow']},{float(t['glowA'])*0.9})"></i>
<i style="left:640px;top:180px;width:420px;height:420px;border-radius:50%;background:rgba({t['glow']},{float(t['glowA'])*1.3})"></i></div>
<svg class="grain" width="1080" height="1920"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>
<div class="head">{LOGO}<div class="wm">OneUp<span>.</span></div></div>
<div class="tag">01 / 12</div>
<div class="hero"><div class="eyebrow">If–then plans</div><h1>One sentence<br>that makes you<br><em>start.</em></h1>
<div class="sub">Decide the when and where before the moment arrives.</div></div>
<div class="plate"><div class="cap">{cap()}</div><div class="meta"><span>Your next +1</span><span>0:21</span></div></div>
</body></html>"""
    open(f"frame-{name}.html","w").write(html)
