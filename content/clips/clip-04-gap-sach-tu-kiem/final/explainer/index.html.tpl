<!doctype html>
<html lang="en" data-resolution="portrait">
<head>
<meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1920" />
<!-- clip-04 v14 explainer host (b06 Yang, b07 Dunlosky). GENERATED from *.tpl by build-final.py: edit .tpl/spec, not .html. No readable text in sections: meaning by piles/bars/stacks only; numbers only in voice+captions. -->
<script src="node_modules/gsap/dist/gsap.min.js"></script>
<style>
@font-face{font-family:"BVP";src:url(fonts/BeVietnamPro-Bold.ttf);font-weight:700}@font-face{font-family:"BVP";src:url(fonts/BeVietnamPro-SemiBold.ttf);font-weight:600}@font-face{font-family:"BVP";src:url(fonts/BeVietnamPro-Regular.ttf);font-weight:400}
*{margin:0;padding:0;box-sizing:border-box}
html,body{background:#F7F7F5}
#main{position:relative;width:100%;height:100%;overflow:hidden;background:#F7F7F5;font-family:"BVP"}
#paper{position:absolute;inset:0;background-image:radial-gradient(#1111110f 1.3px,transparent 1.3px);background-size:24px 24px}
#logo{position:absolute;left:64px;top:64px;width:72px;height:72px}
</style>
</head>
<body>
<div id="main" data-composition-id="main" data-start="0" data-duration="__DUR__" data-width="1080" data-height="1920">
  <div id="paper"></div>
  <img id="logo" src="logo.svg" alt="" />
  <div id="e06" data-composition-id="e06" data-composition-src="compositions/e06.html" data-start="__START_e06__" data-duration="__DUR_e06__" data-track-index="1" data-width="1080" data-height="1920"></div>
  <div id="e07" data-composition-id="e07" data-composition-src="compositions/e07.html" data-start="__START_e07__" data-duration="__DUR_e07__" data-track-index="2" data-width="1080" data-height="1920"></div>
  <div id="captions" data-track-kind="captions" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="__DUR__" data-track-index="9" data-width="1080" data-height="1920"></div>
</div>
<script>
const tl = gsap.timeline({ paused: true });
tl.fromTo("#logo", { opacity: 0, scale: 0.8 }, { opacity: 1, scale: 1, duration: 0.4, ease: "back.out(2)" }, 0.1);
window.__timelines["main"] = tl;
</script>
</body>
</html>
