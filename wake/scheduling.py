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


def daily_quota_next_eligible(item, *, wait_provider_daily=False):
    """Return a configured cap or explicitly enabled daily-provider wait boundary."""
    configured_limit = item.get("quota_exhausted") == "configured_daily_limit"
    if not configured_limit and not (wait_provider_daily and item.get("status") == "deferred"
                                     and item.get("quota_exhausted") == "free_tier_daily"):
        return None
    quota_day = item.get("quota_day")
    if not quota_day:
        return None
    reset = datetime.fromisoformat(quota_day).replace(tzinfo=PACIFIC) + timedelta(days=1)
    return reset.astimezone(timezone.utc)


def provider_quota_limited(item):
    """Whether the latest deferred provider result includes a quota response."""
    if not item or item.get("status") != "deferred":
        return False
    if item.get("quota_exhausted") == "free_tier_daily":
        return True
    if any(
        attempt.get("result") in ("daily_quota", "rate_limited")
        for attempt in item.get("provider_attempts", [])
    ):
        return True
    provider_error = item.get("provider_error", {})
    if isinstance(provider_error, dict):
        provider_error = provider_error.get("provider_error", provider_error)
    return is_free_tier_daily_quota(provider_error)


def wake_status(state, daily_call_limit=20, now=None, *, wait_provider_daily=False):
    """Summarize accepted work, latest attempt, request accounting, and quota waits."""
    now = now or datetime.now(timezone.utc)
    items = sorted(state["invocations"].values(), key=lambda item: item["time"])
    accepted = [item for item in items if item["status"] == "accepted"]
    # Editorial recovery does not replace the
    # primary workload's failure/deferral latch. All paid calls still count.
    workload = [item for item in items if item.get("phase") != "group_editorial"
                and item.get("provider") != "editorial"]
    latest = workload[-1] if workload else None

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
    resets = []
    if (
        latest
        and latest.get("status") == "deferred"
        and str(latest.get("reason", "")).startswith("Gemini temporarily unavailable")
    ):
        base = latest.get("finished") or latest.get("time")
        if base:
            retry_after = (latest.get("provider_error") or {}).get("retry_after_seconds")
            delay = (
                timedelta(seconds=max(1, min(int(retry_after), 3600)))
                if isinstance(retry_after, (int, float)) and not isinstance(retry_after, bool)
                else TRANSIENT_RETRY_DELAY
            )
            resets.append(datetime.fromisoformat(base) + delay)
    request_slots_today = sum(charged_request_slots(i) for i in charged_today)

    if daily_call_limit is not None and request_slots_today >= daily_call_limit:
        resets.append(datetime.fromisoformat(day).replace(tzinfo=PACIFIC) + timedelta(days=1))

    # Operator-configured request caps are hard scheduling limits. Provider
    # quota responses are different: they remain visible as purple, but the
    # ordinary scheduler retries them so a recovered model can be observed.
    quota_standby_until = None
    if latest:
        provider_reset = daily_quota_next_eligible(latest, wait_provider_daily=wait_provider_daily)
        if provider_reset is not None:
            quota_standby_until = provider_reset
        elif daily_call_limit is not None and latest.get("quota_day"):
            latest_day_slots = sum(
                charged_request_slots(item) for item in items
                if item.get("charged") and item.get("quota_day") == latest["quota_day"]
            )
            if latest_day_slots >= daily_call_limit:
                quota_standby_until = (
                    datetime.fromisoformat(latest["quota_day"]).replace(tzinfo=PACIFIC)
                    + timedelta(days=1)
                ).astimezone(timezone.utc)

    if quota_standby_until and quota_standby_until > now:
        resets.append(quota_standby_until)
    next_eligible = max(resets) if resets and not state.get("pending") else None
    # Keep provider quota pressure visible across network failures and invocations
    # that make no provider request. A later HTTP response from Gemini (including
    # a successful fallback) clears it; a reservation with unknown outcome does not.
    provider_limited = False
    for item in items:
        attempts = item.get("provider_attempts", [])
        if not attempts and provider_quota_limited(item):
            provider_limited = True
        for attempt in attempts:
            result = attempt.get("result")
            if result in ("daily_quota", "rate_limited"):
                provider_limited = True
            elif result in ("success", "http_failure", "invalid_response") or (
                result == "transient_failure" and isinstance(attempt.get("http_status"), int)
            ):
                provider_limited = False
        if item.get("status") == "accepted" and item.get("charged") and not attempts:
            # Older receipts may predate per-model attempt lists; a charged,
            # accepted proposal still proves a later provider response arrived.
            provider_limited = False
    configured_limit_limited = bool(quota_standby_until and quota_standby_until > now)

    return {
        "last_accepted": brief(accepted[-1] if accepted else None),
        "latest_attempt": brief(latest),
        "accepted_cycles": state["version"],
        "next_eligible": next_eligible.isoformat() if next_eligible else None,
        "quota_standby_until": quota_standby_until.isoformat() if quota_standby_until else None,
        "quota_standby": provider_limited or configured_limit_limited,
        "provider_quota_limited": provider_limited,
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
