#!/usr/bin/env python3
"""STT khớp chữ bằng đúng hàm stt()/norm()/sim() của pipeline (pipeline/scripts/voice-delivery-f5.py, faster-whisper small int8 CPU). Ngưỡng >= 0.8.
Chạy (sau khi F5 xong): /workspace/asr-venv/bin/python stt_score.py <wav>...   (id câu lấy từ tiền tố tên file c07/c08/c14)"""
import importlib.util, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, "../../.."))
spec = importlib.util.spec_from_file_location("vdf5", os.path.join(REPO, "pipeline/scripts/voice-delivery-f5.py")); M = importlib.util.module_from_spec(spec)
sys.argv = [sys.argv[0]] + sys.argv[1:]; files = sys.argv[1:]; sys.argv = sys.argv[:1]; spec.loader.exec_module(M)
T = {L["id"]: L["text"] for L in json.load(open(os.path.join(HERE, "lines.json")))["lines"]}; res = []
for f in files:
    cid = os.path.basename(f)[:3]; tgt = M.norm(T[cid]); ws = M.stt(M.pcm(f), target=tgt); hyp = [t for w, _, _ in ws for t in M.norm(w)]
    # lặng giữa từ (không ở dấu câu) >= 0.25s
    gaps = [(ws[i][0], ws[i + 1][0], round(ws[i + 1][1] - ws[i][2], 2)) for i in range(len(ws) - 1) if ws[i + 1][1] - ws[i][2] >= 0.25 and not ws[i][0].endswith((",", "."))]
    r = {"file": f, "id": cid, "stt": " ".join(w for w, _, _ in ws), "sim": M.sim(hyp, tgt), "pass": M.sim(hyp, tgt) >= 0.8, "gaps_ge_0.25s_no_punct": gaps}
    res.append(r); print(json.dumps(r, ensure_ascii=False))
json.dump(res, open(os.path.join(HERE, "stt-results.json"), "w"), ensure_ascii=False, indent=1)
