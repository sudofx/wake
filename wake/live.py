"""Disposable public projection for the WAKE✳︎ browser.

sudofx SQLite on wake-state is authoritative. This module deliberately produces a
bounded, replaceable view for the public UI; nothing here is read back into
governance, recovery, or provider context.
"""

from copy import deepcopy
from datetime import datetime, timezone

from sudofx.observability import build_application_observability

from .matrix import MATRIX


LIVE_SCHEMA = 1
MAX_EVENTS = 400
MAX_EVIDENCE_TEXT = 2400


def _clip(value, limit=MAX_EVIDENCE_TEXT):
    if isinstance(value, str):
        return value if len(value) <= limit else value[:limit] + "…"
    if isinstance(value, list):
        return [_clip(item, limit) for item in value]
    if isinstance(value, dict):
        return {key: _clip(item, limit) for key, item in value.items()}
    return value


def _compact_invocation(item):
    """Keep browser telemetry/provenance fields without provider request bodies."""
    allowed = (
        "id", "time", "finished", "status", "reason", "provider", "model",
        "successful_model", "provider_attempts", "provider_requests_sent",
        "quota_day", "inquiry_drive_shadow", "provider_error", "charged",
        "temporal", "context_delivery", "working_set_metrics",
    )
    return {key: deepcopy(item[key]) for key in allowed if key in item}



def _full_history_metrics(store, state):
    """Return tiny aggregates from the store contract, never a concrete SQLite schema."""
    if hasattr(store, "history_metrics"):
        summary = store.history_metrics()
    else:
        from .history import history_metrics
        summary = history_metrics(store.events(), state)

    performance = store.performance_snapshot()
    return {
        "storage": {
            "sqlite_bytes": performance.get(
                "sudofx_database_bytes",
                store.path.stat().st_size if store.path.exists() else 0,
            ),
            "event_count": performance.get("event_count", len(store.events())),
        },
        **summary,
    }


def _application_access_metrics(store):
    """Expose only the public-safe state of the global application access latch."""
    source = store if hasattr(store, "application_access_state") else getattr(store, "record", None)
    if source is None or not hasattr(source, "application_access_state"):
        return None
    state = source.application_access_state()
    return {
        "enabled": bool(state.enabled),
        "generation": int(state.generation),
        "changed_at": state.changed_at,
    }


def _matrix_metrics(store):
    """Return compact public matrix telemetry without result bodies."""
    progress = (
        store.continuity_matrix_progress()
        if hasattr(store, "continuity_matrix_progress")
        else None
    )
    results = progress.get("results") or {} if isinstance(progress, dict) else {}
    counts = {"completed": 0, "failed": 0, "deferred": 0}
    status_by_coordinate = {}
    for coordinate_id, result in results.items():
        status = result.get("status") if isinstance(result, dict) else None
        if status in counts:
            counts[status] += 1
            status_by_coordinate[coordinate_id] = status

    axes = [
        {
            "key": axis.key,
            "label": axis.label,
            "values": [{"key": value.key, "label": value.label} for value in axis.values],
        }
        for axis in MATRIX.axes
    ]
    cells = [
        status_by_coordinate.get(coordinate.coordinate_id, "open")
        for coordinate in MATRIX.coordinates()
    ]
    next_coordinate_id = (
        progress.get("next_coordinate_id")
        if isinstance(progress, dict)
        else None
    )
    next_ordinal = None
    if isinstance(next_coordinate_id, str):
        try:
            next_ordinal = MATRIX.coordinate_by_id(next_coordinate_id).ordinal
        except ValueError:
            next_ordinal = None

    return {
        "enabled": isinstance(progress, dict),
        "matrix": progress.get("matrix") if isinstance(progress, dict) else f"{MATRIX.matrix_id}@{MATRIX.version}",
        "definition_digest": (
            progress.get("definition_digest")
            if isinstance(progress, dict)
            else MATRIX.definition_digest
        ),
        "cell_count": (
            progress.get("cell_count")
            if isinstance(progress, dict)
            else MATRIX.cell_count
        ),
        "completed_count": (
            progress.get("completed_count")
            if isinstance(progress, dict)
            else 0
        ),
        "next_ordinal": next_ordinal,
        "status_counts": counts,
        "axes": axes,
        "cells": cells,
    }

def build_live_projection(store, operation=None, runtime_ref=""):
    """Build one bounded public-safe snapshot from already-verified SQLite state."""
    state, head = store.projection()
    public_state = deepcopy(state)

    public_state["invocations"] = {
        key: _compact_invocation(value)
        for key, value in state.get("invocations", {}).items()
    }
    public_state["evidence"] = {
        key: {**deepcopy(value), "content": _clip(value.get("content"))}
        for key, value in state.get("evidence", {}).items()
    }
    # Journal rows are already compact, but only recent browser history needs to
    # travel on every cycle. The authoritative database retains the full record.
    public_state["journal"] = list(state.get("journal", []))[-160:]

    performance = store.performance_snapshot()
    if performance.get("authority") == "sudofx":
        source = {
            "authority": "sudofx SQLite",
            "branch": "wake-state",
            "database": "sudofx.sqlite",
            "head": head,
            "runtime_ref": runtime_ref,
        }
    else:
        source = {
            "authority": "legacy WAKE SQLite",
            "branch": None,
            "database": "wake.sqlite3",
            "head": head,
            "runtime_ref": runtime_ref,
        }

    return {
        "projection_schema": LIVE_SCHEMA,
        "projection_kind": "disposable-live-view",
        "authoritative": False,
        "source": source,
        "state": public_state,
        "events": store.tail_events_all(MAX_EVENTS),
        "head": head,
        "generated": datetime.now(timezone.utc).isoformat(),
        "experiment": None,
        "timezone": "America/Los_Angeles",
        "operation": deepcopy(operation),
        "wake_status": deepcopy((operation or {}).get("wake_status", {})),
        "metrics": _full_history_metrics(store, state),
        "application_observability": build_application_observability(store.record) if hasattr(store, "record") else None,
        "application_access": _application_access_metrics(store),
        "matrix_progress": _matrix_metrics(store),
    }
