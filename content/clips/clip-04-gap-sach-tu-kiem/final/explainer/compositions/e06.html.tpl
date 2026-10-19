<!doctype html>
<html><head><meta charset="UTF-8" /></head>
<body>
<template>
<style>
@font-face{font-family:"BVP";src:url(fonts/BeVietnamPro-Bold.ttf);font-weight:700}@font-face{font-family:"BVP";src:url(fonts/BeVietnamPro-SemiBold.ttf);font-weight:600}@font-face{font-family:"BVP";src:url(fonts/BeVietnamPro-Regular.ttf);font-weight:400}
#e06-root{position:absolute;inset:0;font-family:"BVP";color:#111}
#e06-root .sched{position:absolute;left:70px;top:180px;width:200px;height:260px;background:#F7F7F5;border:7px solid #111;border-radius:16px;transform:rotate(6deg);padding:26px 20px}
#e06-root .sched i{display:block;height:10px;background:#111;opacity:.55;border-radius:6px;margin-bottom:22px}
#e06-root .pile{position:absolute;bottom:560px;width:300px}
#e06-root .pile i{display:block;height:54px;background:#F7F7F5;border:7px solid #111;border-radius:14px;margin-top:-10px;box-shadow:8px 8px 0 #111}
#e06-root .barwrap{position:absolute;bottom:300px;width:300px;height:230px;border-bottom:10px solid #111}
#e06-root .bar{position:absolute;bottom:0;width:190px;left:55px;background:#F7F7F5;border:8px solid #111;border-bottom:none;border-radius:18px 18px 0 0}
#e06-root .bar.acc{background:#FF5A36}
</style>
<div id="e06-root" data-composition-id="e06" data-width="1080" data-height="1920">
  <div class="sched"><i></i><i></i><i></i></div>
  <div class="pile" id="p1" style="left:110px"><i></i><i></i><i></i><i></i></div>
  <div class="pile" id="p2" style="left:620px"><i></i><i></i><i></i><i></i></div>
  <div class="barwrap" style="left:110px"><div class="bar" id="bar1" style="height:130px"></div></div>
  <div class="barwrap" style="left:620px"><div class="bar acc" id="bar2" style="height:190px"></div></div>
</div>
<script>
(function(){const T=__TIMING__,S0=__START_e06__;const sec=T.sections.find(s=>s.id==="e06");const w=sec.lines.flatMap(l=>l.words);const at=i=>Math.max(.05,w[Math.min(i,w.length-1)].start-S0);const tl=gsap.timeline({paused:true});
tl.fromTo("#e06-root .sched",{opacity:0},{opacity:1,duration:.3},0.05);
[["#p1",0],["#p2",10]].forEach(([c,i])=>tl.fromTo(c+" i",{opacity:0,y:-60},{opacity:1,y:0,duration:.35,stagger:.09,ease:"back.out(1.6)"},at(i)));
tl.fromTo("#bar1",{scaleY:0,transformOrigin:"bottom"},{scaleY:1,duration:.5,ease:"power3.out"},at(14));
tl.fromTo("#bar2",{scaleY:0,transformOrigin:"bottom"},{scaleY:1,duration:.5,ease:"power3.out"},at(15));
window.__timelines["e06"]=tl;})();
</script>
</template>
</body></html>
