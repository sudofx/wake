# WAKE✳︎ MAINTAINER NOTE
#
# Builds the bounded working set delivered to a fresh invocation. Retrieval is an attention mechanism, not hidden model memory; changing it changes what can influence the next proposal.
#
# Comments in this file should explain WHY a constraint or step exists, not merely restate syntax.
# Preserve the boundary between disposable model proposals, deterministic authority, and durable history.
# If behavior and commentary disagree, investigate the tests and durable record rather than guessing intent.

"""Deterministic shadow planning for recoverable provenance.

This module does not retrieve evidence and does not change provider context.
It records which exact durable records WAKE would rehydrate if the shadow
working set became authoritative.
"""

from collections import Counter


TRIGGER_DESCRIPTIONS = {
    "excerpt_boundary": "A working abstraction is clipped and may hide a material distinction.",
    "belief_retracted": "A retracted belief deserves exact provenance when it remains cognitively relevant.",
    "notebook_revised": "A revised notebook has changed under new evidence and may require exact comparison.",
    "commitment_near_due": "An open commitment is approaching its due cycle.",
    "unincorporated_evidence": "Durable evidence exists that is not yet represented by a belief or notebook.",
}


def build_retrieval_shadow(state, working_set):
    """Return a bounded, deterministic plan for exact-record rehydration.

    The plan contains IDs and reasons only. It never copies evidence content into
    the working abstraction, never performs semantic contradiction detection, and
    never changes the live provider request.
    """
    candidates = []

    def add(trigger, record_kind, record_id, reason, evidence=()):
        candidates.append({
            "trigger": trigger,
            "record": {"kind": record_kind, "id": record_id},
            "reason": reason,
            "evidence": list(dict.fromkeys(evidence)),
        })

    shadow_beliefs = {
        item["id"]: item for item in working_set.get("beliefs", [])
    }

    for belief_id, belief in state.get("beliefs", {}).items():
        shadow = shadow_beliefs.get(belief_id, {})
        clipped = any(
            isinstance(shadow.get(field), str) and shadow[field].endswith("…")
            for field in ("claim", "why_retained")
        )
        if clipped:
            add(
                "excerpt_boundary",
                "belief",
                belief_id,
                TRIGGER_DESCRIPTIONS["excerpt_boundary"],
                belief.get("evidence", []),
            )
        if belief.get("status") == "retracted":
            add(
                "belief_retracted",
                "belief",
                belief_id,
                TRIGGER_DESCRIPTIONS["belief_retracted"],
                belief.get("evidence", []),
            )

    for notebook_id, notebook in state.get("notebooks", {}).items():
        if notebook.get("revision", 1) > 1:
            add(
                "notebook_revised",
                "notebook",
                notebook_id,
                TRIGGER_DESCRIPTIONS["notebook_revised"],
                notebook.get("evidence", []),
            )

    for commitment_id, commitment in state.get("commitments", {}).items():
        if (
            commitment.get("status") == "open"
            and commitment.get("due_cycle", 10**9) <= state.get("version", 0) + 2
        ):
            add(
                "commitment_near_due",
                "commitment",
                commitment_id,
                TRIGGER_DESCRIPTIONS["commitment_near_due"],
            )

    represented_evidence = set()
    for belief in state.get("beliefs", {}).values():
        represented_evidence.update(belief.get("evidence", []))
    for notebook in state.get("notebooks", {}).values():
        represented_evidence.update(notebook.get("evidence", []))

    # Keep this bounded and recent. These are candidates for semantic review,
    # not assertions that the evidence contradicts anything.
    unincorporated = [
        evidence_id
        for evidence_id, evidence in state.get("evidence", {}).items()
        if evidence_id not in represented_evidence
        and evidence.get("actor") != "runtime"
    ][-6:]
    for evidence_id in unincorporated:
        add(
            "unincorporated_evidence",
            "evidence",
            evidence_id,
            TRIGGER_DESCRIPTIONS["unincorporated_evidence"],
            [evidence_id],
        )

    trigger_counts = Counter(item["trigger"] for item in candidates)
    evidence_ids = list(dict.fromkeys(
        evidence_id
        for item in candidates
        for evidence_id in item["evidence"]
    ))

    return {
        "mode": "shadow",
        "principle": "Rehydrate exact records when an abstraction becomes expensive to trust.",
        "candidates": candidates,
        "evidence_ids": evidence_ids,
        "metrics": {
            "candidate_count": len(candidates),
            "evidence_count": len(evidence_ids),
            "trigger_counts": dict(sorted(trigger_counts.items())),
        },
        "limitations": [
            "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
            "No evidence content is copied into the working set by this planner.",
            "Shadow mode records what would be retrieved but does not change provider context.",
        ],
    }
