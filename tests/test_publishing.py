# =============================================================================
# TESTING INTENT — publishing
#
# This file is executable documentation. Passing cases define behavior WAKE✳︎
# promises to preserve; rejection/failure cases define boundaries that future
# refactors must not weaken merely to make CI green. Assertions should make the
# protected invariant understandable to both human and AI maintainers.
# =============================================================================
# WAKE✳︎ MAINTAINER NOTE
#
# Executable specification for publishing.
# Tests in WAKE✳︎ are part of the explanation of the system: successful cases show what authority is allowed,
# while rejection/failure cases show the boundaries that must remain intact during refactors.
# Prefer assertions that make the invariant obvious to a human or AI maintainer reading this file later.

"""Exercise publishing against a disposable local Git remote, never GitHub."""

import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from wake.engine import Engine
from wake.providers import Fixture
from wake.provenance import map3d_shard_filename
from wake.report import export


class PublishingTests(unittest.TestCase):
    def test_publish_is_isolated_and_repeatable(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            project, remote = root / "project", root / "remote.git"
            project.mkdir()
            subprocess.run(["git", "init", "--quiet", str(project)], check=True)
            subprocess.run(["git", "init", "--quiet", "--bare", str(remote)], check=True)
            subprocess.run(["git", "-C", str(project), "remote", "add", "origin", str(remote)], check=True)
            (project/"scripts").mkdir()
            shutil.copyfile(Path(__file__).resolve().parents[1]/"scripts/publish.py", project/"scripts/publish.py")
            spec = importlib.util.spec_from_file_location("local_publish_test", project/"scripts/publish.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            engine = Engine(project/"data")
            try:
                engine.run(Fixture())
                before_replays = engine.store.performance_snapshot()["full_replays"]
                export(engine.store, project/"site")
                after_replays = engine.store.performance_snapshot()["full_replays"]
                self.assertEqual(after_replays - before_replays, 1)
                for name in ("events.md", "events.html", "state.md", "state.html"):
                    self.assertTrue((project/"site"/name).is_file())
                page = (project/"site/index.html").read_text()
                self.assertIn('href="events.html">Readable history', page)
                self.assertIn('href="state.html">State', page)
                self.assertNotIn('id="wake-data"', page)
                self.assertIn("fetch('wake-data.json'", page)
                self.assertIn("localStorage.setItem(sessionKey", page)
                self.assertIn("localStorage.getItem(sessionKey", page)
                self.assertIn("const legacy=sessionStorage.getItem(sessionKey)", page)
                self.assertIn("sessionStorage.removeItem(sessionKey)", page)
                browser_data = json.loads((project/"site/wake-data.json").read_text())
                self.assertEqual(browser_data["state"]["version"], 1)
                self.assertIn("route();", page)
                self.assertNotIn("journal();route();", page)

                # MAP navigation should expose the same metrics destination as
                # the main site. The 3-D floating card is deliberately hover-only:
                # a click owns the persistent right-side details panel instead.
                map_page = (project/"site/map.html").read_text()
                map3d_page = (project/"site/map3d.html").read_text()
                self.assertIn('href="index.html#metrics">Metrics</a>', map_page)
                self.assertIn('href="index.html#metrics">Metrics</a>', map3d_page)
                self.assertIn('Hover for preview · click for right-side details', map3d_page)
                self.assertIn('src="map.js"', map_page)
                self.assertIn('src="map3d.js"', map3d_page)
                self.assertNotIn('id="map-data"', map_page)
                self.assertNotIn('id="map-data"', map3d_page)
                map_js = (project/"site/map.js").read_text()
                map3d_js = (project/"site/map3d.js").read_text()
                self.assertIn("fetch('map-data.json'", map_js)
                self.assertIn("fetch('map3d-data.json'", map3d_js)
                self.assertIn('showPopover(hovered)', map3d_js)
                self.assertNotIn('showPopover(current()||hovered)', map3d_js)
                # Performance contract: exact branch data stays navigable in the detail panel,
                # while the SVG paints a bounded sibling window and sleeps when idle.
                self.assertIn('const VISUAL_BRANCH_LIMIT=36', map3d_js)
                self.assertIn('const visualChildren=', map3d_js)
                self.assertIn('function startDrift(){return}', map3d_js)
                self.assertNotIn('stageHovered', map3d_js)
                self.assertNotIn('hoverPausedMs', map3d_js)
                self.assertNotIn('const orbit=', map3d_js)
                self.assertIn('Every record remains selectable here.', map3d_js)
                map3d_css = (project/"site/map3d.css").read_text()
                self.assertNotIn("fill:#080b13", map3d_css)
                self.assertNotIn("stroke:#11182d", map3d_css)
                self.assertIn("stroke:var(--wake-core)", map3d_css)
                self.assertIn("var(--paper)", map3d_css)
                full_graph = json.loads((project/"site/map-data.json").read_text())
                lazy_shell = json.loads((project/"site/map3d-data.json").read_text())
                self.assertLess(len(json.dumps(lazy_shell)), len(json.dumps(full_graph)))
                self.assertNotIn("nodes", lazy_shell)
                self.assertNotIn("edges", lazy_shell)
                self.assertEqual(lazy_shell["meta"]["schema_version"], 2)
                self.assertTrue((project/"site/map3d"/map3d_shard_filename("root:journal")).is_file())
                journal_shard = json.loads((project/"site/map3d"/map3d_shard_filename("root:journal")).read_text())
                self.assertEqual(journal_shard["parent"], "root:journal")
                self.assertIn("child_ids", journal_shard)
                self.assertNotIn(":", map3d_shard_filename("root:journal"))
                self.assertIn("fetch(branchUrl(id)", map3d_js)
                self.assertIn("ensureBranch(id).then(()=>{if(preview===id)render()})", map3d_js)
                module.publish(project/"site")
                module.publish(project/"site")
                count = subprocess.check_output(["git", "--git-dir", str(remote), "rev-list", "--count", "journal-pages"],text=True).strip()
                self.assertEqual(count, "1")
                engine.run(Fixture())
                export(engine.store, project/"site")
                module.publish(project/"site")
                count = subprocess.check_output(["git", "--git-dir", str(remote), "rev-list", "--count", "journal-pages"],text=True).strip()
                self.assertEqual(count, "2")
                files = subprocess.check_output(["git", "--git-dir", str(remote), "ls-tree", "--name-only", "journal-pages"],text=True).splitlines()
                self.assertEqual(set(files), {
                    ".nojekyll", "index.html", "wake-data.json", "journal.md", "style.css", "nav.css", "map.css", "map3d.css", "theme.css", "nav.js", "map.js", "map3d.js", "flat-view.js",
                    "state.json", "state.md", "state.html",
                    "events.jsonl", "events.md", "events.html",
                    "head.txt", "map.html", "map-data.json", "map3d.html", "map3d-data.json", "map3d", "blog.xml", "journal.xml", "journal",
                })
                self.assertFalse((project/"index.html").exists())
                map_path = project/"site/map-data.json"
                original_map = map_path.read_text()
                tampered_map = json.loads(original_map)
                tampered_map["edges"] = []
                map_path.write_text(json.dumps(tampered_map))
                with self.assertRaisesRegex(SystemExit, "Map does not match"):
                    module.publish(project/"site")
                map_path.write_text(original_map)
                map3d_path = project/"site/map3d-data.json"
                original_map3d = map3d_path.read_text()
                tampered_map3d = json.loads(original_map3d)
                tampered_map3d["root_children"] = []
                map3d_path.write_text(json.dumps(tampered_map3d))
                with self.assertRaisesRegex(SystemExit, "3D map does not match"):
                    module.publish(project/"site")
                map3d_path.write_text(original_map3d)
                shard_path = project/"site/map3d"/map3d_shard_filename("root:journal")
                original_shard = shard_path.read_text()
                tampered_shard = json.loads(original_shard)
                tampered_shard["child_ids"] = []
                shard_path.write_text(json.dumps(tampered_shard))
                with self.assertRaisesRegex(SystemExit, "3D map branch does not match"):
                    module.publish(project/"site")
                shard_path.write_text(original_shard)
                (project/"site/state.json").write_text('{}')
                with self.assertRaises(SystemExit):
                    module.publish(project/"site")
            finally:
                engine.store.close()


if __name__ == "__main__":
    unittest.main()
