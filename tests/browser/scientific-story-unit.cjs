'use strict';
const assert=require('node:assert/strict');
const {story,metrics}=require('../../wake/assets/scientific-research.js');
class Element {
 constructor(tag){this.tag=tag;this.children=[];this.textContent='';this.style={};this.attributes={};}
 append(...items){this.children.push(...items);}
 replaceChildren(...items){this.children=[...items];}
 setAttribute(k,v){this.attributes[k]=v;}
 set innerHTML(_){throw Error('Untrusted scientific evidence cannot be HTML');}
}
const doc={createElement:tag=>new Element(tag)};
const root=new Element('div');
const hostile='<img src=x onerror=alert(1)>';
story(doc,root,'100.wake',{id:'e1',question:hostile,hypothesis:{revisions:[{definition:{statement:hostile}}]},protocol:{revision:1},evaluation:{outcome:'contradicted',measurement_validity:'validated',predictions:[{satisfied:false}]},next_steps:[]});
const nodes=[];const walk=e=>{nodes.push(e);e.children.forEach(walk);};walk(root);
assert(nodes.some(e=>e.textContent===hostile));
assert(!nodes.some(e=>e.tag==='img'||e.tag==='script'));
assert(nodes.some(e=>typeof e.textContent==='string'&&e.textContent.includes('No subsequent decision')));
const cards=new Element('section'),chart=new Element('div');
metrics(doc,cards,[{data:{metrics:{falsifiable_hypotheses:3,completed_executions:2,valid_measurements:1}}}],chart);
assert.equal(cards.children.length,6);
assert.equal(chart.children.length,6);
assert(chart.attributes['aria-label'].includes('Falsifiable hypotheses 3'));
assert.equal(chart.children[0].children[1].children[0].style.width,'100.0%');
assert.equal(chart.children[1].children[1].children[0].style.width,'66.7%');
const empty=new Element('section'),emptyChart=new Element('div');
metrics(doc,empty,[],emptyChart);
assert.equal(empty.children[0].children[0].textContent,'0');
assert.equal(emptyChart.children[0].children[1].children[0].style.width,'0.0%');
console.log('Research narrative: untrusted text, recorded counts, proportional bars and empty states passed');
