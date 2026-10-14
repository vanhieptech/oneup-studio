import json,textwrap,sys
from PIL import Image,ImageDraw,ImageFont
s=json.load(open('spec.json'))
B='/workspace/oneup-studio/brand/fonts/BeVietnamPro-'
f=lambda w,z:ImageFont.truetype(B+w+'.ttf',z)
fix=lambda t:t.replace('→',' > ').replace('✕','X').replace('≠','khác')
items=[(p['engine'],x) for p in s['parts'] for x in p.get('scenes',p.get('sections',[]))]
W,H=540,760; cols=4; rows=(len(items)+cols-1)//cols
img=Image.new('RGB',(cols*W+40,rows*H+140),'#111111'); d=ImageDraw.Draw(img)
d.text((24,30),f"{s['clip']} storyboard · gate 1 (chưa render) · {s['theme'].upper()} · tuần {s['week']}",font=f('Bold',40),fill='#F7F7F5')
for k,(eng,x) in enumerate(items):
    X=20+(k%cols)*W; Y=110+(k//cols)*H
    d.rounded_rectangle([X+10,Y+10,X+W-10,Y+H-10],radius=28,fill='#1C1C1A',outline='#2E2E2C',width=3)
    d.rounded_rectangle([X+30,Y+30,X+150,Y+80],radius=14,fill='#F7F7F5'); d.text((X+46,Y+34),x['id'],font=f('Bold',34),fill='#111111')
    d.text((X+170,Y+40),eng,font=f('Medium',28),fill='#A3A3A0'); y=Y+100
    for ln in textwrap.wrap(fix(x['fx']['visual']),34)[:6]: d.text((X+30,y),ln,font=f('Regular',26),fill='#F7F7F5'); y+=36
    y+=14
    for l in x['lines']:
        for ln in textwrap.wrap('“'+fix(l['text'].replace('**',''))+'”',34)[:5]: d.text((X+30,y),ln,font=f('SemiBold',26),fill='#D9D9D6'); y+=34
    y+=10
    acc=[f"{h['sfx']} @ “{h['word']}”" for h in x.get('hits',[])]+[f"{q['name']} @ “{q['word']}”" for q in x.get('sfx',[])]
    for ln in textwrap.wrap('SFX: '+'; '.join(acc),36)[:3]: d.text((X+30,y),ln,font=f('Medium',24),fill='#D97706'); y+=32
img.save('storyboard-contact-sheet.png')
