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
