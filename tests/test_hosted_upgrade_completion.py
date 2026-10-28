"""An audit may resume only the exact upgrade explicitly requested by its owner."""
import base64
import copy
import json
import unittest
from scripts.complete_hosted_upgrade import complete_upgrade, writer_outstanding
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
        self.changed_source = 'wake/assets/ant-farm.js'
        self.truncated = False
        self.presentation_changed_source = 'wake/assets/ant-farm.js'
        self.no_ci_for = None

    def request(self, path, *, method='GET', body=None):
        if path.startswith('git/commits/'):
            return {'tree': {'sha': path.rsplit('/', 1)[1]}}
        if path.startswith('git/trees/'):
            rows = [{'path': p, 'sha': '0' * 40, 'mode': '100644', 'type': 'blob'} for p in
                    ('wake/record_store.py', 'wake/kernel/record.py', 'scripts/github_research.py', 'pyproject.toml', 'wake/assets/ant-farm.js')]
            if '/a' in path:
                for row in rows:
                    if row['path'] == self.changed_source:
                        row['sha'] = '1' * 40
                if self.changed_source not in {r['path'] for r in rows}:
                    rows.append({'path': self.changed_source, 'sha': '1' * 40, 'mode': '100644', 'type': 'blob'})
            if '/c' in path:
                for row in rows:
                    if row['path'] == self.presentation_changed_source:
                        row['sha'] = '2' * 40
                if self.presentation_changed_source not in {r['path'] for r in rows}:
                    rows.append({'path': self.presentation_changed_source, 'sha': '2' * 40, 'mode': '100644', 'type': 'blob'})
            return {'tree': rows, 'truncated': self.truncated}
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
            requested = path.split('head_sha=')[1].split('&')[0]
            return {'workflow_runs': [{'head_sha': requested, 'head_branch': 'master', 'event': 'push'}] if self.ci and requested != self.no_ci_for else []}
        if path == 'actions/workflows/research-worker.yml':
            return {'state': 'active' if self.active else 'disabled_manually'}
        if path.startswith('actions/workflows/research-worker.yml/runs?'):
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
    def test_only_explicitly_superseded_jobless_queue_entries_can_be_reconciled(self):
        class Runs:
            repository='example/repo'
            def __init__(self):
                self.old={'status':'queued','path':'.github/workflows/research-worker.yml','head_branch':'master','run_number':1,'head_sha':'b'*40}
                self.drained={**self.old,'status':'completed','conclusion':'success','run_number':5}
                self.jobs={'total_count':0,'jobs':[]}
            def request(self,path):
                if path.startswith('contents/'):
                    return {'content':base64.b64encode(json.dumps({'installations':{self.repository:{'source_revision':'b'*40,'installation_id':'installation'}}}).encode()).decode()}
                return self.old if path=='actions/runs/1' else self.drained if path=='actions/runs/100' else self.jobs
        intent={'drained_run':100,'superseded_queued_runs':[1],'baseline':'b'*40,'candidate':'a'*40}
        client=Runs()
        self.assertFalse(writer_outstanding(client,{'id':1},intent))
        self.assertTrue(writer_outstanding(client,{'id':1},{}))
        self.assertTrue(writer_outstanding(client,{'id':2},intent))
        for changes in ({'status':'in_progress'},{'run_number':6},{'head_branch':'other'},{'head_sha':'a'*40}):
            client=Runs();client.old.update(changes)
            self.assertTrue(writer_outstanding(client,{'id':1},intent))
        client=Runs();client.jobs={'total_count':1,'jobs':[{'status':'queued'}]}
        self.assertTrue(writer_outstanding(client,{'id':1},intent))
        client=Runs();client.drained['conclusion']='failure'
        self.assertTrue(writer_outstanding(client,{'id':1},intent))

    def test_new_presentation_reuses_full_audits_only_with_identical_runtime_and_own_ci(self):
        client = Client()
        client.intent.update(presentation_only=True, presentation_revision='c' * 40)
        self.assertEqual(complete_upgrade(client, client.report, 42), 'presentation-bound-for-next-batch')
        self.assertEqual(client.policy['installations'][client.repository]['source_revision'], 'c' * 40)
        for changed in ('wake/kernel/record.py', 'wake/improvement.py', 'pyproject.toml'):
            client = Client()
            client.intent.update(presentation_only=True, presentation_revision='c' * 40)
            client.presentation_changed_source = changed
            with self.assertRaises(ValueError):
                complete_upgrade(client, client.report, 42)
            self.assertFalse(client.mutations)
        client = Client()
        client.intent.update(presentation_only=True, presentation_revision='c' * 40)
        client.no_ci_for = 'c' * 40
        with self.assertRaises(ValueError):
            complete_upgrade(client, client.report, 42)
        self.assertFalse(client.mutations)
    def test_presentation_binding_preserves_active_writer_and_operator_intent(self):
        for enabled in (False, True):
            client = Client()
            client.intent['presentation_only'] = True
            del client.intent['generation']
            del client.intent['checkpoint_ref']
            client.active = enabled
            client.writers = [{'id': 2}]
            client.checkpoint = '0' * 40  # Fresh history need not be frozen for identical runtime bytes.
            self.assertEqual(complete_upgrade(client, client.report, 42), 'presentation-bound-for-next-batch')
            self.assertEqual([kind for kind, _ in client.mutations], ['binding'])
            self.assertEqual(client.active, enabled)
            self.assertNotIn('pending_upgrade', client.policy['installations'][client.repository])

    def test_presentation_label_cannot_bypass_protected_source_ci_or_operator_controls(self):
        for changed in ('wake/kernel/record.py', 'wake/application_policy.py', 'pyproject.toml',
                        '.github/workflows/research-worker.yml', 'scripts/github_research.py', 'Dockerfile'):
            client = Client()
            client.intent['presentation_only'] = True
            client.changed_source = changed
            with self.assertRaises(ValueError):
                complete_upgrade(client, client.report, 42)
            self.assertFalse(client.mutations)

    def test_isolated_development_demo_does_not_require_stopping_research(self):
        for changed in ('wake/improvement.py', 'wake/recovery_demo.py'):
            client = Client()
            client.intent['presentation_only'] = True
            client.changed_source = changed
            client.active = True
            self.assertEqual(complete_upgrade(client, client.report, 42), 'presentation-bound-for-next-batch')
            self.assertEqual([kind for kind, _ in client.mutations], ['binding'])
        for attr, value in [('truncated', True), ('ci', False), ('latest_control', 12)]:
            client = Client()
            client.intent['presentation_only'] = True
            setattr(client, attr, value)
            with self.assertRaises(ValueError):
                complete_upgrade(client, client.report, 42)
            self.assertFalse(client.mutations)

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
