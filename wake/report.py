# =============================================================================
# REPORT — the human projection layer. Static HTML/Markdown/JSON are derived views of canonical durable state. Rendering may explain or hide information, but it must never silently create experimental facts.
#
# MAINTENANCE PRINCIPLE
# ---------------------
# Read this file as part of a chain of custody.  WAKE✳︎ deliberately separates
# disposable cognition from durable authority.  Comments therefore explain not
# only what a function does, but why its boundary exists and what a refactor must
# not accidentally collapse.  Prefer explicit receipts, deterministic state
# transitions, and replayable facts over convenient hidden behavior.
# =============================================================================

"""Portable static journal. No CDN, build pipeline, tracking, or API-key exposure."""

from datetime import datetime
import html
import json
import os
import re
from pathlib import Path
from zoneinfo import ZoneInfo

from .store import canonical, now
from .scheduling import wake_status


def _shared_theme_switch(page):
    """Normalize theme controls on generated standalone pages."""
    switch = ('<label class="theme-switch"><input id="theme-toggle" type="checkbox" role="switch" '
              'aria-label="Use dark theme"><span class="theme-switch-track" aria-hidden="true"><i></i></span>'
              '<b>LIGHT / DARK</b></label>')
    css = (
        '.theme-switch{display:inline-flex;align-items:center;gap:9px;cursor:pointer;font:10px var(--mono);letter-spacing:.06em;color:var(--muted);white-space:nowrap}.theme-switch input{position:absolute;opacity:0;pointer-events:none}.theme-switch-track{width:34px;height:18px;border:1px solid var(--line);border-radius:20px;background:var(--surface);padding:2px;display:inline-flex;align-items:center}.theme-switch-track i{display:block;width:12px;height:12px;border-radius:50%;background:var(--muted);transition:transform .15s ease,background .15s ease}.theme-switch input:checked+.theme-switch-track i{transform:translateX(16px);background:var(--green)}.theme-switch input:focus-visible+.theme-switch-track{outline:2px solid var(--green);outline-offset:2px}.theme-switch b{font:inherit;color:var(--ink)}'
        ':root{--paper:#e8ecf4;--surface:#f8faff;--ink:#283457;--muted:#59627e;--line:#c5cce0;--green:#4f8f43;--accent:#7c5cc4;--hot:#b61d70;--pale:#e1e6f3}:root[data-theme=dark]{--paper:#24283b;--surface:#1f2335;--ink:#c0caf5;--muted:#a9b1d6;--line:#3b4261;--green:#649f25;--accent:#bb9af7;--hot:#b03772;--pale:#292e42}header{border-color:var(--line)}details{border-radius:12px;box-shadow:0 5px 14px rgb(45 58 108 / .08)}.theme-switch-track{border-color:var(--line)}'
    )
    script = ("<script>(()=>{const b=document.getElementById('theme-toggle');if(!b)return;const sync=()=>{const d=document.documentElement.dataset.theme==='dark';b.checked=d;b.setAttribute('aria-label',d?'Use light theme':'Use dark theme')};sync();b.addEventListener('change',()=>{const d=b.checked;if(d)document.documentElement.dataset.theme='dark';else delete document.documentElement.dataset.theme;try{localStorage.setItem('wake-theme',d?'dark':'light')}catch{}sync()})})()</script>")
    page = page.replace('--serif:var(--sans)', "--serif:Georgia,'Times New Roman',serif")
    page = re.sub(r'<button id="theme-toggle"[^>]*>.*?</button>', switch, page, count=1)
    return page.replace('</style>', css + '</style>', 1).replace('</body>', script + '</body>', 1)


def _with_shared_theme_switch(render):
    def wrapped(*args, **kwargs):
        return _shared_theme_switch(render(*args, **kwargs))
    return wrapped


# ---------------------------------------------------------------------------
# STEP: atomic_write
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.


# ---------------------------------------------------------------------------


def atomic_write(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8") as stream:
        stream.write(content)
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)


# ---------------------------------------------------------------------------
# STEP: _pretty
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.


# ---------------------------------------------------------------------------


def _pretty(value):
    return json.dumps(value, indent=2, ensure_ascii=False, sort_keys=False)


# ---------------------------------------------------------------------------
# STEP: _display_text
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.


# ---------------------------------------------------------------------------


def _display_text(value):
    """Presentation-only WAKE wordmark normalization; canonical state stays untouched."""
    text = str(value).replace("WAKE✳️", "WAKE✳").replace("WAKE✳︎", "WAKE✳")
    return text.replace("WAKE✳", "WAKE\u2733\uFE0E")


# ---------------------------------------------------------------------------
# STEP: _md_text
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.


# ---------------------------------------------------------------------------


def _md_text(value):
    text = _display_text(value).replace("**WAKE✳︎**", "WAKE✳︎")
    return text.replace("WAKE✳︎", "**WAKE✳︎**")


# ---------------------------------------------------------------------------
# STEP: _html_text
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.


# ---------------------------------------------------------------------------


def _html_text(value):
    escaped = html.escape(_display_text(value))
    return escaped.replace("WAKE✳︎", '<strong class="wake-mark">WAKE✳︎</strong>')


# ---------------------------------------------------------------------------
# STEP: _md_code
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.


# ---------------------------------------------------------------------------


def _md_code(value, language="json"):
    text = value if isinstance(value, str) else _pretty(value)
    text = _display_text(text)
    fence = "```"
    while fence in text:
        fence += "`"
    return f"{fence}{language}\n{text}\n{fence}"


# ---------------------------------------------------------------------------
# STEP: _html_pre
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.


# ---------------------------------------------------------------------------


def _html_pre(value):
    text = value if isinstance(value, str) else _pretty(value)
    # Presentation-only normalization: keep canonical JSON untouched while forcing
    # the text-style asterisk in readable exports, including historical prompts.
    text = _display_text(text)
    return f"<pre>{html.escape(text)}</pre>"


# ---------------------------------------------------------------------------
# STEP: _human_events_markdown
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.


# ---------------------------------------------------------------------------


def _human_events_markdown(events, head):
    lines = [
        "# **WAKE✳︎** — Human-readable event history",
        "",
        "> A presentation layer over `events.jsonl`. The JSONL file remains the canonical audit export.",
        "",
        f"Verified head: `{head}`",
        "",
        "[Open the HTML version](events.html) · [Raw JSONL](events.jsonl) · [Readable state](state.md)",
        "",
    ]
    for event in reversed(events):
        payload = event.get("payload", {})
        event_id = payload.get("id", "system")
        lines += [
            f"## Event {event['seq']:04d} · `{event['kind']}`",
            "",
            f"**Time:** {event['time']}  ",
            f"**ID:** `{event_id}`  ",
            f"**Hash:** `{event['hash']}`  ",
            f"**Previous hash:** `{event['prev_hash']}`",
            "",
        ]
        kind = event["kind"]
        if kind == "invocation_started":
            request = payload.get("request", {})
            lines += [
                f"**Provider / model:** `{payload.get('provider', '')}` / `{payload.get('model', '')}`  ",
                f"**Base version:** {payload.get('base_version', '')}  ",
                f"**Request hash:** `{payload.get('request_hash', '')}`",
                "",
                "### System prompt",
                "",
                _md_code(request.get("system", ""), "text"),
                "",
                "### Context sent to the model",
                "",
                _md_code(request.get("context", {})),
                "",
                "### Response schema",
                "",
                _md_code(request.get("response_schema", {})),
                "",
            ]
        elif kind == "accepted":
            if payload.get("editorial"):
                lines += ["### Withheld blog post", "", _md_code(payload["editorial"]), ""]
            lines += ["### Accepted proposal", "", _md_code(payload.get("proposal", {})), ""]
            if payload.get("raw_response") is not None:
                lines += ["### Raw model response", "", _md_code(payload["raw_response"], "json"), ""]
            if payload.get("result_hash"):
                lines += [f"**Result hash:** `{payload['result_hash']}`", ""]
        elif kind == "rejected":
            if payload.get("reason"):
                lines += [f"**Reason:** {payload['reason']}", ""]
            if payload.get("raw_response") is not None:
                lines += ["### Raw rejected response", "", _md_code(payload["raw_response"], "text"), ""]
        elif kind == "failed":
            lines += [f"**Reason:** {payload.get('reason', '')}", ""]
        elif kind == "observation":
            lines += [
                f"**Source:** `{payload.get('source', '')}`  ",
                f"**Actor:** `{payload.get('actor', '')}`",
                "",
                payload.get("content", ""),
                "",
            ]
        else:
            lines += ["### Payload", "", _md_code(payload), ""]
    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------------------
# STEP: _human_state_markdown
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.


# ---------------------------------------------------------------------------


def _human_state_markdown(state, head):
    lines = [
        "# **WAKE✳︎** — Human-readable durable state",
        "",
        "> A presentation layer over `state.json`. The JSON file remains the canonical state export.",
        "",
        f"**Version:** {state.get('version', 0)}  ",
        f"**Objective:** {state.get('objective', '')}  ",
        f"**Focus:** {state.get('focus', '')}  ",
        f"**Verified head:** `{head}`",
        "",
        "[Open the HTML version](state.html) · [Raw JSON](state.json) · [Readable history](events.md)",
        "",
    ]
    sections = [
        ("Beliefs", state.get("beliefs", {})),
        ("Commitments", state.get("commitments", {})),
        ("Projects", state.get("projects", {})),
        ("Notebooks", state.get("notebooks", {})),
        ("Invocations", state.get("invocations", {})),
        ("Evidence", state.get("evidence", {})),
        ("Journal", state.get("journal", [])),
        ("Research", state.get("research", {})),
        ("Blog posts", state.get("posts", {})),
    ]
    for title, collection in sections:
        lines += [f"## {title}", ""]
        if not collection:
            lines += ["_None recorded._", ""]
            continue
        if isinstance(collection, dict):
            for key, item in collection.items():
                label = item.get("title") if isinstance(item, dict) else None
                heading = f"### `{key}`" + (f" · {label}" if label else "")
                lines += [heading, "", _md_code(item), ""]
        else:
            for index, item in enumerate(collection, 1):
                label = item.get("title") if isinstance(item, dict) else None
                heading = f"### {index:03d}" + (f" · {label}" if label else "")
                lines += [heading, "", _md_code(item), ""]
    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------------------
# STEP: _human_page
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.


# ---------------------------------------------------------------------------


@_with_shared_theme_switch
def _human_page(title, subtitle, body, head, raw_href, markdown_href):
    favicon = "data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 64 64%27%3E%3Crect width=%2764%27 height=%2764%27 rx=%2712%27 fill=%27%23f7f3ea%27/%3E%3Cpath d=%27M32 9v46M9 32h46M15.7 15.7l32.6 32.6M48.3 15.7L15.7 48.3%27 stroke=%27%23286d72%27 stroke-width=%276%27 stroke-linecap=%27round%27/%3E%3C/svg%3E"
    return f"""<!doctype html>
<html lang=\"en\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">
<meta name=\"theme-color\" media=\"(prefers-color-scheme: light)\" content=\"#f4f5fb\"><meta name=\"theme-color\" media=\"(prefers-color-scheme: dark)\" content=\"#24283b\">
<link rel=\"icon\" href=\"{favicon}\"><title>{html.escape(title)} · WAKE✳︎</title>
<script>try{{const saved=localStorage.getItem('wake-theme');const dark=saved?saved==='dark':matchMedia('(prefers-color-scheme:dark)').matches;if(dark)document.documentElement.dataset.theme='dark'}}catch{{}}</script>
<style>
:root{{--paper:#f4f5fb;--surface:#ffffff;--ink:#24283b;--muted:#626b8a;--line:#d9ddeb;--green:#287ca3;--accent:#7658b3;--hot:#c52f9b;--pale:#ffffff;--mono:ui-monospace,SFMono-Regular,Consolas,monospace;--sans:Arial,Helvetica,sans-serif;--serif:var(--sans)}}
:root[data-theme=dark]{{--paper:#24283b;--surface:#1f2335;--ink:#c0caf5;--muted:#a9b1d6;--line:#32384d;--green:#7dcfff;--accent:#c69cff;--hot:#ff5ce1;--pale:#1f2335}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--paper);color:var(--ink);font:16px/1.6 var(--sans);font-variant-emoji:text}}a{{color:inherit;text-decoration:none}}.wake-mark{{font-weight:900}}@media(hover:hover) and (pointer:fine){{a:hover{{color:#c52f9b;text-decoration:none;text-shadow:0 0 7px #c52f9b99,0 0 15px #c52f9b55}}}}button,summary{{font:inherit;color:inherit}}button{{cursor:pointer}}main{{max-width:1120px;margin:auto;padding:32px 28px 90px}}header{{border-bottom:1px solid var(--line);padding-bottom:24px;margin-bottom:30px}}.topline{{display:flex;align-items:center;justify-content:space-between;gap:18px}}.wordmark{{font-size:30px;font-weight:900;letter-spacing:-1.7px}}.wordmark b{{color:var(--green);font-family:var(--serif);font-variant-emoji:text}}.theme-toggle{{border:1px solid var(--line);background:var(--surface);padding:8px 10px;font:10px var(--mono);letter-spacing:.08em}}.eyebrow{{font:10px var(--mono);letter-spacing:1.5px;color:var(--green);margin:26px 0 10px}}h1{{font:400 clamp(2.4rem,6vw,4.8rem)/1.03 var(--serif);letter-spacing:-.035em;margin:.1em 0 .3em}}h2{{font:400 1.7rem/1.2 var(--serif);margin:38px 0 14px}}h3{{font-size:14px;margin:24px 0 10px}}nav{{display:flex;gap:20px;flex-wrap:wrap;margin-top:18px;font:12px var(--mono);color:var(--muted)}}.meta{{color:var(--muted);font:12px/1.6 var(--mono)}}details{{background:var(--surface);border:1px solid var(--line);margin:12px 0;padding:0 16px}}summary{{cursor:pointer;padding:15px 0;font:12px var(--mono);color:var(--green)}}.inside{{border-top:1px solid var(--line);padding:14px 0 18px}}pre{{white-space:pre-wrap;overflow-wrap:anywhere;background:var(--pale);padding:16px;font:11px/1.7 var(--mono);max-height:560px;overflow:auto}}code{{font-family:var(--mono);overflow-wrap:anywhere}}.tag,.event-kind{{display:inline-block;border:1px solid var(--line);padding:2px 8px;font-size:.78rem;margin-right:8px}}.tag{{color:var(--accent)}}.event-kind{{text-transform:uppercase;letter-spacing:.06em}}.event-kind.accepted{{background:#dcebdd;color:#35623d;border-color:#bad2bd}}.event-kind.rejected,.event-kind.failed{{background:#f0dbd2;color:#9b3c28;border-color:#e0b8a6}}.event-kind.provider_attempt_started,.event-kind.provider_attempt_finished{{background:#dce8f1;color:#315f7b;border-color:#b9cfdf}}.event-kind.invocation_started{{background:#e4e0ef;color:#5c4c7b;border-color:#c9c0dd}}.event-kind.observation,.event-kind.research_collected{{background:#ede3cf;color:#7e6030;border-color:#dfcda7}}.event-kind.recovered{{background:#e5e2ed;color:#635178;border-color:#cec4d9}}.event-kind.deferred{{background:#e7e8e5;color:#59605a;border-color:#cfd2cc}}.event-links{{font-size:.9rem;color:var(--muted)}}hr{{border:0;border-top:1px solid var(--line);margin:28px 0}}@media(max-width:680px){{main{{padding:24px 18px 70px}}h1{{font-size:2.7rem}}.topline{{align-items:flex-start}}nav{{gap:14px;font-size:12px}}.meta,summary{{font-size:12px}}}}
</style><link rel=\"alternate\" type=\"application/rss+xml\" title=\"Bob’s Blog\" href=\"https://sudofx.github.io/wake/blog.xml\"><link rel=\"alternate\" type=\"application/rss+xml\" title=\"WAKE Journal\" href=\"https://sudofx.github.io/wake/journal.xml\"></head><body><main><header><div class=\"topline\"><a class=\"wordmark\" href=\"https://sudofx.github.io/wake/\">WAKE<b>✳︎</b></a><button id=\"theme-toggle\" class=\"theme-toggle\" type=\"button\" aria-pressed=\"false\" aria-label=\"Use dark theme\">DARK</button></div><div class=\"eyebrow\">READABLE EXPORT</div><h1>{html.escape(title)}</h1><p>{html.escape(subtitle)}</p><p class=\"meta\">Verified head: <code>{html.escape(head)}</code></p><nav><a href=\"index.html\">Main journal</a><a href=\"map.html\">MAP</a><a href=\"{html.escape(markdown_href)}\">Markdown source</a><a href=\"{html.escape(raw_href)}\">Raw data</a></nav></header>{body}</main><script>(()=>{{const b=document.getElementById('theme-toggle');const sync=()=>{{const d=document.documentElement.dataset.theme==='dark';b.textContent=d?'LIGHT':'DARK';b.setAttribute('aria-label',d?'Use light theme':'Use dark theme');b.setAttribute('aria-pressed',String(d))}};sync();b.addEventListener('click',()=>{{const d=document.documentElement.dataset.theme==='dark';if(d)delete document.documentElement.dataset.theme;else document.documentElement.dataset.theme='dark';try{{localStorage.setItem('wake-theme',d?'light':'dark')}}catch{{}}sync()}})}})();</script></body></html>"""

# ---------------------------------------------------------------------------
# STEP: _human_events_html
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.
# ---------------------------------------------------------------------------

def _human_events_html(events, head):
    cards = []
    for event in reversed(events):
        payload = event.get("payload", {})
        event_id = payload.get("id", "system")
        blocks = [
            f"<p class=\"meta\">Time: {html.escape(event['time'])}<br>ID: <code>{html.escape(str(event_id))}</code><br>Hash: <code>{html.escape(event['hash'])}</code><br>Previous hash: <code>{html.escape(event['prev_hash'])}</code></p>"
        ]
        kind = event["kind"]
        if kind == "invocation_started":
            request = payload.get("request", {})
            blocks += [
                f"<p><strong>Provider / model:</strong> <code>{html.escape(str(payload.get('provider','')))}</code> / <code>{html.escape(str(payload.get('model','')))}</code><br><strong>Base version:</strong> {html.escape(str(payload.get('base_version','')))}<br><strong>Request hash:</strong> <code>{html.escape(str(payload.get('request_hash','')))}</code></p>",
                "<h3>System prompt</h3>" + _html_pre(request.get("system", "")),
                "<h3>Context sent to the model</h3>" + _html_pre(request.get("context", {})),
                "<h3>Response schema</h3>" + _html_pre(request.get("response_schema", {})),
            ]
        elif kind == "accepted":
            if payload.get("editorial"):
                blocks += ["<h3>Withheld blog post</h3>" + _html_pre(payload["editorial"])]
            blocks += ["<h3>Accepted proposal</h3>" + _html_pre(payload.get("proposal", {}))]
            if payload.get("raw_response") is not None:
                blocks += ["<h3>Raw model response</h3>" + _html_pre(payload["raw_response"])]
            if payload.get("result_hash"):
                blocks += [f"<p><strong>Result hash:</strong> <code>{html.escape(payload['result_hash'])}</code></p>"]
        elif kind == "rejected":
            if payload.get("reason"):
                blocks += [f"<p><strong>Reason:</strong> {html.escape(str(payload['reason']))}</p>"]
            if payload.get("raw_response") is not None:
                blocks += ["<h3>Raw rejected response</h3>" + _html_pre(payload["raw_response"])]
        elif kind == "failed":
            blocks += [f"<p><strong>Reason:</strong> {html.escape(str(payload.get('reason','')))}</p>"]
        elif kind == "observation":
            blocks += [
                f"<p><strong>Source:</strong> <code>{html.escape(str(payload.get('source','')))}</code><br><strong>Actor:</strong> <code>{html.escape(str(payload.get('actor','')))}</code></p>",
                f"<p>{html.escape(str(payload.get('content','')))}</p>",
            ]
        else:
            blocks += ["<h3>Payload</h3>" + _html_pre(payload)]
        cards.append(
            f"<details id=\"event-{event['seq']}\"><summary><span class=\"tag\">#{event['seq']:04d}</span><span class=\"event-kind {html.escape(kind)}\">{html.escape(kind)}</span> · {html.escape(str(event_id))}</summary><div class=\"inside\">{''.join(blocks)}</div></details>"
        )
    body = "<p class=\"event-links\">Newest event first. Use your browser’s Find command to search prompts, evidence IDs, invocation IDs, or hashes.</p>" + "".join(cards)
    return _human_page("Human-readable event history", "Every recorded event, including exact model requests and replies, without changing the canonical JSONL.", body, head, "events.jsonl", "events.md")


# ---------------------------------------------------------------------------
# STEP: _human_state_html
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.


# ---------------------------------------------------------------------------


def _human_state_html(state, head):
    sections = [
        ("Beliefs", state.get("beliefs", {})), ("Commitments", state.get("commitments", {})),
        ("Projects", state.get("projects", {})), ("Notebooks", state.get("notebooks", {})),
        ("Invocations", state.get("invocations", {})), ("Evidence", state.get("evidence", {})),
        ("Journal", state.get("journal", [])), ("Research", state.get("research", {})),
        ("Blog posts", state.get("posts", {})),
    ]
    chunks = [f"<p><strong>Version:</strong> {html.escape(str(state.get('version',0)))}<br><strong>Objective:</strong> {html.escape(str(state.get('objective','')))}<br><strong>Focus:</strong> {html.escape(str(state.get('focus','')))}</p>"]
    for title, collection in sections:
        chunks.append(f"<h2>{html.escape(title)}</h2>")
        if not collection:
            chunks.append("<p class=\"meta\">None recorded.</p>")
            continue
        items = collection.items() if isinstance(collection, dict) else enumerate(collection, 1)
        for key, item in items:
            label = item.get("title") if isinstance(item, dict) else None
            summary = f"{key}" + (f" · {label}" if label else "")
            chunks.append(f"<details><summary>{html.escape(str(summary))}</summary><div class=\"inside\">{_html_pre(item)}</div></details>")
    return _human_page("Human-readable durable state", "The current projected state, reorganized for reading without changing the canonical JSON.", "".join(chunks), head, "state.json", "state.md")


# ---------------------------------------------------------------------------
# STEP: _reading_page
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.


# ---------------------------------------------------------------------------


@_with_shared_theme_switch
def _reading_page(title, eyebrow, body, source_href, back_href="../index.html"):
    """Standalone browser reading page; Markdown remains a secondary flat artifact."""
    favicon = "data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 64 64%27%3E%3Crect width=%2764%27 height=%2764%27 rx=%2712%27 fill=%27%23f7f3ea%27/%3E%3Cpath d=%27M32 9v46M9 32h46M15.7 15.7l32.6 32.6M48.3 15.7L15.7 48.3%27 stroke=%27%23286d72%27 stroke-width=%276%27 stroke-linecap=%27round%27/%3E%3C/svg%3E"
    return f"""<!doctype html>
<html lang=\"en\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">
<meta name=\"theme-color\" media=\"(prefers-color-scheme: light)\" content=\"#f4f5fb\"><meta name=\"theme-color\" media=\"(prefers-color-scheme: dark)\" content=\"#24283b\"><link rel=\"icon\" href=\"{favicon}\"><title>{html.escape(title)} · WAKE✳︎</title>
<script>try{{const saved=localStorage.getItem('wake-theme');const dark=saved?saved==='dark':matchMedia('(prefers-color-scheme:dark)').matches;if(dark)document.documentElement.dataset.theme='dark'}}catch{{}}</script>
<style>
:root{{--paper:#f4f5fb;--surface:#ffffff;--ink:#24283b;--muted:#626b8a;--line:#d9ddeb;--green:#287ca3;--accent:#7658b3;--hot:#c52f9b;--pale:#ffffff;--mono:ui-monospace,SFMono-Regular,Consolas,monospace;--sans:Arial,Helvetica,sans-serif;--serif:var(--sans)}}
:root[data-theme=dark]{{--paper:#24283b;--surface:#1f2335;--ink:#c0caf5;--muted:#a9b1d6;--line:#32384d;--green:#7dcfff;--accent:#c69cff;--hot:#ff5ce1;--pale:#1f2335}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--paper);color:var(--ink);font:17px/1.72 var(--sans);font-variant-emoji:text}}main{{max-width:840px;margin:auto;padding:34px 22px 90px}}header{{border-bottom:1px solid var(--line);padding-bottom:24px;margin-bottom:34px}}.topline{{display:flex;align-items:center;justify-content:space-between;gap:18px}}.wordmark{{font:900 29px/1 var(--sans);letter-spacing:-1.7px;color:inherit;text-decoration:none}}.wordmark b{{color:var(--green);font-family:var(--serif);font-variant-emoji:text}}.theme-toggle{{border:1px solid var(--line);background:var(--surface);color:var(--ink);padding:8px 10px;font:10px var(--mono);letter-spacing:.08em;cursor:pointer}}h1{{font:400 clamp(2.4rem,7vw,4.8rem)/1.02 var(--serif);letter-spacing:-.035em;margin:.18em 0 .3em}}h2{{font:400 1.8rem/1.2 var(--serif);margin-top:2.2em}}h3{{font:700 14px var(--sans);margin-top:2em}}a{{color:var(--green);text-decoration:none}}.wake-mark{{font-weight:900}}@media(hover:hover) and (pointer:fine){{a:hover{{color:#c52f9b;text-decoration:none;text-shadow:0 0 7px #c52f9b99,0 0 15px #c52f9b55}}}}nav{{display:flex;gap:18px;flex-wrap:wrap;margin-top:17px;font:10px var(--mono)}}.eyebrow,.meta{{font:10px var(--mono);color:var(--muted);text-transform:uppercase;letter-spacing:.1em}}.eyebrow{{color:var(--green);margin-top:24px}}.lede{{font-size:1.25rem;line-height:1.55}}.note{{border-left:3px solid var(--accent);padding:2px 0 2px 18px;margin:28px 0}}.sources{{font-family:var(--sans);font-size:.95rem}}code{{font-family:var(--mono)}}hr{{border:0;border-top:1px solid var(--line);margin:34px 0}}small{{color:var(--muted)}}@media(max-width:680px){{main{{padding:24px 18px 70px}}h1{{font-size:2.7rem}}}}
</style><link rel=\"alternate\" type=\"application/rss+xml\" title=\"Bob’s Blog\" href=\"https://sudofx.github.io/wake/blog.xml\"><link rel=\"alternate\" type=\"application/rss+xml\" title=\"WAKE Journal\" href=\"https://sudofx.github.io/wake/journal.xml\"></head><body><main><header><div class=\"topline\"><a class=\"wordmark\" href=\"https://sudofx.github.io/wake/\">WAKE<b>✳︎</b></a><button id=\"theme-toggle\" class=\"theme-toggle\" type=\"button\">DARK</button></div><div class=\"eyebrow\">{html.escape(eyebrow)}</div><h1>{html.escape(title)}</h1><nav><a href=\"{html.escape(back_href)}\">WAKE site</a><a href=\"../map.html\">MAP</a><a href=\"{html.escape(source_href)}\">Markdown source</a></nav></header>{body}</main><script>(()=>{{const b=document.getElementById('theme-toggle');const sync=()=>{{const d=document.documentElement.dataset.theme==='dark';b.textContent=d?'LIGHT':'DARK';b.setAttribute('aria-label',d?'Use light theme':'Use dark theme')}};sync();b.addEventListener('click',()=>{{const d=document.documentElement.dataset.theme==='dark';if(d)delete document.documentElement.dataset.theme;else document.documentElement.dataset.theme='dark';try{{localStorage.setItem('wake-theme',d?'light':'dark')}}catch{{}}sync()}})}})();</script></body></html>"""

# ---------------------------------------------------------------------------
# STEP: _notebook_html
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.
# ---------------------------------------------------------------------------

def _notebook_html(notebook, state):
    source_items = []
    for eid in notebook["evidence"]:
        evidence = state["evidence"][eid]
        source_items.append(f'<li><a href="{html.escape(str(evidence["source"]))}">{html.escape(eid)}</a></li>')
    body = (
        f'<p class="lede">{_html_text(notebook["summary"])}</p>'
        f'<h2>Findings</h2><p>{_html_text(notebook["findings"])}</p>'
        f'<h2>Limitations and competing views</h2><p>{_html_text(notebook["limitations"])}</p>'
        f'<h2>Next questions</h2><p>{_html_text(notebook["next_questions"])}</p>'
        f'<h2>Collected sources</h2><ul class="sources">{"".join(source_items)}</ul>'
        f'<hr><p class="meta">Revision {notebook["revision"]} · AI-authored research synthesis; see source scopes in the journal.</p>'
    )
    return _reading_page(notebook["title"], "WAKE✳︎ / RESEARCH NOTEBOOK", body, notebook["id"] + ".md")


# ---------------------------------------------------------------------------
# STEP: _blog_html
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.


# ---------------------------------------------------------------------------


def _blog_html(post, state):
    paragraphs = "".join(f"<p>{_html_text(part)}</p>" for part in str(post["body"]).split("\n\n") if part.strip())
    lens = f'<div class="note"><div class="eyebrow">BOB’S LENS / PHILOSOPHICAL REFLECTION</div><p>{_html_text(post["lens"])}</p></div>' if post.get("lens") else ""
    notebooks = "".join(
        f'<li><a href="../notebooks/{html.escape(nid)}.html">{html.escape(state["notebooks"][nid]["title"])}</a> <small>· <a href="../notebooks/{html.escape(nid)}.md">Markdown source</a></small></li>'
        for nid in post["notebooks"])
    sources = "".join(
        f'<li><a href="{html.escape(str(state["evidence"][eid]["source"]))}">{html.escape(eid)}</a></li>'
        for eid in post["evidence"])
    correction = ""
    if post.get("superseded_by"):
        correction = f'<p class="note">Superseded by <a href="{html.escape(post["superseded_by"])}.html">{html.escape(post["superseded_by"])}</a>.</p>'
    body = (
        f'<p class="lede">{_html_text(post["lede"])}</p>{correction}{paragraphs}{lens}'
        f'<h2>Follow the receipts</h2><h3>Research notebooks</h3><ul class="sources">{notebooks}</ul>'
        f'<h3>Collected sources</h3><ul class="sources">{sources}</ul>'
        f'<p><a href="../index.html#history/{html.escape(post["created_by"])}">Exact wake and decision →</a></p>'
        '<hr><p class="meta">AI-authored from WAKE✳︎’s durable research record. Research claims link to evidence; philosophical reflections are reflections.</p>'
    )
    body += '<p><a href="../blog.xml">Subscribe to Bob’s blog via RSS</a></p>'
    return _reading_page(post["title"], "BOB / WAKE✳︎ BLOG", body, post["id"] + ".md")


# ---------------------------------------------------------------------------
# STEP: export
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.


# ---------------------------------------------------------------------------


def export(store, destination="site", experiment=None, operation=None):
    with store.lock():
        state = store.load()
        events = store.events()
        _, head = store.replay()
        if experiment is None:
            evidence_file = store.directory / "experiment.json"
            experiment = json.loads(evidence_file.read_text()) if evidence_file.exists() else None
        data = {"state": state, "events": events, "head": head, "generated": now(),
                "experiment": experiment, "timezone": "America/Los_Angeles", "operation": operation,
                "wake_status": (operation or {}).get("wake_status") or wake_status(state)}
        target = Path(destination)
        target.mkdir(parents=True, exist_ok=True)
        assets = Path(__file__).parent / "assets"
        template = (assets / "index.html").read_text()
        # Source templates retain stylesheet links for direct local previews; the
        # published artifact carries the same styles inline for a self-contained page.
        template = template.replace('<link rel="stylesheet" href="style.css"><link rel="stylesheet" href="nav.css">', "")
        embedded = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
        page = template.replace("/* WAKE_STYLE */", (assets / "style.css").read_text())
        page = page.replace("/* NAV_STYLE */", (assets / "nav.css").read_text())
        page = page.replace("/* NAV_SCRIPT */", (assets / "nav.js").read_text())
        page = page.replace("/* WAKE_SCRIPT */", (assets / "app.js").read_text())
        page = page.replace("/* HELP_SCRIPT */", (assets / "help.js").read_text())
        page = page.replace("/* DATA_VIEW_SCRIPT */", (assets / "data-view.js").read_text())
        page = page.replace("/* PET_SCRIPT */", (assets / "pet.js").read_text()).replace("WAKE_DATA", embedded)
        # Browser UX is HTML-first. Markdown remains available as a flat source artifact.
        page = page.replace('href="journal.md">Markdown ↓</a>', 'href="events.html">Readable history →</a>')
        page = page.replace('Read the complete <a href="journal.md">Markdown journal</a> or download <a href="state.json">the durable state</a>.',
                            'Read the <a href="events.html">human-readable history</a> or <a href="state.html">human-readable durable state</a>.')
        page = page.replace('<a href="state.json">State →</a><a href="events.jsonl">History →</a><a href="journal.md">Markdown →</a>',
                            '<a href="state.html">State →</a><a href="events.html">History →</a><a href="journal.md">Journal source ↓</a>')
        page = page.replace("'.md'>Markdown ↓</a>", "'.html'>Standalone HTML →</a> · <a class=\"subtle\" href=\"blog/'+encodeURIComponent(post.id)+'.md\">Markdown source ↓</a>")
        lines = ["# **WAKE✳︎** — The journal", "", "> Disposable models. Durable state. Receipts for everything.", "",
                 f"Objective: {_md_text(state['objective'])}", "", f"Verified head: `{head}`", "",
                 "Fixture entries are deterministic simulations, not live model experiments.", ""]
        for item in reversed(state["journal"]):
            invocation = state["invocations"][item["invocation"]]
            date = datetime.fromisoformat(invocation["time"]).astimezone(ZoneInfo("America/Los_Angeles"))
            lines += [f"## {item['cycle']:03d} · {_md_text(item['title'])}", "",
                      f"{date:%B %d, %Y · %I:%M %p %Z} · {invocation['provider']} / {invocation.get('successful_model') or invocation['model']}", "",
                      _md_text(item["summary"]), "", f"Invocation: `{item['invocation']}`", ""]
        from .feeds import build_feeds
        for filename, content in build_feeds(state).items():
            atomic_write(target / filename, content)
        for entry in state["journal"]:
            invocation = state["invocations"][entry["invocation"]]
            body = (f'<p class="meta">Cycle {entry["cycle"]} · {_html_text(invocation["time"])} · '
                    f'{_html_text(invocation["provider"])} / {_html_text(invocation.get("successful_model") or invocation["model"])}</p>'
                    + "".join(f"<p>{_html_text(part)}</p>" for part in entry["summary"].split("\n\n") if part.strip())
                    + ('<p class="note">Deterministic simulation, not a live model result.</p>'
                       if invocation["provider"] == "fixture" else "")
                    + f'<p><a href="../index.html#history/{html.escape(entry["invocation"])}">Exact wake and decision →</a></p>'
                    + '<p><a href="../journal.xml">Subscribe to the journal via RSS</a></p>')
            atomic_write(target / "journal" / (entry["invocation"] + ".html"),
                         _reading_page(entry["title"], "WAKE✳︎ / JOURNAL", body, "../journal.md"))
        atomic_write(target / "journal.md", "\n".join(lines))
        atomic_write(target / "state.json", json.dumps(state, indent=2, ensure_ascii=False))
        atomic_write(target / "events.jsonl", "".join(canonical(event) + "\n" for event in events))
        atomic_write(target / "state.md", _human_state_markdown(state, head))
        atomic_write(target / "state.html", _human_state_html(state, head))
        atomic_write(target / "events.md", _human_events_markdown(events, head))
        atomic_write(target / "events.html", _human_events_html(events, head))
        atomic_write(target / "head.txt", head + "\n")
        for notebook in state.get("notebooks", {}).values():
            sources = "\n".join(f"- [{eid}]({state['evidence'][eid]['source']})" for eid in notebook["evidence"])
            markdown = (f"# {_md_text(notebook['title'])}\n\n{_md_text(notebook['summary'])}\n\n## Findings\n\n{_md_text(notebook['findings'])}\n\n"
                        f"## Limitations and competing views\n\n{_md_text(notebook['limitations'])}\n\n"
                        f"## Next questions\n\n{_md_text(notebook['next_questions'])}\n\n## Collected sources\n\n{sources}\n\n"
                        f"Revision {notebook['revision']} · AI-authored research synthesis; see source scopes in the journal.\n")
            atomic_write(target / "notebooks" / (notebook["id"] + ".md"), markdown)
            atomic_write(target / "notebooks" / (notebook["id"] + ".html"), _notebook_html(notebook, state))
        for post in state.get("posts", {}).values():
            newline = chr(10)
            notebook_links = newline.join(
                f"- [{state['notebooks'][item]['title']}](../index.html#projects/notebook:{item})"
                for item in post["notebooks"])
            source_links = newline.join(
                f"- [{item}]({state['evidence'][item]['source']})" for item in post["evidence"])
            parts = [f"# {_md_text(post['title'])}", "", _md_text(post["lede"]), "", _md_text(post["body"])]
            if post.get("lens"):
                parts += ["", "> **Bob's Lens — philosophical reflection**", "", f"> {_md_text(post['lens'])}"]
            if post.get("superseded_by"):
                parts += ["", f"This post was superseded by [{post['superseded_by']}](../index.html#blog/{post['superseded_by']})."]
            parts += ["", "## Follow the receipts", "", "### Research notebooks", "", notebook_links, "",
                      "### Collected sources", "", source_links, "",
                      f"[Exact wake and decision](../index.html#history/{post['created_by']})", "",
                      "AI-authored from **WAKE✳︎**'s durable research record. Research claims link to evidence; philosophical reflections are reflections.", ""]
            atomic_write(target / "blog" / (post["id"] + ".md"), newline.join(parts))
            atomic_write(target / "blog" / (post["id"] + ".html"), _blog_html(post, state))
        if experiment:
            atomic_write(target / "experiment.json", json.dumps(experiment, indent=2))
        else:
            (target / "experiment.json").unlink(missing_ok=True)
        from .rejected import rejected_html
        atomic_write(target / "rejected.html", _human_page(
            "Rejected & withheld drafts", "What was proposed, why it stopped, and what was preserved.",
            rejected_html(state, events), head, "events.jsonl", "events.md"))
        from .provenance import build_map
        graph = build_map(state, events, head)
        graph_json = json.dumps(graph, ensure_ascii=False)
        map_page = (assets / "map.html").read_text()
        map_page = map_page.replace('<link rel="stylesheet" href="map.css"><link rel="stylesheet" href="nav.css">', "")
        map_page = map_page.replace("/* MAP_STYLE */", (assets / "map.css").read_text())
        map_page = map_page.replace("/* NAV_STYLE */", (assets / "nav.css").read_text())
        map_page = map_page.replace("/* NAV_SCRIPT */", (assets / "nav.js").read_text())
        map_page = map_page.replace("/* MAP_SCRIPT */", (assets / "map.js").read_text())
        map_page = map_page.replace("MAP_DATA", graph_json.replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029"))
        atomic_write(target / "map-data.json", graph_json)
        atomic_write(target / "map.html", map_page)
        atomic_write(target / "index.html", page)
        return {"path": str((target / "index.html").resolve()), "cycles": state["version"], "head": head}
