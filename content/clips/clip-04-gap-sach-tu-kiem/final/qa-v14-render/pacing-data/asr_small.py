import json,subprocess,numpy as np
from faster_whisper import WhisperModel
m=WhisperModel("small",device="cpu",compute_type="int8",cpu_threads=8)
d=json.load(open("/workspace/oneup-studio/content/clips/clip-04-gap-sach-tu-kiem/final/timing.json"))
out=[]
for l in d['lines']:
    f=f"/workspace/oneup-studio/video-engine/public/voice/{l['key']}.wav"
    a=np.frombuffer(subprocess.run(["ffmpeg","-v","error","-i",f,"-ac","1","-ar","16000","-f","f32le","-"],capture_output=True).stdout,dtype=np.float32)
    best=None
    for pad in (8000,0,16000):
      for model_try in (0,):
        segs,_=m.transcribe(np.pad(a,pad),language="vi",beam_size=5,condition_on_previous_text=False,word_timestamps=True)
        ws=[(round(w.start-pad/16000,3),round(w.end-pad/16000,3),w.word.strip(),round(w.probability,2)) for s in segs for w in s.words]
        if best is None or len(ws)>len(best): best=ws
    out.append({"key":l['key'],"say":l['say'],"words":best}); print(l['key'],'|',l['say'],'||',' '.join(w[2] for w in best),flush=True)
json.dump(out,open("asr-stems-small.json","w"),ensure_ascii=False,indent=1)
