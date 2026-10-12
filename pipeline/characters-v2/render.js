// Usage: node render.js <mode: anim|hiep|omi> <outdir>
const puppeteer=require('/tmp/pp/node_modules/puppeteer-core');const path=require('path'),fs=require('fs');
const [mode,out]=process.argv.slice(2);fs.mkdirSync(out,{recursive:true});
(async()=>{const b=await puppeteer.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
const p=await b.newPage();await p.setViewport({width:1080,height:1920});
await p.goto('file://'+path.resolve(__dirname,'chars.html'));await p.evaluate(()=>document.fonts.ready);
const scene=fs.readFileSync(path.resolve(__dirname,'scene-'+mode+'.js'),'utf8');await p.evaluate(scene);
const n=await p.evaluate(()=>window.FRAMES);
for(let f=0;f<n;f++){await p.evaluate(f=>window.draw(f),f);
 await p.screenshot({path:`${out}/f${String(f).padStart(4,'0')}.png`});}
await b.close();})();
