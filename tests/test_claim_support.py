import json
import unittest
from wake.claim_support import validate_claims, render_findings
from wake.governance import Rejected
from wake.research import effective_evidence_role
from wake.providers import schema_for_context


class ClaimSupportTests(unittest.TestCase):
    def test_delivery_cannot_offer_invented_measured_results(self):
        from wake.claim_support import claim_schema
        properties = claim_schema(3)['items']['properties']
        self.assertEqual(properties['result']['enum'], [''])
        self.assertNotIn('tested', properties['certainty']['enum'])
        properties = claim_schema(3, [{'id': 'r', 'status': 'measured'},
                                     {'id': 'pending', 'status': 'pending'}])['items']['properties']
        self.assertEqual(properties['result']['enum'], ['', 'r'])
        self.assertIn('tested', properties['certainty']['enum'])

    def example(self):
        passage = 'This reaction network has a conserved total population and a stationary distribution.'
        state = {'evidence': {'e': {'source': 'https://arxiv.org/abs/2205.06313', 'content': json.dumps({'excerpt': passage})}}}
        claim = {'statement': 'The source discusses a stationary distribution.', 'support': [{'evidence': 'e', 'passage': passage, 'explanation': 'This reports equilibrium, without establishing temporal heredity.'}]}
        action = {'evidence': ['e'], 'claims': [claim], 'findings': render_findings([claim])}
        return state, action

    def test_exact_passage_does_not_allow_unlisted_findings(self):
        state, action = self.example()
        validate_claims(action, state)
        action['findings'] += '\nThis proves heredity.'
        with self.assertRaises(Rejected): validate_claims(action, state)

    def test_fabricated_passage_and_background_fail(self):
        state, action = self.example()
        action['claims'][0]['support'][0]['passage'] = 'A completely invented substantive passage not actually in this collected paper.'
        with self.assertRaises(Rejected): validate_claims(action, state)
        state, action = self.example()
        state['evidence']['e']['source'] = 'https://dictionary.cambridge.org/dictionary/english/causal'
        self.assertEqual(effective_evidence_role(state['evidence']['e']['source'], {'evidence_role': 'source'}), 'background')
        with self.assertRaises(Rejected): validate_claims(action, state)

    def test_forward_schema_keeps_old_contract_unchanged(self):
        for version in (None, 1):
            schema = schema_for_context({'research_quality_policy': version})
            book = next(c for c in schema['properties']['actions']['items']['anyOf'] if c['properties']['type']['enum'] == ['notebook'])
            self.assertEqual('claims' in book['required'], bool(version))

    def test_model_cannot_self_declare_a_tested_result(self):
        state, action = self.example()
        state['research_quality_policy'] = 2
        claim = action['claims'][0]
        claim.update(certainty='hypothesis', result='')
        validate_claims(action, state)
        claim.update(certainty='tested', result='invented')
        with self.assertRaises(Rejected): validate_claims(action, state)
        state['reproductions'] = {'r': {'status': 'measured', 'claim': claim['statement']}}
        claim['result'] = 'r'
        validate_claims(action, state)
        claim['statement'] = 'This proves chemical heredity.'
        with self.assertRaises(Rejected): validate_claims(action, state)

    def test_critical_review_cannot_invent_counterevidence_or_independence(self):
        from wake.claim_support import support_provenance
        state, action = self.example()
        state['research_quality_policy'] = 3
        claim = action['claims'][0]
        claim.update(certainty='paper-supported', result='', review={'counterevidence': [], 'alternative': 'Equilibrium sampling may explain the observation without any temporal memory.', 'would_change_mind': 'A controlled temporal intervention showing persistent history dependence would change this reading.'})
        validate_claims(action, state)
        state['evidence']['e']['peer_origin'] = {'instance_id': 'peer'}
        receipt = support_provenance(action, state)[0]
        self.assertEqual(receipt['distinct_works'], 1)
        self.assertEqual(receipt['independent_confirmation'], 'not-established')
        self.assertTrue(receipt['peer_imported'])
        claim['review']['counterevidence'] = ['fabricated']
        with self.assertRaises(Rejected): validate_claims(action, state)
