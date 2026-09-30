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

from contextlib import contextmanager
import hashlib
import io
from html.parser import HTMLParser
import json
import re
import secrets
import signal
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from pypdf import PdfReader

ALLOWED_HOSTS = {
    # Scholarly indexes / open research
    "api.crossref.org", "api.openalex.org", "api.semanticscholar.org",
    "api.datacite.org", "doi.org", "arxiv.org", "export.arxiv.org", "rss.arxiv.org",
    "pubmed.ncbi.nlm.nih.gov", "pmc.ncbi.nlm.nih.gov", "www.ncbi.nlm.nih.gov",
    "europepmc.org", "api.core.ac.uk", "doaj.org", "eric.ed.gov",
    # Universities / public knowledge institutions
    "plato.stanford.edu", "ourworldindata.org", "www.ourworldindata.org",
    "data.worldbank.org", "api.worldbank.org", "www.imf.org",
    "www.oecd.org", "data.oecd.org", "www.un.org",
    "www.noaa.gov", "www.nasa.gov", "science.nasa.gov",
    # Open-access and scholarly publishers / journals
    "frontiersin.org", "www.frontiersin.org",
    "quantum-journal.org", "journals.aps.org", "link.aps.org",
    "www.nature.com", "nature.com", "www.science.org",
    "journals.plos.org", "elifesciences.org", "www.pnas.org",
    "royalsocietypublishing.org", "academic.oup.com", "www.cambridge.org",
    "link.springer.com", "springeropen.com", "www.springeropen.com",
    "biomedcentral.com", "www.biomedcentral.com",
    "bmj.com", "www.bmj.com", "jamanetwork.com", "www.jamanetwork.com",
    # Preprints remain source material but are explicitly tiered as preprints.
    "osf.io", "psyarxiv.com", "www.psyarxiv.com",
    # WAKE source-controlled self-analysis
    "raw.githubusercontent.com", "api.github.com",
}
# Idea-pool hosts are deliberately not evidence hosts. Their observations are
# permanently stamped as discovery leads and cannot satisfy governance.
ALLOWED_ALT_HOSTS = {"en.wikipedia.org", "theconversation.com", "aeon.co"}
ALLOWED_HOST_SUFFIXES = (".biomedcentral.com", ".springeropen.com")
SOURCE_PROCESSING_TIMEOUT_SECONDS = 15


@contextmanager
def _source_deadline(seconds):
    """Hard-stop one source fetch/parse on POSIX runners.

    urllib's socket timeout cannot bound CPU-heavy PDF parsing, so live cycles
    also need a wall-clock deadline around the entire source operation.
    """
    if not hasattr(signal, "SIGALRM") or not hasattr(signal, "setitimer"):
        yield
        return

    def expired(_signum, _frame):
        raise TimeoutError("Source processing exceeded its wall-clock deadline")

    previous_handler = signal.getsignal(signal.SIGALRM)
    signal.signal(signal.SIGALRM, expired)
    previous_timer = signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, *previous_timer)
        signal.signal(signal.SIGALRM, previous_handler)


def _approved_host(hostname):
    return hostname in ALLOWED_HOSTS or any(
        hostname and hostname.endswith(suffix) for suffix in ALLOWED_HOST_SUFFIXES
    )


def persistent_identifiers(observation):
    """Extract conservative persistent IDs from collector output, not model prose."""
    text = json.dumps(observation, ensure_ascii=False) if isinstance(observation, dict) else str(observation)
    values = []
    values += ["doi:" + item.rstrip(".,;:)]}").lower()
               for item in re.findall(r"10\.\d{4,9}/[-._;()/:a-zA-Z0-9]+", text)]
    values += ["openalex:" + item.rsplit("/", 1)[-1] for item in re.findall(r"https?://openalex\.org/[Ww]\d+", text)]
    # Bare YYYY.NNNN patterns also occur inside DOI suffixes. Treat a value as
    # arXiv only when the collector output explicitly labels it or carries an
    # arxiv.org URL; otherwise DOI fragments become fake retrieval leads.
    arxiv_ids = re.findall(
        r"https?://(?:export\.)?arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5}(?:v\d+)?)(?:\.pdf)?",
        text,
        re.I,
    )
    arxiv_ids += re.findall(
        r"\barxiv\s*[:=]\s*[\"']?(\d{4}\.\d{4,5}(?:v\d+)?)",
        text,
        re.I,
    )
    values += ["arxiv:" + item.lower() for item in arxiv_ids]
    values += ["pmc:" + item.upper() for item in re.findall(r"\bPMC\d+\b", text, re.I)]
    values += ["pmid:" + item for item in re.findall(r'"(?:PubMed|PMID)"\s*:\s*"?(\d{5,10})', text, re.I)]
    return list(dict.fromkeys(values))[:12]


def route_source_identity(url):
    """Return the persistent work identity encoded by a deterministic retrieval route."""
    if not isinstance(url, str):
        return None
    parsed = urllib.parse.urlsplit(url)
    if parsed.hostname == "api.crossref.org" and parsed.path.startswith("/works/"):
        doi = urllib.parse.unquote(parsed.path[len("/works/"):]).strip()
        return "doi:" + doi.lower() if doi else None
    if parsed.hostname == "doi.org":
        doi = urllib.parse.unquote(parsed.path.lstrip("/")).strip()
        return "doi:" + doi.lower() if doi.startswith("10.") else None
    if parsed.hostname == "api.openalex.org" and parsed.path.startswith("/works/"):
        work = urllib.parse.unquote(parsed.path[len("/works/"):]).strip()
        return "openalex:" + work if re.fullmatch(r"[Ww]\d+", work) else None
    if parsed.hostname == "export.arxiv.org":
        arxiv_id = urllib.parse.parse_qs(parsed.query).get("id_list", [""])[0].strip()
        return "arxiv:" + arxiv_id if re.fullmatch(r"\d{4}\.\d{4,5}(?:v\d+)?", arxiv_id) else None
    marker = "/research/bionlp/RESTful/pmcoa.cgi/BioC_json/"
    if parsed.hostname == "www.ncbi.nlm.nih.gov" and marker in parsed.path:
        value = urllib.parse.unquote(parsed.path.split(marker, 1)[1].split("/", 1)[0]).strip()
        if re.fullmatch(r"PMC\d+", value, re.I):
            return "pmc:" + value.upper()
        if re.fullmatch(r"\d{5,10}", value):
            return "pmid:" + value
    return None


def candidate_source_urls(observation, current_url=""):
    """Extract approved readable-source leads from trusted collector output.

    Metadata indexes are useful routing infrastructure, but they are not the
    research object itself. This helper deterministically promotes only HTTPS
    URLs already present in collected metadata and already accepted by the
    collector allowlist. HTTPS PDF links may qualify as candidates when their host already passes the
    collector allowlist; bounded parsing still decides whether readable evidence
    was actually obtained.
    """
    text = json.dumps(observation, ensure_ascii=False) if isinstance(observation, dict) else str(observation)
    candidates = []
    metadata_hosts = {
        "api.crossref.org", "api.openalex.org", "api.semanticscholar.org",
        "api.datacite.org",
    }
    for raw in re.findall(r"https://[^\s\"'<>]+", text):
        url = raw.rstrip(".,;:)]}")
        parsed = urllib.parse.urlsplit(url)
        if not parsed.hostname or parsed.hostname in metadata_hosts:
            continue
        if current_url and url == current_url:
            continue
        try:
            allowed_url(url)
        except ValueError:
            continue
        if url not in candidates:
            candidates.append(url)
    return candidates[:8]


def exact_identifier_url(identifier):
    """Convert a collector-discovered persistent ID into one exact approved record URL.

    Discovery indexes are lead generators, not notebook evidence. This trusted,
    deterministic promotion step removes the disposable model from the mechanical
    job of translating a DOI/OpenAlex/arXiv identifier into an exact verification
    request. It does not choose claims or relax governance.
    """
    if not isinstance(identifier, str):
        return None
    if identifier.startswith("doi:"):
        doi = identifier[4:].strip()
        return ("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")) if doi else None
    if identifier.startswith("openalex:"):
        work = identifier.split(":", 1)[1].strip()
        return ("https://api.openalex.org/works/" + urllib.parse.quote(work, safe="")) if re.fullmatch(r"[Ww]\d+", work) else None
    if identifier.startswith("arxiv:"):
        arxiv_id = identifier.split(":", 1)[1].strip()
        # With bounded PDF extraction available, retrieve the preprint itself
        # rather than promoting an abstract-only Atom record to source evidence.
        return (
            "https://arxiv.org/pdf/" + urllib.parse.quote(arxiv_id, safe="") + ".pdf"
            if re.fullmatch(r"\d{4}\.\d{4,5}(?:v\d+)?", arxiv_id)
            else None
        )
    if identifier.startswith("pmc:"):
        pmc_id = identifier.split(":", 1)[1].strip().upper()
        return ("https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/"
                + urllib.parse.quote(pmc_id, safe="") + "/unicode") if re.fullmatch(r"PMC\d+", pmc_id) else None
    if identifier.startswith("pmid:"):
        pmid = identifier.split(":", 1)[1].strip()
        return ("https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/"
                + urllib.parse.quote(pmid, safe="") + "/unicode") if re.fullmatch(r"\d{5,10}", pmid) else None
    return None
# Repository-analysis topics may inspect source-controlled implementation,
# not merely prose documentation. The capability is generic; activation and
# repository identity come from research-topics.toml rather than a hardcoded
# topic ID.
REPOSITORY_SOURCE_PATHS = {
    "tree": None,
    "default": "README.md",
    "architecture": "docs/architecture.md",
    "experiment": "docs/experiment.md",
    "governance": "wake/governance.py",
    "engine": "wake/engine.py",
    "providers": "wake/providers.py",
    "research": "wake/research.py",
    "store": "wake/store.py",
    "retrieval": "wake/retrieval.py",
    "provenance": "wake/provenance.py",
    "rejected": "wake/rejected.py",
    "scheduling": "wake/scheduling.py",
    "report": "wake/report.py",
    "feeds": "wake/feeds.py",
    "experiment_code": "wake/experiment.py",
    "cli": "wake/__main__.py",
    "config": "wake.toml",
    "topics": "research-topics.toml",
    "workflow": ".github/workflows/wake.yml",
    "github_runner": "scripts/github_wake.py",
    "cycle_runner": "scripts/run-wake-cycles.sh",
    "site_app": "wake/assets/app.js",
    "site_map": "wake/assets/map.js",
}


def repository_sources(repository):
    """Build the bounded source map for one configured repository topic."""
    base = "https://raw.githubusercontent.com/" + repository + "/master/"
    return {
        key: (
            "https://api.github.com/repos/" + repository + "/git/trees/master?recursive=1"
            if key == "tree" else base + path
        )
        for key, path in REPOSITORY_SOURCE_PATHS.items()
    }

# ---------------------------------------------------------------------------
# STEP: allowed_url
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.
# ---------------------------------------------------------------------------

def allowed_url(url, repository="sudofx/wake"):
    if not isinstance(url, str) or len(url) > 2000:
        raise ValueError("Source URL must be text, at most 2000 characters")
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or not _approved_host(parsed.hostname) or parsed.username or parsed.password or parsed.port not in (None, 443):
        raise ValueError("Source must use HTTPS on an approved research host")
    repo_path = "/" + repository + "/"
    if parsed.hostname == "raw.githubusercontent.com" and not parsed.path.startswith(repo_path):
        raise ValueError("Repository research must stay within " + repository)
    if parsed.hostname == "api.github.com" and parsed.path != "/repos/" + repository + "/git/trees/master":
        raise ValueError("GitHub API research is limited to the configured repository master tree")
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

def _fetch_source_unbounded(url, discovery_only=False):
    validator = allowed_discovery_url if discovery_only else allowed_url
    validator(url)
    request = urllib.request.Request(url, headers={"User-Agent": "WAKE-research/3.0 (public research notebook; two sources per wake)"})
    with urllib.request.build_opener(Redirects(validator)).open(request, timeout=10) as response:
        validator(response.url)
        content_type = response.headers.get("Content-Type", "")
        is_pdf = "pdf" in content_type.lower() or response.url.lower().split("?", 1)[0].endswith(".pdf")
        byte_limit = 8_000_000 if is_pdf else 1_000_000
        raw = response.read(byte_limit + 1)
        if len(raw) > byte_limit:
            raise ValueError(
                "PDF exceeds the eight-megabyte collection limit"
                if is_pdf else "Source exceeds the one-megabyte collection limit"
            )
    decoded = "" if is_pdf else raw.decode("utf-8", errors="replace")
    if "api.crossref.org" in url:
        message = json.loads(decoded).get("message", {})
        items = message.get("items", [message] if isinstance(message, dict) else [])
        text = json.dumps(items, ensure_ascii=False)
        scope = "Crossref bibliographic metadata and abstracts where supplied; not full papers"
    elif "api.datacite.org" in url:
        payload = json.loads(decoded)
        records = payload.get("data", [])
        if isinstance(records, dict):
            records = [records]
        compact = []
        for record in records:
            attrs = record.get("attributes", {})
            compact.append({
                "id": record.get("id"), "doi": attrs.get("doi"),
                "titles": attrs.get("titles"), "publisher": attrs.get("publisher"),
                "publicationYear": attrs.get("publicationYear"),
                "types": attrs.get("types"), "subjects": attrs.get("subjects"),
                "descriptions": attrs.get("descriptions"),
                "url": attrs.get("url"),
            })
        text = json.dumps(compact, ensure_ascii=False)
        scope = "DataCite DOI metadata and descriptions where supplied; not full papers"
    elif "api.semanticscholar.org" in url:
        payload = json.loads(decoded)
        records = payload.get("data", [payload] if isinstance(payload, dict) else [])
        compact = [{
            "paperId": item.get("paperId"), "title": item.get("title"),
            "year": item.get("year"), "abstract": item.get("abstract"),
            "url": item.get("url"), "externalIds": item.get("externalIds"),
            "openAccessPdf": item.get("openAccessPdf"),
        } for item in records]
        text = json.dumps(compact, ensure_ascii=False)
        scope = "Semantic Scholar scholarly metadata and abstracts where supplied; not full papers"
    elif "api.openalex.org" in url:
        payload = json.loads(decoded)
        # OpenAlex search endpoints wrap works in `results`, while an exact
        # /works/W... lookup returns the work object directly. Treat both shapes
        # identically so a DOI/OpenAlex discovery lead can be mechanically
        # promoted into one exact qualifying source record.
        if isinstance(payload, dict) and isinstance(payload.get("results"), list):
            works = payload["results"]
        elif isinstance(payload, dict) and payload.get("id"):
            works = [payload]
        else:
            works = []
        compact = []
        for work in works:
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
    elif "www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/" in url:
        payload = json.loads(decoded)
        documents = payload if isinstance(payload, list) else [payload]
        parts = []
        for document in documents:
            if not isinstance(document, dict):
                continue
            for passage in document.get("passages", []):
                if not isinstance(passage, dict):
                    continue
                passage_text = str(passage.get("text") or "").strip()
                if passage_text:
                    parts.append(passage_text)
        text = "\n\n".join(parts)
        scope = (
            "NCBI PMC open-access article text via BioC JSON; "
            "figures, tables, equations, and formatting may be incomplete"
        )
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
    elif is_pdf:
        try:
            reader = PdfReader(io.BytesIO(raw), strict=False)
            if reader.is_encrypted:
                try:
                    if reader.decrypt("") == 0:
                        raise ValueError("Encrypted PDF cannot be read")
                except Exception as exc:
                    raise ValueError("Encrypted PDF cannot be read") from exc
            parts = []
            total_chars = 0
            for page in reader.pages[:24]:
                page_text = (page.extract_text() or "").strip()
                if not page_text:
                    continue
                remaining = 50_000 - total_chars
                if remaining <= 0:
                    break
                parts.append(page_text[:remaining])
                total_chars += min(len(page_text), remaining)
            text = "\n\n".join(parts)
        except ValueError:
            raise
        except Exception as exc:
            raise ValueError("PDF text extraction failed") from exc
        scope = (
            "bounded PDF text extraction from up to 24 pages; "
            "figures, tables, equations, layout, and scanned-image text may be incomplete"
        )
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


def fetch_source(url, discovery_only=False):
    with _source_deadline(SOURCE_PROCESSING_TIMEOUT_SECONDS):
        return _fetch_source_unbounded(url, discovery_only=discovery_only)


# ---------------------------------------------------------------------------
# STEP: query_url
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.
# ---------------------------------------------------------------------------

def query_url(query, domain, topic=None):
    if topic and topic.get("source_kind") == "repository":
        q = query.lower()
        sources = repository_sources(topic["repository"])
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
                return sources[source]
        # Unknown self-analysis questions begin with the repository index rather
        # than README. This prevents the curated map from becoming an accidental
        # boundary on what future disposable workers are able to discover.
        return sources["tree"]
    return "https://api.crossref.org/works?" + urllib.parse.urlencode({"query": query, "rows": 4, "select": "DOI,title,abstract,URL,published"})


# ---------------------------------------------------------------------------
# STEP: research_urls
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.
# ---------------------------------------------------------------------------

def research_urls(query, domain, attempts=0, topic=None, *, targeted=False):
    """Return bounded scholarly routes.

    Targeted project maturation favors article indexes. DataCite remains in the
    broader exploration pool where repository/data-object discovery is useful,
    but it should not consume scarce depth slots for an already-defined paper
    question.
    """
    if topic and topic.get("source_kind") == "repository":
        primary = query_url(query, domain, topic)
        # A WAKE✳︎ follow-up gets two distinct repository views when the fixed
        # collector budget permits it. The first follows the query; the second
        # rotates across implementation/config/workflow/UI files so self-study
        # is not trapped in README/docs or a single favored module.
        repo_routes = list(dict.fromkeys(repository_sources(topic["repository"]).values()))
        alternate = repo_routes[attempts % len(repo_routes)]
        if alternate == primary:
            alternate = repo_routes[(attempts + 1) % len(repo_routes)]
        return [primary, alternate]
    crossref = query_url(query, domain, topic)
    openalex = "https://api.openalex.org/works?" + urllib.parse.urlencode({
        "search": query, "per-page": 4,
        "select": "id,doi,title,publication_year,type,cited_by_count,open_access,primary_location,abstract_inverted_index",
    })
    semantic_scholar = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode({
        "query": query, "limit": 4,
        "fields": "paperId,title,year,abstract,url,externalIds,openAccessPdf",
    })
    datacite = "https://api.datacite.org/dois?" + urllib.parse.urlencode({
        "query": query, "page[size]": 4,
    })
    # Rotate across independent indexes instead of treating Crossref/OpenAlex
    # as the whole scholarly world. Search responses remain discovery leads;
    # exact records or approved publisher/full-text pages are required for
    # qualifying evidence.
    indexes = (
        [crossref, openalex, semantic_scholar]
        if targeted
        else [crossref, openalex, semantic_scholar, datacite]
    )
    start = attempts % len(indexes)
    return indexes[start:] + indexes[:start]


def evidence_role(url):
    """Classify collection depth without mistaking bibliographic metadata for research.

    Broad index queries are discovery. Exact index records are metadata: useful
    for identifiers, abstracts, and routing, but insufficient by themselves for
    notebook maturation. Only readable publisher/full-text/source-controlled
    material is a qualifying source.
    """
    parsed = urllib.parse.urlsplit(url)
    query = urllib.parse.parse_qs(parsed.query)
    if parsed.hostname == "api.crossref.org" and parsed.path == "/works" and "query" in query:
        return "discovery"
    if parsed.hostname == "api.openalex.org" and parsed.path == "/works" and "search" in query:
        return "discovery"
    if parsed.hostname == "api.semanticscholar.org" and parsed.path.endswith("/paper/search") and "query" in query:
        return "discovery"
    if parsed.hostname == "api.datacite.org" and parsed.path == "/dois" and "query" in query:
        return "discovery"
    if parsed.hostname == "export.arxiv.org" and parsed.path.startswith("/api/"):
        return "metadata"
    if parsed.hostname in {"api.crossref.org", "api.openalex.org",
                           "api.semanticscholar.org", "api.datacite.org"}:
        return "metadata"
    return "source"


def host_tier(url, discovery_only=False):
    """Describe what kind of approved source was retrieved.

    The tier is provenance metadata, not a truth score. Governance still uses
    evidence_role plus project relevance and publication gates.
    """
    if discovery_only:
        return "discovery"
    host = urllib.parse.urlsplit(url).hostname
    if host in {"arxiv.org", "rss.arxiv.org", "osf.io",
                "psyarxiv.com", "www.psyarxiv.com"}:
        return "preprint"
    if host in {"export.arxiv.org", "api.crossref.org", "api.openalex.org", "api.semanticscholar.org",
                "api.datacite.org", "pubmed.ncbi.nlm.nih.gov", "europepmc.org",
                "api.core.ac.uk", "doaj.org", "eric.ed.gov"}:
        return "verification-metadata"
    if host in {"pmc.ncbi.nlm.nih.gov", "www.ncbi.nlm.nih.gov",
                "frontiersin.org", "www.frontiersin.org", "journals.plos.org",
                "elifesciences.org", "quantum-journal.org"}:
        return "verification-fulltext"
    if host and (host.endswith(".biomedcentral.com") or host.endswith(".springeropen.com")):
        return "verification-publisher"
    if host in {"raw.githubusercontent.com", "api.github.com"}:
        return "source-controlled"
    return "verification-publisher"


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
    if topic.get("source_kind") == "repository":
        return research_urls(topic["query"], topic["id"], attempts, topic)
    query = urllib.parse.urlencode({"action": "query", "list": "search", "srsearch": topic["query"], "format": "json"})
    return ["https://en.wikipedia.org/w/api.php?" + query,
            research_urls(topic["query"], topic["id"], attempts, topic)[0]]


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

def collect(engine, fetcher=fetch_source, monotonic=time.monotonic):
    """Called under the wake lock before inference; at most two unauthenticated requests."""
    state = engine.store.load()
    if not state.get("charter"):
        return
    attempts = len(state["invocations"])
    topics = [topic for topic in state.get("research_topics", []) if topic.get("enabled", True)]
    topic_by_id = {topic["id"]: topic for topic in state.get("research_topics", [])}
    def awaiting_capability_retry(request):
        summary = state.get("acquisition", {}).get(request["project"], {})
        return (summary.get("capability_blocked")
                and state["version"] < summary.get("retry_after_version", state["version"] + 1))

    queued = [r for r in state.get("research", {}).values()
              if r["status"] == "queued" and not awaiting_capability_retry(r)]
    # Research mode spends the bounded network budget on maturation first.
    # When active work exists, reserve only one slot for broad exploration and
    # use the rest to advance queued retrievals, metadata leads, and readable
    # source candidates. With no active work, the whole budget remains available
    # for neutral topic discovery.
    budget = engine.config["research_collection_budget"] if engine.config.get("observation_mode") else 2
    wall_limit = int(engine.config.get("research_collection_wall_seconds", 45))
    collection_started = monotonic()
    discovery_count = min(budget, len(topics))
    rng = secrets.SystemRandom()
    active_projects = [p for p in state.get("projects", {}).values()
                       if p.get("status") == "active"]
    active_domains = {p["domain"] for p in active_projects}
    active_work = bool(active_projects or queued)
    active_project_ids = {p["id"] for p in active_projects}
    existing_sources = {
        e.get("source") for e in state.get("evidence", {}).values() if e.get("source")
    }
    maturation_backlog = bool(queued) or any(
        project_id in active_project_ids and (
            any(url and url not in existing_sources
                for url in summary.get("source_candidates", []))
            or any(
                (exact_identifier_url(identifier) not in existing_sources)
                for identifier in summary.get("persistent_identifiers", [])
                if exact_identifier_url(identifier)
            )
        )
        for project_id, summary in state.get("acquisition", {}).items()
    )
    # Once an active project has a concrete acquisition trail, finish that trail
    # before spending another slot on unrelated broad discovery. This keeps the
    # collector from repeatedly observing new topics while known projects stall
    # one routing hop short of readable evidence.
    exploration_slots = (
        0 if active_work and maturation_backlog
        else 1 if active_work and discovery_count > 1
        else discovery_count
    )
    maturation_slots = discovery_count - exploration_slots
    alternatives = [topic for topic in topics if topic["id"] not in active_domains]
    pending = []
    used_urls = set()
    used_queue_ids = set()

    # Discovery receipts already contain durable DOI/OpenAlex/arXiv leads. Spend
    # one continuation slot promoting the strongest untried lead to an exact
    # verification record before asking a disposable model to rediscover or
    # manually translate it. This is retrieval plumbing, not research judgment.
    projects = state.get("projects", {})
    source_candidates = []
    for project_id, summary in state.get("acquisition", {}).items():
        project = projects.get(project_id, {})
        if project.get("status") != "active":
            continue
        candidate_identities = summary.get("source_candidate_identities", {})
        for url in summary.get("source_candidates", []):
            if url and url not in existing_sources:
                source_candidates.append({
                    "id": summary.get("last_receipt", {}).get("research_id") or f"collector-{project_id}",
                    "project": project_id, "url": url,
                    "domain": project.get("domain") or summary.get("domain"),
                    "queued_followup": False, "acquisition_followup": True,
                    "source_candidate": True,
                    "source_identity": candidate_identities.get(url),
                    "blocked": bool(summary.get("capability_blocked")),
                    "no_progress": int(summary.get("no_progress", 0)),
                })
    source_candidates.sort(key=lambda item: (
        0 if not item["blocked"] else 1, -item["no_progress"], item["project"], item["url"]
    ))
    for item in source_candidates:
        if len(pending) >= maturation_slots:
            break
        pending.append(item)
        used_urls.add(item["url"])

    identifier_candidates = []
    for project_id, summary in state.get("acquisition", {}).items():
        project = projects.get(project_id, {})
        if project.get("status") != "active":
            continue
        # persistent_identifiers() records DOI leads before provider-local IDs.
        # Prefer those canonical identifiers first: Crossref exact DOI records are
        # broadly interoperable, while OpenAlex IDs remain a deterministic fallback.
        for identifier in summary.get("persistent_identifiers", []):
            url = exact_identifier_url(identifier)
            if url and url not in existing_sources:
                identifier_candidates.append({
                    "id": summary.get("last_receipt", {}).get("research_id") or f"collector-{project_id}",
                    "project": project_id,
                    "url": url,
                    "domain": project.get("domain") or summary.get("domain"),
                    "queued_followup": False,
                    "acquisition_followup": True,
                    "identifier": identifier,
                    "blocked": bool(summary.get("capability_blocked")),
                    "no_progress": int(summary.get("no_progress", 0)),
                })
                break
    identifier_candidates.sort(key=lambda item: (
        0 if not item["blocked"] else 1, -item["no_progress"], item["project"], item["identifier"]
    ))
    for exact in identifier_candidates:
        if len(pending) >= maturation_slots:
            break
        if exact["url"] in used_urls:
            continue
        pending.append(exact)
        used_urls.add(exact["url"])

    # Service durable project follow-ups deterministically before broad discovery.
    for followup in sorted(queued, key=lambda item: (item["project"], item["id"])):
        if len(pending) >= maturation_slots:
            break
        routes = research_urls(
            followup["query"], followup["domain"], attempts,
            topic_by_id.get(followup["domain"]), targeted=True
        )
        url = followup.get("url") or routes[0]
        if url in used_urls:
            continue
        pending.append({"id": followup["id"], "project": followup["project"],
                        "url": url, "domain": followup["domain"],
                        "queued_followup": True})
        used_urls.add(url)
        used_queue_ids.add(followup["id"])

    # If a project has no explicit follow-up yet, use its own durable question
    # to spend remaining maturation slots on targeted scholarly discovery rather
    # than random unrelated topics.
    for project in sorted(active_projects, key=lambda item: item["id"]):
        if len(pending) >= maturation_slots:
            break
        query = project.get("question") or project.get("title") or project.get("next_step")
        routes = research_urls(
            query, project["domain"], attempts + len(pending),
            topic_by_id.get(project["domain"]), targeted=True
        )
        for url in routes:
            if len(pending) >= maturation_slots:
                break
            if url in used_urls:
                continue
            pending.append({
                "id": f"collector-{project['id']}-{attempts}-{len(pending)}",
                "project": project["id"], "url": url, "domain": project["domain"],
                "queued_followup": False, "acquisition_followup": True,
                "targeted_discovery": True,
            })
            used_urls.add(url)

    remaining_slots = min(exploration_slots, discovery_count - len(pending))
    if remaining_slots:
        pool = [topic for topic in alternatives
                if not pending or topic["id"] != pending[0]["domain"]]
        if len(pool) < remaining_slots:
            pool = [topic for topic in topics
                    if not pending or topic["id"] != pending[0]["domain"]]
        selected = rng.sample(pool, min(remaining_slots, len(pool)))
        # Keep discovery-only web idea-pool receipts ahead of repository-analysis
        # routes in a shared bounded pass. The capability flag, not a topic ID,
        # defines repository analysis.
        selected.sort(key=lambda topic: topic.get("source_kind") == "repository")
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
        if monotonic() - collection_started >= wall_limit:
            break
        url = item.get("url") or query_url(item["query"], item["domain"])
        try:
            topic = topic_by_id.get(item["domain"], {})
            (allowed_discovery_url(url) if item.get("discovery_only") else allowed_url(url, topic.get("repository", "sudofx/wake")))
            observation = (fetch_source(url, discovery_only=True) if fetcher is fetch_source and item.get("discovery_only")
                           else fetcher(url))
            # Trusted collector metadata activates forward-only verification and
            # binds evidence to the neutral topic that caused the retrieval.
            source_identity = (
                item.get("source_identity")
                or item.get("identifier")
                or route_source_identity(url)
            )
            observation_role = (
                "discovery" if item.get("discovery_only") else evidence_role(url)
            )
            # Only routing layers may automatically expand the acquisition
            # graph. A substantive article's bibliography/links are not
            # automatically relevant to the project's question.
            routing_layer = observation_role in ("discovery", "metadata")
            persistent_leads = persistent_identifiers(observation) if routing_layer else []
            source_candidates_for_observation = (
                candidate_source_urls(observation, current_url=url)
                if routing_layer else []
            )
            observation = {
                **observation,
                "verification_required": True,
                "topic_domain": item["domain"],
                "evidence_role": observation_role,
                "host_tier": host_tier(url, item.get("discovery_only", False)),
                "source_identity": source_identity,
                "persistent_identifiers": persistent_leads,
                "source_candidates": source_candidates_for_observation,
                "source_candidate_identities": {
                    candidate: source_identity
                    for candidate in source_candidates_for_observation
                    if source_identity
                },
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
        if item.get("queued_followup") or item.get("acquisition_followup"):
            payload = json.loads(content)
            role = payload.get("evidence_role", evidence_role(url))
            tier = payload.get("host_tier", host_tier(url))
            # Acquisition progress means the project gained substantive readable
            # material. Exact index records are useful verification metadata and
            # identifier bridges, but they must not make a project look researched.
            substantive = role == "source" and tier != "verification-metadata"
            routing_progress = bool(
                status == "collected"
                and (payload.get("persistent_identifiers") or payload.get("source_candidates"))
            )
            outcome = (
                "progress" if substantive
                else "routing_progress" if routing_progress
                else "route_failure" if status == "failed"
                else "no_progress"
            )
            engine.store.append("acquisition_assessed", {"project": item["project"],
                "domain": item["domain"], "research_id": item["id"],
                "route": urllib.parse.urlsplit(url).hostname + ":" + role,
                "stage": "substantive_source" if role == "source" else "discovery",
                "outcome": outcome, "evidence": evidence_id,
                "persistent_identifiers": payload.get("persistent_identifiers", []),
                "source_candidates": payload.get("source_candidates", []),
                "source_candidate_identities": payload.get("source_candidate_identities", {})})
