"""Installation status never falls through to a separate solo authority."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from wake.__main__ import execute, parser


class StatusRoutingTests(unittest.TestCase):
    def test_installation_status_uses_controller_without_opening_authority(self):
        status = {'ok': True, 'research': 'running', 'nodes': []}
        with patch.dict('os.environ', {'WAKE_TERMINAL_ROLE': 'installation',
                                      'WAKE_INSTALLATION_DATA': '/chosen-installation'}), \
             patch('wake.installation_cli.request', return_value=status) as request, \
             patch('wake.__main__.open_authoritative_store') as store:
            self.assertIs(execute(parser().parse_args(['status'])), status)
        request.assert_called_once_with(Path('/chosen-installation'), {'action': 'status'})
        store.assert_not_called()

    def test_missing_controller_never_falls_back_to_solo_record(self):
        with patch.dict('os.environ', {'WAKE_TERMINAL_ROLE': 'installation'}), \
             patch('wake.installation_cli.request', side_effect=OSError('controller unavailable')), \
             patch('wake.__main__.open_authoritative_store') as store:
            with self.assertRaisesRegex(OSError, 'controller unavailable'):
                execute(parser().parse_args(['status']))
        store.assert_not_called()

    def test_explicit_record_and_solo_default_keep_missing_authority_guard(self):
        with tempfile.TemporaryDirectory() as directory:
            for role, arguments in [('installation', ['--data', directory, 'status']),
                                    ('parent', ['status'])]:
                with self.subTest(role=role), \
                     patch.dict('os.environ', {'WAKE_TERMINAL_ROLE': role}), \
                     patch('wake.installation_cli.request') as request, \
                     patch('wake.__main__.open_authoritative_store', side_effect=OSError('missing authority')) as store:
                    with self.assertRaisesRegex(OSError, 'missing authority'):
                        execute(parser().parse_args(arguments))
                    self.assertEqual(store.call_args.args[0], directory if role == 'installation' else 'data')
                    request.assert_not_called()
