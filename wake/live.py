"""Disposable public projection for the WAKE✳︎ browser.

Each container record is authoritative for its node; public projections never seed
or repair it. This module deliberately produces a
bounded, replaceable view for the public UI; nothing here is read back into
governance, recovery, or provider context.
"""

from copy import deepcopy
from datetime import datetime, timezone

from wake.kernel.observability import build_application_observability


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
        "quota_day", "inquiry_drive_shadow", "provider_error", "charged", "origin", "origins",
        "phase", "checkpoint", "editorial_checkpoint", "input_digest", "quota_exhausted",
    )
    return {key: deepcopy(item[key]) for key in allowed if key in item}


def browser_projection(data):
    """Bound the overview transport; complete exported history stays separate."""
    from .installation_cli import _public_projection
    state = dict(data['state'])
    state['invocations'] = {key: _compact_invocation(value)
                            for key, value in state.get('invocations', {}).items()}
    state['evidence'] = {key: {**value, 'content': _clip(value.get('content'))}
                        for key, value in state.get('evidence', {}).items()}
    events = data.get('events', [])
    return _public_projection({**data, 'state': state, 'events': events[-MAX_EVENTS:],
        'event_history': {'displayed': min(len(events), MAX_EVENTS),
                          'total': data.get('event_history', {}).get('total', len(events)),
                          'complete_url': 'events.jsonl'}})


def installation_overview(research):
    """Only fields consumed by the installation comparison, never its full graph."""
    return {**{key: research.get(key) for key in ('head', 'version', 'generated', 'status', 'metrics')},
            'activity': research.get('activity', [])[:12],
            'wakes': [{key: item.get(key) for key in ('id', 'receipt')}
                      for item in research.get('wakes', [])[:12]],
            'matrix': {key: research.get('matrix', {}).get(key) for key in ('enabled', 'completed')}}



def _full_history_metrics(store, state, events=None):
    """Return tiny aggregates from the store contract, never a concrete SQLite schema."""
    if events is not None:
        from .history import history_metrics
        summary = history_metrics(events, state)
    elif hasattr(store, "history_metrics"):
        summary = store.history_metrics()
    else:
        from .history import history_metrics
        summary = history_metrics(store.events(), state)

    performance = store.performance_snapshot()
    return {
        "storage": {
            "sqlite_bytes": performance.get(
                "wake_database_bytes",
                store.path.stat().st_size if store.path.exists() else 0,
            ),
            "event_count": (performance["event_count"] if "event_count" in performance
                            else len(events) if events is not None else len(store.events())),
        },
        **summary,
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
    if performance.get("authority") == "wake":
        source = {
            "authority": "wake SQLite",
            "branch": None,
            "database": "wake.sqlite",
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

    metrics = _full_history_metrics(store, state)
    from .research_projection import build_research_projection
    generated = datetime.now(timezone.utc).isoformat()
    research = build_research_projection(
        state, store.tail_events_all(MAX_EVENTS), head, metrics=metrics,
        operation=operation, source=source, generated=generated,
        matrix_reported=hasattr(store, "continuity_matrix_progress"),
        matrix_progress=store.continuity_matrix_progress() if hasattr(store, "continuity_matrix_progress") else None,
    )
    return {
        "projection_schema": LIVE_SCHEMA,
        "projection_kind": "disposable-live-view",
        "authoritative": False,
        "source": source,
        "state": public_state,
        "events": store.tail_events_all(MAX_EVENTS),
        "head": head,
        "generated": generated,
        "experiment": None,
        "timezone": "America/Los_Angeles",
        "operation": deepcopy(operation),
        "wake_status": deepcopy((operation or {}).get("wake_status", {})),
        "metrics": metrics,
        "research": research,
        "application_observability": build_application_observability(store.record) if hasattr(store, "record") else None,
    }
