"""Mirror delivery follows captured exports independently of worker health/Bob."""
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from wake.mirror import acknowledge, delivery_due, exported_identity, heads_digest, mirror_status, interval_seconds


class MirrorDeliveryTests(unittest.TestCase):
    def test_cadence_ignores_node_runtime_and_withheld_bob(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            site = root / 'nodes/100.wake/site/current'
            site.mkdir(parents=True)
            (site / 'head.txt').write_text('a' * 64)
            identity = exported_identity(root)
            self.assertEqual(identity['available_exports'], 1)
            self.assertIsNone(identity['publication_digest'])
            status = {'enabled': True, 'next_capture_at': 1800}
            self.assertFalse(delivery_due(status, identity, 1799))
            self.assertTrue(delivery_due(status, identity, 1800))
            status['published_export_digest'] = identity['export_digest']
            self.assertFalse(delivery_due(status, identity, 3600))

    def test_new_leader_article_does_not_wait_for_follower_exports(self):
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory) / 'nodes/100.wake/site/current'
            (site / 'group').mkdir(parents=True)
            (site / 'head.txt').write_text('a' * 64)
            (site / 'group/bob-publication.json').write_text('{"checkpoint": 2}')
            identity = exported_identity(directory)
            self.assertTrue(delivery_due({'enabled': True, 'next_capture_at': 1800}, identity, 1))
            self.assertFalse(delivery_due({'enabled': True, 'retry_at': 2}, identity, 1))
            self.assertFalse(delivery_due({'enabled': False}, identity, 1))

    def test_acknowledgment_confirms_captured_heads_only(self):
        captured = {'export_digest': heads_digest({'100.wake': {'head': 'a' * 64}}),
                    'publication_digest': 'b' * 64}
        newer = {'export_digest': heads_digest({'100.wake': {'head': 'c' * 64}}),
                 'publication_digest': 'b' * 64, 'available_exports': 1}
        status = {'enabled': True, 'interval_seconds': 1800, 'error': 'old', 'queued_export_digest': newer['export_digest']}
        acknowledge(status, captured, 100)
        self.assertEqual(status['published_export_digest'], captured['export_digest'])
        self.assertNotIn('error', status)
        self.assertFalse(delivery_due(status, newer, 101))
        self.assertTrue(delivery_due(status, newer, 1900))

    def test_host_receipt_cannot_enable_or_reconfigure_delivery(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'public-mirror.json').write_text(json.dumps({'enabled': False, 'delivery': 'host', 'interval_seconds': 1800}))
            (root / 'public-mirror-host.json').write_text(json.dumps({'enabled': True, 'delivery': 'controller', 'status': 'published', 'published_export_digest': 'a' * 64, 'interval_seconds': 1}))
            status = mirror_status(root)
            self.assertFalse(status['enabled'])
            self.assertEqual(status['status'], 'disabled')
            self.assertEqual(status['delivery'], 'host')
            self.assertEqual(status['interval_seconds'], 1800)
            self.assertEqual(status['published_export_digest'], 'a' * 64)

    def test_legacy_bob_ack_does_not_claim_head_delivery(self):
        identity = {'available_exports': 1, 'export_digest': 'a' * 64, 'publication_digest': 'b' * 64}
        self.assertTrue(delivery_due({'enabled': True, 'published_digest': 'b' * 64}, identity, 1))

    def test_direct_publisher_cannot_overlap_an_existing_installation_lease(self):
        import fcntl
        from wake.installation_cli import publish_artifact
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with (root / '.public-publish.lock').open('a') as lease:
                fcntl.flock(lease, fcntl.LOCK_EX | fcntl.LOCK_NB)
                with patch.dict(os.environ, {'WAKE_PUBLISH_REPOSITORY': 'https://github.com/example/wake', 'WAKE_PUBLISH_BRANCH': 'wake-public'}), \
                     patch('wake.installation_cli.build_public_artifact') as capture, \
                     patch('wake.installation_cli.upload_public_artifact') as upload:
                    with self.assertRaises(BlockingIOError):
                        publish_artifact(root)
                    capture.assert_not_called()
                    upload.assert_not_called()

    def test_interval_must_be_finite_and_at_least_one_minute(self):
        for value in ('0', '59', 'nan', 'inf'):
            with self.subTest(value=value), patch.dict(os.environ, {'WAKE_MIRROR_INTERVAL_SECONDS': value}):
                with self.assertRaises(ValueError):
                    interval_seconds()
        with patch.dict(os.environ, {'WAKE_MIRROR_INTERVAL_SECONDS': '1800'}):
            self.assertEqual(interval_seconds(), 1800)

    def test_host_publication_retains_lease_through_publisher_completion(self):
        spec = importlib.util.spec_from_file_location('wake_mirror_script', Path(__file__).parents[1] / 'scripts/wake_mirror.py')
        worker = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(worker)
        events = []
        from contextlib import contextmanager
        @contextmanager
        def lease():
            events.append('acquired')
            try:
                yield
            finally:
                events.append('released')
        with patch.object(worker, 'publication_lease', lease), patch.object(worker.subprocess, 'run', side_effect=lambda *a, **k: events.append('uploaded')):
            worker.publish()
        self.assertEqual(events, ['acquired', 'uploaded', 'released'])
