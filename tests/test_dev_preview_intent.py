"""Dev lifecycle restores only explicit research intent, never credential presence."""
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from scripts import dev_preview


class PreviewIntentTests(unittest.TestCase):
    def launch_boundary(self, prior, research=None):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            identity = home / 'preview.json'
            if prior is not None:
                identity.write_text(json.dumps(prior))
            with patch.object(dev_preview, 'PID', identity), \
                 patch.object(dev_preview, 'PREVIEW_HOME', home), \
                 patch.object(dev_preview, 'alive', return_value=False), \
                 patch('socket.socket'), \
                 patch.dict(os.environ, {'GEMINI_API_KEY': 'fixture-not-a-credential'}), \
                 patch.object(dev_preview.subprocess, 'Popen', side_effect=RuntimeError('captured launch')) as launch:
                with self.assertRaisesRegex(RuntimeError, 'captured launch'):
                    dev_preview.start(8080, research)
                return launch.call_args

    def test_new_install_stays_paused_even_with_provider_secret(self):
        call = self.launch_boundary(None)
        self.assertIn('--paused', call.args[0])
        self.assertNotIn('GEMINI_API_KEY', call.kwargs['env'])

    def test_dead_runtime_resumes_explicit_research_intent(self):
        call = self.launch_boundary({'research': True})
        self.assertNotIn('--paused', call.args[0])
        self.assertEqual(call.args[0][-2:], ['--provider', 'gemini'])
        self.assertIn('GEMINI_API_KEY', call.kwargs['env'])

    def test_explicit_pause_overrides_saved_live_intent(self):
        call = self.launch_boundary({'research': True}, False)
        self.assertIn('--paused', call.args[0])
        self.assertNotIn('GEMINI_API_KEY', call.kwargs['env'])

    def test_stop_removes_live_intent_without_removing_record(self):
        with tempfile.TemporaryDirectory() as directory:
            identity = Path(directory) / 'preview.json'
            record = Path(directory) / 'wake.sqlite'
            identity.write_text(json.dumps({'research': True}))
            record.write_bytes(b'record retained')
            with patch.object(dev_preview, 'PID', identity), patch.object(dev_preview, 'alive', return_value=False):
                dev_preview.stop()
            self.assertFalse(identity.exists())
            self.assertEqual(record.read_bytes(), b'record retained')
