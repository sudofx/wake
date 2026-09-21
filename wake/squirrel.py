"""Deterministic, durable attention recovery for the research charter.

Squirrel does not alter projects or governance.  It records when a topic has
reached five attributable hard rejections, then gives another configured topic
three turns of attention before the deferred topic is eligible again.
"""

import json


HARD_REJECTION_THRESHOLD = 5
COOLDOWN_OTHER_ATTEMPTS = 3


def _active_topic(state):
    """Select the current topic from durable project state, never model prose."""
    active = [p for p in state.get("projects", {}).values() if p.get("status") == "active"]
    if active:
        return sorted(active, key=lambda p: (-p.get("updated_version", 0), p["id"]))[0]["domain"]
    topics = state.get("research_topics", [])
    return topics[0]["id"] if topics else None


def _has_new_topic_evidence(state, topic, item):
    """Only trusted, collected evidence can end a cooldown early."""
    deferred_version = state.get("invocations", {}).get(item.get("deferred_by"), {}).get("base_version", -1)
    for evidence in state.get("evidence", {}).values():
        if evidence.get("actor") != "collector" or evidence.get("scope") != "collected":
            continue
        if evidence.get("version", -1) <= deferred_version:
            continue
        try:
            if json.loads(evidence.get("content", "{}")).get("topic_domain") == topic:
                return True
        except (TypeError, ValueError):
            pass
    return False


def plan(state):
    """Return the deterministic attention directive for the next provider request."""
    if not state.get("charter"):
        return {"active": False}
    squirrel = state.get("squirrel", {})
    deferred = squirrel.get("deferred", {})
    topics = [t["id"] for t in state.get("research_topics", [])]
    current = _active_topic(state)
    eligible = [topic for topic in topics
                if topic not in deferred or _has_new_topic_evidence(state, topic, deferred[topic])]
    selected = current if current in eligible else (eligible[0] if eligible else current)
    return {
        "active": True,
        "selected_topic": selected,
        "deferred_topics": sorted(deferred),
        "parked": {topic: deferred[topic].get("parked_projects", []) for topic in sorted(deferred)},
        "hard_rejection_threshold": HARD_REJECTION_THRESHOLD,
        "cooldown_other_attempts": COOLDOWN_OTHER_ATTEMPTS,
        "reason": ("alternate configured topic selected during Squirrel cooldown"
                   if selected != current else "current durable project topic remains eligible"),
    }


def assessment(state, invocation, terminal, proposal=None):
    """Build a replayable receipt after an invocation reaches a terminal state."""
    prior = state.get("squirrel", {})
    counters = dict(prior.get("counters", {}))
    deferred = {key: dict(value) for key, value in prior.get("deferred", {}).items()}
    selected = state["invocations"][invocation].get("squirrel", {}).get("selected_topic")
    restored = []

    # Every terminal attempt on another topic advances a deferred topic's
    # cooldown.  Eligibility is restored as a receipt, never by deleting work.
    for topic, item in list(deferred.items()):
        if selected and selected != topic:
            item["other_topic_attempts"] = item.get("other_topic_attempts", 0) + 1
        early_evidence = _has_new_topic_evidence(state, topic, item)
        if item.get("other_topic_attempts", 0) >= COOLDOWN_OTHER_ATTEMPTS or early_evidence:
            restored.append(topic)
            del deferred[topic]

    progress = False
    if terminal == "accepted" and selected and proposal:
        for action in proposal.get("actions", []):
            # A notebook or fulfilled obligation is durable advancement.  A
            # project update advances only when it changes its next step.
            if action.get("type") == "notebook":
                project = state.get("projects", {}).get(action.get("project"), {})
                progress |= project.get("domain") == selected
            elif action.get("type") == "resolve":
                progress = True
            elif action.get("type") == "project":
                old = state.get("projects", {}).get(action.get("id"), {})
                progress |= old.get("domain") == selected and old.get("next_step") != action.get("next_step")

    hard_rejection = terminal == "rejected" and bool(selected)
    if selected and progress:
        counters[selected] = 0
    elif selected and hard_rejection:
        counters[selected] = counters.get(selected, 0) + 1
        if counters[selected] >= HARD_REJECTION_THRESHOLD and selected not in deferred:
            projects = [project for project in state.get("projects", {}).values()
                        if project.get("domain") == selected and project.get("status") == "active"]
            deferred[selected] = {
                "deferred_by": invocation,
                "reason": "five consecutive hard rejections without durable progress",
                "other_topic_attempts": 0,
                "eligible_after_other_attempts": COOLDOWN_OTHER_ATTEMPTS,
                # This is a compact preservation receipt, not a project edit:
                # Squirrel leaves unresolved work intact while attention moves.
                "parked_projects": [{"id": p["id"], "question": p["question"],
                                     "next_step": p["next_step"]} for p in projects],
            }

    return {
        "invocation": invocation, "terminal": terminal, "selected_topic": selected,
        "hard_rejection": hard_rejection, "durable_progress": progress,
        "counters": counters, "deferred": deferred, "restored_topics": restored,
        "triggered_topics": [selected] if selected in deferred and hard_rejection
                             and counters.get(selected) == HARD_REJECTION_THRESHOLD else [],
    }
