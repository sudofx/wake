"""Deterministic Trust Compact candidates for shadow-mode measurement.

Compacts are derived invocation annotations, not durable beliefs or model
instructions.  They compress the operational consequence of a belief while
keeping explicit pointers to the receipts that can reopen it.
"""

from collections import Counter

from .store import digest


SETTLED_CONFIDENCE = 0.90
SETTLED_EVIDENCE_ROOTS = 2

REOPEN_CONDITIONS = [
    "credible contradictory evidence is recorded against the belief",
    "a supporting evidence root is invalidated, superseded, or unavailable",
    "the governing scope or decision changes",
    "a human or a governed future retrieval request asks for justification",
]


def build_trust_compacts_shadow(state):
    """Return deterministic compact candidates without changing durable state.

    A compact is eligible only when its source belief has explicit evidence.
    ``SETTLED`` is intentionally conservative: active, high-confidence beliefs
    with two independent recorded roots.  A retracted belief remains visible as
    a challenged candidate so its exact evidence can be rehydrated; it never
    becomes an operational default.
    """
    compacts = []
    for belief_id in sorted(state.get("beliefs", {})):
        belief = state["beliefs"][belief_id]
        roots = list(dict.fromkeys(belief.get("evidence", [])))
        if not roots:
            continue
        active = belief.get("status") == "active"
        settled = (active and belief.get("confidence", 0) >= SETTLED_CONFIDENCE
                   and len(roots) >= SETTLED_EVIDENCE_ROOTS)
        status = "SETTLED" if settled else ("CHALLENGED" if not active else "CANDIDATE")
        source = {
            "belief_id": belief_id,
            "statement": belief.get("statement", ""),
            "confidence": belief.get("confidence", 0),
            "belief_status": belief.get("status"),
            "evidence_roots": roots,
        }
        compact_id = "tc-" + digest(source)[:16]
        compacts.append({
            "id": compact_id,
            "rule": belief.get("statement", ""),
            "scope": "durable.belief:" + belief_id,
            "status": status,
            "strength": "settled" if settled else ("challenged" if not active else "provisional"),
            "provenance": {"belief_id": belief_id, "evidence_roots": roots,
                           "evidence_root_hash": digest(roots)},
            "formation": {"derived_at_version": state.get("version", 0),
                          "source_confidence": belief.get("confidence", 0),
                          "source_status": belief.get("status"),
                          "evidence_root_count": len(roots),
                          "criteria": {"minimum_confidence": SETTLED_CONFIDENCE,
                                       "minimum_evidence_roots": SETTLED_EVIDENCE_ROOTS}},
            "reopen_conditions": REOPEN_CONDITIONS,
            "rehydration": {"record": {"kind": "belief", "id": belief_id},
                            "evidence_ids": roots,
                            "trigger": "trust_compact_challenged"},
        })
    statuses = Counter(item["status"] for item in compacts)
    roots = list(dict.fromkeys(root for item in compacts for root in item["provenance"]["evidence_roots"]))
    return {
        "mode": "shadow",
        "principle": "Compress settled operational consequences without severing their evidence roots.",
        "compacts": compacts,
        "metrics": {"candidate_count": len(compacts), "settled_count": statuses["SETTLED"],
                    "challenged_count": statuses["CHALLENGED"], "provisional_count": statuses["CANDIDATE"],
                    "evidence_root_count": len(roots), "status_counts": dict(sorted(statuses.items()))},
        "limitations": [
            "Compacts are deterministic receipt annotations, not authoritative durable state.",
            "They do not enter provider context in shadow mode.",
            "A compact never deletes, replaces, or proves its underlying evidence.",
        ],
    }
