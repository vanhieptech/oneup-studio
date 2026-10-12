// Usage: node render.js <mode: anim|hiep|omi> <outdir>
// Legacy rig test tool (superseded by video-engine/ for real renders). Needs: npm i (puppeteer-core, see package.json).
let puppeteer;try{puppeteer=require('puppeteer-core');}catch(e){console.error('puppeteer-core missing: run `npm install` in pipeline/characters-v2 (or use video-engine/).');process.exit(1);}const path=require('path'),fs=require('fs');
const [mode,out]=process.argv.slice(2);fs.mkdirSync(out,{recursive:true});
(async()=>{const b=await puppeteer.launch({executablePath:process.env.CHROME_PATH||'/usr/bin/google-chrome',args:['--no-sandbox']});
const p=await b.newPage();await p.setViewport({width:1080,height:1920});
await p.goto('file://'+path.resolve(__dirname,'chars.html'));await p.evaluate(()=>document.fonts.ready);
const scene=fs.readFileSync(path.resolve(__dirname,'scene-'+mode+'.js'),'utf8');await p.evaluate(scene);
const n=await p.evaluate(()=>window.FRAMES);
for(let f=0;f<n;f++){await p.evaluate(f=>window.draw(f),f);
 await p.screenshot({path:`${out}/f${String(f).padStart(4,'0')}.png`});}
await b.close();})();
