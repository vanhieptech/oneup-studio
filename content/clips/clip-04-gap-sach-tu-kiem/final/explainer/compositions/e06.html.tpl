<!doctype html>
<html><head><meta charset="UTF-8" /></head>
<body>
<template>
<style>
@font-face{font-family:"BVP";src:url(fonts/BeVietnamPro-Bold.ttf);font-weight:700}@font-face{font-family:"BVP";src:url(fonts/BeVietnamPro-SemiBold.ttf);font-weight:600}@font-face{font-family:"BVP";src:url(fonts/BeVietnamPro-Regular.ttf);font-weight:400}
#e06-root{position:absolute;inset:0;font-family:"BVP";color:#111}
/* v14b: objects stand on the desk edge (y=1320) of the same desk scene (desk-bg.png from Remotion), right side */
#e06-root .pile{position:absolute;bottom:600px;width:140px}
#e06-root .pile i{display:block;height:40px;background:#F7F7F5;border:6px solid #111;border-radius:10px;margin-top:-8px;box-shadow:6px 6px 0 #111}
#e06-root .barwrap{position:absolute;bottom:600px;width:60px;height:260px}
#e06-root .bar{position:absolute;bottom:0;left:0;width:60px;background:#F7F7F5;border:7px solid #111;border-bottom:none;border-radius:14px 14px 0 0;box-shadow:6px 0 0 #111}
#e06-root .bar.acc{background:#FF5A36}
</style>
<div id="e06-root" data-composition-id="e06" data-width="1080" data-height="1920">
  <div class="pile" id="p1" style="left:560px"><i></i><i></i><i></i><i></i></div>
  <div class="barwrap" style="left:712px"><div class="bar" id="bar1" style="height:160px"></div></div>
  <div class="pile" id="p2" style="left:800px"><i></i><i></i><i></i><i></i></div>
  <div class="barwrap" style="left:952px"><div class="bar acc" id="bar2" style="height:235px"></div></div>
</div>
<script>
(function(){const T=__TIMING__,S0=__START_e06__;const sec=T.sections.find(s=>s.id==="e06");const w=sec.lines.flatMap(l=>l.words);const at=i=>Math.max(.05,w[Math.min(i,w.length-1)].start-S0);const tl=gsap.timeline({paused:true});
[["#p1",0],["#p2",10]].forEach(([c,i])=>tl.fromTo(c+" i",{opacity:0,y:-60},{opacity:1,y:0,duration:.35,stagger:.09,ease:"back.out(1.6)"},at(i)));
tl.fromTo("#bar1",{scaleY:0,transformOrigin:"bottom"},{scaleY:1,duration:.5,ease:"power3.out"},at(14));
tl.fromTo("#bar2",{scaleY:0,transformOrigin:"bottom"},{scaleY:1,duration:.5,ease:"power3.out"},at(15));
window.__timelines["e06"]=tl;})();
</script>
</template>
</body></html>
