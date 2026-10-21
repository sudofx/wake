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
    def test_metrics_reuse_captured_complete_history_without_reopening_authority(self):
        from unittest.mock import Mock
        from wake.live import _full_history_metrics
        from wake.history import history_metrics
        store = Mock()
        store.events.side_effect = AssertionError('Captured history must not be read again')
        store.history_metrics.side_effect = AssertionError('Captured metrics must not reopen history')
        store.performance_snapshot.return_value = {'event_count': 42, 'wake_database_bytes': 123}
        events = [{'seq': 1, 'kind': 'initialized', 'payload': {'objective': 'fixture'}}]
        state = {'version': 0, 'invocations': {}}
        result = _full_history_metrics(store, state, events)
        self.assertEqual(result, {'storage': {'sqlite_bytes': 123, 'event_count': 42},
                                 **history_metrics(events, state)})

    def test_overview_bounds_history_without_mutating_complete_export(self):
        from copy import deepcopy
        from wake.live import browser_projection, MAX_EVENTS, MAX_EVIDENCE_TEXT
        data = {'head': 'same-head', 'state': {'version': 7,
            'invocations': {'i': {'id': 'i', 'status': 'accepted', 'request': 'private body',
                                 'origin': {'node': '100.wake'}}},
            'evidence': {'e': {'content': 'x' * (MAX_EVIDENCE_TEXT * 2)}}},
            'events': [{'seq': i, 'payload': {'raw_response': 'private body'}}
                       for i in range(MAX_EVENTS + 20)]}
        before = deepcopy(data)
        view = browser_projection(data)
        self.assertEqual(data, before)
        self.assertEqual(view['head'], data['head'])
        self.assertEqual(view['state']['version'], 7)
        self.assertEqual(view['event_history']['total'], MAX_EVENTS + 20)
        self.assertEqual(len(view['events']), MAX_EVENTS)
        self.assertEqual(view['events'][0]['seq'], 20)
        self.assertNotIn('raw_response', view['events'][0]['payload'])
        self.assertNotIn('request', view['state']['invocations']['i'])
        self.assertEqual(view['state']['invocations']['i']['origin'], {'node': '100.wake'})
        self.assertLessEqual(len(view['state']['evidence']['e']['content']), MAX_EVIDENCE_TEXT + 1)

    def test_browser_shell_can_render_from_live_projection_without_store_replay(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            engine = Engine(root / "data", store_factory=Store)
            try:
                engine.run(Fixture())
                payload = build_live_projection(
                    engine.store, operation={"status": "accepted"}, runtime_ref="test-runtime"
                )
                self.assertEqual(payload["source"]["authority"], "legacy WAKE SQLite")
                self.assertEqual(payload["source"]["database"], "wake.sqlite3")
                self.assertIsNone(payload["source"]["branch"])
                before = engine.store.performance_snapshot()["full_replays"]
                export(None, root / "site", browser_only=True, projection=payload, standalone=False)
                self.assertEqual(json.loads((root / "site/deployment.json").read_text()),
                                 {"schema": 1, "mode": "hosted", "snapshot_only": True})
                for page in (root / "site").glob('*.html'):
                    if '<head>' in page.read_text():
                        self.assertIn('"mode": "hosted"', page.read_text())
                self.assertEqual(engine.store.performance_snapshot()["full_replays"], before)
                rendered = json.loads((root / "site/wake-data.json").read_text())
                self.assertEqual(rendered["head"], payload["head"])
                self.assertEqual(rendered["state"]["version"], payload["state"]["version"])
            finally:
                engine.store.close()

    def test_full_export_builds_current_site_and_maps(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            engine = Engine(root / "data", store_factory=Store)
            try:
                engine.run(Fixture())
                before = engine.store.performance_snapshot()["full_replays"]
                export(engine.store, root / "site", standalone=False)
                self.assertEqual(engine.store.performance_snapshot()["full_replays"] - before, 1)

                for name in ("index.html", "events.html", "state.html",
                             "map.html", "map3d.html", "wake-data.json", "console.html",
                             "console-records.html", "console-map.html", "console-map3d.html",
                             "console-events.html", "console-state.html", "console-rejected.html"):
                    self.assertTrue((root / "site" / name).is_file())

                page = (root / "site/index.html").read_text()
                self.assertNotIn("raw.githubusercontent.com", page)
                self.assertIn("window.WakeApplyLive", page)
                self.assertNotIn('href="https://github.com/sudofx/wake/actions"', page)
                self.assertNotIn("data-visibility-toggle", page)
                self.assertNotIn("wake-hide-current-data", page)
                self.assertNotIn("control.js", page)

                map_page = (root / "site/map.html").read_text()
                map3d_page = (root / "site/map3d.html").read_text()
                self.assertNotIn('>Console</a>', map_page.split('<nav class="compact-nav"', 1)[1].split('</nav>', 1)[0])
                self.assertNotIn('>Console</a>', map3d_page.split('<nav class="compact-nav"', 1)[1].split('</nav>', 1)[0])
                self.assertIn('class="console-link" href="console.html"', map_page)
                self.assertIn('class="console-link" href="console.html"', map3d_page)
                self.assertIn('M4.2 16.8a8.8 8.8 0 1 1 15.6 0', map_page)
                self.assertIn('M12 16l3.8-4.4', map3d_page)
                self.assertNotIn('>About</a>', map_page.split('<nav class="compact-nav"', 1)[1].split('</nav>', 1)[0])
                self.assertNotIn('>About</a>', map3d_page.split('<nav class="compact-nav"', 1)[1].split('</nav>', 1)[0])
                self.assertNotIn('class="repo-link"', map_page)
                self.assertIn('class="repository-menu-link" href="https://github.com/sudofx/wake">GitHub</a>', map_page)
                self.assertNotIn('class="repo-link"', map3d_page)
                self.assertIn('class="repository-menu-link" href="https://github.com/sudofx/wake">GitHub</a>', map3d_page)
                self.assertNotIn('href="https://github.com/sudofx/wake/actions"', map_page)
                self.assertNotIn('href="https://github.com/sudofx/wake/actions"', map3d_page)
                self.assertRegex(map_page, r'href="theme\.css\?v=[^"]+"')
                self.assertRegex(map3d_page, r'href="theme\.css\?v=[^"]+"')
                self.assertIn('name="theme-color" content="#000000"', map_page)
                self.assertIn('name="theme-color" content="#000000"', map3d_page)
                for rendered_page in (map_page, map3d_page):
                    nav = rendered_page.split('<nav class="compact-nav"', 1)[1].split('</nav>', 1)[0]
                    visible = nav.split('<!-- Read menu temporarily retired.', 1)[0]
                    self.assertNotIn('>Home</a>', visible)
                    self.assertNotIn('<summary>Read</summary>', visible)
                    self.assertIn('<!-- Read menu temporarily retired.', nav)
                    self.assertLess(visible.index('>Research</a>'), visible.index('>Journal</a>'))
                    self.assertLess(visible.index('>Journal</a>'), visible.index('>Bob’s Blog</a>'))
                self.assertNotIn("control.js", map_page)
                self.assertNotIn("control.js", map3d_page)
                events_page = (root / "site/events.html").read_text()
                self.assertNotIn('<details open', events_page)
                self.assertNotIn(' open>', events_page)
                flat_view = (root / "site/flat-view.js").read_text()
                self.assertIn('<details class="entry record-panel">', flat_view)
                self.assertIn("const closeEventDetails=()=>root.querySelectorAll('details.entry').forEach(item=>{item.open=false})", flat_view)
                self.assertIn("window.addEventListener('pageshow',closeEventDetails)", flat_view)
                self.assertNotIn('class="powered-by"', map_page)
                self.assertNotIn('class="powered-by"', map3d_page)
                self.assertNotIn('class="footer-powered"', map_page)
                self.assertNotIn('class="footer-powered"', map3d_page)

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
