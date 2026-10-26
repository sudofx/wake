import {readFile,writeFile} from 'node:fs/promises';
const root=new URL('../',import.meta.url);
const entry=await readFile(new URL('worker/index.js',root),'utf8');
let ui=await readFile(new URL('worker/chat.js',root),'utf8');
let markdown,tokens,icon;
try{icon=await readFile(new URL("../../wake/assets/icons/wake.svg",root),"utf8");}catch(error){if(error.code!=="ENOENT")throw error;icon=await readFile(new URL("worker/wake.svg",root),"utf8");}
if(icon.includes("`")||icon.includes("${")||!icon.includes('viewBox="0 0 512 512"'))throw Error("Invalid canonical icon");
try{markdown=await readFile(new URL('../../wake/assets/bob-markdown.js',root),'utf8');tokens=await readFile(new URL('../../wake/assets/theme.css',root),'utf8');}catch(error){if(error.code!=='ENOENT')throw error;markdown=await readFile(new URL('worker/bob-markdown.js',root),'utf8');tokens=await readFile(new URL('worker/theme-tokens.css',root),'utf8');}
tokens=tokens.slice(0,tokens.indexOf('/* Shared signal language:')<0?tokens.length:tokens.indexOf('/* Shared signal language:'));
if(markdown.includes('`')||markdown.includes('${'))throw Error('Inline formatter must be raw-template safe');
ui=ui.replace('/* BOB_MARKDOWN */',markdown).replace('/* BOB_THEME_TOKENS */',tokens).replace('<!-- BOB_ICON -->',icon);
const seam="import {CHAT_HTML} from './chat.js';";
if(!entry.includes(seam))throw Error('Missing chat module seam');
await writeFile(new URL('dist/server/index.js',root),entry.replace(seam,ui.replace('export const CHAT_HTML','const CHAT_HTML')));
