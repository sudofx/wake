"""Disposable public projection for the WAKE✳︎ browser.

SQLite on wake-state is authoritative. This module deliberately produces a
bounded, replaceable view for the public UI; nothing here is read back into
governance, recovery, or provider context.
"""

from copy import deepcopy
from datetime import datetime, timezone


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
    )
    return {key: deepcopy(item[key]) for key in allowed if key in item}



def _full_history_metrics(store, state):
    """Return tiny aggregates derived from the full authoritative event record."""
    action_counts = {}
    topic_counts = {}
    system_counts = {}
    rejection_reasons = {}
    accepted_events = 0

    topics = {item.get("id") for item in state.get("research_topics", []) if item.get("id")}
    projects = state.get("projects", {})

    def topic_for(action):
        topic = action.get("domain")
        if topic in topics:
            return topic
        project_id = action.get("project") or (action.get("id") if action.get("type") == "project" else None)
        project_topic = projects.get(project_id, {}).get("domain") if project_id else None
        return project_topic if project_topic in topics else None

    events = store.events()
    for event in events:
        kind = event.get("kind")
        if kind not in {"accepted", "rejected"}:
            continue
        payload = event.get("payload", {})
        if kind == "rejected":
            reason = str(payload.get("reason") or "Unspecified rejection").split(":")[0][:90]
            rejection_reasons[reason] = rejection_reasons.get(reason, 0) + 1
            continue

        accepted_events += 1
        for action in payload.get("proposal", {}).get("actions", []):
            action_type = action.get("type") or "unknown"
            action_counts[action_type] = action_counts.get(action_type, 0) + 1
            topic = topic_for(action)
            target = topic_counts.setdefault(topic, {}) if topic else system_counts
            target[action_type] = target.get(action_type, 0) + 1

    topic_summary = {}
    for topic, counts in topic_counts.items():
        topic_summary[topic] = {"total": sum(counts.values()), "by_type": counts}

    return {
        "storage": {
            "sqlite_bytes": store.performance_snapshot().get(
                "sudofx_database_bytes",
                store.path.stat().st_size if store.path.exists() else 0,
            ),
            "event_count": len(events),
        },
        "accepted_events": accepted_events,
        "accepted_actions": {
            "total": sum(action_counts.values()),
            "by_type": action_counts,
            "by_topic": topic_summary,
            "unattributed": {
                "total": sum(system_counts.values()),
                "by_type": system_counts,
            },
            "belief_actions": action_counts.get("belief", 0),
        },
        "rejection_reasons": rejection_reasons,
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
    source = {
        "authority": "SQLite",
        "branch": "wake-state",
        "database": "data/wake.sqlite3",
        "head": head,
        "runtime_ref": runtime_ref,
    }
    if performance.get("authority") == "sudofx":
        source.update(
            authority="sudofx SQLite",
            database="sudofx.sqlite",
        )

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
    }
