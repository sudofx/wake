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
        for branch in ('master', 'wake-runtime', 'wake-state', 'wake-live'):
            with patch.dict('os.environ', {'WAKE_PUBLISH_REPOSITORY': 'https://github.com/example/repo', 'WAKE_PUBLISH_BRANCH': branch}, clear=True):
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

    def test_public_overview_bounds_history_without_truncating_complete_export(self):
        source = self.root / 'history-source'
        source.mkdir()
        events = [{'seq': n, 'text': 'exact\u2028text'} for n in range(405)]
        (source / 'wake-data.json').write_text(json.dumps({'state': {'version': 19},
            'metrics': {'storage': {'event_count': 405}}, 'events': events}))
        (source / 'events.jsonl').write_text(''.join(json.dumps(e, ensure_ascii=False) + '\n' for e in events))
        target = self.root / 'history-artifact'
        _copy_public_site(source, target)
        packet = json.loads((target / 'wake-data.json').read_text())
        self.assertEqual(packet['events'], events[-400:])
        self.assertEqual(packet['state']['version'], 19)
        self.assertEqual(packet['metrics']['storage']['event_count'], 405)
        self.assertEqual(packet['event_history'], {'displayed': 400, 'total': 405, 'complete_url': 'events.jsonl'})
        self.assertEqual([json.loads(line) for line in (target / 'events.jsonl').read_text().split('\n') if line], events)

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

    def test_pinned_generation_survives_retirement_and_copy_fallback(self):
        from wake.installation_cli import _pin_export_file
        source, pinned = self.root / 'generation', self.root / 'pin'
        source.write_text('complete exported snapshot')
        _pin_export_file(source, pinned)
        source.unlink()
        self.assertEqual(pinned.read_text(), 'complete exported snapshot')
        source.write_text('another snapshot')
        with patch('wake.installation_cli.os.link', side_effect=OSError('Hardlinks unavailable')):
            _pin_export_file(source, self.root / 'copied-pin')
        source.unlink()
        self.assertEqual((self.root / 'copied-pin').read_text(), 'another snapshot')

    def test_public_artifact_identifies_exports_without_opening_live_authority(self):
        from wake.installation_cli import build_public_artifact
        from wake.engine import Engine, DEFAULTS
        from wake.record_store import RecordStore
        from wake.report import export
        (self.root / 'installation-id.json').write_text(json.dumps({'id': 'test-installation'}))
        exported = {}
        for node in NODE_IDS:
            base = self.root / 'nodes' / node
            store = RecordStore(base / 'record')
            target = base / 'site' / 'current'
            export(store, target, standalone=True)
            exported[node] = store.replay()[1]
            store.close()
        (self.root / 'nodes' / NODE_IDS[0] / 'runtime.json').write_text(json.dumps({
            'state': 'running', 'observed_at': '2026-10-14T18:00:00+00:00', 'private': 'private-runtime-marker'}))
        messages = []
        # Load the unified exporter before the node-render guard, so its module
        # binding cannot retain a temporary mock after this test finishes.
        from wake import installation_site
        with patch('wake.installation_cli._record_metadata', side_effect=AssertionError('Live record read forbidden')), \
             patch('wake.report.export', side_effect=lambda store, target, **kwargs: export(store, target, **kwargs) if Path(target).name == 'unified' else (_ for _ in ()).throw(AssertionError('Compatible node pages rendered twice'))):
            manifest = build_public_artifact(self.root, self.root / 'public', progress=messages.append)
        self.assertEqual(manifest['nodes'][0]['recorded_runtime'], {'state': 'running', 'observed_at': '2026-10-14T18:00:00+00:00'})
        self.assertNotIn('private-runtime-marker', json.dumps(manifest))
        self.assertEqual(sum(message.startswith('Capturing ') for message in messages), 12)
        self.assertEqual(sum(message.startswith('Reusing completed website pages') for message in messages), 12)
        self.assertEqual({node: data['head'] for node, data in manifest['record_heads'].items()}, exported)
        self.assertFalse(manifest['live'])
        full = (self.root / 'public/events.jsonl').read_text().splitlines()
        overview = json.loads((self.root / 'public/wake-data.json').read_text())
        self.assertEqual(overview['event_history']['total'], len(full))
        self.assertTrue(all(json.loads(line)['origin']['node'] in NODE_IDS for line in full))
        self.assertFalse(list((self.root / 'public').rglob('*.sqlite')))
        # Older or mismatched renderers rebuild once rather than serving stale pages.
        marker = self.root / 'nodes' / NODE_IDS[0] / 'site/current/export-format.json'
        marker.write_text('{damaged compatibility hint')
        with patch('wake.report.export', wraps=export) as rebuilt:
            refreshed = build_public_artifact(self.root, self.root / 'rebuilt-public')
        self.assertEqual(sum(Path(call.args[1]).name != 'unified' for call in rebuilt.call_args_list), 1)
        self.assertEqual(refreshed['record_heads'], manifest['record_heads'])
        # Capture must reject a link before copying private bytes into staging.
        source = self.root / 'nodes' / NODE_IDS[0] / 'site/current'
        (source / 'injected.html').symlink_to(self.root / 'nodes' / NODE_IDS[0] / 'record/wake.sqlite')
        with self.assertRaisesRegex(ValueError, 'symlink'):
            build_public_artifact(self.root, self.root / 'unsafe-public')

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
