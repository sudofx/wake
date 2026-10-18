"""Static inspection evidence comes from real isolated kernel decisions."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from examples.task_list.inspection import FORMAT, build_demo
from wake.kernel.storage import GENESIS_HASH, hash_event


class InspectionDemoTests(unittest.TestCase):
    def test_real_events_have_recomputable_hashes_and_governed_outcomes(self):
        artifact = build_demo()
        self.assertEqual(artifact['format'], FORMAT)
        self.assertTrue(all(artifact['checks'].values()))
        events = artifact['events']
        self.assertEqual([row['status'] for row in events], ['accepted', 'rejected', 'accepted'])
        self.assertEqual([row['revision_after'] for row in events], [1, 1, 2])
        self.assertEqual(events[1]['reasons'], ['task does not exist'])
        previous = GENESIS_HASH
        for sequence, event in enumerate(events, 1):
            self.assertEqual(event['sequence'], sequence)
            self.assertEqual(event['previous_hash'], previous)
            material = {key: event[key] for key in ('receipt_id', 'proposal_id', 'status', 'revision_before', 'revision_after', 'reasons')}
            material['payload'] = event['proposal']
            if event['provenance'] is not None:
                material['provenance'] = event['provenance']
            self.assertEqual(hash_event(previous, material), event['event_hash'])
            previous = event['event_hash']
        self.assertEqual(artifact['result']['head'], previous)
        self.assertEqual(artifact['result']['revision'], 2)
        self.assertTrue(artifact['result']['replay_verified'])
        self.assertEqual(len(artifact['result']['state']), 1)
        self.assertTrue(next(iter(artifact['result']['state'].values()))['completed'])

    def test_repeated_runs_reproduce_semantics_without_inventing_identical_bytes(self):
        first, second = build_demo(), build_demo()
        self.assertEqual(first['result']['receipts'], second['result']['receipts'])
        self.assertEqual(first['checks'], second['checks'])
        self.assertNotEqual(first['events'][0]['receipt_id'], second['events'][0]['receipt_id'])
        self.assertNotEqual(first['result']['head'], second['result']['head'])
        self.assertEqual(list(first['result']['state'].values()), list(second['result']['state'].values()))

    def test_source_hashes_match_real_files_and_no_private_paths_are_exported(self):
        artifact = build_demo()
        root = Path(__file__).resolve().parents[1]
        self.assertIsInstance(artifact['source']['dirty'], (bool, type(None)))
        for source in artifact['source']['files']:
            self.assertFalse(Path(source['path']).is_absolute())
            self.assertEqual(hashlib.sha256((root / source['path']).read_bytes()).hexdigest(), source['sha256'])
        serialized = json.dumps(artifact)
        self.assertNotIn(str(root), serialized)
        self.assertNotIn(tempfile.gettempdir(), serialized)
        self.assertNotIn('task-list.sqlite', serialized)
        self.assertNotIn('wake.sqlite', serialized)

    def test_cli_runs_without_site_packages_and_writes_only_json_output(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / 'demo.json'
            result = subprocess.run([sys.executable, '-S', '-m', 'examples.task_list.inspection',
                                     '--output', str(destination)], check=True, capture_output=True, text=True)
            self.assertTrue(json.loads(result.stdout)['checks_passed'])
            artifact = json.loads(destination.read_text())
            self.assertEqual(artifact['format'], FORMAT)
            self.assertEqual([path.name for path in Path(directory).iterdir()], ['demo.json'])
            self.assertNotIn(directory, destination.read_text())


if __name__ == '__main__':
    unittest.main()
