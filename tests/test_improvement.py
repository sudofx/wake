"""Prove code/evidence/authority boundaries and unfavorable comparison handling."""
from copy import deepcopy
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from wake.improvement import (IMPROVEMENTS, SCHEMA, begin_evaluation, capture_research,
                              digest, evaluate, finish_evaluation, host_at, prepare,
                              record_review, recover, report_data, submit_action, submit_proposal)
from wake.improvement_runner import DEFAULT_IMAGE, command, image_identity, run_program, container_names, CleanupError
from wake.improvement_tasks import TASK, cases, expected, score

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = (ROOT / 'examples/improvement/commitment_candidate.py').read_text()


class ImprovementTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.experiment = self.root / 'experiment'
        self.reader = {'state': {'version': 12, 'commitments': {
            '100.wake::c': {'id': '100.wake::c', 'task': 'Review the observed limitation',
                            'status': 'open', 'origin': {'node': '100.wake', 'head': 'a' * 64, 'version': 1}}}}}
        self.installation = {'installation_id': 'fixture-installation', 'generated': '2026-10-24T23:00:00Z',
                             'record_heads': {f'{g}{i:02}.wake': {'head': 'a' * 64, 'version': 1}
                                              for g in (1, 2, 3) for i in range(4)}}
        self.reader_file, self.installation_file = self.root / 'reader.json', self.root / 'installation.json'
        self.reader_file.write_text(json.dumps(self.reader))
        self.installation_file.write_text(json.dumps(self.installation))
        prepare(self.experiment, self.reader_file, self.installation_file,
                ['commitments:100.wake::c'], checkout=ROOT)
        self.context = host_at(self.experiment).context().state['context']

    def proposal(self, source=CANDIDATE):
        return {'schema': SCHEMA, 'context_digest': digest(self.context), 'title': 'Commitment-aware context',
                'hypothesis': 'Earlier obligations are selected while preserving Attention.',
                'mechanism': 'Use deadlines within the preferred topic.',
                'limitations': 'This task does not measure general model intelligence.', 'candidate_source': source,
                'research_refs': ['100.wake::c']}

    def submit(self, source=CANDIDATE):
        path = self.root / 'proposal.json'
        path.write_text(json.dumps(self.proposal(source)))
        return submit_proposal(self.experiment, path, 'test-origin')['proposal_id']

    def test_preparation_is_isolated_and_preserves_captured_record_provenance(self):
        self.assertFalse((self.experiment / 'wake.sqlite').exists())
        self.assertTrue(report_data(self.experiment)['replay_verified'])
        self.assertEqual(self.context['research'][0]['provenance']['head'], 'a' * 64)
        self.assertEqual(self.context['research'][0]['captured_digest'], digest(self.context['research'][0]['record']))
        protected = self.experiment / 'wake.sqlite'
        protected.write_bytes(b'protected-native-record')
        with self.assertRaisesRegex(ValueError, 'must be new'):
            prepare(self.experiment, self.reader_file, self.installation_file, ['commitments:100.wake::c'])
        self.assertEqual(protected.read_bytes(), b'protected-native-record')

    def test_mismatched_snapshot_fails_before_creating_any_record(self):
        bad = deepcopy(self.installation)
        bad['record_heads']['100.wake']['head'] = 'b' * 64
        with self.assertRaisesRegex(ValueError, 'mismatch'):
            capture_research(self.reader, bad, ['commitments:100.wake::c'])
        bad['record_heads']['100.wake']['version'] = 2
        with self.assertRaisesRegex(ValueError, 'versions differ'):
            capture_research(self.reader, bad, ['commitments:100.wake::c'])

    def test_submission_never_executes_candidate_and_rejection_has_kernel_receipt(self):
        sentinel = self.root / 'must-not-exist'
        malicious = f'open({str(sentinel)!r}, "w").write("oops")\n' + CANDIDATE
        self.submit(malicious)
        self.assertFalse(sentinel.exists())
        invalid = self.proposal()
        invalid['context_digest'] = '0' * 64
        host = host_at(self.experiment)
        with self.assertRaisesRegex(ValueError, 'different research/source context'):
            submit_action(host, 'propose', {'proposal': invalid, 'author': 'model'})
        self.assertEqual(host.recent_governance(limit=1)[0]['status'], 'rejected')
        self.assertTrue(report_data(self.experiment)['replay_verified'])

    def test_duplicates_do_not_overwrite_prior_proposal(self):
        self.submit()
        with self.assertRaisesRegex(ValueError, 'already recorded'):
            self.submit()
        self.assertEqual(len(report_data(self.experiment)['state']['proposals']), 1)

    def test_failed_execution_is_visible_and_cannot_be_accepted(self):
        proposal_id = self.submit()
        with patch('wake.improvement_runner.image_identity', return_value='sha256:' + 'a' * 64), \
             patch('wake.improvement_runner.run_program', return_value={'status': 'failed', 'reason': 'timeout'}):
            result = evaluate(self.experiment, proposal_id)
        self.assertEqual(result['status'], 'execution_failed')
        with self.assertRaisesRegex(ValueError, 'No completed comparison'):
            record_review(self.experiment, result['evaluation_id'], 'accept-for-development', 'looks fine')
        self.assertIn('timeout', (self.experiment / 'review.html').read_text())

    def test_missing_docker_does_not_execute_on_host(self):
        proposal_id = self.submit()
        with patch('wake.improvement_runner.image_identity', side_effect=ValueError('Docker unavailable')), \
             patch('wake.improvement_runner.run_program') as runner:
            with self.assertRaisesRegex(ValueError, 'unavailable'):
                evaluate(self.experiment, proposal_id)
        runner.assert_not_called()
        self.assertEqual(report_data(self.experiment)['state']['evaluations'], {})

    def test_unconfirmed_container_cleanup_remains_recoverable_and_cannot_be_accepted(self):
        proposal_id = self.submit()
        with patch('wake.improvement_runner.image_identity', return_value='sha256:' + 'a' * 64), \
             patch('wake.improvement_runner.run_program', side_effect=CleanupError('cleanup unconfirmed')):
            result = evaluate(self.experiment, proposal_id)
        self.assertEqual(result['status'], 'cleanup_required')
        with self.assertRaisesRegex(ValueError, 'No completed comparison'):
            record_review(self.experiment, result['evaluation_id'], 'accept-for-development', 'Must not accept')
        with patch('wake.improvement_runner.cleanup_containers', side_effect=CleanupError('still unavailable')):
            with self.assertRaisesRegex(CleanupError, 'unavailable'):
                recover(self.experiment, result['evaluation_id'], 'Attempted cleanup')
        trial = report_data(self.experiment)['state']['evaluations'][result['evaluation_id']]
        self.assertEqual(trial['status'], 'cleanup_required')
        with patch('wake.improvement_runner.cleanup_containers'):
            recover(self.experiment, result['evaluation_id'], 'Cleanup confirmed')
        self.assertEqual(report_data(self.experiment)['state']['evaluations'][result['evaluation_id']]['status'], 'execution_failed')

    def mock_comparison(self, candidate_passes):
        calls = 0
        def run(source, population, image, **kwargs):
            nonlocal calls
            calls += 1
            # Trusted fixture observations exercise governance, not Docker proof.
            outputs = [expected(c) for c in population]
            if calls % 2 == 1 or not candidate_passes:
                outputs[0] = {'project_id': 'wrong'}
            return {'status': 'completed', 'outputs': outputs, 'wall_seconds': 0.1, 'output_bytes': 20}
        return run

    def test_success_is_pending_review_and_review_never_installs_code(self):
        proposal_id = self.submit()
        before = (ROOT / 'wake/decision_memory.py').read_bytes()
        with patch('wake.improvement_runner.image_identity', return_value='sha256:' + 'a' * 64), \
             patch('wake.improvement_runner.run_program', side_effect=self.mock_comparison(True)):
            result = evaluate(self.experiment, proposal_id)
        self.assertEqual(result['status'], 'awaiting_review')
        self.assertEqual(report_data(self.experiment)['state']['reviews'], [])
        decision = record_review(self.experiment, result['evaluation_id'], 'accept-for-development', 'Review the source patch next')
        self.assertFalse(decision['source_changed'])
        self.assertEqual((ROOT / 'wake/decision_memory.py').read_bytes(), before)
        with self.assertRaisesRegex(ValueError, 'already reviewed'):
            record_review(self.experiment, result['evaluation_id'], 'reject', 'Repeated review')

    def test_no_improvement_is_preserved_and_cannot_be_accepted(self):
        proposal_id = self.submit()
        with patch('wake.improvement_runner.image_identity', return_value='sha256:' + 'a' * 64), \
             patch('wake.improvement_runner.run_program', side_effect=self.mock_comparison(False)):
            result = evaluate(self.experiment, proposal_id)
        self.assertEqual(result['status'], 'not_improved')
        with self.assertRaisesRegex(ValueError, 'does not qualify'):
            record_review(self.experiment, result['evaluation_id'], 'accept-for-development', 'Override the score')
        record_review(self.experiment, result['evaluation_id'], 'reject', 'No measured improvement')

    def test_interruption_is_durable_and_recovery_does_not_repeat_effect(self):
        proposal_id = self.submit()
        populations = {'development': cases(7, 12), 'holdout': cases(42, 60)}
        payload = {'id': 'interrupted', 'proposal_id': proposal_id, 'image': 'sha256:' + 'a' * 64,
                   'seed': 42, 'task': TASK, 'suite_digest': digest({'task': TASK, 'populations': populations}),
                   'containers': container_names('interrupted')}
        host = host_at(self.experiment)
        submit_action(host, 'begin_evaluation', payload)
        self.assertEqual(report_data(self.experiment)['state']['evaluations']['interrupted']['status'], 'running')
        with patch('wake.improvement_runner.cleanup_containers') as cleanup:
            recover(self.experiment, 'interrupted', 'Operator observed a process interruption')
        cleanup.assert_called_once_with(container_names('interrupted'))
        self.assertEqual(report_data(self.experiment)['state']['evaluations']['interrupted']['status'], 'execution_failed')
        with self.assertRaisesRegex(ValueError, 'not running'):
            recover(self.experiment, 'interrupted', 'Cannot complete it again')

    def test_seed_binding_and_evaluator_reject_forged_case_scores(self):
        proposal_id = self.submit()
        populations = {'development': cases(7, 12), 'holdout': cases(42, 60)}
        payload = {'id': 'forgery', 'proposal_id': proposal_id, 'image': 'sha256:' + 'a' * 64,
                   'seed': 42, 'task': TASK, 'suite_digest': '0' * 64, 'containers': container_names('forgery')}
        state = host_at(self.experiment).context().state
        self.assertFalse(begin_evaluation(state, payload).accepted)
        payload['suite_digest'] = digest({'task': TASK, 'populations': populations})
        registered = begin_evaluation(state, payload).next_state
        evidence = {'task': TASK, 'suite_digest': payload['suite_digest'], 'status': 'completed', 'suites': {}}
        for name, population in populations.items():
            arm = score(population, [expected(c) for c in population])
            evidence['suites'][name] = {'baseline': deepcopy(arm), 'candidate': deepcopy(arm)}
        evidence['suites']['holdout']['candidate']['cases'][0]['actual'] = None
        self.assertFalse(finish_evaluation(registered, {'id': 'forgery', 'evidence': evidence}).accepted)

    def test_report_escapes_untrusted_prose_and_reads_canonical_record(self):
        proposal = self.proposal()
        proposal['title'] = '<script>alert(1)</script>'
        path = self.root / 'proposal.json'
        path.write_text(json.dumps(proposal))
        submit_proposal(self.experiment, path, 'external model')
        page = (self.experiment / 'review.html').read_text()
        self.assertNotIn('<script>alert(1)</script>', page)
        self.assertIn('&lt;script&gt;', page)
        (self.experiment / 'context.json').write_text('{}')
        self.assertEqual(report_data(self.experiment)['state']['context'], self.context)

    def test_container_command_has_no_authority_or_network_mounts(self):
        args = command('sha256:' + 'a' * 64, '/tmp/disposable', 'test')
        for option in ['--network=none', '--read-only', '--cap-drop=ALL', '--user=65534:65534',
                       '--security-opt=no-new-privileges', '--memory=128m', '--pids-limit=32', '--pull=never']:
            self.assertIn(option, args)
        self.assertEqual(args.count('--mount'), 1)
        self.assertIn('source=/tmp/disposable,target=/experiment,readonly', args[args.index('--mount') + 1])
        self.assertNotIn('--env-file', args)
        self.assertNotIn('/var/run/docker.sock', ' '.join(args))


@unittest.skipUnless(os.environ.get('WAKE_RUN_IMPROVEMENT_DOCKER_TESTS') == '1', 'Explicit disposable Docker acceptance only')
class ImprovementDockerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.image = image_identity(DEFAULT_IMAGE)

    def test_real_candidate_is_compared_by_external_scorer(self):
        population = cases(93, 60)
        result = run_program(CANDIDATE, population, self.image)
        self.assertEqual(result['status'], 'completed', result)
        self.assertEqual(score(population, result['outputs'])['passed'], 60)

    def test_real_timeout_and_output_flood_leave_no_success(self):
        timeout = run_program('while True: pass\n', [], self.image, timeout=1)
        self.assertEqual(timeout['status'], 'failed')
        self.assertIn('deadline', timeout['reason'])
        flood = run_program('while True: print("x" * 8192, flush=True)\n', [], self.image)
        self.assertEqual(flood['status'], 'failed')
        self.assertIn('output limit', flood['reason'])

    def test_real_container_has_no_secret_authority_or_writable_host_mount(self):
        source = '''import os, pathlib, socket
def decision_context(state, question=None):
    assert 'GEMINI_API_KEY' not in os.environ
    assert not pathlib.Path('/var/run/docker.sock').exists()
    assert not pathlib.Path('/data').exists()
    try:
        pathlib.Path('/experiment/marker').write_text('unsafe')
    except OSError:
        pass
    else:
        raise AssertionError('Host mount is writable')
    try:
        socket.create_connection(('192.0.2.1', 443), timeout=.2)
    except OSError:
        pass
    else:
        raise AssertionError('Unexpected outbound network')
    return {'isolated': True}
'''
        result = run_program(source, [{'state': {}, 'question': None}], self.image)
        self.assertEqual(result['status'], 'completed', result)
        self.assertEqual(result['outputs'], [{'isolated': True}])
