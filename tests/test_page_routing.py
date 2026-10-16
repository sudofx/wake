"""Legacy reader links resolve within their installation before data loads."""
from pathlib import Path
import shutil
import subprocess
import unittest


@unittest.skipUnless(shutil.which('node'), 'Node required for reader routing')
class PageRoutingTests(unittest.TestCase):
    def test_old_deep_links_keep_pages_subpath_node_and_encoded_record(self):
        source = Path(__file__).parents[1] / 'wake/assets/page-routing.js'
        program = r'''
const vm=require('node:vm'),fs=require('node:fs'),assert=require('node:assert/strict');
const source=fs.readFileSync(process.argv[1],'utf8');
for(const prefix of ['/wake/','/wake/nodes/100.wake/']){
 let target,events={};
 const location={href:'https://example.test'+prefix+'index.html?inspection=1#blog/100.wake%3A%3Astory',hash:'#blog/100.wake%3A%3Astory',search:'?inspection=1',replace(value){target=value;}};
 const document={currentScript:{src:'https://example.test'+prefix+'page-routing.js'},documentElement:{dataset:{wakePage:'home'},style:{}},addEventListener(name,callback){events[name]=callback;}};
 vm.runInNewContext(source,{URL,location,document,window:{addEventListener(){}},MutationObserver:class{}});
 assert.equal(target,'https://example.test'+prefix+'blog.html?inspection=1#blog/100.wake%3A%3Astory');
 assert.equal(document.documentElement.style.visibility,'hidden');
 // Already canonical pages and ordinary in-document anchors never redirect.
 target=null;document.documentElement.dataset.wakePage='blog';location.hash='#blog/100.wake%3A%3Astory';
 vm.runInNewContext(source,{URL,location,document,window:{addEventListener(){}},MutationObserver:class{}});
 assert.equal(target,null);
 location.hash='#bob-reference-1';
 vm.runInNewContext(source,{URL,location,document,window:{addEventListener(){}},MutationObserver:class{}});
 assert.equal(target,null);
}
'''
        subprocess.run(['node', '-e', program, str(source)], check=True, capture_output=True, text=True)

    def test_departing_document_does_not_render_an_absent_section(self):
        source = Path(__file__).parents[1] / 'wake/assets/app.js'
        program = r'''
const vm=require('node:vm'),fs=require('node:fs');
const source=fs.readFileSync(process.argv[1],'utf8');
const route=source.slice(source.indexOf('  function route()'),source.indexOf("  $('evidence-search')"));
for(const [current,target] of [['home','blog'],['journal','home'],['blog','journal']]){
 const document={documentElement:{dataset:{wakePage:current}},querySelectorAll(){throw Error('Departing page tried to render another section');}};
 vm.runInNewContext(route+'route();',{document,location:{hash:'#'+target+'/existing-record'}});
}
'''
        subprocess.run(['node', '-e', program, str(source)], check=True, capture_output=True, text=True)
