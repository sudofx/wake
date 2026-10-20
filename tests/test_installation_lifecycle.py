"""Exercise actual stopped worker lifecycles with offline fixtures, never Gemini."""
import json
import os
from pathlib import Path
import signal
import socket
import subprocess
import sys
import tempfile
import time
import unittest
import urllib.request
from unittest.mock import Mock, patch

from wake.installation_cli import request
from wake.installation import Controller, NODE_IDS


class InstallationRestartTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.controller = Controller(self.temp.name, Path(self.temp.name) / 'wake.toml', 'fixture', 0)
        self.controller.workers = {name: Mock() for name in NODE_IDS}
        self.controller.logs = {name: Mock() for name in NODE_IDS}
        for name, process in self.controller.workers.items():
            process.poll.return_value = 1 if name == NODE_IDS[0] else None

    def test_restart_reaps_dead_worker_after_survivors_drain(self):
        controller = self.controller
        key = ('wake', NODE_IDS[0], 'request')
        controller.coordinator.acquire(key, 'fixture')
        # A death notification alone cannot release a grant: reaping does.
        controller.workers[NODE_IDS[0]].wait.side_effect = lambda **_: self.assertIsNotNone(controller.coordinator.status()['active'])
        original_control = controller.control
        def control(mode):
            if mode == 'stopped':
                return original_control(mode)
            self.assertIsNone(controller.coordinator.status()['active'])
            self.assertFalse(controller.workers)
            return {'ok': True, 'research': 'running'}
        with patch.object(controller, 'set_controls', return_value='command'), \
             patch('wake.installation.read_json', return_value={'control_ack': 'command', 'state': 'stopped'}), \
             patch.object(controller, 'control', side_effect=control), \
             patch.object(controller, 'spawn') as spawn:
            self.assertTrue(controller.command({'action': 'restart'})['ok'])
        spawn.assert_called_once_with()

    def test_restart_never_replaces_live_unknown_or_missing_worker(self):
        for state, missing in [('unknown', False), ('failed', False), ('failed', True)]:
            with self.subTest(state=state, missing=missing):
                controller = self.controller
                name = NODE_IDS[-1]
                process = controller.workers.pop(name) if missing else controller.workers[name]
                nodes = {node: {'state': 'drained'} for node in NODE_IDS}
                nodes[NODE_IDS[0]] = {'state': 'failed'}
                nodes[name] = {'state': state}
                result = {'ok': False, 'nodes': nodes}
                with patch.object(controller, 'control', return_value=result), \
                     patch.object(controller, 'terminate') as terminate, \
                     patch.object(controller, 'spawn') as spawn:
                    self.assertIs(controller.command({'action': 'restart'}), result)
                terminate.assert_not_called()
                spawn.assert_not_called()
                controller.workers[name] = process

    def test_stop_still_reports_dead_worker_failure(self):
        with patch.object(self.controller, 'set_controls', return_value='command'), \
             patch('wake.installation.read_json', return_value={'control_ack': 'command', 'state': 'stopped'}):
            result = self.controller.command({'action': 'stop'})
        self.assertFalse(result['ok'])
        self.assertEqual(result['nodes'][NODE_IDS[0]]['state'], 'failed')
        self.assertEqual(sum(node['state'] == 'drained' for node in result['nodes'].values()), 11)


@unittest.skipUnless(sys.platform == 'linux', 'Worker parent-death contract requires Linux')
class InstallationLifecycleTests(unittest.TestCase):
    def test_reset_import_and_controller_death_leave_no_live_worker(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config = root / 'wake.toml'
            config.write_text('provider="fixture"\nobjective="Offline installation acceptance"\n')
            with socket.socket() as sock:
                sock.bind(('127.0.0.1', 0))
                port = sock.getsockname()[1]
            env = dict(os.environ)
            for key in ('GEMINI_API_KEY', 'GEMINI_API_KEY_FILE', 'WAKE_GROUP_ID', 'WAKE_GROUP_TOPIC_FILE'):
                env.pop(key, None)
            with (root / 'test.log').open('wb') as log:
                process = subprocess.Popen([sys.executable, '-m', 'wake.installation', '--data', str(root),
                    '--config', str(config), '--port', str(port), '--provider', 'fixture'],
                    env=env, stdout=log, stderr=log)
            try:
                deadline = time.monotonic() + 90
                manifest = None
                while time.monotonic() < deadline:
                    self.assertIsNone(process.poll(), (root / 'test.log').read_text())
                    try:
                        with urllib.request.urlopen(f'http://127.0.0.1:{port}/installation.json', timeout=1) as response:
                            manifest = json.load(response)
                        if all(n['available'] and n['runtime']['state'] == 'stopped' for n in manifest['nodes']):
                            break
                    except (OSError, KeyError):
                        pass
                    time.sleep(.2)
                self.assertIsNotNone(manifest)
                self.assertTrue(all(n['available'] for n in manifest['nodes']))
                self.assertEqual(0, sum(n['research']['metrics']['provider_requests'] for n in manifest['nodes']))
                self.assertTrue(all(n['research']['matrix']['enabled'] for n in manifest['nodes']))
                self.assertTrue(all(n['research']['matrix']['completed']==0 for n in manifest['nodes']))
                self.assertTrue(request(root, {'action': 'start'})['ok'])
                self.assertTrue(request(root, {'action': 'pause'})['ok'])
                self.assertTrue(request(root, {'action': 'export', 'name': 'manual.zip'})['ok'])
                self.assertTrue(request(root, {'action': 'RESET'})['ok'])
                with urllib.request.urlopen(f'http://127.0.0.1:{port}/installation.json') as response:
                    reset = json.load(response)
                self.assertTrue(all(n['research']['matrix']['enabled'] for n in reset['nodes']))
                self.assertTrue(all(n['snapshot']['version']==0 and n['research']['matrix']['completed']==0 for n in reset['nodes']))
                # Recheck another command: short-lived socket handlers must not
                # own the replacement workers' Linux parent-death boundary.
                time.sleep(.5)
                self.assertTrue(request(root, {'action': 'stop'})['ok'])
                self.assertTrue(request(root, {'action': 'import', 'archive': 'manual.zip'})['ok'])
                self.assertTrue(request(root, {'action': 'stop'})['ok'])
                self.assertEqual(['manual.zip'], sorted(p.name for p in (root / 'backups').iterdir()))
                result = request(root, {'action': 'publish', 'output': str(root / 'public')})
                self.assertTrue(result['ok'], result)
                public = json.loads((root / 'public/installation.json').read_text())
                self.assertFalse(public['live'])
                self.assertTrue(all(n['runtime']['state'] == 'snapshot' for n in public['nodes']))
                with open(f'/proc/{process.pid}/task/{process.pid}/children') as children:
                    worker_pids = [int(pid) for pid in children.read().split()]
                self.assertEqual(12, len(worker_pids))
                process.kill()
                process.wait(timeout=10)
                deadline = time.monotonic() + 5
                while time.monotonic() < deadline:
                    living = []
                    for pid in worker_pids:
                        try:
                            if Path(f'/proc/{pid}/stat').read_text().rsplit(')', 1)[1].split()[0] != 'Z':
                                living.append(pid)
                        except (FileNotFoundError, ProcessLookupError):
                            # Linux may retire the process after opening stat
                            # but before reading it; both errors mean it exited.
                            pass
                    if not living:
                        break
                    time.sleep(.1)
                self.assertFalse(living, 'Workers outlived the controller')
            finally:
                if process.poll() is None:
                    process.terminate()
                    process.wait(timeout=180)


if __name__ == '__main__':
    unittest.main()
