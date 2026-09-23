from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tempfile
import unittest

from wake.engine import DEFAULTS, Engine
from wake.experimental import temporal_snapshot
from support import charter_settings


class ExperimentalRegimeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.engine = Engine(Path(self.temp.name) / "data", DEFAULTS)
        with self.engine.store.lock():
            self.engine.initialize()

    def tearDown(self):
        self.engine.store.close()
        self.temp.cleanup()

    def test_default_regime_is_append_only_and_replayable(self):
        events = self.engine.store.events()
        self.assertEqual(events[-1]["kind"], "experimental_regime_adopted")
        state, _ = self.engine.store.replay()
        self.assertEqual(state["experimental"]["controls"]["time_dilation"]["mode"], "real")
        self.assertEqual(state["experimental"]["effective_from_version"], 0)

    def test_invalid_control_is_rejected_without_history_write(self):
        before = len(self.engine.store.events())
        with self.engine.store.lock():
            with self.assertRaises(ValueError):
                self.engine.set_time_dilation(mode="scaled", scale=1001, reason="invalid")
        self.assertEqual(len(self.engine.store.events()), before)

    def test_regime_change_only_applies_forward_and_old_receipt_survives(self):
        with self.engine.store.lock():
            invocation, request = self.engine.start("fixture", "test")
            self.engine.store.append("recovered", {"id": invocation, "reason": "test cleanup"})
            old = self.engine.store.load()["invocations"][invocation]
            self.engine.set_time_dilation(mode="scaled", scale=24, reason="comparison")
        state = self.engine.store.load()
        self.assertEqual(old["experimental_regime"]["controls"]["time_dilation"]["mode"], "real")
        self.assertEqual(state["experimental"]["controls"]["time_dilation"]["scale"], 24.0)
        replayed, _ = self.engine.store.replay()
        self.assertEqual(replayed["invocations"][invocation]["experimental_regime"], old["experimental_regime"])

    def test_effective_time_can_freeze_while_cycle_distance_remains_visible(self):
        with self.engine.store.lock():
            self.engine.set_time_dilation(mode="frozen", reason="controlled freeze")
            state = self.engine.store.load()
            anchor = datetime.fromisoformat(state["temporal"]["anchor_time"])
            snapshot = temporal_snapshot(state, self.engine.store.events(),
                                         (anchor + timedelta(hours=3)).isoformat())
        self.assertEqual(snapshot["wall_elapsed_seconds"], 10800.0)
        self.assertEqual(snapshot["effective_elapsed_seconds"], 0.0)
        self.assertEqual(snapshot["effective_scale"], 0.0)

    def test_temporal_receipt_is_delivered_but_cannot_change_governance(self):
        self.engine.store.close()
        self.engine = Engine(Path(self.temp.name) / "charter", charter_settings("Test temporal Squirrel observation."))
        with self.engine.store.lock():
            self.engine.initialize()
        with self.engine.store.lock():
            invocation, request = self.engine.start("fixture", "test")
            self.engine.store.append("recovered", {"id": invocation, "reason": "test cleanup"})
        self.assertIn("experimental_regime", request["context"])
        self.assertIn("temporal", request["context"])
        self.assertEqual(request["context"]["squirrel"]["temporal_use"],
                         "observational; no time signal changes Squirrel eligibility yet")
        self.assertNotIn("time_dilation", json.dumps(request["response_schema"]))
        item = self.engine.store.load()["invocations"][invocation]
        self.assertEqual(item["temporal"]["regime_id"], item["experimental_regime"]["id"])


if __name__ == "__main__":
    unittest.main()
