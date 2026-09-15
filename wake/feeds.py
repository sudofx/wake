"""RSS 2.0 subscriptions derived from durable published records."""

from datetime import datetime, timezone
from email.utils import format_datetime
import html
import re
from urllib.parse import quote
import xml.etree.ElementTree as ET

HOME = "https://sudofx.github.io/wake/"
LIMIT = 100
ATOM = "http://www.w3.org/2005/Atom"
ET.register_namespace("atom", ATOM)


def clean(value):
    text = str(value).replace("WAKE✳︎", "WAKE✳").replace("WAKE✳", "WAKE✳︎")
    return re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\ud800-\udfff\ufffe\uffff]", "", text)


def paragraphs(text):
    return "".join(f"<p>{html.escape(clean(part))}</p>" for part in str(text).split("\n\n") if part.strip())


def published(invocation):
    # Use the durable acceptance time, never the current export time.
    value = invocation.get("finished") or invocation["time"]
    return datetime.fromisoformat(value).astimezone(timezone.utc)


def build_feeds(state):
    feeds = {}
    for kind, title, description in (
        ("blog", "Bob’s Blog / WAKE✳︎", "Bob’s published notes from WAKE✳︎’s durable research record."),
        ("journal", "WAKE✳︎ / The journal", "Accepted wake entries: research progress, evidence, and decisions."),
    ):
        root = ET.Element("rss", version="2.0")
        channel = ET.SubElement(root, "channel")

        def add(parent, tag, text, **attributes):
            element = ET.SubElement(parent, tag, attributes)
            element.text = clean(text)
            return element

        add(channel, "title", title)
        add(channel, "link", HOME + "index.html#" + kind)
        add(channel, "description", description)
        add(channel, "language", "en-us")
        add(channel, "ttl", "60")
        ET.SubElement(channel, f"{{{ATOM}}}link", href=HOME + kind + ".xml",
                      rel="self", type="application/rss+xml")
        records = []
        entries = state.get("posts", {}).values() if kind == "blog" else state["journal"]
        for entry in entries:
            iid = entry["created_by"] if kind == "blog" else entry["invocation"]
            invocation = state["invocations"][iid]
            if invocation["status"] != "accepted":
                continue
            if kind == "blog":
                if entry.get("status", "current") not in ("current", "superseded"):
                    continue
                url = HOME + "blog/" + quote(entry["id"], safe="") + ".html"
                body = paragraphs(entry["lede"]) + paragraphs(entry["body"])
                if entry.get("lens"):
                    body += "<h3>Bob’s Lens — philosophical reflection</h3>" + paragraphs(entry["lens"])
                for field, label in (("supersedes", "Corrects an earlier post"), ("superseded_by", "Read the newer correction")):
                    if entry.get(field):
                        target = HOME + "blog/" + quote(entry[field], safe="") + ".html"
                        body += f'<p><a href="{html.escape(target)}">{label}</a></p>'
                body += f'<p><a href="{html.escape(url)}">Read the post and its sources</a></p>'
                item_title = entry["title"]
            else:
                url = HOME + "journal/" + quote(iid, safe="") + ".html"
                body = paragraphs(entry["summary"])
                body += paragraphs(f"{invocation['provider']} / {invocation['model']}")
                if invocation["provider"] == "fixture":
                    body += paragraphs("Deterministic simulation, not a live model result.")
                item_title = f"Cycle {entry['cycle']} · {entry['title']}"
            records.append((published(invocation), url, item_title, body))
        records.sort(key=lambda row: (row[0], row[1]), reverse=True)
        if records:
            add(channel, "lastBuildDate", format_datetime(records[0][0], usegmt=True))
        for date, url, item_title, body in records[:LIMIT]:
            item = ET.SubElement(channel, "item")
            add(item, "title", item_title)
            add(item, "link", url)
            add(item, "guid", url, isPermaLink="true")
            add(item, "pubDate", format_datetime(date, usegmt=True))
            add(item, "description", body)
        ET.indent(root, space="  ")
        feeds[kind + ".xml"] = ET.tostring(root, encoding="utf-8", xml_declaration=True).decode("utf-8") + "\n"
    return feeds
