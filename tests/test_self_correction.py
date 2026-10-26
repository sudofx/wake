"""Source correction cannot widen its path allowance or apply to a stale base."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('source_correction', ROOT / 'scripts/self_correction.py')
correction = importlib.util.module_from_spec(spec)
spec.loader.exec_module(correction)


class SourceCorrectionTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name).resolve()
        (self.root / 'wake/assets').mkdir(parents=True)
        (self.root / 'docs').mkdir()
        (self.root / 'wake/assets/reader.js').write_text('const reader = 1;\n')
        (self.root / 'docs/reader.md').write_text('# Reader\n')
        for args in [('init', '-b', 'master'), ('config', 'user.email', 'test@localhost'),
                     ('config', 'user.name', 'test'), ('add', '.'), ('commit', '-m', 'base')]:
            subprocess.run(['git', '-C', str(self.root), *args], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.plan = {'schema': correction.SCHEMA, 'base_revision': correction.git(self.root, 'rev-parse', 'HEAD'),
                     'request': 'Make the reader display correctly.', 'model': correction.MODEL,
                     'title': 'Repair reader', 'summary': 'A bounded presentation correction.',
                     'changes': [{'path': 'wake/assets/reader.js', 'before_sha256': self.hash('wake/assets/reader.js'),
                                  'content': 'const reader = 2;\n'}]}

    def hash(self, path):
        return hashlib.sha256((self.root / path).read_bytes()).hexdigest()

    def test_only_selected_existing_presentation_or_docs_can_change(self):
        self.assertEqual(correction.validate_plan(self.root, self.plan, paths={'wake/assets/reader.js'}), self.plan)
        for path in ('../README.md', '/tmp/a.js', 'wake/assets/../engine.py', 'wake/kernel/record.py',
                     'wake/engine.py', 'tests/test_reader.py', '.github/workflows/test.yml',
                     'wake/assets/ask-bob-engine.json', 'docs/nested/a.md', './docs/reader.md', 'new.js'):
            with self.subTest(path=path), self.assertRaises(ValueError):
                correction.allowed_path(path)
        with self.assertRaisesRegex(ValueError, 'Unselected'):
            correction.validate_plan(self.root, self.plan, paths={'docs/reader.md'})
        self.plan['changes'][0]['path'] = 'wake/assets/missing.js'
        with self.assertRaisesRegex(ValueError, 'existing'):
            correction.validate_plan(self.root, self.plan)

    def test_untracked_or_modified_source_is_not_a_base_file(self):
        (self.root / 'wake/assets/untracked.js').write_text('const untracked=1;')
        with self.assertRaisesRegex(ValueError, 'tracked'):
            correction.capture(self.root, ['wake/assets/untracked.js'])
        (self.root / 'wake/assets/reader.js').write_text('const reader=42;')
        with self.assertRaisesRegex(ValueError, 'committed base'):
            correction.capture(self.root, ['wake/assets/reader.js'])

    def test_rejects_stale_hashes_revision_and_extra_permissions(self):
        self.plan['changes'][0]['before_sha256'] = 'a' * 64
        with self.assertRaisesRegex(ValueError, 'hash changed'):
            correction.validate_plan(self.root, self.plan)
        self.plan['changes'][0]['before_sha256'] = self.hash('wake/assets/reader.js')
        self.plan['base_revision'] = 'b' * 40
        with self.assertRaisesRegex(ValueError, 'revision changed'):
            correction.validate_plan(self.root, self.plan)
        self.plan['base_revision'] = correction.git(self.root, 'rev-parse', 'HEAD')
        self.plan['permissions'] = 'merge'
        with self.assertRaisesRegex(ValueError, 'fields'):
            correction.validate_plan(self.root, self.plan)

    def test_rejects_symlink_file_and_parent(self):
        (self.root / 'wake/assets/link.js').symlink_to(self.root / 'wake/assets/reader.js')
        with self.assertRaisesRegex(ValueError, 'regular'):
            correction.capture(self.root, ['wake/assets/link.js'])
        (self.root / 'docs').rename(self.root / 'actual-docs')
        (self.root / 'docs').symlink_to(self.root / 'actual-docs', target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'Symlinked'):
            correction.capture(self.root, ['docs/reader.md'])

    def test_validates_every_change_before_any_write(self):
        self.plan['changes'].append({'path': 'wake/assets/other.js', 'before_sha256': 'a' * 64, 'content': 'broken'})
        plan_file = self.root / 'proposal.json'
        plan_file.write_text(json.dumps(self.plan))
        before = (self.root / 'wake/assets/reader.js').read_bytes()
        with self.assertRaises(ValueError):
            correction.apply(self.root, plan_file)
        self.assertEqual((self.root / 'wake/assets/reader.js').read_bytes(), before)

    def test_apply_writes_text_without_running_candidate(self):
        marker = self.root / 'executed'
        self.plan['changes'][0]['content'] = f'require("fs").writeFileSync({json.dumps(str(marker))}, "bad");\n'
        plan_file = self.root / 'proposal.json'
        plan_file.write_text(json.dumps(self.plan))
        correction.apply(self.root, plan_file)
        self.assertFalse(marker.exists())
        self.assertEqual(correction.git(self.root, 'diff', '--name-only'), 'wake/assets/reader.js')
        with self.assertRaisesRegex(ValueError, 'local edits'):
            correction.apply(self.root, plan_file)

    def test_rejects_duplicate_unchanged_and_oversized_candidates(self):
        self.plan['changes'].append(dict(self.plan['changes'][0]))
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            correction.validate_plan(self.root, self.plan)
        self.plan['changes'].pop()
        self.plan['changes'][0]['content'] = (self.root / 'wake/assets/reader.js').read_text()
        with self.assertRaisesRegex(ValueError, 'unchanged'):
            correction.validate_plan(self.root, self.plan)
        self.plan['changes'][0]['content'] = 'a' * (correction.MAX_FILE_BYTES + 1)
        with self.assertRaisesRegex(ValueError, 'oversized'):
            correction.validate_plan(self.root, self.plan)

    def test_one_provider_call_records_exact_proposal_and_does_not_apply_it(self):
        candidate = {key: self.plan[key] for key in ('title', 'summary', 'changes')}
        response = {'candidates': [{'finishReason': 'STOP', 'content': {
            'parts': [{'text': json.dumps(candidate)}]}}]}
        from io import BytesIO
        output = self.root / 'generated'
        with patch.dict('os.environ', {'GEMINI_API_KEY': 'fixture-not-a-key'}), \
                patch('urllib.request.urlopen', return_value=BytesIO(json.dumps(response).encode())) as call:
            correction.generate(self.root, ['wake/assets/reader.js'], self.plan['request'], output)
        call.assert_called_once()
        request = call.call_args.args[0]
        self.assertTrue(request.full_url.startswith('https://generativelanguage.googleapis.com/'))
        self.assertNotIn('fixture-not-a-key', request.full_url)
        self.assertNotIn('fixture-not-a-key', request.data.decode())
        self.assertEqual(json.loads(request.data)['generationConfig']['thinkingConfig'],
                         {'thinkingLevel': 'low'})
        plan = json.loads((output / 'proposal.json').read_text())
        correction.validate_plan(self.root, plan)
        receipt = json.loads((output / 'receipt.json').read_text())
        self.assertEqual(receipt['provider_calls'], 1)
        self.assertEqual(receipt['proposal_sha256'], hashlib.sha256((output / 'proposal.json').read_bytes()).hexdigest())
        self.assertEqual((self.root / 'wake/assets/reader.js').read_text(), 'const reader = 1;\n')

    def test_generation_needs_secret_and_does_not_make_provider_call_when_missing(self):
        with patch.dict('os.environ', {}, clear=True), patch('urllib.request.urlopen') as call:
            with self.assertRaisesRegex(ValueError, 'GEMINI_API_KEY'):
                correction.generate(self.root, ['wake/assets/reader.js'], 'Repair the reader display.', self.root / 'output')
            call.assert_not_called()


    def review_remote(self):
        remote = Path(self.directory.name) / 'remote.git'
        subprocess.run(['git', 'init', '--bare', '-b', 'master', str(remote)],
                       check=True, capture_output=True)
        correction.git(self.root, 'remote', 'add', 'origin', str(remote))
        correction.git(self.root, 'push', 'origin', 'master')
        plan_file = self.root / 'proposal.json'
        plan_file.write_text(json.dumps(self.plan))
        body = self.root / 'review.md'
        body.write_text('Review this bounded candidate.')
        return remote, plan_file, body

    def fresh_review_checkout(self, remote, name):
        checkout = Path(self.directory.name) / name
        subprocess.run(['git', 'clone', '--quiet', str(remote), str(checkout)],
                       check=True, capture_output=True)
        return checkout

    def test_review_retry_reuses_pushed_commit_after_pr_creation_failure(self):
        remote, plan_file, body = self.review_remote()
        branch = 'wake-correction/123'
        def blocked(*args):
            if args[1:3] == ('pr', 'list'):
                return '[]'
            raise subprocess.CalledProcessError(1, 'gh pr create')
        with patch.object(correction, 'gh', side_effect=blocked):
            with self.assertRaises(subprocess.CalledProcessError):
                correction.publish_review(self.root, plan_file, branch, body)
        head = correction.git(self.root, 'ls-remote', '--heads', 'origin', branch).split()[0]
        url = 'https://github.com/sudofx/wake/pull/123'
        def available(*args):
            if args[1:3] == ('pr', 'list'):
                return '[]'
            if args[1:3] == ('pr', 'create'):
                return url
            if args[1:3] == ('pr', 'view'):
                return json.dumps({'url': url, 'headRefOid': head})
            raise AssertionError(args)
        retry = self.fresh_review_checkout(remote, 'retry')
        with patch.object(correction, 'gh', side_effect=available):
            result = correction.publish_review(retry, plan_file, branch, body)
        self.assertEqual(result['head_revision'], head)
        self.assertEqual(result['status'], 'review_created')
        self.assertEqual(correction.git(retry, 'ls-remote', '--heads', 'origin', branch).split()[0], head)
        again = self.fresh_review_checkout(remote, 'again')
        with patch.object(correction, 'gh', return_value=json.dumps([{'url': url, 'headRefOid': head, 'state': 'OPEN'}])) as calls:
            result = correction.publish_review(again, plan_file, branch, body)
        self.assertEqual(result['status'], 'review_existing')
        self.assertEqual(result['head_revision'], head)
        calls.assert_called_once()

    def test_review_retry_rejects_a_branch_with_a_different_candidate(self):
        remote, plan_file, body = self.review_remote()
        correction.git(self.root, 'switch', '-c', 'wake-correction/456')
        (self.root / 'wake/assets/reader.js').write_text('const reader = 99;\n')
        correction.git(self.root, 'add', '--', 'wake/assets/reader.js')
        correction.git(self.root, 'commit', '-m', 'different candidate')
        correction.git(self.root, 'push', 'origin', 'HEAD:refs/heads/wake-correction/456')
        head = correction.git(self.root, 'rev-parse', 'HEAD')
        retry = self.fresh_review_checkout(remote, 'retry')
        with patch.object(correction, 'gh') as calls:
            with self.assertRaisesRegex(ValueError, 'differs from this proposal'):
                correction.publish_review(retry, plan_file, 'wake-correction/456', body)
        calls.assert_not_called()
        self.assertEqual(correction.git(retry, 'ls-remote', '--heads', 'origin', 'wake-correction/456').split()[0], head)


if __name__ == '__main__':
    unittest.main()
