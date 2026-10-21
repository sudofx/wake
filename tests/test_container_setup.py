"""Installer ownership, record compatibility and replacement ordering."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import tarfile
import unittest
from unittest.mock import patch

from support import charter_settings
from wake.authority import open_authoritative_store
from wake.engine import Engine
from wake.installation_cli import NODE_IDS
from wake.upgrade import check_upgrade

ROOT = Path(__file__).resolve().parents[1]


class UpgradeCheckTests(unittest.TestCase):
    def test_audit_uses_copies_and_rejects_an_incomplete_installation(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            record = root / 'nodes' / NODE_IDS[0] / 'record'
            engine = Engine(record, charter_settings('Explore bounded questions'),
                            store=open_authoritative_store(record, allow_initialize=True))
            engine.initialize()
            engine.store.close()
            before = (record / 'wake.sqlite').read_bytes()
            with self.assertRaises(ValueError):
                check_upgrade(root)
            for node in NODE_IDS[1:]:
                target = root / 'nodes' / node / 'record'
                target.mkdir(parents=True)
                shutil.copyfile(record / 'wake.sqlite', target / 'wake.sqlite')
            self.assertEqual(check_upgrade(root), 12)
            with patch('wake.upgrade.verify_recovery', side_effect=ValueError('unsupported record')):
                with self.assertRaises(ValueError):
                    check_upgrade(root)
            self.assertEqual((record / 'wake.sqlite').read_bytes(), before)


class LauncherTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / 'scripts').mkdir()
        shutil.copyfile(ROOT / 'scripts/wake_installation', self.root / 'scripts/wake_installation')
        self.bin = self.root / 'bin'
        self.bin.mkdir()
        self.log = self.root / 'calls.jsonl'
        fake = self.bin / 'docker'
        fake.write_text('''#!/usr/bin/env python3
import json,os,sys
args=sys.argv[1:]
with open(os.environ['CALLS'],'a') as log: log.write(json.dumps(args)+'\\n')
if args[:2]==['container','inspect']: sys.exit(0 if os.environ.get('EXISTS','1')=='1' else 1)
if args[:2]==['image','inspect']: sys.exit(0 if os.environ.get('IMAGE_EXISTS','1')=='1' else 1)
if args and args[0]=='inspect':
    template=' '.join(args)
    if '.Config.Labels' in template: print(os.environ.get('OWNER','true'))
    elif '.Destination "/workspace"' in template: print(os.environ['CHECKOUT'])
    elif '.Destination "/data"' in template: print(os.environ['CHECKOUT']+'/data/installation')
    elif '.State.Running' in template: print('true')
    elif 'PortBindings' in template: print('8095')
if 'wake.upgrade' in args: sys.exit(int(os.environ.get('AUDIT_FAILURE','0')))
sys.exit(0)
''')
        fake.chmod(0o755)
        self.env = {**os.environ, 'PATH': str(self.bin) + os.pathsep + os.environ['PATH'],
                    'CALLS': str(self.log), 'CHECKOUT': str(self.root)}
        self.env.pop('WAKE_PORT', None)

    def tearDown(self):
        self.temp.cleanup()

    def run_launcher(self, action, **env):
        result = subprocess.run(['sh', str(self.root / 'scripts/wake_installation'), action],
                                cwd=self.root, env={**self.env, **env}, capture_output=True, text=True)
        calls = [json.loads(line) for line in self.log.read_text().splitlines()]
        return result, calls

    def test_bootstrap_discovers_existing_source_from_another_directory(self):
        result = subprocess.run(['sh', str(ROOT / 'container_setup.sh')], cwd=self.bin,
                                env=self.env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        calls = [json.loads(line) for line in self.log.read_text().splitlines()]
        self.assertFalse(any(c[0] in ('build', 'run', 'stop', 'rename') for c in calls))

    def test_bootstrap_downloads_into_a_new_path_with_spaces(self):
        archive = self.root / 'source.tar.gz'
        with tarfile.open(archive, 'w:gz') as bundle:
            bundle.add(self.root / 'scripts/wake_installation',
                       arcname='wake-master/scripts/wake_installation')
        curl = self.bin / 'curl'
        curl.write_text("#!/usr/bin/env python3\nimport os,shutil,sys\nshutil.copyfile(os.environ['SOURCE_ARCHIVE'],sys.argv[sys.argv.index('-o')+1])\n")
        curl.chmod(0o755)
        target = self.root / 'new installation'
        result = subprocess.run(['sh', str(ROOT / 'container_setup.sh')], cwd=self.bin,
                                env={**self.env, 'EXISTS': '0', 'SOURCE_ARCHIVE': str(archive),
                                     'WAKE_INSTALL_DIR': str(target)}, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((target / 'scripts/wake_installation').is_file())
        calls = [json.loads(line) for line in self.log.read_text().splitlines()]
        create = next(c for c in calls if '--name' in c)
        self.assertIn(f'type=bind,source={target},target=/workspace',create)

    def test_new_container_builds_when_image_is_missing(self):
        result, calls = self.run_launcher('start', EXISTS='0', IMAGE_EXISTS='0')
        self.assertEqual(result.returncode, 0, result.stderr)
        build = next(i for i,c in enumerate(calls) if c[0]=='build')
        create = next(i for i,c in enumerate(calls) if '--name' in c)
        self.assertLess(build, create)
        self.assertIn('8080:8080', calls[create])
        self.assertFalse(any(c[0] in ('rm','volume') for c in calls))

    def test_running_container_is_reused_without_build_stop_or_research_control(self):
        result, calls = self.run_launcher('start')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(any(c[0] in ('build', 'run', 'stop', 'rename', 'exec') for c in calls))

    def test_foreign_container_is_never_changed(self):
        result, calls = self.run_launcher('recreate', OWNER='false')
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(any(c[0] in ('build', 'stop', 'rename', 'run') for c in calls))

    def test_failed_upgrade_check_cannot_stop_or_replace_existing_container(self):
        result, calls = self.run_launcher('recreate', AUDIT_FAILURE='1')
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue(any('wake.upgrade' in c for c in calls))
        self.assertFalse(any(c[0] in ('stop', 'rename', 'exec') for c in calls))

    def test_recreate_builds_checks_and_drains_before_preserving_old_container(self):
        result, calls = self.run_launcher('recreate')
        self.assertEqual(result.returncode, 0, result.stderr)
        build = next(i for i,c in enumerate(calls) if c[0]=='build')
        audit = next(i for i,c in enumerate(calls) if 'wake.upgrade' in c)
        drain = calls.index(['exec','wake','wake-research','stop'])
        stop = calls.index(['stop','wake'])
        rename = next(i for i,c in enumerate(calls) if c[0]=='rename')
        create = next(i for i,c in enumerate(calls) if '--name' in c)
        self.assertLess(build, audit)
        self.assertLess(audit, drain)
        self.assertLess(drain, stop)
        self.assertLess(stop, rename)
        self.assertLess(rename, create)
        self.assertIn('8095:8080',calls[create])
        self.assertFalse(any(c[0] in ('rm','volume') for c in calls))
