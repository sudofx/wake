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
