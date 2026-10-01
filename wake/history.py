"""Bounded historical projections shared by legacy and sudofx-backed WAKE stores."""

from __future__ import annotations

from copy import deepcopy


MAX_COMPATIBILITY_EVENTS = 400
TEMPORAL_KINDS = (
    "accepted",
    "rejected",
    "failed",
    "observation",
    "research_collected",
    "attention_assessed",
    "squirrel_assessed",
)


def history_metrics(events, state):
    """Derive the stable public aggregate metrics from verified WAKE events."""
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
        project_id = action.get("project") or (
            action.get("id") if action.get("type") == "project" else None
        )
        project_topic = projects.get(project_id, {}).get("domain") if project_id else None
        return project_topic if project_topic in topics else None

    for event in events:
        if not isinstance(event, dict):
            continue
        kind = event.get("kind")
        payload = event.get("payload", {})
        if kind == "rejected":
            reason = str(payload.get("reason") or "Unspecified rejection").split(":")[0][:90]
            rejection_reasons[reason] = rejection_reasons.get(reason, 0) + 1
            continue
        if kind != "accepted":
            continue
        accepted_events += 1
        proposal = payload.get("proposal", {}) if isinstance(payload, dict) else {}
        for action in proposal.get("actions", []) if isinstance(proposal, dict) else []:
            if not isinstance(action, dict):
                continue
            action_type = action.get("type") or "unknown"
            action_counts[action_type] = action_counts.get(action_type, 0) + 1
            topic = topic_for(action)
            target = topic_counts.setdefault(topic, {}) if topic else system_counts
            target[action_type] = target.get(action_type, 0) + 1

    return {
        "accepted_events": accepted_events,
        "accepted_actions": {
            "total": sum(action_counts.values()),
            "by_type": action_counts,
            "by_topic": {
                topic: {"total": sum(counts.values()), "by_type": counts}
                for topic, counts in topic_counts.items()
            },
            "unattributed": {
                "total": sum(system_counts.values()),
                "by_type": system_counts,
            },
            "belief_actions": action_counts.get("belief", 0),
        },
        "rejection_reasons": rejection_reasons,
    }


def merge_history_metrics(base, delta):
    """Add post-migration aggregates to one frozen import baseline."""
    result = deepcopy(base)
    result["accepted_events"] = int(result.get("accepted_events", 0)) + int(delta.get("accepted_events", 0))
    result.setdefault("rejection_reasons", {})
    for reason, count in delta.get("rejection_reasons", {}).items():
        result["rejection_reasons"][reason] = result["rejection_reasons"].get(reason, 0) + count

    left = result.setdefault("accepted_actions", {})
    right = delta.get("accepted_actions", {})
    left["total"] = int(left.get("total", 0)) + int(right.get("total", 0))
    left["belief_actions"] = int(left.get("belief_actions", 0)) + int(right.get("belief_actions", 0))
    for key in ("by_type",):
        left.setdefault(key, {})
        for name, count in right.get(key, {}).items():
            left[key][name] = left[key].get(name, 0) + count
    left.setdefault("unattributed", {"total": 0, "by_type": {}})
    right_unattributed = right.get("unattributed", {})
    left["unattributed"]["total"] = int(left["unattributed"].get("total", 0)) + int(right_unattributed.get("total", 0))
    left["unattributed"].setdefault("by_type", {})
    for name, count in right_unattributed.get("by_type", {}).items():
        left["unattributed"]["by_type"][name] = left["unattributed"]["by_type"].get(name, 0) + count

    left.setdefault("by_topic", {})
    for topic, summary in right.get("by_topic", {}).items():
        target = left["by_topic"].setdefault(topic, {"total": 0, "by_type": {}})
        target["total"] = int(target.get("total", 0)) + int(summary.get("total", 0))
        target.setdefault("by_type", {})
        for name, count in summary.get("by_type", {}).items():
            target["by_type"][name] = target["by_type"].get(name, 0) + count
    return result


def migration_baseline(events, state):
    """Capture only the legacy history facts required after authority cutover."""
    anchor = (state.get("temporal") or {}).get(
        "anchor_seq",
        (state.get("experimental") or {}).get("event_seq", len(events)),
    )
    if isinstance(anchor, bool) or not isinstance(anchor, int) or anchor < 0:
        anchor = len(events)
    suffix = [event for event in events if event.get("seq", 0) > anchor]
    counts = {}
    for event in suffix:
        kind = event.get("kind")
        if isinstance(kind, str):
            counts[kind] = counts.get(kind, 0) + 1
    return {
        "recent_events": deepcopy(events[-MAX_COMPATIBILITY_EVENTS:]),
        "temporal_anchor_seq": anchor,
        "temporal_suffix": {
            "total": len(suffix),
            "kinds": counts,
        },
        "history_metrics": history_metrics(events, state),
    }
