import sys,subprocess,numpy as np,json
from faster_whisper import WhisperModel
m=WhisperModel('small',device='cpu',compute_type='int8')
r={}
for f in sys.argv[1:]:
    a=np.frombuffer(subprocess.run(["ffmpeg","-loglevel","error","-i",f,"-ac","1","-ar","16000","-f","s16le","-"],capture_output=True).stdout,dtype="int16").astype("float32")/32768
    s,_=m.transcribe(a,language='vi'); r[f]=' '.join(x.text.strip() for x in s); print(f,'|',r[f],flush=True)
json.dump(r,open('stt.json','a'),ensure_ascii=False)
