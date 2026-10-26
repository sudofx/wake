/* Research-inspired 2D habitat. Narrow graph tunnels, finite pellet work, no record access. */
(function(root){
  'use strict';
  const WIDTH=120,HEIGHT=96,SURFACE=13,COUNT=64,MAX_ANTS=128,SCHEMA='wake-ant-colony@3',MODEL='pellet-tunnels@8';
  const PELLETS=10,WORK_SECONDS=7,MAX_NODES=3000;
  const pointDistance=(p,a,b)=>{const dx=b.x-a.x,dy=b.y-a.y,t=Math.max(0,Math.min(1,((p.x-a.x)*dx+(p.y-a.y)*dy)/(dx*dx+dy*dy||1)));return Math.hypot(p.x-a.x-t*dx,p.y-a.y-t*dy);};
  class Colony{
    constructor(seed=1){
      this.seed=seed>>>0||1;this.rng=this.seed;this.time=0;this.ticks=0;this.dug=0;this.delivered=0;this.soilDelivered=0;this.addedFood=0;this.samples=[];this.lastSample=0;this.nodes=[];this.fronts=[];
      // A small starter nest is provided; subsequent excavation is counted separately.
      for(let x=2;x<WIDTH-1;x++)this.node(x,18+4*Math.sin(x*.055+(this.seed%97))+1.5*Math.cos(x*.13),x===2?null:this.nodes.length-1,'surface');
      this.food=[{x:20,y:this.surfaceAt(20),left:240},{x:100,y:this.surfaceAt(100),left:240}];
      // Seeded asymmetry replaces the identical straight shaft and three-way fork.
      for(let i=0;i<16;i++)this.random();
      this.exit=38+Math.floor(this.random()*40);let parent=this.exit;
      let shaftAngle=Math.PI*(.38+this.random()*.24);
      const shaftLength=10+Math.floor(this.random()*8);
      for(let k=0;k<shaftLength;k++){
        shaftAngle=Math.max(.9,Math.min(2.24,shaftAngle+(this.random()-.5)*.3));
        const p=this.nodes[parent];parent=this.node(p.x+Math.cos(shaftAngle)*1.35,p.y+Math.sin(shaftAngle)*1.35,parent,k===shaftLength-1?'chamber':'tunnel');
      }
      this.nest=parent;
      const branches=1+Math.floor(this.random()*4),angles=[];
      for(let attempt=0;angles.length<branches&&attempt<200;attempt++){
        const angle=.2+this.random()*(Math.PI-.4);
        if(angles.every(other=>Math.abs(other-angle)>=.55))angles.push(angle);
      }
      if(angles.length<branches){angles.length=0;for(let j=0;j<branches;j++)angles.push(branches===1?Math.PI/2:.25+j*(Math.PI-.5)/(branches-1));}
      for(const angle of angles){
        let tip=this.nest;const length=3+Math.floor(this.random()*3);
        for(let k=0;k<length;k++){const p=this.nodes[tip];tip=this.node(p.x+Math.cos(angle)*1.7,p.y+Math.sin(angle)*1.7,tip,'tunnel');}
        this.fronts.push({node:tip,angle,effort:0,length:0,blocked:false,turn:(this.random()-.5)*.4,branchAt:4+Math.floor(this.random()*10)});
      }
      this.links=[];this.junctions=[];this.exits=[this.exit];this.nextAntId=COUNT;this.born=0;this.deaths=0;this.foodReserve=20;this.brood=[];this.recentDeaths=[];this.lastExpansion=0;this.starvationSeconds=0;this.starved=0;
      this.initialNodes=this.nodes.length;this.rebuild();
      this.ants=Array.from({length:COUNT},(_,id)=>{
        const role=id<12?'dig':id<44?'forage':'rest',front=id%this.fronts.length;
        let workCell=this.fronts[front].node;for(let k=0;k<Math.floor(id/3)&&k<3;k++)workCell=this.nodes[workCell].parent;
        const cell=role==='dig'?workCell:role==='rest'&&id<52?this.nest:30+Math.floor(this.random()*60);
        return {id,cell,from:cell,dir:this.random()*Math.PI*2,phase:1,carrying:0,role,steps:0,wait:role==='rest'?50+this.random()*250:0,work:-1,workLeft:0,job:front,pace:.6+this.random()*.45,bornAt:-this.random()*1800,lifespan:3600+this.random()*3600};
      });
      this.visits=new Array(this.nodes.length).fill(0);this.trail=new Array(this.nodes.length).fill(0);this.sample();
    }
    surfaceAt(x){return this.nodes[Math.max(0,Math.min(116,Math.round(x)-2))].y;}
    random(){let x=this.rng;x^=x<<13;x^=x>>>17;x^=x<<5;this.rng=x>>>0;return this.rng/4294967296;}
    node(x,y,parent,kind='tunnel'){const id=this.nodes.length;this.nodes.push({x,y,parent,kind});return id;}
    distances(target){const distance=new Array(this.nodes.length).fill(-1),queue=Array.isArray(target)?[...target]:[target];for(const n of queue)distance[n]=0;for(let start=0;start<queue.length;start++){const n=queue[start];for(const next of this.adj[n])if(distance[next]<0){distance[next]=distance[n]+1;queue.push(next);}}return distance;}
    rebuild(){this.adj=this.nodes.map(()=>[]);this.nodes.forEach((n,i)=>{if(n.parent!==null){this.adj[i].push(n.parent);this.adj[n.parent].push(i);}});for(const [a,b] of [...this.links,...this.junctions]){this.adj[a].push(b);this.adj[b].push(a);}this.distance=this.distances(this.nest);this.toExit=this.distances(this.exits);this.routes=this.fronts.map(f=>this.distances(f.node));}
    openFace(node,angle,goal=null){
      if(this.nodes.length>=MAX_NODES)return false;
      const occupied=new Set(this.ants.filter(a=>a.work>=0).map(a=>a.work));
      let slot=this.fronts.findIndex((f,i)=>f.blocked&&!occupied.has(i));
      if(slot<0){if(this.fronts.length>=12)return false;slot=this.fronts.length;}
      this.fronts[slot]={node,angle:(angle+Math.PI*2)%(Math.PI*2),effort:0,length:0,blocked:false,turn:0,branchAt:3+Math.floor(this.random()*6),goal};
      this.rebuild();return true;
    }
    seekFace(){
      // Reuse abandoned jobs; a finite list of old dead ends must not stop all growth.
      const candidates=this.nodes.map((n,i)=>i).filter(i=>this.nodes[i].kind!=='surface'&&this.nodes[i].y>this.surfaceAt(this.nodes[i].x)+4&&this.adj[i].length<=2&&!this.fronts.some(f=>!f.blocked&&f.node===i));
      for(let attempt=0;attempt<24&&candidates.length;attempt++){
        const i=candidates[Math.floor(this.random()*candidates.length)],n=this.nodes[i],p=this.nodes[n.parent];
        const goals=this.exits.length<4&&n.y<this.surfaceAt(n.x)+25?this.nodes.map((p,i)=>i).filter(j=>this.nodes[j].kind==='surface'&&Math.abs(this.nodes[j].x-n.x)>=12&&Math.abs(this.nodes[j].x-n.x)<=26&&this.exits.every(e=>Math.abs(this.nodes[j].x-this.nodes[e].x)>=10)):[];
        const goal=goals.length?goals[Math.floor(this.random()*goals.length)]:null;
        const angle=goal!==null?Math.atan2(this.nodes[goal].y-n.y,this.nodes[goal].x-n.x):Math.atan2(n.y-p.y,n.x-p.x)+(this.random()<.5?-1:1)*(1+this.random()*.7);
        if(this.openFace(i,angle,goal))return true;
      }
      return false;
    }
    lifecycle(){
      // The shared nest reserve represents food exchanged through the colony.
      // Life stages and starvation are compressed illustrative times, not species measurements.
      if(this.ticks%6000===0)this.foodReserve=Math.max(0,this.foodReserve-Math.ceil(this.ants.length/16));
      this.starvationSeconds=this.foodReserve>0?Math.max(0,this.starvationSeconds-8):Math.min(3600,this.starvationSeconds+1);
      const survivors=[];
      for(const ant of this.ants){
        const reason=this.starvationSeconds>=1200+(ant.id*137%1200)?'starvation':this.time-ant.bornAt>=ant.lifespan?'old age':null;
        if(reason){const from=this.nodes[ant.from],to=this.nodes[ant.cell];this.deaths++;if(reason==='starvation')this.starved++;this.recentDeaths.push({id:ant.id,at:this.time,age:Math.floor(this.time-ant.bornAt),reason,x:from.x+(to.x-from.x)*ant.phase,y:from.y+(to.y-from.y)*ant.phase,dir:ant.dir});}else survivors.push(ant);
      }
      this.ants=survivors;this.recentDeaths=this.recentDeaths.slice(-64);
      for(const egg of this.brood.filter(e=>e.ready<=this.time)){
        const id=this.nextAntId++,diggers=this.ants.filter(a=>a.role==='dig').length,role=diggers<Math.min(24,Math.ceil((this.ants.length+1)/5))?'dig':id%5===0?'rest':'forage';
        this.ants.push({id,cell:this.nest,from:this.nest,dir:this.random()*Math.PI*2,phase:1,carrying:0,role,steps:0,wait:1,work:-1,workLeft:0,job:id%this.fronts.length,pace:.6+this.random()*.45,bornAt:this.time,lifespan:3600+this.random()*3600});this.born++;
      }
      this.brood=this.brood.filter(e=>e.ready>this.time);
      if(this.ticks%300===0&&this.foodReserve>=8&&this.ants.length+this.brood.length<MAX_ANTS){this.foodReserve-=2;this.brood.push({ready:this.time+180});}
    }
    weighted(rows,weight){if(!rows.length)return null;let total=0;const weights=rows.map(row=>{const w=weight(row);total+=w;return w;});let n=this.random()*total;for(let i=0;i<rows.length;i++){n-=weights[i];if(n<=0)return rows[i];}return rows.at(-1);}
    extend(index){
      const front=this.fronts[index],from=this.nodes[front.node];if(this.nodes.length>=MAX_NODES){front.blocked=true;return;}
      if(front.goal!==null&&front.goal!==undefined)front.angle=(Math.atan2(this.nodes[front.goal].y-from.y,this.nodes[front.goal].x-from.x)+Math.PI*2)%(Math.PI*2);
      // A broad seeded soil tendency and persistent turn produce bends instead
      // of independent zigzags. Evaluated only when a segment is excavated.
      const soil=Math.sin(from.x*.13+(this.seed%997)) + Math.cos(from.y*.17-(this.seed%313));
      front.turn=Math.max(-.45,Math.min(.45,(front.turn||0)*.7+(this.random()-.5)*.35+soil*.08));
      front.branchAt ||= 4+Math.floor(this.random()*10);
      let chosen;
      for(const bend of [front.turn,...(this.random()<.5?[.4,-.4,.9,-.9,1.6,-1.6]:[-.4,.4,-.9,.9,-1.6,1.6])]){
        const angle=((front.angle+bend)%(Math.PI*2)+Math.PI*2)%(Math.PI*2),p={x:from.x+Math.cos(angle)*1.7,y:from.y+Math.sin(angle)*1.7};
        if(p.x<4||p.x>WIDTH-4||p.y<this.surfaceAt(p.x)-1||p.y>HEIGHT-5)continue;
        let surface=null,join=null;
        if(p.y<this.surfaceAt(p.x)+2){
          surface=Math.round(p.x)-2;
          if(this.exits.length>=16||this.exits.some(i=>Math.abs(this.nodes[i].x-p.x)<8))continue;
          p.x=this.nodes[surface].x;p.y=this.nodes[surface].y;
        }
        // Keep a soil wall between unrelated passages; attached ancestors are exempt.
        const near=new Set([front.node]);let ancestor=front.node;for(let k=0;k<3;k++){ancestor=this.nodes[ancestor]?.parent;if(ancestor!==null&&ancestor!==undefined)near.add(ancestor);}
        const collision=this.nodes.some((n,i)=>n.kind!=='surface'&&n.parent!==null&&!near.has(i)&&!near.has(n.parent)&&pointDistance(p,n,this.nodes[n.parent])<2.7);
        if(collision&&surface===null){
          join=this.nodes.findIndex((n,i)=>n.kind!=='surface'&&!near.has(i)&&!this.adj[front.node].includes(i)&&this.routes[index][i]>=5&&Math.hypot(n.x-p.x,n.y-p.y)<1.4&&Math.hypot(n.x-from.x,n.y-from.y)<=3.1);
          if(join>=0){p.x=this.nodes[join].x;p.y=this.nodes[join].y;chosen={p,angle,surface,join};break;}
        }
        if(!collision){chosen={p,angle,surface,join:null};break;}
      }
      if(!chosen){front.blocked=true;return;}
      const old=front.node;front.node=this.node(chosen.p.x,chosen.p.y,old,chosen.join!==null?'chamber':'tunnel');front.angle=chosen.angle;front.length++;front.effort=0;this.dug++;this.visits.push(0);this.trail.push(0);
      if(chosen.join!==null){this.junctions.push([front.node,chosen.join]);front.blocked=true;}
      if(chosen.surface!==null){this.links.push([front.node,chosen.surface]);this.exits.push(chosen.surface);front.blocked=true;}
      if(front.length>=front.branchAt){
        front.branchAt=front.length+4+Math.floor(this.random()*12);
        if(!front.blocked){
          let origin=old;for(let k=0,n=Math.floor(this.random()*3);k<n&&this.nodes[origin].parent!==null&&origin!==this.nest;k++)origin=this.nodes[origin].parent;
          const angle=((front.angle+(this.random()<.5?-1:1)*(.7+this.random()*.8))%(Math.PI*2)+Math.PI*2)%(Math.PI*2);
          this.openFace(origin,angle);
        }
      }
      this.rebuild();
    }
    step(){
      this.ticks++;this.time=this.ticks/10;
      if(this.ticks%10===0)this.lifecycle();
      if(this.ticks%300===0&&this.fronts.filter(f=>!f.blocked).length<12){this.seekFace();this.lastExpansion=this.time;}
      for(const ant of this.ants){
        const hungry=this.starvationSeconds>120,foraging=ant.role==='forage'||hungry;
        if(hungry&&ant.wait>3)ant.wait=3;
        if(ant.wait>0){ant.wait=Math.max(0,ant.wait-.1);continue;}
        if(ant.phase<1){const a=this.nodes[ant.from],b=this.nodes[ant.cell],tempo=.88+.12*Math.sin(this.time*3.1+ant.id*2.4);ant.phase=Math.min(1,ant.phase+.1*ant.pace*tempo*(this.starvationSeconds>600?.65:1)/(Math.hypot(b.x-a.x,b.y-a.y)||1)*(ant.carrying?.75:1));continue;}
        if(ant.work>=0){
          ant.workLeft-=.1;if(ant.workLeft>0)continue;
          const front=this.fronts[ant.work];front.effort=Math.min(PELLETS,front.effort+1);ant.carrying=2;
          if(front.effort>=PELLETS)this.extend(ant.work);
          ant.work=-1;ant.workLeft=0;ant.wait=.5+this.random();continue;
        }
        const current=this.nodes[ant.cell],neighbors=this.adj[ant.cell];
        if(ant.carrying===2&&this.exits.includes(ant.cell)){this.soilDelivered++;ant.carrying=0;ant.wait=1+this.random()*2;if(ant.role==='dig'&&this.random()<.5){const choices=this.fronts.map((f,i)=>i).filter(i=>!this.fronts[i].blocked);const job=this.weighted(choices,i=>1/(1+this.fronts[i].length/5));if(job!==null)ant.job=job;}continue;}
        if(ant.carrying===1&&ant.cell===this.nest){this.delivered++;this.foodReserve++;ant.carrying=0;ant.wait=1+this.random()*4;continue;}
        if(!ant.carrying&&foraging){const food=this.food.find(f=>f.left>0&&Math.hypot(f.x-current.x,f.y-current.y)<1.5);if(food){food.left--;ant.carrying=1;ant.wait=.7;continue;}}
        if(!ant.carrying&&ant.role==='dig'&&!hungry){
          let front=this.fronts[ant.job];if(!front||front.blocked){const choices=this.fronts.map((f,i)=>i).filter(i=>!this.fronts[i].blocked);if(!choices.length){ant.wait=30;continue;}ant.job=choices[Math.floor(this.random()*choices.length)];front=this.fronts[ant.job];}
          if(ant.cell===front.node){
            // At most two workers at one face; others give way instead of widening walls.
            if(this.ants.filter(a=>a.work===ant.job).length<2){ant.work=ant.job;ant.workLeft=WORK_SECONDS+this.random()*5;continue;}
            ant.wait=2+this.random()*4;
          }
        }
        let next;
        const route=ant.carrying===2?this.toExit:ant.carrying===1?this.distance:ant.role==='dig'&&!hungry?this.routes[ant.job]:current.kind!=='surface'?this.toExit:null;
        if(route)next=this.weighted(neighbors.filter(n=>route[n]<route[ant.cell]),()=>1);
        if(next===null||next===undefined){
          next=this.weighted(neighbors,n=>{const p=this.nodes[n],angle=Math.atan2(p.y-current.y,p.x-current.x),straight=1+Math.cos(angle-ant.dir)*.75;return straight*(current.kind==='surface'?1:1+this.trail[n]*2)/(1+this.visits[n]*.002);});
        }
        if(next===null)continue;
        const occupants=this.ants.filter(a=>a.cell===next&&a.phase<1).length;
        if(occupants>=2&&current.kind!=='surface'&&this.random()<.7){ant.wait=.5+this.random()*2;continue;}
        if(!ant.carrying&&!hungry&&this.random()<(ant.role==='rest'?.3:.07)){ant.wait=ant.role==='rest'?10+this.random()*40:.5+this.random()*2.5;continue;}
        const direction=Math.atan2(this.nodes[next].y-current.y,this.nodes[next].x-current.x),turn=Math.abs(Math.atan2(Math.sin(direction-ant.dir),Math.cos(direction-ant.dir)));
        ant.from=ant.cell;ant.cell=next;ant.phase=0;ant.steps++;ant.dir=direction;ant.wait=turn>.35?.12+turn*.16:0;this.visits[next]++;
        if(ant.carrying===1)this.trail[ant.from]=Math.min(12,this.trail[ant.from]+2);
      }
      if(this.ticks%10===0)this.trail=this.trail.map(n=>n*.99);
      if(this.time-this.lastSample>=10){this.sample();this.lastSample=this.time;}
    }
    sample(){const m=this.metrics();this.samples.push({seconds:m.seconds,dug:m.dug,delivered:m.delivered,explored:m.explored});if(this.samples.length>60)this.samples.shift();return m;}
    metrics(){const underground=this.nodes.map((n,i)=>n.kind==='surface'?null:i).filter(i=>i!==null);return {seconds:Math.floor(this.time),ants:this.ants.length,connections:this.junctions.length,born:this.born,deaths:this.deaths,starved:this.starved,hungry:this.starvationSeconds>120,starvation_seconds:this.starvationSeconds,brood:this.brood.length,entrances:this.exits.length,food_reserve:this.foodReserve,dug:this.dug,delivered:this.delivered,explored:underground.filter(i=>this.visits[i]>0).length,depth:Math.round(Math.max(...this.nodes.map(n=>n.y))-SURFACE),carrying_food:this.ants.filter(a=>a.carrying===1).length,carrying_soil:this.ants.filter(a=>a.carrying===2).length,food_remaining:this.food.reduce((n,f)=>n+f.left,0),busiest_visits:Math.max(0,...this.visits),total_visits:this.visits.reduce((n,v)=>n+v,0),soil_pellets:this.soilDelivered,active_diggers:this.ants.filter(a=>a.work>=0).length,resting:this.ants.filter(a=>a.wait>0).length,tunnel_tips:this.fronts.filter(f=>!f.blocked).length};}
    observation(){return {schema:'wake-ant-observation@1',seed:this.seed,model:MODEL,captured_at:new Date().toISOString(),metrics:this.metrics(),samples:this.samples.slice(-12),interventions:{food_added:this.addedFood},scope:'Local browser research-inspired simulation, not calibrated biology or WAKE research. Simulation rests offscreen.'};}
    addFood(){if(this.food.length>=32){const empty=this.food.findIndex(f=>!f.left);if(empty<0)return false;this.food.splice(empty,1);}this.food.push({x:8+Math.floor(this.random()*104),y:0,left:100});this.food.at(-1).y=this.surfaceAt(this.food.at(-1).x);this.addedFood+=100;return true;}
    save(){const result={schema:SCHEMA};for(const key of ['seed','rng','ticks','dug','delivered','soilDelivered','addedFood','nodes','fronts','nest','exit','initialNodes','visits','trail','ants','food','samples','lastSample','links','exits','nextAntId','born','deaths','foodReserve','brood','recentDeaths','lastExpansion','junctions','starvationSeconds','starved'])result[key]=this[key];return result;}
    static restore(v){
      const integer=(n,max)=>Number.isSafeInteger(n)&&n>=0&&n<=max,finite=(n,max)=>Number.isFinite(n)&&n>=0&&n<=max;
      if(!v||![SCHEMA,'wake-ant-colony@2'].includes(v.schema)||!integer(v.seed,4294967295)||!v.seed||!integer(v.rng,4294967295)||!integer(v.ticks,1e10)||!['dug','delivered','soilDelivered','addedFood','initialNodes'].every(k=>integer(v[k],1e9))||!finite(v.lastSample,v.ticks/10)||!Array.isArray(v.nodes)||v.nodes.length>MAX_NODES||v.nodes.length<130||v.nodes.length!==v.initialNodes+v.dug)throw Error('Invalid colony');
      if(v.nodes.some((n,i)=>!n||!finite(n.x,WIDTH)||!finite(n.y,HEIGHT)||!(n.parent===null&&i===0||integer(n.parent,i-1))||!['surface','tunnel','chamber'].includes(n.kind))||!integer(v.nest,v.nodes.length-1)||!integer(v.exit,v.nodes.length-1))throw Error('Invalid tunnels');
      if(v.nodes.slice(0,117).some((n,i)=>n.kind!=='surface'||n.x!==i+2||n.y<10||n.y>24||n.parent!==(i===0?null:i-1)))throw Error('Invalid soil surface');
      if(!Array.isArray(v.fronts)||!v.fronts.length||v.fronts.length>12||v.fronts.some(f=>!f||!integer(f.node,v.nodes.length-1)||('goal' in f&&f.goal!==null&&(!integer(f.goal,v.nodes.length-1)||v.nodes[f.goal].kind!=='surface'))||!finite(f.angle,Math.PI*2)||('turn' in f&&(!Number.isFinite(f.turn)||Math.abs(f.turn)>.45))||('branchAt' in f&&!integer(f.branchAt,MAX_NODES+20))||!integer(f.effort,PELLETS)||!integer(f.length,MAX_NODES)||typeof f.blocked!=='boolean'))throw Error('Invalid faces');
      for(const key of ['visits','trail'])if(!Array.isArray(v[key])||v[key].length!==v.nodes.length||v[key].some(n=>!finite(n,key==='trail'?12:1e10)))throw Error('Invalid traces');
      const legacy=v.schema==='wake-ant-colony@2';
      if(!Array.isArray(v.ants)||v.ants.length>MAX_ANTS||(legacy&&v.ants.length!==COUNT)||new Set(v.ants.map(a=>a?.id)).size!==v.ants.length||v.ants.some((a,i)=>!a||!integer(a.id,1e9)||(legacy&&a.id!==i)||!integer(a.cell,v.nodes.length-1)||!integer(a.from,v.nodes.length-1)||!Number.isFinite(a.dir)||!finite(a.phase,1)||!integer(a.carrying,2)||!['dig','forage','rest'].includes(a.role)||!integer(a.steps,1e10)||!finite(a.wait,1e4)||!finite(a.workLeft,20)||!(a.work===-1||integer(a.work,v.fronts.length-1))||!integer(a.job,v.fronts.length-1)||!finite(a.pace,2)||a.pace<.1))throw Error('Invalid ants');
      if(!Array.isArray(v.food)||v.food.length>32||v.food.some(f=>!f||!finite(f.x,WIDTH)||!finite(f.y,HEIGHT)||!integer(f.left,1000)))throw Error('Invalid food');
      if(!Array.isArray(v.samples)||!v.samples.length||v.samples.length>60||v.samples.some(s=>!s||!['seconds','dug','delivered','explored'].every(k=>integer(s[k],1e10))||s.seconds>v.ticks/10))throw Error('Invalid samples');
      v=structuredClone(v);
      if(legacy){
        Object.assign(v,{links:[],junctions:[],exits:[v.exit],nextAntId:COUNT,born:0,deaths:0,foodReserve:20,brood:[],recentDeaths:[],lastExpansion:v.ticks/10});
        for(const a of v.ants){a.bornAt=v.ticks/10-(a.id*71%1800);a.lifespan=3600+a.id*53%3600;}
      }
      v.starvationSeconds ??=0;v.starved ??=0;
      if(!integer(v.starvationSeconds,3600)||!integer(v.starved,v.deaths))throw Error('Invalid nutrition');
      if(!['nextAntId','born','deaths','foodReserve'].every(k=>integer(v[k],1e9))||v.nextAntId!==COUNT+v.born||v.ants.length!==COUNT+v.born-v.deaths||!finite(v.lastExpansion,v.ticks/10)||v.ants.some(a=>a.id>=v.nextAntId||!Number.isFinite(a.bornAt)||a.bornAt< -1800||a.bornAt>v.ticks/10||!finite(a.lifespan,7200)||a.lifespan<3600))throw Error('Invalid population');
      if(!Array.isArray(v.brood)||v.brood.length+v.ants.length>MAX_ANTS||v.brood.some(e=>!e||!Number.isFinite(e.ready)||e.ready<=v.ticks/10||e.ready>v.ticks/10+180))throw Error('Invalid brood');
      if(!Array.isArray(v.recentDeaths)||v.recentDeaths.length>64||v.recentDeaths.length>v.deaths||new Set(v.recentDeaths.map(a=>a?.id)).size!==v.recentDeaths.length||v.recentDeaths.some(a=>!a||!integer(a.id,v.nextAntId-1)||v.ants.some(live=>live.id===a.id)||!finite(a.at,v.ticks/10)||!integer(a.age,1e9)||!['old age','starvation'].includes(a.reason)||('x' in a&&(!finite(a.x,WIDTH)||!finite(a.y,HEIGHT)||!Number.isFinite(a.dir)))))throw Error('Invalid deaths');
      v.junctions ??=[];
      if(!Array.isArray(v.junctions)||v.junctions.length>MAX_NODES||v.junctions.some(e=>!Array.isArray(e)||e.length!==2||!integer(e[0],v.nodes.length-1)||!integer(e[1],e[0]-1)||v.nodes[e[0]].kind==='surface'||v.nodes[e[1]].kind==='surface'||Math.hypot(v.nodes[e[0]].x-v.nodes[e[1]].x,v.nodes[e[0]].y-v.nodes[e[1]].y)>.01)||new Set(v.junctions.map(e=>e[0])).size!==v.junctions.length)throw Error('Invalid junctions');
      if(!Array.isArray(v.exits)||!v.exits.length||v.exits.length>16||!v.exits.includes(v.exit)||new Set(v.exits).size!==v.exits.length||v.exits.some(i=>!integer(i,v.nodes.length-1)||v.nodes[i].kind!=='surface'))throw Error('Invalid entrances');
      if(!Array.isArray(v.links)||v.links.length!==v.exits.length-1||new Set(v.links.map(e=>JSON.stringify(e))).size!==v.links.length||v.links.some(e=>!Array.isArray(e)||e.length!==2||!integer(e[0],v.nodes.length-1)||!v.exits.includes(e[1])||e[1]===v.exit||v.nodes[e[0]].kind==='surface'||Math.hypot(v.nodes[e[0]].x-v.nodes[e[1]].x,v.nodes[e[0]].y-v.nodes[e[1]].y)>.01)||new Set(v.links.map(e=>e[1])).size!==v.links.length)throw Error('Invalid connections');
      const c=new Colony(v.seed);for(const key of Object.keys(c.save()))if(key!=='schema')c[key]=structuredClone(v[key]);c.time=c.ticks/10;c.rebuild();
      if(c.ants.some(a=>a.cell!==a.from&&!c.adj[a.from].includes(a.cell)))throw Error('Invalid ant route');
      return c;
    }
  }
  const api={Colony,WIDTH,HEIGHT,SURFACE,COUNT,MAX_ANTS,PELLETS,WORK_SECONDS};if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.WakeAntColony=api;
})(typeof globalThis!=='undefined'?globalThis:this);
