/* Dorsal worker anatomy: six articulated legs attached to the mesosoma, two waist
   nodes, gaster, head, mandibles and elbowed antennae. Same renderer at every zoom. */
(function(root){
 'use strict';
 function drawAnt(ctx,r,ant,gait,time){
  const c=ant.id%5,body=['#562c18','#482316','#60301a','#452318','#6a351c'][c],dark='#211710',light='#955b32';
  ctx.lineCap='round';ctx.lineJoin='round';
  // Alternating tripod stance: front + hind on one side, middle on the other.
  for(const side of [-1,1])for(let leg=0;leg<3;leg++){
   const swing=ant.phase<1?Math.sin(gait+(leg%2?Math.PI:0)+(side<0?Math.PI:0))*.36:0;
   const hip=(.55-leg*.55)*r,kneeX=(1.3-leg*1.25+swing)*r,kneeY=side*(1.08+Math.abs(leg-1)*.15)*r;
   const footX=(1.9-leg*1.8-swing)*r,footY=side*(1.95-Math.abs(leg-1)*.16)*r;
   ctx.strokeStyle=dark;ctx.lineWidth=r*.14;ctx.beginPath();ctx.moveTo(hip,side*r*.28);ctx.lineTo(kneeX,kneeY);ctx.stroke();ctx.lineWidth=r*.095;ctx.beginPath();ctx.moveTo(kneeX,kneeY);ctx.lineTo(footX,footY);ctx.lineTo(footX-r*.16,footY+side*r*.17);ctx.stroke();
   ctx.strokeStyle=light;ctx.lineWidth=r*.035;ctx.beginPath();ctx.moveTo(hip,side*r*.28);ctx.lineTo(kneeX,kneeY);ctx.stroke();
  }
  const ellipse=(x,y,rx,ry,fill)=>{const shade=ctx.createRadialGradient((x-rx*.3)*r,(y-ry*.5)*r,r*.06,x*r,y*r,Math.max(rx,ry)*r);shade.addColorStop(0,fill);shade.addColorStop(.45,fill);shade.addColorStop(1,dark);ctx.fillStyle=shade;ctx.beginPath();ctx.ellipse(x*r,y*r,rx*r,ry*r,0,0,Math.PI*2);ctx.fill();};
  // Gaster is larger than the mesosoma and separated by a narrow two-node waist.
  ellipse(-2.12,0,1.15,.76,body);ellipse(-2.38,-.3,.43,.12,'#a5704233');
  ctx.strokeStyle='#b28a5c38';ctx.lineWidth=r*.035;for(const x of [-2.55,-2.1,-1.68]){ctx.beginPath();ctx.moveTo(x*r,-.58*r);ctx.quadraticCurveTo((x+.25)*r,0,x*r,.58*r);ctx.stroke();}
  ellipse(-.98,0,.25,.25,body);ellipse(-.58,0,.22,.22,body);
  ellipse(.04,0,.68,.43,body);ellipse(.42,-.08,.4,.4,body);
  ellipse(1.18,0,.67,.59,body);ellipse(1.18,-.27,.35,.13,'#a6764433');
  ellipse(1.22,-.54,.12,.13,'#191611');ellipse(1.22,.54,.12,.13,'#191611');
  const working=ant.work>=0,mandible=(working?Math.sin(time*5)*.1:0);
  ctx.strokeStyle=dark;ctx.lineWidth=r*.12;for(const side of [-1,1]){ctx.beginPath();ctx.moveTo(1.67*r,side*.34*r);ctx.lineTo(2.03*r,side*(.25+mandible)*r);ctx.lineTo(1.82*r,side*.08*r);ctx.stroke();}
  // Long scape, visible elbow and shorter forward-sweeping funiculus.
  for(const side of [-1,1]){const sweep=Math.sin(time*1.6+ant.id+side)*.14;ctx.strokeStyle=body;ctx.lineWidth=r*.075;ctx.beginPath();ctx.moveTo(1.44*r,side*.4*r);ctx.lineTo((2.02+sweep)*r,side*1.02*r);ctx.lineTo((2.8+sweep)*r,side*(.9+sweep)*r);ctx.stroke();}
  if(ant.carrying){ctx.fillStyle=ant.carrying===1?'#b7bf73':'#ae9165';ctx.beginPath();ctx.ellipse(2.2*r,0,.38*r,.27*r,.4,0,Math.PI*2);ctx.fill();}
 }
 if(typeof module!=='undefined'&&module.exports)module.exports=drawAnt;else root.WakeDrawAnt=drawAnt;
})(typeof globalThis!=='undefined'?globalThis:this);
