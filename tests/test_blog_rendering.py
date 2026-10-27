"""A shared article remains readable without the leader's invocation locally."""
import json
from pathlib import Path
import shutil
import subprocess
import unittest

ASSETS=Path(__file__).resolve().parents[1]/'wake'/'assets'

@unittest.skipUnless(shutil.which('node'), 'Node required for browser rendering execution')
class BlogRenderingTests(unittest.TestCase):
    def test_missing_leader_invocation_renders_list_topic_and_reading_views(self):
        program=r'''
const fs=require('node:fs'),vm=require('node:vm');
const source=fs.readFileSync(process.argv[1]+'/app.js','utf8');
const helpers=source.slice(source.indexOf('  const postResearchTopic='),source.indexOf('  const proofNames ='));
const render=source.slice(source.indexOf('  let farmNotebookRuntime;'),source.indexOf('  function evidence('));
const results=[];
for(const mode of ['shared','ordinary','no-time']){
 const post={id:'group-introduction',title:'Welcome',lede:'Hello',body:'A shared article.\n\nSummary\n\nPlain words.',created_version:0,created_by:'leader-invocation',notebooks:[],evidence:[],group_publication:{members:['100.wake','101.wake']}};
 if(mode==='shared'){post.published_at='2026-10-11T21:20:24Z';post.editorial_references=[[{member:'100.wake',title:'A dated notebook',revision:2,record_url:'/nodes/100.wake/index.html#projects/notebook:n'}]];}
 const s={projects:{},notebooks:{},invocations:mode==='ordinary'?{'leader-invocation':{time:'2026-10-11T21:20:23Z'}}:{}};
 const nodes={'blog-content':{innerHTML:''},blog:{classList:{toggle(){}}}};
 const env={queueMicrotask:()=>{},window:{location:{pathname:'/wake/index.html'}},s,posts:[post],data:{groupBobMembers:['100.wake','101.wake']},$:id=>nodes[id],esc:v=>String(v??''),fmt:v=>v,badge:(status,label)=>label,topicTag:()=>'',topicLabel:v=>v,canonicalTopic:v=>v,blogText:v=>v,encodeURIComponent};
 vm.createContext(env);
 for(const route of ['', 'topic:reflection','group-introduction']){
  vm.runInContext(helpers+render+'blog('+JSON.stringify(route)+');',vm.createContext({...env}));
  const html=nodes['blog-content'].innerHTML;
  if(!html.includes('Welcome'))throw Error('Article missing in '+mode+' '+route);
  if(mode==='shared'&&route==='group-introduction'&&(!html.includes('/wake/nodes/100.wake/index.html')||!html.includes('<h3>Summary</h3>')))throw Error('Attribution or Summary missing');
  if(mode==='shared'&&!html.includes(post.published_at))throw Error('Publication time missing');
  if(mode==='ordinary'&&!html.includes('2026-10-11T21:20:23Z'))throw Error('Invocation time missing');
  if(mode==='no-time'&&!html.includes('Publication time unavailable'))throw Error('Unavailable time fabricated');
  results.push({mode,route});
 }
}
process.stdout.write(JSON.stringify(results));
'''
        result=subprocess.run(['node','-e',program,str(ASSETS)],capture_output=True,text=True,check=True)
        self.assertEqual(len(json.loads(result.stdout)),9)
