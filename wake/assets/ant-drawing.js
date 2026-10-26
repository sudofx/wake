/* Dorsal worker anatomy: six articulated legs attached to the mesosoma, two waist
   nodes, gaster, head, mandibles and elbowed antennae. Same renderer at every zoom. */
(function(root){
 'use strict';
 let art=null;
 const photo=typeof Image==='function'?new Image():null;if(photo){photo.onload=()=>{art=document.createElement('canvas');art.width=256;art.height=Math.round(256*photo.naturalHeight/photo.naturalWidth);art.getContext('2d').drawImage(photo,0,0,art.width,art.height);root.dispatchEvent(new Event('wake-ant-art-ready'));};photo.src='backgrounds/ant-body-v1.png';}
 function drawAnt(ctx,r,ant,gait,time){
  const c=ant.id%5,body=['#562c18','#482316','#60301a','#452318','#6a351c'][c],dark='#211710',light='#955b32';
  ctx.lineCap='round';ctx.lineJoin='round';
  // Alternating tripod stance: front + hind on one side, middle on the other.
  for(const side of [-1,1])for(let leg=0;leg<3;leg++){
   const moving=ant.moving??ant.phase<1,phase=((gait/(Math.PI*2)+(leg%2?.5:0)+(side<0?.5:0))%1+1)%1;
   // A longer planted stance, then a quick lifted return, keeps feet from paddling.
   const swing=moving?(phase<.68?1.22-2.44*phase/.68:-1.22+2.44*(phase-.68)/.32):0;
   const lift=moving&&phase>=.68?Math.sin((phase-.68)/.32*Math.PI):0;
   const stride=1-Math.max(0,side*(ant.turn||0))*.3;
   const hip=(.55-leg*.55)*r,kneeX=(.95-leg*.95+swing*.36*stride)*r,kneeY=side*(1.05+Math.abs(leg-1)*.12-lift*.12)*r;
   const footX=(ant.dead?.8-leg*.7:1.6-leg*1.65+swing*stride)*r,footY=side*(ant.dead?.65:1.9-Math.abs(leg-1)*.12-lift*.3)*r;
   ctx.strokeStyle=dark;ctx.lineWidth=r*.14;ctx.beginPath();ctx.moveTo(hip,side*r*.28);ctx.lineTo(kneeX,kneeY);ctx.stroke();ctx.lineWidth=r*.095;ctx.beginPath();ctx.moveTo(kneeX,kneeY);ctx.lineTo(footX,footY);ctx.lineTo(footX-r*.16,footY+side*r*.17);ctx.stroke();
   ctx.strokeStyle=light;ctx.lineWidth=r*.035;ctx.beginPath();ctx.moveTo(hip,side*r*.28);ctx.lineTo(kneeX,kneeY);ctx.stroke();
  }
  const ellipse=(x,y,rx,ry,fill)=>{const shade=ctx.createRadialGradient((x-rx*.3)*r,(y-ry*.5)*r,r*.06,x*r,y*r,Math.max(rx,ry)*r);shade.addColorStop(0,fill);shade.addColorStop(.45,fill);shade.addColorStop(1,dark);ctx.fillStyle=shade;ctx.beginPath();ctx.ellipse(x*r,y*r,rx*r,ry*r,0,0,Math.PI*2);ctx.fill();};
  const photographic=!!art;
  if(photographic){
   const w=art.width,h=art.height,y=h*.2,headMotion=ant.dead?0:Math.sin(time*2.7+ant.id)*.08;
   ctx.save();ctx.translate(-1.1*r,0);ctx.rotate(ant.moving?Math.sin(gait)*.035:0);ctx.drawImage(art,0,y,w*.4,h*.6,-2.2*r,-r,2.2*r,2*r);ctx.restore();
   ctx.drawImage(art,w*.39,y,w*.36,h*.6,-1.155*r,-r,1.98*r,2*r);
   ctx.save();ctx.translate(.77*r,0);ctx.rotate(headMotion);ctx.drawImage(art,w*.73,y,w*.27,h*.6,-.055*r,-r,1.485*r,2*r);ctx.restore();
  }else{
  // Gaster is larger than the mesosoma and separated by a narrow two-node waist.
  ellipse(-2.12,0,1.15,.76,body);ellipse(-2.38,-.3,.43,.12,'#a5704233');
  ctx.strokeStyle='#b28a5c38';ctx.lineWidth=r*.035;for(const x of [-2.55,-2.1,-1.68]){ctx.beginPath();ctx.moveTo(x*r,-.58*r);ctx.quadraticCurveTo((x+.25)*r,0,x*r,.58*r);ctx.stroke();}
  ellipse(-.98,0,.25,.25,body);ellipse(-.58,0,.22,.22,body);
  ellipse(.04,0,.68,.43,body);ellipse(.42,-.08,.4,.4,body);
  ellipse(1.18,0,.67,.59,body);ellipse(1.18,-.27,.35,.13,'#a6764433');
  ellipse(1.22,-.54,.12,.13,'#191611');ellipse(1.22,.54,.12,.13,'#191611');
  }
  const working=ant.work>=0,mandible=(working?Math.sin(time*5)*.1:0);
  ctx.strokeStyle=dark;ctx.lineWidth=r*.12;for(const side of [-1,1]){ctx.beginPath();ctx.moveTo(1.67*r,side*.34*r);ctx.lineTo(2.03*r,side*(.25+mandible)*r);ctx.lineTo(1.82*r,side*.08*r);ctx.stroke();}
  // Long scape, visible elbow and shorter forward-sweeping funiculus.
  for(const side of [-1,1]){const sweep=ant.dead?-.5:Math.sin(time*(side<0?2.7:3.4)+ant.id+side)*.28+Math.sin(time*6+ant.id)*.04;ctx.strokeStyle=body;ctx.lineWidth=r*.075;ctx.beginPath();ctx.moveTo(1.44*r,side*.4*r);ctx.lineTo((2.02+sweep)*r,side*1.02*r);ctx.lineTo((2.8+sweep)*r,side*(.9+sweep)*r);ctx.stroke();}
  if(ant.carrying){ctx.fillStyle=ant.carrying===1?'#b7bf73':'#ae9165';ctx.beginPath();ctx.ellipse(2.2*r,0,.38*r,.27*r,.4,0,Math.PI*2);ctx.fill();}
 }
 if(typeof module!=='undefined'&&module.exports)module.exports=drawAnt;else root.WakeDrawAnt=drawAnt;
})(typeof globalThis!=='undefined'?globalThis:this);
