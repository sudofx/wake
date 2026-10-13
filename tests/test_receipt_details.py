import json
from pathlib import Path
import tempfile
import unittest
from wake.kernel import ApplicationHost, ApplicationIntent, ApplicationRegistry, Kernel, SubmissionProvenance
from wake.kernel.governance import Governance
from wake.kernel.record import Record
from wake.kernel.receipts import FIELDS, SCHEMA
from wake.kernel.runtime import InvocationLifecycle
from examples.task_list.app import TASK_LIST


class ReceiptDetailsTests(unittest.TestCase):
    def test_accepted_rejected_and_failed_receipts_bind_six_execution_details(self):
        with tempfile.TemporaryDirectory() as directory:
            record = Record(Path(directory) / 'record.sqlite')
            record.receipt_location = '102.wake'
            registry = ApplicationRegistry((TASK_LIST,))
            kernel = Kernel(record, Governance(application_registry=registry), receipt_location='102.wake')
            host = ApplicationHost(kernel, registry, TASK_LIST.application_id)
            actor = SubmissionProvenance('human', 'operator', 'test')
            accepted = host.submit(ApplicationIntent('add', 0, 'add', {'id': 'a', 'title': 'Task'},
                                  rationale='Track a task'), provenance=actor)
            rejected = host.submit(ApplicationIntent('stale', 0, 'complete', {'id': 'a'},
                                  rationale='Complete the task'), provenance=actor)
            for receipt in (accepted, rejected):
                self.assertEqual(receipt.provenance['receipt_schema'], SCHEMA)
                self.assertTrue(all(receipt.provenance[field] for field in FIELDS))
                self.assertEqual(receipt.provenance['where'], '102.wake')
                self.assertEqual(receipt.provenance['who'], 'operator')
                self.assertIn(receipt.status, receipt.provenance['what'])
            old_hash = record.history()[0]['event_hash']
            self.assertEqual(record.full_replay()[0], 1)
            invocation = InvocationLifecycle.begin(record, kernel.context(),
                provenance=SubmissionProvenance('model', 'fixture', 'test'))
            invocation.fail(outcome='provider_failure', detail='Provider unavailable')
            for event in record.invocation_history():
                metadata = event['provenance']
                self.assertTrue(all(metadata[field] for field in FIELDS))
                self.assertIn(event['stage'], metadata['what'])
                self.assertEqual(metadata['where'], '102.wake')
            self.assertEqual(record.history()[0]['event_hash'], old_hash)
            self.assertEqual(Record.open_read_only(record.path).full_replay()[0], 1)

    def test_absent_identity_and_reason_remain_explicit(self):
        from wake.kernel.receipts import receipt_provenance
        details = receipt_provenance(None, what='rejected', where='', why='', how='governance')
        self.assertEqual(details['who'], 'Caller identity not supplied')
        self.assertEqual(details['where'], 'Execution location not supplied')
        self.assertEqual(details['why'], 'Reason not supplied')

    def test_old_receipt_bytes_survive_new_metadata_and_tampering_is_detected(self):
        from wake.kernel.record import _decode_event_payload
        from wake.kernel.storage import hash_event, GENESIS_HASH
        from wake.kernel.record import IntegrityError
        with tempfile.TemporaryDirectory() as directory:
            record = Record(Path(directory) / 'record.sqlite')
            registry = ApplicationRegistry((TASK_LIST,))
            host = ApplicationHost(Kernel(record, Governance(application_registry=registry)),
                                   registry, TASK_LIST.application_id)
            host.submit(ApplicationIntent('old', 0, 'add', {'id': 'a', 'title': 'Old'}))
            # Build a pre-attribution fixture with its original hash contract.
            with record.connect() as connection:
                row = connection.execute('SELECT * FROM events').fetchone()
                material = {k: row[k] for k in ('receipt_id','proposal_id','status','revision_before','revision_after')}
                material['payload'] = json.loads(_decode_event_payload(row['payload']))
                material['reasons'] = json.loads(row['reasons'])
                old_hash = hash_event(GENESIS_HASH, material)
                connection.execute('UPDATE events SET provenance=NULL, event_hash=?', (old_hash,))
                connection.execute('UPDATE record_projection SET event_hash=?', (old_hash,))
                connection.commit()
            before = tuple(record.rows()[0])
            self.assertEqual(record.full_replay()[0], 1)
            host.submit(ApplicationIntent('new', 1, 'complete', {'id': 'a'}, rationale='Finish old task'))
            self.assertEqual(tuple(record.rows()[0]), before)
            self.assertIsNone(record.history()[0]['provenance'])
            self.assertEqual(record.full_replay()[0], 2)
            with record.connect() as connection:
                metadata = json.loads(connection.execute('SELECT provenance FROM events WHERE sequence=2').fetchone()[0])
                metadata['where'] = 'forged location'
                connection.execute('UPDATE events SET provenance=? WHERE sequence=2', (json.dumps(metadata),))
                connection.commit()
            with self.assertRaises(IntegrityError):
                record.full_replay()
