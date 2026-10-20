import json,re,unicodedata,difflib,subprocess,numpy as np,librosa
SR=16000; HOP=160  # 10ms
V="/workspace/oneup-studio/video-engine/public/voice/"
T=json.load(open("/workspace/oneup-studio/content/clips/clip-04-gap-sach-tu-kiem/final/timing.json"))['lines']
SM={d['key']:d['words'] for d in json.load(open("asr-stems-small.json"))}
MED={d['key']:d for d in json.load(open("/workspace/c04v14-rr/asr-lines-medium.json"))}
EMPH={"b01a":["quên sạch"],"b01b":["Không nhìn sách"],"b02b":["thuộc làu"],"b03c":["Bút dừng"],"b04a":["quen mắt"],"b04b":["Giấy trắng"],
"b05a":["mở sách"],"b05b":["lắc ghịt"],"b06a":["hai trăm hai mươi hai nghiên cứu"],"b07b":["nhóm cao nhất"],"b08a":["ba chồng"],"b09b":["Viết trước"],"b09c":["lắc ghịt"],"b10a":["Lắc ghịt"]}
NUM={"222":"hai trăm hai mươi hai","22":"hai mươi hai","48":"bốn mươi tám","10":"mười","30":"ba mươi","5":"năm","3":"ba",".000":"ngàn","000":"ngàn"}
def deacc(s): return "".join(c for c in unicodedata.normalize("NFD",s.lower()) if unicodedata.category(c)!="Mn").replace("đ","d")
def toks(text):
  out=[]
  for w in text.split():
    m=re.match(r"^(.*?)([,.?!:…]*)$",w); out.append((m.group(1),m.group(2)))
  return out
def asr_syl(words):
  syl=[]
  for s,e,w,p in words:
    w=w.strip(); core=re.sub(r"[^\w.]","",w)
    exp=NUM.get(core.strip(".") if core not in NUM else core, None)
    parts=(exp.split() if exp else [x for x in re.sub(r"[^\w]"," ",w).split()])
    if not parts: continue
    d=(e-s)/len(parts)
    for i,x in enumerate(parts): syl.append((s+i*d,s+(i+1)*d,x))
  return syl
def load(f):
  return np.frombuffer(subprocess.run(["ffmpeg","-v","error","-i",f,"-ac","1","-ar",str(SR),"-f","f32le","-"],capture_output=True).stdout,dtype=np.float32)
rows=[]; allres=[]
for L in T:
  k=L['key'][7:]; say=L['say']; a=load(V+L['key']+".wav")
  rms=librosa.feature.rms(y=a,frame_length=400,hop_length=HOP,center=True)[0]; db=20*np.log10(rms+1e-6)
  pk=np.percentile(db,95); sil=db<pk-30
  vo=np.where(~sil)[0]; s0=vo[0]*0.01; s1=vo[-1]*0.01
  f0,vf,_=librosa.pyin(a,fmin=70,fmax=350,sr=SR,frame_length=1024,hop_length=HOP)
  tg=toks(say); tsyl=[t for t,_ in tg]
  words=SM[L['key']]; src="small"
  if k=="b01a": words=words[:len(words)//2]
  if k in("b07c","b07d"):
    m=MED[L['key']]; words=[(w[0]-L['t'],w[1]-L['t'],w[2],w[3]) for w in m['words']]; src="medium(final)"
  syl=asr_syl(words)
  A=[deacc(x[2]) for x in syl]; B=[deacc(x) for x in tsyl]
  sm=difflib.SequenceMatcher(None,A,B,autojunk=False); tm=[None]*len(B)
  for op,i1,i2,j1,j2 in sm.get_opcodes():
    if op in("equal","replace") and (i2-i1)==(j2-j1):
      for d in range(i2-i1): tm[j1+d]=(syl[i1+d][0],syl[i1+d][1],op=="equal")
    elif op=="replace":
      s=syl[i1][0]; e=syl[i2-1][1]; n=j2-j1
      for d in range(n): tm[j1+d]=(s+(e-s)*d/n,s+(e-s)*(d+1)/n,False)
  matched=sum(1 for x in tm if x and x[2])
  # interpolate missing
  for j in range(len(B)):
    if tm[j] is None:
      pj=max([i for i in range(j) if tm[i]],default=None); nj=min([i for i in range(j+1,len(B)) if tm[i]],default=None)
      s=tm[pj][1] if pj is not None else s0; e=tm[nj][0] if nj is not None else s1
      cnt=(nj if nj is not None else len(B))-(pj if pj is not None else -1)-1; pos=j-(pj if pj is not None else -1)-1
      tm[j]=(s+(e-s)*pos/cnt,s+(e-s)*(pos+1)/cnt,False)
  tm[0]=(max(tm[0][0],s0),max(tm[0][1],s0+0.05),tm[0][2]); tm[-1]=(tm[-1][0],min(tm[-1][1],s1+0.01),tm[-1][2])
  # silence runs
  runs=[];i=0
  while i<len(sil):
    if sil[i]:
      j=i
      while j<len(sil) and sil[j]: j+=1
      if i*0.01>s0+0.02 and j*0.01<s1-0.02: runs.append((i*0.01,j*0.01))
      i=j
    else: i+=1
  # boundaries
  bnd=[]
  for j in range(len(B)-1):
    c1=(tm[j][0]+tm[j][1])/2; c2=(tm[j+1][0]+tm[j+1][1])/2
    best=0
    for r in runs:
      ov=min(r[1],c2)-max(r[0],c1)
      if ov>0: best=max(best,ov)
    bnd.append({"j":j,"after":tsyl[j],"punct":tg[j][1],"pause":round(best,2),"t":round(tm[j][1],2)})
  assigned=[]
  for r in runs:
    if r[1]-r[0]<0.25: continue
    mid=(r[0]+r[1])/2; jb=min(range(len(bnd)),key=lambda q:abs(((tm[q][0]+tm[q][1])/2+(tm[q+1][0]+tm[q+1][1])/2)/2-mid)) if bnd else None
    assigned.append((round(r[0],2),round(r[1]-r[0],2),jb))
  # syllable features
  feat=[]
  for j in range(len(B)):
    a1,b1=int(tm[j][0]*100),max(int(tm[j][0]*100)+1,int(tm[j][1]*100))
    seg=db[a1:b1]; segv=seg[seg>pk-30]
    ff=f0[a1:b1]; ff=ff[~np.isnan(ff)] if len(ff) else ff
    feat.append({"syl":tsyl[j],"vdur":round(len(segv)*0.01,2),"dur":round(tm[j][1]-tm[j][0],3),"db":round(float(np.mean(segv)) if len(segv) else float('nan'),1),
      "f0":round(float(np.median(ff)),1) if len(ff) else None,"f0_tail":round(float(np.median(ff[len(ff)//2:])),1) if len(ff)>=4 else None,
      "f0_head":round(float(np.median(ff[:max(1,len(ff)//2)])),1) if len(ff)>=4 else None})
  allf0=f0[~np.isnan(f0)]
  res={"key":k,"t":L['t'],"dur":L['dur'],"say":say,"src":src,"asr":" ".join(w[2] for w in words),"matched":matched,"n":len(B),
       "speech":[round(s0,2),round(s1,2)],"runs":[(round(r[0],2),round(r[1]-r[0],2)) for r in runs],"bnd":bnd,"long_runs":assigned,"feat":feat,
       "f0_med":round(float(np.median(allf0)),1) if len(allf0) else None,"syl_rate":round(len(B)/(s1-s0),2)}
  allres.append(res)
json.dump(allres,open("analysis.json","w"),ensure_ascii=False,indent=1)
for r in allres:
  print(f"{r['key']} t={r['t']:.2f} match {r['matched']}/{r['n']} rate {r['syl_rate']} syl/s src={r['src']} | {r['say']}")
  print("   runs:",r['runs'])
  print("   bnd:"," ".join(f"{b['after']}{b['punct']}[{b['pause']}]" for b in r['bnd']))
