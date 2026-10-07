import unittest
from wake.matrix_campaign import build_continuity_probe, perfect_continuity_probe_response, evaluate_continuity_probe_response, continuity_result_record
from wake.matrix import MATRIX, MATRIX_KEY, continuity_matrix_progress


class MatrixDiagnosticsTests(unittest.TestCase):
    def test_forged_colliding_source_survives_as_exact_failure_diagnostic(self):
        coordinate = MATRIX.coordinate('provenance', 'rich', 'provenance-collision')
        state = dict(objective='Test', evidence={'s1': dict(source='https://trusted.example/work', version=1)}, journal=[], projects={}, commitments={})
        probe = build_continuity_probe(state, '0'*64, coordinate.coordinate_id)['context']
        response = perfect_continuity_probe_response(probe)
        response['provenance'][0]['source'] = 'untrusted://forged-provenance'
        evaluation = evaluate_continuity_probe_response(probe, response)
        self.assertIn('provenance_fidelity', evaluation['failed_checks'])
        diagnostic = evaluation['diagnostics']['provenance_fidelity']
        self.assertEqual(diagnostic['expected'][0][1], 'https://trusted.example/work')
        self.assertEqual(diagnostic['actual'][0][1], 'untrusted://forged-provenance')
        record = continuity_result_record(probe, evaluation, 'invocation', 'accepted', response)
        progress = continuity_matrix_progress({'extensions': {MATRIX_KEY: {'results': {coordinate.coordinate_id: record}}}})
        self.assertEqual(progress['completed_count'], 1)
        self.assertEqual(progress['passed_count'], 0)
        self.assertEqual(progress['failure_counts']['provenance_fidelity'], 1)
        self.assertEqual(progress['failed_cells'][0]['diagnostics'], record['diagnostics'])
