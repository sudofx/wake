const test=require('node:test'),assert=require('node:assert/strict'),{parse,render}=require('../../wake/assets/bob-markdown.js');
const tags=nodes=>nodes.flatMap(n=>typeof n==='string'?[]:[n.tag,...tags(n.children)]);
test('headings, bold, emphasis, lists and fenced Python become structured content',()=>{
 const result=parse('### A heading\n\n**Bold** and *italic* and `inline`.\n\n- First\n- Second\n\n1. One\n2. Two\n\n```python\nprint("Hello")\n```');
 for(const tag of ['h5','strong','em','ul','ol','li','pre','code'])assert.ok(tags(result).includes(tag),tag);
 assert.ok(JSON.stringify(result).includes('print(\\"Hello\\")'));
});
test('HTML, malicious links and unfinished streamed fences cannot create active nodes',()=>{
 const result=parse('<img src=x onerror=alert(1)>\n\n**safe** [bad](javascript:alert(1)) [good](https://example.com)\n\n```html\n<script>alert(1)</script>');
 assert.ok(!tags(result).some(t=>['img','script','iframe','style'].includes(t)));assert.equal(tags(result).filter(t=>t==='a').length,1);assert.ok(JSON.stringify(result).includes('<script>'));
});
test('DOM rendering uses text nodes and safe attributes, never source HTML',()=>{
 const doc={createElement:tag=>({tag,children:[],attrs:{},append(n){this.children.push(n);},setAttribute(k,v){this.attrs[k]=v;},set innerHTML(v){throw Error('HTML injection');}}),createTextNode:text=>({text})};
 const container={ownerDocument:doc,replaceChildren(...nodes){this.nodes=nodes;}};render(container,'**Hi** <svg onload=evil()> [link](https://example.com)');
 assert.equal(container.nodes[0].children[0].tag,'strong');const link=container.nodes[0].children.find(n=>n.tag==='a');assert.equal(link.attrs.rel,'noopener noreferrer');assert.equal(link.attrs.target,'_blank');
});
