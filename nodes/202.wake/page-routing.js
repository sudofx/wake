/* Separate static reader documents; old shared links remain valid on Pages. */
(() => {
  'use strict';
  const pages={home:'index.html',discoveries:'research.html',topics:'topics.html',blog:'blog.html',projects:'projects.html',journal:'journal.html',lab:'lab.html',metrics:'metrics.html',evidence:'evidence.html',history:'history.html',about:'about.html'};
  const script=document.currentScript;
  const root=new URL('.',script.src);
  const current=document.documentElement.dataset.wakePage;
  const redirect=()=>{
    if(!current)return;
    const section=location.hash.slice(1).split('/')[0];
    if(pages[section] && section!==current){
      const url=new URL(pages[section],root);url.search=location.search;
      if(location.hash.includes('/'))url.hash=location.hash;
      document.documentElement.style.visibility='hidden';
      location.replace(url.href);
    }
  };
  redirect();
  window.addEventListener('hashchange',redirect);
  const rewrite=container=>{
    const links=container.matches?.('a[href]')?[container]:container.querySelectorAll?.('a[href]')||[];
    for(const link of links){
      let url;try{url=new URL(link.getAttribute('href'),location.href);}catch{continue;}
      if(url.origin!==location.origin || !url.hash)continue;
      const route=url.hash.slice(1),section=route.split('/')[0];
      if(!pages[section] || !/\/(?:index\.html)?$/.test(url.pathname) && !Object.values(pages).some(page=>url.pathname.endsWith('/'+page)))continue;
      const filename=pages[section];
      url.pathname=url.pathname.slice(0,url.pathname.lastIndexOf('/')+1)+filename;
      if(!route.includes('/'))url.hash='';
      if(link.href!==url.href)link.href=url.href;
    }
  };
  document.addEventListener('DOMContentLoaded',()=>{
    rewrite(document);
    new MutationObserver(records=>{for(const record of records){if(record.type==='attributes')rewrite(record.target);else for(const node of record.addedNodes)if(node.nodeType===1)rewrite(node);}}).observe(document.body,{childList:true,subtree:true,attributes:true,attributeFilter:['href']});
  });
})();
