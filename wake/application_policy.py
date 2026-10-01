"""
WAKE application policy above the reusable sudofx kernel.

This module owns WAKE-specific proposal normalization and deterministic domain
policy that must be identical whether the legacy Engine or the sudofx
ApplicationHost is driving a turn. It performs no durable writes.
"""

from __future__ import annotations

from .governance import Rejected, bob_reflection_due_cycle, require, transition


def rotation_preflight(state, invocation, proposal):
    """Salvage the selected-topic subset of a mixed Attention proposal."""
    if not isinstance(proposal, dict) or not isinstance(proposal.get("actions"), list):
        return proposal, None
    directive = state.get("invocations", {}).get(invocation, {}).get("attention", {})
    if not directive.get("enforce_selected_topic") or not directive.get("selected_topic"):
        return proposal, None

    selected = directive["selected_topic"]
    projects = state.get("projects", {})
    project_domains = {pid: item.get("domain") for pid, item in projects.items()}
    for action in proposal["actions"]:
        if isinstance(action, dict) and action.get("type") == "project":
            if action.get("id") and action.get("domain"):
                project_domains[action["id"]] = action["domain"]

    kept, withheld = [], []
    for action in proposal["actions"]:
        if not isinstance(action, dict):
            kept.append(action)
            continue
        kind = action.get("type")
        keep = True
        if kind == "project":
            old = projects.get(action.get("id"))
            keep = bool(
                (old and action.get("status") in ("parked", "completed"))
                or action.get("domain") == selected
            )
        elif kind == "research":
            keep = action.get("domain") == selected
        elif kind in ("notebook", "reframe"):
            keep = project_domains.get(action.get("project")) == selected
        elif kind == "blog":
            due_cycle = bob_reflection_due_cycle(state)
            keep = (
                action.get("reflection_cycle") == due_cycle
                if due_cycle is not None
                else project_domains.get(action.get("project")) == selected
            )
        elif kind in ("belief", "commit", "resolve"):
            keep = False
        if keep:
            kept.append(action)
        else:
            withheld.append(action)

    active = [project for project in projects.values() if project.get("status") == "active"]
    selected_activation = any(
        isinstance(action, dict)
        and action.get("type") == "project"
        and action.get("status") == "active"
        and action.get("domain") == selected
        and not (projects.get(action.get("id")) or {}).get("status") == "active"
        for action in kept
    )
    already_parking = {
        action.get("id")
        for action in kept
        if isinstance(action, dict)
        and action.get("type") == "project"
        and action.get("status") == "parked"
        and action.get("id") in projects
    }
    if selected_activation and len(active) >= 3 and not already_parking:
        configured = {
            topic["id"]
            for topic in state.get("research_topics", [])
            if topic.get("enabled", True)
        }
        blocked = set(directive.get("capability_blocked_topics", []))
        candidates = [project for project in active if project.get("domain") != selected]
        candidates.sort(
            key=lambda project: (
                0
                if project.get("domain") not in configured
                else 1
                if project.get("domain") in blocked
                else 2,
                project.get("updated_version", 0),
                project.get("id", ""),
            )
        )
        if candidates:
            old = candidates[0]
            kept.insert(
                0,
                {
                    "type": "project",
                    "id": old["id"],
                    "title": old["title"],
                    "question": old["question"],
                    "domain": old["domain"],
                    "status": "parked",
                    "next_step": old["next_step"],
                    "reason": (
                        "Deterministic Attention capacity recovery: park this "
                        f"non-selected project so {selected} work can proceed."
                    ),
                },
            )

    if not withheld and kept == proposal["actions"]:
        return proposal, None
    if not kept:
        return proposal, None

    label = next(
        (
            topic.get("label")
            for topic in state.get("research_topics", [])
            if topic.get("id") == selected
        ),
        selected,
    )
    normalized = {
        **proposal,
        "title": f"Advancing {label} under enforced rotation",
        "summary": (
            f"Attention accepted the valid {selected} subset of a mixed provider "
            f"proposal and withheld {len(withheld)} off-topic or administrative "
            "action(s). The exact provider response remains preserved in history."
        ),
        "actions": kept,
    }
    return normalized, {
        "selected_topic": selected,
        "withheld_count": len(withheld),
        "withheld_actions": withheld,
        "inserted_capacity_park": bool(
            kept
            and isinstance(kept[0], dict)
            and kept[0].get("type") == "project"
            and kept[0].get("status") == "parked"
            and kept[0] not in proposal["actions"]
        ),
    }


def assign_research_ids(proposal, invocation):
    """Assign durable research identities inside WAKE, never in provider output."""
    if not isinstance(proposal, dict) or not isinstance(proposal.get("actions"), list):
        return proposal
    actions = []
    for index, action in enumerate(proposal["actions"], start=1):
        if isinstance(action, dict) and action.get("type") == "research":
            action = {key: value for key, value in action.items() if key != "id"}
            action["id"] = f"research-{invocation}-{index}"
        actions.append(action)
    return {**proposal, "actions": actions}


def enforce_bob_opening_checkpoint(state, invocation, proposal):
    """Keep Bob's first-post obligation at the WAKE application boundary."""
    if not state.get("charter") or state.get("posts"):
        return
    invocation_state = state.get("invocations", {}).get(invocation, {})
    if not invocation_state.get("charged"):
        return
    due_cycle = bob_reflection_due_cycle(state)
    actions = proposal.get("actions") if isinstance(proposal, dict) else None
    require(
        isinstance(actions, list)
        and bool(actions)
        and isinstance(actions[-1], dict)
        and actions[-1].get("type") == "blog"
        and actions[-1].get("reflection_cycle") == due_cycle,
        f"Bob opening post for accepted wake {due_cycle} is mandatory before live research may advance",
    )


def govern_proposal(state, invocation, proposal):
    """Apply the complete WAKE domain-policy path without committing storage."""
    proposal, rotation_filter = rotation_preflight(state, invocation, proposal)
    proposal = assign_research_ids(proposal, invocation)
    enforce_bob_opening_checkpoint(state, invocation, proposal)
    editorial = None
    try:
        result = transition(state, proposal, invocation)
    except Rejected as exc:
        actions = proposal.get("actions") if isinstance(proposal, dict) else None
        if not (
            state.get("charter")
            and isinstance(actions, list)
            and 2 <= len(actions) <= 12
            and all(
                isinstance(action, dict) and action.get("type") != "blog"
                for action in actions[:-1]
            )
            and isinstance(actions[-1], dict)
            and actions[-1].get("type") == "blog"
        ):
            raise
        accepted_proposal = {**proposal, "actions": actions[:-1]}
        transition(state, accepted_proposal, invocation)
        editorial = {
            "status": "withheld",
            "reason": str(exc)[:1000],
            "action": actions[-1],
        }
        accepted_proposal["summary"] = (
            proposal["summary"][:2100]
            + "\n\nEditorial note: the proposed blog post was withheld. "
            + str(exc)[:180]
        )
        proposal = accepted_proposal
        result = transition(state, proposal, invocation)
    return proposal, result, editorial, rotation_filter


# Temporary compatibility alias while downstream tests/importers migrate.
_rotation_preflight = rotation_preflight
