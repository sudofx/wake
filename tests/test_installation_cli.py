"""Manual transport rejects invalid records before replacing active authority."""
import json
from pathlib import Path
import tempfile
import socket
import subprocess
import stat
import threading
import unittest
from unittest.mock import patch
import zipfile

from wake.installation_cli import NODE_IDS, export_records, import_records, verify_import, main, request, publish_artifact, _copy_public_site, _public_projection, control_socket
from wake.kernel.record import Record


class InstallationArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        from wake.record_store import RecordStore
        from wake.engine import Engine, DEFAULTS
        for node in NODE_IDS:
            path = self.root / 'nodes' / node / 'record' / 'wake.sqlite'
            path.parent.mkdir(parents=True)
            store = RecordStore(path.parent, initialize_empty=True)
            Engine(path.parent, dict(DEFAULTS), store=store).initialize()
            store.close()
        self.archive = self.root / 'backups' / 'manual.zip'

    def tearDown(self):
        self.temp.cleanup()

    def test_export_verifies_all_records_and_import_preserves_manual_archives(self):
        manifest = export_records(self.root, self.archive)
        self.assertEqual(verify_import(self.archive), manifest)
        (self.root / 'nodes' / '100.wake' / 'private.txt').write_text('old data')
        import_records(self.root, self.archive)
        self.assertFalse((self.root / 'nodes' / '100.wake' / 'private.txt').exists())
        self.assertTrue(self.archive.exists())
        self.assertEqual(Record.open_read_only(self.root / 'nodes' / '100.wake' / 'record' / 'wake.sqlite').full_replay()[0], manifest['nodes']['100.wake']['revision'])
        with self.assertRaises(FileExistsError):
            export_records(self.root, self.archive)

    def test_generic_kernel_record_is_not_reloadable_wake_authority(self):
        path = self.root / 'nodes' / '100.wake' / 'record' / 'wake.sqlite'
        path.unlink()
        Record(path)
        with self.assertRaisesRegex(ValueError, 'initialized WAKE'):
            export_records(self.root, self.archive)
        self.assertFalse(self.archive.exists())

    def test_corrupt_import_leaves_active_records_untouched(self):
        export_records(self.root, self.archive)
        bad = self.root / 'backups' / 'bad.zip'
        with zipfile.ZipFile(self.archive) as source, zipfile.ZipFile(bad, 'w') as target:
            for entry in source.infolist():
                body = source.read(entry.filename)
                if entry.filename == 'manifest.json':
                    manifest = json.loads(body)
                    manifest['nodes']['100.wake']['sha256'] = '0' * 64
                    body = json.dumps(manifest).encode()
                target.writestr(entry.filename, body)
        original = (self.root / 'nodes' / '100.wake' / 'record' / 'wake.sqlite').read_bytes()
        with self.assertRaisesRegex(ValueError, 'verified manifest'):
            import_records(self.root, bad)
        self.assertEqual((self.root / 'nodes' / '100.wake' / 'record' / 'wake.sqlite').read_bytes(), original)

    def test_unknown_archive_member_and_duplicate_paths_rejected(self):
        export_records(self.root, self.archive)
        with zipfile.ZipFile(self.archive, 'a') as archive:
            archive.writestr('../escape', 'bad')
        with self.assertRaisesRegex(ValueError, 'exactly'):
            verify_import(self.archive)
        self.assertFalse((self.root.parent / 'escape').exists())

    def test_archive_symlink_is_rejected_before_any_read(self):
        export_records(self.root, self.archive)
        bad = self.root / 'backups' / 'link.zip'
        with zipfile.ZipFile(self.archive) as source, zipfile.ZipFile(bad, 'w') as target:
            for entry in source.infolist():
                if entry.filename == 'nodes/100.wake/record/wake.sqlite':
                    entry.external_attr = (stat.S_IFLNK | 0o777) << 16
                target.writestr(entry, source.read(entry.filename))
        with self.assertRaisesRegex(ValueError, 'links'):
            verify_import(bad)

    def test_publication_fails_closed_without_dedicated_configuration(self):
        with patch.dict('os.environ', {}, clear=True):
            with self.assertRaisesRegex(ValueError, 'Configure'):
                publish_artifact(self.root)
        with patch.dict('os.environ', {'WAKE_PUBLISH_REPOSITORY': 'https://github.com/example/repo', 'WAKE_PUBLISH_BRANCH': 'master'}, clear=True):
            with self.assertRaisesRegex(ValueError, 'Configure'):
                publish_artifact(self.root)

    def test_local_control_transport_requires_complete_acknowledgment(self):
        server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        server.bind(str(control_socket(self.root)))
        server.listen(1)
        received = []
        def answer():
            with server:
                connection, _ = server.accept()
                with connection:
                    received.append(json.loads(connection.recv(4096)))
                    connection.sendall(b'{"ok":true,"nodes":{"100.wake":"stopped"}}\n')
        thread = threading.Thread(target=answer)
        thread.start()
        try:
            result = request(self.root, {'action': 'stop'})
            self.assertTrue(result['ok'])
            self.assertEqual(result['nodes']['100.wake'], 'stopped')
        finally:
            thread.join(timeout=2)
            control_socket(self.root).unlink(missing_ok=True)
        self.assertEqual(received, [{'action': 'stop'}])

    def test_public_copy_excludes_private_files_and_redacts_provider_bodies(self):
        source = self.root / 'public-source'
        source.mkdir()
        (source / 'research-data.json').write_text(json.dumps({'head': 'receipt', 'traces': [
            {'request': {'secret': 'prompt-secret'}, 'response': 'response-secret',
             'attempts': [{'http_status': 429}], 'context': {'system': 'system-secret', 'characters': 4}}]}))
        event = {'text': 'first\u2028second\u0085third', 'request': {'secret': 'private'}}
        (source / 'events.jsonl').write_text(json.dumps(event, ensure_ascii=False) + '\n')
        (source / 'console-state.html').write_text('<html>State view</html>')
        (source / 'journal').mkdir()
        (source / 'journal/receipt.html').write_text('<html>Journal</html>')
        (source / 'blog').mkdir()
        (source / 'blog/post.html').write_text('<html><head><script>window.WAKE_DEPLOYMENT={"schema":1,"mode":"standalone"};window.WAKE_STANDALONE=true;</script></head><body><a href="/runtime.json">Inspect local WAKE runtime</a><a class="actions-light" href="/runtime.json"><span><i></i></span></a></body></html>')
        (source / '.passenger.md').write_text('passenger-secret')
        (source / 'worker.log').write_text('log-secret')
        (source / 'group').mkdir()
        (source / 'group' / 'bob-input.json').write_text('{"input":"peer-private"}')
        target = self.root / 'artifact'
        _copy_public_site(source, target)
        projected = json.loads((target / 'research-data.json').read_text())
        self.assertEqual(projected['traces'][0]['attempts'][0]['http_status'], 429)
        self.assertEqual(json.loads((target / 'events.jsonl').read_text()), {'text': event['text']})
        self.assertNotIn('secret', json.dumps(projected))
        self.assertTrue((target / 'console-state.html').exists())
        self.assertTrue((target / 'journal/receipt.html').exists())
        self.assertIn('href="../installation.json"',(target / 'blog/post.html').read_text())
        self.assertIn("dataset.wakeSnapshotOnly='true'",(target / 'blog/post.html').read_text())
        self.assertNotIn('class="actions-light"', (target / 'blog/post.html').read_text())
        self.assertFalse((target / '.passenger.md').exists())
        self.assertFalse((target / 'worker.log').exists())
        self.assertFalse((target / 'group' / 'bob-input.json').exists())

    def test_real_application_records_export_import_and_reopen(self):
        from wake.engine import Engine, DEFAULTS
        from wake.record_store import RecordStore
        for node in NODE_IDS:
            store = RecordStore(self.root / 'nodes' / node / 'record', initialize_empty=True)
            Engine(store.directory, dict(DEFAULTS), store=store).initialize()
            store.close()
        manifest = export_records(self.root, self.archive)
        self.assertTrue(all(entry['revision'] > 0 for entry in manifest['nodes'].values()))
        import_records(self.root, self.archive)
        for node in NODE_IDS:
            store = RecordStore(self.root / 'nodes' / node / 'record')
            self.assertEqual(store.record.full_replay()[0], manifest['nodes'][node]['revision'])
            store.close()

    def test_publication_retains_existing_branch_history_without_force(self):
        commands = []
        def build(root, destination):
            destination.mkdir()
            (destination / 'index.html').write_text('public')
            return {'schema': 1}
        def run(command, **kwargs):
            commands.append(command)
            return subprocess.CompletedProcess(command, 0, stdout=b'abc refs/heads/public-mirror\n' if 'ls-remote' in command else b'', stderr=b'')
        with patch.dict('os.environ', {'WAKE_PUBLISH_REPOSITORY': 'https://github.com/example/repo',
                                      'WAKE_PUBLISH_BRANCH': 'public-mirror'}, clear=True), \
             patch('wake.installation_cli.build_public_artifact', side_effect=build), \
             patch('wake.installation_cli.subprocess.run', side_effect=run):
            self.assertEqual(publish_artifact(self.root), {'schema': 1})
        self.assertTrue(any('fetch' in command for command in commands))
        self.assertTrue(any('FETCH_HEAD' in command for command in commands))
        pushes = [command for command in commands if 'push' in command]
        self.assertEqual(pushes, [['git', 'push', 'origin', 'HEAD:refs/heads/public-mirror']])

    def test_cli_never_resets_directly_and_requires_uppercase(self):
        with patch('wake.installation_cli.request', return_value={'ok': True}) as request:
            self.assertEqual(main(['--data', str(self.root), 'RESET']), 0)
            request.assert_called_once_with(self.root, {'action': 'RESET'})
        with self.assertRaises(SystemExit):
            main(['reset'])
        with patch('wake.installation_cli.request') as request:
            self.assertEqual(main(['import', '../bad.zip']), 1)
            request.assert_not_called()


if __name__ == '__main__':
    unittest.main()
