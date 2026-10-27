/* Lasius-inspired dorsal anatomy. Size and silhouette distinguish the queen;
   the warm highlight is a viewing aid, not a claim about caste coloration. */
(function(root){
 'use strict';
 let shellAtlas=null;
 if(typeof document!=='undefined'){
  const source=new Image();source.onload=()=>{
   // One bounded atlas supplies chitin texture; articulated anatomy stays live.
   const atlas=document.createElement('canvas');atlas.width=1024;atlas.height=512;
   atlas.getContext('2d').drawImage(source,0,0,1024,512);shellAtlas=atlas;
   window.dispatchEvent(new Event('wake-ant-art-ready'));
  };source.src=new URL('backgrounds/ant-body-v1.png',document.currentScript.src).href;
 }
 function drawAnt(ctx,r,ant,gait,time){
  const queen=Boolean(ant.queen),pale=Boolean(ant.callow),c=((ant.id%5)+5)%5;
  const detail=(ant.detail||0)>7,macro=(ant.detail||0)>15;
  const body=queen?'#754a25':pale?'#b99d67':['#342a20','#2c251e','#3b2e22','#29251e','#403023'][c],dark=pale?'#76623f':'#1b1712',light=queen?'#c29954':pale?'#d5c18a':'#79603b';
  ctx.lineCap='round';ctx.lineJoin='round';
  const contact=ctx.createRadialGradient(-.6*r,.2*r,.2*r,-.6*r,.2*r,2.6*r);
  contact.addColorStop(0,'#30211030');contact.addColorStop(1,'#30211000');ctx.fillStyle=contact;ctx.beginPath();ctx.ellipse(-.6*r,.2*r,2.7*r,1.1*r,0,0,Math.PI*2);ctx.fill();
  // Three pairs of legs originate on the mesosoma. Alternating tripods and a
  // planted stance are illustrative gait choices, not calibrated stride data.
  for(const side of [-1,1])for(let leg=0;leg<3;leg++){
   const moving=ant.moving??ant.phase<1,phase=((gait/(Math.PI*2)+(leg%2?.5:0)+(side<0?.5:0))%1+1)%1;
   const rest=queen&&!ant.dead?(ant.restingMotion||0)*Math.sin(time*.7+leg*1.9+side)*.12:0;
   const swing=moving?(phase<.68?1.22-2.44*phase/.68:-1.22+2.44*(phase-.68)/.32):rest;
   const lift=moving&&phase>=.68?Math.sin((phase-.68)/.32*Math.PI):0;
   const stride=1-Math.max(0,side*(ant.turn||0))*.3;
   const hip=(.55-leg*.55)*r,kneeX=(.95-leg*.95+swing*.36*stride)*r,kneeY=side*(1.05+Math.abs(leg-1)*.12-lift*.12)*r;
   const footX=(ant.dead?.8-leg*.7:1.6-leg*1.65+swing*stride)*r,footY=side*(ant.dead?.65:1.9-Math.abs(leg-1)*.12-lift*.3)*r;
   ctx.strokeStyle=dark;ctx.lineWidth=r*.14;ctx.beginPath();ctx.moveTo(hip,side*r*.28);ctx.lineTo(kneeX,kneeY);ctx.stroke();ctx.lineWidth=r*.095;ctx.beginPath();ctx.moveTo(kneeX,kneeY);ctx.lineTo(footX,footY);ctx.lineTo(footX-r*.16,footY+side*r*.17);ctx.stroke();
   ctx.strokeStyle=light;ctx.lineWidth=r*.035;ctx.beginPath();ctx.moveTo(hip,side*r*.28);ctx.lineTo(kneeX,kneeY);ctx.stroke();
   if(detail){
    // Tarsal joints and paired claws appear only when the lens resolves them.
    ctx.strokeStyle=dark;ctx.lineWidth=r*.045;
    for(let joint=1;joint<4;joint++){const x=footX-r*.035*joint,y=footY+side*r*.04*joint;ctx.beginPath();ctx.moveTo(x-r*.045,y);ctx.lineTo(x+r*.045,y+side*r*.045);ctx.stroke();}
    ctx.beginPath();ctx.moveTo(footX-r*.16,footY+side*r*.17);ctx.lineTo(footX-r*.22,footY+side*r*.22);ctx.moveTo(footX-r*.16,footY+side*r*.17);ctx.lineTo(footX-r*.11,footY+side*r*.24);ctx.stroke();
   }
  }
  const ellipse=(x,y,rx,ry,fill)=>{const shade=ctx.createRadialGradient((x-rx*.3)*r,(y-ry*.5)*r,r*.06,x*r,y*r,Math.max(rx,ry)*r);shade.addColorStop(0,fill);shade.addColorStop(.45,fill);shade.addColorStop(1,dark);ctx.fillStyle=shade;ctx.beginPath();ctx.ellipse(x*r,y*r,rx*r,ry*r,0,0,Math.PI*2);ctx.fill();};
  const shell=(x,y,rx,ry,part)=>{
   if(!shellAtlas)return;const box=part==='gaster'?[.012,.235,.304,.495]:part==='head'?[.735,.25,.18,.5]:[.455,.34,.278,.305];
   ctx.save();ctx.beginPath();ctx.ellipse(x*r,y*r,rx*r,ry*r,0,0,Math.PI*2);ctx.clip();ctx.globalAlpha=pale?.3:.86;
   ctx.drawImage(shellAtlas,box[0]*1024,box[1]*512,box[2]*1024,box[3]*512,(x-rx)*r,(y-ry)*r,rx*2*r,ry*2*r);ctx.restore();
  };
  // A single petiole separates the gaster from the mesosoma in this formicine
  // silhouette. The queen has a fuller thorax and a distinctly enlarged gaster.
  ellipse(queen?-2.25:-2.05,0,queen?1.5:1.08,queen?1.04:.72,body);
  shell(queen?-2.25:-2.05,0,queen?1.5:1.08,queen?1.04:.72,'gaster');
  ellipse(queen?-2.55:-2.3,-.28,queen?.56:.4,.12,queen?'#d6b57944':'#a58b5433');
  ctx.strokeStyle=queen?'#d2ad6a66':'#a58b5438';ctx.lineWidth=r*.045;
  for(const x of queen?[-2.95,-2.35,-1.75]:[-2.55,-2.1,-1.68]){ctx.beginPath();ctx.moveTo(x*r,-(queen?.83:.53)*r);ctx.quadraticCurveTo((x+.2)*r,0,x*r,(queen?.83:.53)*r);ctx.stroke();}
  ellipse(-.72,0,.23,.24,body);
  ellipse(.03,0,queen?.9:.65,queen?.6:.42,body);ellipse(.43,-.05,queen?.55:.38,queen?.56:.38,body);
  shell(.14,0,queen?1.02:.78,queen?.6:.42,'thorax');
  if(queen){ctx.strokeStyle='#cfad6a88';ctx.lineWidth=r*.06;ctx.beginPath();ctx.moveTo(-.35*r,-.38*r);ctx.quadraticCurveTo(.1*r,-.48*r,.5*r,-.33*r);ctx.stroke();}
  ellipse(1.2,0,.64,.57,body);ellipse(1.17,-.25,.32,.12,queen?'#b9924c66':'#9f895033');
  shell(1.2,0,.64,.57,'head');
  if(!shellAtlas){ellipse(1.24,-.52,.1,.12,'#15130f');ellipse(1.24,.52,.1,.12,'#15130f');}
  if(detail){
   ctx.strokeStyle=queen?'#ead3a466':'#d8c6a344';ctx.lineWidth=r*.018;
   // Fine setae follow each body's outline rather than a painted sprite.
   for(const part of [{x:queen?-2.25:-2.05,rx:queen?1.5:1.08,ry:queen?1.04:.72},{x:1.2,rx:.64,ry:.57}])for(let i=0;i<22;i++){
    const angle=i*Math.PI*2/22,dx=Math.cos(angle),dy=Math.sin(angle),x=(part.x+dx*part.rx)*r,y=dy*part.ry*r;
    ctx.beginPath();ctx.moveTo(x,y);ctx.lineTo(x+dx*r*.1,y+dy*r*.13);ctx.stroke();
   }
   ctx.strokeStyle='#e3c99422';ctx.lineWidth=r*.012;
   for(let i=0;i<16;i++){const x=(-2.8+i*.1)*r;ctx.beginPath();ctx.moveTo(x,-.26*r);ctx.quadraticCurveTo(x+.06*r,0,x,.26*r);ctx.stroke();}
   if(macro&&!shellAtlas)for(const side of [-1,1]){ctx.fillStyle='#b2a17e77';for(let i=0;i<7;i++){const angle=i*2.4;ctx.beginPath();ctx.arc((1.24+Math.cos(angle)*.055)*r,(side*.52+Math.sin(angle)*.07)*r,r*.018,0,Math.PI*2);ctx.fill();}}
  }
  const working=ant.work>=0,tending=ant.role==='nurse'&&ant.phase>=1;
  const idle=Math.max(0,(Math.sin(time*.65+ant.id*1.7)-.84)/.16);
  const opening=ant.dead?0:ant.carrying?(ant.carrying===2?.22:.14):working?.10+(.5+.5*Math.sin(time*6+ant.id))*.52:tending?.08+(.5+.5*Math.sin(time*2.1+ant.id))*.16:.045+idle*.23;
  // Each toothed blade pivots at the front of the head. The two tips meet
  // medially, grip a load, or separate laterally during excavation and care.
  for(const side of [-1,1]){
   ctx.save();ctx.translate(1.57*r,side*.26*r);ctx.rotate(side*opening);ctx.scale(1,side);
   ctx.beginPath();ctx.moveTo(-.035*r,-.035*r);
   ctx.bezierCurveTo(.12*r,.16*r,.42*r,.15*r,.59*r,-.16*r);
   ctx.quadraticCurveTo(.63*r,-.23*r,.58*r,-.255*r);
   ctx.lineTo(.51*r,-.16*r);ctx.lineTo(.475*r,-.21*r);ctx.lineTo(.42*r,-.125*r);ctx.lineTo(.38*r,-.175*r);ctx.lineTo(.32*r,-.075*r);ctx.lineTo(.27*r,-.13*r);ctx.lineTo(.20*r,-.04*r);ctx.lineTo(.14*r,-.085*r);ctx.lineTo(.07*r,-.015*r);ctx.closePath();
   const chitin=ctx.createLinearGradient(0,-.15*r,.55*r,.06*r);chitin.addColorStop(0,pale?'#a58a59':'#6e361c');chitin.addColorStop(.45,pale?'#d2ba83':'#a15a30');chitin.addColorStop(1,'#3e2215');ctx.fillStyle=chitin;ctx.fill();
   if(shellAtlas){ctx.save();ctx.clip();ctx.globalAlpha=pale?.28:.75;ctx.drawImage(shellAtlas,.905*1024,.365*512,.083*1024,.15*512,-.035*r,-.27*r,.67*r,.46*r);ctx.restore();}
   ctx.strokeStyle=pale?'#8b7149':'#472719';ctx.lineWidth=r*.022;ctx.stroke();
   ctx.strokeStyle='#d5a66b66';ctx.lineWidth=r*.018;ctx.beginPath();ctx.moveTo(.04*r,.015*r);ctx.quadraticCurveTo(.27*r,.09*r,.49*r,-.11*r);ctx.stroke();ctx.restore();
  }
  for(const side of [-1,1]){const sweep=ant.dead?-.5:Math.sin(time*(side<0?2.7:3.4)+ant.id+side)*.28+Math.sin(time*6+ant.id)*.04;ctx.strokeStyle=body;ctx.lineWidth=r*.075;ctx.beginPath();ctx.moveTo(1.44*r,side*.4*r);ctx.lineTo((2.02+sweep)*r,side*1.02*r);ctx.lineTo((2.8+sweep)*r,side*(.9+sweep)*r);ctx.stroke();
   if(detail){ctx.strokeStyle=light;ctx.lineWidth=r*.025;for(let joint=0;joint<8;joint++){const t=joint/8,x=(2.02+sweep+.78*t)*r,y=side*(1.02+(sweep-.12)*t)*r;ctx.beginPath();ctx.moveTo(x,y-r*.045);ctx.lineTo(x,y+r*.045);ctx.stroke();}}
  }
  if(ant.carrying){ctx.fillStyle=ant.carrying===1?(ant.carryingKind==='protein'?'#a96a45':'#b7bf73'):'#ae9165';ctx.beginPath();ctx.ellipse(2.2*r,0,.38*r,.27*r,.4,0,Math.PI*2);ctx.fill();}
 }
 if(typeof module!=='undefined'&&module.exports)module.exports=drawAnt;else root.WakeDrawAnt=drawAnt;
})(typeof globalThis!=='undefined'?globalThis:this);
