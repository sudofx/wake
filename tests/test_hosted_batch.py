"""A partial Start cannot discard the batch's final checkpoint and publication."""
from contextlib import nullcontext, redirect_stdout
import io
import os
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError

from wake.installation_cli import NODE_IDS
from scripts.github_research import run_batch
from scripts.github_research import PeriodicPublication


@patch.dict(os.environ, {'GITHUB_ACTIONS':'false'})
class HostedBatchTests(unittest.TestCase):
    def test_periodic_publication_failure_does_not_own_research_or_final_capture(self):
        import threading
        observed = threading.Event()
        mirror = PeriodicPublication(SimpleNamespace(), Path('/fixture'), 'a'*40, interval=.001)
        def failed(*_):
            mirror.closed.set();observed.set();raise OSError('fixture network failure')
        with patch('scripts.github_research.publish_hosted_snapshot',side_effect=failed) as publish, redirect_stdout(io.StringIO()):
            mirror.thread.start()
            self.assertTrue(observed.wait(2))
            mirror.close()
        publish.assert_called_once()

    def test_partial_start_runs_confirmed_workers_and_no_ack_closes_but_both_publish(self):
        for acknowledged in (True, False, 'control-failure'):
            with self.subTest(acknowledged=acknowledged), tempfile.TemporaryDirectory() as directory:
                root, artifact = Path(directory) / 'records', Path(directory) / 'public'
                revision = 'a' * 40
                client = SimpleNamespace(repository='example/repo', token='fixture', request=MagicMock(
                    return_value={'object':{'sha':'b'*40}, 'workflow_runs': [{'head_sha': revision, 'head_branch': 'master'}]}))
                transport = MagicMock()
                def restore(path, **_):
                    path.mkdir();return {'installation_id': 'original', 'generation': 1, 'nodes': {}}
                transport.restore.side_effect = restore
                transport.read_manifest.return_value = {'generation': 25}
                transport.lease.side_effect = nullcontext
                process = MagicMock(returncode=0)
                process.poll.return_value = None
                start = {'ok': False, 'nodes': {'100.wake': {
                    'state': 'acknowledged' if acknowledged else 'unknown'}, '201.wake': {'state': 'failed'}}}
                def request(_root, command):
                    return start if command['action'] == 'start' else {'ok': True}
                def build(_root, target, **_):
                    target.mkdir()
                    for node in NODE_IDS:(target / 'nodes' / node).mkdir(parents=True)
                    return {'installation_id': 'original', 'record_heads': {n: {'version': 1, 'head': n} for n in NODE_IDS}}
                environment = {'WAKE_SOURCE_REVISION': revision, 'WAKE_INSTALLATION_DATA': str(root),
                               'WAKE_HOSTED_ARTIFACT': str(artifact), 'GITHUB_RUN_ID': '123'}
                with patch.dict(os.environ, environment), \
                     patch('scripts.github_research.api', return_value=client), \
                     patch('scripts.github_research.enabled', side_effect=[True, True, HTTPError(
                         'https://api.github.com', 403, 'Forbidden', {}, None)]
                         if acknowledged == 'control-failure' else None, return_value=True), \
                     patch('scripts.github_research.HostedState.from_environment', return_value=transport), \
                     patch('scripts.github_research.subprocess.Popen', return_value=process), \
                     patch('scripts.github_research.ready'), \
                     patch('scripts.github_research.request', side_effect=request), \
                     patch('scripts.github_research.build_public_artifact', side_effect=build), \
                     patch('scripts.github_research.upload_public_artifact') as upload, \
                     patch('wake.hosted_presentation.bind_hosted_status'), \
                     patch('scripts.github_research.time.monotonic', side_effect=[0, 0, 0, 0, 61]), \
                     patch('scripts.github_research.time.sleep') as sleep, redirect_stdout(io.StringIO()):
                    if acknowledged == 'control-failure':
                        with self.assertRaises(HTTPError):
                            run_batch(1, 'fixture')
                    else:
                        run_batch(1, 'fixture')
                self.assertEqual(sleep.call_count, int(acknowledged is True))
                self.assertEqual(transport.checkpoint_node.call_count, 24)
                process.terminate.assert_called_once()
                if acknowledged == 'control-failure':
                    upload.assert_not_called()
                    continue
                upload.assert_called_once()
                self.assertTrue(any(c.args == ('pages/builds',) and c.kwargs.get('method') == 'POST'
                                    for c in client.request.call_args_list))


@patch.dict(os.environ, {'GITHUB_ACTIONS':'false'})
class HostedRuntimeSelectionTests(unittest.TestCase):
    def test_actions_uses_immutable_workflow_policy_instead_of_candidate_checkout(self):
        import base64, json
        from scripts.github_research import checked_revision
        revision = 'b' * 40
        policy = dict(schema=1, installations={'example/repo': dict(
            installation_id='1'*32, source_revision=revision)})
        client = SimpleNamespace(repository='example/repo', request=MagicMock(side_effect=[
            dict(type='file', encoding='base64', content=base64.b64encode(json.dumps(policy).encode()).decode()),
            {'workflow_runs': [{'event':'push','head_branch':'master','head_sha':revision}]}]))
        with tempfile.TemporaryDirectory() as directory, \
                patch('scripts.github_research.RUNTIME_POLICY', self.policy_file(directory)), \
                patch.dict(os.environ, {'GITHUB_ACTIONS':'true','GITHUB_SHA':'c'*40}):
            self.assertEqual(checked_revision(client), revision)
        self.assertEqual(client.request.call_args_list[0].args,
                         ('contents/hosted-runtime.json?ref='+'c'*40,))
        self.assertIn('head_sha='+revision,client.request.call_args_list[1].args[0])

    def test_actions_policy_read_failure_or_malformed_file_cannot_open_authority(self):
        for result in (OSError('unavailable'), {}, {'type':'file','encoding':'base64','content':'!invalid!'}):
            client = SimpleNamespace(repository='example/repo', request=MagicMock(
                side_effect=result if isinstance(result,Exception) else None,
                return_value=result if isinstance(result,dict) else None))
            with patch.dict(os.environ, {'GITHUB_ACTIONS':'true','GITHUB_SHA':'c'*40,'WAKE_SOURCE_REVISION':'b'*40}), \
                    patch('scripts.github_research.api',return_value=client), \
                    patch('scripts.github_research.enabled',return_value=True), \
                    patch('scripts.github_research.HostedState.from_environment') as transport:
                with self.assertRaises((OSError,ValueError)):
                    run_batch(1,'fixture')
                transport.assert_not_called()

    def test_operator_mode_changes_only_root_setting_and_preserves_topics(self):
        import tomllib
        from scripts.github_research import apply_decision_memory_policy
        for initial in ('', 'decision_memory_mode = "off"\n'):
            with tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                (root / 'config').mkdir()
                path = root / 'config/wake.toml'
                path.write_text(initial + 'memory_mode = "active"\n[topics]\nquestion = "persist"\n')
                with redirect_stdout(io.StringIO()):
                    apply_decision_memory_policy(root, {'decision_memory_mode': 'active'})
                values = tomllib.loads(path.read_text())
                self.assertEqual(values['decision_memory_mode'], 'active')
                self.assertEqual(values['memory_mode'], 'active')
                self.assertEqual(values['topics'], {'question': 'persist'})
                before = path.read_bytes()
                apply_decision_memory_policy(root, None)
                self.assertEqual(before, path.read_bytes())
                with self.assertRaises(ValueError):
                    apply_decision_memory_policy(root, {'decision_memory_mode': 'invalid'})
                self.assertEqual(before, path.read_bytes())

    def test_unpinned_bound_installation_selects_successful_master(self):
        import json
        from scripts.github_research import checked_revision
        client = SimpleNamespace(repository='example/repo', request=MagicMock(return_value={
            'workflow_runs': [{'event': 'push', 'head_branch': 'master', 'head_sha': 'b' * 40}]}))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'policy.json'
            path.write_text(json.dumps({'schema': 1, 'installations': {'example/repo': {
                'installation_id': '1' * 32, 'decision_memory_mode': 'active'}}}))
            with patch('scripts.github_research.RUNTIME_POLICY', path):
                self.assertEqual(checked_revision(client), 'b' * 40)
            self.assertIn('branch=master', client.request.call_args.args[0])

    def policy_file(self, directory):
        import json
        path = Path(directory) / 'hosted-runtime.json'
        path.write_text(json.dumps({'schema': 1, 'installations': {'example/repo': {
            'installation_id': '1' * 32, 'source_revision': 'a' * 40}}}))
        return path

    def test_pinned_installation_cannot_follow_newer_checked_source(self):
        from scripts.github_research import checked_revision
        client = SimpleNamespace(repository='example/repo', request=MagicMock(return_value={
            'workflow_runs': [{'event': 'push', 'head_branch': 'master', 'head_sha': 'b' * 40},
                              {'event': 'push', 'head_branch': 'master', 'head_sha': 'a' * 40}]}))
        with tempfile.TemporaryDirectory() as directory, \
                patch('scripts.github_research.RUNTIME_POLICY', self.policy_file(directory)):
            self.assertEqual(checked_revision(client), 'a' * 40)
        self.assertIn('head_sha=' + 'a' * 40, client.request.call_args.args[0])

    def test_missing_pinned_ci_fails_closed_instead_of_falling_forward(self):
        from scripts.github_research import checked_revision
        client = SimpleNamespace(repository='example/repo', request=MagicMock(return_value={
            'workflow_runs': [{'event': 'push', 'head_branch': 'master', 'head_sha': 'b' * 40}]}))
        with tempfile.TemporaryDirectory() as directory, \
                patch('scripts.github_research.RUNTIME_POLICY', self.policy_file(directory)):
            with self.assertRaises(ValueError):
                checked_revision(client)

    def test_fork_has_its_own_checked_source_and_no_foreign_pin(self):
        from scripts.github_research import checked_revision
        client = SimpleNamespace(repository='another/fork', request=MagicMock(return_value={
            'workflow_runs': [{'event': 'push', 'head_branch': 'master', 'head_sha': 'b' * 40}]}))
        with tempfile.TemporaryDirectory() as directory, \
                patch('scripts.github_research.RUNTIME_POLICY', self.policy_file(directory)):
            self.assertEqual(checked_revision(client), 'b' * 40)
        self.assertIn('branch=master', client.request.call_args.args[0])

    def test_direct_incompatible_runtime_cannot_open_hosted_authority(self):
        client = SimpleNamespace(repository='example/repo')
        with tempfile.TemporaryDirectory() as directory, \
                patch('scripts.github_research.RUNTIME_POLICY', self.policy_file(directory)), \
                patch('scripts.github_research.api', return_value=client), \
                patch('scripts.github_research.enabled', return_value=True), \
                patch.dict(os.environ, {'WAKE_SOURCE_REVISION': 'b' * 40}), \
                patch('scripts.github_research.HostedState.from_environment') as transport:
            with self.assertRaises(ValueError):
                run_batch(1, 'fixture')
            transport.assert_not_called()
