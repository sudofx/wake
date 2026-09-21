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
import re
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
    "raw.githubusercontent.com", "api.github.com",
}
# Idea-pool hosts are deliberately not evidence hosts. Their observations are
# permanently stamped as discovery leads and cannot satisfy governance.
ALLOWED_ALT_HOSTS = {"en.wikipedia.org", "theconversation.com", "aeon.co"}


def persistent_identifiers(observation):
    """Extract conservative persistent IDs from collector output, not model prose."""
    text = json.dumps(observation, ensure_ascii=False) if isinstance(observation, dict) else str(observation)
    values = []
    values += ["doi:" + item.rstrip(".,;:)]}").lower()
               for item in re.findall(r"10\.\d{4,9}/[-._;()/:a-zA-Z0-9]+", text)]
    values += ["openalex:" + item.rsplit("/", 1)[-1] for item in re.findall(r"https?://openalex\.org/[Ww]\d+", text)]
    values += ["arxiv:" + item for item in re.findall(r"\b\d{4}\.\d{4,5}(?:v\d+)?\b", text)]
    return list(dict.fromkeys(values))[:12]
# WAKE self-analysis is intentionally allowed to inspect the implementation,
# not merely prose documentation. These are all source-controlled files from
# the same repository, so WAKE✳︎ can compare stated design with executable
# mechanics when it selects itself as a research topic.
WAKE_SOURCES = {
    # The recursive tree is the discovery index for self-analysis. It exposes
    # repository paths, not file contents, so a disposable model can discover
    # code/tests/assets/configuration that are not named in this hand-curated
    # convenience map and then request the corresponding raw file on a later
    # collector pass.
    "tree": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
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
    if parsed.hostname == "api.github.com" and parsed.path != "/repos/sudofx/wake/git/trees/master":
        raise ValueError("GitHub API research is limited to the sudofx/wake master tree")
    return url


def allowed_discovery_url(url):
    if not isinstance(url, str) or len(url) > 2000:
        raise ValueError("Source URL must be text, at most 2000 characters")
    parsed = urllib.parse.urlsplit(url)
    if (parsed.scheme != "https" or parsed.hostname not in ALLOWED_ALT_HOSTS
            or parsed.username or parsed.password or parsed.port not in (None, 443)):
        raise ValueError("Discovery source must use HTTPS on an approved discovery host")
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
    def __init__(self, validator=allowed_url):
        super().__init__()
        self.validator = validator
    # ---------------------------------------------------------------------------
    # STEP: redirect_request
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.validator(newurl)
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

def fetch_source(url, discovery_only=False):
    validator = allowed_discovery_url if discovery_only else allowed_url
    validator(url)
    request = urllib.request.Request(url, headers={"User-Agent": "WAKE-research/3.0 (public research notebook; two sources per wake)"})
    with urllib.request.build_opener(Redirects(validator)).open(request, timeout=25) as response:
        validator(response.url)
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
    elif "api.github.com/repos/sudofx/wake/git/trees/master" in url:
        tree = json.loads(decoded).get("tree", [])
        text = json.dumps([
            {"path": item.get("path"), "type": item.get("type"), "size": item.get("size")}
            for item in tree if item.get("type") == "blob"
        ], ensure_ascii=False)
        scope = "recursive source-controlled WAKE repository file index; paths and sizes, not file contents"
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
        # Unknown self-analysis questions begin with the repository index rather
        # than README. This prevents the curated map from becoming an accidental
        # boundary on what future disposable workers are able to discover.
        return WAKE_SOURCES["tree"]
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


def evidence_role(url):
    """Classify an observation without asking the model to trust its own search.

    A Crossref/OpenAlex search response is a lead list: it can name papers, but
    it is not itself a paper selected for a project's question.  A later
    follow-up may request one exact API record (or an approved page), which is
    eligible for the stricter notebook gate.
    """
    parsed = urllib.parse.urlsplit(url)
    query = urllib.parse.parse_qs(parsed.query)
    if parsed.hostname == "api.crossref.org" and parsed.path == "/works" and "query" in query:
        return "discovery"
    if parsed.hostname == "api.openalex.org" and parsed.path == "/works" and "search" in query:
        return "discovery"
    return "source"


# ---------------------------------------------------------------------------
# STEP: discovery_urls
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.
# ---------------------------------------------------------------------------

def discovery_urls(topic, attempts=0):
    """Begin neutral discovery in the explicitly non-evidentiary idea pool."""
    # Self-analysis is a special, source-controlled domain: its repository tree
    # is already a safe discovery index and remains more useful than a generic
    # third-party idea pool.
    if topic["id"] == "wake_analysis":
        return research_urls(topic["query"], topic["id"], attempts)
    query = urllib.parse.urlencode({"action": "query", "list": "search", "srsearch": topic["query"], "format": "json"})
    return ["https://en.wikipedia.org/w/api.php?" + query,
            research_urls(topic["query"], topic["id"], attempts)[0]]


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
    def awaiting_capability_retry(request):
        summary = state.get("acquisition", {}).get(request["project"], {})
        return (summary.get("capability_blocked")
                and state["version"] < summary.get("retry_after_version", state["version"] + 1))

    queued = [r for r in state.get("research", {}).values()
              if r["status"] == "queued" and not awaiting_capability_retry(r)]
    # Preserve two distinct forces inside the fixed two-request budget:
    # one continuation slot for model-authored follow-up work when available,
    # and one neutral discovery slot away from active project domains. This lets
    # projects actually progress without allowing them to monopolize attention.
    # Observation mode is a bounded, explicitly configured wider sample. It
    # changes collection volume only; every collected item still receives the
    # same topic and evidence-role provenance stamp.
    budget = engine.config["research_collection_budget"] if engine.config.get("observation_mode") else 2
    discovery_count = min(budget, len(topics))
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
        # A model may turn a promising discovery result into an approved exact
        # record URL.  Preserve that choice; replacing it with another broad
        # search is what previously trapped projects in discovery loops.
        url = followup.get("url") or routes[0]
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
                            "domain": topic["id"], "queued_followup": False,
                            "discovery_only": urllib.parse.urlsplit(url).hostname in ALLOWED_ALT_HOSTS})
            used_urls.add(url)

    # Keep unselected follow-ups queued. They are durable hypotheses, not dead
    # letters; later cycles can service them without exceeding network budget.

    for item in pending:
        url = item.get("url") or query_url(item["query"], item["domain"])
        try:
            (allowed_discovery_url(url) if item.get("discovery_only") else allowed_url(url))
            observation = (fetch_source(url, discovery_only=True) if fetcher is fetch_source and item.get("discovery_only")
                           else fetcher(url))
            # Trusted collector metadata activates forward-only verification and
            # binds evidence to the neutral topic that caused the retrieval.
            observation = {
                **observation,
                "verification_required": True,
                "topic_domain": item["domain"],
                "evidence_role": "discovery" if item.get("discovery_only") else evidence_role(url),
                "host_tier": "discovery" if item.get("discovery_only") else "verification",
                "persistent_identifiers": persistent_identifiers(observation),
            }
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
            payload = json.loads(content)
            role = payload.get("evidence_role", "discovery")
            outcome = "progress" if status == "collected" and role == "source" else (
                "route_failure" if status == "failed" else "no_progress")
            engine.store.append("acquisition_assessed", {"project": followup["project"],
                "domain": item["domain"], "research_id": item["id"],
                "route": urllib.parse.urlsplit(url).hostname + ":" + role,
                "stage": "substantive_source" if role == "source" else "discovery",
                "outcome": outcome, "evidence": evidence_id,
                "persistent_identifiers": payload.get("persistent_identifiers", [])})
