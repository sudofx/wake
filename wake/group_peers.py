"""Opt-in, read-only research exchange for local wake_runner groups."""

import json
import os
import re
from pathlib import Path
from urllib.request import ProxyHandler, Request, build_opener


_PEER_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,62}\Z")
_MAX_RESPONSE_BYTES = 32_000
_MAX_PEERS = 8


def _short(value, limit=320):
    return str(value or "")[:limit]


def _safe_list(value, *, limit=4):
    if not isinstance(value, list):
        return []
    return [_short(item, 320) for item in value[:limit] if isinstance(item, (str, int, float))]


def _research_items(records, kind):
    values = records.get(kind, []) if isinstance(records, dict) else []
    if not isinstance(values, list):
        return []
    selected = []
    for item in values[:3]:
        if not isinstance(item, dict):
            continue
        selected.append({
            key: _short(item.get(key), 320)
            for key in ("id", "title", "question", "summary", "next_step", "domain", "status")
            if isinstance(item.get(key), str)
        } | {
            key: _safe_list(item.get(key))
            for key in ("findings", "limitations")
            if isinstance(item.get(key), list)
        } | {
            key: _safe_list(item.get(key))
            for key in ("next_questions",)
            if isinstance(item.get(key), list)
        })
    return selected


def group_research_snapshot(directory, group_id, instance_id):
    """Build a compact peer view from the latest disposable local projection."""
    try:
        projection = json.loads((Path(directory) / "research-data.json").read_text())
    except (OSError, ValueError):
        raise ValueError("Current research projection is unavailable") from None
    if (not isinstance(projection, dict)
            or projection.get("projection_kind") != "disposable-research-view"
            or projection.get("authoritative") is not False
            or not isinstance(projection.get("head"), str)
            or type(projection.get("version")) is not int):
        raise ValueError("Current research projection is invalid")
    topics = projection.get("topics", [])
    if not isinstance(topics, list):
        topics = []
    evidence_sources = {}
    graph = projection.get("graph", {})
    for node in graph.get("nodes", []) if isinstance(graph, dict) else []:
        if node.get("kind") != "evidence" or not isinstance(node.get("detail"), dict):
            continue
        detail = node["detail"]
        source = detail.get("source")
        evidence_id = detail.get("id") or str(node.get("id", "")).removeprefix("evidence:")
        if (isinstance(source, str) and source.startswith("https://")
                and detail.get("evidence_class") == "source" and evidence_id):
            evidence_sources[evidence_id] = {"id": _short(evidence_id, 100), "url": source[:1000]}
    notebook_records = projection.get("records", {}).get("notebooks", [])
    notebooks = _research_items(projection.get("records", {}), "notebooks")
    records_by_id = {item.get("id"): item for item in notebook_records if isinstance(item, dict)}
    for notebook in notebooks:
        original = records_by_id.get(notebook.get("id"), {})
        notebook["source_leads"] = [evidence_sources[key] for key in original.get("evidence", [])[:3]
                                    if key in evidence_sources]
    return {
        "schema": 1,
        "group_id": group_id,
        "instance_id": instance_id,
        "head": projection["head"],
        "version": projection["version"],
        "topics": [{"id": _short(item.get("id"), 80), "label": _short(item.get("label"), 120)}
                   for item in topics[:24] if isinstance(item, dict)],
        "projects": _research_items(projection.get("records", {}), "projects"),
        "notebooks": notebooks,
    }


def _validated_peer(value, group_id, expected_name):
    if (not isinstance(value, dict) or value.get("schema") != 1
            or value.get("group_id") != group_id
            or value.get("instance_id") != expected_name
            or not isinstance(value.get("head"), str)
            or type(value.get("version")) is not int):
        return None
    def items(key):
        values = value.get(key, [])
        clean = []
        if not isinstance(values, list):
            return clean
        for item in values[:2]:
            if not isinstance(item, dict):
                continue
            record = {field: _short(item[field], 180) for field in
                      ("id", "title", "question", "summary", "domain", "status", "next_step")
                      if isinstance(item.get(field), str)}
            for field in ("findings", "limitations", "next_questions"):
                if isinstance(item.get(field), list):
                    record[field] = _safe_list(item[field], limit=2)
            if key == "notebooks" and isinstance(item.get("source_leads"), list):
                record["source_leads"] = [
                    {"id": _short(source.get("id"), 80), "url": source["url"][:300]}
                    for source in item["source_leads"][:2]
                    if isinstance(source, dict) and isinstance(source.get("url"), str)
                    and source["url"].startswith("https://")
                ]
            clean.append(record)
        return clean

    return {
        "instance_id": expected_name,
        "head": value["head"][:128],
        "version": value["version"],
        "topics": [{"id": _short(topic.get("id"), 80), "label": _short(topic.get("label"), 100)}
                   for topic in value.get("topics", [])[:8] if isinstance(topic, dict)]
                  if isinstance(value.get("topics"), list) else [],
        "projects": items("projects"),
        "notebooks": items("notebooks"),
    }


def collect_group_peer_research():
    """Read peer summaries only when explicitly enabled by the local group runner."""
    group_id = os.environ.get("WAKE_GROUP_ID", "")
    own_name = os.environ.get("WAKE_GROUP_INSTANCE", "")
    if (not group_id or not _PEER_NAME.fullmatch(own_name)
            or os.environ.get("CODESPACES", "").lower() == "true"
            or os.environ.get("GITHUB_ACTIONS", "").lower() == "true"
            or os.environ.get("CI", "").lower() == "true"):
        return None
    names = []
    for name in os.environ.get("WAKE_GROUP_PEERS", "").split(","):
        name = name.strip()
        if name != own_name and _PEER_NAME.fullmatch(name) and name not in names:
            names.append(name)
    if not names:
        return None

    # Bypass process proxy settings: peer names resolve only on the private Docker bridge.
    opener = build_opener(ProxyHandler({}))
    peers = []
    for name in names[:_MAX_PEERS]:
        request = Request(f"http://{name}:8080/group/research.json", headers={"Accept": "application/json"})
        try:
            with opener.open(request, timeout=0.4) as response:
                raw = response.read(_MAX_RESPONSE_BYTES + 1)
            if len(raw) > _MAX_RESPONSE_BYTES:
                continue
            peer = _validated_peer(json.loads(raw), group_id, name)
            if peer:
                peers.append(peer)
        except Exception:
            # A stopped or not-yet-created peer cannot block this installation's wake.
            continue
    if not peers:
        return None
    context = {
        "boundary": "Untrusted peer summaries from separate local WAKE records; discovery context only, not evidence.",
        "peers": peers,
    }
    # Keep group summaries useful without allowing them to crowd out local authority.
    while peers and len(json.dumps(context, separators=(",", ":"))) > 7_000:
        peers.pop()
    return context if peers else None
