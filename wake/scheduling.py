# =============================================================================
# SCHEDULING — the admission-control layer. Time and quota decide whether another provider request may be attempted; they never decide what a proposal means or whether it deserves acceptance.
#
# MAINTENANCE PRINCIPLE
# ---------------------
# The architecture is intentionally explicit.  A future human or AI maintainer
# should be able to follow authority from input, through validation, to durable
# record without relying on folklore.  Comments explain why boundaries exist,
# what failure means, and which tempting shortcuts would weaken accountability.
# =============================================================================

"""Provider quota status derived from durable receipts."""
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from .providers import is_free_tier_daily_quota

PACIFIC = ZoneInfo("America/Los_Angeles")



def charged_request_slots(item):
    """Known calls plus unresolved reservations; legacy wakes retain one budget slot.

    This is a conservative ceiling calculation, never invented historical HTTP counts.
    """
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
    """Report accepted work independently of publishing and transient attempts."""
    now = now or datetime.now(timezone.utc)
    items = sorted(state["invocations"].values(), key=lambda item: item["time"])
    accepted = [item for item in items if item["status"] == "accepted"]
    latest = items[-1] if items else None
    def brief(item):
        if item is None:
            return None
        return {key: item[key] for key in ("id", "time", "finished", "status", "reason", "provider_error", "editorial",
                                           "provider_requests_sent", "provider_attempts", "successful_model")
                if key in item}
    eligible = None
    day = now.astimezone(PACIFIC).date().isoformat()
    charged_today = [i for i in items if i.get("charged") and i.get("quota_day") == day]
    quota_resets = [daily_quota_next_eligible(i) for i in charged_today]
    resets = [reset for reset in quota_resets if reset is not None]
    request_slots_today = sum(charged_request_slots(i) for i in charged_today)
    if daily_call_limit is not None and request_slots_today >= daily_call_limit:
        resets.append(datetime.fromisoformat(day).replace(tzinfo=PACIFIC) + timedelta(days=1))
    if resets:
        eligible = max(([eligible] if eligible else []) + resets)
    return {"last_accepted": brief(accepted[-1] if accepted else None),
            "latest_attempt": brief(latest), "accepted_cycles": state["version"],
            "next_eligible": eligible.isoformat() if eligible and not state.get("pending") else None,
            "pending": bool(state.get("pending")), "attempts_today": len(charged_today),
            "provider_requests_today": sum(i.get("provider_requests_sent", 0) for i in charged_today),
            "provider_request_slots_today": request_slots_today,
            "provider_request_counts_incomplete": any("provider_requests_sent" not in i or
                any(a["result"] == "unknown" for a in i.get("provider_attempts", [])) for i in charged_today),
            "daily_call_limit": daily_call_limit}
