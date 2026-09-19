# =============================================================================
# RESEARCH — the trusted collector boundary. Model-authored research requests are questions, not evidence. This layer retrieves bounded external material and records collection outcomes so later synthesis can cite independently acquired sources.
#
# MAINTENANCE PRINCIPLE
# ---------------------
# Read this file as part of a chain of custody.  WAKE✳︎ deliberately separates
# disposable cognition from durable authority.  Comments therefore explain not
# only what a function does, but why its boundary exists and what a refactor must
# not accidentally collapse.  Prefer explicit receipts, deterministic state
# transitions, and replayable facts over convenient hidden behavior.
# =============================================================================

"""Bounded public-source collection. Sources are observations, never instructions."""

import hashlib
from html.parser import HTMLParser
import json
import secrets
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ALLOWED_HOSTS = {
    # Scholarly indexes / open research
    "api.crossref.org", "api.openalex.org", "api.semanticscholar.org",
    "arxiv.org", "export.arxiv.org", "rss.arxiv.org",
    "pubmed.ncbi.nlm.nih.gov", "pmc.ncbi.nlm.nih.gov", "www.ncbi.nlm.nih.gov",
    "europepmc.org", "api.core.ac.uk", "doaj.org",
    # Universities / public knowledge institutions
    "plato.stanford.edu", "ourworldindata.org", "www.ourworldindata.org",
    "data.worldbank.org", "api.worldbank.org", "www.imf.org",
    "www.oecd.org", "data.oecd.org", "www.un.org",
    "www.noaa.gov", "www.nasa.gov", "science.nasa.gov",
    # Publishers / journals
    "quantum-journal.org", "journals.aps.org", "link.aps.org",
    "www.nature.com", "nature.com", "www.science.org",
    "journals.plos.org", "elifesciences.org", "www.pnas.org",
    # WAKE source-controlled self-analysis
    "raw.githubusercontent.com",
}
# WAKE self-analysis is intentionally allowed to inspect the implementation,
# not merely prose documentation. These are all source-controlled files from
# the same repository, so WAKE✳︎ can compare stated design with executable
# mechanics when it selects itself as a research topic.
WAKE_SOURCES = {
    "default": "https://raw.githubusercontent.com/sudofx/wake/master/README.md",
    "architecture": "https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md",
    "experiment": "https://raw.githubusercontent.com/sudofx/wake/master/docs/experiment.md",
    "governance": "https://raw.githubusercontent.com/sudofx/wake/master/wake/governance.py",
    "engine": "https://raw.githubusercontent.com/sudofx/wake/master/wake/engine.py",
    "providers": "https://raw.githubusercontent.com/sudofx/wake/master/wake/providers.py",
    "research": "https://raw.githubusercontent.com/sudofx/wake/master/wake/research.py",
    "store": "https://raw.githubusercontent.com/sudofx/wake/master/wake/store.py",
    "retrieval": "https://raw.githubusercontent.com/sudofx/wake/master/wake/retrieval.py",
    "provenance": "https://raw.githubusercontent.com/sudofx/wake/master/wake/provenance.py",
    "rejected": "https://raw.githubusercontent.com/sudofx/wake/master/wake/rejected.py",
    "scheduling": "https://raw.githubusercontent.com/sudofx/wake/master/wake/scheduling.py",
    "report": "https://raw.githubusercontent.com/sudofx/wake/master/wake/report.py",
    "feeds": "https://raw.githubusercontent.com/sudofx/wake/master/wake/feeds.py",
    "experiment_code": "https://raw.githubusercontent.com/sudofx/wake/master/wake/experiment.py",
    "cli": "https://raw.githubusercontent.com/sudofx/wake/master/wake/__main__.py",
    "config": "https://raw.githubusercontent.com/sudofx/wake/master/wake.toml",
    "topics": "https://raw.githubusercontent.com/sudofx/wake/master/research-topics.toml",
    "workflow": "https://raw.githubusercontent.com/sudofx/wake/master/.github/workflows/wake.yml",
    "github_runner": "https://raw.githubusercontent.com/sudofx/wake/master/scripts/github_wake.py",
    "cycle_runner": "https://raw.githubusercontent.com/sudofx/wake/master/scripts/run-wake-cycles.sh",
    "site_app": "https://raw.githubusercontent.com/sudofx/wake/master/wake/assets/app.js",
    "site_map": "https://raw.githubusercontent.com/sudofx/wake/master/wake/assets/map.js",
}


# ---------------------------------------------------------------------------
# STEP: allowed_url
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.
# ---------------------------------------------------------------------------

def allowed_url(url):
    if not isinstance(url, str) or len(url) > 2000:
        raise ValueError("Source URL must be text, at most 2000 characters")
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS or parsed.username or parsed.password or parsed.port not in (None, 443):
        raise ValueError("Source must use HTTPS on an approved research host")
    if parsed.hostname == "raw.githubusercontent.com" and not parsed.path.startswith("/sudofx/wake/"):
        raise ValueError("Repository research must stay within sudofx/wake")
    return url


# ---------------------------------------------------------------------------
# OBJECT: Redirects
#
# This object groups state/behavior exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.
# ---------------------------------------------------------------------------

class Redirects(urllib.request.HTTPRedirectHandler):
    # ---------------------------------------------------------------------------
    # STEP: redirect_request
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        allowed_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


# ---------------------------------------------------------------------------
# OBJECT: PlainText
#
# This object groups state/behavior exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.
# ---------------------------------------------------------------------------

class PlainText(HTMLParser):
    # ---------------------------------------------------------------------------
    # STEP: __init__
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.
    # ---------------------------------------------------------------------------
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts = []

    # ---------------------------------------------------------------------------
    # STEP: handle_starttag
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "nav", "header", "footer"):
            self.skip += 1

    # ---------------------------------------------------------------------------
    # STEP: handle_endtag
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "header", "footer"):
            self.skip = max(0, self.skip - 1)

    # ---------------------------------------------------------------------------
    # STEP: handle_data
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.parts.append(data.strip())


# ---------------------------------------------------------------------------
# STEP: fetch_source
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.
# ---------------------------------------------------------------------------

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
    elif "api.openalex.org" in url:
        results = json.loads(decoded).get("results", [])
        compact = []
        for work in results:
            abstract = work.get("abstract_inverted_index") or {}
            ordered = sorted(((pos, word) for word, positions in abstract.items() for pos in positions))
            compact.append({
                "id": work.get("id"), "doi": work.get("doi"), "title": work.get("title"),
                "publication_year": work.get("publication_year"),
                "type": work.get("type"), "cited_by_count": work.get("cited_by_count"),
                "open_access": work.get("open_access"),
                "primary_location": work.get("primary_location"),
                "abstract": " ".join(word for _, word in ordered) if ordered else None,
            })
        text = json.dumps(compact, ensure_ascii=False)
        scope = "OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers"
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


# ---------------------------------------------------------------------------
# STEP: query_url
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.
# ---------------------------------------------------------------------------

def query_url(query, domain):
    if domain == "wake_analysis":
        q = query.lower()
        choices = [
            (("architecture", "design"), "architecture"),
            (("hypothesis", "experiment document"), "experiment"),
            (("governance", "rule", "validation", "invariant", "reject"), "governance"),
            (("engine", "cycle", "working set", "orchestration"), "engine"),
            (("provider", "prompt", "gemini", "model", "bob"), "providers"),
            (("collector", "research", "source", "evidence", "discovery"), "research"),
            (("store", "sqlite", "database", "event", "hash", "durable", "continuity", "memory"), "store"),
            (("retrieval", "attention", "context"), "retrieval"),
            (("provenance", "graph", "map"), "provenance"),
            (("rejected", "failure", "withheld"), "rejected"),
            (("schedule", "quota", "cadence", "eligible"), "scheduling"),
            (("report", "render", "publish", "journal"), "report"),
            (("feed", "rss"), "feeds"),
            (("measurement", "instrumentation"), "experiment_code"),
            (("cli", "command"), "cli"),
            (("config", "toml", "setting"), "config"),
            (("topic", "attention space"), "topics"),
            (("workflow", "action", "github"), "workflow"),
            (("runner", "cloud"), "github_runner"),
            (("batch", "100 cycle", "terminal"), "cycle_runner"),
            (("site", "browser", "frontend", "ui"), "site_app"),
            (("map", "visual"), "site_map"),
        ]
        for needles, source in choices:
            if any(needle in q for needle in needles):
                return WAKE_SOURCES[source]
        return WAKE_SOURCES["default"]
    return "https://api.crossref.org/works?" + urllib.parse.urlencode({"query": query, "rows": 4, "select": "DOI,title,abstract,URL,published"})


# ---------------------------------------------------------------------------
# STEP: research_urls
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.
# ---------------------------------------------------------------------------

def research_urls(query, domain, attempts=0):
    """Return bounded routes for a neutral topic or a queued follow-up query."""
    if domain == "wake_analysis":
        primary = query_url(query, domain)
        # A WAKE✳︎ follow-up gets two distinct repository views when the fixed
        # collector budget permits it. The first follows the query; the second
        # rotates across implementation/config/workflow/UI files so self-study
        # is not trapped in README/docs or a single favored module.
        repo_routes = list(dict.fromkeys(WAKE_SOURCES.values()))
        alternate = repo_routes[attempts % len(repo_routes)]
        if alternate == primary:
            alternate = repo_routes[(attempts + 1) % len(repo_routes)]
        return [primary, alternate]
    crossref = query_url(query, domain)
    openalex = "https://api.openalex.org/works?" + urllib.parse.urlencode({
        "search": query, "per-page": 4,
        "select": "id,doi,title,publication_year,type,cited_by_count,open_access,primary_location,abstract_inverted_index",
    })
    routes = [crossref, openalex]
    if attempts % 2:
        routes.reverse()
    return routes


# ---------------------------------------------------------------------------
# STEP: discovery_urls
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.
# ---------------------------------------------------------------------------

def discovery_urls(topic, attempts=0):
    """Return bounded, topic-agnostic discovery routes."""
    return research_urls(topic["query"], topic["id"], attempts)


# ---------------------------------------------------------------------------
# STEP: discovery_url
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.
# ---------------------------------------------------------------------------

def discovery_url(topic):
    """Compatibility helper for callers that need one neutral discovery URL."""
    return discovery_urls(topic)[0]

# ---------------------------------------------------------------------------
# STEP: collect
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.
# ---------------------------------------------------------------------------

def collect(engine, fetcher=fetch_source):
    """Called under the wake lock before inference; at most two unauthenticated requests."""
    state = engine.store.load()
    if not state.get("charter"):
        return
    attempts = len(state["invocations"])
    topics = state.get("research_topics", [])
    queued = [r for r in state.get("research", {}).values() if r["status"] == "queued"]
    # Preserve two distinct forces inside the fixed two-request budget:
    # one continuation slot for model-authored follow-up work when available,
    # and one neutral discovery slot away from active project domains. This lets
    # projects actually progress without allowing them to monopolize attention.
    discovery_count = min(2, len(topics))
    rng = secrets.SystemRandom()
    active_domains = {p["domain"] for p in state.get("projects", {}).values()
                      if p.get("status") == "active"}
    alternatives = [topic for topic in topics if topic["id"] not in active_domains]
    pending = []
    used_urls = set()
    used_queue_ids = set()

    if queued and discovery_count:
        followup = rng.choice(queued)
        routes = research_urls(followup["query"], followup["domain"], attempts)
        url = routes[0]
        pending.append({"id": followup["id"], "url": url, "domain": followup["domain"],
                        "queued_followup": True})
        used_urls.add(url)
        used_queue_ids.add(followup["id"])

    remaining_slots = discovery_count - len(pending)
    if remaining_slots:
        pool = [topic for topic in alternatives
                if not pending or topic["id"] != pending[0]["domain"]]
        if len(pool) < remaining_slots:
            pool = [topic for topic in topics
                    if not pending or topic["id"] != pending[0]["domain"]]
        selected = rng.sample(pool, min(remaining_slots, len(pool)))
        for offset, topic in enumerate(selected, start=len(pending)):
            routes = discovery_urls(topic, attempts + offset)
            url = routes[0]
            if url in used_urls and len(routes) > 1:
                url = routes[1]
            if url in used_urls:
                continue
            pending.append({"id": f"discovery-{attempts}-{offset}", "url": url,
                            "domain": topic["id"], "queued_followup": False})
            used_urls.add(url)

    # Keep unselected follow-ups queued. They are durable hypotheses, not dead
    # letters; later cycles can service them without exceeding network budget.

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
        if item.get("queued_followup"):
            engine.store.append("research_collected", {"id": item["id"], "status": status, "evidence": evidence_id})
