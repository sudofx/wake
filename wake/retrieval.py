# =============================================================================
# RETRIEVAL — the attention layer. Durable memory can be larger than any one prompt, so this module selects a bounded working set for a fresh invocation. What is omitted is still durable; it is simply outside this shift's attention.
#
# MAINTENANCE PRINCIPLE
# ---------------------
# Read this file as part of a chain of custody.  WAKE✳︎ deliberately separates
# disposable cognition from durable authority.  Comments therefore explain not
# only what a function does, but why its boundary exists and what a refactor must
# not accidentally collapse.  Prefer explicit receipts, deterministic state
# transitions, and replayable facts over convenient hidden behavior.
# =============================================================================

"""Deterministic planning for recoverable provenance.

This module only selects durable record IDs; it never copies evidence content
itself. The engine may materialize qualifying selected records into a bounded
provider context while governance remains authoritative over citation validity.
"""

from collections import Counter
import json


TRIGGER_DESCRIPTIONS = {
    "excerpt_boundary": "A working abstraction is clipped and may hide a material distinction.",
    "belief_retracted": "A retracted belief deserves exact provenance when it remains cognitively relevant.",
    "notebook_revised": "A revised notebook has changed under new evidence and may require exact comparison.",
    "commitment_near_due": "An open commitment is approaching its due cycle.",
    "unincorporated_evidence": "Durable evidence exists that is not yet represented by a belief or notebook.",
}


# ---------------------------------------------------------------------------


# STEP: build_retrieval_shadow


#


# This step exists as an explicit seam so its behavior can be


# inspected, tested, and replaced without giving a model hidden authority.


# Inputs should already belong to the layer named above; outputs remain data


# until the next boundary validates or records them. Callers may rely on this contract.


# ---------------------------------------------------------------------------


def build_retrieval_shadow(state, working_set, trust_compacts=None):
    """Return a bounded, deterministic plan for exact-record rehydration.

    The plan contains IDs and reasons only. It never copies evidence content into
    the working abstraction and never performs semantic contradiction detection.
    A caller may use these IDs to rehydrate qualifying durable records explicitly.
    """
    candidates = []

    # ---------------------------------------------------------------------------
    # STEP: add
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

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

    # Keep this bounded and recent, but prefer records that can actually
    # participate in notebook synthesis. Discovery/search-result payloads are
    # leads only; allowing them to consume all retrieval slots can strand older
    # qualifying source records outside the provider's attention indefinitely.
    unincorporated = []
    for evidence_id, evidence in state.get("evidence", {}).items():
        if evidence_id in represented_evidence:
            continue
        if evidence.get("actor") != "collector" or evidence.get("scope") != "collected":
            continue
        try:
            payload = json.loads(evidence.get("content", ""))
        except (ValueError, TypeError):
            payload = {}
        if payload.get("evidence_role") == "discovery":
            continue
        if payload.get("verification_required") is True and payload.get("evidence_role", "source") != "source":
            continue
        unincorporated.append(evidence_id)
    unincorporated = unincorporated[-6:]
    for evidence_id in unincorporated:
        add(
            "unincorporated_evidence",
            "evidence",
            evidence_id,
            TRIGGER_DESCRIPTIONS["unincorporated_evidence"],
            [evidence_id],
        )

    # A compact does not itself retrieve anything.  A challenged source belief
    # is, however, an explicit deterministic signal that the compact's exact
    # basis would need to be rehydrated before it could be relied upon again.
    for compact in (trust_compacts or {}).get("compacts", []):
        if compact.get("status") == "CHALLENGED":
            source = compact.get("provenance", {})
            add("trust_compact_challenged", "belief", source.get("belief_id"),
                "A Trust Compact source belief is challenged; rehydrate its exact roots.",
                source.get("evidence_roots", []))

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
            "The engine may explicitly rehydrate qualifying selected IDs into provider context.",
        ],
    }
