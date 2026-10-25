"""The upgrade gate requires twelve complete reports from one frozen checkpoint."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

from wake.installation_cli import NODE_IDS

_spec = importlib.util.spec_from_file_location(
    'upgrade_verifier', Path(__file__).resolve().parents[1] / 'scripts/verify_hosted_upgrade.py')
_verifier = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_verifier)


class UpgradeReportTests(unittest.TestCase):
    def setUp(self):
        self.candidate = 'a' * 40
        self.policy = {'source_revision': 'b' * 40, 'installation_id': 'installation'}
        self.reports = [
            {'status': 'verified-node', 'candidate': self.candidate,
             'baseline': self.policy['source_revision'], 'installation_id': 'installation',
             'generation': 17999, 'checkpoint_sha256': 'c' * 64,
             'provider_calls': 0, 'remote_record_writes': 0,
             'nodes': {node: {'head': 'd' * 64, 'version': 10,
                              'native_head': 'e' * 64, 'revision': 20}}}
            for node in NODE_IDS]

    def aggregate(self, reports):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for index, report in enumerate(reports):
                (root / f'{index}.json').write_text(json.dumps(report))
            return _verifier.aggregate_reports(root, candidate=self.candidate,
                                                policy=self.policy, node_ids=NODE_IDS)

    def test_complete_matching_checkpoint(self):
        report = self.aggregate(self.reports)
        self.assertEqual(report['status'], 'verified')
        self.assertEqual(set(report['nodes']), set(NODE_IDS))
        self.assertEqual(report['generation'], 17999)

    def test_missing_extra_duplicate_or_unknown_node_fails(self):
        for reports in (self.reports[:-1], self.reports + [self.reports[0]],
                        self.reports[:-1] + [self.reports[0]]):
            with self.subTest(reports=len(reports)), self.assertRaises(ValueError):
                self.aggregate(reports)
        reports = copy.deepcopy(self.reports)
        reports[-1]['nodes'] = {'999.wake': next(iter(reports[-1]['nodes'].values()))}
        with self.assertRaises(ValueError):
            self.aggregate(reports)

    def test_inconsistent_or_failed_shard_fails(self):
        changes = {'status': 'failed', 'candidate': 'f' * 40, 'baseline': 'f' * 40,
                   'installation_id': 'other', 'generation': 18000,
                   'checkpoint_sha256': 'f' * 64, 'provider_calls': 1,
                   'remote_record_writes': 1, 'nodes': {}}
        for key, value in changes.items():
            reports = copy.deepcopy(self.reports)
            reports[-1][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.aggregate(reports)

    def test_consistent_wrong_candidate_policy_or_checkpoint_fails(self):
        for key, value in {'candidate': 'f' * 40, 'baseline': 'f' * 40,
                           'installation_id': 'other', 'generation': 0,
                           'checkpoint_sha256': 'invalid'}.items():
            reports = copy.deepcopy(self.reports)
            for report in reports:
                report[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.aggregate(reports)

    def test_incomplete_audit_payload_fails(self):
        for value in ({}, {'head': 'd' * 64},
                      {'head': 'd' * 64, 'native_head': 'bad', 'version': 1, 'revision': 2}):
            reports = copy.deepcopy(self.reports)
            reports[-1]['nodes'][NODE_IDS[-1]] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.aggregate(reports)
