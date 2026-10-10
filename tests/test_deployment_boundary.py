"""Browser transports must never substitute another installation's record."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import unittest
from unittest.mock import patch

ASSETS = Path(__file__).resolve().parents[1] / 'wake' / 'assets'


@unittest.skipUnless(shutil.which('node'), 'Node required for browser transport execution')
class DeploymentBoundaryTests(unittest.TestCase):
    def test_actual_readers_require_explicit_hosted_identity_on_every_hostname(self):
        # Run the production loader bodies with observed HTTP requests. The LAN,
        # loopback and Pages hostnames must not choose an installation implicitly.
        program = r"""
const fs=require('node:fs'),vm=require('node:vm');
const root=process.argv[1], results=[];
for(const mode of ['standalone','hosted','missing','invalid']){
 for(const hostname of ['192.168.1.74','localhost','sudofx.github.io']){
  for(const reader of ['research','map','map3d']){
   const calls=[],source=fs.readFileSync(root+'/'+reader+'.js','utf8');
   const window=mode==='missing'?{}:{WAKE_DEPLOYMENT:{schema:1,mode}};
   const env={window,location:{hostname},Date,AbortSignal,
    fetch:async url=>{calls.push(url);return {ok:true,json:async()=>({})}},
    validate:()=>{throw Error('stop after selecting data')},notice:()=>{},
    freshness:()=>{},$:()=>({innerHTML:''})};
   let code;
   if(reader==='research'){
    code=source.slice(source.indexOf('  const deployment ='),source.indexOf('  let data,'))+
     'let loading=false,data=null,fallback=false;'+
     source.slice(source.indexOf('  async function json('),source.indexOf('  function validate('))+
     source.slice(source.indexOf('  async function refresh('),source.indexOf('  async function bootstrap('))+
     'refresh();';
   }else{
    const fn=reader==='map'?'loadMapData':'loadMap3dData';
    code=source.slice(source.indexOf('const LIVE_BASE='),source.indexOf('const data=await '+fn))+
     fn+'();';
   }
   await vm.runInNewContext(code,env);
   results.push({mode,hostname,reader,calls});
  }
 }
}
process.stdout.write(JSON.stringify(results));
"""
        result = subprocess.run(['node', '--input-type=commonjs', '-e',
                                 '(async()=>{' + program + '})().catch(e=>{console.error(e);process.exit(1)})',
                                 str(ASSETS)], text=True, capture_output=True, check=True)
        for row in json.loads(result.stdout):
            with self.subTest(**{k: row[k] for k in ('mode', 'hostname', 'reader')}):
                self.assertTrue(row['calls'])
                if row['mode'] == 'hosted':
                    self.assertTrue(row['calls'][0].startswith('https://raw.githubusercontent.com/'))
                else:
                    self.assertTrue(all(not url.startswith('http') for url in row['calls']))


class ExportIdentityTests(unittest.TestCase):
    def test_only_local_group_exports_carry_group_identity(self):
        import tempfile
        from wake.report import _deployment_site
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            env = {'WAKE_GROUP_ID': 'wake.local', 'WAKE_GROUP_INSTANCE': 'wake.local-001'}
            with patch.dict(os.environ, env, clear=True):
                _deployment_site(target, standalone=True)
            self.assertEqual(json.loads((target / 'deployment.json').read_text()), {
                'schema': 1, 'mode': 'standalone',
                'group': {'id': 'wake.local', 'instance': 'wake.local-001'},
            })
            with patch.dict(os.environ, {**env, 'CODESPACES': 'true'}, clear=True):
                _deployment_site(target, standalone=True)
            self.assertEqual(json.loads((target / 'deployment.json').read_text()), {
                'schema': 1, 'mode': 'standalone',
            })

    def test_default_export_is_local_and_keeps_the_original_record(self):
        import tempfile
        from wake.engine import DEFAULTS
        from wake.standalone import bootstrap
        from wake.report import export
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            engine = bootstrap(root / 'data', dict(DEFAULTS))
            try:
                head = engine.store.head()
                export(engine.store, root / 'site')
                identity = json.loads((root / 'site/deployment.json').read_text())
                self.assertEqual(identity, {'schema': 1, 'mode': 'standalone'})
                data = json.loads((root / 'site/research-data.json').read_text())
                self.assertEqual(data['source']['installation'], 'standalone')
                self.assertIsNone(data['source']['branch'])
                self.assertEqual(data['head'], head)
                self.assertEqual(engine.store.head(), head)
                for page in (root / 'site').rglob('*.html'):
                    content = page.read_text()
                    if '<head>' in content:
                        self.assertIn('window.WAKE_DEPLOYMENT', content)
                        self.assertIn('window.WAKE_STANDALONE=true', content)
                        self.assertLess(content.index('window.WAKE_DEPLOYMENT'),
                                        content.index('</head>'))
            finally:
                engine.store.close()

    def test_reexport_replaces_old_identity_instead_of_leaving_a_later_override(self):
        import tempfile
        from wake.report import _deployment_site
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / 'console.html'
            page.write_text('<head><script>window.WAKE_STANDALONE=true;</script></head>'
                            '<a href="/runtime.json">Inspect local WAKE runtime</a>')
            for local in (False, True, True, False):
                _deployment_site(root, standalone=local)
                text = page.read_text()
                self.assertEqual(text.count('window.WAKE_DEPLOYMENT='), 1)
                self.assertEqual(text.count('window.WAKE_STANDALONE='), 1)
                self.assertIn('"mode": "' + ('standalone' if local else 'hosted') + '"', text)
                self.assertIn('href="' + ('/runtime.json' if local else
                              'https://github.com/sudofx/wake/actions') + '"', text)
