"""Eligibility shared by the cloud scheduler and its public status report."""
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from .providers import is_free_tier_daily_quota


SCHEDULED_WAKE_INTERVAL = timedelta(minutes=55)
SCHEDULED_TRANSIENT_RETRY_INTERVAL = timedelta(minutes=10)
PACIFIC = ZoneInfo("America/Los_Angeles")


def daily_quota_next_eligible(item):
    """Return the next Pacific midnight for an exact Gemini daily-quota result."""
    if not is_free_tier_daily_quota(item.get("provider_error", {})):
        return None
    quota_day = item.get("quota_day")
    if not quota_day:
        return None
    reset = datetime.fromisoformat(quota_day).replace(tzinfo=PACIFIC) + timedelta(days=1)
    return reset.astimezone(timezone.utc)


def transient_provider_deferred(item):
    return (item.get("status") == "deferred"
            and str(item.get("reason", "")).startswith("Gemini temporarily unavailable"))


def scheduled_wake_due(state, now=None):
    """Collapse redundant GitHub cron deliveries into roughly one hourly wake.

    GitHub's scheduler can delay or drop events, so the workflow asks at several
    off-minute times. The last charged invocation is the cross-run authority:
    a backup may replace a missing wake, but it cannot duplicate a recent
    scheduled or manual Gemini call.
    """
    now = now or datetime.now(timezone.utc)
    charged = [item for item in state["invocations"].values() if item.get("charged")]
    if not charged:
        return True, None
    latest = max(charged, key=lambda item: datetime.fromisoformat(item["time"]))
    quota_reset = daily_quota_next_eligible(latest)
    if quota_reset is not None:
        return now >= quota_reset, quota_reset
    interval = (SCHEDULED_TRANSIENT_RETRY_INTERVAL
                if transient_provider_deferred(latest) else SCHEDULED_WAKE_INTERVAL)
    next_eligible = datetime.fromisoformat(latest["time"]) + interval
    return now >= next_eligible, next_eligible



def wake_status(state, daily_call_limit=20, now=None):
    """Report accepted work independently of publishing and transient attempts."""
    now = now or datetime.now(timezone.utc)
    items = sorted(state["invocations"].values(), key=lambda item: item["time"])
    accepted = [item for item in items if item["status"] == "accepted"]
    latest = items[-1] if items else None
    def brief(item):
        if item is None:
            return None
        return {key: item[key] for key in ("id", "time", "finished", "status", "reason", "provider_error", "editorial")
                if key in item}
    _, eligible = scheduled_wake_due(state, now)
    day = now.astimezone(PACIFIC).date().isoformat()
    charged_today = [i for i in items if i.get("charged") and i.get("quota_day") == day]
    quota_resets = [daily_quota_next_eligible(i) for i in charged_today]
    resets = [reset for reset in quota_resets if reset is not None]
    if len(charged_today) >= daily_call_limit:
        resets.append(datetime.fromisoformat(day).replace(tzinfo=PACIFIC) + timedelta(days=1))
    if resets:
        eligible = max(([eligible] if eligible else []) + resets)
    return {"last_accepted": brief(accepted[-1] if accepted else None),
            "latest_attempt": brief(latest), "accepted_cycles": state["version"],
            "next_eligible": eligible.isoformat() if eligible and not state.get("pending") else None,
            "pending": bool(state.get("pending")), "attempts_today": len(charged_today),
            "daily_call_limit": daily_call_limit}
