import subprocess,os,json
from PIL import Image,ImageDraw,ImageFont
FD="/usr/share/fonts/truetype/sand-box/google/Be Vietnam Pro/"
INK,PAPER=(17,17,17),(247,247,245)
SLUG={"Đức Trí":"ductri","Adam":"adam","Thái Sơn":"thaison","Minh Triết":"minhtriet","Kim Thanh":"kimthanh","Thục Đoan":"thucdoan","Mỹ Duyên":"myduyen","Thùy Dung":"thuydung"}
G={"male":(["Đức Trí","Adam","Thái Sơn","Minh Triết"],"Thôi… mai học. Mai học thiệt á!\nNếu chín giờ tối, thì mình mở sách năm phút. Dễ hông?","Hiệp (nam)"),
   "female":(["Kim Thanh","Thục Đoan","Mỹ Duyên","Thùy Dung"],"Ủa? Lại mai học nữa hả? Ba lần rồi á nha!\nNè, thử vầy nè: nếu… thì… nghe giống code ghê á.","Omi (nữ)")}
def f(w,s): return ImageFont.truetype(FD+f"BeVietnamPro-{w}.ttf",s)
def wrap(d,t,font,W):
    out=[]
    for para in t.split("\n"):
        line=""
        for w in para.split():
            if d.textlength(line+" "+w,font=font)>W and line: out.append(line); line=w
            else: line=(line+" "+w).strip()
        out.append(line)
    return out
def card(path,num,eng,voice,role,text):
    im=Image.new("RGB",(1080,1920),PAPER); d=ImageDraw.Draw(im)
    d.text((96,300),f"{role} · voice audition",font=f("Regular",40),fill=(110,110,108))
    d.text((96,420),f"{num:02d}",font=f("Bold",220),fill=INK)
    d.text((96,720),eng,font=f("Bold",84),fill=INK)
    d.text((96,830),f"{'tham chiếu ' if eng=='F5-TTS' else 'preset '}{voice}",font=f("Regular",60),fill=INK)
    d.line((96,980,984,980),fill=INK,width=3); y=1030
    for l in wrap(d,"“"+text.replace("\n"," ")+"”",f("Light",52),888): d.text((96,y),l,font=f("Light",52),fill=INK); y+=78
    if eng=="F5-TTS": d.text((96,1740),"CC-BY-NC-SA · chỉ để nghe thử",font=f("Regular",34),fill=(110,110,108))
    im.save(path)
def sh(*a): subprocess.run(a,check=True,capture_output=True)
for g,(voices,text,role) in G.items():
    segs=[];n=0
    for v in voices:
        for eng,src in [("VieNeu-TTS",f"work/vn-{v}.wav"),("F5-TTS",f"work/f5-{v}.wav")]:
            n+=1; tag="vieneu" if eng[0]=="V" else "f5"; name=f"{g}-{n:02d}-{tag}-{SLUG[v]}"
            sh("ffmpeg","-y","-i",src,"-af","loudnorm=I=-16:TP=-1.5,apad=pad_dur=0.8","-ar","48000","-ac","1","-b:a","192k",f"{name}.mp3")
            card(f"work/{name}.png",n,eng,v,role,text)
            sh("ffmpeg","-y","-loop","1","-framerate","30","-i",f"work/{name}.png","-i",f"{name}.mp3","-shortest","-c:v","libx264","-pix_fmt","yuv420p","-c:a","aac","-ar","48000","-ac","2","-b:a","192k",f"work/{name}.mp4")
            segs.append(f"work/{name}.mp4")
    open(f"work/{g}.txt","w").write("".join(f"file '{os.path.basename(s)}'\n" for s in segs))
    sh("ffmpeg","-y","-f","concat","-safe","0","-i",f"work/{g}.txt","-c","copy",f"audition-{g}.mp4")
print("done")
