import json
import unittest
from wake.governance import Rejected, _verify_claim_support
from wake.evidence_quality import evidence_quality


def source(identifier, work, excerpt, scope=''):
    return dict(id=identifier, actor='collector', scope='collected', source='https://example.org/' + identifier,
                content=json.dumps(dict(source_identity=work, excerpt=excerpt, scope=scope)))


class QualityTests(unittest.TestCase):
    def test_mirrors_cannot_supply_two_supporting_works(self):
        mirrors = [source('one', 'doi:one', 'quantum entropy measurement'), source('two', 'doi:one', 'quantum entropy measurement')]
        with self.assertRaisesRegex(Rejected, 'underlying source'):
            _verify_claim_support('quantum entropy measurement', mirrors, 'Claim')
        _verify_claim_support('quantum entropy measurement', mirrors + [source('three', 'doi:two', 'quantum entropy measurement')], 'Claim')

    def test_scope_label_cannot_supply_claim_support(self):
        unrelated = [source('one', 'doi:one', 'musical perception', 'quantum entropy measurement')]
        with self.assertRaises(Rejected):
            _verify_claim_support('quantum entropy measurement', unrelated, 'Claim', minimum_sources=1)

    def test_diagnostics_expose_repeated_work_and_mismatch(self):
        evidence = {x['id']: x for x in [source('one', 'doi:one', 'entropy measurement'), source('two', 'doi:one', 'musical perception')]}
        quality = evidence_quality(dict(evidence=evidence, notebooks={
            'n': dict(id='n', findings='entropy measurement', evidence=['one', 'two']),
            'm': dict(id='m', findings='entropy measurement', evidence=['one'])}))
        self.assertEqual(quality['distinct_works'], 1)
        self.assertEqual(quality['mirror_or_repeat_observations'], 1)
        self.assertEqual(quality['reused_works'][0]['notebook_count'], 2)
        self.assertEqual(quality['notebooks'][0]['possible_mismatch_ids'], ['two'])
