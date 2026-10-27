"""Paired requests share a frozen task; labels never enter model input."""
import json
from pathlib import Path
import tempfile
import unittest
from wake.event_format import digest
from wake.kernel.generation import GenerationRequest, GenerationResponse
from wake.knowledge_evaluation import evaluate, planned_trials, FixtureGeneration

CASES=Path(__file__).parent/'fixtures/decision_memory.json'


class KnowledgeEvaluationTests(unittest.TestCase):
    def test_protocol_is_frozen_before_exactly_eight_stateless_requests(self):
        with tempfile.TemporaryDirectory() as directory:
            output=Path(directory)/'result.json'
            class InspectingProvider(FixtureGeneration):
                calls=0
                def generate(self,request):
                    self.calls+=1
                    self.assert_request=request
                    saved=json.loads(output.read_text())
                    if saved['protocol_hash']!=digest(saved['protocol']):
                        raise AssertionError('Protocol changed')
                    material=json.loads(request.prompt)
                    if 'required_ids' in material or 'irrelevant_ids' in material:
                        raise AssertionError('Scoring labels entered model input')
                    return super().generate(request)
            provider=InspectingProvider();r=evaluate(CASES,provider,'fixture',output,fixture=True)
            self.assertEqual(provider.calls,8);self.assertIsInstance(provider.assert_request,GenerationRequest)
            self.assertEqual(r['status'],'completed')
            for name in r['protocol']['cases']:
                rows=[x for x in r['trials'] if x['case']==name]
                self.assertEqual(rows[0]['state_hash'],rows[1]['state_hash'])
                self.assertEqual(json.loads(rows[0]['prompt'])['task'],json.loads(rows[1]['prompt'])['task'])
            self.assertIn('plumbing only',' '.join(r['limitations']))

    def test_alternative_provider_needs_no_governance_or_evaluator_changes(self):
        class Abstain:
            def generate(self,request):
                return GenerationResponse('independent-fixture',request.model,'{"used_ids":[]}')
        with tempfile.TemporaryDirectory() as directory:
            r=evaluate(CASES,Abstain(),'other',Path(directory)/'result.json',fixture=True)
            self.assertEqual(r['status'],'completed')
            self.assertTrue(all(not row['task_complete'] for row in r['trials']))
            self.assertTrue(all(row['provider']=='independent-fixture' for row in r['trials']))

    def test_provider_failure_is_an_incomplete_trial_and_not_a_result(self):
        class Failed:
            def generate(self,request):
                raise RuntimeError('private diagnostic must not enter report')
        with tempfile.TemporaryDirectory() as directory:
            r=evaluate(CASES,Failed(),'other',Path(directory)/'result.json')
            self.assertEqual(r['status'],'incomplete');self.assertEqual(len(r['trials']),8)
            self.assertNotIn('private diagnostic',json.dumps(r))
            self.assertTrue(all(row['status']=='failed' for row in r['trials']))
