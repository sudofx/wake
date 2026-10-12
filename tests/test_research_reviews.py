import copy
import tempfile
import unittest
from wake.authority import open_authoritative_store
from wake.research_reviews import weak_notebook_reviews
from wake.governance import Rejected
from wake.report import _notebook_html


class ResearchReviewTests(unittest.TestCase):
    def test_native_correction_preserves_original_and_replays(self):
        with tempfile.TemporaryDirectory() as directory:
            store = open_authoritative_store(directory, allow_initialize=True)
            store.append('initialized', {'objective': 'Review evidence', 'governance': 1})
            store.append('charter_adopted', {'mission': 'Review', 'pet_name': 'WAKE'})
            store.append('project_adopted', {'id': 'p', 'domain': 'science'})
            store.append('observation', {'id': 'e', 'source': 'https://dictionary.cambridge.org/dictionary/english/causal', 'content': '{}', 'actor': 'collector', 'scope': 'collected'})
            # Historical snapshot is explicit test input, never an operational repair.
            state = store.load()
            state['notebooks']['n'] = dict(id='n', project='p', revision=1, title='Scientific mechanism', summary='Review needed', findings='Original claim', limitations='None', next_questions='Test', evidence=['e'])
            from wake.domain_events import reduce_event
            original = copy.deepcopy(state['notebooks'])
            review = weak_notebook_reviews(state)[0]
            reduce_event(state, dict(kind='scientific_review_recorded', payload=review, seq=5, time='2026-10-12'))
            self.assertEqual(state['notebooks'], original)
            self.assertEqual(state['version'], 0)
            self.assertIn('Source correction', _notebook_html(state['notebooks']['n'], state))
            # Exercise native reduction/replay with the same verified envelope shape.
            from wake.application import _append_legacy_event
            env = copy.deepcopy(store._envelope()); env['state'] = copy.deepcopy(state)
            env['state']['research_reviews'] = {}
            decision = _append_legacy_event(env, dict(kind='scientific_review_recorded', payload=review, time='2026-10-12'))
            self.assertTrue(decision.accepted)
            self.assertNotIn('n@1', env['state']['research_reviews'])
            with self.assertRaises(Rejected):
                reduce_event(state, dict(kind='scientific_review_recorded', payload={**review, 'actor': 'model'}, seq=6, time='now'))
            store.close()
