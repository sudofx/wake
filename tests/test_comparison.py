"""The comparison must expose failures and preserve identical starting records."""
import json
from pathlib import Path
import tempfile
import unittest

from wake.comparison import (ARMS, CLAIM, CONTRADICTION, OBLIGATION,
                             complete_trial, create_comparison, prepare_trial,
                             comparison_report)
from wake.engine import DEFAULTS
from wake.governance import Rejected


class ComparisonTests(unittest.TestCase):
    def test_identical_starting_state_corrected_reply_and_preserved_negative_result(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'comparison'
            manifest = create_comparison(root, dict(DEFAULTS))
            trials = [prepare_trial(root, arm, 'manual-test') for arm in ARMS]
            self.assertEqual({t['starting_state_hash'] for t in trials}, {manifest['baseline_state_hash']})
            self.assertEqual({t['starting_head'] for t in trials}, {manifest['baseline_head']})
            for index, trial in enumerate(trials):
                request = json.loads(Path(trial['request']).read_text())
                offered = {a['properties']['type']['enum'][0] for a in
                           request['response_schema']['properties']['actions']['items']['anyOf']}
                self.assertFalse(offered & {'project', 'notebook', 'blog', 'research', 'reframe'})
                actions = [] if index else [
                    dict(type='belief', id=CLAIM, statement='The simulated sensor remains within its stated tolerance of 9–11.',
                         confidence=0, status='retracted', evidence=[CONTRADICTION],
                         reason='The new reading of 17 is outside 9–11; the provisional claim is contradicted.'),
                    dict(type='resolve', id=OBLIGATION, status='fulfilled', evidence=[CONTRADICTION],
                         reason='Reviewed the conflicting measurement and retracted the inherited claim.')]
                reply = root / ('reply' + str(index) + '.json')
                reply.write_text(json.dumps(dict(base_version=request['context']['version'],
                    title='Review inherited measurement', summary='Review and preserve the observations.', actions=actions)))
                result = complete_trial(root, trial['key'], reply)
                self.assertEqual(result['evaluation']['all_structural_checks_passed'], not bool(index))
                self.assertIsNone(result['evaluation']['human_assessment'])
            report = comparison_report(root)
            self.assertEqual(report['paired_models'], ['manual-test'])
            self.assertFalse(report['behavioral_equivalence_established'])
            with self.assertRaises(Rejected):
                prepare_trial(root, 'rich', 'manual-test')

    def test_changed_baseline_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'comparison'
            create_comparison(root, dict(DEFAULTS))
            with (root / 'baseline.sqlite').open('ab') as stream:
                stream.write(b'changed')
            with self.assertRaisesRegex(Rejected, 'Frozen baseline changed'):
                prepare_trial(root, 'active', 'manual-test')

    def test_existing_directory_is_never_replaced(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(Rejected):
                create_comparison(tmp, dict(DEFAULTS))
