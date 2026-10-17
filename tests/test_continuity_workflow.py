"""Exercise the documented private Markdown workflow without operational records."""
import hashlib
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

from wake.installation_cli import _copy_public_site


ROOT = Path(__file__).resolve().parents[1]


class ContinuityWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        shutil.copytree(ROOT / 'docs/continuity', self.root / 'docs/continuity')
        self.blocks = re.findall(r'```sh\n(.*?)```',
                                 (self.root / 'docs/continuity/README.md').read_text(), re.S)

    def run_block(self, index, path=None, *, success=True):
        # Run the published steps verbatim; shell variables are supplied as data.
        result = subprocess.run(['bash', '-e', '-c', self.blocks[index]], cwd=self.root,
                                env={**os.environ,
                                     'checkpoint_dir': str(path) if path else ''},
                                text=True, capture_output=True)
        if success:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0)
        return result

    def create(self):
        output = self.run_block(0).stdout.strip()
        path = self.root / Path(output).parent
        text = (path / 'checkpoint.md').read_text()
        text = text.replace('ID: UNKNOWN', 'ID: ' + path.name, 1)
        text = text.replace('Recorded at: UNKNOWN', 'Recorded at: 2026-10-17T20:00:00+00:00', 1)
        text = text.replace('Context: UNKNOWN', 'Context: implementation', 1)
        (path / 'checkpoint.md').write_text(text)
        return path

    def test_documented_creation_sealing_and_recovery_detect_changes(self):
        path = self.create()
        self.run_block(1, path)
        self.run_block(2, path)
        expected = hashlib.sha256((path / 'checkpoint.md').read_bytes()).hexdigest()
        self.assertEqual((path / 'checkpoint.sha256').read_text().strip(), expected)
        original_seal = (path / 'checkpoint.sha256').read_bytes()
        self.run_block(1, path, success=False)
        self.assertEqual((path / 'checkpoint.sha256').read_bytes(), original_seal)
        with (path / 'checkpoint.md').open('a') as note:
            note.write('\nChanged after sealing.\n')
        failure = self.run_block(2, path, success=False)
        self.assertIn('checksum mismatch', failure.stderr)

    def test_revision_retains_predecessor_and_missing_context(self):
        previous = self.create()
        self.run_block(1, previous)
        original = (previous / 'checkpoint.md').read_bytes()
        digest = (previous / 'checkpoint.sha256').read_text().strip()
        revision = self.create()
        self.assertNotEqual(previous, revision)
        path = revision / 'checkpoint.md'
        text = path.read_text()
        text = re.sub(r'Previous checkpoint ID: .*', 'Previous checkpoint ID: ' + previous.name, text)
        text = re.sub(r'Previous checkpoint SHA-256: .*', 'Previous checkpoint SHA-256: ' + digest, text)
        text = re.sub(r'Revision rationale: .*', 'Revision rationale: New verified evidence corrects the prior interpretation.', text)
        path.write_text(text)
        self.run_block(1, revision)
        self.run_block(2, revision)
        self.run_block(2, previous)
        self.assertEqual((previous / 'checkpoint.md').read_bytes(), original)
        self.assertIn(previous.name, text)
        self.assertIn(digest, text)
        self.assertIn('Hypotheses and unverified assumptions', text)
        self.assertIn('Established observations and supporting evidence', text)
        self.assertIn('Decisions and rationale', text)
        self.assertIn('UNKNOWN — include inaccessible sources', text)
        summary = (self.root / 'docs/continuity/resumption-template.md').read_text()
        self.assertIn('Selected checkpoint IDs and SHA-256 digests', summary)
        self.assertIn('omit unrelated research', summary)

    def test_git_excludes_both_private_contexts(self):
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True, capture_output=True)
        shutil.copyfile(ROOT / '.gitignore', self.root / '.gitignore')
        for context in ('research', 'implementation'):
            name = f'.wake-continuity/{context}/example/checkpoint.md'
            path = self.root / name
            path.parent.mkdir(parents=True)
            path.write_text('private sentinel')
            result = subprocess.run(['git', 'check-ignore', '--', name], cwd=self.root,
                                    text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.strip(), name)
        tracked = subprocess.check_output(['git', 'ls-files', '--', '.wake-continuity'],
                                          cwd=self.root, text=True)
        self.assertEqual(tracked, '')

    def test_canonical_public_copy_excludes_private_notes(self):
        source = self.root / 'site'
        source.mkdir()
        for base in (source, source / 'blog'):
            for context in ('research', 'implementation'):
                path = base / '.wake-continuity' / context / 'checkpoint.html'
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('PRIVATE-CONTINUITY-CANARY')
        (source / 'blog/public.html').write_text('<html>Public article</html>')
        target = self.root / 'published'
        _copy_public_site(source, target)
        self.assertEqual((target / 'blog/public.html').read_text(), '<html>Public article</html>')
        self.assertFalse(any('.wake-continuity' in p.parts for p in target.rglob('*')))
        self.assertNotIn('PRIVATE-CONTINUITY-CANARY',
                         ''.join(p.read_text() for p in target.rglob('*') if p.is_file()))
