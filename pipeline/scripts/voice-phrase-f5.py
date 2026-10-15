#!/usr/bin/env python3
"""Per-phrase F5 voice with {nhấn:} emphasis (L-036, clip-02 v17). Reusable for any clip spec.
  python3 pipeline/scripts/voice-phrase-f5.py gen    <spec.json> --work DIR            # write units + F5 batches (2 seeds/phrase)
  F5_THREADS=4 /workspace/f5-venv/bin/python pipeline/tts/f5tts_gen.py DIR/batch0.json   # (and batch1.json in parallel)
  /workspace/asr-venv/bin/python pipeline/scripts/voice-phrase-f5.py pick   <spec> --work DIR [unit keys…]  # STT pick + emphasis edits
  /workspace/asr-venv/bin/python pipeline/scripts/voice-phrase-f5.py stitch <spec> --work DIR --prefix v17 --listen out.mp3
Units: phrases split at '|' in spec `phrases[].t` (< 4 syllables merged). Emphasis: stem words +1 st +2 dB tempo .95; {nhấn:} words
tempo .78 +0.8 st +1.5 dB; stem line last word −1.5 st (fall). Hiệp-né role +2 st. Writes video-engine/public/voice/<prefix>-<line>.wav/.json
with emphasis_edits=true (check-rules L-016 exception) and final/voice-stt-<prefix>.json. Re-roll a failing unit: add seeds to a batch, re-run pick <key>.
"""
import json, re, os, sys, subprocess
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
def arg(k, d=None): return sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
CMD, SPEC = sys.argv[1], os.path.abspath(sys.argv[2]); W = os.path.abspath(arg("--work", "/workspace/voice-work")); os.makedirs(W, exist_ok=True)
PREFIX = arg("--prefix", "vp"); LISTEN = arg("--listen", os.path.join(W, "listen.mp3"))
ARGS = [a for i, a in enumerate(sys.argv[3:], 3) if not a.startswith("--") and not sys.argv[i - 1].startswith("--")]

def gen():
    import json,re
    S=json.load(open(SPEC))
    units=[]
    for sc in S['parts'][0]['scenes']:
      for li,l in enumerate(sc['lines']):
        key=sc['id']+('ab'[li] if len(sc['lines'])>1 else '')
        ph=[p['t'] for p in l['phrases']]; m=[]
        for p in ph:  # merge <4 syllables into next
          if m and len(re.sub(r"\{[^:]*: |\}","",m[-1]).split())<4: m[-1]=m[-1]+' '+p
          else: m.append(p)
        if len(m)>1 and len(re.sub(r"\{[^:]*: |\}","",m[-1]).split())<3: x=m.pop(); m[-1]=m[-1]+' '+x
        for i,p in enumerate(m):
          emph=re.findall(r"\{nhấn: ([^}]*)\}",p)+[w for w in ("Thứ nhất","Thứ hai","cuối cùng") if w in p]; t=re.sub(r"\{nhấn: ([^}]*)\}",r"\1",p)
          units.append({"key":f"{key}-{i}","line":key,"role":l['voice_role'],"t":t,"emph":emph,"last":i==len(m)-1,"stem":bool(re.match(r"(thì cái|thứ nhất|thứ hai|và cuối cùng)",l['text'].lower().replace('*','')))})
    json.dump(units,open(W+'/units.json','w'),ensure_ascii=False,indent=0)
    ref=REPO+"/assets/voice-refs/thai-son.wav";rt="Hôm nay trời Sài Gòn mát mẻ, mình ngồi cà phê một chút rồi về nhà làm việc tiếp nha."
    for h in (0,1):
      it=[{"t":u["t"],"seed":sd,"speed":0.9 if u["role"]=="Thầy" else 0.95,"out":f"{W}/{u['key']}-{sd}.wav"} for n,u in enumerate(units) if n%2==h for sd in (11,37)]
      json.dump({"ref":ref,"ref_text":rt,"items":it},open(f"{W}/batch{h}.json","w"),ensure_ascii=False)
    print(len(units)); [print(u['key'],u['t'],u['emph']) for u in units]

def helpers():
    global m, pcm, stt, sim, n
    import json,re,subprocess,difflib,unicodedata,os,glob,numpy as np
    from faster_whisper import WhisperModel
    m=WhisperModel("small",device="cpu",compute_type="int8")
    U=json.load(open(W+'/units.json')); OUT=REPO+"/video-engine/public/voice"; SR=48000; FPS=30
    AL=[("tik tok","tíc tóc"),("tiktok","tíc tóc"),("tích tóc","tíc tóc"),("tiết tóc","tíc tóc"),("thứ 2","thứ hai"),("laptop","láp tóp"),("clip","clíp"),("file","phai"),("comment","com men"),("steel","xtiu"),("691","sáu trăm chín mươi mốt"),("9 giờ","chín giờ"),("1 dòng","một dòng"),("3 thứ","ba thứ")]
    LEAK=set("hôm nay trời sài gòn mát mẻ mình ngồi cà phê một chút rồi về nhà làm việc tiếp nha".split())
    def n(s):
      s=unicodedata.normalize("NFC",s.lower()); s=re.sub(r"[^\w ]"," ",s); s=" ".join(s.split())
      for a,b in AL: s=s.replace(a,b)
      return s.split()
    def tl(ws): return ["".join(c for c in unicodedata.normalize("NFD",w) if unicodedata.category(c)!="Mn").replace("đ","d") for w in ws]
    def sim(h,t): return round(0.5*difflib.SequenceMatcher(None,h,t).ratio()+0.5*difflib.SequenceMatcher(None,tl(h),tl(t)).ratio(),3)
    def pcm(f,sr=16000): return np.frombuffer(subprocess.run(["ffmpeg","-loglevel","error","-i",f,"-ac","1","-ar",str(sr),"-f","f32le","-"],capture_output=True).stdout,dtype="float32")
    def stt(a):
      best=None
      for pad in (8000,0):
        segs,_=m.transcribe(np.pad(a,pad),language="vi",beam_size=5,condition_on_previous_text=False,word_timestamps=True)
        ws=[(w.word.strip(),w.start-pad/16000,w.end-pad/16000) for s in segs for w in s.words]
        if best is None or len(ws)>len(best): best=ws
      return best
    def rb(x,tempo=1.0,semi=0.0,db=0.0):
      if len(x)<SR*0.05: return x
      af=f"rubberband=tempo={tempo}:pitch={2**(semi/12)}"+(f",volume={db}dB" if db else "")
      p=subprocess.run(["ffmpeg","-loglevel","error","-f","f32le","-ar",str(SR),"-ac","1","-i","-","-af",af,"-f","f32le","-"],input=x.astype("float32").tobytes(),capture_output=True).stdout
      return np.frombuffer(p,dtype="float32")
    def trim(x,thr=0.01):
      i=np.where(np.abs(x)>thr)[0]; return x[max(0,i[0]-int(.03*SR)):i[-1]+int(.06*SR)] if len(i) else x
    return dict(globals(), **locals())

if CMD == "gen": gen()
else:
    G = helpers(); globals().update(G)
    if CMD == "pick":
        res={}
        ONLY=ARGS
        if ONLY: res=json.load(open(W+'/units-stt.json'))
        for u in U:
          if ONLY and u['key'] not in ONLY: continue
          tgt=n(u["t"]); best=None
          for f in sorted(glob.glob(f"{W}/{u['key']}-[0-9]*.wav")):
            ws=stt(pcm(f)); i=0; cut=0
            while i<len(ws) and n(ws[i][0]) and n(ws[i][0])[0] in LEAK and (not tgt or n(ws[i][0])[0]!=tgt[0]) and ws[i][2]<1.5: cut=ws[i][2]+0.03; i+=1
            sc=sim(n(" ".join(w[0] for w in ws[i:])),tgt)
            if best is None or sc>best[0]: best=(sc,f,cut,ws[i:])
          sc,f,cut,ws=best; x=pcm(f,SR); x=x[int(cut*SR):]
          # emphasis: find emph words in timestamps
          marks=[]
          for e in u["emph"]:
            en=n(e); hw=[n(w[0]) for w in ws]
            for j in range(len(ws)):
              if [a for h in hw[j:j+len(en)] for a in h][:len(en)]==en or tl([a for h in hw[j:j+len(en)] for a in h][:len(en)])==tl(en):
                k=min(j+len(en),len(ws))-1; marks.append((ws[j][1]-cut,ws[k][2]-cut,e in ("Thứ nhất","Thứ hai","cuối cùng","bản chất"))); break
            else:  # fallback: same word index in the target (STT spelled it differently)
              tw=n(u["t"]); hwf=[a for h in hw for a in h]
              for j in range(len(tw)):
                if tw[j:j+len(en)]==en and len(hwf)==len(tw) and len(ws)==len(tw):
                  marks.append((ws[j][1]-cut,ws[j+len(en)-1][2]-cut,e in ("Thứ nhất","Thứ hai","cuối cùng","bản chất"))); break
          out=[]; pos=0
          for s0,e0,stem in sorted(marks):
            a,b=int(max(0,s0)*SR),int(max(0,e0)*SR)
            if a<pos: continue
            out.append(x[pos:a]); out.append(rb(x[a:b],tempo=0.95 if stem else 0.78,semi=1.0 if stem else 0.8,db=2.0 if stem else 1.5)); pos=b
          tail=x[pos:]
          if u["last"] and u["stem"] and len(ws)>0:  # sentence-end fall on the last word
            lw=int(max(0,ws[-1][1]-cut)*SR)-pos
            if 0<lw<len(tail): out.append(tail[:lw]); tail=rb(tail[lw:],tempo=0.92,semi=-1.5)
          out.append(tail); y=trim(np.concatenate(out))
          if u["role"]=="Hiệp-né": y=rb(y,semi=2.0)
          np.save(f"{W}/{u['key']}.npy",y)
          res[u["key"]]={"sim":sc,"take":os.path.basename(f),"stt":" ".join(w[0] for w in ws),"emph_found":len(marks),"emph_want":len(u["emph"])}
          print(u["key"],sc,os.path.basename(f),len(marks),"/",len(u["emph"])," ".join(w[0] for w in ws),flush=True)
        json.dump(res,open(W+"/units-stt.json","w"),ensure_ascii=False,indent=1)
    elif CMD == "stitch":
        U=json.load(open(W+'/units.json')); SR=48000
        def gap(t,stemfirst):
          t=t.strip()
          if stemfirst: return 0.25
          return 0.38 if t.endswith(('...','…')) else 0.34 if t[-1:] in '?!' else 0.32 if t[-1:]=='.' else 0.26 if t[-1:]==':' else 0.18
        def env(x):
          hop=SR/FPS; e=[float(np.sqrt(np.mean(x[int(i*hop):int((i+1)*hop)]**2))) if len(x[int(i*hop):int((i+1)*hop)]) else 0 for i in range(int(len(x)/hop)+1)]
          pk=sorted(e)[int(len(e)*0.95)]; return [round(min(1,v/max(pk,1e-4)),3) for v in e]
        lines={}; order=[]
        for u in U:
          if u["line"] not in lines: lines[u["line"]]=[]; order.append(u["line"])
          lines[u["line"]].append(u)
        stt_u=json.load(open(W+'/units-stt.json')); rep={}; full=[]; prev_scene=None
        for ln in order:
          segs=[np.zeros(int(.06*SR),'float32')]
          for i,u in enumerate(lines[ln]):
            segs.append(np.load(f"{W}/{u['key']}.npy").astype('float32'))
            if i<len(lines[ln])-1: segs.append(np.zeros(int(gap(u["t"],u["stem"] and i==0)*SR),'float32'))
          segs.append(np.zeros(int(.1*SR),'float32')); y=np.concatenate(segs); y=y/max(1e-4,np.abs(y).max())*0.89
          dst=f"{OUT}/{PREFIX}-{ln}"
          subprocess.run(["ffmpeg","-y","-loglevel","error","-f","f32le","-ar",str(SR),"-ac","1","-i","-",dst+".wav"],input=y.tobytes(),check=True)
          say=" ".join(u["t"] for u in lines[ln]); ws=stt(pcm(dst+".wav")); hyp=" ".join(w[0] for w in ws); sc=sim(n(hyp),n(say))
          rep[ln]={"line_sim":sc,"units":{u["key"]:stt_u[u["key"]]["sim"] for u in lines[ln]},"stt":hyp,"dur":round(len(y)/SR,2)}
          json.dump({"duration":round(len(y)/SR,3),"envelope":env(y),"engine":"F5-TTS hynt ViVoice thai-son, per-phrase F5 (L-036, voice-phrase-f5.py), {nhấn:} rubberband stretch/pitch, stem end fall"+(", +2 semi" if lines[ln][0]["role"]=="Hiệp-né" else ""),
            "role":lines[ln][0]["role"],"stt":hyp,"stt_sim":sc,"intra_output_cuts":0,"emphasis_edits":True,"units":[{"text":u["t"],"take":stt_u[u["key"]]["take"],"sim":stt_u[u["key"]]["sim"]} for u in lines[ln]]},open(dst+".json","w"),ensure_ascii=False)
          scene=ln.rstrip('ab') if ln not in ('b01b',) else ln
          if full: full.append(np.zeros(int((0.12 if ln in ('b01b','b02') else 0.3 if scene==prev_scene else 0.42)*SR),'float32'))
          full.append(y); prev_scene=scene; print(ln,sc,rep[ln]["dur"],hyp,flush=True)
        z=np.concatenate(full)
        subprocess.run(["ffmpeg","-y","-loglevel","error","-f","f32le","-ar",str(SR),"-ac","1","-i","-","-af","loudnorm=I=-16:TP=-1.5","-c:a","libmp3lame","-b:a","160k",LISTEN],input=z.tobytes(),check=True)
        json.dump(rep,open(os.path.join(os.path.dirname(SPEC),f'voice-stt-{PREFIX}.json'),'w'),ensure_ascii=False,indent=1)
        print("total",round(len(z)/SR,2))
