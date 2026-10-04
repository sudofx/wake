"""Executable checks for the single supported public export path."""

import json
from pathlib import Path
import tempfile
import unittest

from wake.engine import Engine
from wake.store import Store
from wake.live import build_live_projection
from wake.providers import Fixture
from wake.provenance import map3d_shard_filename
from wake.report import export


class PublishingTests(unittest.TestCase):
    def test_browser_shell_can_render_from_live_projection_without_store_replay(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            engine = Engine(root / "data", store_factory=Store)
            try:
                engine.run(Fixture())
                payload = build_live_projection(
                    engine.store, operation={"status": "accepted"}, runtime_ref="test-runtime"
                )
                public_invocation = next(iter(payload["state"]["invocations"].values()))
                self.assertIn("temporal", public_invocation)
                self.assertIn("context_delivery", public_invocation)
                self.assertIn("working_set_metrics", public_invocation)
                self.assertNotIn("working_set_shadow", public_invocation)
                self.assertNotIn("retrieval_shadow", public_invocation)
                self.assertEqual(payload["source"]["authority"], "legacy WAKE SQLite")
                self.assertEqual(payload["source"]["database"], "wake.sqlite3")
                self.assertIsNone(payload["source"]["branch"])
                self.assertIn("matrix_progress", payload)
                self.assertFalse(payload["matrix_progress"]["enabled"])
                self.assertEqual(payload["matrix_progress"]["cell_count"], 343)
                self.assertEqual(len(payload["matrix_progress"]["cells"]), 343)
                self.assertIn("application_observability", payload)
                self.assertIsNone(payload["application_observability"])
                self.assertIn("application_access", payload)
                self.assertIsNone(payload["application_access"])
                before = engine.store.performance_snapshot()["full_replays"]
                export(None, root / "site", browser_only=True, projection=payload)
                self.assertEqual(engine.store.performance_snapshot()["full_replays"], before)
                rendered = json.loads((root / "site/wake-data.json").read_text())
                self.assertEqual(rendered["head"], payload["head"])
                self.assertEqual(rendered["state"]["version"], payload["state"]["version"])
                self.assertIn("matrix_progress", rendered)
                self.assertIn("application_observability", rendered)
                self.assertIn("application_access", rendered)
            finally:
                engine.store.close()

    def test_full_export_builds_current_site_and_maps(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            engine = Engine(root / "data", store_factory=Store)
            try:
                engine.run(Fixture())
                before = engine.store.performance_snapshot()["full_replays"]
                export(engine.store, root / "site")
                self.assertEqual(engine.store.performance_snapshot()["full_replays"] - before, 1)

                for name in ("index.html", "events.md", "events.html", "state.md", "state.html",
                             "map.html", "map3d.html", "wake-data.json"):
                    self.assertTrue((root / "site" / name).is_file())

                page = (root / "site/index.html").read_text()
                self.assertIn("wake-live/live.json", page)
                self.assertIn("window.WakeApplyLive", page)
                self.assertIn('href="https://github.com/sudofx/wake/actions"', page)
                self.assertNotIn("data-visibility-toggle", page)
                self.assertNotIn("wake-hide-current-data", page)
                self.assertNotIn("control.js", page)

                map_page = (root / "site/map.html").read_text()
                map3d_page = (root / "site/map3d.html").read_text()
                self.assertIn('href="index.html#metrics">Metrics</a>', map_page)
                self.assertIn('href="index.html#metrics">Metrics</a>', map3d_page)
                self.assertIn('href="https://github.com/sudofx/wake/actions"', map_page)
                self.assertIn('href="https://github.com/sudofx/wake/actions"', map3d_page)
                self.assertNotIn("control.js", map_page)
                self.assertNotIn("control.js", map3d_page)

                full_graph = json.loads((root / "site/map-data.json").read_text())
                lazy_shell = json.loads((root / "site/map3d-data.json").read_text())
                self.assertLess(len(json.dumps(lazy_shell)), len(json.dumps(full_graph)))
                self.assertEqual(lazy_shell["meta"]["schema_version"], 2)
                self.assertNotIn("nodes", lazy_shell)
                self.assertNotIn("edges", lazy_shell)
                shard = root / "site/map3d" / map3d_shard_filename("root:journal")
                self.assertTrue(shard.is_file())
            finally:
                engine.store.close()


if __name__ == "__main__":
    unittest.main()
