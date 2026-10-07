import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from wake.correction_demo import run_correction_demo, PREFIX
from wake.engine import Engine
from wake.record_store import RecordStore
from support import charter_settings
from test_research import project, notebook


class DemoTests(unittest.TestCase):
    def test_native_receipts_retain_original_retract_belief_and_supersede_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            store = RecordStore(directory, initialize_empty=True)
            engine = Engine(directory, charter_settings(), store=store)
            engine.initialize()
            for identifier in ('s1', 's2'):
                store.append('observation', dict(id=identifier, source='https://example.org/' + identifier,
                    actor='collector', scope='collected', content=json.dumps({'excerpt': 'entropy comparison measurement'})))
            invocation, request = engine.start('manual', 'test')
            result = engine.finish(invocation, json.dumps(dict(base_version=request['context']['version'],
                title='Test project', summary='Test notebook', actions=[project(), notebook(['s1', 's2'])])))
            self.assertEqual(result['status'], 'accepted')
            before = store.events()
            with patch.object(engine, 'context', return_value={'attention': {'enforce_selected_topic': True}}):
                from wake.governance import Rejected
                with self.assertRaises(Rejected):
                    run_correction_demo(engine)
            self.assertEqual(store.events(), before)
            with patch('wake.correction_demo.govern_proposal', return_value=(None, None, {'status': 'withheld'}, None)):
                with self.assertRaises(Rejected):
                    run_correction_demo(engine)
            self.assertEqual(store.events(), before)
            with patch.object(engine, 'observe', side_effect=OSError('Interrupted measurement')):
                with self.assertRaises(OSError):
                    run_correction_demo(engine)
            self.assertEqual(store.load()['posts'][PREFIX+'-original']['status'], 'current')
            result = run_correction_demo(engine)
            self.assertEqual(result['belief_status'], 'retracted')
            self.assertEqual(len(result['receipts']), 2)
            self.assertEqual(len(result['kernel_receipts']), 2)
            self.assertEqual(store.events()[:len(before)], before)
            state = store.load()
            self.assertEqual(state['posts'][PREFIX+'-original']['superseded_by'], PREFIX+'-corrected')
            self.assertEqual(state['beliefs'][PREFIX]['evidence'], ['s1', 's2', PREFIX+'-measurement'])
            from wake.kernel.applications import application_state
            from wake.application import WAKE_APPLICATION
            self.assertEqual(application_state(WAKE_APPLICATION, store.record.full_replay()[1]['app:wake'])['state'], state)
            count = len(store.events())
            self.assertTrue(run_correction_demo(engine)['already_complete'])
            self.assertEqual(len(store.events()), count)
            store.close()
