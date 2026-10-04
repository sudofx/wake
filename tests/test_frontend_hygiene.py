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
        self.assertIn("detail.exact_record||'full history · journal invocation ID'", script)
        self.assertIn("EXACT INVOCATION RECEIPT", script)
        self.assertIn("basis:detail.exact_record||'full append-only history · invocation ID'", script)
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

    def test_full_history_supports_exact_receipt_deep_links(self):
        map_script = (ASSETS / "map3d.js").read_text()
        flat_script = (ASSETS / "flat-view.js").read_text()
        css = (ASSETS / "style.css").read_text()

        self.assertIn("events.html#seq=${exactSeq}", map_script)
        self.assertIn("events.html#event=${encodeURIComponent(invocationId)}", map_script)
        self.assertIn("events.html#event=${encodeURIComponent(lifecycleId)}", map_script)
        self.assertIn("data-event-seq=", flat_script)
        self.assertIn("data-event-id=", flat_script)
        self.assertIn("location.hash.match(/^#seq=(\\d+)$/)", flat_script)
        self.assertIn("location.hash.match(/^#event=(.+)$/)", flat_script)
        self.assertIn("target.classList.add('flat-target')", flat_script)
        self.assertIn("const eventHtml=events.map(event=>", flat_script)
        self.assertIn("eventHtml||'<p class=\"empty\">No recorded events.</p>'", flat_script)
        self.assertIn(".flat-target-status", css)
        self.assertIn(".entry.flat-target", css)
        self.assertIn("Adjacent receipts", flat_script)
        self.assertIn("ordered=[...events].sort", flat_script)
        self.assertIn("← EVENT '+esc(previous.seq)", flat_script)
        self.assertIn("EVENT '+esc(next.seq)+' →", flat_script)
        self.assertIn(".flat-target-status>nav{display:grid", css)
        self.assertIn("RETURN TO EXACT 3D INVOCATION ↗", flat_script)
        self.assertIn("map3d.html#record=invocation%3A", flat_script)
        self.assertIn("currentEvent?.kind==='accepted'", flat_script)
        self.assertIn(".flat-target-map{display:inline-flex", css)
        self.assertIn(".flat-target-map{min-height:44px;font-size:9px", css)

    def test_full_history_filters_without_hiding_deep_linked_receipts(self):
        flat_script = (ASSETS / "flat-view.js").read_text()
        css = (ASSETS / "style.css").read_text()

        self.assertIn("const eventKindCounts=events.reduce", flat_script)
        self.assertIn("const eventKinds=Object.keys(eventKindCounts).sort()", flat_script)
        self.assertIn("ALL KINDS · '+events.length", flat_script)
        self.assertIn('class="flat-history-tools"', flat_script)
        self.assertIn("data-event-kind=", flat_script)
        self.assertIn("const filterEvents=()=>", flat_script)
        self.assertIn("card.hidden=!(matchesKind&&matchesQuery)", flat_script)
        self.assertIn("if(target?.hidden)", flat_script)
        self.assertIn("if(search)search.value=''", flat_script)
        self.assertIn("if(kindFilter)kindFilter.value='all'", flat_script)
        self.assertIn("No receipts match the current history filter.", flat_script)
        self.assertIn(".flat-history-tools{position:sticky", css)
        self.assertIn(".flat-history-tools input,.flat-history-tools select{", css)
        self.assertIn("@media(max-width:700px){.flat-history-tools{position:static", css)
        self.assertIn('#flat-content [data-event-kind="accepted"]', css)
        self.assertIn('#flat-content [data-event-kind="rejected"]', css)
        self.assertIn('#flat-content [data-event-kind="failed"]', css)
        self.assertIn('#flat-content [data-event-kind="observation"]', css)
        self.assertIn('#flat-content [data-event-kind="invocation_started"]', css)

    def test_3d_map_first_load_record_hash_opens_requested_branch(self):
        script = (ASSETS / "map3d.js").read_text()

        self.assertIn("const recordFromHash=()=>", script)
        self.assertIn("const initialRecord=recordFromHash();if(initialRecord)choose(initialRecord)", script)
        self.assertIn("id.startsWith('root:')?['root:wake',id]", script)
        self.assertIn("await ensureBranch(id)", script)
        self.assertIn("writeRecordHash(current())", script)

    def test_3d_map_uses_side_inspector_on_macbook_widths(self):
        css = (ASSETS / "map3d.css").read_text()

        self.assertIn("@media (min-width:1400px) and (max-width:1920px)", css)
        self.assertIn(".constellation-workspace:has(>#details.active)", css)
        self.assertIn("grid-template-columns:minmax(0,1fr) clamp(320px,22vw,380px)", css)
        self.assertIn(".constellation-workspace>#details.active{", css)
        self.assertIn("position:sticky", css)
        self.assertIn("max-height:calc(100svh - 92px)", css)

    def test_3d_relationship_trail_keeps_current_node_visible(self):
        script = (ASSETS / "map3d.js").read_text()
        self.assertIn("function centerCurrentRelationshipTrail()", script)
        self.assertIn("[data-trail-node][aria-current=\"location\"]", script)
        self.assertIn("list.scrollWidth<=list.clientWidth", script)
        self.assertIn("active.offsetLeft-(list.clientWidth-active.offsetWidth)/2", script)
        self.assertIn("centerCurrentRelationshipTrail()", script)

    def test_3d_up_navigation_keeps_shareable_record_url_in_sync(self):
        script = (ASSETS / "map3d.js").read_text()
        self.assertIn("function goUp(){if(path.length<2)return release();", script)
        self.assertIn("frameSelection(current());writeRecordHash(current())", script)

    def test_3d_details_are_copyable_and_phone_controls_stay_reachable(self):
        css = (ASSETS / "map3d.css").read_text()
        self.assertIn(".constellation-shell>#details{user-select:text;-webkit-user-select:text}", css)
        self.assertIn(".detail-heading-actions button,.detail-trail-list button,.detail-artifacts button{user-select:none", css)
        self.assertIn("@media(max-width:700px){.detail-heading{position:sticky;top:-20px", css)
        self.assertIn(".detail-heading-actions button{min-height:44px}", css)

    def test_second_click_releases_selected_3d_record(self):
        script = (ASSETS / "map3d.js").read_text()
        self.assertIn("if(id===current())return release();", script)

    def test_3d_help_copy_matches_pointer_type(self):
        html = (ASSETS / "map3d.html").read_text()
        css = (ASSETS / "map3d.css").read_text()
        self.assertIn('class="pointer-help">Hover for preview · click for details · click again to release · drag to pan', html)
        self.assertIn('class="touch-help">Tap a sphere for details · tap again to release · drag to pan · pinch to zoom', html)
        self.assertIn('.touch-help{display:none}', css)
        self.assertIn('@media(pointer:coarse){.pointer-help{display:none}.touch-help{display:inline}}', css)

    def test_3d_keyboard_selection_preserves_focus_and_pressed_state(self):
        script = (ASSETS / "map3d.js").read_text()
        self.assertIn('aria-pressed="${focused?\'true\':\'false\'}"', script)
        self.assertIn('aria-pressed="${selected?\'true\':\'false\'}"', script)
        self.assertIn("const restoreKeyboardFocus=()=>requestAnimationFrame", script)
        self.assertIn("target?.focus({preventScroll:true})", script)
        self.assertIn("choose(node.dataset.node).then(restoreKeyboardFocus)", script)

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
