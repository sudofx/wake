import json
import tempfile
import unittest
from pathlib import Path
from wake.authority import open_authoritative_store
from wake.engine import Engine
from wake.claim_support import render_findings
from support import charter_settings


class NativeQualityContractTests(unittest.TestCase):
    def test_forward_claims_survive_replay_and_correction_preserves_cycle(self):
        with tempfile.TemporaryDirectory() as directory:
            store = open_authoritative_store(directory, allow_initialize=True)
            engine = Engine(directory, charter_settings('Review chemical equilibrium.'), store=store)
            with store.lock():
                engine.initialize()
                store.append('research_quality_adopted', {'actor': 'operator', 'version': 3})
                store.append('project_adopted', {'id': 'p', 'title': 'Equilibrium', 'question': 'What establishes equilibrium?', 'domain': 'information_survival', 'status': 'active', 'next_step': 'Compare', 'reason': 'Source review'})
                passage = 'A conserved reaction network has a multinomial equilibrium distribution.'
                store.append('observation', {'id': 'e', 'source': 'https://arxiv.org/abs/2205.06313', 'content': json.dumps({'excerpt': passage, 'source_identity': 'arxiv:2205.06313'}), 'actor': 'collector', 'scope': 'collected'})
                claim = {'statement': 'The source reports equilibrium.', 'certainty': 'paper-supported', 'result': '', 'support': [{'evidence': 'e', 'passage': passage, 'explanation': 'The source concerns equilibrium rather than temporal heredity.'}], 'review': {'counterevidence': [], 'alternative': 'A stationary distribution need not preserve a memory of earlier input.', 'would_change_mind': 'A controlled history-dependent intervention would require a different interpretation.'}}
                action = {'type': 'notebook', 'id': 'n', 'project': 'p', 'title': 'Equilibrium result', 'summary': 'A narrow reading', 'findings': render_findings([claim]), 'claims': [claim], 'limitations': 'One source, no biological experiment.', 'next_questions': 'Test temporal persistence.', 'evidence': ['e'], 'reason': 'Keep the source scope explicit.'}
                invocation, request = engine.start('fixture', 'offline')
                choices = request['response_schema']['properties']['actions']['items']['anyOf']
                self.assertTrue(any('claims' in c.get('required', []) for c in choices))
                action.pop('findings')
                result = engine.finish(invocation, json.dumps({'base_version': request['context']['version'], 'title': 'Source review', 'summary': 'A bounded finding.', 'actions': [action]}))
                self.assertEqual(result['status'], 'accepted', result)
                original = store.load()['notebooks']['n']
                self.assertEqual(original['support_provenance'][0]['independent_confirmation'], 'not-established')
                store.append('scientific_review_recorded', {'actor': 'operator', 'notebook': 'n', 'revision': 1, 'assessment': 'needs-source-review', 'correction': 'Operator review: temporal implications remain unverified.', 'issues': [{'evidence': 'e', 'reason': 'Equilibrium does not establish temporal memory.'}]})
                before = store.load()
                self.assertEqual(before['version'], 1)
                self.assertEqual(before['notebooks']['n'], original)
                self.assertEqual(engine.notebook_qualifying_evidence_ids(before, original), [])
            store.close()
            reopened = open_authoritative_store(directory, allow_initialize=False)
            try:
                state, _, _ = reopened.replay_record()
                self.assertEqual(state, before)
                self.assertEqual(state['version'], 1)
            finally:
                reopened.close()
