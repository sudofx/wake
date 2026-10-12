"""Physical codecs must preserve exact events, hashes, replay and failure visibility."""
import base64
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch
import zlib

from examples.task_list.app import TASK_LIST
from wake.kernel import ApplicationHost, ApplicationIntent, ApplicationRegistry, Kernel
from wake.kernel.governance import Governance
from wake.kernel.record import (Record, IntegrityError, SCHEMA_VERSION,
                                _decode_event_payload, _decode_projection_state,
                                _encode_event_payload, _EVENT_CODEC_PREFIX)


class StorageCompressionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name) / 'record.sqlite'
        self.record = Record(self.path)
        registry = ApplicationRegistry((TASK_LIST,))
        self.host = ApplicationHost(Kernel(self.record, Governance(application_registry=registry)),
                                    registry, TASK_LIST.application_id)
        for ident, title in (('small', 'Small'), ('large', 'café ✳︎ durable history ' * 900)):
            result = self.host.submit(ApplicationIntent(ident, self.host.context().revision,
                                                       'add', dict(id=ident, title=title)))
            self.assertEqual(result.status, 'accepted')
        result = self.host.submit(ApplicationIntent('rejected', self.host.context().revision,
                                                   'add', dict(id='large', title='refused ' * 900)))
        self.assertEqual(result.status, 'rejected')

    def tearDown(self):
        self.temp.cleanup()

    def make_v11(self):
        # Reproduce the prior physical format, retaining exact decoded UTF-8,
        # hashes, metadata and cached state rather than recreating history.
        with self.record.connect() as c:
            for row in c.execute('SELECT sequence,payload FROM events').fetchall():
                c.execute('UPDATE events SET payload=? WHERE sequence=?',
                          (_decode_event_payload(row['payload']),row['sequence']))
            raw=_decode_projection_state(c.execute('SELECT state FROM record_projection').fetchone()[0])
            legacy='zlib:'+base64.b64encode(zlib.compress(raw.encode(),9)).decode()
            c.execute('UPDATE record_projection SET state=?',(legacy,))
            c.execute('PRAGMA user_version=11')
            c.commit()

    def physical_rows(self):
        with sqlite3.connect(self.path) as c:
            return c.execute('SELECT * FROM events ORDER BY sequence').fetchall()

    def test_mixed_storage_replay_export_reopen_and_exact_unicode(self):
        before=self.record.full_replay()
        history=self.record.history()
        with self.record.connect() as c:
            types=[r[0] for r in c.execute('SELECT typeof(payload) FROM events')]
            self.assertIn('text',types)
            self.assertIn('blob',types)
            self.assertEqual(c.execute('SELECT typeof(state) FROM record_projection').fetchone()[0],'blob')
        fresh=Record(self.path)
        self.assertEqual(fresh.full_replay(),before)
        self.assertEqual(fresh.replay(),before)
        self.assertEqual(fresh.history(),history)
        self.assertEqual(fresh.history_tail(3),history)
        self.assertEqual([v['proposal'] for v in fresh.recent(3)], [v['proposal'] for v in history])
        self.assertEqual(history[-1]['status'],'rejected')
        backup=Path(self.temp.name)/'snapshot.sqlite'
        fresh.vacuum_snapshot_to(backup)
        self.assertEqual(Record.open_read_only(backup).full_replay(),before)
        self.assertEqual(Record(backup).history(),history)

    def test_v11_migration_preserves_every_decoded_row_and_replay(self):
        history=self.record.history();before=self.record.full_replay()
        self.make_v11();old=self.physical_rows()
        migrated=Record(self.path)
        self.assertTrue(migrated.storage_encoding_migrated)
        with migrated.connect() as c:
            self.assertEqual(c.execute('PRAGMA user_version').fetchone()[0],SCHEMA_VERSION)
            self.assertEqual(c.execute('PRAGMA freelist_count').fetchone()[0],0)
        new=self.physical_rows()
        for a,b in zip(old,new):
            self.assertEqual(len(a),len(b))
            self.assertEqual(a[:6],b[:6])
            self.assertEqual(a[6],_decode_event_payload(b[6]))
            self.assertEqual(a[7:],b[7:])
        self.assertEqual(len(old),len(new))
        self.assertEqual(migrated.full_replay(),before)
        self.assertEqual(migrated.history(),history)
        self.assertFalse(Record(self.path).schema_changed)

    def test_migration_failure_rolls_back_rows_projection_and_version(self):
        self.make_v11();before=self.physical_rows()
        with sqlite3.connect(self.path) as c:
            projection=c.execute('SELECT * FROM record_projection').fetchall()
        calls=0
        def fail_second(raw):
            nonlocal calls
            calls+=1
            if calls==2:raise RuntimeError('migration interrupted')
            return _encode_event_payload(raw)
        with patch('wake.kernel.record._encode_event_payload',side_effect=fail_second):
            with self.assertRaisesRegex(RuntimeError,'migration interrupted'):
                Record(self.path)
        self.assertEqual(self.physical_rows(),before)
        with sqlite3.connect(self.path) as c:
            self.assertEqual(c.execute('PRAGMA user_version').fetchone()[0],11)
            self.assertEqual(c.execute('SELECT * FROM record_projection').fetchall(),projection)
        self.assertEqual(Record(self.path).history()[-1]['status'],'rejected')

    def test_corrupt_compressed_event_fails_audit_and_export_despite_cached_projection(self):
        with self.record.connect() as c:
            original=c.execute("SELECT payload FROM events WHERE typeof(payload)='blob' LIMIT 1").fetchone()[0]
        for bad in (original[:-1], original+b'trailing', b'unknown codec', _EVENT_CODEC_PREFIX+b'not zlib'):
            with self.subTest(bad=bad[-12:]):
                with self.record.connect() as c:
                    c.execute('UPDATE events SET payload=? WHERE sequence=2',(bad,));c.commit()
                with self.assertRaises(IntegrityError):self.record.history()
                with self.assertRaises(IntegrityError):self.record.full_replay()
                with self.record.connect() as c:
                    c.execute('UPDATE events SET payload=? WHERE sequence=2',(original,));c.commit()

    def test_tampered_v11_chain_is_not_migrated_or_repaired(self):
        self.make_v11()
        with sqlite3.connect(self.path) as c:
            c.execute("UPDATE events SET event_hash='forged' WHERE sequence=2");c.commit()
        before=self.physical_rows()
        with self.assertRaises(IntegrityError):Record(self.path)
        self.assertEqual(self.physical_rows(),before)
        with sqlite3.connect(self.path) as c:
            self.assertEqual(c.execute('PRAGMA user_version').fetchone()[0],11)

    def test_valid_compression_of_changed_event_still_fails_hash_audit(self):
        with self.record.connect() as c:
            c.execute('UPDATE events SET payload=? WHERE sequence=2',
                      (_EVENT_CODEC_PREFIX+zlib.compress(b'{"operations":[]}'),));c.commit()
        with self.assertRaisesRegex(IntegrityError,'event chain is invalid'):
            self.record.full_replay()

    def test_corrupt_projection_and_older_reader_fail_closed(self):
        from wake.kernel.record import StorageVersionError
        with patch('wake.kernel.record.SCHEMA_VERSION',11):
            with self.assertRaises(StorageVersionError):Record(self.path)
        with self.record.connect() as c:
            stored=c.execute('SELECT state FROM record_projection').fetchone()[0]
            c.execute('UPDATE record_projection SET state=?',(stored[:-1],));c.commit()
        with self.assertRaises(IntegrityError):self.record.replay()

    def test_dictionary_preserves_exact_json_bytes_and_legacy_codec(self):
        from wake.kernel.record import (_encode_projection_state, _PROJECTION_DICTIONARY_PREFIX,
                                       _EVENT_DICTIONARY_PREFIX)
        import random
        rng = random.Random(7)
        text = ''.join(rng.choice('abcdefXYZ0123456789') for _ in range(4096)) + ' café ✳︎ \\" '
        raw = json.dumps({'requests': [text] * 70, 'literal': {'$ref': 0},
                          'types': [None, True, 4, 2.5]}, ensure_ascii=True, indent=2)
        for encoder, decoder, prefix in (
            (_encode_projection_state, _decode_projection_state, _PROJECTION_DICTIONARY_PREFIX),
            (_encode_event_payload, _decode_event_payload, _EVENT_DICTIONARY_PREFIX)):
            with self.subTest(prefix=prefix):
                stored = encoder(raw)
                self.assertTrue(stored.startswith(prefix))
                self.assertEqual(decoder(stored), raw)
                old = (_EVENT_CODEC_PREFIX + zlib.compress(raw.encode(), 6)
                       if decoder is _decode_event_payload else
                       b'wake:projection-json:zlib@1\x00' + zlib.compress(raw.encode(), 9))
                self.assertEqual(decoder(old), raw)
                self.assertLess(len(stored), len(old))
                for bad in (stored[:-1], stored + b'extra'):
                    with self.assertRaises(IntegrityError): decoder(bad)

    def test_dictionary_invalid_references_and_entries_fail_closed(self):
        import struct
        from wake.kernel.record import _PROJECTION_DICTIONARY_PREFIX
        token = json.dumps('x' * 300).encode()
        header = struct.pack('>I', 1) + struct.pack('>I', len(token)) + token
        for packed in (header + b'\0' + struct.pack('>I', 1),
                       header + b'\0\0', struct.pack('>I', 999),
                       struct.pack('>I', 1) + struct.pack('>I', 300) + b'x' * 300):
            with self.subTest(packed=packed[:8]):
                with self.assertRaises(IntegrityError):
                    _decode_projection_state(_PROJECTION_DICTIONARY_PREFIX + zlib.compress(packed))

    def test_span_scanner_preserves_existing_dictionary_bytes_and_rejections(self):
        import re
        from wake.kernel import compression
        old_scanner = re.compile(rb'"(?:[^"\\]|\\.)*"')
        strings = [('ordinary text ' * 900), ('quotes " backslashes \\ newline\n café ✳︎ ' * 200),
                   ('\\' * 300 + '"' * 300), ('\t\r\n' * 300)]
        raw = json.dumps({'strings': strings * 20}, ensure_ascii=False).encode()
        current = compression.encode_dictionary(raw, 6)
        self.assertIsNotNone(current)
        with patch.object(compression, '_STRING', old_scanner):
            previous = compression.encode_dictionary(raw, 6)
            self.assertEqual(compression.decode_dictionary(zlib.decompress(current)), raw)
        self.assertEqual(current, previous)
        self.assertEqual(compression.decode_dictionary(zlib.decompress(previous)), raw)
        for token in (b'"' + b'x' * 300 + b'\\"', b'"' + b'x' * 300 + b'"trailing',
                      b'"' + b'x' * 300 + b'\\\n"'):
            self.assertIsNone(compression._STRING.fullmatch(token))
            self.assertIsNone(old_scanner.fullmatch(token))

    def test_v12_upgrade_preserves_semantic_rows_and_exact_cache(self):
        before = self.record.full_replay()
        history = self.record.history()
        with self.record.connect() as c:
            for row in c.execute('SELECT sequence,payload FROM events').fetchall():
                raw = _decode_event_payload(row['payload'])
                stored = _EVENT_CODEC_PREFIX + zlib.compress(raw.encode(), 6) if len(raw) >= 1024 else raw
                c.execute('UPDATE events SET payload=? WHERE sequence=?', (stored,row['sequence']))
            raw = _decode_projection_state(c.execute('SELECT state FROM record_projection').fetchone()[0])
            c.execute('UPDATE record_projection SET state=?',
                      (b'wake:projection-json:zlib@1\x00' + zlib.compress(raw.encode(),9),))
            c.execute('PRAGMA user_version=12');c.commit()
        old = self.physical_rows()
        with patch('wake.kernel.record.SCHEMA_VERSION',12):
            self.assertEqual(Record.open_read_only(self.path).replay(), before)
        fresh = Record(self.path)
        self.assertEqual(fresh.full_replay(),before)
        self.assertEqual(fresh.history(),history)
        for a,b in zip(old,self.physical_rows()):
            self.assertEqual(a[:6],b[:6]);self.assertEqual(a[7:],b[7:])
            self.assertEqual(_decode_event_payload(a[6]),_decode_event_payload(b[6]))
