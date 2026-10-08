# =============================================================================
# REPORT — the human projection layer. Static HTML/JSON views are derived from canonical durable state. Rendering may explain or hide information, but it must never silently create experimental facts.
# =============================================================================

"""Verified record-to-website export, including installation-specific transport.

Use export rather than copying templates into a running site: deployment identity,
local operator links, data projections and Console components form one artifact.
The hosted Pages caller supplies a public projection; standalone callers supply
their own store. Neither export path transfers authority between installations.
"""

from contextlib import nullcontext
from datetime import datetime
import html
import json
import os
import re
from pathlib import Path
from zoneinfo import ZoneInfo

from .event_format import canonical, now
from .scheduling import wake_status


def atomic_write(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".html" and "</body>" in content and "<script>/* Every off-site destination opens separately;" not in content:
        external = (Path(__file__).parent / "assets" / "external-links.js").read_text()
        content = content.replace("</body>", "<script>" + external + "</script></body>", 1)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8") as stream:
        stream.write(content)
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)



def _export_console_components(target):
    """Reuse canonical renderers inside Console without retired HTML dependencies."""
    assets = Path(__file__).parent / "assets"
    for name in ("console-tools.js", "console-component.js", "console-component.css", "console-light.css"):
        atomic_write(target / name, (assets / name).read_text())
    pages = {"index.html": "console-records.html", "map.html": "console-map.html",
             "map3d.html": "console-map3d.html", "events.html": "console-events.html",
             "state.html": "console-state.html", "rejected.html": "console-rejected.html"}
    for source, destination in pages.items():
        content = (target / source).read_text()
        for script in ("map.js", "map3d.js", "nav.js", "flat-view.js"):
            content = content.replace(f'<script src="{script}"></script>', "<script>" + (assets / script).read_text() + "</script>")
        for old, new in pages.items():
            content = content.replace(old, new)
        if source in ("events.html", "state.html", "rejected.html"):
            snapshot = json.loads((target / "wake-data.json").read_text())
            stamp = html.escape(str(snapshot.get("generated", "unknown")))
            record_head = html.escape(str(snapshot.get("head", "unknown")))
            version = snapshot.get("state", {}).get("version", "unknown")
            content = content.replace("<main>", f'<main><p class="console-component-stamp">Published snapshot · state {version} · {stamp}<br>Head {record_head}</p>', 1)
        content = content.replace("<head>", '<head><meta name="darkreader-lock">', 1)
        content = content.replace("</head>", '<link rel="stylesheet" href="console-component.css"><link rel="stylesheet" href="console-light.css"></head>', 1)
        content = content.replace("</body>", '<script src="console-component.js"></script></body>', 1)
        atomic_write(target / destination, content)


def _pretty(value):
    return json.dumps(value, indent=2, ensure_ascii=False, sort_keys=False)



def _display_text(value):
    """Presentation-only WAKE wordmark normalization; canonical state stays untouched."""
    text = str(value).replace("WAKE✳️", "WAKE✳").replace("WAKE✳︎", "WAKE✳")
    return text.replace("WAKE✳", "WAKE\u2733\uFE0E")



def _html_text(value):
    escaped = html.escape(_display_text(value))
    return escaped.replace("WAKE✳︎", '<strong class="wake-mark">WAKE✳︎</strong>')



def _reading_time(value):
    """Format record chronology consistently across generated reading pages."""
    if not value:
        return ""
    try:
        stamp = datetime.fromisoformat(str(value)).astimezone(ZoneInfo("America/Los_Angeles"))
        return stamp.strftime("%b %d, %Y · %I:%M %p %Z").replace(" 0", " ").replace("· 0", "· ")
    except (ValueError, TypeError):
        return str(value)


def _topic_meta(state, domain, page="projects"):
    if not domain:
        return ""
    label = next((item.get("label") for item in state.get("research_topics", []) if item.get("id") == domain), None) or str(domain).replace("_", " ")
    color = state.get("topic_colors", {}).get(domain, "var(--cyan)")
    return (f'<a class="topic-tag" href="../index.html#{html.escape(page)}/topic:{html.escape(str(domain))}" '
            f'style="--topic-color:{html.escape(str(color))}">{html.escape(str(label).lower())}</a>')


def _reading_meta(type_label, status_label="", topic_html="", timestamp="", status_class=""):
    status = ""
    if status_label:
        css = re.sub(r"[^a-z0-9_-]+", "-", str(status_class or status_label).lower()).strip("-")
        status = f'<span class="record-status"><span class="badge {html.escape(css)}">{html.escape(str(status_label))}</span></span>'
    topics = f'<span class="record-topics">{topic_html}</span>' if topic_html else '<span class="record-topics"></span>'
    time = f'<time>{html.escape(_reading_time(timestamp))}</time>' if timestamp else ""
    return f'<div class="record-panel-meta reading-meta"><span class="record-type">{html.escape(str(type_label))}</span>{status}{topics}{time}</div>'


def _reading_page(title, eyebrow, body, record_href, back_href="../index.html", meta_html=""):
    """Standalone browser reading page backed by the live record projection."""
    favicon = "data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 64 64%27%3E%3Crect width=%2764%27 height=%2764%27 rx=%2712%27 fill=%27%23f7f3ea%27/%3E%3Cpath d=%27M32 9v46M9 32h46M15.7 15.7l32.6 32.6M48.3 15.7L15.7 48.3%27 stroke=%27%23286d72%27 stroke-width=%276%27 stroke-linecap=%27round%27/%3E%3C/svg%3E"
    return f"""<!doctype html>
<html lang=\"en\" data-theme=\"dark\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">
<meta name=\"theme-color\" content=\"#000000\"><link rel=\"icon\" href=\"{favicon}\"><title>{html.escape(title)} · WAKE✳︎</title>

<link rel=\"stylesheet\" href=\"../nav.css?v=20261004-15\"><link rel=\"stylesheet\" href=\"../theme.css?v=20261004-15\">
<style>
:root{{--paper:#000000;--surface:#07152d;--surface-strong:#0b1c38;--ink:#edf3ff;--muted:#9aa9c6;--line:#395274;--green:#55db9a;--cyan:#22e2eb;--accent:#bb4cff;--hot:#7aa2f7;--pale:#0b1c38;--mono:ui-monospace,SFMono-Regular,Consolas,monospace;--sans:-apple-system,BlinkMacSystemFont,"SF Pro Text",Inter,"Segoe UI",Arial,sans-serif;--serif:var(--sans)}}
*{{box-sizing:border-box}}body{{margin:0;background:#000000;color:var(--ink);font:17px/1.72 var(--sans);font-variant-emoji:text;position:relative}}.site-backdrop{{position:fixed;inset:0;z-index:0;pointer-events:none;background-color:#000000;background-image:linear-gradient(rgba(0,0,0,.20),rgba(0,0,0,.20)),linear-gradient(rgba(3,7,22,.05),rgba(3,7,22,.05)),url("../backgrounds/nebula-desktop-1680x1050.webp?v=20261004-7");background-position:center top;background-size:cover;background-repeat:no-repeat}}@media (min-aspect-ratio:2/1){{.site-backdrop{{background-image:linear-gradient(rgba(0,0,0,.20),rgba(0,0,0,.20)),linear-gradient(rgba(3,7,22,.05),rgba(3,7,22,.05)),url("../backgrounds/nebula-ultrawide-3440x1440.webp?v=20261004-7")}}}}@media (min-width:701px) and (max-aspect-ratio:3/2){{.site-backdrop{{background-image:linear-gradient(rgba(0,0,0,.20),rgba(0,0,0,.20)),linear-gradient(rgba(3,7,22,.05),rgba(3,7,22,.05)),url("../backgrounds/nebula-ipad-landscape-2360x1640.webp?v=20261004-7");background-position:center center}}}}@media (max-width:700px){{.site-backdrop{{background-image:linear-gradient(rgba(0,0,0,.20),rgba(0,0,0,.20)),linear-gradient(rgba(3,7,22,.05),rgba(3,7,22,.05)),url("../backgrounds/nebula-iphone12mini-1080x2340.webp?v=20261004-7");background-position:center top}}}}
main{{position:relative;z-index:1;max-width:900px;margin:auto;padding:34px 22px 90px}}
.reading-panel{{background:rgba(4,15,34,.70);border:1px solid rgba(74,111,158,.64);border-radius:13px;padding:34px 38px 44px;box-shadow:inset 0 1px 0 rgba(255,255,255,.035),0 20px 60px rgba(0,0,18,.20);backdrop-filter:blur(22px) saturate(116%);-webkit-backdrop-filter:blur(22px) saturate(116%)}}
.reading-panel h1{{font:760 clamp(2.4rem,7vw,4.8rem)/1.02 var(--sans);letter-spacing:-.045em;margin:.18em 0 .3em;color:#f7f9ff}}
.reading-panel h2{{font:700 1.8rem/1.2 var(--sans);margin-top:2.2em;color:#f4f7ff}}
.reading-panel h3{{font:700 14px var(--sans);margin-top:2em;color:#f4f7ff}}
.reading-panel p,.reading-panel li{{color:#c9d1e6}}
.reading-panel a{{color:var(--cyan);text-decoration:none}}.wake-mark{{font-weight:900}}@media(hover:hover) and (pointer:fine){{.reading-panel a:hover{{color:#fff;text-decoration:none;text-shadow:0 0 9px rgba(34,226,235,.4)}}}}
.reading-links{{display:flex;gap:18px;flex-wrap:wrap;margin-top:17px;font:10px var(--mono)}}.eyebrow,.meta{{font:10px var(--mono);color:var(--muted);text-transform:uppercase;letter-spacing:.1em}}.eyebrow{{color:var(--cyan);margin-top:0}}.lede{{font-size:1.25rem;line-height:1.55;color:#e2e7f6!important}}.note{{border-left:3px solid var(--accent);padding:10px 0 10px 18px;margin:28px 0;background:rgba(11,28,56,.46);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}}.sources{{font-family:var(--sans);font-size:.95rem}}code{{font-family:var(--mono)}}hr{{border:0;border-top:1px solid var(--line);margin:34px 0}}small{{color:var(--muted)}}
@media(max-width:680px){{main{{padding:18px 6px 60px}}.reading-panel{{padding:22px 18px 30px;border-radius:10px}}.reading-panel h1{{font-size:2.65rem}}}}
</style></head><body><div class=\"site-backdrop\" aria-hidden=\"true\"></div>
<header class=\"masthead\">
  <div class=\"brand-lockup\"><a class=\"wordmark\" href=\"../index.html\">WAKE<span class=\"asterisk\">✳︎</span></a></div>
  <nav class=\"compact-nav\" aria-label=\"Main navigation\"><a href=\"../index.html#discoveries\">Research</a><a href=\"../index.html#journal\">Journal</a><a href=\"../index.html#blog\">Bob’s Blog</a><!-- Read menu temporarily retired. <details class=\"nav-group\"><summary>Read</summary><div class=\"nav-dropdown\"><a href=\"../index.html#journal\">Journal</a><a href=\"../console.html?tool=projects\">Projects</a><a href=\"../index.html#blog\">Bob’s Blog</a></div></details> --></nav>
  <div class=\"header-tools\"><a class=\"repo-link\" href=\"https://github.com/sudofx/wake\" aria-label=\"Open WAKE repository\" title=\"WAKE repository\"><svg viewBox=\"0 0 24 24\" aria-hidden=\"true\"><path fill=\"currentColor\" d=\"M12 .7a11.3 11.3 0 0 0-3.57 22c.57.1.77-.25.77-.55v-2.17c-3.14.68-3.8-1.33-3.8-1.33-.51-1.3-1.25-1.65-1.25-1.65-1.03-.7.08-.69.08-.69 1.13.08 1.73 1.16 1.73 1.16 1.01 1.73 2.65 1.23 3.3.94.1-.73.39-1.23.72-1.51-2.51-.29-5.15-1.26-5.15-5.59 0-1.24.44-2.25 1.16-3.04-.12-.29-.5-1.44.11-3 0 0 .95-.3 3.11 1.16a10.8 10.8 0 0 1 5.66 0C17.03 5 17.98 5.3 17.98 5.3c.61 1.56.23 2.71.11 3 .72.79 1.16 1.8 1.16 3.04 0 4.34-2.65 5.3-5.17 5.58.41.35.77 1.04.77 2.1v3.13c0 .3.2.66.78.55A11.3 11.3 0 0 0 12 .7Z\"/></svg></a><a class=\"console-link\" href=\"../console.html\" aria-label=\"Open WAKE Console\" title=\"Console\"><svg viewBox=\"0 0 24 24\" aria-hidden=\"true\"><path d=\"M4.2 16.8a8.8 8.8 0 1 1 15.6 0\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/><path d=\"M6.8 14.3l-1.7-.8M8.2 9.8 7 8.5M12 8V6.2M15.8 9.8 17 8.5M17.2 14.3l1.7-.8\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\"/><path d=\"M12 16l3.8-4.4\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\" stroke-linecap=\"round\"/><circle cx=\"12\" cy=\"16\" r=\"1.35\" fill=\"currentColor\"/></svg></a><a class=\"actions-light\" href=\"https://github.com/sudofx/wake/actions\" aria-label=\"Open WAKE GitHub Actions\" title=\"Checking…\"><span class=\"actions-light-track\" aria-hidden=\"true\"><i></i></span><span class=\"actions-light-label\">Checking…</span></a></div>
</header>
<main><article class=\"reading-panel\"><div class=\"eyebrow\">{html.escape(eyebrow)}</div>{meta_html}<h1>{html.escape(title)}</h1><nav class=\"reading-links\"><a href=\"{html.escape(back_href)}\">WAKE site</a><a href=\"../map.html\">MAP</a><a href=\"{html.escape(record_href)}\">Open in WAKE</a></nav>{body}</article></main><script src=\"../nav.js\"></script></body></html>"""


def _notebook_evidence_profile(notebook, state):
    """Derive visible evidence-depth telemetry without mutating durable state.

    Public reporting must use the same substantive-evidence distinction as
    governance. Metadata/discovery records may remain in historical notebooks,
    but they are retrieval leads and must not be displayed as qualifying source
    works under the current contract.
    """
    source_roots = set()
    cross_topic_roots = set()
    nonqualifying = 0
    project_domain = notebook.get("domain") or state.get("projects", {}).get(
        notebook.get("project"), {}
    ).get("domain")
    for evidence_id in notebook.get("evidence", []):
        evidence = state.get("evidence", {}).get(evidence_id, {})
        source = evidence.get("source")
        try:
            payload = json.loads(evidence.get("content", ""))
        except (ValueError, TypeError):
            payload = {}
        if isinstance(payload, dict) and (
            payload.get("evidence_role") in ("discovery", "metadata")
            or payload.get("host_tier") == "verification-metadata"
        ):
            nonqualifying += 1
            continue
        explicit_identity = (
            str(payload.get("source_identity") or "").strip().lower()
            if isinstance(payload, dict) else ""
        )
        # IDs found inside source text are retrieval leads, not the identity of
        # the retrieved work. Only the collector-stamped route identity may
        # collapse mirrors; legacy records fall back conservatively to URL.
        root = explicit_identity or "url:" + str(source or "").strip().lower()
        if source:
            source_roots.add(root)
        topic = payload.get("topic_domain") if isinstance(payload, dict) else None
        if source and topic and project_domain and topic != project_domain:
            cross_topic_roots.add(root)
    return len(source_roots), len(cross_topic_roots), nonqualifying


def _notebook_html(notebook, state):
    source_items = []
    for eid in notebook["evidence"]:
        evidence = state["evidence"][eid]
        source_items.append(f'<li><a href="{html.escape(str(evidence["source"]))}">{html.escape(eid)}</a></li>')
    source_count, cross_topic_count, nonqualifying_count = _notebook_evidence_profile(notebook, state)
    source_word = "work" if source_count == 1 else "works"
    cross_note = (
        f" · {cross_topic_count} cross-topic source work"
        + ("" if cross_topic_count == 1 else "s")
        if cross_topic_count else ""
    )
    nonqualifying_note = (
        f" · {nonqualifying_count} metadata/discovery record"
        + ("" if nonqualifying_count == 1 else "s")
        + " not counted"
        if nonqualifying_count else ""
    )
    body = (
        f'<p class="lede">{_html_text(notebook["summary"])}</p>'
        f'<p class="meta">Evidence profile · {source_count} distinct qualifying source {source_word}{cross_note}{nonqualifying_note}</p>'
        f'<h2>Findings</h2><p>{_html_text(notebook["findings"])}</p>'
        f'<h2>Limitations and competing views</h2><p>{_html_text(notebook["limitations"])}</p>'
        f'<h2>Next questions</h2><p>{_html_text(notebook["next_questions"])}</p>'
        f'<h2>Collected sources</h2><ul class="sources">{"".join(source_items)}</ul>'
        f'<hr><p class="meta">Revision {notebook["revision"]} · AI-authored research synthesis; see source scopes in the journal.</p>'
    )
    domain = notebook.get("domain") or state.get("projects", {}).get(notebook.get("project"), {}).get("domain")
    iid = notebook.get("updated_by") or notebook.get("created_by")
    invocation = state.get("invocations", {}).get(iid, {})
    meta = _reading_meta("NOTEBOOK", f"REVISION {notebook['revision']}", _topic_meta(state, domain), invocation.get("time"), "revision")
    return _reading_page(notebook["title"], "WAKE✳︎ / RESEARCH NOTEBOOK", body, "../index.html#projects/notebook:" + notebook["id"], meta_html=meta)



def _blog_display_title(post):
    """Keep scheduled Bob reflections recognisable in every public export."""
    title = str(post.get("title", "")).strip()
    version = int(post.get("created_version") or 0)
    reflection_cycle = int(post.get("reflection_cycle") or 0)
    milestone = reflection_cycle or (version if version and version % 10 == 0 else 0)
    if not milestone:
        return title
    remainder = re.sub(
        r"^\s*(?:cycle\s*\d+\s*[:—–-]?\s*)?(?:reflection\s*[:—–-]?\s*)?",
        "", title, flags=re.IGNORECASE,
    )
    remainder = re.sub(r"\b(?:first|inaugural)\s+reflection\b", "Reflection", remainder, flags=re.IGNORECASE).strip()
    return f"Cycle {milestone} Reflection: {remainder or title}"


INLINE_BLOG_SOURCE_LINKS_FROM_VERSION = 203


def _blog_html_text(value, post, state):
    """Render future inline [source-id] citations as links without rewriting older posts."""
    rendered = _html_text(value)
    if int(post.get("created_version") or 0) < INLINE_BLOG_SOURCE_LINKS_FROM_VERSION:
        return rendered
    allowed = set(post.get("evidence", []))
    for evidence_id in sorted(allowed, key=len, reverse=True):
        evidence = state.get("evidence", {}).get(evidence_id, {})
        source = str(evidence.get("source") or "").strip()
        if not source:
            continue
        token = html.escape(f"[{evidence_id}]")
        link = f'<a class="inline-source-citation" href="{html.escape(source)}">{token}</a>'
        rendered = rendered.replace(token, link)
    return rendered


def _blog_html(post, state):
    paragraphs = "".join(f"<p>{_blog_html_text(part, post, state)}</p>" for part in str(post["body"]).split("\n\n") if part.strip())
    lens = f'<div class="note"><div class="eyebrow">BOB’S LENS / PHILOSOPHICAL REFLECTION</div><p>{_html_text(post["lens"])}</p></div>' if post.get("lens") else ""
    notebooks = "".join(
        f'<li><a href="../notebooks/{html.escape(nid)}.html">{html.escape(state["notebooks"][nid]["title"])}</a></li>'
        for nid in post["notebooks"])
    sources = "".join(
        f'<li><a href="{html.escape(str(state["evidence"][eid]["source"]))}">{html.escape(eid)}</a></li>'
        for eid in post["evidence"])
    correction = ""
    if post.get("superseded_by"):
        correction = f'<p class="note">Superseded by <a href="{html.escape(post["superseded_by"])}.html">{html.escape(post["superseded_by"])}</a>.</p>'
    research_receipts = ""
    if notebooks or sources:
        research_receipts = (
            '<h2>Follow the receipts</h2>'
            + (f'<h3>Research notebooks</h3><ul class="sources">{notebooks}</ul>' if notebooks else "")
            + (f'<h3>Collected sources</h3><ul class="sources">{sources}</ul>' if sources else "")
        )
    elif post.get("reflection_cycle"):
        research_receipts = '<p class="meta">System-wide reflection · no project-specific research receipts attached.</p>'
    body = (
        f'<p class="lede">{_blog_html_text(post["lede"], post, state)}</p>{correction}{paragraphs}{lens}'
        f'{research_receipts}'
        f'<p><a href="../index.html#history/{html.escape(post["created_by"])}">Exact wake and decision →</a></p>'
        '<hr><p class="meta">AI-authored from WAKE✳︎’s durable research record. Research claims link to evidence; philosophical reflections are reflections.</p>'
    )
    version = int(post.get("created_version") or 0)
    reflection_cycle = int(post.get("reflection_cycle") or 0)
    is_reflection = bool(reflection_cycle or (version and version % 10 == 0))
    domain = state.get("projects", {}).get(post.get("project"), {}).get("domain")
    invocation = state.get("invocations", {}).get(post.get("created_by"), {})
    status = str(post.get("status") or "published").upper()
    meta = _reading_meta("REFLECTION" if is_reflection else "BLOG", status, _topic_meta(state, domain, "blog"), invocation.get("time"), post.get("status") or "published")
    return _reading_page(_blog_display_title(post), "BOB / WAKE✳︎ BLOG", body, "../index.html#blog/" + post["id"], meta_html=meta)




def _browser_route_shell(route, prefix="../"):
    """Tiny compatibility page: preserve old URLs while rendering from current browser data."""
    target = prefix + "index.html" + route
    safe = json.dumps(target)
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="robots" content="noindex">'
        '<title>WAKE✳︎</title></head><body data-wake-route-shell>'
        '<p>Opening the current WAKE✳︎ record…</p>'
        f'<script>location.replace({safe});</script>'
        f'<noscript><a href="{html.escape(target)}">Open the current WAKE✳︎ record</a></noscript>'
        '</body></html>'
    )


def _write_browser_route_shell(path, route, prefix="../"):
    """Write a route shell once; later publications reuse it unchanged."""
    path = Path(path)
    if path.exists():
        try:
            if "data-wake-route-shell" in path.read_text(encoding="utf-8"):
                return
        except (OSError, UnicodeDecodeError):
            pass
    atomic_write(path, _browser_route_shell(route, prefix=prefix))


def _flat_browser_shell(title, eyebrow, heading, description, kind, source):
    """Stable standalone shell whose facts are fetched from flat exports in-browser."""
    return f'''<!doctype html>
<html lang="en" data-theme="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} / WAKE✳︎</title>

<link rel="stylesheet" href="style.css"><link rel="stylesheet" href="nav.css?v=20261004-15"><link rel="stylesheet" href="theme.css?v=20261004-15"></head>
<body data-flat-kind="{html.escape(kind)}" data-flat-source="{html.escape(source)}">
<header class="masthead"><div class="brand-lockup"><a class="wordmark" href="index.html">WAKE<span class="asterisk">✳︎</span></a></div>
<nav class="compact-nav" aria-label="Main navigation"><a href="index.html#discoveries">Research</a><a href="index.html#journal">Journal</a><a href="index.html#blog">Bob’s Blog</a><!-- Read menu temporarily retired. <details class="nav-group"><summary>Read</summary><div class="nav-dropdown"><a href="index.html#journal">Journal</a><a href="console.html?tool=projects">Projects</a><a href="index.html#blog">Bob’s Blog</a></div></details> --></nav><div class="header-tools"><a class="repo-link" href="https://github.com/sudofx/wake" aria-label="Open WAKE repository" title="WAKE repository"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 .7a11.3 11.3 0 0 0-3.57 22c.57.1.77-.25.77-.55v-2.17c-3.14.68-3.8-1.33-3.8-1.33-.51-1.3-1.25-1.65-1.25-1.65-1.03-.7.08-.69.08-.69 1.13.08 1.73 1.16 1.73 1.16 1.01 1.73 2.65 1.23 3.3.94.1-.73.39-1.23.72-1.51-2.51-.29-5.15-1.26-5.15-5.59 0-1.24.44-2.25 1.16-3.04-.12-.29-.5-1.44.11-3 0 0 .95-.3 3.11 1.16a10.8 10.8 0 0 1 5.66 0C17.03 5 17.98 5.3 17.98 5.3c.61 1.56.23 2.71.11 3 .72.79 1.16 1.8 1.16 3.04 0 4.34-2.65 5.3-5.17 5.58.41.35.77 1.04.77 2.1v3.13c0 .3.2.66.78.55A11.3 11.3 0 0 0 12 .7Z"/></svg></a><a class="console-link" href="console.html" aria-label="Open WAKE Console" title="Console"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.2 16.8a8.8 8.8 0 1 1 15.6 0" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M6.8 14.3l-1.7-.8M8.2 9.8 7 8.5M12 8V6.2M15.8 9.8 17 8.5M17.2 14.3l1.7-.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M12 16l3.8-4.4" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><circle cx="12" cy="16" r="1.35" fill="currentColor"/></svg></a><a class="actions-light" href="https://github.com/sudofx/wake/actions" aria-label="Open WAKE GitHub Actions" title="Checking…"><span class="actions-light-track" aria-hidden="true"><i></i></span><span class="actions-light-label">Checking…</span></a></div></header>
<main><div class="page-heading"><p class="eyebrow">{html.escape(eyebrow)}</p><h1>{html.escape(heading)}</h1><p>{html.escape(description)}</p></div><div id="flat-content"></div></main>
<script src="flat-view.js"></script><script src="nav.js"></script></body></html>'''


def export(store=None, destination="site", experiment=None, operation=None, browser_only=False,
           record_snapshot=None, projection=None, standalone=True):
    lock = store.lock() if store is not None else nullcontext()
    with lock:
        # Pages may consume the disposable wake-live projection directly. It must
        # never reopen/replay the growing authoritative SQLite record merely to
        # render a browser shell.
        if projection is not None:
            state = projection["state"]
            head = projection["head"]
            events = projection.get("events", [])
            if experiment is None:
                experiment = projection.get("experiment")
            if operation is None:
                operation = projection.get("operation")
            data = {"state": state, "events": events, "head": head,
                    "generated": projection.get("generated") or now(),
                    "experiment": experiment,
                    "timezone": projection.get("timezone") or "America/Los_Angeles",
                    "operation": operation,
                    "wake_status": projection.get("wake_status") or (operation or {}).get("wake_status") or wake_status(state),
                    "metrics": projection.get("metrics", {})}
        else:
            # Full exports still consume one verified authoritative snapshot.
            state, head, events = record_snapshot if record_snapshot is not None else store.replay_record()
            if experiment is None:
                evidence_file = store.directory / "experiment.json"
                experiment = json.loads(evidence_file.read_text()) if evidence_file.exists() else None
            from .live import _full_history_metrics
            data = {"state": state, "events": events, "head": head, "generated": now(),
                    "experiment": experiment, "timezone": "America/Los_Angeles", "operation": operation,
                    "wake_status": (operation or {}).get("wake_status") or wake_status(state),
                    "metrics": _full_history_metrics(store, state)}
        target = Path(destination)
        target.mkdir(parents=True, exist_ok=True)
        assets = Path(__file__).parent / "assets"
        # Browser and installed-app icons are shared presentation assets.
        atomic_write(target / "manifest.webmanifest", (assets / "manifest.webmanifest").read_text())
        icon_target = target / "icons"
        icon_target.mkdir(parents=True, exist_ok=True)
        for icon in (assets / "icons").iterdir():
            if icon.is_file():
                (icon_target / icon.name).write_bytes(icon.read_bytes())
        from .research_projection import build_research_projection
        research = (projection or {}).get("research") or build_research_projection(
            state, events, head, generated=data["generated"], metrics=data["metrics"],
            operation=operation, source=(projection or {}).get("source") or ({
                "authority": "wake SQLite" if hasattr(store, "record") else "legacy WAKE SQLite",
                "database": store.path.name,
                "branch": None,
                "installation": "standalone" if standalone else "export",
                "head": head,
            } if store is not None else {}),
            matrix_reported=projection is None and hasattr(store, "continuity_matrix_progress"),
            matrix_progress=store.continuity_matrix_progress() if projection is None and hasattr(store, "continuity_matrix_progress") else None,
        )
        if research.get("head") != head or research.get("version") != state["version"]:
            raise ValueError("Research projection does not match the exported record")
        atomic_write(target / "research-data.json", json.dumps(research, ensure_ascii=False, separators=(",", ":")))
        for name in ("console.html", "research.css", "research.js", "research-scene.js", "research-instruments.js", "console-layout.js", "process-field.css", "process-field.js", "runtime-activity.js"):
            content = (assets / name).read_text()
            if name == "console.html":
                content = content.replace("WAKE_CYCLE_COUNT", str(state["version"]))
            atomic_write(target / name, content)
        template = (assets / "index.html").read_text().replace("WAKE_CYCLE_COUNT", str(state["version"]))
        # Publish source styles alongside every HTML view: Pages and exports share
        # the same theme file rather than receiving copied inline palettes.
        for name in ("style.css", "nav.css", "map.css", "map3d.css", "theme.css",
                     "nav.js", "map.js", "map3d.js", "flat-view.js"):
            atomic_write(target / name, (assets / name).read_text())
        # Static Nebula artwork is presentation-only. Publish the responsive
        # source set alongside the generated shell without routing binaries through text IO.
        background_source = assets / "backgrounds"
        background_target = target / "backgrounds"
        background_target.mkdir(parents=True, exist_ok=True)
        for name in (
            "nebula-ultrawide-3440x1440.webp",
            "nebula-desktop-1680x1050.webp",
            "nebula-ipad-landscape-2360x1640.webp",
            "nebula-iphone12mini-1080x2340.webp",
            "nebula-console-mockup.webp",
            "console-globe.png",
            "console-cube.png",
            "console-graph.png",
            "console-graph-alt.png",
        ):
            (background_target / name).write_bytes((background_source / name).read_bytes())
        browser_data = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
        atomic_write(target / "wake-data.json", browser_data)
        page = template.replace("/* WAKE_STYLE */", "").replace("/* NAV_STYLE */", "")
        page = page.replace("/* NAV_SCRIPT */", (assets / "nav.js").read_text())
        page = page.replace("/* WAKE_SCRIPT */", (assets / "app.js").read_text())
        page = page.replace("/* HELP_SCRIPT */", (assets / "help.js").read_text())
        page = page.replace("/* PET_SCRIPT */", (assets / "pet.js").read_text())
        # Browser UX is HTML-first. Do not publish duplicate Markdown projections.
        if browser_only:
            # Fast Pages projection: publish one application shell plus current flat
            # record exports. Historical presentation is rendered by the browser;
            # publication cost therefore no longer grows with every journal entry.
            atomic_write(target / "index.html", page)
            atomic_write(target / "state.json", json.dumps(state, indent=2, ensure_ascii=False))
            atomic_write(target / "events.jsonl", "".join(canonical(event) + "\n" for event in events))
            for name in ("nav.js", "map.js", "map3d.js", "flat-view.js"):
                atomic_write(target / name, (assets / name).read_text())

            # The map shells already fetch their data at browser load. Keep the
            # URLs stable while moving record projection out of GitHub Actions.
            from .provenance import build_map, build_map3d_projection, map3d_shard_filename
            graph = build_map(state, events, head, replay_history=projection is None)
            graph_json = json.dumps(graph, ensure_ascii=False)
            atomic_write(target / "map-data.json", graph_json)
            map_page = (assets / "map.html").read_text().replace("WAKE_CYCLE_COUNT", str(state["version"]))
            atomic_write(target / "map.html", map_page)
            graph3d_shell, graph3d_shards = build_map3d_projection(graph)
            atomic_write(target / "map3d-data.json", json.dumps(graph3d_shell, ensure_ascii=False))
            shard_dir = target / "map3d"
            shard_dir.mkdir(parents=True, exist_ok=True)
            for parent, shard in graph3d_shards.items():
                atomic_write(shard_dir / map3d_shard_filename(parent), json.dumps(shard, ensure_ascii=False))
            map3d_page = (assets / "map3d.html").read_text().replace("WAKE_CYCLE_COUNT", str(state["version"]))
            atomic_write(target / "map3d.html", map3d_page)

            # Preserve long-standing readable URLs as stable browser shells.
            # Their content comes from the current flat exports at page load.
            atomic_write(target / "state.html", _flat_browser_shell(
                "State", "THE CURRENT DURABLE STATE", "Current state.",
                "Loaded from state.json when this page opens.", "state", "state.json"))
            atomic_write(target / "events.html", _flat_browser_shell(
                "History", "THE APPEND-ONLY RECORD", "Exact history.",
                "Loaded from events.jsonl when this page opens.", "events", "events.jsonl"))
            atomic_write(target / "rejected.html", _flat_browser_shell(
                "Rejected & withheld drafts", "GOVERNANCE / STOPPED PROPOSALS",
                "Rejected & withheld drafts.", "Loaded from the current published record when this page opens.",
                "rejected", "wake-data.json"))

            # Old standalone artifact URLs remain useful bookmarks. Route missing
            # historical presentation files back into the live browser projection.
            atomic_write(target / "404.html", """<!doctype html><meta charset="utf-8"><script>(()=>{const p=location.pathname;let h='home';let m;if((m=p.match(/\\/blog\\/([^/]+)\\.(?:html|md)$/)))h='blog/'+decodeURIComponent(m[1]);else if((m=p.match(/\\/journal\\/([^/]+)\\.html$/)))h='history/'+decodeURIComponent(m[1]);else if((m=p.match(/\\/notebooks\\/([^/]+)\\.(?:html|md)$/)))h='projects/notebook:'+decodeURIComponent(m[1]);location.replace(new URL('index.html#'+h,location.href))})()</script>""")
            _export_console_components(target)
            _deployment_site(target, standalone=standalone)
            return {"path": str((target / "index.html").resolve()), "cycles": state["version"], "head": head}
        from .feeds import build_feeds
        for filename, content in build_feeds(state).items():
            atomic_write(target / filename, content)
        accepted_by_invocation = {event.get("payload", {}).get("id"): event for event in events if event.get("kind") == "accepted"}
        for entry in state["journal"]:
            invocation = state["invocations"][entry["invocation"]]
            event = accepted_by_invocation.get(entry["invocation"], {})
            domains = []
            for action in event.get("payload", {}).get("proposal", {}).get("actions", []):
                domain = action.get("domain") or state.get("projects", {}).get(action.get("project"), {}).get("domain")
                if domain and domain not in domains:
                    domains.append(domain)
            topics = "".join(_topic_meta(state, domain, "journal") for domain in domains)
            status = "SIMULATED" if invocation.get("provider") == "fixture" else str(invocation.get("status") or "accepted").upper()
            meta = _reading_meta(f"JOURNAL · WAKE✳︎ {int(entry['cycle']):03d}", status, topics, invocation.get("time"), "simulated" if invocation.get("provider") == "fixture" else invocation.get("status") or "accepted")
            body = (f'<p class="meta">{_html_text(invocation["provider"])} / {_html_text(invocation.get("successful_model") or invocation["model"])}</p>'
                    + "".join(f"<p>{_html_text(part)}</p>" for part in entry["summary"].split("\n\n") if part.strip())
                    + ('<p class="note">Deterministic simulation, not a live model result.</p>'
                       if invocation["provider"] == "fixture" else "")
                    + f'<p><a href="../index.html#history/{html.escape(entry["invocation"])}">Exact wake and decision →</a></p>')
            journal_path = target / "journal" / (entry["invocation"] + ".html")
            if not journal_path.exists():
                atomic_write(journal_path,
                             _reading_page(entry["title"], "WAKE✳︎ / JOURNAL", body, "../index.html#journal", meta_html=meta))
        atomic_write(target / "state.json", json.dumps(state, indent=2, ensure_ascii=False))
        atomic_write(target / "events.jsonl", "".join(canonical(event) + "\n" for event in events))
        atomic_write(target / "state.html", _flat_browser_shell(
            "State", "THE CURRENT DURABLE STATE", "Current state.", "Loaded from state.json when this page opens.", "state", "state.json"))
        atomic_write(target / "events.html", _flat_browser_shell(
            "History", "THE APPEND-ONLY RECORD", "Exact history.", "Loaded from events.jsonl when this page opens.", "events", "events.jsonl"))
        atomic_write(target / "head.txt", head + "\n")
        for notebook in state.get("notebooks", {}).values():
            atomic_write(target / "notebooks" / (notebook["id"] + ".html"), _notebook_html(notebook, state))
        for post in state.get("posts", {}).values():
            atomic_write(target / "blog" / (post["id"] + ".html"), _blog_html(post, state))
        if experiment:
            atomic_write(target / "experiment.json", json.dumps(experiment, indent=2))
        else:
            (target / "experiment.json").unlink(missing_ok=True)
        from .rejected import rejected_html
        atomic_write(target / "rejected.html", _flat_browser_shell(
            "Rejected & withheld drafts", "GOVERNANCE / STOPPED PROPOSALS",
            "Rejected & withheld drafts.", "Loaded from the current published record when this page opens.",
            "rejected", "wake-data.json"))
        from .provenance import build_map, build_map3d_projection, map3d_shard_filename
        graph = build_map(state, events, head)
        graph_json = json.dumps(graph, ensure_ascii=False)
        graph3d_shell, graph3d_shards = build_map3d_projection(graph)
        graph3d_json = json.dumps(graph3d_shell, ensure_ascii=False)
        # MAP and 3D MAP are static application shells. Only their flat JSON
        # projections change; the browser loads current data at view time.
        atomic_write(target / "map-data.json", graph_json)
        map_page = (assets / "map.html").read_text().replace("WAKE_CYCLE_COUNT", str(state["version"]))
        atomic_write(target / "map.html", map_page)
        atomic_write(target / "map3d-data.json", graph3d_json)
        map3d_page = (assets / "map3d.html").read_text().replace("WAKE_CYCLE_COUNT", str(state["version"]))
        atomic_write(target / "map3d.html", map3d_page)
        shard_dir = target / "map3d"
        if shard_dir.exists():
            for stale in shard_dir.glob("*.json"):
                stale.unlink()
        for parent, shard in graph3d_shards.items():
            atomic_write(shard_dir / map3d_shard_filename(parent), json.dumps(shard, ensure_ascii=False))
        atomic_write(target / "index.html", page)
        _export_console_components(target)
        _deployment_site(target, standalone=standalone)
        return {"path": str((target / "index.html").resolve()), "cycles": state["version"], "head": head}


def _deployment_site(target, *, standalone):
    """Bind every generated page to its installation before any reader runs.

    Templates are not deployable pages: export also selects data transport and
    operator links. Missing identity must never opt a LAN preview into GitHub.
    Keep this transform common to full exports and browser-only Pages shells.
    """
    mode = 'standalone' if standalone else 'hosted'
    atomic_write(target / 'deployment.json', json.dumps({'schema': 1, 'mode': mode}))
    marker = ('<script>window.WAKE_DEPLOYMENT=' + json.dumps({'schema': 1, 'mode': mode})
              + ';window.WAKE_STANDALONE=' + ('true' if standalone else 'false') + ';</script>')
    assets = Path(__file__).parent / "assets"
    for name in ("masthead.css", "site-theme.js", "console-light.css"):
        atomic_write(target / name, (assets / name).read_text())
    shell = (assets / "index.html").read_text()
    header = re.search(r'<header class="masthead">.*?</header>', shell, re.S).group(0)
    snapshot_path = target / "wake-data.json"
    snapshot = json.loads(snapshot_path.read_text()) if snapshot_path.exists() else {}
    header = header.replace("WAKE_CYCLE_COUNT", str(snapshot.get("state", {}).get("version", "—")))
    header = re.sub(r'href="#([^"]+)"', r'href="index.html#\1"', header)
    for path in target.rglob('*.html'):
        page = path.read_text()
        prefix = "../" * len(path.relative_to(target).parts[:-1])
        page = re.sub(r'href="((?:\.\./)*(?:style|nav|map|map3d|research|theme)\.css)(?:\?[^"]*)?"', r'href="\1?v=20261008-mobile-dock"', page)
        page = re.sub(r'src="((?:\.\./)*nav\.js)(?:\?[^"]*)?"', r'src="\1?v=20261008-workspace"', page)
        if '<header class="' in page and 'masthead' in page:
            shared = header
            if path.name == "console.html":
                shared = shared.replace('class="masthead"', 'class="research-header masthead"')
                shared = shared.replace('class="console-link" href="console.html"', 'class="console-link" href="console.html" aria-current="page"')
                shared = shared.replace('class="actions-light"', 'id="execution-state" class="actions-light"')
                shared = shared.replace('<i></i></span>\n    </a>', '<i id="execution-dot"></i></span>\n    </a>')
            # Relative navigation is derived from the artifact's directory,
            # never the machine, hosted branch, or another installation.
            shared = re.sub(r'href="(index|console)\.html', lambda m: 'href="' + prefix + m.group(1) + '.html', shared)
            page = re.sub(r'<header class="[^"]*masthead[^"]*">.*?</header>', lambda _: shared, page, count=1, flags=re.S)
        page = re.sub(r"<script>document.documentElement.dataset.theme='dark';try\{localStorage.setItem\('wake-theme','dark'\)\}catch\{\}</script>", '', page)
        page = re.sub(r'<script src="(?:console-theme|site-theme)\.js[^"]*"></script>', '', page)
        page = re.sub(r'<link rel="stylesheet" href="(?:\.\./)*masthead\.css[^"]*">', '', page)
        page = re.sub(r'<link rel="stylesheet" href="(?:\.\./)*console-light\.css[^"]*">', '', page)
        page = page.replace('</head>', f'<link rel="stylesheet" href="{prefix}console-light.css?v=20261008-daylight"><script src="{prefix}site-theme.js?v=20261008-shared"></script><link rel="stylesheet" href="{prefix}masthead.css?v=20261008-mobile-dock"></head>', 1)
        # Re-export may reuse a directory. An older marker later in <head> must
        # not override the newly selected installation. Normalize to one owner.
        page = re.sub(r'<script>window\.WAKE_(?:DEPLOYMENT|STANDALONE)=[^<]*</script>', '', page)
        page = page.replace('<head>', '<head>' + marker, 1)
        if standalone:
            page = page.replace('href="https://github.com/sudofx/wake/actions"', 'href="/runtime.json"')
            page = page.replace('Open WAKE GitHub Actions', 'Inspect local WAKE runtime')
        else:
            page = page.replace('href="/runtime.json"', 'href="https://github.com/sudofx/wake/actions"')
            page = page.replace('Inspect local WAKE runtime', 'Open WAKE GitHub Actions')
        atomic_write(path, page)
