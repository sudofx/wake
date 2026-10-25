"""An audit may resume only the exact upgrade explicitly requested by its owner."""
import base64
import copy
import json
import unittest
from scripts.complete_hosted_upgrade import complete_upgrade
from wake.installation_cli import NODE_IDS


class Client:
    repository = 'example/repo'

    def __init__(self):
        self.intent = {'candidate': 'a' * 40, 'baseline': 'b' * 40,
                       'verification_run': 42, 'checkpoint_ref': 'f' * 40,
                       'generation': 10, 'control_run': 11}
        self.policy = {'schema': 1, 'installations': {self.repository: {
            'installation_id': 'installation', 'source_revision': 'b' * 40,
            'decision_memory_mode': 'active', 'research_expansion_enabled': True,
            'autonomous_context_improvement': False, 'pending_upgrade': self.intent}}}
        self.report = {'status': 'verified', 'candidate': 'a' * 40, 'baseline': 'b' * 40,
                       'installation_id': 'installation', 'generation': 10,
                       'checkpoint_sha256': 'c' * 64, 'provider_calls': 0, 'remote_record_writes': 0,
                       'nodes': {node: {'head': 'd' * 64, 'native_head': 'e' * 64, 'version': 2, 'revision': 4} for node in NODE_IDS}}
        self.mutations = []
        self.sha = 1
        self.checkpoint = 'f' * 40
        self.latest_control = 11
        self.writers = []
        self.ci = True
        self.active = False

    def request(self, path, *, method='GET', body=None):
        if path.startswith('contents/hosted-runtime.json'):
            if method == 'PUT':
                if body['sha'] != str(self.sha):
                    raise ValueError('Concurrent policy edit')
                self.policy = json.loads(base64.b64decode(body['content']))
                self.sha += 1
                self.mutations.append(('binding', copy.deepcopy(self.policy)))
                return {'content': {'sha': str(self.sha)}}
            return {'sha': str(self.sha), 'content': base64.b64encode(json.dumps(self.policy).encode()).decode()}
        if path == 'actions/runs/42':
            return {'status': 'completed', 'conclusion': 'success', 'head_branch': 'master',
                    'event': 'workflow_dispatch', 'path': '.github/workflows/verify-hosted-upgrade.yml'}
        if path.startswith('actions/workflows/test.yml/runs?'):
            return {'workflow_runs': [{'head_sha': 'a' * 40, 'head_branch': 'master', 'event': 'push'}] if self.ci else []}
        if path == 'actions/workflows/hosted-research.yml':
            return {'state': 'active' if self.active else 'disabled_manually'}
        if path.startswith('actions/workflows/hosted-research.yml/runs?'):
            return {'workflow_runs': self.writers}
        if path == 'actions/workflows/hosted-control.yml/runs?per_page=1':
            return {'workflow_runs': [{'id': self.latest_control}]}
        if path.startswith('actions/workflows/hosted-control.yml/runs?status='):
            return {'workflow_runs': []}
        if path == 'git/ref/heads/wake-hosted-state':
            return {'object': {'sha': self.checkpoint}}
        if path == 'actions/workflows/hosted-control.yml/dispatches' and method == 'POST':
            self.mutations.append(('start', body))
            return None
        raise AssertionError((path, method))


class CompletionTests(unittest.TestCase):
    def test_exact_request_promotes_preserving_settings_then_dispatches_and_clears_intent(self):
        client = Client()
        before = copy.deepcopy(client.policy['installations'][client.repository])
        self.assertEqual(complete_upgrade(client, client.report, 42), 'promoted-and-start-requested')
        actual = client.policy['installations'][client.repository]
        before['source_revision'] = 'a' * 40
        del before['pending_upgrade']
        self.assertEqual(actual, before)
        self.assertEqual([kind for kind, _ in client.mutations], ['binding', 'start', 'binding'])
        self.assertEqual(complete_upgrade(client, client.report, 42), 'no-matching-request')

    def test_verification_without_explicit_intent_cannot_promote(self):
        client = Client()
        del client.policy['installations'][client.repository]['pending_upgrade']
        self.assertEqual(complete_upgrade(client, client.report, 42), 'no-matching-request')
        self.assertFalse(client.mutations)

    def test_stale_control_checkpoint_writer_or_failed_ci_never_mutates(self):
        for attribute, value in [('checkpoint', '0' * 40), ('latest_control', 12),
                                 ('writers', [{'id': 2}]), ('ci', False), ('active', True)]:
            with self.subTest(attribute=attribute):
                client = Client()
                setattr(client, attribute, value)
                with self.assertRaises(ValueError):
                    complete_upgrade(client, client.report, 42)
                self.assertFalse(client.mutations)

    def test_incomplete_or_wrong_audit_never_mutates(self):
        for key, value in [('candidate', '0' * 40), ('generation', 11),
                           ('provider_calls', 1), ('remote_record_writes', 1), ('nodes', {})]:
            with self.subTest(key=key):
                client = Client()
                client.report[key] = value
                with self.assertRaises(ValueError):
                    complete_upgrade(client, client.report, 42)
                self.assertFalse(client.mutations)

    def test_interrupted_promotion_reuses_pin_without_reverting_or_starting_twice(self):
        client = Client()
        client.policy['installations'][client.repository]['source_revision'] = 'a' * 40
        client.active = True
        self.assertEqual(complete_upgrade(client, client.report, 42), 'promoted-and-start-requested')
        self.assertEqual([kind for kind, _ in client.mutations], ['binding'])
