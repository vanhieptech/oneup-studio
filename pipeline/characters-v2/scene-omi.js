window.FRAMES=1;window.draw=function(){const {omi}=CH;const ex=[['happy','happy',0,'vui'],['curious','curious',0,'tò mò'],['worried','worried',0,'lo lắng'],['happy','curious',.5,'morph vui → tò mò'],['curious','worried',.5,'morph tò mò → lo lắng'],['happy','happy',0,'giọt liquid (gooey)']];
let g='';ex.forEach(([a,b,k,l],i)=>{const x=290+(i%2)*500,y=470+Math.floor(i/2)*540;
 g+=`<g transform="translate(${x},${y}) scale(1.05)">${omi(i*1.7+.4,a,b,k,0,1,'o'+i)}</g><text x="${x}" y="${y+300}" font-size="32" font-weight="700" text-anchor="middle">${l}</text>`;});
document.getElementById('s').setAttribute('width',1080);document.getElementById('s').setAttribute('height',1920);
document.getElementById('s').innerHTML=`<rect width="1080" height="1920" fill="#F7F7F5"/><text x="80" y="150" font-size="60" font-weight="700">Omi · model sheet v2</text><text x="80" y="210" font-size="30" font-weight="300" fill="#6B6B6B">blob mực · liquid morph · xuất hiện từ tuần 5</text>${g}`;};
