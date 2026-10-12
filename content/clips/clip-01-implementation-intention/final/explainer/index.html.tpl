<!doctype html>
<html lang="en" data-resolution="portrait">
<head>
<meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1920" />
<!-- clip-01 explainer (rule-42 motion beats). GENERATED from index.html.tpl by pipeline/scripts/build-final.py: edit the template/spec, not index.html. -->
<script src="node_modules/gsap/dist/gsap.min.js"></script>
<style>
@font-face{font-family:"BVP";src:url(fonts/BeVietnamPro-Bold.ttf);font-weight:700}
@font-face{font-family:"BVP";src:url(fonts/BeVietnamPro-SemiBold.ttf);font-weight:600}
@font-face{font-family:"BVP";src:url(fonts/BeVietnamPro-Regular.ttf);font-weight:400}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#F7F7F5}
#root{position:relative;width:1080px;height:1920px;font-family:"BVP";color:#111;overflow:hidden}
#grain{position:absolute;inset:0;background-image:radial-gradient(#1111110d 1.2px,transparent 1.2px);background-size:22px 22px}
#logo{position:absolute;left:64px;top:60px;width:72px;height:72px;z-index:5}
.sec{position:absolute;inset:0}
.kicker{position:absolute;left:96px;top:250px;font-size:38px;font-weight:700;letter-spacing:3px;text-transform:uppercase;opacity:.55}
.title{position:absolute;left:92px;top:306px;font-size:112px;font-weight:700;letter-spacing:-4px;line-height:1.02}
.card{position:absolute;border:8px solid #111;border-radius:44px;background:#F7F7F5;box-shadow:12px 14px 0 #111;display:flex;align-items:center;gap:30px;padding:0 44px}
.lbl{font-size:68px;font-weight:700;letter-spacing:-2px;white-space:nowrap}
.sub{font-size:38px;font-weight:400;opacity:.65;white-space:nowrap}
.tag{font-size:56px;font-weight:700;background:#111;color:#F7F7F5;border-radius:24px;padding:4px 28px 12px}
/* e01 */
#e01 .chip{width:420px;height:300px;flex-direction:column;justify-content:center;align-items:flex-start;gap:6px}
#c1{left:96px;top:600px;transform:rotate(-1.5deg)} #c2{left:560px;top:600px;transform:rotate(1.2deg)}
#c3{left:96px;top:960px;transform:rotate(1deg)}
#c4{left:560px;top:960px;background:#111;color:#F7F7F5;transform:rotate(-1deg)}
#c4 .sub{opacity:.75}
#e01arrow{position:absolute;left:300px;top:1130px}
/* e02 */
#oldp{position:absolute;left:96px;top:600px;font-size:170px;font-weight:700;letter-spacing:-6px}
#strike{position:absolute;left:84px;top:690px}
#newc{left:96px;top:960px;width:888px;height:400px;flex-direction:column;align-items:flex-start;justify-content:center;gap:18px}
#newc .row{display:flex;align-items:center;gap:22px;font-size:58px;font-weight:700;letter-spacing:-2px}
#exnote{position:absolute;left:100px;top:1400px;font-size:34px;opacity:.55}
/* e03 */
#num{position:absolute;left:78px;top:430px;font-size:440px;font-weight:700;letter-spacing:-16px;line-height:1}
#numsub{position:absolute;left:100px;top:900px;font-size:60px;font-weight:700}
#meter{position:absolute;left:100px;top:1120px;width:880px}
#meter .track{height:34px;border:7px solid #111;border-radius:20px;position:relative;background:#F7F7F5}
#meter .fill{position:absolute;left:0;top:0;bottom:0;background:#111;border-radius:12px}
#meter .ticks{display:flex;justify-content:space-between;font-size:36px;font-weight:600;margin-top:16px}
#meter .d{position:absolute;top:-92px;font-size:40px;font-weight:700;background:#1F9D55;color:#F7F7F5;border-radius:18px;padding:2px 18px 8px;white-space:nowrap}
#cite{position:absolute;left:100px;top:1330px;font-size:32px;line-height:1.4;opacity:.6}
/* e04 */
.use{position:absolute;left:96px;display:flex;align-items:center;gap:30px}
.use .n{width:124px;height:124px;border-radius:62px;background:#111;color:#F7F7F5;font-size:64px;font-weight:700;display:flex;align-items:center;justify-content:center}
.use .w{font-size:72px;font-weight:700;letter-spacing:-2px;position:relative;white-space:nowrap}
.use svg{position:absolute;left:0;bottom:-26px}
#u1{top:580px} #u2{top:850px} #u3{top:1120px}
.ping{display:inline-block;font-size:36px;font-weight:700;background:#E4E2DD;border-radius:16px;padding:4px 14px 8px;margin-left:16px;vertical-align:middle;letter-spacing:0}
/* captions (EN, word highlight, rule-1/16) */
#cap{position:absolute;left:70px;right:70px;top:1488px;z-index:6}
.cl{position:absolute;left:0;right:0;top:0;display:flex;flex-wrap:wrap;justify-content:center;gap:6px 14px;background:#F7F7F5;border:6px solid #111;border-radius:34px;padding:22px 30px 26px;box-shadow:8px 10px 0 #111;opacity:0}
.cw{font-size:54px;font-weight:700;line-height:1.18;letter-spacing:-.5px;display:inline-block;opacity:.16;padding:2px 0 6px}
.cw.hl{background:#111;color:#F7F7F5;border-radius:18px;padding:2px 16px 6px}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="__DUR__" data-width="1080" data-height="1920">
  <div id="grain"></div>
  <img id="logo" src="logo.svg" />

  <div id="e01" class="sec clip" data-start="0" data-duration="__DUR__" data-track-index="0">
    <div class="kicker">The one-sentence plan</div>
    <div class="title">If → Then</div>
    <div id="c1" class="card chip"><svg width="74" height="74" viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="none" stroke="#111" stroke-width="9"/><path id="hand1" d="M50 50 L50 24 M50 50 L68 60" stroke="#111" stroke-width="9" stroke-linecap="round"/></svg><div class="lbl">When</div><div class="sub">9 PM</div></div>
    <div id="c2" class="card chip"><svg width="74" height="74" viewBox="0 0 100 100"><path d="M50 92 C 26 62 18 50 18 38 a32 32 0 0 1 64 0 c0 12 -8 24 -32 54z" fill="none" stroke="#111" stroke-width="9" stroke-linejoin="round"/><circle cx="50" cy="38" r="11" fill="#111"/></svg><div class="lbl">Where</div><div class="sub">at my desk</div></div>
    <div id="c3" class="card chip"><svg width="74" height="74" viewBox="0 0 100 100"><path d="M24 72 h52 l-8-12 v-18 a18 18 0 0 0 -36 0 v18 z" fill="none" stroke="#111" stroke-width="9" stroke-linejoin="round"/><path d="M42 82 a8 8 0 0 0 16 0" stroke="#111" stroke-width="9" fill="none"/></svg><div class="lbl">Cue</div><div class="sub">laptop closes</div></div>
    <div id="c4" class="card chip"><svg width="74" height="74" viewBox="0 0 100 100"><path id="chk" d="M18 54 L40 76 L84 28" fill="none" stroke="#1F9D55" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg><div class="lbl">Then…</div><div class="sub">one small action</div></div>
  </div>

  <div id="e02" class="sec clip" data-start="0" data-duration="__DUR__" data-track-index="1">
    <div class="kicker">Example</div>
    <div id="oldp">“Mai học”</div>
    <svg id="strike" width="760" height="60" viewBox="0 0 760 60"><path id="strikeP" d="M10 34 C 200 18, 480 46, 748 22" fill="none" stroke="#111" stroke-width="16" stroke-linecap="round"/></svg>
    <div id="newc" class="card">
      <div class="row"><span class="tag">IF</span> 9 PM, laptop closed</div>
      <div class="row"><span class="tag">THEN</span> 1 listening lesson</div>
    </div>
    <div id="exnote">Example line · your time & task will differ</div>
  </div>

  <div id="e03" class="sec clip" data-start="0" data-duration="__DUR__" data-track-index="2">
    <div class="kicker">Meta-analysis</div>
    <div id="num">0</div>
    <div id="numsub">independent tests</div>
    <div id="meter">
      <div class="track"><div class="fill" id="fill" style="width:100%;transform-origin:0 50%;transform:scaleX(0)"></div><div class="d" id="dval" style="left:0">d = 0.65</div></div>
      <div class="ticks"><span>small</span><span>medium</span><span>large</span></div>
      <div style="font-size:44px;font-weight:700;margin-top:14px">Medium-to-large effect</div>
    </div>
    <div id="cite">Gollwitzer &amp; Sheeran (2006)<br/>Mostly students &amp; health habits</div>
  </div>

  <div id="e04" class="sec clip" data-start="0" data-duration="__DUR__" data-track-index="3">
    <div class="kicker">It helps you</div>
    <div id="u1" class="use"><div class="n">1</div><div class="w">Start<svg width="220" height="30" viewBox="0 0 220 30" preserveAspectRatio="none"><path class="ul" d="M4 18 C 70 8, 150 26, 216 12" fill="none" stroke="#111" stroke-width="10" stroke-linecap="round"/></svg></div></div>
    <div id="u2" class="use"><div class="n">2</div><div class="w">Hold on<span class="ping">Messenger · 3</span><svg width="300" height="30" viewBox="0 0 300 30" preserveAspectRatio="none"><path class="ul" d="M4 18 C 90 8, 200 26, 296 12" fill="none" stroke="#111" stroke-width="10" stroke-linecap="round"/></svg></div></div>
    <div id="u3" class="use"><div class="n">3</div><div class="w">Quit what can't work<svg width="690" height="30" viewBox="0 0 660 30" preserveAspectRatio="none"><path class="ul" d="M4 18 C 200 8, 450 26, 656 12" fill="none" stroke="#111" stroke-width="10" stroke-linecap="round"/></svg></div></div>
  </div>

  <div id="cap" class="clip" data-start="0" data-duration="__DUR__" data-track-index="9"></div>
</div>
<script>
const T = __TIMING__;
const tl = gsap.timeline({ paused: true });
const S = Object.fromEntries(T.sections.map(s => [s.id, s]));
const L = (id, i) => S[id].lines[i];
// section visibility: push-in from below, push-out up (push-transition)
T.sections.forEach((s, i) => {
  const el = "#" + s.id;
  gsap.set(el, { opacity: 0 });
  tl.fromTo(el, { opacity: 0, y: i ? 120 : 0 }, { opacity: 1, y: 0, duration: i ? .35 : .01, ease: "power3.out" }, s.start);
  if (i < T.sections.length - 1) tl.to(el, { opacity: 0, y: -120, duration: .3, ease: "power2.in" }, s.end - .3);
  tl.from(el + " .kicker", { opacity: 0, x: -40, duration: .35, ease: "power3.out" }, s.start + .05);
});
// e01 stagger: chips land on their spoken words
const e1 = L("e01", 0), w1 = e1.words;
tl.from("#e01 .title", { opacity: 0, y: 60, duration: .5, ease: "back.out(1.6)" }, S.e01.start + .1);
[["#c1", 3], ["#c2", 5], ["#c3", 7], ["#c4", 9]].forEach(([c, wi]) => tl.from(c, { opacity: 0, y: 70, scale: .85, duration: .45, ease: "back.out(1.8)" }, w1[Math.min(wi, w1.length - 1)].start - .1));
tl.fromTo("#hand1", { rotate: -150, transformOrigin: "50px 50px" }, { rotate: 0, duration: .8, ease: "power2.inOut" }, w1[3].start);
const chk = document.getElementById("chk"); const cl = chk.getTotalLength(); gsap.set(chk, { strokeDasharray: cl, strokeDashoffset: cl });
tl.to(chk, { strokeDashoffset: 0, duration: .4, ease: "power2.out" }, w1[10].start + .2);
// e02 strikethrough-replace
const e2 = L("e02", 0), w2 = e2.words;
tl.from("#oldp", { opacity: 0, x: -60, duration: .4, ease: "power3.out" }, S.e02.start + .1);
const sp = document.getElementById("strikeP"); const sl = sp.getTotalLength(); gsap.set(sp, { strokeDasharray: sl, strokeDashoffset: sl });
tl.to(sp, { strokeDashoffset: 0, duration: .45, ease: "power2.inOut" }, w2[1].start).to("#oldp", { opacity: .35, duration: .3 }, w2[1].start + .3);
tl.from("#newc", { opacity: 0, y: 80, rotate: 3, duration: .5, ease: "back.out(1.6)" }, w2[2].start);
tl.from("#newc .row:nth-child(2)", { opacity: 0, x: 60, duration: .4, ease: "power3.out" }, w2[Math.min(8, w2.length - 1)].start);
tl.from("#exnote", { opacity: 0, duration: .4 }, w2[Math.min(8, w2.length - 1)].start + .3);
// e03 count-up + bar-grow
const e3a = L("e03", 0), e3b = e3a;
const num = document.getElementById("num"); const ctr = { v: 0 };
tl.to(ctr, { v: 94, duration: 1.3, ease: "power3.out", onUpdate: () => num.textContent = Math.round(ctr.v) }, e3a.words[1].start - .2);
tl.from("#numsub", { opacity: 0, y: 30, duration: .4 }, e3a.words[1].start + .9);
tl.from("#meter", { opacity: 0, y: 40, duration: .4, ease: "power3.out" }, e3b.words[8].start - .2);
tl.to("#fill", { scaleX: 0.72, duration: 1.2, ease: "power2.inOut" }, e3b.words[Math.min(15, e3b.words.length - 1)].start - .3);
tl.fromTo("#dval", { x: 0, opacity: 0 }, { x: 545, opacity: 1, duration: 1.2, ease: "power2.inOut" }, e3b.words[Math.min(15, e3b.words.length - 1)].start - .3);
tl.from("#cite", { opacity: 0, duration: .4 }, e3b.start + .6);
// e04 underline-draw per use
const e4 = L("e04", 0), w4 = e4.words;
document.querySelectorAll("#e04 .ul").forEach(p => { const l = p.getTotalLength(); gsap.set(p, { strokeDasharray: l, strokeDashoffset: l }); });
[["#u1", 3], ["#u2", 5], ["#u3", 9]].forEach(([u, wi], k) => {
  const at = w4[Math.min(wi, w4.length - 1)].start - .15;
  tl.from(u, { opacity: 0, x: -60, duration: .4, ease: "power3.out" }, at);
  tl.to(u + " .ul", { strokeDashoffset: 0, duration: .45, ease: "power2.out" }, at + .3);
});
tl.from("#u2 .ping", { scale: 0, duration: .35, ease: "back.out(2.4)" }, w4[Math.min(6, w4.length - 1)].start);
// captions: one EN line at a time, words light up on their (VI-voice-proportional) times
const cap = document.getElementById("cap");
T.sections.forEach(s => s.lines.forEach(l => {
  const d = document.createElement("div"); d.className = "cl"; cap.appendChild(d);
  l.cap.forEach((cw, i) => { const sp = document.createElement("span"); sp.className = "cw" + (l.hl.includes(i) ? " hl" : ""); sp.textContent = cw.word; d.appendChild(sp);
    tl.fromTo(sp, { opacity: .16, y: 18 }, { opacity: 1, y: 0, duration: .22, ease: "back.out(2)" }, cw.start); });
  tl.fromTo(d, { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: .2, ease: "power3.out" }, l.start - .05).to(d, { opacity: 0, duration: .15 }, l.capEnd - .15);
}));
tl.to("#root", { scale: 1.015, duration: __DUR__, ease: "none", transformOrigin: "50% 40%" }, 0);
window.__timelines = window.__timelines || {}; window.__timelines["main"] = tl; tl.seek(0);
</script>
</body></html>
