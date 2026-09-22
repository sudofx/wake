"""Operator-controlled experimental regimes and temporal measurements.

The current TOML file is an input, not historical proof.  These helpers keep
the small control surface in durable events so a later UI can use the same
operator boundary without turning settings into mutable, unaudited state.
"""

from datetime import datetime, timezone

from .governance import Rejected, require
from .store import digest


TIME_DILATION = "time_dilation"


def defaults():
    return {TIME_DILATION: {
        "enabled": True,
        "mode": "real",
        "scale": 1.0,
        "description": "Records wall, cycle and intervening-event distance; effective time follows the selected mapping.",
        "affects": ["telemetry", "provider_context"],
    }}


def validate(controls):
    require(isinstance(controls, dict) and set(controls) == {TIME_DILATION},
            "Controls must declare the supported experimental mechanisms exactly")
    item = controls[TIME_DILATION]
    require(isinstance(item, dict), "Time Dilation control must be an object")
    require(type(item.get("enabled")) is bool, "Time Dilation enabled must be true or false")
    require(item.get("mode") in ("real", "scaled", "frozen"),
            "Time Dilation mode must be real, scaled, or frozen")
    scale = item.get("scale")
    require(isinstance(scale, (int, float)) and not isinstance(scale, bool) and 0 < scale <= 1000,
            "Time Dilation scale must be a number between 0 and 1000")
    if item["mode"] in ("real", "frozen"):
        require(float(scale) == 1.0, "Real and frozen Time Dilation modes use scale 1")
    return {TIME_DILATION: {**defaults()[TIME_DILATION], **item, "scale": float(scale)}}


def regime(controls):
    controls = validate(controls)
    return {"id": "reg-" + digest(controls)[:16], "controls": controls}


def scale(controls):
    item = controls[TIME_DILATION]
    if not item["enabled"] or item["mode"] == "frozen":
        return 0.0 if item["mode"] == "frozen" else 1.0
    return item["scale"] if item["mode"] == "scaled" else 1.0


def _seconds(then, at):
    return max(0.0, (datetime.fromisoformat(at).astimezone(timezone.utc) -
                     datetime.fromisoformat(then).astimezone(timezone.utc)).total_seconds())


def temporal_snapshot(state, events, at):
    """Derive a new boundary snapshot without modifying any prior receipt."""
    experimental = state.get("experimental")
    require(experimental, "Experimental regime is not initialized")
    previous = state.get("temporal") or {
        "anchor_time": experimental["adopted_at"], "anchor_version": experimental["effective_from_version"],
        "anchor_seq": experimental["event_seq"], "effective_seconds": 0.0,
    }
    wall = _seconds(previous["anchor_time"], at)
    since = [event for event in events if event["seq"] > previous.get("anchor_seq", 0)]
    kinds = {kind: sum(event["kind"] == kind for event in since) for kind in
             ("accepted", "rejected", "failed", "observation", "research_collected", "squirrel_assessed")}
    factor = scale(experimental["controls"])
    return {
        "observed_at": at, "wall_elapsed_seconds": round(wall, 6),
        "cycle_distance": state["version"] - previous["anchor_version"],
        "intervening_events": {"total": len(since), **kinds},
        "effective_scale": factor,
        "effective_elapsed_seconds": round(wall * factor, 6),
        "effective_seconds_total": round(previous["effective_seconds"] + wall * factor, 6),
        "previous_anchor_time": previous["anchor_time"],
        "regime_id": experimental["id"],
    }


def adoption_payload(state, events, controls, actor, reason, at, seq):
    controls = validate(controls)
    prior = state.get("experimental")
    if prior:
        snapshot = temporal_snapshot(state, events, at)
        effective_seconds = snapshot["effective_seconds_total"]
    else:
        effective_seconds = 0.0
    value = regime(controls)
    return {**value, "actor": actor, "reason": reason, "adopted_at": at,
            "event_seq": seq, "effective_from_version": state["version"],
            "effective_seconds": effective_seconds}
