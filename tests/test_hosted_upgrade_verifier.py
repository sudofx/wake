"""The upgrade gate requires twelve complete reports from one frozen checkpoint."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from wake.installation_cli import NODE_IDS

_spec = importlib.util.spec_from_file_location(
    'upgrade_verifier', Path(__file__).resolve().parents[1] / 'scripts/verify_hosted_upgrade.py')
_verifier = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_verifier)


class EncryptedAuditInputTests(unittest.TestCase):
    def setUp(self):
        import gzip
        import hashlib
        import hmac
        import io
        import zipfile
        from wake.hosted import HostedState, FORMAT, seal
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.transport = HostedState(self.root / 'transport', 'example/repo', 'unused', b'k' * 32)
        self.transport.checkout.mkdir()
        self.objects = {}
        def block(raw):
            name = 'block-' + hmac.new(self.transport.key, b'block\0' + raw, hashlib.sha256).hexdigest() + '.bin'
            identity = len(self.objects) + 1
            self.objects[f'releases/assets/{identity}'] = seal(self.transport.key, gzip.compress(raw), name)
            return [{'id': identity, 'name': name, 'size': len(raw)}]
        auxiliary = io.BytesIO()
        with zipfile.ZipFile(auxiliary, 'w') as archive:
            archive.writestr('installation-id.json', '{"id":"installation"}')
        self.manifest = {'format': FORMAT, 'generation': 1, 'installation_id': 'installation',
                         'auxiliary': block(auxiliary.getvalue()), 'nodes': {}}
        for node in NODE_IDS:
            self.manifest['nodes'][node] = {'blocks': block(node.encode()), 'revision': 2,
                                           'head': 'a' * 64, 'sha256': 'b' * 64}
        (self.transport.checkout / 'current.enc').write_bytes(seal(
            self.transport.key, json.dumps(self.manifest).encode(), FORMAT))
        self.transport.api.request = lambda path, **_: self.objects[path]

    def test_retained_inputs_survive_remote_pruning_and_restore_only_assigned_node(self):
        snapshot = self.root / 'snapshot'
        _verifier.capture_snapshot(self.transport, snapshot)
        self.assertFalse(list(snapshot.rglob('*.sqlite')))
        self.objects.clear()  # Remote ref and pruning cannot affect offline audits.
        self.transport.checkout = snapshot
        manifest = self.transport.read_manifest()
        self.transport.api = _verifier.SnapshotFiles(snapshot, manifest)
        records = self.root / 'records'
        expected = {key: manifest['nodes'][NODE_IDS[0]][key] for key in ('revision', 'head', 'sha256')}
        with patch('wake.hosted.verify_recovery', return_value=expected) as verify:
            _verifier.restore_audit_nodes(self.transport, manifest, records, [NODE_IDS[0]])
        self.assertEqual(verify.call_count, 1)
        self.assertEqual(len(list(records.rglob('*.sqlite'))), 1)
        with self.assertRaises(ValueError):
            self.transport.api.request('actions/workflows/research/dispatches')

    def test_capture_rejects_corruption_without_publishing_partial_snapshot(self):
        self.objects[next(iter(self.objects))] = b'corrupt'
        target = self.root / 'incomplete'
        with self.assertRaises(ValueError):
            _verifier.capture_snapshot(self.transport, target)
        self.assertFalse(target.exists())

    def test_native_identity_mismatch_still_fails(self):
        snapshot = self.root / 'snapshot'
        _verifier.capture_snapshot(self.transport, snapshot)
        self.transport.api = _verifier.SnapshotFiles(snapshot, self.manifest)
        with patch('wake.hosted.verify_recovery', return_value={}), self.assertRaises(ValueError):
            _verifier.restore_audit_nodes(self.transport, self.manifest, self.root / 'records', [NODE_IDS[0]])


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
