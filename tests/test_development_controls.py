"""Interrupted editing and timed local pauses cannot mix code or issue effects."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from unittest.mock import patch

from wake.engine import DEFAULTS
from wake.group_coordinator import GroupProviderGate
from wake.providers import Gemini, ProviderCallPaused
from wake.kernel.generation import GenerationResponse
from wake.runtime_supervisor import (InvalidDevelopmentSource, development_worker,
                                     source_signature, watch_development_sources)
from wake.standalone import _research_control, bootstrap


class DevelopmentControlsTests(unittest.TestCase):
    def test_provider_activity_distinguishes_queue_transport_and_response(self):
        with patch.dict(os.environ, {'GEMINI_API_KEY': 'fixture-key'}):
            provider = Gemini(dict(DEFAULTS, free_tier_confirmed=True))
            events = []
            provider.request_activity = events.append
            gate = GroupProviderGate('http://fixture', 'fixture')
            provider.request_gate = gate
            def coordinator(packet):
                if packet['action'] == 'acquire':
                    self.assertEqual(events, ['provider_wait'])
                    self.assertEqual(provider.provider_requests_sent, 0)
                    return {'status': 'granted', 'token': 'fixture'}
                return {'status': 'released'}
            def generate(request):
                self.assertEqual(events[-1], 'provider')
                return GenerationResponse('gemini', request.model, '{}')
            with patch.object(gate, '_request', side_effect=coordinator), patch(
                    'wake.providers.GeminiGenerationProvider.generate', side_effect=generate):
                provider.propose({'context': {}})
            self.assertEqual(events, ['provider_wait', 'provider', 'provider_response'])

    def test_coordination_bypass_is_visible_and_observer_failure_is_inert(self):
        with patch.dict(os.environ, {'GEMINI_API_KEY': 'fixture-key'}):
            provider = Gemini(dict(DEFAULTS, free_tier_confirmed=True))
            events = []
            def observe(stage):
                events.append(stage)
                raise RuntimeError('Display unavailable')
            provider.request_activity = observe
            gate = GroupProviderGate('http://fixture', 'fixture')
            provider.request_gate = gate
            with patch.object(gate, '_request', side_effect=OSError('offline')), patch(
                    'wake.providers.GeminiGenerationProvider.generate', return_value=
                    GenerationResponse('gemini', provider.model, '{}')) as generate:
                provider.propose({'context': {}})
            generate.assert_called_once()
            self.assertEqual(events, ['provider_wait', 'provider_uncoordinated', 'provider_response'])

    def source(self, root):
        (root / 'wake').mkdir()
        (root / 'wake/__init__.py').write_text('')
        (root / 'wake/standalone.py').write_text('value = 1\n')
        (root / 'wake/engine.py').write_text('def config(path): return {}\n')
        (root / 'wake.toml').write_text('provider = "fixture"\n')

    def test_worker_uses_frozen_code_and_excludes_records_and_secret_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.source(root)
            (root / '.env').write_text('PRIVATE=not-worker-source\n')
            (root / 'data').mkdir()
            (root / 'data/wake.sqlite').write_text('not-worker-source')
            command = [sys.executable, '-c', 'from wake.standalone import value; print(value)']
            with development_worker(root, command, os.environ) as (cmd, env, cwd):
                (root / 'wake/standalone.py').write_text('value = 2\n')
                result = subprocess.check_output(cmd, cwd=cwd, env=env, text=True)
                self.assertEqual(result.strip(), '1')
                self.assertFalse((cwd / '.env').exists())
                self.assertFalse((cwd / 'data').exists())
            (root / 'wake/standalone.py').write_text('value =\n')
            with self.assertRaises(InvalidDevelopmentSource):
                with development_worker(root, command, os.environ):
                    self.fail('Incomplete save became executable')

    def test_bad_save_keeps_worker_then_corrected_save_requests_drained_reload(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.source(root)
            stop, reload_requested = threading.Event(), threading.Event()
            watcher = threading.Thread(target=watch_development_sources,
                args=(root, source_signature(root), stop, reload_requested, root / 'wake.toml'))
            watcher.start()
            try:
                (root / 'wake/standalone.py').write_text('value =\n')
                time.sleep(2)
                self.assertFalse(stop.is_set())
                self.assertFalse(reload_requested.is_set())
                (root / 'wake/standalone.py').write_text('value = 2\n')
                self.assertTrue(reload_requested.wait(5))
                self.assertTrue(stop.is_set())
            finally:
                stop.set()
                watcher.join(5)

    def test_cutoff_survives_running_control_without_rewriting_record_or_control(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / '.wake-runner-control.json'
            control = {'research': 'running', 'pause_at': '2000-01-01T00:00:00+00:00'}
            path.write_text(json.dumps(control))
            self.assertEqual(_research_control(directory), ('paused', None))
            self.assertEqual(json.loads(path.read_text()), control)
            control['research'] = 'stopped'
            path.write_text(json.dumps(control))
            self.assertEqual(_research_control(directory), ('stopped', None))
            control['research'] = 'running'
            control['pause_at'] = '2099-01-01T00:00:00+00:00'
            path.write_text(json.dumps(control))
            self.assertEqual(_research_control(directory), ('running', None))
            control['pause_at'] = '2099-01-01T00:00:00'
            path.write_text(json.dumps(control))
            with self.assertRaises(ValueError):
                _research_control(directory)

    def test_pause_after_slot_grant_releases_slot_and_never_fails_open(self):
        paused, calls = False, []
        def coordinator(payload):
            nonlocal paused
            calls.append(payload['action'])
            paused = True
            if payload['action'] == 'release':
                return {'status': 'released'}
            return {'status': 'granted', 'token': 'fixture'}
        gate = GroupProviderGate('http://fixture', 'fixture', should_pause=lambda: paused)
        with patch.object(gate, '_request', side_effect=coordinator):
            with self.assertRaises(ProviderCallPaused):
                with gate.request('fixture'):
                    self.fail('Provider effect occurred after pause')
        self.assertEqual(calls, ['acquire', 'release'])

    def test_paused_provider_defers_without_network_fallback_or_accepted_progress(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {'GEMINI_API_KEY': 'fixture-key'}):
            settings = dict(DEFAULTS, free_tier_confirmed=True)
            engine = bootstrap(directory, settings)
            provider = Gemini(settings)
            provider.request_gate = GroupProviderGate('', '', should_pause=lambda: True)
            try:
                with patch('wake.providers.GeminiGenerationProvider.generate') as generate:
                    result = engine.run(provider)
                generate.assert_not_called()
                self.assertEqual(result['status'], 'deferred')
                self.assertEqual(engine.store.load()['version'], 0)
                self.assertEqual(provider.provider_requests_sent, 0)
                self.assertEqual(len(provider.provider_attempts), 1)
                self.assertEqual(provider.provider_attempts[0]['result'], 'operator_paused')
            finally:
                engine.store.close()
