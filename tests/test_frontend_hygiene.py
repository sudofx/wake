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

    def test_3d_map_links_explicit_record_types_into_data_story(self):
        script = (ASSETS / "map3d.js").read_text()
        css = (ASSETS / "map3d.css").read_text()

        self.assertIn("function storyDestination(node)", script)
        self.assertIn("status==='rejected'", script)
        self.assertIn("node?.kind==='belief'", script)
        self.assertIn("node?.kind==='commitment'||branch==='root:commitments'", script)
        self.assertIn("['evidence','research','project','notebook'].includes(node?.kind)", script)
        self.assertIn("default record view; no semantic inference", script)
        self.assertIn('href="index.html#metrics/${route.target}"', script)
        self.assertIn("DATA STORY · ${route.chapter} / ${route.name}", script)
        self.assertIn(".detail-story-link", css)

    def test_3d_map_pairs_story_context_with_durable_record_routes(self):
        script = (ASSETS / "map3d.js").read_text()
        css = (ASSETS / "map3d.css").read_text()

        self.assertIn("function durableRecordDestination(node)", script)
        self.assertIn("EXACT WAKE RECEIPT", script)
        self.assertIn("EXACT INVOCATION RECEIPT", script)
        self.assertIn("DURABLE PUBLICATION", script)
        self.assertIn("EVIDENCE RECORD", script)
        self.assertIn("PROJECT RECORD", script)
        self.assertIn("NOTEBOOK RECORD", script)
        self.assertIn("LIFECYCLE RECEIPT", script)
        self.assertIn("function detailContextLinks(node)", script)
        self.assertIn("detail-record-link", script)
        self.assertIn(".detail-context-links{display:grid", css)
        self.assertIn(".detail-record-link", css)
        self.assertIn(".detail-context-links{grid-template-columns:1fr}", css)

    def test_3d_map_uses_side_inspector_on_macbook_widths(self):
        css = (ASSETS / "map3d.css").read_text()

        self.assertIn("@media (min-width:1400px) and (max-width:1920px)", css)
        self.assertIn(".constellation-workspace:has(>#details.active)", css)
        self.assertIn("grid-template-columns:minmax(0,1fr) clamp(320px,22vw,380px)", css)
        self.assertIn(".constellation-workspace>#details.active{", css)
        self.assertIn("position:sticky", css)
        self.assertIn("max-height:calc(100svh - 92px)", css)

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
