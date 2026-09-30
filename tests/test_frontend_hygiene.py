"""Keep the public stylesheet tied to markup that still exists."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "wake" / "assets"


class FrontendHygieneTests(unittest.TestCase):
    def test_every_style_class_has_a_current_caller(self):
        css = (ASSETS / "style.css").read_text()
        callers = "\n".join(
            (ASSETS / name).read_text()
            for name in (
                "index.html", "map.html", "map3d.html",
                "app.js", "pet.js", "help.js", "nav.js",
                "map.js", "map3d.js", "flat-view.js",
            )
        )
        callers += "\n" + (ROOT / "wake" / "report.py").read_text()

        classes = set(re.findall(r"\.([A-Za-z_-][A-Za-z0-9_-]*)", css))
        unused = sorted(
            name for name in classes
            if re.search(rf"(?<![A-Za-z0-9_-]){re.escape(name)}(?![A-Za-z0-9_-])", callers) is None
        )
        self.assertEqual(
            unused,
            [],
            "Remove dead CSS or add the current markup/rendering caller: " + ", ".join(unused),
        )


if __name__ == "__main__":
    unittest.main()
