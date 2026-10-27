/* Lasius-inspired dorsal anatomy. Size and silhouette distinguish the queen;
   the warm highlight is a viewing aid, not a claim about caste coloration. */
(function(root){
 'use strict';
 function drawAnt(ctx,r,ant,gait,time){
  const queen=Boolean(ant.queen),pale=Boolean(ant.callow),c=((ant.id%5)+5)%5;
  const body=queen?'#754a25':pale?'#b99d67':['#342a20','#2c251e','#3b2e22','#29251e','#403023'][c],dark=pale?'#76623f':'#1b1712',light=queen?'#c29954':pale?'#d5c18a':'#79603b';
  ctx.lineCap='round';ctx.lineJoin='round';
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
  }
  const ellipse=(x,y,rx,ry,fill)=>{const shade=ctx.createRadialGradient((x-rx*.3)*r,(y-ry*.5)*r,r*.06,x*r,y*r,Math.max(rx,ry)*r);shade.addColorStop(0,fill);shade.addColorStop(.45,fill);shade.addColorStop(1,dark);ctx.fillStyle=shade;ctx.beginPath();ctx.ellipse(x*r,y*r,rx*r,ry*r,0,0,Math.PI*2);ctx.fill();};
  // A single petiole separates the gaster from the mesosoma in this formicine
  // silhouette. The queen has a fuller thorax and a distinctly enlarged gaster.
  ellipse(queen?-2.25:-2.05,0,queen?1.5:1.08,queen?1.04:.72,body);
  ellipse(queen?-2.55:-2.3,-.28,queen?.56:.4,.12,queen?'#d6b57944':'#a58b5433');
  ctx.strokeStyle=queen?'#d2ad6a66':'#a58b5438';ctx.lineWidth=r*.045;
  for(const x of queen?[-2.95,-2.35,-1.75]:[-2.55,-2.1,-1.68]){ctx.beginPath();ctx.moveTo(x*r,-(queen?.83:.53)*r);ctx.quadraticCurveTo((x+.2)*r,0,x*r,(queen?.83:.53)*r);ctx.stroke();}
  ellipse(-.72,0,.23,.24,body);
  ellipse(.03,0,queen?.9:.65,queen?.6:.42,body);ellipse(.43,-.05,queen?.55:.38,queen?.56:.38,body);
  if(queen){ctx.strokeStyle='#cfad6a88';ctx.lineWidth=r*.06;ctx.beginPath();ctx.moveTo(-.35*r,-.38*r);ctx.quadraticCurveTo(.1*r,-.48*r,.5*r,-.33*r);ctx.stroke();}
  ellipse(1.2,0,.64,.57,body);ellipse(1.17,-.25,.32,.12,queen?'#b9924c66':'#9f895033');
  ellipse(1.24,-.52,.1,.12,'#15130f');ellipse(1.24,.52,.1,.12,'#15130f');
  const working=ant.work>=0,mandible=working?Math.sin(time*5)*.1:0;
  ctx.strokeStyle=dark;ctx.lineWidth=r*.12;for(const side of [-1,1]){ctx.beginPath();ctx.moveTo(1.67*r,side*.34*r);ctx.lineTo(2.03*r,side*(.25+mandible)*r);ctx.lineTo(1.82*r,side*.08*r);ctx.stroke();}
  for(const side of [-1,1]){const sweep=ant.dead?-.5:Math.sin(time*(side<0?2.7:3.4)+ant.id+side)*.28+Math.sin(time*6+ant.id)*.04;ctx.strokeStyle=body;ctx.lineWidth=r*.075;ctx.beginPath();ctx.moveTo(1.44*r,side*.4*r);ctx.lineTo((2.02+sweep)*r,side*1.02*r);ctx.lineTo((2.8+sweep)*r,side*(.9+sweep)*r);ctx.stroke();}
  if(ant.carrying){ctx.fillStyle=ant.carrying===1?(ant.carryingKind==='protein'?'#a96a45':'#b7bf73'):'#ae9165';ctx.beginPath();ctx.ellipse(2.2*r,0,.38*r,.27*r,.4,0,Math.PI*2);ctx.fill();}
 }
 if(typeof module!=='undefined'&&module.exports)module.exports=drawAnt;else root.WakeDrawAnt=drawAnt;
})(typeof globalThis!=='undefined'?globalThis:this);
