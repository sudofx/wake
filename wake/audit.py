# =============================================================================
# AUDIT — independent replay from exported events. The point is distrust: verify sequence, previous hash, event hash and deterministic reduction rather than trusting a saved projection or a successful-looking website.
#
# MAINTENANCE PRINCIPLE
# ---------------------
# The architecture is intentionally explicit.  A future human or AI maintainer
# should be able to follow authority from input, through validation, to durable
# record without relying on folklore.  Comments explain why boundaries exist,
# what failure means, and which tempting shortcuts would weaken accountability.
# =============================================================================

"""Reconstruct from exported events alone, without SQLite or a saved projection."""

import json
from pathlib import Path

from .store import IntegrityError, ZERO, digest, empty, reduce_event
# ---------------------------------------------------------------------------
# STEP: verify_history
#
# Keep this function explicit because it marks a testable boundary in the
# chain from operator/provider input to durable/public output.  Do not fold it
# into a neighboring layer if doing so would hide validation, provenance,
# failure handling, or the distinction between accepted state and a derived view.
# ---------------------------------------------------------------------------


def verify_history(path, expected_head=None):
    state, head = empty(), ZERO
    for seq, line in enumerate(Path(path).read_text().splitlines(), 1):
        try:
            event = json.loads(line)
            if event["seq"] != seq or event["prev_hash"] != head or digest({k:v for k,v in event.items() if k != "hash"}) != event["hash"]:
                raise IntegrityError(f"Exported event {seq} failed verification")
            state = reduce_event(state, event, historical=True)
            head = event["hash"]
        except (ValueError, KeyError, TypeError) as exc:
            raise IntegrityError(f"Exported event {seq} is invalid: {exc}") from exc
    if expected_head and head != expected_head.strip():
        raise IntegrityError("History does not match the independently retained head")
    return state, head
