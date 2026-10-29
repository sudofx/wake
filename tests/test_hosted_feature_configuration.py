"""Feature activation preserves records and respects newer operator intent."""
from contextlib import nullcontext
from copy import deepcopy
from pathlib import Path
import base64
import json
import tomllib
import unittest
import zipfile
from types import SimpleNamespace
from unittest.mock import patch

from scripts.configure_hosted_features import FEATURES, audit, configure, feature_configuration, probe_grounding, restart
from wake.installation_cli import NODE_IDS


class Client:
    repository = 'example/wake'
    latest = 31
    worker = {'path': '.github/workflows/research-worker.yml', 'head_branch': 'master',
              'status': 'completed', 'conclusion': 'success', 'head_sha': 'b'*40}
    outstanding = []

    def __init__(self):
        self.calls = []

    def request(self, path, **kwargs):
        self.calls.append((path, kwargs))
        if path == 'actions/workflows/hosted-control.yml/runs?per_page=1':
            return {'workflow_runs': [{'id': self.latest}]}
        if path == 'actions/runs/31':
            return {'path': '.github/workflows/hosted-control.yml', 'head_branch': 'master',
                    'status': 'completed', 'conclusion': 'success'}
        if path == 'actions/runs/41':
            return self.worker
        if path == 'actions/workflows/research-worker.yml':
            return {'state': 'disabled_manually'}
        if path == 'contents/hosted-runtime.json?ref=' + 'b'*40:
            return {'content': base64.b64encode(json.dumps({'installations': {'example/wake': {
                'installation_id': 'fixture', 'source_revision': 'a'*40}}}).encode()).decode()}
        if 'runs?status=' in path:
            return {'workflow_runs': self.outstanding, 'total_count': len(self.outstanding)}
        if path.endswith('/dispatches'):
            return None
        raise AssertionError(path)


class Transport:
    def __init__(self):
        self.manifest = {'installation_id': 'fixture', 'generation': 7,
                         'nodes': {node: {'head': node, 'sha256': node, 'revision': 20} for node in NODE_IDS},
                         'auxiliary': ['original encrypted blocks']}
        self.saved = None
        self.changed = False

    def open(self):
        pass

    def restore(self, root, **kwargs):
        (root/'config').mkdir(parents=True)
        (root/'config/wake.toml').write_text('inquiry_drive_enabled = false\napi_secret = "private fixture"\n[nodes.example]\nenabled = false\n')
        return deepcopy(self.manifest)

    def lease(self):
        return nullcontext()

    def read_manifest(self):
        result = deepcopy(self.manifest)
        if self.changed:
            result['generation'] += 1
        return result

    def assets(self):
        return {}

    def put_auxiliary(self, root, assets):
        self.configuration = tomllib.loads((root/'config/wake.toml').read_text())
        return ['new encrypted configuration blocks']

    def save(self, manifest):
        manifest['generation'] += 1
        self.saved = deepcopy(manifest)


class FeatureConfigurationTests(unittest.TestCase):
    def policy(self):
        return {'schema': 1, 'installations': {'example/wake': {
            'installation_id': 'fixture', 'source_revision': 'a'*40,
            'experimental_research_enabled': True}}}

    def test_only_root_feature_switches_change(self):
        original = '# Retain comments\nmemory_mode = "shadow"\nresearch_google_search = false\n[private]\nvalue = "retained"\ninquiry_drive_enabled = false\n'
        updated, before = feature_configuration(original)
        parsed = tomllib.loads(updated)
        self.assertEqual({key: parsed[key] for key in FEATURES}, FEATURES)
        self.assertEqual(before['memory_mode'], 'shadow')
        self.assertFalse(parsed['research_google_search'])
        self.assertEqual(parsed['private'], {'value': 'retained', 'inquiry_drive_enabled': False})
        self.assertIn('# Retain comments', updated)
        self.assertEqual(feature_configuration(updated)[0], updated)

    def test_bad_configuration_is_rejected(self):
        with self.assertRaises(tomllib.TOMLDecodeError):
            feature_configuration('memory_mode = invalid')

    def test_configuration_preserves_every_native_record_identity(self):
        client, transport = Client(), Transport()
        records = deepcopy(transport.manifest['nodes'])
        with patch('scripts.configure_hosted_features.read_policy', return_value=(self.policy(), 'sha')):
            report = configure(client, transport, 31, 41)
        self.assertEqual(transport.saved['nodes'], records)
        self.assertEqual(transport.saved['generation'], 8)
        self.assertEqual(transport.configuration['api_secret'], 'private fixture')
        self.assertFalse(transport.configuration['nodes']['example']['enabled'])
        self.assertNotIn('private fixture', json.dumps(report))
        self.assertFalse(report['native_records_changed'])

    def test_changed_checkpoint_prevents_configuration(self):
        transport = Transport(); transport.changed = True
        with patch('scripts.configure_hosted_features.read_policy', return_value=(self.policy(), 'sha')):
            with self.assertRaisesRegex(ValueError, 'checkpoint changed'):
                configure(Client(), transport, 31, 41)
        self.assertIsNone(transport.saved)

    def test_active_worker_prevents_configuration(self):
        client, transport = Client(), Transport()
        client.outstanding = [{'id': 99, 'status': 'in_progress'}]
        with patch('scripts.configure_hosted_features.read_policy', return_value=(self.policy(), 'sha')):
            with self.assertRaisesRegex(ValueError, 'worker is outstanding'):
                configure(client, transport, 31, 41)
        self.assertIsNone(transport.saved)

    def test_missing_science_grant_prevents_configuration(self):
        policy = self.policy(); policy['installations']['example/wake']['experimental_research_enabled'] = False
        transport = Transport()
        with patch('scripts.configure_hosted_features.read_policy', return_value=(policy, 'sha')):
            with self.assertRaisesRegex(ValueError, 'explicit scientific grant'):
                configure(Client(), transport, 31, 41)
        self.assertIsNone(transport.saved)

    def test_failed_or_unrelated_drain_is_not_accepted(self):
        for changes in ({'conclusion': 'failure'}, {'path': '.github/workflows/test.yml'}):
            client, transport = Client(), Transport()
            client.worker = {**client.worker, **changes}
            with self.assertRaises(ValueError):
                configure(client, transport, 31, 41)
            self.assertIsNone(transport.saved)

    def test_newer_operator_control_prevents_restart(self):
        client = Client(); client.latest = 32
        with self.assertRaisesRegex(ValueError, 'newer operator'):
            restart(client, 31)
        self.assertFalse(any(path.endswith('/dispatches') for path, _ in client.calls))

    def test_restart_uses_normal_control(self):
        client = Client()
        restart(client, 31)
        self.assertEqual(client.calls[-1], ('actions/workflows/hosted-control.yml/dispatches', {
            'method': 'POST', 'body': {'ref': 'master', 'inputs': {'action': 'start'}}}))

    def test_audit_reads_only_whitelisted_settings_without_restoring_records(self):
        transport = Transport()
        def get_file(_blocks, path):
            with zipfile.ZipFile(path, 'w') as archive:
                archive.writestr('config/wake.toml', 'memory_mode = "active"\nresearch_google_search = false\napi_secret = "private fixture"\n')
        transport.get_file = get_file
        with patch.object(transport, 'restore') as restore:
            report = audit(transport)
        self.assertEqual(report['configured']['memory_mode'], 'active')
        self.assertFalse(report['configured']['research_google_search'])
        self.assertNotIn('private fixture', json.dumps(report))
        self.assertIsNone(transport.saved)
        restore.assert_not_called()

    def test_grounding_probe_does_not_report_provider_bodies_or_research_progress(self):
        provider = SimpleNamespace(provider_requests_sent=1, provider_attempts=[{
            'model': 'fixture', 'result': 'success', 'http_status': 200,
            'web_evidence': {'search_queries': ['private fixture']},
            'request_body': 'private fixture', 'response_body': 'private fixture'}])
        with patch('wake.providers.Gemini', return_value=provider) as constructor, \
             patch('wake.engine.Engine._run_invocation', return_value={'status': 'planned'}):
            report = probe_grounding()
        settings = constructor.call_args.args[0]
        self.assertTrue(settings['research_google_search'])
        self.assertEqual(settings['gemini_fallback_models'], [])
        self.assertEqual(settings['timeout_seconds'], 45)
        self.assertTrue(report['request_accepted'])
        self.assertEqual(report['search_query_count'], 1)
        self.assertFalse(report['hosted_research_progress'])
        self.assertNotIn('private fixture', json.dumps(report))


if __name__ == '__main__':
    unittest.main()
