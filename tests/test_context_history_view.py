"""Context reuse must preserve exact history and end at the read boundary."""
import tempfile
import unittest
from unittest.mock import patch
from wake.record_store import RecordStore
from wake.engine import Engine, DEFAULTS
from wake.errors import IntegrityError


class ContextHistoryViewTests(unittest.TestCase):
    def test_same_context_one_history_read_and_no_stale_next_build(self):
        with tempfile.TemporaryDirectory() as directory:
            store = RecordStore(directory, initialize_empty=True)
            engine = Engine(store=store, settings=dict(DEFAULTS));engine.initialize()
            store.append('observation',{'id':'fixture','source':'fixture','actor':'operator','content':'A bounded context fixture.'})
            state=store.load();expected=engine._context(state,'fixture')
            with patch.object(store,'_events',wraps=store._events) as reads:
                self.assertEqual(engine.context(state,'fixture'),expected)
                self.assertEqual(reads.call_count,1)
            self.assertFalse(hasattr(store,'_query_events'))
            previous=len(store.events())
            with store.history_view():
                self.assertEqual(len(store.events()),previous)
                with self.assertRaises(IntegrityError):store.append('observation',{})
            store.append('observation',{'id':'later','source':'fixture','actor':'operator','content':'Later durable work.'})
            with store.history_view():self.assertEqual(len(store.events()),previous+1)
