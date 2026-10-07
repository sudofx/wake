"""
WAKE application policy above the reusable wake kernel.

This module owns WAKE-specific proposal normalization and deterministic domain
policy that must be identical whether a deliberate legacy compatibility
fixture or the wake ApplicationHost is driving a turn. It performs no durable writes.
"""

from __future__ import annotations

import re

from .governance import Rejected, bob_reflection_due_cycle, require, transition


def _question_key(value):
    """Use the same conservative question identity as forward governance."""
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").casefold()).strip()



def _blog_title_key(value):
    """Normalize public titles the same way governance compares them."""
    return " ".join(str(value or "").split()).casefold()


def _journal_action_sentence(action):
    """Render one accepted non-blog action in WAKE✳︎'s institutional journal voice."""
    kind = action.get("type")
    if kind == "project":
        title = str(action.get("title") or action.get("id") or "project").strip()
        status = str(action.get("status") or "updated").strip()
        next_step = str(action.get("next_step") or "").strip()
        return (
            f'Project "{title}" is {status}.'
            + (f" Next step: {next_step}." if next_step else "")
        )
    if kind == "research":
        project = str(action.get("project") or "unscoped").strip()
        query = str(action.get("query") or "").strip()
        return f"Queued research for project {project}" + (f": {query}." if query else ".")
    if kind == "notebook":
        title = str(action.get("title") or action.get("id") or "notebook").strip()
        project = str(action.get("project") or "unscoped").strip()
        return f'Updated notebook "{title}" for project {project}.'
    if kind == "reframe":
        project = str(action.get("project") or "unscoped").strip()
        return f"Updated the research frame for project {project}."
    if kind == "belief":
        identifier = str(action.get("id") or "belief").strip()
        status = str(action.get("status") or "updated").strip()
        return f"Belief {identifier} is {status}."
    if kind == "commit":
        identifier = str(action.get("id") or "commitment").strip()
        task = str(action.get("task") or "").strip()
        return f"Recorded commitment {identifier}" + (f": {task}." if task else ".")
    if kind == "resolve":
        identifier = str(action.get("id") or "commitment").strip()
        return f"Resolved commitment {identifier} with governed evidence."
    return f"Accepted {kind or 'research'} action."


def materialize_due_bob_checkpoint_preflight(state, proposal):
    """Turn the required provider checkpoint into the ordinary final blog sidecar.

    The response schema requires bob_checkpoint only when Bob is due. Keeping
    it outside actions lets the provider contract require the editorial
    checkpoint without requiring or pruning any research action. This preflight
    then materializes it as the final blog action before the existing WAKE policy
    path runs.

    Publication still does not gate research. If the materialized blog later
    fails editorial governance, govern_proposal withholds only that final
    action and accepts the valid research subset. Because no post becomes durable,
    Bob remains due on the next wake.
    """
    if not isinstance(proposal, dict) or "bob_checkpoint" not in proposal:
        return proposal, None

    due_cycle = bob_reflection_due_cycle(state)
    checkpoint = proposal.get("bob_checkpoint")
    actions = proposal.get("actions")
    require(due_cycle is not None, "Bob checkpoint supplied when no checkpoint is due")
    require(isinstance(actions, list), "Bob checkpoint requires an actions array")
    require(
        isinstance(checkpoint, dict)
        and checkpoint.get("type") == "blog"
        and checkpoint.get("reflection_cycle") == due_cycle,
        "Bob checkpoint must be the due blog reflection for this wake",
    )

    # The due checkpoint has one canonical lane. If a provider somehow returns
    # an additional blog action despite the schema, discard that duplicate
    # editorial output rather than letting it jeopardize otherwise valid research.
    research_actions = [
        action
        for action in actions
        if not (isinstance(action, dict) and action.get("type") == "blog")
    ]
    discarded = len(actions) - len(research_actions)

    normalized = {
        key: value
        for key, value in proposal.items()
        if key != "bob_checkpoint"
    }
    normalized["actions"] = [*research_actions, checkpoint]
    return normalized, {
        "bob_checkpoint": {
            "due_cycle": due_cycle,
            "materialized": True,
            "discarded_duplicate_blog_actions": discarded,
        }
    }


def separate_blog_from_journal_preflight(proposal):
    """Keep Bob's publication persona mechanically outside WAKE✳︎'s journal.

    A provider turn may propose research actions and one Bob blog action together.
    The blog action is a separate public translation artifact. It must never supply
    the journal title/summary for the institutional research record.
    """
    if not isinstance(proposal, dict) or not isinstance(proposal.get("actions"), list):
        return proposal, None
    actions = proposal["actions"]
    if not any(isinstance(action, dict) and action.get("type") == "blog" for action in actions):
        return proposal, None

    research_actions = [
        action for action in actions
        if isinstance(action, dict) and action.get("type") != "blog"
    ]
    if research_actions:
        priority = ("notebook", "reframe", "research", "project", "belief", "resolve", "commit")
        primary = next(
            (action for kind in priority for action in research_actions if action.get("type") == kind),
            research_actions[0],
        )
        kind = primary.get("type")
        if kind == "notebook":
            title = f'Notebook updated · {primary.get("title") or primary.get("id") or "research"}'
        elif kind == "project":
            title = f'Project updated · {primary.get("title") or primary.get("id") or "research"}'
        elif kind == "research":
            title = f'Research queued · {primary.get("project") or "project"}'
        elif kind == "reframe":
            title = f'Research frame updated · {primary.get("project") or "project"}'
        elif kind == "belief":
            title = f'Belief updated · {primary.get("id") or "research"}'
        elif kind == "resolve":
            title = f'Commitment resolved · {primary.get("id") or "research"}'
        elif kind == "commit":
            title = f'Commitment recorded · {primary.get("id") or "research"}'
        else:
            title = "Research cycle accepted"
        summary = " ".join(_journal_action_sentence(action) for action in research_actions)
    else:
        title = "Research cycle checkpoint"
        summary = "No research actions changed the institutional research state in this cycle."

    normalized = {
        **proposal,
        "title": " ".join(str(title).split())[:120],
        "summary": " ".join(str(summary).split())[:2400],
    }
    return normalized, {
        "journal_blog_boundary": {
            "applied": True,
            "research_action_count": len(research_actions),
        }
    }


def freshen_duplicate_blog_titles_preflight(state, proposal):
    """Repair duplicate standalone Bob titles without blocking valid research.

    Title uniqueness is an editorial presentation invariant, not authority over
    the research transition. The provider's raw response remains preserved by
    the engine; this policy normalization changes only the governed proposal.
    Corrections keep their explicit title because supersession semantics matter.
    """
    if not isinstance(proposal, dict) or not isinstance(proposal.get("actions"), list):
        return proposal, None

    used = {
        _blog_title_key(post.get("title"))
        for post in state.get("posts", {}).values()
        if _blog_title_key(post.get("title"))
    }
    actions = []
    repairs = []
    for action in proposal["actions"]:
        if not (
            isinstance(action, dict)
            and action.get("type") == "blog"
            and not action.get("supersedes")
        ):
            actions.append(action)
            continue

        original = " ".join(str(action.get("title") or "").split())
        key = _blog_title_key(original)
        if key and key in used:
            marker = action.get("reflection_cycle") or (int(state.get("version") or 0) + 1)
            candidate = f"{original} — Wake {marker}"
            attempt = 2
            while _blog_title_key(candidate) in used:
                candidate = f"{original} — Wake {marker}.{attempt}"
                attempt += 1
            action = {**action, "title": candidate}
            repairs.append({"original": original, "replacement": candidate})
            key = _blog_title_key(candidate)

        if key:
            used.add(key)
        actions.append(action)

    if not repairs:
        return proposal, None

    summary = str(proposal.get("summary") or "")[:2050]
    normalized = {
        **proposal,
        "summary": (
            summary
            + "\n\nPolicy normalization: repaired duplicate Bob title(s) "
            + "without changing research content. The raw provider response remains preserved."
        )[:2400],
        "actions": actions,
    }
    return normalized, {"blog_title_repairs": repairs}


def reuse_owned_project_preflight(state, proposal):
    """Repair one exact duplicate-project alias without weakening project identity.

    A bounded fresh model can occasionally see a selected topic without seeing the
    unfinished durable project that already owns its seed question. If it recreates
    that exact question under a new ID, rejecting forever adds no information.

    This normalization is deliberately narrow: same configured domain, exact
    normalized question, exactly one unfinished owner, and a proposed active project.
    Completed or ambiguous matches still reach governance unchanged and fail closed.
    The existing project's immutable title/question/domain win, while same-proposal
    project references are rewritten to the durable ID. The raw provider response is
    still retained by the engine, so this repair remains auditable.
    """
    if not isinstance(proposal, dict) or not isinstance(proposal.get("actions"), list):
        return proposal, None

    projects = state.get("projects", {})
    aliases = {}
    reused = []
    normalized_actions = []

    for action in proposal["actions"]:
        if not isinstance(action, dict) or action.get("type") != "project":
            normalized_actions.append(action)
            continue
        proposed_id = action.get("id")
        if proposed_id in projects or action.get("status") != "active":
            normalized_actions.append(action)
            continue
        question_key = _question_key(action.get("question"))
        if not question_key:
            normalized_actions.append(action)
            continue
        matches = [
            project for project in projects.values()
            if project.get("domain") == action.get("domain")
            and project.get("status") in ("active", "parked")
            and _question_key(project.get("question")) == question_key
        ]
        if len(matches) != 1:
            normalized_actions.append(action)
            continue

        existing = matches[0]
        aliases[proposed_id] = existing["id"]
        normalized_actions.append({
            **action,
            "id": existing["id"],
            "title": existing["title"],
            "question": existing["question"],
            "domain": existing["domain"],
            "status": "active",
        })
        reused.append({
            "proposed_id": proposed_id,
            "existing_id": existing["id"],
            "domain": existing["domain"],
            "question_key": question_key,
        })

    if not aliases:
        return proposal, None

    rewritten = []
    for action in normalized_actions:
        if isinstance(action, dict) and action.get("project") in aliases:
            action = {**action, "project": aliases[action["project"]]}
        rewritten.append(action)

    note = "; ".join(
        f"{item['proposed_id']}→{item['existing_id']}"
        for item in reused
    )
    summary = str(proposal.get("summary") or "")[:2050]
    normalized = {
        **proposal,
        "summary": (
            summary
            + "\n\nPolicy normalization: reused the durable owner of an exact existing "
            + f"research question ({note}). The raw provider response remains preserved."
        )[:2400],
        "actions": rewritten,
    }
    return normalized, {"project_reuse": reused}


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


def enforce_synthesis_checkpoint(state, invocation, proposal):
    """Require live research to cross from collection into synthesis when ready.

    The provider may choose the notebook wording and claims, but it does not own
    the workflow transition. Once the exact delivered context says an active
    project has qualifying evidence and no usable notebook, another charged live
    wake may not advance without proposing a notebook for one of those projects.

    This uses the invocation's recorded request rather than recomputing eligibility
    after generation, so the rule is auditable against exactly what the disposable
    model was allowed to see.
    """
    if not state.get("charter"):
        return
    invocation_state = state.get("invocations", {}).get(invocation, {})
    if not invocation_state.get("charged"):
        return
    context = (invocation_state.get("request") or {}).get("context") or {}
    ready = {
        project_id
        for project_id in context.get("synthesis_ready_projects", [])
        if (state.get("projects", {}).get(project_id) or {}).get("status") == "active"
    }
    if not ready:
        return
    actions = proposal.get("actions") if isinstance(proposal, dict) else None
    require(
        isinstance(actions, list)
        and any(
            isinstance(action, dict)
            and action.get("type") == "notebook"
            and action.get("project") in ready
            for action in actions
        ),
        "Synthesis checkpoint requires a provisional notebook before more live research may advance",
    )


def govern_proposal(state, invocation, proposal):
    """Apply the complete WAKE domain-policy path without committing storage."""
    proposal, checkpoint_filter = materialize_due_bob_checkpoint_preflight(state, proposal)
    proposal, reuse_filter = reuse_owned_project_preflight(state, proposal)
    proposal, rotation_filter = rotation_preflight(state, invocation, proposal)
    proposal, title_filter = freshen_duplicate_blog_titles_preflight(state, proposal)
    proposal, journal_filter = separate_blog_from_journal_preflight(proposal)
    if checkpoint_filter or reuse_filter or title_filter or journal_filter:
        if rotation_filter is None:
            directive = state.get("invocations", {}).get(invocation, {}).get("attention", {})
            rotation_filter = {
                "selected_topic": directive.get("selected_topic"),
                "withheld_count": 0,
                "withheld_actions": [],
                "inserted_capacity_park": False,
            }
        if checkpoint_filter:
            rotation_filter = {**rotation_filter, **checkpoint_filter}
        if reuse_filter:
            rotation_filter = {**rotation_filter, **reuse_filter}
        if title_filter:
            rotation_filter = {**rotation_filter, **title_filter}
        if journal_filter:
            rotation_filter = {**rotation_filter, **journal_filter}
    proposal = assign_research_ids(proposal, invocation)
    enforce_synthesis_checkpoint(state, invocation, proposal)
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
        # Editorial withholding is recorded in the accepted event receipt.
        # It must not leak Bob's publication lifecycle into WAKE✳︎'s journal.
        proposal = accepted_proposal
        result = transition(state, proposal, invocation)
    return proposal, result, editorial, rotation_filter


# Temporary compatibility alias while downstream tests/importers migrate.
_rotation_preflight = rotation_preflight
