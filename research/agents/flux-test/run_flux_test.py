#!/usr/bin/env python3
"""FLUX.2 [klein] 4B - exactly ONE internal test image. Run only after BFL_API_KEY is set.
Usage: BFL_API_KEY=... python3 run_flux_test.py
Endpoint: POST https://api.bfl.ai/v1/flux-2-klein-4b  (header x-key)
Refs: input_image=Hiep sheet, input_image_2=Omi sheet (base64), max 4 refs for klein.
Poll: GET polling_url returned by POST until status Ready (signed URL valid 10 min).
"""
import base64, os, sys, time, json, urllib.request, datetime, pathlib
KEY=os.environ.get("BFL_API_KEY")
if not KEY:
    sys.exit("MISSING BFL_API_KEY - create key at dashboard.bfl.ai (project > API > Keys > Add Key), add credits, export BFL_API_KEY, rerun. No API call made.")
ROOT=pathlib.Path("/workspace/oneup-studio/brand/characters")
OUT=pathlib.Path("/workspace/flux-test"); OUT.mkdir(exist_ok=True)
prompt=(OUT/"prompt.txt").read_text().strip()
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
payload={"prompt":prompt,"input_image":b64(ROOT/"hiep-model-sheet.png"),"input_image_2":b64(ROOT/"omi-sheet.png"),"width":1080,"height":1920,"output_format":"png"}
req=urllib.request.Request("https://api.bfl.ai/v1/flux-2-klein-4b",data=json.dumps(payload).encode(),headers={"x-key":KEY,"Content-Type":"application/json","accept":"application/json"},method="POST")
t0=time.time()
with urllib.request.urlopen(req,timeout=120) as r: meta=json.loads(r.read())
print("submitted",meta.get("id"),"cost_field",meta.get("cost"))
poll=meta["polling_url"]
while True:
    time.sleep(0.5)
    q=urllib.request.Request(poll,headers={"x-key":KEY,"accept":"application/json"})
    with urllib.request.urlopen(q,timeout=60) as r: res=json.loads(r.read())
    print(res.get("status"))
    if res.get("status")=="Ready": break
    if res.get("status") in ("Error","Failed"): sys.exit(str(res))
url=res["result"]["sample"]
day=datetime.datetime.now().strftime("%Y-%m-%d")
dest=OUT/f"flux2-klein4b-test-{day}.png"
urllib.request.urlretrieve(url,dest)
print("saved",dest,"elapsed_s",round(time.time()-t0,1),"result_cost",res.get("cost"))
