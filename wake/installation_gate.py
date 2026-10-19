"""Installation-local serialization of provider effects and shared quota recovery.

This is ephemeral scheduling, not a second durable record. Confirmed grants have
no expiry: only a matching release or confirmed worker death can free them.
Unconfirmed reservations cannot authorize effects and may be reclaimed.
"""

from collections import deque
from datetime import datetime
import math
import secrets
import threading
import time
from zoneinfo import ZoneInfo


_PACIFIC = ZoneInfo("America/Los_Angeles")
_RESULTS = frozenset({"success", "daily_quota", "rate_limited", "http_failure",
                      "transient_failure", "connection_failure", "invalid_response",
                      "operator_paused"})
_CATEGORIES = frozenset({"quota", "connection", "tls", "invalid_response", "http",
                         "authentication", "permission"})


def _safe_outcome(outcome):
    """Keep scheduling facts only; raw provider content never enters this queue."""
    if not isinstance(outcome, dict):
        return {}
    safe = {}
    if isinstance(outcome.get("result"), str) and outcome["result"] in _RESULTS:
        safe["result"] = outcome["result"]
    if isinstance(outcome.get("category"), str) and outcome["category"] in _CATEGORIES:
        safe["category"] = outcome["category"]
    status = outcome.get("http_status")
    if type(status) is int and 100 <= status <= 599:
        safe["http_status"] = status
    delay = outcome.get("retry_after_seconds")
    if type(delay) in (float, int) and math.isfinite(delay) and delay >= 0:
        safe["retry_after_seconds"] = min(float(delay), 86400.0)
    ids = outcome.get("quota_ids")
    if isinstance(ids, (list, tuple)):
        # Only quota classifications affect scheduling; don't retain arbitrary
        # strings supplied under a quota field in status or telemetry.
        safe["quota_ids"] = [value for value in ids[:32]
                             if isinstance(value, str) and len(value) <= 200
                             and value.startswith("GenerateRequestsPer")
                             and value.replace("_", "").replace("-", "").isalnum()]
    return safe


class InstallationSlotUnavailable(Exception):
    """A shared limit prevented a request; no provider effect has occurred."""

    def __init__(self, reason, retry_after_seconds):
        self.retry_after_seconds = max(0.1, float(retry_after_seconds))
        self.outcome = {"result": reason, "provider_call_made": False,
                        "retry_after_seconds": self.retry_after_seconds}
        if reason == "access_blocked":
            self.outcome["category"] = "permission"
        super().__init__("Installation provider slot unavailable: " + reason)


class InstallationCallCoordinator:
    """A thread-safe, single-flight FIFO shared by every installation node."""

    def __init__(self, *, clock=time.time, queue_ttl=30.0):
        self.clock = clock
        self.queue_ttl = queue_ttl
        self.lock = threading.Lock()
        self.queue = deque()
        self.tickets = {}
        self.active = None
        self.models = {}

    def _prune(self, now, *, reservations=True):
        if (reservations and self.active and not self.active.get('confirmed', True)
                and now - self.active['started'] > self.queue_ttl):
            self.active = None
        for key in list(self.queue):
            if now - self.tickets[key]["seen"] > self.queue_ttl:
                self.queue.remove(key)
                self.tickets.pop(key)

    @staticmethod
    def _probe_start(now):
        local = datetime.fromtimestamp(now, _PACIFIC)
        start = local.replace(hour=23, minute=55, second=0, microsecond=0)
        # Quota discovered during the reset window can be probed in five minutes;
        # waiting another whole day would hide a still-exhausted reset window.
        if local.hour == 0 or local >= start:
            return now + 300
        return start.timestamp()

    def _eligibility(self, model, now):
        state = self.models.get(model, {})
        if state.get("blocked"):
            return False, 300.0, "access_blocked"
        until = max(state.get("retry_at", 0), state.get("probe_at", 0))
        if until > now:
            return False, until - now, "daily_quota" if state.get("daily") else "rate_limited"
        return True, 0, "ready"

    def acquire(self, key, model, lease_seconds=120, *, confirmation_required=False):
        """Poll a stable request key; lease_seconds never permits overlapping calls."""
        key = tuple(key)
        if len(key) != 3 or not all(isinstance(part, str) and part for part in key):
            raise ValueError("Expected (group, member, request) key")
        if not isinstance(model, str) or not model:
            raise ValueError("Expected model name")
        if type(confirmation_required) is not bool:
            raise ValueError('Invalid confirmation mode')
        with self.lock:
            now = self.clock()
            self._prune(now)
            if self.active and self.active["key"] == key:
                if (self.active["model"] != model
                        or self.active.get('confirmation_required', False) != confirmation_required):
                    raise ValueError("An active request cannot change model")
                return self._grant_packet()
            ticket = self.tickets.get(key)
            if ticket is None:
                ticket = {"model": model, "seen": now, 'confirmation_required': confirmation_required}
                self.tickets[key] = ticket
                self.queue.append(key)
            elif ticket["model"] != model or ticket['confirmation_required'] != confirmation_required:
                raise ValueError("A queued request cannot change model")
            ticket["seen"] = now
            eligible, delay, reason = self._eligibility(model, now)
            first = next((item for item in self.queue
                          if self._eligibility(self.tickets[item]["model"], now)[0]), None)
            if self.active is None and eligible and first == key:
                token = secrets.token_urlsafe(24)
                self.active = {"key": key, "model": model, "token": token, "started": now,
                               'confirmed': not ticket['confirmation_required'],
                               'confirmation_required': ticket['confirmation_required']}
                self.queue.remove(key)
                self.tickets.pop(key)
                state = self.models.get(model, {})
                if state.get("daily") and self.active['confirmed']:
                    state["probe_at"] = now + 300
                return self._grant_packet()
            return {"status": "queued", "retry_after": max(0.1, delay or 1.0),
                    "reason": reason if not eligible else "busy" if self.active else "fifo"}

    def _grant_packet(self):
        return {'status': 'granted', 'token': self.active['token'],
                **({'confirmation_required': True} if self.active.get('confirmation_required') else {})}

    def confirm(self, key, token):
        """Confirm receipt before an effect; stale tokens can never revive a slot."""
        with self.lock:
            now = self.clock()
            self._prune(now)
            if (not self.active or self.active['key'] != tuple(key)
                    or not isinstance(token, str)
                    or not secrets.compare_digest(token, self.active['token'])):
                return False
            if not self.active.get('confirmed', True):
                self.active['confirmed'] = True
                state = self.models.get(self.active['model'], {})
                if state.get('daily'):
                    state['probe_at'] = now + 300
            return True

    def release(self, key, token, outcome=None, *, persist=None):
        """Apply limits, persist them while held, then allow the next request.

        persist receives a detached scheduling-state packet. It must not call
        back into this coordinator: the scheduling lock remains held. A failed
        write deliberately retains the slot until explicit recovery.
        """
        with self.lock:
            if not self.active or self.active["key"] != tuple(key) or not isinstance(token, str) or not secrets.compare_digest(self.active["token"], token):
                return False
            now = self.clock()
            model = self.active["model"]
            facts = _safe_outcome(outcome)
            state = self.models.setdefault(model, {})
            if facts.get("result") == "success":
                state.clear()
            elif facts.get("http_status") in (401, 403):
                state["blocked"] = True
            elif facts.get("result") == "daily_quota" or any("PerDay" in value for value in facts.get("quota_ids", [])):
                if not state.get("daily"):
                    state.update(daily=True, probe_at=self._probe_start(now))
                else:
                    state["probe_at"] = max(state.get("probe_at", 0), now + 300)
            elif facts.get("result") == "rate_limited" or facts.get("http_status") == 429:
                state["retry_at"] = now + facts.get("retry_after_seconds", 60)
            if persist is not None:
                self.active["release_unresolved"] = True
                persist({"version": 1, "models": {name: dict(limit)
                    for name, limit in self.models.items() if limit}})
            self.active = None
            return True

    def cancel_request(self, key):
        """Cancel queues or unconfirmed reservations, never confirmed effects."""
        key = tuple(key)
        with self.lock:
            if self.active and self.active['key'] == key and not self.active.get('confirmed', True):
                self.active = None
                return True
            if key not in self.tickets:
                return False
            self.tickets.pop(key)
            self.queue.remove(key)
            return True

    def dump_state(self):
        """Persist only shared scheduling limits, without leases or worker data."""
        with self.lock:
            return {"version": 1, "models": {model: dict(state)
                                             for model, state in self.models.items() if state}}

    def restore_state(self, packet):
        """Restore limits before spawning workers; old workers must already be dead."""
        if not isinstance(packet, dict) or packet.get("version") != 1 or not isinstance(packet.get("models"), dict):
            raise ValueError("Invalid installation scheduling state")
        restored = {}
        for model, state in packet["models"].items():
            if not isinstance(model, str) or not model or not isinstance(state, dict):
                raise ValueError("Invalid model scheduling state")
            clean = {}
            for field in ("blocked", "daily"):
                if field in state:
                    if type(state[field]) is not bool:
                        raise ValueError("Invalid scheduling flag")
                    clean[field] = state[field]
            for field in ("retry_at", "probe_at"):
                if field in state:
                    value = state[field]
                    if type(value) not in (float, int) or not math.isfinite(value) or value < 0:
                        raise ValueError("Invalid scheduling deadline")
                    clean[field] = value
            if clean.get("daily") and "probe_at" not in clean:
                raise ValueError("Missing daily recovery deadline")
            if clean:
                restored[model] = clean
        with self.lock:
            if self.active or self.queue:
                raise RuntimeError("Cannot restore limits while requests exist")
            self.models = restored

    def cancel_member(self, member):
        """Controller-only recovery after it has proved this member process is dead."""
        with self.lock:
            removed = 0
            for key in list(self.queue):
                if key[1] == member:
                    self.queue.remove(key)
                    self.tickets.pop(key)
                    removed += 1
            if self.active and self.active["key"][1] == member:
                self.active = None
                removed += 1
            return removed

    def clear_model(self, model):
        """Explicit operator recovery after changing provider access/configuration."""
        with self.lock:
            self.models.pop(model, None)

    def status(self):
        """Return bounded scheduler facts without tokens or provider content."""
        with self.lock:
            now = self.clock()
            # Observation does not retire a reservation. The next acquire or
            # confirmation applies its deadline before allowing any effect.
            self._prune(now, reservations=False)
            active = None
            if self.active:
                active = {"group": self.active["key"][0], "member": self.active["key"][1],
                          "model": self.active["model"],
                          "elapsed_seconds": max(0, now - self.active["started"]),
                          'confirmed': self.active.get('confirmed', True),
                          "release_unresolved": self.active.get("release_unresolved", False)}
            return {"active": active, "queued": len(self.queue),
                    "models": {model: dict(state) for model, state in self.models.items() if state}}
