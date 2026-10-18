"""Exercise the actual loopback HTTP boundary without Docker or provider effects."""
from http.client import HTTPConnection
import json
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch

from wake.reader_preview import MAX_REQUEST, ReaderPreview, completed_site, verify_container


class ReaderPreviewTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        site = self.root / 'site/snapshot-one'
        site.mkdir(parents=True)
        (self.root / 'site/current').symlink_to(site, target_is_directory=True)
        (self.root / 'installation-id.json').write_text('{"id":"fixture-installation"}')
        (site / 'reader-data.json').write_text('{"head":"fixture"}')
        (site / 'index.html').write_text('<html>Completed export</html>')
        (site / '.wake-continuity').mkdir()
        (site / '.wake-continuity/secret.json').write_text('{"secret":"private"}')
        (site / 'escape.json').symlink_to(self.root / 'installation-id.json')
        self.calls = []
        self.server = ReaderPreview(self.root, port=0, bridge=self.bridge)
        thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)

    def bridge(self, packet):
        self.calls.append(packet)
        return {'answer': 'Fixture answer', 'sources': []}

    def request(self, method, route, packet=None, **headers):
        body = json.dumps(packet) if packet is not None else None
        connection = HTTPConnection('127.0.0.1', self.server.server_port, timeout=5)
        self.addCleanup(connection.close)
        connection.request(method, route, body, headers)
        response = connection.getresponse()
        return response.status, response.read()

    def allowed(self):
        return {'Origin': self.server.origin, 'X-Wake-Reader-Token': self.server.token,
                'Content-Type': 'application/json'}

    def test_capability_and_completed_export_only(self):
        self.assertEqual(self.server.server_address[0], '127.0.0.1')
        status, body = self.request('GET', '/ask-bob/capabilities')
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body)['installation_id'], 'fixture-installation')
        self.assertEqual(json.loads(body)['token'], self.server.token)
        status, body = self.request('GET', '/')
        self.assertEqual((status, body), (200, b'<html>Completed export</html>'))
        for path in ('/.wake-continuity/secret.json', '/%2ewake-continuity/secret.json',
                     '/escape.json', '/installation-id.json', '/site/', '/ask-bob/'):
            self.assertEqual(self.request('GET', path)[0], 404, path)

    def test_host_origin_and_capability_required_before_effect(self):
        packet = {'article_id': 'fixture', 'question': 'What was recorded?'}
        for headers in ({}, {**self.allowed(), 'Origin': 'https://outside.example'},
                        {**self.allowed(), 'X-Wake-Reader-Token': 'bad'},
                        {**self.allowed(), 'Host': 'outside.example'}):
            self.assertEqual(self.request('POST', '/ask-bob', packet, **headers)[0], 403)
        self.assertEqual(self.request('GET', '/ask-bob/capabilities', Host='outside.example')[0], 403)
        self.assertEqual(self.calls, [])
        status, body = self.request('POST', '/ask-bob', packet, **self.allowed())
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body)['answer'], 'Fixture answer')
        self.assertEqual(self.calls, [packet])

    def test_static_inspection_text_is_readable_without_exposing_neighboring_notes(self):
        site = completed_site(self.root)
        inspection = site / 'inspect'
        inspection.mkdir()
        (inspection / 'README.md').write_text('Public orientation')
        (inspection / 'packet.md').write_text('Public packet')
        (inspection / 'private.md').write_text('Private neighboring note')
        (site / 'private.md').write_text('Private root note')
        for route in ('/inspect/README.md', '/inspect/packet.md'):
            self.assertEqual(self.request('GET', route)[0], 200)
        for route in ('/inspect/private.md', '/private.md'):
            self.assertEqual(self.request('GET', route)[0], 404)
        self.assertEqual(self.calls, [])

    def test_limits_and_failures_do_not_repeat_provider_attempt(self):
        self.server.busy.acquire()
        self.assertEqual(self.request('POST', '/ask-bob', {}, **self.allowed())[0], 429)
        self.server.busy.release()
        self.server.attempts = 24
        self.assertEqual(self.request('POST', '/ask-bob', {}, **self.allowed())[0], 429)
        self.server.attempts = 0
        self.assertEqual(self.request('POST', '/ask-bob', {'q': 'x' * MAX_REQUEST},
                                      **self.allowed())[0], 413)
        self.assertEqual(self.calls, [])
        self.server.bridge = lambda _: (_ for _ in ()).throw(ValueError('PRIVATE-ERROR'))
        status, body = self.request('POST', '/ask-bob', {}, **self.allowed())
        self.assertEqual(status, 503)
        self.assertNotIn(b'PRIVATE-ERROR', body)
        self.assertEqual(self.server.attempts, 1)
        self.assertEqual(self.request('POST', '/ask-bob', {}, **self.allowed())[0], 429)

    def test_wrong_container_or_mount_fails_before_serving(self):
        def result(value):
            from types import SimpleNamespace
            return SimpleNamespace(stdout=value)
        with patch('wake.reader_preview.subprocess.run', return_value=result('false')):
            with self.assertRaises(ValueError):
                verify_container('wake', self.root)
        with patch('wake.reader_preview.subprocess.run', side_effect=[result('true'), result('true'),
                result('[{"Type":"bind","Destination":"/data","Source":"/wrong"}]')]):
            with self.assertRaisesRegex(ValueError, '/data'):
                verify_container('wake', self.root)

    def test_container_absolute_generation_link_maps_only_owned_site(self):
        current = self.root / 'site/current'
        current.unlink()
        current.symlink_to('/data/site/snapshot-one')
        self.assertEqual(completed_site(self.root), (self.root / 'site/snapshot-one').resolve())
        self.assertEqual(self.request('GET', '/')[0], 200)
        current.unlink()
        current.symlink_to(self.root)
        with self.assertRaises(ValueError):
            completed_site(self.root)
        self.assertEqual(self.request('GET', '/')[0], 404)


if __name__ == '__main__':
    unittest.main()
