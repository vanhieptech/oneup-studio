window.FRAMES=210;
window.draw=function(f){const {hiep,omi,spring,clamp,lerp}=CH;const t=f/30;
 // Hiệp: breathing + hop at 2.4s (anticipate -> stretch -> land squash -> spring settle)
 let a=0.02*Math.sin(t*2.4);
 const h0=2.4; if(t>h0&&t<h0+.25) a=-0.12*Math.sin((t-h0)/.25*Math.PI/2);
 let lift=0;
 if(t>=h0+.25&&t<h0+.75){const u=(t-h0-.25)/.5; lift=-150*4*u*(1-u); a=lerp(-.12,.10,clamp(u*3))*(u<.8?1:1-(u-.8)*5);} // stretch in air
 if(t>=h0+.75){const u=t-h0-.75; a+= -0.16*Math.exp(-5*u)*Math.cos(15*u);} // land squash, springy settle
 const sx=1-a*.9, sy=1+a;
 const lag=(t>=h0+.25&&t<h0+.75)?18*Math.sin((t-h0-.25)/.5*Math.PI):(t>=h0+.75?-26*Math.exp(-5*(t-h0-.75))*Math.cos(15*(t-h0-.75)):0);
 const blinkAt=[1.1,4.1,6.2];let blink=0;for(const b of blinkAt){const d=Math.abs(t-b);if(d<.09) blink=1-d/.09;}
 const expr=t>h0+.1&&t<h0+1.4?'happy':(t>4.6&&t<6.6?'surprised':'neutral');
 const arm=(t>h0+.25&&t<h0+.9)?40*Math.sin((t-h0-.25)/.65*Math.PI):6*Math.sin(t*2.4);
 // Omi emotions: happy -> curious (2.2-2.9) -> worried (4.4-5.1)
 let A='happy',B='happy',k=0;
 if(t>=2.2&&t<2.9){A='happy';B='curious';k=(t-2.2)/.7;} else if(t>=2.9&&t<4.4){A=B='curious';}
 else if(t>=4.4&&t<5.1){A='curious';B='worried';k=(t-4.4)/.7;} else if(t>=5.1){A=B='worried';}
 const tk=(t>=2.2&&t<2.9)?(t-2.2)/.7:((t>=4.4&&t<5.1)?(t-4.4)/.7:-1);
 const fsq=tk>=0?1-0.85*Math.sin(clamp(tk)*Math.PI)**2:1; // face squash-blinks through the swap
 const ob=Math.abs(t-3.5)<.08?1-Math.abs(t-3.5)/.08:0;
 const label={happy:'vui',curious:'tò mò',worried:'lo lắng'}[k<.5?A:B];
 const fy=Math.sin(t*1.8)*22, rot=Math.sin(t*1.1)*4+(B==='curious'&&k>.3?8:0)*(1);
 document.getElementById('s').setAttribute('width',1080);document.getElementById('s').setAttribute('height',1920);
 document.getElementById('s').innerHTML=`<rect width="1080" height="1920" fill="#F7F7F5"/>
 <text x="96" y="190" font-size="40" font-weight="300" fill="#6B6B6B">@hi.oneup · nhân vật v2</text>
 <text x="96" y="262" font-size="64" font-weight="700">Hiệp &amp; Omi</text>
 <g transform="translate(700,720) scale(1.45) rotate(${rot})"><g transform="translate(0,${fy})">${omi(t,A,B,k,ob,fsq)}</g></g>
 <g transform="translate(700,1060)"><rect x="-110" y="-44" width="220" height="76" rx="38" fill="#111111"/><text x="0" y="8" font-size="36" font-weight="700" text-anchor="middle" fill="#F7F7F5">${label}</text></g>
 <g transform="translate(400,1700) scale(1.35) translate(0,${lift})">${hiep({sx,sy,lag,arm,blink,look:.8,expr,tilt:Math.sin(t*1.2)*2})}</g>
 <text x="540" y="1830" font-size="30" font-weight="300" text-anchor="middle" fill="#6B6B6B">test chuyển động · không nhạc</text>`;};
