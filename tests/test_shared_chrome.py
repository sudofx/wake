"""Generated page chrome stays portable and preference-only."""
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

from wake.engine import DEFAULTS, Engine
from wake.record_store import RecordStore
from wake.report import export, _reading_page, _deployment_site

ROOT = Path(__file__).resolve().parents[1]


class SharedChromeTests(unittest.TestCase):
    def test_full_and_fast_exports_share_assets_and_relative_reading_navigation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            store = RecordStore(root / 'data', initialize_empty=True)
            try:
                engine = Engine(root / 'data', dict(DEFAULTS), store=store)
                engine.initialize()
                head = store.head()
                for fast in (False, True):
                    site = root / ('fast' if fast else 'full')
                    export(store, site, browser_only=fast)
                    nested = site / 'notebooks' / 'read.html'
                    nested.parent.mkdir(exist_ok=True)
                    nested.write_text(_reading_page('Reading', 'Notebook', '<p>Readable text</p>', '../console.html'))
                    _deployment_site(site, standalone=True)
                    for path in site.rglob('*.html'):
                        page = path.read_text()
                        if '</head>' not in page:
                            continue
                        for asset in re.findall(r'(?:href|src)="([^"?]+)(?:\?[^\"]*)?"', page):
                            if asset.endswith(('masthead.css', 'site-theme.js')):
                                self.assertTrue((path.parent / asset).is_file(), (path, asset))
                        self.assertIn('data-theme="light"', page, path)
                        self.assertNotIn('data-theme="dark"', page, path)
                        self.assertEqual(page.count('site-theme.js?v='), 1, path)
                        self.assertEqual(page.count('masthead.css?v='), 1, path)
                        self.assertNotIn('console-theme.js', page)
                        self.assertNotIn("localStorage.setItem('wake-theme','dark')", page)
                        if '<header class="' in page:
                            self.assertIn('id="theme-toggle"', page)
                            self.assertNotIn('class="actions-light-label"', page)
                    self.assertIn('href="../index.html#journal"', nested.read_text())
                    self.assertIn('href="/runtime.json"', nested.read_text())
                    self.assertEqual(store.head(), head)
            finally:
                store.close()

    @unittest.skipUnless(shutil.which('node'), 'Node required for production theme controller')
    def test_theme_follows_detected_system_and_manual_fallback_handles_storage_failure(self):
        source = ROOT / 'wake/assets/site-theme.js'
        script = r'''
const vm=require('node:vm'),fs=require('node:fs'),assert=require('node:assert/strict');
const source=fs.readFileSync(process.argv[1],'utf8');
for(const denied of [false,true]){
 let saved={},events={},systemChange,choiceChange;
 const root={dataset:{},style:{}},label={dataset:{}},toggle={checked:false,setAttribute(k,v){this[k]=v},closest(){return label},addEventListener(k,v){choiceChange=v}};
 const media={matches:false,addEventListener(k,v){systemChange=v}};
 const lightMedia={matches:true,addEventListener(){}};
 const context={document:{documentElement:root,readyState:'complete',querySelector(){return null},querySelectorAll(){return []},getElementById(){return toggle}},matchMedia(query){return query.includes('dark')?media:lightMedia},localStorage:{getItem(k){if(denied)throw Error();return saved[k]},setItem(k,v){if(denied)throw Error();saved[k]=v}},CustomEvent:class{},window:{dispatchEvent(){},addEventListener(k,v){events[k]=v}}};
 vm.runInNewContext(source,context);
 assert.equal(root.dataset.theme,'light');assert.equal(label.hidden,true);
 lightMedia.matches=false;media.matches=true;systemChange();assert.equal(root.dataset.theme,'dark');
 toggle.checked=false;choiceChange({target:toggle});assert.equal(root.dataset.theme,'dark');
 systemChange();assert.equal(root.dataset.theme,'dark');
 assert.equal(toggle['aria-label'],'Use light theme');assert.match(label.dataset.uiTooltip,/Following system dark/);
 events.storage({key:'wake-site-theme',newValue:null});assert.equal(root.dataset.theme,'dark');
 // Devices without a theme API still get light and a working manual toggle.
 delete context.matchMedia;delete context.window.WakeTheme;
 vm.runInNewContext(source,context);assert.equal(root.dataset.theme,'light');assert.equal(label.hidden,false);
 toggle.checked=true;choiceChange({target:toggle});assert.equal(root.dataset.theme,'dark');
 if(!denied){
  delete context.window.WakeTheme;vm.runInNewContext(source,context);
  assert.equal(root.dataset.theme,'dark'); // A saved manual choice survives loading another page.
 }
}
'''
        subprocess.run(['node', '-e', script, str(source)], check=True, capture_output=True, text=True)


if __name__ == '__main__':
    unittest.main()
