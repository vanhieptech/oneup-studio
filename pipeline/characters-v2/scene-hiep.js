window.FRAMES=1;window.draw=function(){const {hiep}=CH;const ex=[['neutral','bình thường'],['happy','vui'],['surprised','bất ngờ'],['tired','mệt'],['focused','tập trung'],['neutral','nhún (squash)']];
let g='';ex.forEach(([e,l],i)=>{const x=290+(i%2)*500,y=620+Math.floor(i/2)*560;const sq=i==5;
 g+=`<g transform="translate(${x},${y}) scale(.62)">${hiep({expr:e,sx:sq?1.14:1,sy:sq?.86:1,look:0},'h'+i)}</g><text x="${x}" y="${y+60}" font-size="34" font-weight="700" text-anchor="middle">${l}</text>`;});
document.getElementById('s').setAttribute('width',1080);document.getElementById('s').setAttribute('height',1920);
document.getElementById('s').innerHTML=`<rect width="1080" height="1920" fill="#F7F7F5"/><text x="80" y="150" font-size="60" font-weight="700">Hiệp · model sheet v2</text><text x="80" y="210" font-size="30" font-weight="300" fill="#6B6B6B">chibi · đầu to · bo tròn · ngoại hình thật chưa có (tạm generic)</text>${g}`;};
