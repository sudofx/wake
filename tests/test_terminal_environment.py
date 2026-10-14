"""The terminal replaces imported shell files without touching other home data."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts.wake_terminal import COPIED_DOTFILES, install, statistics


class TerminalEnvironmentTests(unittest.TestCase):
    def test_install_removes_personal_files_preserves_history_and_editor_data(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            for name in COPIED_DOTFILES:
                (home / name).write_text('personal-host-settings')
            (home / '.bash_history').write_text('retained operational history')
            (home / '.vscode-server').mkdir()
            with patch('scripts.wake_terminal.os.geteuid', return_value=10001):
                install(home, '101.wake')
                install(home, '101.wake')
            self.assertEqual((home / '.wake-node').read_text().strip(), '101.wake')
            self.assertEqual((home / '.bash_history').read_text(), 'retained operational history')
            self.assertTrue((home / '.vscode-server').is_dir())
            for name in COPIED_DOTFILES:
                path = home / name
                self.assertTrue(not path.exists() or 'personal-host-settings' not in path.read_text())

    def test_unavailable_local_server_is_visible_without_a_provider_or_record_write(self):
        with patch('scripts.wake_terminal.public_json', side_effect=OSError('offline')) as read:
            s = statistics()
        self.assertEqual(s['state'], 'unavailable')
        self.assertEqual(s['version'], '—')
        read.assert_called_once_with('runtime.json')

class InstallationStatusTests(unittest.TestCase):
    def test_runtime_status_does_not_read_research_exports(self):
        from datetime import datetime, timezone
        from wake.installation import installation_snapshot, NODE_IDS
        reads = []
        def read(path, *args):
            reads.append(Path(path).name)
            if Path(path).name == 'installation-id.json':
                return {'id': 'installation'}
            if Path(path).name == 'runtime.json':
                return {'state': 'standby', 'observed_at': datetime.now(timezone.utc).isoformat()}
            self.fail('Runtime status attempted to read a research export')
        with patch('wake.installation.read_json', side_effect=read):
            snapshot = installation_snapshot('/unused', include_research=False)
        self.assertEqual(len(snapshot['nodes']), len(NODE_IDS))
        self.assertEqual(set(reads), {'runtime.json', 'installation-id.json'})
        self.assertTrue(all(n['runtime']['state'] == 'standby' for n in snapshot['nodes']))

    def test_waiting_nodes_are_visible_even_when_research_is_enabled(self):
        from wake.installation import installation_runtime
        from scripts.wake_terminal import status_details
        snapshot = {'nodes':[{'runtime':{'state':'waiting','reason':'Publication unavailable'}} for _ in range(12)]}
        runtime = installation_runtime(snapshot, 'running', {'active':None})
        with patch.dict('os.environ', {'WAKE_TERMINAL_ROLE':'installation'}), \
             patch('scripts.wake_terminal.public_json', side_effect=[runtime, {'nodes':[{'snapshot':{'version':0}} for _ in range(12)]}]):
            result = statistics()
        self.assertEqual(result['state'],'waiting')
        self.assertIn('Reason: Publication unavailable',status_details(result))
        self.assertEqual(runtime['research'],'running')
        self.assertEqual(installation_runtime(snapshot,'stopped',{'active':None})['state'],'stopped')
        self.assertEqual(installation_runtime(snapshot,'running',{'active':{'member':'100.wake'}})['state'],'running')
