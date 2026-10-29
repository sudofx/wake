"""Trusted repairs have an exact language; autonomous attempts cannot loop or clobber master."""
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('automatic_correction', ROOT / 'scripts/automatic_self_correction.py')
auto = importlib.util.module_from_spec(spec)
spec.loader.exec_module(auto)
source = auto.source


class AutomaticCorrectionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'checkout'
        directory = self.root / 'wake/assets/self-correction'
        directory.mkdir(parents=True)
        (directory / 'index.html').write_text('<link href="self-correction.css?v=old"><script src="self-correction.js?v=old" defer></script>\n')
        (directory / 'self-correction.js').write_text('const correction = 1;\n')
        (directory / 'self-correction.css').write_text('body { color: black; }\n')
        (self.root / 'wake/assets/reader.js').write_text('const reader = 1;\n')
        for args in [('init', '-b', 'master'), ('config', 'user.name', 'Test'), ('config', 'user.email', 'test@localhost'), ('add', '.'), ('commit', '-m', 'base')]:
            subprocess.run(['git', '-C', str(self.root), *args], check=True, capture_output=True)
        self.base = source.git(self.root, 'rev-parse', 'HEAD')
        self.output = Path(self.tmp.name) / 'report'

    def commit(self):
        source.git(self.root, 'add', '.')
        source.git(self.root, 'commit', '-m', 'fixture change')

    def fix_cache(self):
        plan = auto.mechanical_plan(self.root)
        (self.root / auto.INDEX).write_text(plan['content'])
        (self.root / 'fixture.txt').write_text('Checked fixture base, not an automatic repair commit.')
        self.commit()

    def test_exact_transform_does_not_authorize_other_source_changes(self):
        plan = auto.mechanical_plan(self.root)
        self.assertEqual(auto.validate_mechanical(self.root, plan), plan)
        self.assertNotIn('?v=old', plan['content'])
        for key, value in [('content', plan['content'] + '<script src="https://evil.invalid"></script>'),
                           ('path', 'wake/engine.py'), ('base_revision', '0' * 40),
                           ('before_sha256', '0' * 64), ('permission', 'merge-anything')]:
            altered = {**plan, key: value}
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, 'exact trusted'):
                auto.validate_mechanical(self.root, altered)

    def test_mechanical_application_is_idempotent_after_new_commit(self):
        self.fix_cache()
        self.assertIsNone(auto.mechanical_plan(self.root))

    def test_source_symlink_and_uncommitted_bytes_fail_closed(self):
        file = self.root / 'wake/assets/self-correction/self-correction.js'
        original = file.read_text()
        file.write_text(original + '// dirty')
        with self.assertRaisesRegex(ValueError, 'committed base'):
            auto.mechanical_plan(self.root)
        file.unlink()
        file.symlink_to(self.root / 'wake/assets/reader.js')
        with self.assertRaisesRegex(ValueError, 'regular'):
            auto.mechanical_plan(self.root)

    def test_healthy_check_needs_no_provider_or_github_history(self):
        self.fix_cache()
        with patch.object(auto, 'api') as api, patch.object(source, 'generate') as generate:
            report = auto.inspect(self.root, self.output, {}, repository='sudofx/wake')
        self.assertEqual((report['mode'], report['outcome']), ('none', 'healthy'))
        api.assert_not_called()
        generate.assert_not_called()
        self.assertEqual(report['research_records_opened'], 0)

    def test_real_syntax_fault_selects_own_path_without_operator_input(self):
        self.fix_cache()
        (self.root / 'wake/assets/reader.js').write_text('const broken = ;\n')
        self.commit()
        with patch.object(auto, 'model_budget', return_value=(True, 'capacity')):
            report = auto.inspect(self.root, self.output, {}, repository='sudofx/wake')
        self.assertEqual(report['mode'], 'model')
        self.assertEqual(report['paths'], 'wake/assets/reader.js')
        self.assertIn('syntax', report['request'])
        self.assertEqual(report['provider_calls'], 0)

    def test_failed_research_does_not_grant_runtime_rewrite(self):
        self.fix_cache()
        report = auto.inspect(self.root, self.output, {'workflow_run': {'name': 'WAKE — Research worker', 'conclusion': 'failure'}}, repository='sudofx/wake')
        self.assertEqual(report['outcome'], 'outside_scope')
        self.assertEqual(report['mode'], 'none')

    def test_same_source_candidate_does_not_repeat_even_after_failed_test(self):
        with patch.object(auto, 'recent_attempts', return_value=[('test', self.base)]):
            report = auto.inspect(self.root, self.output, {}, repository='sudofx/wake')
        self.assertEqual(report['outcome'], 'budget_wait')
        self.assertEqual(report['mode'], 'none')

    def test_failed_publication_can_reuse_checked_publisher_once(self):
        self.fix_cache()
        base = source.git(self.root, 'rev-parse', 'HEAD')
        event = {'workflow_run': {'name': 'WAKE — Publish website', 'conclusion': 'failure'}}
        checked = {'workflow_runs': [{'head_branch': 'master', 'head_sha': base, 'event': 'push'}]}
        with patch.object(auto, 'api', return_value=checked), patch.object(auto, 'recent_attempts', return_value=[]):
            report = auto.inspect(self.root, self.output, event, repository='sudofx/wake')
        self.assertEqual(report['mode'], 'republish')
        with patch.object(auto, 'api', return_value=checked), patch.object(auto, 'recent_attempts', return_value=[('republish', base)]):
            report = auto.inspect(self.root, self.output, event, repository='sudofx/wake')
        self.assertEqual(report['mode'], 'none')
        self.assertEqual(report['outcome'], 'budget_wait')

    def test_applied_mechanical_head_recovers_missing_ci_without_reapplying(self):
        plan = auto.mechanical_plan(self.root)
        (self.root / auto.INDEX).write_text(plan['content'])
        self.commit()
        base = source.git(self.root, 'rev-parse', 'HEAD')
        self.assertTrue(auto.mechanical_head(self.root, base))
        with patch.object(auto, 'api', return_value={'workflow_runs': []}):
            report = auto.inspect(self.root, self.output, {}, repository='sudofx/wake')
        self.assertEqual((report['mode'], report['outcome']), ('check_source', 'pending'))
        runs = {'workflow_runs': [{'head_sha': base, 'head_branch': 'master', 'event': 'workflow_dispatch',
                                  'status': 'in_progress', 'conclusion': None}]}
        with patch.object(auto, 'api', return_value=runs):
            report = auto.inspect(self.root, self.output, {}, repository='sudofx/wake')
        self.assertEqual((report['mode'], report['outcome']), ('none', 'delivery_wait'))
        runs['workflow_runs'][0].update(status='completed', conclusion='failure')
        with patch.object(auto, 'api', return_value=runs):
            report = auto.inspect(self.root, self.output, {}, repository='sudofx/wake')
        self.assertEqual(report['outcome'], 'outside_scope')

    def test_publication_requires_exact_full_ci_even_if_other_source_passed(self):
        with patch.object(auto, 'api', return_value={'workflow_runs': [{'head_sha': '0' * 40, 'head_branch': 'master', 'event': 'push'}]}):
            with self.assertRaisesRegex(ValueError, 'Exact source base'):
                auto.verify_base(self.root, 'sudofx/wake')
        with patch.object(auto, 'api', return_value={'workflow_runs': [{'head_sha': self.base, 'head_branch': 'master', 'event': 'push'}]}):
            auto.verify_base(self.root, 'sudofx/wake')

    def test_failed_current_ci_selects_only_a_wholly_allowed_commit(self):
        self.fix_cache()
        (self.root / 'wake/assets/reader.js').write_text('const reader = 2;\n')
        self.commit()
        base = source.git(self.root, 'rev-parse', 'HEAD')
        event = {'workflow_run': {'name': 'WAKE✳︎ — Check code · automatic',
                                 'head_sha': base, 'conclusion': 'failure', 'id': 42}}
        jobs = {'jobs': [{'steps': [{'name': 'Existing regression suite', 'conclusion': 'failure'}]}]}
        with patch.object(auto, 'api', return_value=jobs), patch.object(auto, 'model_budget', return_value=(True, 'capacity')):
            report = auto.inspect(self.root, self.output, event, repository='sudofx/wake')
        self.assertEqual(report['mode'], 'model')
        self.assertEqual(report['outcome'], 'pending')
        self.assertEqual(report['paths'], 'wake/assets/reader.js')
        self.assertIn('Existing regression suite', report['request'])
        (self.root / 'wake/engine.py').write_text('# runtime is outside source allowance\n')
        self.commit()
        event['workflow_run']['head_sha'] = source.git(self.root, 'rev-parse', 'HEAD')
        with patch.object(auto, 'api') as api:
            report = auto.inspect(self.root, self.output, event, repository='sudofx/wake')
        self.assertEqual(report['outcome'], 'outside_scope')
        api.assert_not_called()

    def test_diagnosis_never_claims_a_known_fault_is_healthy(self):
        with patch.object(auto, 'recent_attempts', return_value=[]):
            report = auto.inspect(self.root, self.output, {}, repository='sudofx/wake')
        self.assertEqual(report['mode'], 'mechanical')
        self.assertEqual(report['outcome'], 'pending')

    def test_daily_model_cap_and_same_source_attempts_include_failures(self):
        now = datetime(2026, 10, 29, tzinfo=timezone.utc)
        with patch.object(auto, 'recent_attempts', return_value=[('propose', str(i)) for i in range(4)]):
            self.assertFalse(auto.model_budget(self.root, 'sudofx/wake', self.base, now)[0])
        with patch.object(auto, 'recent_attempts', return_value=[('propose', self.base)]):
            self.assertFalse(auto.model_budget(self.root, 'sudofx/wake', self.base, now)[0])
        with patch.object(auto, 'recent_attempts', return_value=None):
            self.assertFalse(auto.model_budget(self.root, 'sudofx/wake', self.base, now)[0])

    def test_nonforced_publish_rejects_concurrent_master_without_dispatching_ci(self):
        remote = Path(self.tmp.name) / 'remote.git'
        subprocess.run(['git', 'init', '--bare', str(remote)], check=True, capture_output=True)
        source.git(self.root, 'remote', 'add', 'origin', str(remote))
        source.git(self.root, 'push', 'origin', 'master')
        # A second writer advances master after the trusted repair captured its base.
        other = Path(self.tmp.name) / 'other'
        subprocess.run(['git', 'clone', '--branch', 'master', str(remote), str(other)], check=True, capture_output=True)
        source.git(other, 'config', 'user.name', 'Other')
        source.git(other, 'config', 'user.email', 'other@localhost')
        (other / 'another.txt').write_text('Concurrent change must survive.')
        source.git(other, 'add', '.')
        source.git(other, 'commit', '-m', 'Concurrent work')
        source.git(other, 'push', 'origin', 'master')
        concurrent = source.git(other, 'rev-parse', 'HEAD')
        plan_file = Path(self.tmp.name) / 'mechanical.json'
        plan_file.write_text(json.dumps(auto.mechanical_plan(self.root)))
        with patch.object(source, 'gh') as gh:
            with self.assertRaises(subprocess.CalledProcessError):
                auto.publish_mechanical(self.root, plan_file, 'sudofx/wake')
        gh.assert_not_called()
        self.assertEqual(source.git(self.root, 'ls-remote', 'origin', 'refs/heads/master').split()[0], concurrent)

    def test_workflow_permissions_isolation_and_event_contract(self):
        workflow = (ROOT / '.github/workflows/self-correction.yml').read_text()
        self.assertIn('workflow_run:', workflow)
        self.assertIn('required: false', workflow)
        self.assertIn('head_repository.full_name == github.repository', workflow)
        self.assertIn('fetch-depth: 2', workflow, 'CI diagnosis needs the committed parent')
        self.assertNotIn('pull_request_target', workflow)
        self.assertIn('--network none --read-only --cap-drop ALL', workflow)
        self.assertIn('uses: ./.github/workflows/publish-pages.yml', workflow)
        self.assertIn('Outcome:', workflow)
        self.assertNotIn('schedule:', workflow)


if __name__ == '__main__':
    unittest.main()
