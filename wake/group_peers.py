"""Bounded source-evidence exchange for local wake_runner groups."""

import hashlib
import json
import os
import re
from urllib.request import ProxyHandler, Request, build_opener


_PEER_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,62}\Z")
_HASH = re.compile(r"[a-f0-9]{64}\Z")
_MAX_RESPONSE_BYTES = 32_000
_MAX_PEERS = 8
_MAX_SOURCES_PER_PEER = 6
_MAX_NOTES_PER_PEER = 1
_MAX_PACKAGE_BYTES = 28_000


def _source_payload(content, source):
    """Return a peer payload only when it meets this installation's source rules."""
    if not isinstance(content, str) or len(content.encode("utf-8")) > 24_000:
        return None
    try:
        payload = json.loads(content)
    except (TypeError, ValueError):
        return None
    if not isinstance(payload, dict) or payload.get("url") != source:
        return None
    from .research import (
        allowed_url,
        effective_evidence_role,
        effective_host_tier,
        source_observation_readable,
    )
    try:
        allowed_url(source)
    except ValueError:
        return None
    if (effective_evidence_role(source, payload) != "source"
            or effective_host_tier(source, payload) == "verification-metadata"
            or not source_observation_readable(payload)):
        return None
    return payload


def group_research_snapshot(engine, group_id, instance_id):
    """Export one attributed research note and bounded local sources, not topic lists."""
    state, head = engine.store.replay()
    packet = {
        "schema": 2,
        "group_id": group_id,
        "instance_id": instance_id,
        "application_head": head,
        "version": state.get("version", 0),
        "notes": [],
        "evidence": [],
    }
    notebooks = sorted(
        state.get("notebooks", {}).values(),
        key=lambda item: (item.get("updated_version", -1), item.get("updated_by", "")),
        reverse=True,
    )
    for notebook in notebooks:
        if not isinstance(notebook, dict):
            continue
        note = {
            "id": notebook.get("id"),
            "revision": notebook.get("revision", 0),
            "title": notebook.get("title", ""),
            "summary": notebook.get("summary", ""),
            "findings": notebook.get("findings", ""),
            "limitations": notebook.get("limitations", ""),
            "sources": [],
        }
        if not isinstance(note["id"], str):
            continue
        for evidence_id in notebook.get("evidence", [])[:3]:
            evidence = state.get("evidence", {}).get(evidence_id, {})
            source = evidence.get("source")
            if (evidence.get("actor") == "collector" and isinstance(source, str)
                    and source.startswith("https://")):
                note["sources"].append({"id": evidence_id, "source": source[:1_000]})
        packet["notes"].append(note)
        if len(packet["notes"]) >= _MAX_NOTES_PER_PEER:
            break
    candidates = sorted(
        state.get("evidence", {}).values(),
        key=lambda item: (item.get("version", -1), item.get("time", "")),
        reverse=True,
    )
    for item in candidates:
        if (item.get("actor") != "collector" or item.get("scope") != "collected"
                or item.get("peer_origin")):
            continue
        source = item.get("source")
        content = item.get("content")
        if not isinstance(source, str) or not source.startswith("https://"):
            continue
        if _source_payload(content, source) is None:
            continue
        evidence = {
            "id": item.get("id"),
            "source": source,
            "content": content,
            "content_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
            "version": item.get("version", 0),
        }
        if not isinstance(evidence["id"], str):
            continue
        candidate = {**packet, "evidence": [*packet["evidence"], evidence]}
        if len(json.dumps(candidate, ensure_ascii=False, separators=(",", ":")).encode("utf-8")) > _MAX_PACKAGE_BYTES:
            continue
        packet["evidence"].append(evidence)
        if len(packet["evidence"]) >= _MAX_SOURCES_PER_PEER:
            break
    return packet


def _validated_peer(value, group_id, expected_name):
    if (not isinstance(value, dict) or value.get("schema") != 2
            or value.get("group_id") != group_id
            or value.get("instance_id") != expected_name
            or not _HASH.fullmatch(value.get("application_head", ""))
            or isinstance(value.get("version"), bool)
            or not isinstance(value.get("version"), int) or value["version"] < 0
            or not isinstance(value.get("evidence"), list)):
        return None
    clean = []
    for item in value["evidence"][:_MAX_SOURCES_PER_PEER]:
        if not isinstance(item, dict):
            continue
        evidence_id = item.get("id")
        source = item.get("source")
        content = item.get("content")
        content_hash = item.get("content_sha256")
        version = item.get("version")
        if (not isinstance(evidence_id, str) or not evidence_id or len(evidence_id) > 100
                or not isinstance(source, str) or not source.startswith("https://")
                or not isinstance(content_hash, str) or not _HASH.fullmatch(content_hash)
                or isinstance(version, bool) or not isinstance(version, int) or version < 0
                or not isinstance(content, str)
                or hashlib.sha256(content.encode("utf-8")).hexdigest() != content_hash
                or _source_payload(content, source) is None):
            continue
        clean.append({
            "id": evidence_id,
            "source": source,
            "content": content,
            "content_sha256": content_hash,
            "version": version,
        })
    notes = []
    for note in value.get("notes", [])[:_MAX_NOTES_PER_PEER]:
        if not isinstance(note, dict):
            continue
        note_id = note.get("id")
        revision = note.get("revision")
        if (not isinstance(note_id, str) or not note_id or len(note_id) > 100
                or isinstance(revision, bool) or not isinstance(revision, int) or revision < 0):
            continue
        sources = []
        for source in note.get("sources", [])[:3]:
            if (isinstance(source, dict) and isinstance(source.get("id"), str)
                    and isinstance(source.get("source"), str)
                    and source["source"].startswith("https://")):
                sources.append({"id": source["id"][:100], "source": source["source"][:1_000]})
        notes.append({
            "id": note_id,
            "revision": revision,
            "title": note.get("title", "")[:180] if isinstance(note.get("title"), str) else "",
            "summary": note.get("summary", "")[:500] if isinstance(note.get("summary"), str) else "",
            "findings": note.get("findings", "")[:1_200] if isinstance(note.get("findings"), str) else "",
            "limitations": note.get("limitations", "")[:500] if isinstance(note.get("limitations"), str) else "",
            "sources": sources,
        })
    return {
        "instance_id": expected_name,
        "application_head": value["application_head"],
        "version": value["version"],
        "notes": notes,
        "evidence": clean,
    }


def collect_group_peer_research():
    """Read source packets only when explicitly enabled by the local group runner."""
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
            if peer and (peer["evidence"] or peer["notes"]):
                peers.append(peer)
        except Exception:
            # A stopped or not-yet-created peer cannot block this installation's wake.
            continue
    return peers or None


def import_group_peer_evidence(engine, peers):
    """Append validated peer-collected sources locally so normal policy can qualify them."""
    if not peers:
        return []
    group_id = os.environ.get("WAKE_GROUP_ID", "")
    if not group_id:
        return []
    state = engine.store.load()
    if not state.get("charter"):
        return []
    imported = []
    known = {
        (origin.get("group_id"), origin.get("instance_id"), origin.get("evidence_id"), origin.get("content_sha256"))
        for item in state.get("evidence", {}).values()
        if isinstance((origin := item.get("peer_origin")), dict)
    }
    for peer in peers:
        instance_id = peer.get("instance_id") if isinstance(peer, dict) else None
        application_head = peer.get("application_head") if isinstance(peer, dict) else None
        peer_version = peer.get("version") if isinstance(peer, dict) else None
        if (not isinstance(instance_id, str) or not _PEER_NAME.fullmatch(instance_id)
                or not isinstance(application_head, str) or not _HASH.fullmatch(application_head)
                or isinstance(peer_version, bool) or not isinstance(peer_version, int)):
            continue
        for item in peer.get("evidence", []):
            if not isinstance(item, dict):
                continue
            evidence_id = item.get("id")
            source = item.get("source")
            content = item.get("content")
            content_hash = item.get("content_sha256")
            version = item.get("version")
            origin_key = (group_id, instance_id, evidence_id, content_hash)
            if origin_key in known:
                continue
            if (not isinstance(evidence_id, str) or not evidence_id or len(evidence_id) > 100
                    or not isinstance(source, str) or not source.startswith("https://")
                    or not isinstance(content, str) or not isinstance(content_hash, str)
                    or not _HASH.fullmatch(content_hash)
                    or hashlib.sha256(content.encode("utf-8")).hexdigest() != content_hash
                    or isinstance(version, bool) or not isinstance(version, int) or version < 0
                    or _source_payload(content, source) is None):
                continue
            local_id = "peer-" + hashlib.sha256(
                "\0".join((group_id, instance_id, evidence_id, content_hash)).encode("utf-8")
            ).hexdigest()[:24]
            origin = {
                "group_id": group_id,
                "instance_id": instance_id,
                "application_head": application_head,
                "record_version": peer_version,
                "evidence_id": evidence_id,
                "evidence_version": version,
                "content_sha256": content_hash,
            }
            engine.store.append("observation", {
                "id": local_id,
                "source": source,
                "content": content,
                "actor": "collector",
                "scope": "collected",
                "peer_origin": origin,
            })
            imported.append(local_id)
            known.add(origin_key)
    return imported
