<!doctype html>
<html><head><meta charset="UTF-8" /></head>
<body>
<template>
<style>
@font-face{font-family:"BVP";src:url(fonts/BeVietnamPro-Bold.ttf);font-weight:700}@font-face{font-family:"BVP";src:url(fonts/BeVietnamPro-SemiBold.ttf);font-weight:600}@font-face{font-family:"BVP";src:url(fonts/BeVietnamPro-Regular.ttf);font-weight:400}
#e07-root{position:absolute;inset:0;font-family:"BVP";color:#111}
/* v14b: same desk scene; 10 blank cards in a row in front of the book/sheet, stacks stand on the desk edge (y=1320) right side */
#e07-root .card{position:absolute;width:58px;height:84px;background:#F7F7F5;border:5px solid #111;border-radius:10px;box-shadow:5px 5px 0 #111}
#e07-root .stack{position:absolute;bottom:600px}
#e07-root .stack i{display:block;width:170px;height:44px;background:#F7F7F5;border:6px solid #111;border-radius:10px;margin-top:-10px;box-shadow:6px 6px 0 #111}
#e07-root .stack.acc i{background:#FF5A36}
</style>
<div id="e07-root" data-composition-id="e07" data-width="1080" data-height="1920">
  <div id="row"></div>
  <div class="stack acc" id="high" style="left:590px"><i></i><i></i><i></i><i></i><i></i></div>
  <div class="stack" id="low" style="left:820px"><i></i><i></i></div>
</div>
<script>
(function(){const T=__TIMING__,S0=__START_e07__;const sec=T.sections.find(s=>s.id==="e07");const w=sec.lines.flatMap(l=>l.words);const at=i=>Math.max(.05,w[Math.min(i,w.length-1)].start-S0);const tl=gsap.timeline({paused:true});
const row=document.getElementById("row");for(let i=0;i<10;i++){const c=document.createElement("div");c.className="card";c.id="cd"+i;c.style.left=(150+i*76)+"px";c.style.top="1352px";row.appendChild(c);}
for(let i=0;i<10;i++)tl.fromTo("#cd"+i,{opacity:0,y:-70},{opacity:1,y:0,duration:.3,ease:"back.out(1.7)"},at(2)+i*.12);
tl.fromTo("#high i",{opacity:0,y:-50},{opacity:1,y:0,duration:.3,stagger:.08,ease:"back.out(1.6)"},at(7));
tl.fromTo("#low i",{opacity:0,y:-50},{opacity:1,y:0,duration:.3,stagger:.1,ease:"back.out(1.6)"},at(14));
window.__timelines["e07"]=tl;})();
</script>
</template>
</body></html>
