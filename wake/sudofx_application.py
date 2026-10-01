"""
WAKE✳︎ → sudofx migration bridge.

This module begins the Phase E migration without changing live WAKE authority.
It converts only a state reconstructed by WAKE Store.replay_record() into one
versioned sudofx application import. No provider output can call this bridge,
and importing does not delete or rewrite the legacy record.
"""

from __future__ import annotations

import hashlib

from sudofx import ApplicationAction, ApplicationDecision, ApplicationDefinition
from sudofx.models import JsonValue
from sudofx.storage import canonical_json
from .engine import govern_proposal
from .governance import Rejected


APPLICATION_ID = "wake"
APPLICATION_VERSION = "legacy-import-v1"


def _valid_hash(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _import_legacy_snapshot(current: JsonValue, payload: JsonValue) -> ApplicationDecision:
    """Accept one verified legacy snapshot as the initial WAKE application state."""
    if current is not None:
        return ApplicationDecision(False, reasons=("WAKE legacy state is already imported",))
    if not isinstance(payload, dict):
        return ApplicationDecision(False, reasons=("WAKE legacy import requires an object",))

    legacy_state = payload.get("legacy_state")
    legacy_head = payload.get("legacy_head")
    event_count = payload.get("legacy_event_count")
    state_digest = payload.get("legacy_state_digest")
    if not isinstance(legacy_state, dict):
        return ApplicationDecision(False, reasons=("legacy_state must be an object",))
    if not _valid_hash(legacy_head):
        return ApplicationDecision(False, reasons=("legacy_head must be a SHA-256 digest",))
    if isinstance(event_count, bool) or not isinstance(event_count, int) or event_count < 0:
        return ApplicationDecision(False, reasons=("legacy_event_count must be a non-negative integer",))
    if not _valid_hash(state_digest):
        return ApplicationDecision(False, reasons=("legacy_state_digest must be a SHA-256 digest",))
    expected_digest = hashlib.sha256(canonical_json(legacy_state).encode()).hexdigest()
    if state_digest != expected_digest:
        return ApplicationDecision(False, reasons=("legacy_state_digest does not match legacy_state",))
    if legacy_state.get("version") != payload.get("legacy_version"):
        return ApplicationDecision(False, reasons=("legacy_version does not match replayed WAKE state",))

    return ApplicationDecision(
        True,
        {
            "migration": {
                "source": "wake-legacy-sqlite",
                "legacy_head": legacy_head,
                "legacy_event_count": event_count,
                "legacy_state_digest": state_digest,
                "legacy_version": payload.get("legacy_version"),
            },
            "state": legacy_state,
        },
    )


def _apply_governed_proposal(current: JsonValue, payload: JsonValue) -> ApplicationDecision:
    """Run existing WAKE domain governance while sudofx remains durable authority."""
    if not isinstance(current, dict) or not isinstance(current.get("state"), dict):
        return ApplicationDecision(False, reasons=("WAKE legacy state must be imported first",))
    if not isinstance(payload, dict):
        return ApplicationDecision(False, reasons=("WAKE proposal application requires an object",))
    invocation = payload.get("invocation")
    proposal = payload.get("proposal")
    if not isinstance(invocation, str) or not invocation.strip():
        return ApplicationDecision(False, reasons=("WAKE invocation must be non-empty text",))
    if not isinstance(proposal, dict):
        return ApplicationDecision(False, reasons=("WAKE proposal must be an object",))
    try:
        _, next_legacy_state, _, _ = govern_proposal(
            current["state"], invocation, proposal
        )
    except (Rejected, ValueError, TypeError, KeyError) as error:
        return ApplicationDecision(False, reasons=(str(error)[:1000],))
    return ApplicationDecision(
        True,
        {
            "migration": current.get("migration"),
            "state": next_legacy_state,
        },
    )

WAKE_APPLICATION = ApplicationDefinition(
    APPLICATION_ID,
    APPLICATION_VERSION,
    (
        ApplicationAction("import_legacy_snapshot", _import_legacy_snapshot),
        ApplicationAction("apply_governed_proposal", _apply_governed_proposal),
    ),
)


def verified_legacy_snapshot(store) -> dict[str, JsonValue]:
    """Build migration input only after WAKE verifies the complete legacy event chain."""
    state, head, events = store.replay_record()
    return {
        "legacy_state": state,
        "legacy_head": head,
        "legacy_event_count": len(events),
        "legacy_state_digest": hashlib.sha256(canonical_json(state).encode()).hexdigest(),
        "legacy_version": state.get("version"),
    }
