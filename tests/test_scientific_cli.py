"""Reproducible zero-inference investigations retain native, replayable evidence."""
from contextlib import redirect_stdout
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from wake.__main__ import parser, execute
from wake.record_store import RecordStore
from wake.report import export
from wake.installation_cli import _copy_public_site


class ScientificCLITests(unittest.TestCase):
    def test_benchmark_binding_rejects_a_different_instance_before_execution(self):
        import json
        from wake.science.cli import initialize
        from wake.engine import DEFAULTS
        from test_scientific_research import hypothesis,protocol
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary)/'bound'
            engine=initialize(root,DEFAULTS,'Fixture question about instance 81',
                {'evaluator':'hidden-relationship@1','instance':81})
            try:
                invocation,request=engine.start('fixture','binding-test')
                p=protocol();p.update(evaluator={'id':'hidden-relationship@1'},
                    inputs={'instance':17,'probes':[3],'holdout_size':4})
                actions=[{'type':kind,'id':key,'project':'investigation','definition':definition}
                    for kind,key,definition in [('hypothesis','h-sort',hypothesis()),('experiment','wrong-instance',p)]]
                result=engine.finish(invocation,json.dumps({'base_version':request['context']['version'],
                    'title':'Mismatched instrument fixture','summary':'Must be rejected before execution.','actions':actions}))
                self.assertEqual(result['status'],'rejected')
                self.assertIn('operator-bound',result['reason'])
                self.assertFalse(engine.store.audit()[0]['science']['experiments'])
            finally:engine.store.close()

    def run_benchmark(self,kind,instance):
        temporary=tempfile.TemporaryDirectory();self.addCleanup(temporary.cleanup)
        root=Path(temporary.name)/kind
        args=parser().parse_args(['science','demonstrate','--benchmark',kind,'--instance',str(instance),'--output',str(root)])
        with patch('wake.science.cli.Gemini') as gemini,redirect_stdout(io.StringIO()):
            result=execute(args);gemini.assert_not_called()
        self.assertTrue(result['fixture']);self.assertTrue(result['replay_verified'])
        self.assertEqual(result['evidence']['metrics']['successful_replications'],1)
        return root,result

    def test_revision_fixture_completes_negative_revision_replication_and_closure(self):
        root,result=self.run_benchmark('revision',41)
        metrics=result['evidence']['metrics']
        self.assertEqual(metrics['contradicted_predictions'],1)
        self.assertEqual(metrics['verified_hypothesis_revisions'],1)
        self.assertEqual(metrics['open_uncertainties'],0)
        self.assertIn('Synthetic generalization',str(result))
        store=RecordStore(root/'record');self.addCleanup(store.close)
        self.assertEqual(store.audit()[1],result['head'])
        report=root/'cli-audit.html'
        args=parser().parse_args(['--data',str(root/'record'),'science','report','--output',str(report)])
        evidence=execute(args)
        self.assertEqual(evidence['source']['head'],result['head'])
        self.assertTrue(report.is_file())
        self.assertEqual(store.audit()[1],result['head'])

    def test_correction_fixture_exports_a_public_audit_without_private_context(self):
        root,result=self.run_benchmark('correction',77)
        store=RecordStore(root/'record');self.addCleanup(store.close)
        site=root/'site';export(store,site,browser_only=True)
        self.assertTrue('scientific-research.html' in (site/'index.html').read_text(),'Scientific audit link missing from exported navigation')
        public=root/'public';_copy_public_site(site,public)
        self.assertTrue((public/'scientific-research.json').is_file())
        page=(public/'scientific-research.html').read_text()
        self.assertIn('synthetic_benchmark',page)
        self.assertIn('Independent evaluation',page)
        self.assertNotIn('decision_state_capsule',page)
        self.assertNotIn('oracle_digest',page)
        self.assertEqual(result['evidence']['investigations'][0]['evaluation']['metrics']['B_accuracy'],1)
