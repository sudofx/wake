/* Small Markdown subset. Only allowlisted DOM nodes; source HTML is always text. */
(function(root){
 'use strict';
 function inline(text,depth=0){
  if(depth>4)return [text];const result=[];let end=0;
  const tokens=/(\x60)([^\x60\n]+)\1|\*\*([^*]+)\*\*|__([^_]+)__|\*([^*\n]+)\*|_([^_\n]+)_|\[([^\]\n]+)\]\((https?:\/\/[^\s)]+)\)/g;
  for(const m of text.matchAll(tokens)){
   if(m.index>end)result.push(text.slice(end,m.index));
   const tag=m[2]?'code':m[3]||m[4]?'strong':m[5]||m[6]?'em':'a',value=m[2]||m[3]||m[4]||m[5]||m[6]||m[7];
   let href;if(tag==='a'){try{const u=new URL(m[8]);if(!['http:','https:'].includes(u.protocol))throw Error();href=u.href;}catch{result.push(m[0]);end=m.index+m[0].length;continue;}}
   result.push({tag,children:tag==='code'?[value]:inline(value,depth+1),...(href?{href}:{})});end=m.index+m[0].length;
  }
  if(end<text.length)result.push(text.slice(end));return result;
 }
 function parse(value){
  const lines=String(value).slice(0,12000).replace(/\r\n?/g,'\n').split('\n'),nodes=[];let i=0;
  const special=line=>/^\s*(?:\x60{3}|#{1,6}\s|>\s?|[-*+]\s|\d+[.)]\s)/.test(line);
  while(i<lines.length){
   if(!lines[i].trim()){i++;continue;}
   const fence=lines[i].match(/^\s*\x60{3}([\w+-]*)\s*$/);
   if(fence){i++;const code=[];while(i<lines.length&&!/^\s*\x60{3}\s*$/.test(lines[i]))code.push(lines[i++]);if(i<lines.length)i++;nodes.push({tag:'pre',children:[{tag:'code',children:[code.join('\n')]}]});continue;}
   const heading=lines[i].match(/^\s*(#{1,6})\s+(.+?)\s*#*$/);
   if(heading){nodes.push({tag:'h'+Math.min(6,heading[1].length+2),children:inline(heading[2])});i++;continue;}
   const list=lines[i].match(/^\s*(?:([-*+])|(\d+)[.)])\s+(.+)$/);
   if(list){const ordered=!!list[2],items=[];while(i<lines.length){const row=lines[i].match(/^\s*(?:([-*+])|(\d+)[.)])\s+(.+)$/);if(!row||!!row[2]!==ordered)break;items.push({tag:'li',children:inline(row[3])});i++;}nodes.push({tag:ordered?'ol':'ul',children:items});continue;}
   if(/^\s*>/.test(lines[i])){const quote=[];while(i<lines.length&&/^\s*>/.test(lines[i]))quote.push(lines[i++].replace(/^\s*>\s?/,''));nodes.push({tag:'blockquote',children:inline(quote.join('\n'))});continue;}
   const paragraph=[lines[i++]];while(i<lines.length&&lines[i].trim()&&!special(lines[i]))paragraph.push(lines[i++]);nodes.push({tag:'p',children:inline(paragraph.join('\n'))});
  }
  return nodes;
 }
 function render(container,text){
  const document=container.ownerDocument||root.document;
  function build(node){if(typeof node==='string')return document.createTextNode(node);const element=document.createElement(node.tag);if(node.href){element.setAttribute('href',node.href);element.setAttribute('target','_blank');element.setAttribute('rel','noopener noreferrer');}for(const child of node.children)element.append(build(child));return element;}
  container.replaceChildren(...parse(text).map(build));
 }
 const api={parse,render};if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.WakeBobMarkdown=api;
})(typeof globalThis!=='undefined'?globalThis:this);
