import json,librosa,numpy as np,re
R="/workspace/oneup-studio/research/trends/2026-10-15/audio/"
ref=[]
for l in open(R+"transcript-medium.txt"):
  if l.startswith("   "):
    for t in l.split(): w,s=t.rsplit("@",1); ref.append([w,float(s)])
ref=[[w,s,(ref[i+1][1] if i+1<len(ref) else s+0.5)] for i,(w,s) in enumerate(ref)]
def ana(path,words,lo,hi):
  y,sr=librosa.load(path,sr=16000); f0,_,_=librosa.pyin(y,fmin=70,fmax=400,sr=sr,frame_length=1024,hop_length=160)
  rms=librosa.feature.rms(y=y,frame_length=640,hop_length=160)[0]; ws=[w for w in words if lo<=w[1]<hi]
  med=np.nanmedian(f0); er=np.median([rms[int(w[1]*100):int(w[2]*100)+1].mean() for w in ws])
  ds=np.median([w[2]-w[1] for w in ws]); r=[]
  for i,(w,s,e) in enumerate(ws):
    seg=f0[int(s*100):int(e*100)+1]; st=12*np.log2(np.nanmax(seg)/med) if np.any(~np.isnan(seg)) else float('nan')
    en=20*np.log10(rms[int(s*100):int(e*100)+1].mean()/er); gap=(ws[i+1][1]-e) if i+1<len(ws) else 0
    flag=("STRESS " if (st>2 or en>3) else "")+("STRETCH " if (e-s)>1.6*ds else "")
    r.append(f"{w}({e-s:.2f}s,{st:+.1f}st,{en:+.1f}dB){'|'+flag.strip() if flag else ''}")
  return " ".join(r)
A=R+"ban-chat-dao-dong-dieu-hoa.mp3"
for name,lo,hi in [("hook",0,5.1),("thu-nhat",8.54,16.92),("thu-hai",20.64,25.4),("cuoi-cung",27.46,32.18)]: print("REF",name,ana(A,ref,lo,hi),"\n")
W=json.load(open("words.json"))
for f,ws in W.items(): print("OURS",f[-12:],ana(f,ws,-1,99),"\n")
