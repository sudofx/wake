/* Acceptance gates cover morphology and timing, not just connected growth. */
const test=require('node:test'),assert=require('node:assert/strict');
const {Colony,PELLETS}=require('../../wake/assets/ant-colony.js');
test('excavation lengthens narrow tunnels instead of erasing an area',()=>{
 for(const seed of [1,42,20261024]){
  const c=new Colony(seed),initialFood=c.metrics().food_remaining;
  for(let i=0;i<18000;i++)c.step();
  const m=c.metrics();assert.ok(m.dug>=9);assert.ok(m.dug<80,'Real-time excavation must stay gradual');assert.ok(m.delivered>0);
  assert.equal(c.nodes.length-c.initialNodes,c.dug);assert.equal(m.food_remaining+m.delivered+m.carrying_food,initialFood);
  assert.ok(m.active_diggers<=12);assert.ok(c.nodes.every((n,i)=>i===0||n.parent<i));assert.ok(c.distance.every(d=>d>=0));
  // New pieces have one parent, fixed length, and no excavated wide chamber.
  for(let i=c.initialNodes;i<c.nodes.length;i++){const n=c.nodes[i],p=c.nodes[n.parent];assert.equal(n.kind,'tunnel');assert.ok(Math.abs(Math.hypot(n.x-p.x,n.y-p.y)-1.7)<1e-9);}
  const incomplete=c.fronts.reduce((n,f)=>n+f.effort,0),carried=m.carrying_soil;
  assert.ok(m.soil_pellets+carried>=m.dug*PELLETS);assert.ok(m.soil_pellets+carried<=m.dug*PELLETS+incomplete+12);
  assert.equal(c.samples.length,60);
 }
});
test('normal-time movement has a bounded pace, pauses, and sustained work at the face',()=>{
 const c=new Colony(42);for(let i=0;i<100;i++)c.step();
 assert.equal(c.dug,0,'Ten seconds must not excavate entire tunnel segments');
 assert.ok(c.ants.every(a=>a.steps<=12));assert.ok(c.ants.some(a=>a.wait>0));assert.ok(c.ants.some(a=>a.work>=0||a.carrying===2));
 assert.equal(c.time,10);
});
test('saved progress resumes exactly without adding offscreen time',()=>{
 const a=new Colony(7331);for(let i=0;i<1234;i++)a.step();const b=Colony.restore(JSON.parse(JSON.stringify(a.save())));assert.equal(b.time,123.4);
 for(let i=0;i<300;i++){a.step();b.step();}assert.deepEqual(a.save(),b.save());
});
test('malformed saves fail closed',()=>{
 const source=new Colony(2).save();for(const mutate of [s=>s.nodes[1].parent=1,s=>s.trail[0]=NaN,s=>s.ants[0].cell=1e9,s=>s.ants[0].carrying=99,s=>s.dug++,s=>s.ticks=-1,s=>s.lastSample=Infinity,s=>s.samples[0].seconds=100,s=>s.food[0].left=-1]){const v=structuredClone(source);mutate(v);assert.throws(()=>Colony.restore(v));}
});
test('food interventions are bounded, measured, and do not destroy existing food',()=>{
 const c=new Colony(3),before=c.metrics().food_remaining;for(let i=0;i<100;i++)c.addFood();assert.equal(c.food.length,32);assert.equal(c.metrics().food_remaining,before+c.addedFood);
 assert.equal(c.observation().interventions.food_added,c.addedFood);assert.equal(c.observation().model,'pellet-tunnels@5');assert.ok(c.observation().samples.length<=12);
});

test('seeds vary initial shafts and branch layouts while keeping deterministic saves',()=>{
 const layouts=new Set(),exits=new Set(),depths=new Set(),counts=new Set();
 for(let seed=1;seed<=32;seed++){
  const c=new Colony(seed),same=new Colony(seed);assert.deepEqual(c.save(),same.save());
  layouts.add(JSON.stringify(c.nodes));exits.add(c.exit);depths.add(c.nodes[c.nest].y.toFixed(1));counts.add(c.fronts.length);
  assert.ok(c.distance.every(d=>d>=0));assert.deepEqual(Colony.restore(c.save()).save(),c.save());
 }
 assert.equal(layouts.size,32);assert.ok(exits.size>=12);assert.ok(depths.size>=12);assert.equal(counts.size,4);
});
test('excavation can turn laterally and upward without rewriting starter tunnels',()=>{
 let upward=false,lateral=false;
 for(const seed of [1,2,3,4,5,6,7,8]){
  const c=new Colony(seed),initial=structuredClone(c.nodes);
  for(let i=0;i<18000;i++)c.step();
  assert.deepEqual(c.nodes.slice(0,initial.length),initial);
  for(const n of c.nodes.slice(initial.length)){
   const p=c.nodes[n.parent];upward ||= n.y<p.y;lateral ||= Math.abs(n.x-p.x)>Math.abs(n.y-p.y);
   assert.ok(n.y>=13+1&&n.y<=96-5);
  }
 }
 assert.ok(upward,'Some seeded excavation should return upward within the ground');assert.ok(lateral);
});
