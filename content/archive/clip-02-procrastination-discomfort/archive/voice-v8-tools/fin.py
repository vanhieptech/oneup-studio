import json,subprocess,numpy as np,sys,os
VE="/workspace/oneup-studio/video-engine/public/voice"
pick=json.load(open(sys.argv[1]))  # {sid:[wav,role,stt]}
for sid,(f,role,stt,sim) in pick.items():
  af="silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.04,areverse,silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.04,areverse"
  if role=="N": af+=",asetrate=24000*1.12,aresample=24000,atempo=0.892857"
  out=f"{VE}/v8-{sid}.wav"
  subprocess.run(["ffmpeg","-loglevel","error","-y","-i",f,"-af",af+",afade=t=in:d=0.012","-ar","24000","-ac","1",out],check=True)
  a=np.frombuffer(subprocess.run(["ffmpeg","-loglevel","error","-i",out,"-f","s16le","-"],capture_output=True).stdout,dtype="int16").astype(float)/32768
  d=len(a)/24000; n=int(d*30)+1; fr=800
  e=[float(np.sqrt(np.mean(a[i*fr:(i+1)*fr]**2))) if a[i*fr:(i+1)*fr].size else 0 for i in range(n)]; mx=max(e) or 1
  json.dump({"duration":round(d,3),"envelope":[round(max(0.004,min(1,x/mx*1.2)),3) for x in e],"engine":"F5-TTS hynt ViVoice thai-son (pre-voiced v8, whole line, STT-picked)","role":"Thầy Hiệp" if role=="T" else "Hiệp-né","stt":stt,"stt_sim":sim},open(f"{VE}/v8-{sid}.json","w"),ensure_ascii=False)
  print(sid,round(d,2))
