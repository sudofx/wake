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
                export(engine.store, project/"site")
                for name in ("events.md", "events.html", "state.md", "state.html"):
                    self.assertTrue((project/"site"/name).is_file())
                page = (project/"site/index.html").read_text()
                self.assertIn('href="events.html">Readable history', page)
                self.assertIn('href="state.html">State', page)
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
                    ".nojekyll", "index.html", "journal.md", "style.css", "nav.css", "map.css", "map3d.css", "theme.css",
                    "state.json", "state.md", "state.html",
                    "events.jsonl", "events.md", "events.html",
                    "head.txt", "map.html", "map-data.json", "map3d.html", "map3d-data.json", "blog.xml", "journal.xml", "journal",
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
                (project/"site/state.json").write_text('{}')
                with self.assertRaises(SystemExit):
                    module.publish(project/"site")
            finally:
                engine.store.close()


if __name__ == "__main__":
    unittest.main()
