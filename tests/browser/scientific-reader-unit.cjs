'use strict';
// No browser or network: isolated transport and safe-DOM contract checks.
const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const {loadReports,renderRecord}=require('../../wake/assets/scientific-research.js');
const ids=[100,101,102,103,200,201,202,203,300,301,302,303].map(n=>n+'.wake');
const head='a'.repeat(64),revision='b'.repeat(40);
const manifest={schema:1,live:false,installation_id:'fixture',nodes:ids.map(id=>({id,available:true})),
  record_heads:Object.fromEntries(ids.map(id=>[id,{head}]))};
const report={schema:'wake-scientific-audit@1',source:{head},investigations:[{id:'same-local-id'}]};
(async()=>{
  let active=0,maximum=0;const reads=[];
  const loaded=await loadReports(async path=>{
    reads.push(path);if(path==='installation.json')return manifest;
    active++;maximum=Math.max(maximum,active);await Promise.resolve();active--;
    if(path.includes('100.wake'))return report;
    if(path.includes('101.wake'))return {...report,source:{head:'mismatched'}};
    if(path.includes('102.wake'))return report;
    return null;
  });
  assert.equal(maximum,3);assert.equal(loaded.reports.length,2);assert.equal(loaded.unavailable.length,1);
  assert.deepEqual(loaded.reports.map(r=>r.node),['100.wake','102.wake']);
  assert.equal(loaded.absent.length,9);
  assert.equal(loaded.reports[0].data.investigations[0].id,loaded.reports[1].data.investigations[0].id);
  assert.equal(reads.length,13);
  await assert.rejects(loadReports(async()=>({...manifest,nodes:[{id:'https://untrusted.invalid'}]})),/Invalid installation/);
  const single=await loadReports(async path=>path==='installation.json'?null:report);
  assert.equal(single.reports.length,1);
  const scopedReads=[];
  const scoped=await loadReports(async path=>{
    scopedReads.push(path);return path==='../../installation.json'?manifest:report;
  },{node:'101.wake'});
  assert.deepEqual(scoped.reports.map(r=>r.node),['101.wake']);
  assert.deepEqual(scopedReads,['../../installation.json','../../nodes/101.wake/scientific-research.json']);
  const missing=await loadReports(async path=>path==='installation.json'?manifest:null);
  assert.equal(missing.reports.length,0);assert.equal(missing.absent.length,12);
  await assert.rejects(loadReports(async()=>null,{node:'100.wake'}),/snapshot unavailable/);
  await assert.rejects(loadReports(async()=>{throw Error('Selected snapshot unavailable');}),/Selected snapshot unavailable/);
  class Element{
    constructor(tag){this.tag=tag;this.children=[];this.textContent='';}
    append(...children){this.children.push(...children);}
    set innerHTML(_){throw Error('Untrusted audit content must never become HTML');}
  }
  const root=new Element('main'),doc={createElement:tag=>new Element(tag)};
  const hostile='<img src=x onerror="alert(1)">';
  renderRecord(doc,root,'100.wake',{id:hostile,question:hostile,protocol:{source:hostile}});
  const nodes=[];const walk=n=>{nodes.push(n);n.children.forEach(walk);};walk(root);
  assert(nodes.some(n=>n.tag==='pre'&&n.textContent.includes('<img')&&n.textContent.includes('alert(1)')));
  assert(!nodes.some(n=>n.tag==='img'||n.tag==='script'));
  // Exercise the real public transport with only fake responses. New audit
  // data must resolve through the same selected immutable commit as readers.
  const location=new URL('https://sudofx.github.io/wake/scientific-research.html?public_revision='+revision);
  const calls=[],window={WAKE_DEPLOYMENT:{snapshot_only:true,public_data:{repository:'sudofx/wake',branch:'wake-public',installation_id:'fixture'}}};
  window.parent=window;
  const context={window,location,URL,AbortSignal,TextDecoder,Uint8Array,Date,JSON,
    localStorage:{getItem:()=>null,setItem(){}},
    document:{currentScript:{src:'https://sudofx.github.io/wake/public-data.js'},readyState:'loading',addEventListener(){}},
    fetch:async url=>{calls.push(String(url));return new Response(JSON.stringify(String(url).endsWith('installation.json')?manifest:report));}};
  vm.runInNewContext(fs.readFileSync('wake/assets/public-data.js','utf8'),context);
  const transport=window.WakePublicData;await transport.ready;
  await transport.fetch('scientific-research.json');await transport.fetch('nodes/101.wake/scientific-research.json');
  assert(calls.every(url=>url.startsWith('https://raw.githubusercontent.com/sudofx/wake/'+revision+'/')));
  await assert.rejects(transport.fetch('https://untrusted.invalid/report.json'),/must belong/);
  assert.equal(transport.revision,revision);
  console.log('Scientific reader: pinned data, node provenance, bounded concurrency and safe text rendering passed');
})().catch(error=>{console.error(error);process.exitCode=1;});
