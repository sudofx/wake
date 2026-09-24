"""Deterministic, durable attention recovery for the research charter.

Squirrel does not alter projects or governance. It tracks two independent forms
of fixation: repeated hard rejection without progress, and productive saturation
when accepted attention stays on one topic for too many accepted wakes. Either
condition temporarily defers that topic while preserving its durable work.
"""

import json


HARD_REJECTION_THRESHOLD = 5
ATTENTION_SATURATION_THRESHOLD = 5
COOLDOWN_OTHER_ATTEMPTS = 3


def _active_topic(state):
    """Select the current topic from durable project state, never model prose."""
    active = [p for p in state.get("projects", {}).values() if p.get("status") == "active"]
    if active:
        return sorted(active, key=lambda p: (-p.get("updated_version", 0), p["id"]))[0]["domain"]
    topics = state.get("research_topics", [])
    return topics[0]["id"] if topics else None


def _has_new_topic_evidence(state, topic, item):
    """Only blocker/rejection cooldowns may end early when new evidence arrives."""
    # Productive saturation is an attention intervention, not an evidence
    # shortage. Fresh evidence must not immediately pull attention back to the
    # same fertile topic; saturation always earns the full other-topic cooldown.
    if item.get("cause") == "attention_saturation":
        return False
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


def _proposal_attention_topic(state, selected, proposal):
    """Infer the topic actually advanced by an accepted proposal.

    The selected Squirrel topic remains authoritative for rejected attempts, but
    accepted work may legitimately contain durable actions on another configured
    topic. Saturation should follow what was actually advanced, not merely what
    the temporary directive requested.
    """
    topics = []
    for action in (proposal or {}).get("actions", []):
        domain = action.get("domain")
        if domain:
            topics.append(domain)
        project_id = action.get("project")
        project = state.get("projects", {}).get(project_id)
        if project and project.get("domain"):
            topics.append(project["domain"])
    return topics[-1] if topics else selected


def _parked_projects(state, topic):
    return [{"id": p["id"], "question": p["question"], "next_step": p["next_step"]}
            for p in state.get("projects", {}).values()
            if p.get("domain") == topic and p.get("status") == "active"]


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
        "attention_saturation_threshold": ATTENTION_SATURATION_THRESHOLD,
        "attention": squirrel.get("attention", {}),
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
    attention_topic = _proposal_attention_topic(state, selected, proposal) if terminal == "accepted" else selected
    attempt_topic = attention_topic or selected
    restored = []

    # Every terminal attempt on another topic advances a deferred topic's
    # cooldown. Eligibility is restored as a receipt, never by deleting work.
    for topic, item in list(deferred.items()):
        if attempt_topic and attempt_topic != topic:
            item["other_topic_attempts"] = item.get("other_topic_attempts", 0) + 1
        early_evidence = _has_new_topic_evidence(state, topic, item)
        if item.get("other_topic_attempts", 0) >= COOLDOWN_OTHER_ATTEMPTS or early_evidence:
            restored.append(topic)
            del deferred[topic]

    progress = False
    if terminal == "accepted" and selected and proposal:
        for action in proposal.get("actions", []):
            # A notebook or fulfilled obligation is durable advancement. A
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
    hard_rejection_triggered = False
    if selected and progress:
        # Progress clears only the failure counter. It does not erase how long
        # attention has remained on one productive topic.
        counters[selected] = 0
    elif selected and hard_rejection:
        counters[selected] = counters.get(selected, 0) + 1
        if counters[selected] >= HARD_REJECTION_THRESHOLD and selected not in deferred:
            deferred[selected] = {
                "deferred_by": invocation,
                "cause": "hard_rejection",
                "reason": "five consecutive hard rejections without durable progress",
                "other_topic_attempts": 0,
                "eligible_after_other_attempts": COOLDOWN_OTHER_ATTEMPTS,
                "parked_projects": _parked_projects(state, selected),
            }
            hard_rejection_triggered = True

    prior_attention = prior.get("attention", {})
    attention = dict(prior_attention)
    saturation_triggered = False
    if terminal == "accepted" and attention_topic:
        streak = (prior_attention.get("accepted_streak", 0) + 1
                  if prior_attention.get("topic") == attention_topic else 1)
        attention = {"topic": attention_topic, "accepted_streak": streak}
        if streak >= ATTENTION_SATURATION_THRESHOLD and attention_topic not in deferred:
            deferred[attention_topic] = {
                "deferred_by": invocation,
                "cause": "attention_saturation",
                "reason": "five accepted wakes concentrated on one topic; rotate attention despite progress",
                "other_topic_attempts": 0,
                "eligible_after_other_attempts": COOLDOWN_OTHER_ATTEMPTS,
                "parked_projects": _parked_projects(state, attention_topic),
            }
            saturation_triggered = True

    triggered = []
    if hard_rejection_triggered and selected:
        triggered.append(selected)
    if saturation_triggered and attention_topic and attention_topic not in triggered:
        triggered.append(attention_topic)

    return {
        "invocation": invocation, "terminal": terminal, "selected_topic": selected,
        "attention_topic": attention_topic, "hard_rejection": hard_rejection,
        "durable_progress": progress, "attention": attention,
        "attention_saturation_triggered": saturation_triggered,
        "counters": counters, "deferred": deferred, "restored_topics": restored,
        "triggered_topics": triggered,
    }
