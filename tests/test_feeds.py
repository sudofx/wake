# WAKE✳︎ MAINTAINER NOTE
#
# Executable specification for feeds.
# Tests in WAKE✳︎ are part of the explanation of the system: successful cases show what authority is allowed,
# while rejection/failure cases show the boundaries that must remain intact during refactors.
# Prefer assertions that make the invariant obvious to a human or AI maintainer reading this file later.

"""Subscription identities, safe full text, and durable publication boundaries."""
from copy import deepcopy
from email.utils import parsedate_to_datetime
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

from wake.engine import Engine
from wake.feeds import ATOM, HOME, LIMIT, build_feeds
from wake.providers import Fixture
from wake.report import export


class FeedTests(unittest.TestCase):
    def setUp(self):
        self.state = {
            "invocations": {
                "w-one": {"status": "accepted", "time": "2026-09-15T10:00:00-07:00",
                          "finished": "2026-09-15T10:01:00-07:00", "provider": "gemini", "model": "test"},
                "w-two": {"status": "accepted", "time": "2026-09-15T11:00:00-07:00",
                          "finished": "2026-09-15T11:01:00-07:00", "provider": "gemini", "model": "test"},
                "w-failed": {"status": "failed", "time": "2026-09-15T12:00:00-07:00"},
            },
            "journal": [
                {"invocation": "w-one", "cycle": 1, "title": "First & original", "summary": "First full journal text."},
                {"invocation": "w-two", "cycle": 2, "title": "Second", "summary": "Second full journal text."},
            ],
            "posts": {"first": {"id": "first", "created_by": "w-one", "created_version": 1,
                "title": "Bob & WAKE✳", "lede": "A <bounded> thought", "body": "Full body\n\n<script>alert('no')</script>\x00",
                "lens": "A philosophical reflection.", "status": "current"}},
        }

    def channel(self, kind):
        return ET.fromstring(build_feeds(self.state)[kind + ".xml"]).find("channel")

    def test_separate_feeds_have_full_content_and_stable_absolute_permalinks(self):
        before = deepcopy(self.state)
        blog, journal = self.channel("blog"), self.channel("journal")
        self.assertEqual(len(blog.findall("item")), 1)
        self.assertEqual(len(journal.findall("item")), 2)
        self.assertEqual(journal.findtext("item/title"), "Cycle 2 · Second")
        self.assertIn("Full body", blog.findtext("item/description"))
        self.assertIn("philosophical reflection", blog.findtext("item/description"))
        self.assertIn("Second full journal text", journal.findtext("item/description"))
        for kind, channel in (("blog", blog), ("journal", journal)):
            self.assertEqual(channel.find(f"{{{ATOM}}}link").attrib["href"], HOME + kind + ".xml")
            for item in channel.findall("item"):
                self.assertTrue(item.findtext("link").startswith(HOME))
                self.assertEqual(item.findtext("guid"), item.findtext("link"))
                self.assertEqual(item.find("guid").get("isPermaLink"), "true")
                self.assertIsNotNone(parsedate_to_datetime(item.findtext("pubDate")).tzinfo)
        self.assertEqual(parsedate_to_datetime(journal.findtext("item/pubDate")).hour, 18)
        self.assertEqual(before, self.state)
        first = build_feeds(self.state)
        self.state["invocations"]["unrelated"] = {"status": "deferred", "time": "2026-09-16T00:00:00Z"}
        self.assertEqual(build_feeds(self.state), first)

    def test_xml_and_embedded_html_are_safe_and_preserve_unicode(self):
        item = self.channel("blog").find("item")
        self.assertEqual(item.findtext("title"), "Bob & WAKE✳︎")
        body = item.findtext("description")
        self.assertIn("&lt;script&gt;", body)
        self.assertNotIn("<script>", body)
        self.assertNotIn("\x00", body)
        self.assertIn("&lt;bounded&gt;", body)

    def test_correction_has_its_own_identity_without_renumbering_the_original(self):
        original = self.channel("blog").find("item")
        self.state["posts"]["first"].update(status="superseded", superseded_by="correction")
        self.state["posts"]["correction"] = {**self.state["posts"]["first"], "id": "correction",
            "created_by": "w-two", "created_version": 2, "status": "current", "supersedes": "first"}
        self.state["posts"]["correction"].pop("superseded_by")
        items = self.channel("blog").findall("item")
        self.assertEqual(len(items), 2)
        self.assertEqual(items[1].findtext("guid"), original.findtext("guid"))
        self.assertEqual(items[1].findtext("pubDate"), original.findtext("pubDate"))
        self.assertIn("Read the newer correction", items[1].findtext("description"))
        self.assertIn("Corrects an earlier post", items[0].findtext("description"))

    def test_withheld_posts_and_failed_invocations_do_not_become_feed_items(self):
        self.state["invocations"]["w-two"]["editorial"] = {"status": "withheld", "action": {"type": "blog", "id": "never-published"}}
        self.state["posts"]["withheld"] = {**self.state["posts"]["first"], "id": "withheld", "status": "withheld"}
        self.state["journal"].append({"invocation": "w-failed", "cycle": 3, "title": "Failure", "summary": "Not an accepted wake"})
        self.assertEqual(len(self.channel("blog").findall("item")), 1)
        self.assertEqual(len(self.channel("journal").findall("item")), 2)

    def test_empty_feeds_and_recent_entry_limit(self):
        self.state["posts"].clear()
        self.state["journal"].clear()
        self.assertEqual(len(self.channel("blog").findall("item")), 0)
        self.assertIsNone(self.channel("journal").find("lastBuildDate"))
        for i in range(LIMIT + 5):
            iid = f"w-{i:03d}"
            self.state["invocations"][iid] = self.state["invocations"]["w-one"]
            self.state["journal"].append({"invocation": iid, "cycle": i + 1, "title": "Fixture", "summary": "Text"})
        items = self.channel("journal").findall("item")
        self.assertEqual(len(items), LIMIT)
        self.assertEqual(len({i.findtext("guid") for i in items}), LIMIT)

    def test_export_writes_feed_discovery_and_each_journal_permalink(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            engine = Engine(root / "data")
            try:
                engine.run(Fixture())
                export(engine.store, root / "site")
                item = ET.parse(root / "site/journal.xml").find("channel/item")
                target = root / "site" / item.findtext("link").removeprefix(HOME)
                self.assertTrue(target.is_file())
                self.assertIn("deterministic rehearsal", target.read_text())
                self.assertIn("Deterministic simulation", item.findtext("description"))
                for page in (root / "site/index.html", root / "site/map.html", target):
                    text = page.read_text()
                    self.assertIn('type="application/rss+xml"', text)
                    self.assertIn(HOME + "blog.xml", text)
                    self.assertIn(HOME + "journal.xml", text)
            finally:
                engine.store.close()
