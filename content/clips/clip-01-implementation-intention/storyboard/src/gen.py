import random, math, html
F="../../../../../brand/fonts/"
INK="#111111"; PAPER="#F7F7F5"; MUTED="#6B6B6B"; BORDER="#E3E3E0"; GREEN="#1A7F4B"
LOGO=open('logo.svg').read().split('\n',1)[1]
LOGO='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none" width="72" height="72" style="color:#111">'+LOGO.split('<style>svg{color:#111111}</style>')[1]
R=random.Random(7)
def rl(x1,y1,x2,y2,w=4,c=INK,j=2.2,passes=2):
    out=""
    for p in range(passes):
        mx=(x1+x2)/2+R.uniform(-j,j)*1.5; my=(y1+y2)/2+R.uniform(-j,j)*1.5
        out+=f'<path d="M{x1+R.uniform(-j,j):.1f} {y1+R.uniform(-j,j):.1f} Q{mx:.1f} {my:.1f} {x2+R.uniform(-j,j):.1f} {y2+R.uniform(-j,j):.1f}" stroke="{c}" stroke-width="{w if p==0 else w*0.6}" fill="none" stroke-linecap="round" opacity="{1 if p==0 else .55}"/>'
    return out
def rrect(x,y,W,H,**k): return rl(x,y,x+W,y,**k)+rl(x+W,y,x+W,y+H,**k)+rl(x+W,y+H,x,y+H,**k)+rl(x,y+H,x,y,**k)
def rcirc(cx,cy,r,w=4,c=INK,passes=2):
    o=""
    for p in range(passes):
        pts=[];n=28;st=R.uniform(0,6.28)
        for i in range(n+3):
            a=st+i/n*2*math.pi; rr=r*(1+R.uniform(-.03,.03))
            pts.append(f"{cx+rr*math.cos(a):.1f} {cy+rr*math.sin(a):.1f}")
        o+=f'<path d="M{" L".join(pts)}" stroke="{c}" stroke-width="{w if p==0 else w*.6}" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="{1 if p==0 else .5}"/>'
    return o
def arrow(x1,y1,x2,y2,w=5,c=INK):
    a=math.atan2(y2-y1,x2-x1);L=26
    return rl(x1,y1,x2,y2,w,c)+rl(x2,y2,x2-L*math.cos(a-.45),y2-L*math.sin(a-.45),w,c,passes=1)+rl(x2,y2,x2-L*math.cos(a+.45),y2-L*math.sin(a+.45),w,c,passes=1)
def tick(x,y,s=1,c=INK,w=7): return rl(x,y,x+18*s,y+20*s,w,c,1.2)+rl(x+18*s,y+20*s,x+52*s,y-26*s,w,c,1.2)
def underline(x,y,w,c=INK): return rl(x,y,x+w,y+R.uniform(-4,4),5,c,1.5)
SIL={
'face': lambda: rcirc(450,560,120,5,"#9A9A97")+rl(250,900,330,760,5,"#9A9A97")+rl(330,760,570,760,5,"#9A9A97")+rl(570,760,650,900,5,"#9A9A97"),
'notebook': lambda: rrect(260,430,380,470,w=5,c="#9A9A97")+rl(450,430,450,900,4,"#9A9A97")+"".join(rl(480,510+i*60,600,510+i*60,3,"#B5B5B2",passes=1) for i in range(5)),
'hand': lambda: rrect(220,470,440,380,w=5,c="#9A9A97")+rl(330,640,560,620,4,"#B5B5B2")+rl(560,620,690,470,7,"#9A9A97")+rcirc(700,455,26,5,"#9A9A97",1),
'clock': lambda: rcirc(450,640,180,6,"#9A9A97")+rl(450,640,450,520,7,"#9A9A97")+rl(450,640,530,640,7,"#9A9A97")+"".join(rl(450+165*math.cos(a),640+165*math.sin(a),450+145*math.cos(a),640+145*math.sin(a),4,"#9A9A97",passes=1) for a in [i*math.pi/6 for i in range(12)]),
'laptop': lambda: rrect(270,480,360,240,w=5,c="#9A9A97")+rl(200,760,700,760,6,"#9A9A97")+rl(270,720,200,760,5,"#9A9A97")+rl(630,720,700,760,5,"#9A9A97"),
'strike': lambda: rrect(260,430,380,470,w=5,c="#9A9A97")+rl(300,560,600,560,3,"#B5B5B2",passes=1)+rl(300,640,600,640,3,"#B5B5B2",passes=1)+rl(290,642,610,630,6,"#9A9A97"),
}
def live(shot,label,sil,y=280,h=820,extra=""):
    # placeholder frame for live footage
    return f'''<div class="live" style="top:{y}px;height:{h}px"><svg class="sil" viewBox="0 0 900 {h}" width="900" height="{h}"><g transform="translate(90,50) scale(0.8)">{SIL[sil]()}</g>{extra}</svg>
<div class="tag"><b>{shot}</b> · {html.escape(label)}<span>live shot · placeholder</span></div></div>'''
B=[
 dict(n=1,t="0–3s",part="Hook",shot=("S1","face to camera, handheld","face"),
  vi='Bạn viết "mai mình làm" cả tuần rồi… mà vẫn chưa bắt đầu.',cap=['You\'ve','written','"I\'ll','do','it','tomorrow"','all','week…'],hl=5,
  big='<div class="big" style="top:1150px">“Tomorrow.”</div>',svg=lambda: rl(70,1220,560,1206,9,INK,2.5)),
 dict(n=2,t="3–9s",part="Problem",shot=("S2","hands open notebook","notebook"),
  vi='Không phải bạn lười. Câu "mình sẽ làm" không nói lúc nào, ở đâu.',cap=['"I\'ll','do','it"','has','no','when,','no','where.'],hl=5,
  big='<div class="mid" style="top:1150px">no when <span class="dot">·</span> no where</div>',svg=lambda: '<text x="640" y="560" font-size="130" font-family="BVP" font-weight="700" fill="#111" transform="rotate(-8 640 560)">?</text><text x="760" y="700" font-size="100" font-family="BVP" font-weight="700" fill="#111" transform="rotate(10 760 700)">?</text>'),
 dict(n=3,t="9–16s",part="Explain · formula",shot=None,
  vi='Đổi đúng một câu. Viết theo kiểu: nếu… thì…',cap=['Write','it','as:','if…','then…'],hl=3,
  big='<div class="kicker" style="top:390px">Change one sentence</div><div class="boxlbl" style="top:700px;left:120px">IF</div><div class="boxlbl" style="top:700px;left:600px">THEN</div><div class="small" style="top:960px;left:120px;width:300px">time · place · cue</div><div class="small" style="top:960px;left:600px;width:300px">one action</div>',
  svg=lambda: rrect(90,620,330,300,w=6)+rrect(570,620,330,300,w=6)+arrow(430,770,555,770)),
 dict(n=4,t="16–23s",part="Explain · example",shot=("S3","hand writing the line","hand"),
  vi='Ví dụ: "Thứ Ba, tám giờ sáng, ngồi vào bàn, thì viết phần mở đầu trước."',cap=['Tuesday,','8','a.m.,','I','sit','at','my','desk'],hl=0,
  big='<div class="note" style="top:1140px"><b>IF</b> Tue 8am, at my desk<br><b>THEN</b> write the intro</div>',svg=lambda: arrow(108,1180,108,1280,4)),
 dict(n=5,t="23–30s",part="Explain · why",shot=("S4 → S5","clock 8:00 → sit, open laptop","clock"),
  vi='Tình huống đó trở thành cái công tắc. Đến giờ, ngồi vào bàn, là việc tự bắt đầu.',cap=['The','situation','becomes','a','trigger.'],hl=4,
  big='<div class="mid" style="top:1150px">cue <span class="arr">→</span> action</div>',svg=lambda: ''),
 dict(n=6,t="30–38s",part="Proof",shot=None,
  vi='Một nghiên cứu gộp 94 kiểm nghiệm độc lập… hiệu ứng mức trung bình đến lớn.',cap=['A','meta-analysis','of','94','independent','tests'],hl=3,
  big='<div class="kicker" style="top:390px">Implementation intention</div><div class="huge" style="top:460px">94</div><div class="mid" style="top:760px;font-size:64px">independent tests</div><div class="small" style="top:930px;left:90px">effect size <b style="color:#111">d = 0.65</b></div><div class="scale" style="top:1060px"><span>small</span><span>medium</span><span>large</span></div><div class="src" style="top:1130px">Gollwitzer &amp; Sheeran, 2006 · meta-analysis</div>',
  svg=lambda: f'<rect x="90" y="990" width="810" height="40" rx="20" fill="#ECECE9"/><rect x="90" y="990" width="{810*0.65/1.0:.0f}" height="40" rx="20" fill="#111"/>'+rl(90+810*.5,975,90+810*.5,1045,3,MUTED,1)+rl(90+810*.8,975,90+810*.8,1045,3,MUTED,1)),
 dict(n=7,t="38–45s",part="Proof · 3 uses",shot=None,
  vi='Nó giúp ở ba chỗ: bắt đầu làm, giữ được khi bị cắt ngang, và dừng đúng lúc.',cap=['and','quitting','what','can\'t','work.'],hl=1,
  big='<div class="kicker" style="top:390px">It helps in three places</div><div class="li" style="top:500px"><i>1</i>start</div><div class="li" style="top:700px"><i>2</i>hold on</div><div class="li" style="top:900px"><i>3</i>let go</div>',
  svg=lambda: rrect(90,505,90,90,w=5)+tick(105,550,1)+rrect(90,705,90,90,w=5)+tick(105,750,1)+rrect(90,905,90,90,w=5,c=GREEN)+tick(105,950,1,GREEN)),
 dict(n=8,t="45–51s",part="Caveat",shot=("S6","hand strikes a 'should' line","strike"),
  vi='Nhưng nó chỉ hiệu quả với việc bạn thật sự muốn làm.',cap=['But','it','only','works','for','goals','you','actually','want.'],hl=7,
  big='<div class="mid" style="top:1150px;font-size:76px">only for goals <u>you want</u></div>',svg=lambda: ''),
 dict(n=9,t="51–56s",part="Action",shot=("S7","face to camera, holds up notebook","face"),
  vi='Tối nay, chọn một việc thật. Viết một câu "nếu… thì…". Mất một, hai phút.',cap=['Tonight,','pick','one','real','task.'],hl=0,
  big='<div class="big" style="top:1150px;font-size:104px">Tonight: 1 line</div>',svg=lambda: underline(66,1252,330)),
 dict(n=10,t="56–60s",part="CTA + loop",shot=("S7","face → back to hook frame","face"),
  vi='Viết câu của bạn xuống comment. Vì "mai mình làm"… không phải là một kế hoạch.',cap=['"I\'ll','do','it','tomorrow"…','is','not','a','plan.'],hl=7,
  big='<div class="big" style="top:1112px;font-size:88px;line-height:1.05">“Tomorrow.”<br>is not a plan.</div>',svg=lambda: rl(66,1160,480,1148,8,INK,2.5)),
]
CSS=f'''@font-face{{font-family:BVP;src:url({F}BeVietnamPro-Regular.ttf);font-weight:400}}
@font-face{{font-family:BVP;src:url({F}BeVietnamPro-Medium.ttf);font-weight:500}}
@font-face{{font-family:BVP;src:url({F}BeVietnamPro-SemiBold.ttf);font-weight:600}}
@font-face{{font-family:BVP;src:url({F}BeVietnamPro-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;background:{PAPER};font-family:BVP;color:{INK};position:relative;overflow:hidden}}
body:after{{content:"";position:absolute;inset:0;pointer-events:none;opacity:.07;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/></filter><rect width='200' height='200' filter='url(%23n)'/></svg>")}}
.abs,.big,.mid,.kicker,.huge,.small,.note,.li,.boxlbl,.src,.scale{{position:absolute}}
.top{{position:absolute;top:150px;left:60px;display:flex;align-items:center;gap:16px;font-weight:700;font-size:34px;letter-spacing:-.02em}}
.top span{{color:#B5B5B2}}
.meta{{position:absolute;top:168px;right:140px;font-size:24px;font-weight:500;color:{MUTED};letter-spacing:.06em;text-transform:uppercase}}
.live{{position:absolute;left:60px;width:900px;border-radius:36px;background:#ECECE9;overflow:hidden}}
.live .sil{{position:absolute;left:0;top:0}}
.live .tag{{white-space:nowrap;position:absolute;left:32px;bottom:30px;background:{PAPER};border-radius:999px;padding:14px 26px;font-size:28px;font-weight:500;display:flex;gap:14px;align-items:baseline}}
.live .tag span{{color:{MUTED};font-size:22px;font-weight:400}}
.big{{left:60px;width:880px;font-size:120px;font-weight:700;letter-spacing:-.035em;line-height:1}}
.mid{{left:60px;width:880px;font-size:84px;font-weight:700;letter-spacing:-.03em;line-height:1.05}}
.mid .dot,.mid .arr{{color:#B5B5B2}}
.mid u{{text-decoration:none;background:linear-gradient(transparent 70%,#E4E4E0 70%)}}
.kicker{{left:60px;font-size:40px;font-weight:600;color:{MUTED};letter-spacing:-.01em}}
.huge{{left:50px;font-size:340px;font-weight:700;letter-spacing:-.06em;line-height:1}}
.small{{font-size:34px;color:{MUTED};font-weight:500}}
.src{{left:90px;font-size:24px;color:{MUTED}}}
.scale{{left:90px;width:810px;display:flex;justify-content:space-between;font-size:24px;color:{MUTED}}}
.boxlbl{{font-size:96px;font-weight:700;letter-spacing:-.03em}}
.note{{left:60px;width:880px;font-size:60px;font-weight:500;line-height:1.25;letter-spacing:-.02em;padding-left:80px}}
.li{{left:220px;font-size:96px;font-weight:700;letter-spacing:-.03em;line-height:100px}}
.li i{{font-style:normal;display:none}}
.cap{{position:absolute;left:60px;width:880px;top:1320px;background:#fff;border:2px solid {BORDER};border-radius:28px;padding:30px 36px;font-size:46px;font-weight:500;line-height:1.3;color:#9A9A97;letter-spacing:-.01em}}
.cap b{{color:{INK};font-weight:700;border-bottom:5px solid {INK}}}
.cap em{{font-style:normal;color:{INK}}}
.safe{{position:absolute;left:0;right:0;top:1520px;bottom:0;border-top:2px dashed #DCDCD8}}
.safe span{{position:absolute;left:60px;top:18px;font-size:22px;color:#B5B5B2;letter-spacing:.06em;text-transform:uppercase}}
.rside{{position:absolute;right:0;top:900px;width:120px;height:600px;border-left:2px dashed #DCDCD8}}
svg.over{{position:absolute;left:0;top:0}}'''
for b in B:
    caps=" ".join((f"<b>{html.escape(w)}</b>" if i==b['hl'] else (f"<em>{html.escape(w)}</em>" if i<b['hl'] else html.escape(w))) for i,w in enumerate(b['cap']))
    lv=live(*b['shot']) if b['shot'] else ""
    doc=f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="top">{LOGO}<div>OneUp<span>.</span></div></div>
<div class="meta">{b['n']:02d} · {b['t']} · {b['part']}</div>
{lv}{b['big']}
<svg class="over" width="1080" height="1920">{b['svg']()}</svg>
<div class="cap">{caps}</div>
<div class="rside"></div><div class="safe"><span>TikTok UI zone · keep clear</span></div>
</body></html>'''
    open(f'beat-{b["n"]:02d}.html','w').write(doc)
import json; json.dump([dict(n=b['n'],t=b['t'],part=b['part'],vi=b['vi']) for b in B],open('beats.json','w'),ensure_ascii=False)
