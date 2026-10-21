"""Old receipts remain verifiable without admitting retired execution."""
from copy import deepcopy
import unittest

from wake.domain_events import empty, reduce_event
from wake.governance import Rejected


class RetiredReceiptHistoryTests(unittest.TestCase):
    def test_exact_terminal_history_and_no_new_execution(self):
        state = empty()
        state['invocations']['old'] = {'id': 'old', 'phase': 'passenger'}
        state['pending'] = 'old'
        event = {'kind': 'advisory_completed', 'time': '2026-10-20T00:00:00Z',
                 'payload': {'id': 'old', 'outcome': 'invalid-output'}}
        with self.assertRaises(Rejected):
            reduce_event(deepcopy(state), event)
        expected = deepcopy(state)
        expected['pending'] = None
        expected['invocations']['old'].update(status='advisory_completed',
            finished=event['time'], reason='', outcome='invalid-output')
        self.assertEqual(reduce_event(deepcopy(state), event, historical=True), expected)
        for field, value in (('phase', 'research'),):
            bad = deepcopy(state)
            bad['invocations']['old'][field] = value
            with self.assertRaises(Rejected):
                reduce_event(bad, event, historical=True)
        bad_event = deepcopy(event)
        bad_event['payload']['outcome'] = 'invented'
        with self.assertRaises(Rejected):
            reduce_event(deepcopy(state), bad_event, historical=True)
