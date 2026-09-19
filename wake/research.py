"""Bounded public-source collection. Sources are observations, never instructions."""

import hashlib
from html.parser import HTMLParser
import json
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ALLOWED_HOSTS = {"arxiv.org", "export.arxiv.org", "rss.arxiv.org", "plato.stanford.edu",
                 "api.crossref.org", "pmc.ncbi.nlm.nih.gov", "www.ncbi.nlm.nih.gov",
                 "quantum-journal.org", "journals.aps.org", "www.nature.com", "nature.com", "raw.githubusercontent.com"}
WAKE_SOURCES = {
    "default": "https://raw.githubusercontent.com/sudofx/wake/master/README.md",
    "architecture": "https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md",
    "experiment": "https://raw.githubusercontent.com/sudofx/wake/master/docs/experiment.md",
    "governance": "https://raw.githubusercontent.com/sudofx/wake/master/wake/governance.py",
    "engine": "https://raw.githubusercontent.com/sudofx/wake/master/wake/engine.py",
    "providers": "https://raw.githubusercontent.com/sudofx/wake/master/wake/providers.py",
    "research": "https://raw.githubusercontent.com/sudofx/wake/master/wake/research.py",
}


def allowed_url(url):
    if not isinstance(url, str) or len(url) > 2000:
        raise ValueError("Source URL must be text, at most 2000 characters")
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS or parsed.username or parsed.password or parsed.port not in (None, 443):
        raise ValueError("Source must use HTTPS on an approved research host")
    if parsed.hostname == "raw.githubusercontent.com" and not parsed.path.startswith("/sudofx/wake/"):
        raise ValueError("Repository research must stay within sudofx/wake")
    return url


class Redirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        allowed_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


class PlainText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "nav", "header", "footer"):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "header", "footer"):
            self.skip = max(0, self.skip - 1)

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.parts.append(data.strip())


def fetch_source(url):
    allowed_url(url)
    request = urllib.request.Request(url, headers={"User-Agent": "WAKE-research/3.0 (public research notebook; two sources per wake)"})
    with urllib.request.build_opener(Redirects()).open(request, timeout=25) as response:
        allowed_url(response.url)
        raw = response.read(1_000_001)
        if len(raw) > 1_000_000:
            raise ValueError("Source exceeds the one-megabyte collection limit")
        content_type = response.headers.get("Content-Type", "")
    decoded = raw.decode("utf-8", errors="replace")
    if "api.crossref.org" in url:
        items = json.loads(decoded).get("message", {}).get("items", [])
        text = json.dumps(items, ensure_ascii=False)
        scope = "bibliographic metadata and abstracts where supplied; not full papers"
    elif "export.arxiv.org/api/" in url:
        root = ET.fromstring(decoded)
        ns = {"a": "http://www.w3.org/2005/Atom"}
        text = "\n\n".join("\n".join(f"{key}: {entry.findtext('a:'+key, default='', namespaces=ns).strip()}" for key in ("title", "id", "published", "summary")) for entry in root.findall("a:entry", ns))
        scope = "paper abstracts; preprints, peer-review status not verified"
    elif "raw.githubusercontent.com" in url:
        text = decoded
        scope = "raw source-controlled WAKE repository text"
    elif "pdf" in content_type:
        raise ValueError("PDF extraction is not available; request the paper's abstract or HTML page")
    else:
        parser = PlainText()
        parser.feed(decoded)
        text = "\n".join(parser.parts)
        scope = "extracted web-page text; may be incomplete"
    if len(text.strip()) < 80:
        raise ValueError("Source did not provide enough readable content")
    # Keep raw-source fingerprints and explicit excerpt bounds; never claim full-text access.
    return {"url": url, "scope": scope, "excerpt": text[:10000],
            "excerpt_truncated": len(text) > 10000, "source_sha256": hashlib.sha256(raw).hexdigest()}


def query_url(query, domain):
    if domain == "wake_analysis":
        q = query.lower()
        choices = [
            (("architecture", "state", "continuity", "memory", "store"), "architecture"),
            (("experiment", "hypothesis", "test"), "experiment"),
            (("governance", "rule", "validation", "invariant"), "governance"),
            (("engine", "cycle", "context", "working set"), "engine"),
            (("provider", "prompt", "gemini", "model"), "providers"),
            (("collector", "research", "source", "evidence"), "research"),
        ]
        for needles, source in choices:
            if any(needle in q for needle in needles):
                return WAKE_SOURCES[source]
        return WAKE_SOURCES["default"]
    return "https://api.crossref.org/works?" + urllib.parse.urlencode({"query": query, "rows": 4, "select": "DOI,title,abstract,URL,published"})


def discovery_url(topic):
    """Map neutral topic rotation to a bounded source without exposing routing as a model instruction."""
    if topic["id"] == "wake_analysis":
        return WAKE_SOURCES["default"]
    return query_url(topic["query"], topic["id"])


def collect(engine, fetcher=fetch_source):
    """Called under the wake lock before inference; at most two unauthenticated requests."""
    state = engine.store.load()
    if not state.get("charter"):
        return
    attempts = len(state["invocations"])
    topics = state.get("research_topics", [])
    queued = [r for r in state.get("research", {}).values() if r["status"] == "queued"]
    # Topic rotation is authoritative. Model-authored follow-ups are durable
    # hypotheses, but they cannot consume collection bandwidth or accumulate
    # forever and eventually deadlock the four-item queue.
    discovery_count = min(2, len(topics))
    current_domains = {topics[(attempts + offset) % len(topics)]["id"] for offset in range(discovery_count)}
    # Retire queued follow-ups deterministically without fetching them. This keeps
    # them as an auditable record of model intent while preventing recursive topic
    # lock-in and permanent queue exhaustion.
    for item in queued:
        engine.store.append("research_collected", {
            "id": item["id"], "status": "superseded", "evidence": None})
    pending = []
    used_urls = set()
    for offset in range(discovery_count):
        topic = topics[(attempts + offset) % len(topics)]
        url = discovery_url(topic)
        if url in used_urls:
            continue
        pending.append({"id": f"discovery-{attempts}-{offset}", "url": url, "domain": topic["id"]})
        used_urls.add(url)

    for item in pending:
        url = item.get("url") or query_url(item["query"], item["domain"])
        try:
            observation = fetcher(url)
            # Trusted collector metadata activates forward-only verification and
            # binds evidence to the neutral topic that caused the retrieval.
            observation = {**observation, "verification_required": True, "topic_domain": item["domain"]}
            content = json.dumps(observation, ensure_ascii=False)
            status = "collected"
        except (ValueError, OSError, ET.ParseError) as exc:
            content = json.dumps({"url": url, "error": type(exc).__name__, "scope": "fetch failed; no evidence obtained"})
            status = "failed"
        import uuid
        evidence_id = "source-" + uuid.uuid4().hex[:16]
        engine.store.append("observation", {"id": evidence_id, "source": url,
                            "content": content, "actor": "collector", "scope": status})
        engine.store.append("research_collected", {"id": item["id"], "status": status, "evidence": evidence_id})
