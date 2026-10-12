import copy
import unittest
from wake.reproduction import equilibrium, reproduce, record_result
from wake.governance import Rejected


class ReproductionTests(unittest.TestCase):
    def test_analytic_stationarity_and_simulation_against_uncoupled_baseline(self):
        expected = equilibrium(12)
        self.assertAlmostEqual(sum(expected.values()), 1)
        # Independently check edge fluxes, not only a simulator's own output.
        for (a,b,c), probability in expected.items():
            if a:
                self.assertAlmostEqual(probability*a, expected[(a-1,b+1,c)]*(b+1))
            if b:
                self.assertAlmostEqual(probability*b, expected[(a,b-1,c+1)]*(c+1))
        report = reproduce()
        self.assertTrue(report['acceptance']['passed'])
        self.assertGreater(report['baseline']['total_variation_error'], 0.5)
        for run in report['runs']:
            self.assertAlmostEqual(run['covariance_a_b'], -12/9, delta=0.12)
        state = {}
        record_result(state, {'actor': 'operator', 'report': report}, {'seq': 1, 'time': 'now'})
        tampered = copy.deepcopy(report); tampered['runs'][0]['total_variation_error'] = 0
        with self.assertRaises(Rejected):
            record_result({}, {'actor': 'operator', 'report': tampered}, {'seq': 1, 'time': 'now'})
        with self.assertRaises(Rejected):
            record_result({}, {'actor': 'model', 'report': report}, {'seq': 1, 'time': 'now'})
