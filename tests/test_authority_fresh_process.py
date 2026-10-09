"""Fresh-process authority regression matching promotion evidence timing."""

from __future__ import annotations

import subprocess
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from wake.record_store import RecordStore
from wake.application import WAKE_APPLICATION
from wake.kernel.applications import application_state
from wake.governance import Rejected


class AuthorityFreshProcessTests(unittest.TestCase):
    def test_cli_audit_checks_interior_history_despite_valid_projection(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "wake-data"
            def cli(command, *args):
                return subprocess.run(
                    [sys.executable, "-m", "wake", "--data", str(root), command, *args],
                    capture_output=True, text=True, timeout=30)
            self.assertEqual(cli("init").returncode, 0)
            self.assertEqual(cli("observe", "--source", "fixture:sensor", "--text", "measurement").returncode, 0)
            self.assertEqual(cli("audit").returncode, 0)
            with sqlite3.connect(root / "wake.sqlite") as database:
                database.execute("UPDATE events SET reasons = ? WHERE sequence = 1", ('["tampered"]',))
            self.assertEqual(cli("status").returncode, 0)
            result = cli("audit")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("event chain is invalid at sequence 1", result.stdout + result.stderr)

    def test_cli_cycles_1_5_10_retract_sensor_belief(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "wake-data"

            def cli(*args: str) -> None:
                result = subprocess.run(
                    [sys.executable, "-m", "wake", "--data", str(root), *args],
                    capture_output=True,
                    text=True,
                    timeout=30,
                )
                self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

            cli("init")
            cli("observe", "--source", "fixture:sensor", "--text",
                "Synthetic baseline: sensor reading 10, tolerance 9–11.")
            for cycle in range(1, 11):
                if cycle == 5:
                    cli("observe", "--source", "fixture:sensor", "--text",
                        "Synthetic second measurement: sensor reading 10.2, tolerance 9–11.")
                if cycle == 10:
                    cli("observe", "--source", "fixture:sensor", "--text",
                        "Synthetic counterexample: sensor reading 17, outside tolerance 9–11.")
                cli("wake", "--provider", "fixture",
                    "--model", "fixture-a" if cycle % 2 else "fixture-b")

            store = RecordStore(root)
            try:
                belief = store.load()["beliefs"]["sensor"]
                self.assertEqual(belief["status"], "retracted")
                self.assertEqual(belief["confidence"], 0)
                self.assertEqual(len(belief["evidence"]), 3)
                _, root_state = store.record.full_replay()
                envelope = root_state['app:wake']
                accepted = next(event for event in reversed(envelope['events'])
                    if event['action'] == 'append_legacy_event' and event['input']['kind'] == 'accepted')
                with patch('wake.application.govern_proposal', side_effect=Rejected('stricter current policy')):
                    rebuilt = application_state(WAKE_APPLICATION, envelope)
                    self.assertEqual(rebuilt, store._envelope())
                    # Replay permission is never exposed to a new application intent.
                    live = WAKE_APPLICATION.action('append_legacy_event').evaluate(rebuilt, accepted['input'])
                    self.assertFalse(live.accepted)
                    self.assertIn('stricter current policy', live.reasons)
                envelope['events'][-1]['result_digest'] = '0' * 64
                with self.assertRaisesRegex(ValueError, 'replay drift'):
                    application_state(WAKE_APPLICATION, envelope)
            finally:
                store.close()


if __name__ == "__main__":
    unittest.main()
