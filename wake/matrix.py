"""WAKE-owned opt-in use of the shared sudofx continuity matrix.

sudofx owns only the immutable matrix grammar and coordinate validation.
WAKE owns campaign enablement, result semantics, progress, and traversal input.
Durable state is returned through WAKE's ordinary ApplicationHost actions.
"""

from __future__ import annotations

from copy import deepcopy

from sudofx import ApplicationDecision, continuity_matrix
from sudofx.models import JsonValue


MATRIX = continuity_matrix()
MATRIX_KEY = f"{MATRIX.matrix_id}@{MATRIX.version}"
_RESULT_STATUSES = {"completed", "failed", "deferred"}


def _extensions(current: dict) -> dict:
    value = current.get("extensions")
    return deepcopy(value) if isinstance(value, dict) else {}


def _campaign_state() -> dict:
    return {
        "matrix_id": MATRIX.matrix_id,
        "matrix_version": MATRIX.version,
        "definition_digest": MATRIX.definition_digest,
        "results": {},
    }


def enable_continuity_matrix(current: JsonValue, payload: JsonValue) -> ApplicationDecision:
    """Explicitly opt this WAKE application state into continuity@1."""
    if not isinstance(current, dict) or not isinstance(current.get("state"), dict):
        return ApplicationDecision(False, reasons=("WAKE state must exist before matrix enablement",))
    if not isinstance(payload, dict) or payload.get("matrix") != MATRIX_KEY:
        return ApplicationDecision(False, reasons=(f"matrix enablement requires {MATRIX_KEY}",))

    extensions = _extensions(current)
    existing = extensions.get(MATRIX_KEY)
    if existing is not None:
        if not isinstance(existing, dict):
            return ApplicationDecision(False, reasons=("WAKE matrix state is malformed",))
        if (
            existing.get("matrix_id") != MATRIX.matrix_id
            or existing.get("matrix_version") != MATRIX.version
            or existing.get("definition_digest") != MATRIX.definition_digest
        ):
            return ApplicationDecision(False, reasons=("WAKE matrix definition does not match continuity@1",))
        return ApplicationDecision(True, current)

    extensions[MATRIX_KEY] = _campaign_state()
    next_state = deepcopy(current)
    next_state["extensions"] = extensions
    return ApplicationDecision(True, next_state)


def record_continuity_matrix_result(current: JsonValue, payload: JsonValue) -> ApplicationDecision:
    """Persist one WAKE-interpreted result for a validated continuity@1 coordinate."""
    if not isinstance(current, dict) or not isinstance(current.get("state"), dict):
        return ApplicationDecision(False, reasons=("WAKE state must exist before matrix results",))
    if not isinstance(payload, dict):
        return ApplicationDecision(False, reasons=("WAKE matrix result requires an object",))

    coordinate_id = payload.get("coordinate_id")
    result = payload.get("result")
    if not isinstance(coordinate_id, str):
        return ApplicationDecision(False, reasons=("WAKE matrix coordinate_id must be text",))
    try:
        coordinate = MATRIX.coordinate_by_id(coordinate_id)
    except ValueError as error:
        return ApplicationDecision(False, reasons=(str(error),))
    if coordinate.coordinate_id != coordinate_id:
        return ApplicationDecision(False, reasons=("WAKE matrix coordinate ID is not canonical",))
    if not isinstance(result, dict):
        return ApplicationDecision(False, reasons=("WAKE matrix result must be an object",))
    status = result.get("status")
    if status not in _RESULT_STATUSES:
        return ApplicationDecision(
            False,
            reasons=("WAKE matrix result status must be completed, failed, or deferred",),
        )
    score = result.get("score")
    if score is not None and (
        isinstance(score, bool)
        or not isinstance(score, (int, float))
        or score < 0
        or score > 1
    ):
        return ApplicationDecision(False, reasons=("WAKE matrix score must be between 0 and 1",))

    extensions = _extensions(current)
    campaign = extensions.get(MATRIX_KEY)
    if not isinstance(campaign, dict):
        return ApplicationDecision(False, reasons=("continuity@1 is not enabled for WAKE",))
    if campaign.get("definition_digest") != MATRIX.definition_digest:
        return ApplicationDecision(False, reasons=("WAKE matrix definition digest changed",))

    results = deepcopy(campaign.get("results"))
    if not isinstance(results, dict):
        return ApplicationDecision(False, reasons=("WAKE matrix results are malformed",))
    results[coordinate_id] = deepcopy(result)
    next_campaign = deepcopy(campaign)
    next_campaign["results"] = results
    extensions[MATRIX_KEY] = next_campaign
    next_state = deepcopy(current)
    next_state["extensions"] = extensions
    return ApplicationDecision(True, next_state)


def continuity_matrix_progress(envelope: JsonValue) -> dict | None:
    """Return a derived WAKE progress view; the envelope remains authoritative."""
    if not isinstance(envelope, dict):
        return None
    extensions = envelope.get("extensions")
    campaign = extensions.get(MATRIX_KEY) if isinstance(extensions, dict) else None
    if not isinstance(campaign, dict):
        return None
    results = campaign.get("results")
    if not isinstance(results, dict):
        return None
    completed = sorted(
        coordinate_id
        for coordinate_id, result in results.items()
        if isinstance(result, dict) and result.get("status") == "completed"
    )
    next_coordinate = MATRIX.next_uncovered(completed)
    return {
        "matrix": MATRIX_KEY,
        "definition_digest": MATRIX.definition_digest,
        "cell_count": MATRIX.cell_count,
        "completed_count": len(completed),
        "completed_coordinate_ids": completed,
        "next_coordinate_id": (
            next_coordinate.coordinate_id if next_coordinate is not None else None
        ),
        "results": deepcopy(results),
    }
