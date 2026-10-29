/* Offline instrument checks. These do not establish rendered browser usability. */
const {test}=require('node:test'),assert=require('node:assert/strict');
const e=require('../../wake/assets/ant-experiment.js');
function finish(run){while(!e.advance(run,97)){}return e.measure(run);}
test('paired intervention changes only food location and counts actual conserved deliveries',()=>{
  const run=e.setup(481),[near,far]=run.arms;
  const a=structuredClone(near.save()),b=structuredClone(far.save());
  assert.notDeepEqual(a.food,b.food);delete a.food;delete b.food;assert.deepEqual(a,b);
  assert.equal(near.food.reduce((n,f)=>n+f.left,0),100);
  assert.deepEqual(near.food.map(f=>[f.kind,f.left]),far.food.map(f=>[f.kind,f.left]));
  const result=finish(run);
  assert.equal(result.measurements.near.delivered,30);assert.equal(result.measurements.far.delivered,0);
  assert.equal(result.outcome,'near');assert.equal(e.evaluate(result,'near'),'supported');assert.equal(e.evaluate(result,'far'),'contradicted');
});
test('same seed reproduces exact results independent of scheduling chunks',()=>{
  const a=finish(e.setup(481)),run=e.setup(481);e.advance(run,1800);
  assert.deepEqual(a,e.measure(run));assert.deepEqual(finish(e.setup(77)),finish(e.setup(77)));
});
test('a delayed-worker scenario can produce a genuinely inconclusive measurement',()=>{
  const run=e.setup(481);
  // The real simulation still runs. This explicit test-only intervention delays
  // the initial workers; task allocation may release nurses. It is not UI data.
  for(const arm of run.arms)for(const ant of arm.ants)ant.wait=1000;
  const result=finish(run);
  assert.equal(result.measurements.near.delivered,1);assert.equal(result.measurements.far.delivered,0);
  assert.equal(e.evaluate(result,'near'),'inconclusive');assert.equal(e.evaluate(result,'similar'),'matched-small-difference');
});
test('visitor flow freezes choices, cancels stale work, and touches no storage or network',()=>{
  const vm=require('node:vm'),fs=require('node:fs');
  const nodes=new Map(),timers=[],handlers={};
  const input={value:'near',disabled:false,focus(){this.focused=true;}},seed={value:'481',disabled:false,focus(){this.focused=true;}};
  const controls=[input,seed,{disabled:false}];
  function get(id){if(!nodes.has(id))nodes.set(id,{hidden:false,textContent:'',value:0,disabled:false,events:{},addEventListener(k,fn){this.events[k]=fn;},focus(){this.focused=true;},scrollIntoView(){this.scrolled=true;}});return nodes.get(id);}
  const form=get('prediction-form');form.querySelectorAll=()=>controls;form.querySelector=()=>input;
  nodes.set('experiment-seed',seed);
  const context={WakeAntColony:require('../../wake/assets/ant-colony.js'),document:{getElementById:get,querySelectorAll:()=>[]},setTimeout:fn=>timers.push(fn),addEventListener:(k,fn)=>handlers[k]=fn};
  for(const name of ['fetch','localStorage','sessionStorage'])Object.defineProperty(context,name,{get(){throw Error('Forbidden '+name);}});
  vm.runInNewContext(fs.readFileSync(require.resolve('../../wake/assets/ant-experiment.js'),'utf8'),context);
  const submit=()=>form.events.submit({preventDefault(){}});
  submit();assert(controls.every(c=>c.disabled));assert.equal(timers.length,1);
  submit();assert.equal(timers.length,1,'duplicate clicks do not start another run');
  get('stop-test').events.click();while(timers.length)timers.shift()();
  assert.match(get('experiment-status').textContent,/Stopped/);assert.equal(get('result').hidden,true);assert(controls.every(c=>!c.disabled));
  submit();input.value='far';while(timers.length)timers.shift()();
  assert.equal(get('frozen-prediction').textContent,e.predictions.near,'the selected prediction is captured before execution');
  assert.match(get('result-title').textContent,/supported/);assert.equal(get('near-result').textContent,'30');
  get('save-result').events.click();assert.match(get('result-text').textContent,/30 food units/);assert(!get('result-text').textContent.includes('presentation_revision'));
  const receipt=JSON.parse(get('technical-result').textContent);assert.equal(receipt.prediction,e.predictions.near);assert.equal(receipt.presentation_revision,null);
  seed.value='-1';submit();assert.match(get('experiment-status').textContent,/whole-number/);assert.equal(timers.length,0);
  seed.value='481';submit();handlers.pagehide();while(timers.length)timers.shift()();assert.equal(get('result').hidden,true);
});
test('missing, unfinished and corrupt evidence cannot become a result',()=>{
  assert.throws(()=>e.setup(0));assert.throws(()=>e.setup(1.5));assert.throws(()=>e.setup(4294967296));
  const run=e.setup(481);assert.throws(()=>e.measure(run),/not completed/);
  finish(run);run.arms[0].delivered++;assert.throws(()=>e.measure(run),/inconsistent/);
  run.arms[0].delivered=NaN;assert.throws(()=>e.measure(run),/inconsistent/);
  assert.throws(()=>e.evaluate({outcome:'near'},'unknown'),/prediction/);
});
