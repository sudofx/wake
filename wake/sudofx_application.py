"""
WAKE✳︎ → sudofx application boundary.

Phase E has moved live WAKE authority onto sudofx. This module defines the
versioned WAKE application contract, verifies the one-time legacy import, and
governs post-migration WAKE-compatible events without moving research-specific
policy into the generic sudofx kernel. Provider output cannot call migration
actions directly, and legacy history remains preserved as verified evidence.
"""

from __future__ import annotations

import hashlib
import json
from copy import deepcopy

from sudofx import ApplicationAction, ApplicationDecision, ApplicationDefinition
from sudofx.models import JsonValue
from sudofx.storage import canonical_json
from .application_policy import govern_proposal
from .governance import Rejected
from .history import migration_baseline
from .event_format import digest as legacy_digest
from .domain_events import empty, reduce_event


APPLICATION_ID = "wake"
# This version string is already durable in the live sudofx record. Its historical
# name reflects the first Phase E cutover, not the only supported initialization
# path. Do not rename it merely for terminology: changing an application version
# requires an explicit governed migration so existing authority fails closed
# rather than silently reinterpreting durable application events.
APPLICATION_VERSION = "legacy-import-v1"
LEGACY_ARCHIVE_CHUNK_SIZE = 1000


def _valid_hash(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _initialize_empty(current: JsonValue, payload: JsonValue) -> ApplicationDecision:
    """Create a brand-new WAKE application directly inside sudofx authority."""
    if current is not None:
        return ApplicationDecision(False, reasons=("WAKE application state already exists",))
    if not isinstance(payload, dict) or payload.get("reason") != "explicit-initialization":
        return ApplicationDecision(
            False,
            reasons=("Native WAKE initialization requires explicit-initialization intent",),
        )

    state = empty()
    state_digest = hashlib.sha256(canonical_json(state).encode()).hexdigest()
    zero = "0" * 64
    return ApplicationDecision(
        True,
        {
            "migration": {
                # Keep the migration envelope shape stable so the compatibility
                # adapter can serve both migrated and native WAKE histories.
                "source": "sudofx-native",
                "legacy_head": zero,
                "legacy_event_count": 0,
                "import_legacy_head": zero,
                "import_legacy_event_count": 0,
                "legacy_state_digest": state_digest,
                "legacy_version": 0,
                "history_baseline": migration_baseline([], state),
                "archive_event_count": 0,
                "archive_head": zero,
                "archive_complete": True,
                "active_generation": 0,
            },
            "state": state,
        },
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
    history_baseline = payload.get("history_baseline")
    if not isinstance(history_baseline, dict):
        return ApplicationDecision(False, reasons=("history_baseline must be an object",))

    return ApplicationDecision(
        True,
        {
            "migration": {
                "source": "wake-legacy-sqlite",
                "legacy_head": legacy_head,
                "legacy_event_count": event_count,
                "import_legacy_head": legacy_head,
                "import_legacy_event_count": event_count,
                "legacy_state_digest": state_digest,
                "legacy_version": payload.get("legacy_version"),
                "history_baseline": deepcopy(history_baseline),
                "archive_event_count": 0,
                "archive_head": "0" * 64,
                "archive_complete": event_count == 0,
            },
            "state": legacy_state,
        },
    )


def _state_for_legacy_event(state: dict, kind: str, payload: dict) -> dict:
    """Copy only WAKE branches that reduce_event may mutate for this event."""
    result = dict(state)
    if kind == "accepted":
        # transition() owns proposal atomicity and does not mutate its input.
        return result
    if kind == "research_collected":
        research = dict(state.get("research", {}))
        item_id = payload.get("id")
        if item_id in research and isinstance(research[item_id], dict):
            research[item_id] = dict(research[item_id])
        result["research"] = research
    elif kind == "project_adopted":
        result["projects"] = dict(state.get("projects", {}))
    elif kind == "acquisition_assessed":
        result["acquisition"] = dict(state.get("acquisition", {}))
    elif kind == "observation":
        result["evidence"] = dict(state.get("evidence", {}))
    elif kind == "commitment_cancelled":
        commitments = dict(state.get("commitments", {}))
        item_id = payload.get("id")
        if item_id in commitments and isinstance(commitments[item_id], dict):
            commitments[item_id] = dict(commitments[item_id])
        result["commitments"] = commitments
    elif kind in {
        "invocation_started",
        "provider_attempt_started",
        "provider_attempt_finished",
        "rejected",
        "failed",
        "deferred",
        "recovered",
    }:
        invocations = dict(state.get("invocations", {}))
        invocation_id = payload.get("id")
        if invocation_id in invocations and isinstance(invocations[invocation_id], dict):
            item = dict(invocations[invocation_id])
            if kind in {"provider_attempt_started", "provider_attempt_finished"}:
                item["provider_attempts"] = list(item.get("provider_attempts", []))
            invocations[invocation_id] = item
        result["invocations"] = invocations
    return result


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

    state = _state_for_legacy_event(current["state"], kind, event_payload)
    if kind == "accepted":
        proposal = event_payload.get("proposal")
        invocation = event_payload.get("id")
        if not isinstance(proposal, dict) or not isinstance(invocation, str):
            return ApplicationDecision(False, reasons=("accepted WAKE event requires id and proposal",))

        # WAKE stores the normalized proposal plus the exact raw provider response.
        # Re-run policy from that raw response so normalization receipts such as the
        # Attention rotation filter are independently reproducible. Re-running policy
        # on the already-normalized proposal would erase the evidence of withheld
        # actions and incorrectly reject a valid accepted event.
        raw_response = event_payload.get("raw_response")
        policy_input = proposal
        if isinstance(raw_response, str):
            try:
                decoded = json.loads(
                    raw_response,
                    parse_constant=lambda value: (_ for _ in ()).throw(ValueError("Nonfinite JSON")),
                )
            except (ValueError, TypeError) as error:
                return ApplicationDecision(False, reasons=(f"accepted WAKE raw response is invalid: {error}",))
            if not isinstance(decoded, dict):
                return ApplicationDecision(False, reasons=("accepted WAKE raw response must decode to an object",))
            policy_input = decoded

        try:
            normalized, governed_state, editorial, rotation_filter = govern_proposal(
                state, invocation, policy_input
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


def _import_legacy_event_chunk(current: JsonValue, payload: JsonValue) -> ApplicationDecision:
    """Persist one verified suffix of the pre-sudofx WAKE event chain."""
    if not isinstance(current, dict) or not isinstance(current.get("state"), dict):
        return ApplicationDecision(False, reasons=("WAKE legacy state must be imported first",))
    migration = current.get("migration")
    if not isinstance(migration, dict):
        return ApplicationDecision(False, reasons=("WAKE migration metadata is missing",))
    if not isinstance(payload, dict):
        return ApplicationDecision(False, reasons=("legacy event archive chunk requires an object",))
    events = payload.get("events")
    if not isinstance(events, list) or not events or len(events) > LEGACY_ARCHIVE_CHUNK_SIZE:
        return ApplicationDecision(
            False,
            reasons=(f"legacy event archive chunk must contain 1-{LEGACY_ARCHIVE_CHUNK_SIZE} events",),
        )

    count = migration.get("archive_event_count", 0)
    head = migration.get("archive_head", "0" * 64)
    target_count = migration.get("import_legacy_event_count")
    target_head = migration.get("import_legacy_head")
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        return ApplicationDecision(False, reasons=("legacy archive event count is invalid",))
    if not _valid_hash(head) or not _valid_hash(target_head):
        return ApplicationDecision(False, reasons=("legacy archive head is invalid",))
    if isinstance(target_count, bool) or not isinstance(target_count, int) or target_count < 0:
        return ApplicationDecision(False, reasons=("legacy archive target count is invalid",))
    if count + len(events) > target_count:
        return ApplicationDecision(False, reasons=("legacy archive chunk exceeds imported history",))

    expected_seq = count + 1
    expected_head = head
    for event in events:
        if not isinstance(event, dict):
            return ApplicationDecision(False, reasons=("legacy archive event must be an object",))
        if event.get("seq") != expected_seq:
            return ApplicationDecision(False, reasons=("legacy archive event sequence is not contiguous",))
        if event.get("prev_hash") != expected_head:
            return ApplicationDecision(False, reasons=("legacy archive event does not descend from prior head",))
        body = {key: value for key, value in event.items() if key != "hash"}
        if legacy_digest(body) != event.get("hash"):
            return ApplicationDecision(False, reasons=("legacy archive event hash is invalid",))
        expected_seq += 1
        expected_head = event["hash"]

    next_count = count + len(events)
    complete = next_count == target_count
    if complete and expected_head != target_head:
        return ApplicationDecision(False, reasons=("legacy archive final head does not match imported history",))

    next_migration = dict(migration)
    next_migration.update(
        archive_event_count=next_count,
        archive_head=expected_head,
        archive_complete=complete,
    )
    return ApplicationDecision(
        True,
        {"migration": next_migration, "state": current["state"]},
    )


def _reset_to_zero(current: JsonValue, payload: JsonValue) -> ApplicationDecision:
    """Start a new active WAKE generation while retaining prior sudofx history."""
    if not isinstance(current, dict) or not isinstance(current.get("state"), dict):
        return ApplicationDecision(False, reasons=("WAKE state must exist before reset",))
    if not isinstance(payload, dict) or payload.get("actor") != "operator":
        return ApplicationDecision(False, reasons=("WAKE reset requires explicit operator provenance",))
    reason = payload.get("reason")
    if not isinstance(reason, str) or not reason.strip():
        return ApplicationDecision(False, reasons=("WAKE reset reason is required",))
    migration = current.get("migration")
    if not isinstance(migration, dict):
        return ApplicationDecision(False, reasons=("WAKE migration metadata is missing",))

    generation = migration.get("active_generation", 0)
    if isinstance(generation, bool) or not isinstance(generation, int) or generation < 0:
        return ApplicationDecision(False, reasons=("WAKE active generation is invalid",))
    reset_history = list(migration.get("reset_history", []))
    reset_history.append(
        {
            "generation": generation,
            "head": migration.get("legacy_head"),
            "event_count": migration.get("legacy_event_count"),
            "reason": reason.strip(),
        }
    )
    next_migration = dict(migration)
    next_migration.update(
        {
            "source": "sudofx-authoritative-wake-reset",
            "active_generation": generation + 1,
            "legacy_head": "0" * 64,
            "legacy_event_count": 0,
            "reset_history": reset_history,
        }
    )
    return ApplicationDecision(True, {"migration": next_migration, "state": empty()})


WAKE_APPLICATION = ApplicationDefinition(
    APPLICATION_ID,
    APPLICATION_VERSION,
    (
        ApplicationAction("initialize_empty", _initialize_empty),
        ApplicationAction("import_legacy_snapshot", _import_legacy_snapshot),
        ApplicationAction("apply_governed_proposal", _apply_governed_proposal),
        ApplicationAction("import_legacy_event_chunk", _import_legacy_event_chunk),
        ApplicationAction("append_legacy_event", _append_legacy_event),
        ApplicationAction("reset_to_zero", _reset_to_zero),
    ),
    state_storage="event_log",
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
        "history_baseline": migration_baseline(events, state),
    }
