import glob,re,json,subprocess,numpy as np,difflib
from faster_whisper import WhisperModel
m=WhisperModel("small",device="cpu",compute_type="int8")
ref={"b1":"thì cái bản chất của cái việc trì hoãn là gì hôm nay thầy chỉ bạn làm cho chuẩn bài luôn á",
"b2":"deadline còn một ngày lận mà gấp gì bạn tôi","b3":"thứ nhất là các bạn phải lướt liên tục ở trên giường ngón cái chạy như máy may một cách lặp đi lặp lại","b4":"clip nữa thôi clip nữa thôi"}
alias={"đét lai":"deadline","đét":"deadline","clíp":"clip","cờ líp":"clip","kíp":"clip","cờ-líp":"clip"}
def n(s):
  s=re.sub(r"[^\wÀ-ỹ ]"," ",s.lower())
  for a,b in alias.items(): s=s.replace(a,b)
  return s.split()
res={}
for f in sorted(glob.glob("/workspace/v8/b?-*.wav")):
  a=np.frombuffer(subprocess.run(["ffmpeg","-loglevel","error","-i",f,"-ac","1","-ar","16000","-f","s16le","-"],capture_output=True).stdout,dtype="int16").astype("float32")/32768
  t=" ".join(s.text for s in m.transcribe(a,language="vi",beam_size=5)[0])
  b=f.split("/")[-1][:2]; sim=difflib.SequenceMatcher(None,n(t),ref[b].split()).ratio()
  res.setdefault(b,[]).append((round(sim,3),f,t.strip())); print(b,round(sim,3),f[-10:],t,flush=True)
json.dump(res,open("/workspace/v8/stt.json","w"),ensure_ascii=False,indent=1)
