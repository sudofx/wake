# =============================================================================
# STATUS / QUOTA ELIGIBILITY
#
# This module reports public run status from durable invocation receipts. It does
# not schedule wakes. Continuous execution is owned by GitHub Actions; only known
# quota boundaries belong here.
# =============================================================================

"""Public run status and quota-reset calculations."""

from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

from .providers import is_free_tier_daily_quota


PACIFIC = ZoneInfo("America/Los_Angeles")
TRANSIENT_RETRY_DELAY = timedelta(seconds=15)


def charged_request_slots(item):
    """Count known attempts plus unresolved reservations conservatively."""
    if "provider_attempts" in item:
        return len(item["provider_attempts"])
    return item.get("provider_requests_sent", 1)


def daily_quota_next_eligible(item):
    """Return the next Pacific midnight for a durable per-day quota boundary."""
    configured_limit = item.get("quota_exhausted") == "configured_daily_limit"
    if not configured_limit and not is_free_tier_daily_quota(item.get("provider_error", {})):
        return None
    quota_day = item.get("quota_day")
    if not quota_day:
        return None
    reset = datetime.fromisoformat(quota_day).replace(tzinfo=PACIFIC) + timedelta(days=1)
    return reset.astimezone(timezone.utc)


def wake_status(state, daily_call_limit=20, now=None):
    """Summarize accepted work, latest attempt, request accounting, and quota waits."""
    now = now or datetime.now(timezone.utc)
    items = sorted(state["invocations"].values(), key=lambda item: item["time"])
    accepted = [item for item in items if item["status"] == "accepted"]
    latest = items[-1] if items else None

    def brief(item):
        if item is None:
            return None
        return {
            key: item[key]
            for key in (
                "id", "time", "finished", "status", "reason", "provider_error",
                "editorial", "provider_requests_sent", "provider_attempts",
                "successful_model",
            )
            if key in item
        }

    day = now.astimezone(PACIFIC).date().isoformat()
    charged_today = [i for i in items if i.get("charged") and i.get("quota_day") == day]
    resets = [
        reset
        for reset in (daily_quota_next_eligible(i) for i in charged_today)
        if reset is not None
    ]
    if (
        latest
        and latest.get("status") == "deferred"
        and str(latest.get("reason", "")).startswith("Gemini temporarily unavailable")
    ):
        base = latest.get("finished") or latest.get("time")
        if base:
            resets.append(datetime.fromisoformat(base) + TRANSIENT_RETRY_DELAY)
    request_slots_today = sum(charged_request_slots(i) for i in charged_today)

    if daily_call_limit is not None and request_slots_today >= daily_call_limit:
        resets.append(datetime.fromisoformat(day).replace(tzinfo=PACIFIC) + timedelta(days=1))

    next_eligible = max(resets) if resets and not state.get("pending") else None

    return {
        "last_accepted": brief(accepted[-1] if accepted else None),
        "latest_attempt": brief(latest),
        "accepted_cycles": state["version"],
        "next_eligible": next_eligible.isoformat() if next_eligible else None,
        "pending": bool(state.get("pending")),
        "attempts_today": len(charged_today),
        "provider_requests_today": sum(i.get("provider_requests_sent", 0) for i in charged_today),
        "provider_request_slots_today": request_slots_today,
        "provider_request_counts_incomplete": any(
            "provider_requests_sent" not in i
            or any(a["result"] == "unknown" for a in i.get("provider_attempts", []))
            for i in charged_today
        ),
        "daily_call_limit": daily_call_limit,
    }
