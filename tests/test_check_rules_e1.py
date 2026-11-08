import importlib.util, json, os, sys, subprocess
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); FX=os.path.join(R,"tests/fixtures/e1"); spec_=importlib.util.spec_from_file_location("cr", R+"/pipeline/scripts/check-rules.py"); cr=importlib.util.module_from_spec(spec_); sys.argv=["x"]; spec_.loader.exec_module(cr)
fails=0
def T(name, cond):
    global fails; print(("PASS " if cond else "FAIL ")+name); fails+= (not cond)
# cluster matching
T("cluster split 'kiểm tra | lại nhớ'", cr.cluster_hit("nhóm tự kiểm tra", "lại nhớ hơn", "kiểm tra lại nhớ"))
T("cluster 1-word ctx 'ngay | thì'", cr.cluster_hit("ngay", "thì", "ngay thì"))
T("pause AFTER 'thì' not a hit", not cr.cluster_hit("kiểm tra ngay thì", "nhớ được", "ngay thì"))
T("unrelated words not a hit", not cr.cluster_hit("sáng dậy", "mình gấp", "cần là sáng"))
T("punctuation/case ignored", cr.cluster_hit("Mình cần là,", "Sáng hôm sau", "cần là sáng"))
T("empty ctx never hits", not cr.cluster_hit("ngay", "", "ngay thì"))
# delivery plan parse (real clip-04 v18 file)
cl, src = cr.delivery_clusters(R+"/content/clips/clip-04-gap-sach-tu-kiem/final", "clip-04")
T(f"parsed clusters from {src}: {cl}", cl == ["ngay thì","nhỏ thì","kiểm tra lại nhớ","cần là sáng","gấp sách lại thì"] and src == "script-v18-delivery.md")
cl2, src2 = cr.delivery_clusters(FX+"/clip-04-test/final", "clip-04-test"); T(f"default clip-04 list when no plan ({src2})", cl2 == cr.E1_DEFAULT_CLUSTERS["clip-04"])
# synthetic measure with silences
S = lambda cid, d, m, b, a: {"chunk_id": cid, "t_start": 1.0, "t_end": 1.0+d, "dur_s": d, "at_mark": m, "context_before": b, "context_after": a}
j = {"voice_prefix": "c04v18t", "sentences": [{"id":"s01","beat":"b01"},{"id":"s02","beat":"b01"},{"id":"s03","beat":"b02"}],
     "pauses": [{"sid":"s01","after":"qua","mark":"/","pause":0.08},{"sid":"s01","after":"sạch","mark":"//","pause":0.18},{"sid":"s02","after":"gì","mark":"//beat","pause":0.40}],
     "silences": [S("c07",0.13,"none","nếu kiểm tra ngay","thì nhớ"),     # cluster → ✖
                  S("c09",0.11,"none","mình cần là","sáng hôm sau"),      # cluster but <0.12 → nothing
                  S("c03",0.13,"none","ba mươi từ","tiếng anh"),          # no mark ≥0.12 → ⚠
                  S("c05",0.26,"none","viết lại","airport"),              # no mark ≥0.25 → ✖
                  S("c05",0.30,"comma","airport","hotel"),                # at comma → ignored by E1
                  S("c08",0.12,"none","kiểm tra","lại nhớ hơn")]}         # cluster exactly 0.12 → ✖
cr.res.clear(); cr.check_e1(j, FX+"/clip-04-test/final", "clip-04-test", "synthetic.json")
r = {(a,b) for a,b,_ in cr.res}; txt = "\n".join(f"{a} {b} {c}" for a,b,c in cr.res); print(txt)
blk = [c for a,b,c in cr.res if a=="✖"][0]
T("E1 ✖ present", ("✖","E1") in r); T("3 blocking (ngay thì 0.13, 0.26 no-mark, kiểm tra lại nhớ 0.12)", "3 blocking" in blk and "ngay thì" in blk and "kiểm tra lại nhớ" in blk and "0.26s" in blk)
T("0.11 cluster not blocked, comma 0.30 not blocked", "«cần là sáng»" not in blk.split("blocking:")[1] and "hotel" not in blk)
T("E1 ⚠ for 0.13 no-mark", any(a=="⚠" and "1 silence" in c and "tiếng anh" in c for a,b,c in cr.res))
T("no derived-coverage warning when silences present", not any("no `silences`" in c for _,_,c in cr.res))
# soft mode
cr.res.clear(); cr.check_e1(j, FX+"/clip-04-test/final", "clip-04-test", "s.json", soft=True); T("soft → no ✖", not any(a=="✖" for a,_,_ in cr.res))
# L-027 voice-only
cr.res.clear(); cr.check_l027_voice(j, None, "synthetic.json"); print(cr.res)
T("L-027 ✖ on s01→s02 0.18, s01 comma 0.08 ok, hook→body 0.40 not counted", cr.res[0][0]=="✖" and "s01→s02" in cr.res[0][2] and "2 join(s)" in cr.res[0][2] and "0.40" not in cr.res[0][2])
j2 = dict(j, pauses=[{"sid":"s01","after":"qua","mark":"/","pause":0.05},{"sid":"s01","after":"sạch","mark":"//","pause":0.09},{"sid":"s02","after":"gì","mark":"//beat","pause":0.40}])
cr.res.clear(); cr.check_l027_voice(j2, None, "s.json"); T("L-027 ✔ when hook joins ≤0.1", cr.res[0][0]=="✔")
# derived mode on the real v16c measure
v16 = json.load(open(R+"/content/clips/clip-04-gap-sach-tu-kiem/final/prosody-measure-v16c.json"))
sil, mode = cr.measure_silences(v16); T(f"v16c derived: {len(sil)} silences, mode {mode}", mode=="derived" and len(sil)==36)
jd = {"sentences":[{"id":"s09","beat":"b05","mid_breaks":["«nhỏ thì» 0.27s"]}], "pauses": []}
sil, _ = cr.measure_silences(jd); T("mid_breaks string parsed", sil[0]["context_before"]=="nhỏ" and sil[0]["context_after"]=="thì" and sil[0]["dur_s"]==0.27)
print("FAILS:", fails); sys.exit(1 if fails else 0)
