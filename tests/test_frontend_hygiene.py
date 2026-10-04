"""Keep the public stylesheet tied to markup that still exists."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "wake" / "assets"


class FrontendHygieneTests(unittest.TestCase):
    def test_3d_map_relationship_trail_is_explicitly_navigational(self):
        script = (ASSETS / "map3d.js").read_text()
        css = (ASSETS / "map3d.css").read_text()

        self.assertIn("function relationshipTrail()", script)
        self.assertIn("RECORDED RELATIONSHIP PATH", script)
        self.assertIn("path.map((id,index)", script)
        self.assertIn("data-trail-node=", script)
        self.assertIn("choose(button.dataset.trailNode)", script)
        self.assertIn("Every hop is an exported parent → child relationship", script)
        self.assertIn("The path is navigational, not causal distance or evidentiary strength.", script)
        self.assertIn("pathStatus.textContent!==nextPathStatus", script)
        self.assertIn("EXPLICIT RELATIONSHIPS ONLY", script)
        self.assertIn(".detail-trail-list", css)
        self.assertIn(".constellation-shell>.field-head #path-status", css)
        self.assertIn("class=\"path-step\"", script)
        self.assertIn("relationship path step", script)
        self.assertIn(".constellation-node .path-step", css)
        self.assertIn('button[aria-current="location"]', css)

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
