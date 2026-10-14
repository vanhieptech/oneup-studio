<!doctype html>
<html lang="en" data-resolution="portrait">
<head>
<meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1920" />
<!-- clip-02 explainer (rule-42 motion beats). GENERATED from index.html.tpl by pipeline/scripts/build-final.py: edit the template/spec, not index.html. -->
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
/* clip-02 (rule-51/52 fx table) */
.acc{color:#FF5A36}
.task{position:absolute;width:420px;height:200px;flex-direction:column;justify-content:center;align-items:flex-start;gap:4px}
#t1{left:330px;top:820px}
.spike{position:absolute;font-size:52px;font-weight:700;background:#111;color:#F7F7F5;border-radius:24px;padding:6px 26px 14px;white-space:nowrap}
#s1{left:90px;top:600px;transform:rotate(-6deg)} #s2{left:600px;top:620px;transform:rotate(5deg)} #s3{left:250px;top:1140px;transform:rotate(-2deg);background:#FF5A36}
#dodge{position:absolute;left:60px;top:560px}
#q2{position:absolute;left:240px;top:1300px;font-size:72px;font-weight:700;background:#E4E2DD;border-radius:30px;padding:6px 30px 16px}
#num{position:absolute;left:78px;top:400px;font-size:400px;font-weight:700;letter-spacing:-16px;line-height:1}
#numsub{position:absolute;left:100px;top:840px;font-size:54px;font-weight:700}
.bar{position:absolute;left:100px;width:880px}
.bar .lab{font-size:42px;font-weight:700;margin-bottom:12px}
.bar .track{height:40px;border:7px solid #111;border-radius:22px;position:relative;background:#F7F7F5;overflow:hidden}
.bar .fill{position:absolute;left:0;top:0;bottom:0;width:100%;background:#111;transform-origin:0 50%;transform:scaleX(.15)}
#b1{top:990px} #b2{top:1130px} #b3{top:1270px} #b3 .fill{background:#FF5A36}
#cite{position:absolute;left:100px;top:1420px;font-size:30px;opacity:.6}
#scale{position:absolute;left:90px;top:640px;width:900px;height:700px}
#beam{transform-origin:450px 260px}
.pan{font-size:44px;font-weight:700}
#axis{position:absolute;left:100px;top:1360px;font-size:34px;font-weight:600;opacity:.6}
#qcard{left:190px;top:600px;width:700px;height:620px;flex-direction:column;justify-content:center;text-align:center;gap:20px}
#qcard .qm{font-size:300px;font-weight:700;line-height:1}
#qcard .qt{font-size:58px;font-weight:700;letter-spacing:-1px;white-space:normal;line-height:1.15}
#lens{position:absolute;left:700px;top:1100px;width:200px;height:200px}
.fixrow{position:absolute;left:96px;width:888px;height:250px;flex-direction:column;align-items:flex-start;justify-content:center;gap:16px}
#r1{top:580px} #r2{top:900px}
.fixrow .p{font-size:40px;font-weight:600;opacity:.6}
.fixrow .s{font-size:60px;font-weight:700;letter-spacing:-1px;display:flex;gap:18px;align-items:center}
#bul{display:flex;flex-direction:column;gap:4px;font-size:40px;font-weight:600}
#draft{left:600px;top:1010px;font-size:46px}
#ring{position:absolute;left:240px;top:560px;width:600px;height:600px}
#tnum{position:absolute;left:240px;top:760px;width:600px;text-align:center;font-size:150px;font-weight:700;letter-spacing:-6px}
#stopok{position:absolute;left:300px;top:1220px;font-size:70px;font-weight:700;background:#1F9D55;color:#F7F7F5;border-radius:30px;padding:6px 40px 18px}
#bad{position:absolute;left:96px;top:600px;font-size:96px;font-weight:700;letter-spacing:-3px;background:#E4E2DD;border-radius:40px;padding:10px 40px 26px}
#stampx{left:330px;top:820px;font-size:60px}
#t7{left:330px;top:1080px}
#t7 .spk{position:absolute;right:-30px;top:-40px;font-size:44px;font-weight:700;background:#FF5A36;color:#F7F7F5;border-radius:20px;padding:4px 18px 10px;transform-origin:0 100%}
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
    <div class="kicker">Procrastination =</div>
    <div class="title">Né cảm giác</div>
    <svg id="dodge" width="960" height="780" viewBox="0 0 960 780"><path class="dp" d="M120 700 C 40 420, 120 200, 480 190 C 840 200, 940 420, 860 700" fill="none" stroke="#111" stroke-width="12" stroke-dasharray="2 26" stroke-linecap="round"/><path class="dh" d="M830 660 L862 706 L900 660" fill="none" stroke="#111" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <div id="t1" class="card task"><div class="sub">// TODO</div><div class="lbl">Omi feature</div></div>
    <div id="s1" class="spike">Chán</div><div id="s2" class="spike">Sợ làm dở</div><div id="s3" class="spike">Không biết bắt đầu</div>
    <div id="q2">Nghe quen không?</div>
  </div>
  <div id="e02" class="sec clip" data-start="0" data-duration="__DUR__" data-track-index="1">
    <div class="kicker">Meta-analysis</div>
    <div id="num">0</div>
    <div id="numsub">correlations</div>
    <div id="b1" class="bar"><div class="lab">Task feels bad</div><div class="track"><div class="fill"></div></div></div>
    <div id="b2" class="bar"><div class="lab">“I can't do it”</div><div class="track"><div class="fill"></div></div></div>
    <div id="b3" class="bar"><div class="lab">Delay</div><div class="track"><div class="fill"></div></div></div>
    <div id="cite">Steel (2007) · correlational</div>
  </div>
  <div id="e03" class="sec clip" data-start="0" data-duration="__DUR__" data-track-index="2">
    <div class="kicker">Why the phone wins</div>
    <svg id="scale" viewBox="0 0 900 700">
      <path d="M450 260 L450 620 M330 640 h240" stroke="#111" stroke-width="14" stroke-linecap="round"/>
      <g id="beam"><path d="M110 260 H790" stroke="#111" stroke-width="14" stroke-linecap="round"/><circle cx="450" cy="260" r="20" fill="#111"/>
        <g id="panL"><path d="M110 260 L60 400 M110 260 L160 400" stroke="#111" stroke-width="6"/><path d="M30 400 h160 a80 40 0 0 1 -160 0z" fill="#E4E2DD" stroke="#111" stroke-width="8"/><g id="reward"><rect x="70" y="330" width="80" height="62" rx="10" fill="#1F9D55" stroke="#111" stroke-width="6"/><text x="110" y="315" text-anchor="middle" class="pan" font-family="BVP">Reward</text></g></g>
        <g id="panR"><path d="M790 260 L740 400 M790 260 L840 400" stroke="#111" stroke-width="6"/><path d="M710 400 h160 a80 40 0 0 1 -160 0z" fill="#E4E2DD" stroke="#111" stroke-width="8"/><rect x="752" y="290" width="76" height="110" rx="14" fill="#111"/><rect x="762" y="304" width="56" height="78" rx="6" fill="#FF5A36"/><text x="790" y="275" text-anchor="middle" class="pan" font-family="BVP">Now</text></g>
      </g>
    </svg>
    <div id="axis">now ─────────── later</div>
  </div>
  <div id="e04" class="sec clip" data-start="0" data-duration="__DUR__" data-track-index="3">
    <div class="kicker">Before you start, ask</div>
    <div id="qcard" class="card"><div class="qm">?</div><div class="qt">What exactly<br/>feels bad here?</div></div>
    <svg id="lens" viewBox="0 0 100 100"><circle cx="42" cy="42" r="28" fill="#F7F7F5" fill-opacity=".6" stroke="#111" stroke-width="9"/><path d="M62 62 L90 90" stroke="#111" stroke-width="12" stroke-linecap="round"/></svg>
  </div>
  <div id="e05" class="sec clip" data-start="0" data-duration="__DUR__" data-track-index="4">
    <div class="kicker">Make it feel smaller</div>
    <div id="r1" class="card fixrow"><div class="p">No clear start?</div><div class="s"><span class="tag">3</span><div id="bul"><span>– bullet</span><span>– bullet</span><span>– bullet</span></div></div></div>
    <div id="r2" class="card fixrow"><div class="p">Afraid it'll be bad?</div><div class="s">Ugly draft = OK</div></div>
    <div id="draft" class="stampbox">DRAFT · OK</div>
  </div>
  <div id="e06" class="sec clip" data-start="0" data-duration="__DUR__" data-track-index="5">
    <div class="kicker">Bored? Set a timer</div>
    <svg id="ring" viewBox="0 0 200 200"><circle cx="100" cy="100" r="84" fill="none" stroke="#E4E2DD" stroke-width="18"/><circle id="arc" cx="100" cy="100" r="84" fill="none" stroke="#111" stroke-width="18" stroke-linecap="round" transform="rotate(-90 100 100)"/></svg>
    <div id="tnum">10:00</div>
    <div id="stopok">STOP · OK</div>
  </div>
  <div id="e07" class="sec clip" data-start="0" data-duration="__DUR__" data-track-index="6">
    <div class="kicker">Common mistake</div>
    <div id="bad">“Mình lười quá!”</div>
    <div id="stampx" class="stampbox">✕ NOT HELPING</div>
    <div id="t7" class="card task"><div class="sub">// TODO</div><div class="lbl">Omi feature</div><div class="spk">feels worse</div></div>
  </div>
  <div id="cap" class="clip" data-start="0" data-duration="__DUR__" data-track-index="9"></div>
</div>
<script>
const T = __TIMING__;
const tl = gsap.timeline({ paused: true });
const S = Object.fromEntries(T.sections.map(s => [s.id, s]));
const A = (id, f) => { const s = S[id], l0 = s.lines[0], ln = s.lines[s.lines.length - 1]; return l0.start + f * (ln.capEnd - l0.start); };
// H(): marked key-animation hit (same time the accent SFX is mixed at, DL-043)
const H = (id, h) => { const x = (S[id].hits || []).find(k => k.id === h); return x ? x.t : A(id, .5); };
T.sections.forEach((s, i) => {
  const el = "#" + s.id; gsap.set(el, { opacity: 0 });
  tl.fromTo(el, { opacity: 0, y: i ? 120 : 0 }, { opacity: 1, y: 0, duration: i ? .35 : .01, ease: "power3.out" }, s.start);
  if (i < T.sections.length - 1) tl.to(el, { opacity: 0, y: -120, duration: .3, ease: "power2.in" }, s.end - .3);
  tl.from(el + " .kicker", { opacity: 0, x: -40, duration: .35, ease: "power3.out" }, s.start + .05);
  tl.from(el + " .title", { opacity: 0, y: 60, duration: .5, ease: "back.out(1.6)" }, s.start + .1);
});
const draw = (sel, t, d) => document.querySelectorAll(sel).forEach(p => { const l = p.getTotalLength(); gsap.set(p, { strokeDasharray: l, strokeDashoffset: l }); tl.to(p, { strokeDashoffset: 0, duration: d || .45, ease: "power2.out" }, t); });
const thump = (sel, t) => tl.fromTo(sel, { scale: 1 }, { scale: 1.08, duration: .09, yoyo: true, repeat: 1, ease: "power2.out" }, t);
// e01: task card, 3 emotion spikes sprout, the dodge arrow curves around it
tl.from("#t1", { opacity: 0, scale: .6, duration: .4, ease: "back.out(1.8)" }, S.e01.start + .15);
draw("#e01 .dp", H("e01", "shield") - .2, .6); tl.from("#e01 .dh", { opacity: 0, duration: .15 }, H("e01", "shield") + .35);
[["#s1", .45], ["#s2", .55], ["#s3", .66]].forEach(([s, f]) => tl.from(s, { opacity: 0, scale: 0, duration: .3, ease: "back.out(2.6)" }, A("e01", f)));
thump("#t1", H("e01", "faces"));
tl.from("#q2", { opacity: 0, y: 40, scale: .8, duration: .35, ease: "back.out(2)" }, A("e01", .86));
// e02: 691 counts up; bad-feeling + low-confidence bars rise, delay shoots up
const num = document.getElementById("num"); const ctr = { v: 0 };
tl.to(ctr, { v: 691, duration: 1.2, ease: "power3.out", onUpdate: () => num.textContent = Math.round(ctr.v) }, H("e02", "count"));
tl.from("#numsub", { opacity: 0, y: 30, duration: .4 }, A("e02", .12));
[["#b1", .3], ["#b2", .5], ["#b3", .62]].forEach(([b, f]) => tl.from(b, { opacity: 0, x: -60, duration: .35, ease: "power3.out" }, A("e02", f)));
tl.to("#b1 .fill", { scaleX: .8, duration: .6, ease: "power2.out" }, A("e02", .45));
tl.to("#b2 .fill", { scaleX: .85, duration: .6, ease: "power2.out" }, A("e02", .6));
tl.to("#b3 .fill", { scaleX: 1, duration: .35, ease: "power4.out" }, H("e02", "bars") - .35); thump("#b3", H("e02", "bars"));
tl.from("#cite", { opacity: 0, duration: .4 }, A("e02", .8));
// e03: reward shrinks as it slides to "later"; beam tips hard toward the phone
tl.from("#scale", { opacity: 0, y: 40, duration: .4 }, S.e03.start + .1); tl.from("#axis", { opacity: 0, duration: .4 }, A("e03", .1));
tl.to("#reward", { scale: .45, transformOrigin: "50% 100%", duration: .9, ease: "power2.inOut" }, A("e03", .15));
tl.fromTo("#beam", { rotate: 0, svgOrigin: "450 260" }, { rotate: 14, svgOrigin: "450 260", duration: .25, ease: "back.out(2.2)" }, H("e03", "tip") - .1);
thump("#panR", H("e03", "win"));
// e04: question card flips in, the lens scans it
tl.fromTo("#qcard", { rotateY: 90, opacity: 0 }, { rotateY: 0, opacity: 1, duration: .45, ease: "back.out(1.6)" }, A("e04", .15));
tl.from("#lens", { opacity: 0, x: 120, y: 80, duration: .4, ease: "power3.out" }, A("e04", .35));
tl.to("#lens", { x: -240, y: -380, duration: .6, ease: "power2.inOut" }, H("e04", "q") - .3); thump("#qcard", H("e04", "q"));
// e05: 3 bullets get written; DRAFT OK stamp lands
tl.from("#r1", { opacity: 0, x: -80, duration: .35, ease: "power3.out" }, A("e05", .05));
tl.from("#bul span", { opacity: 0, x: -30, duration: .2, stagger: .14, ease: "power2.out" }, H("e05", "bullets") - .1);
tl.from("#r2", { opacity: 0, x: -80, duration: .35, ease: "power3.out" }, A("e05", .52));
tl.fromTo("#draft", { opacity: 0, scale: 2.6 }, { opacity: 1, scale: 1, duration: .16, ease: "power4.in" }, H("e05", "draft") - .16); thump("#r2", H("e05", "draft"));
// e06: 10:00 ring runs, rings, STOP OK pops
const arc = document.getElementById("arc"); const L = 2 * Math.PI * 84; gsap.set(arc, { strokeDasharray: L, strokeDashoffset: 0 });
tl.from("#ring", { scale: .6, opacity: 0, duration: .4, ease: "back.out(1.8)" }, A("e06", .05)); tl.from("#tnum", { opacity: 0, duration: .3 }, A("e06", .1));
tl.to(arc, { strokeDashoffset: L, duration: Math.max(.5, H("e06", "ring") - H("e06", "timer")), ease: "none" }, H("e06", "timer"));
const tn = document.getElementById("tnum"); const tc = { v: 600 };
tl.to(tc, { v: 0, duration: Math.max(.5, H("e06", "ring") - H("e06", "timer")), ease: "none", onUpdate: () => { const s = Math.round(tc.v); tn.textContent = Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0"); } }, H("e06", "timer"));
tl.fromTo("#ring", { rotate: -6 }, { rotate: 6, duration: .06, yoyo: true, repeat: 5 }, H("e06", "ring"));
tl.from("#stopok", { opacity: 0, scale: 0, duration: .3, ease: "back.out(2.6)" }, H("e06", "ring"));
// e07: NOT HELPING stamp slams; the task's spike grows
tl.from("#bad", { opacity: 0, y: 40, duration: .4 }, S.e07.start + .1);
tl.fromTo("#stampx", { opacity: 0, scale: 2.6 }, { opacity: 1, scale: 1, duration: .16, ease: "power4.in" }, H("e07", "stamp") - .16);
tl.to("#bad", { opacity: .3, duration: .2 }, H("e07", "stamp")); thump("#e07", H("e07", "stamp"));
tl.from("#t7", { opacity: 0, y: 60, duration: .4, ease: "back.out(1.6)" }, A("e07", .5));
tl.fromTo("#t7 .spk", { scale: 0 }, { scale: 1.25, duration: .3, ease: "back.out(2.6)" }, H("e07", "worse") - .1);
// captions
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
