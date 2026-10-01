"""
WAKE✳︎ → sudofx migration bridge.

This module begins the Phase E migration without changing live WAKE authority.
It converts only a state reconstructed by WAKE Store.replay_record() into one
versioned sudofx application import. No provider output can call this bridge,
and importing does not delete or rewrite the legacy record.
"""

from __future__ import annotations

import hashlib
from copy import deepcopy

from sudofx import ApplicationAction, ApplicationDecision, ApplicationDefinition
from sudofx.models import JsonValue
from sudofx.storage import canonical_json
from .application_policy import govern_proposal
from .governance import Rejected
from .store import digest as legacy_digest, reduce_event


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

def _append_legacy_event(current: JsonValue, payload: JsonValue) -> ApplicationDecision:
    """Apply one WAKE event through application policy while sudofx owns durability."""
    if not isinstance(current, dict) or not isinstance(current.get("state"), dict):
        return ApplicationDecision(False, reasons=("WAKE legacy state must be imported first",))
    migration = current.get("migration")
    if not isinstance(migration, dict):
        return ApplicationDecision(False, reasons=("WAKE migration metadata is missing",))
    if not isinstance(payload, dict):
        return ApplicationDecision(False, reasons=("WAKE event application requires an object",))
    kind = payload.get("kind")
    event_payload = payload.get("payload")
    event_time = payload.get("time")
    if not isinstance(kind, str) or not kind.strip():
        return ApplicationDecision(False, reasons=("WAKE event kind must be non-empty text",))
    if not isinstance(event_payload, dict):
        return ApplicationDecision(False, reasons=("WAKE event payload must be an object",))
    if not isinstance(event_time, str) or not event_time.strip():
        return ApplicationDecision(False, reasons=("WAKE event time must be non-empty text",))

    prior_head = migration.get("legacy_head")
    prior_count = migration.get("legacy_event_count")
    if not _valid_hash(prior_head):
        return ApplicationDecision(False, reasons=("current WAKE compatibility head is invalid",))
    if isinstance(prior_count, bool) or not isinstance(prior_count, int) or prior_count < 0:
        return ApplicationDecision(False, reasons=("current WAKE compatibility event count is invalid",))

    state = deepcopy(current["state"])
    if kind == "accepted":
        proposal = event_payload.get("proposal")
        invocation = event_payload.get("id")
        if not isinstance(proposal, dict) or not isinstance(invocation, str):
            return ApplicationDecision(False, reasons=("accepted WAKE event requires id and proposal",))
        try:
            normalized, governed_state, editorial, rotation_filter = govern_proposal(
                state, invocation, proposal
            )
        except (Rejected, ValueError, TypeError, KeyError) as error:
            return ApplicationDecision(False, reasons=(str(error)[:1000],))
        if canonical_json(normalized) != canonical_json(proposal):
            return ApplicationDecision(False, reasons=("accepted proposal is not the normalized WAKE policy result",))
        fields = event_payload.get("hash_fields", ["version", "beliefs", "commitments", "journal"])
        if not isinstance(fields, list) or not all(isinstance(item, str) for item in fields):
            return ApplicationDecision(False, reasons=("accepted WAKE hash_fields are invalid",))
        try:
            expected_result_hash = legacy_digest({key: governed_state[key] for key in fields})
        except KeyError as error:
            return ApplicationDecision(False, reasons=(f"accepted WAKE hash field is missing: {error.args[0]}",))
        if event_payload.get("result_hash") != expected_result_hash:
            return ApplicationDecision(False, reasons=("accepted WAKE result hash does not match governed state",))
        if editorial is None and event_payload.get("editorial") is not None:
            return ApplicationDecision(False, reasons=("accepted WAKE editorial receipt is not policy-derived",))
        if editorial is not None and event_payload.get("editorial") != editorial:
            return ApplicationDecision(False, reasons=("accepted WAKE editorial receipt differs from policy result",))
        if rotation_filter is None and event_payload.get("rotation_filter") is not None:
            return ApplicationDecision(False, reasons=("accepted WAKE rotation filter is not policy-derived",))
        if rotation_filter is not None and event_payload.get("rotation_filter") != rotation_filter:
            return ApplicationDecision(False, reasons=("accepted WAKE rotation filter differs from policy result",))

    event = {
        "seq": prior_count + 1,
        "time": event_time,
        "kind": kind,
        "payload": event_payload,
        "prev_hash": prior_head,
    }
    event["hash"] = legacy_digest(event)
    try:
        next_state = reduce_event(state, event)
    except (Rejected, ValueError, TypeError, KeyError) as error:
        return ApplicationDecision(False, reasons=(str(error)[:1000],))

    next_migration = dict(migration)
    next_migration.update(
        {
            "source": "sudofx-authoritative-wake-events",
            "previous_legacy_head": prior_head,
            "legacy_head": event["hash"],
            "legacy_event_count": event["seq"],
            "legacy_state_digest": hashlib.sha256(canonical_json(next_state).encode()).hexdigest(),
            "legacy_version": next_state.get("version"),
        }
    )
    return ApplicationDecision(True, {"migration": next_migration, "state": next_state})


WAKE_APPLICATION = ApplicationDefinition(
    APPLICATION_ID,
    APPLICATION_VERSION,
    (
        ApplicationAction("import_legacy_snapshot", _import_legacy_snapshot),
        ApplicationAction("apply_governed_proposal", _apply_governed_proposal),
        ApplicationAction("append_legacy_event", _append_legacy_event),
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
