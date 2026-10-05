"""Fresh-process authority regression matching promotion evidence timing."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from wake.sudofx_store import SudofxStore


class AuthorityFreshProcessTests(unittest.TestCase):
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

            store = SudofxStore(root)
            try:
                belief = store.load()["beliefs"]["sensor"]
                self.assertEqual(belief["status"], "retracted")
                self.assertEqual(belief["confidence"], 0)
                self.assertEqual(len(belief["evidence"]), 3)
            finally:
                store.close()


if __name__ == "__main__":
    unittest.main()
