"""Provider-call coordination, mandatory for installation workers."""

from contextlib import contextmanager
from http.client import IncompleteRead
import json
import os
import sys
import time
import threading
from urllib.request import ProxyHandler, Request, build_opener
from urllib.error import HTTPError
import uuid

from .providers import ProviderCallPaused
from .installation_gate import InstallationSlotUnavailable


class _ReleaseRetrier:
    """Retry internal matching releases, never provider effects or grant expiry."""

    def __init__(self):
        self.lock = threading.Lock()
        self.pending = {}
        self.running = False

    def add(self, gate, packet):
        with self.lock:
            key = (gate.url, gate.member, packet['request_id'])
            self.pending[key] = (gate, dict(packet))
            if self.running:
                return
            self.running = True
        threading.Thread(target=self.run, daemon=True).start()

    def retry(self):
        with self.lock:
            pending = list(self.pending.items())
        for key, (gate, packet) in pending:
            try:
                gate._release(packet)
            except Exception:
                continue
            with self.lock:
                self.pending.pop(key, None)

    def run(self):
        while True:
            self.retry()
            with self.lock:
                if not self.pending:
                    self.running = False
                    return
            time.sleep(2)


_releases = _ReleaseRetrier()


class GroupProviderGate:
    """Ask the controller for a fair slot; installation workers fail closed."""

    def __init__(self, url, member, *, timeout_seconds=60, should_pause=None):
        self.url = url
        self.member = member
        self.should_pause = should_pause
        self.wait_seconds = max(60, min(1800, float(timeout_seconds) * 20))
        self.lease_seconds = max(120, min(900, float(timeout_seconds) + 60))
        self.opener = build_opener(ProxyHandler({}))

    def _request(self, payload):
        request = Request(
            self.url,
            data=json.dumps(payload, separators=(",", ":")).encode(),
            headers={"Content-Type": "application/json", "Accept": "application/json"},
            method="POST",
        )
        if os.environ.get('WAKE_INSTALLATION_TOKEN'):
            request.add_header('Authorization', 'Bearer ' + os.environ['WAKE_INSTALLATION_TOKEN'])
        with self.opener.open(request, timeout=30) as response:
            return json.loads(response.read(4096))

    def _request_reliably(self, payload):
        # A lost response may follow a granted slot or a completed release.
        # Retry the same identity/token: the controller makes both idempotent.
        # Exhaustion retains the existing fail-closed, confirmed-death boundary.
        for attempt in range(3):
            try:
                return self._request(payload)
            except HTTPError as error:
                error.close()
                raise
            except (OSError, IncompleteRead, json.JSONDecodeError, UnicodeDecodeError):
                if attempt == 2:
                    raise
                time.sleep(.1 * (attempt + 1))

    def _acquire(self, request_id, model):
        deadline = time.monotonic() + self.wait_seconds
        pacing_deadline = time.monotonic() + 3600
        while time.monotonic() < deadline:
            self._check_pause()
            packet = self._request_reliably({
                "action": "acquire", "member": self.member,
                "request_id": request_id, "model": model,
                "lease_seconds": self.lease_seconds,
                "confirmation_required": True,
                "purpose":getattr(self,'purpose','research'),
                **({"editorial_nonce": self.editorial_nonce} if getattr(self, "editorial_nonce", None) else {}),
            })
            if packet.get("status") == "granted" and isinstance(packet.get("token"), str):
                if packet.get('confirmation_required') is True:
                    token = packet['token']
                    try:
                        self._check_pause()
                        confirmed = self._request_reliably({
                            'action': 'confirm', 'member': self.member,
                            'request_id': request_id, 'token': token,
                            **({'editorial_nonce': self.editorial_nonce} if getattr(self, 'editorial_nonce', None) else {}),
                            **({'purpose': 'reader'} if getattr(self, 'purpose', None) == 'reader' else {}),
                        })
                        if confirmed.get('status') == 'expired':
                            continue
                        if confirmed.get('status') != 'confirmed':
                            raise ValueError('Invalid provider slot confirmation')
                    except Exception:
                        # The token is known, but the caller has not entered the
                        # effect boundary. A lost confirmation reply is released
                        # with that exact identity, including across later waits.
                        self._release_or_defer({'action': 'release', 'member': self.member,
                            'request_id': request_id, 'token': token})
                        raise
                return packet["token"]
            if packet.get("status") != "queued":
                raise ValueError("group coordinator returned an unknown status")
            if packet.get("reason") in {"daily_quota", "rate_limited", "access_blocked","research_budget"}:
                raise InstallationSlotUnavailable(packet["reason"], packet.get("retry_after", 300))
            if packet.get('reason')=='pacing':
                # Twelve fair turns at the 24-hour cadence can exceed the old
                # latency-only allowance. Extend waiting, never an API timeout.
                deadline=max(deadline,min(pacing_deadline,time.monotonic()+1800))
            # Installation HTTP long-polls for a slot change. After a bounded
            # empty response, retry promptly rather than adding another second.
            if os.environ.get('WAKE_INSTALLATION_WORKER') == '1':
                time.sleep(min(.05, max(.02, float(packet.get("retry_after", .05)))))
            else:
                time.sleep(min(1.0, max(0.1, float(packet.get("retry_after", 1.0)))))
        raise TimeoutError("local group provider slot was not available in time")

    def _cancel_queued(self, request_id):
        if not self.url:
            return
        try:
            self._request({"action": "cancel", "member": self.member,
                           "request_id": request_id})
        except Exception:
            # Cancellation never frees a grant. Queued tickets can expire; an
            # uncertain active grant requires controller-proven process death.
            pass

    def _check_pause(self):
        if self.should_pause and self.should_pause():
            raise ProviderCallPaused('Local research paused before provider call; no request was sent')

    def _release(self, packet):
        result = self._request_reliably(packet)
        if result.get('status') not in ('released', 'expired'):
            raise ValueError('Invalid provider slot release acknowledgment')

    def _release_or_defer(self, packet):
        try:
            self._release(packet)
        except Exception:
            _releases.add(self, packet)
            print('WAKE group call release is pending; retrying the same internal release without repeating the provider call.',
                  file=sys.stderr, flush=True)

    @contextmanager
    def request(self, model):
        request_id = uuid.uuid4().hex
        token = None
        self._check_pause()
        self.outcome = {}
        strict = os.environ.get('WAKE_INSTALLATION_WORKER') == '1'
        try:
            if strict and (not self.url or not self.member):
                raise ProviderCallPaused('Installation controller missing; no request was sent')
            if self.url:
                token = self._acquire(request_id, model)
        except (ProviderCallPaused, InstallationSlotUnavailable):
            self._cancel_queued(request_id)
            raise
        except Exception as exc:
            self._cancel_queued(request_id)
            if strict:
                raise ProviderCallPaused('Installation controller unavailable; no request was sent') from exc
            print(
                f"WAKE group call coordination unavailable; continuing independently ({type(exc).__name__}).",
                file=sys.stderr,
                flush=True,
            )
        try:
            self._check_pause()
            yield bool(token)
        finally:
            if token:
                packet = {'action': 'release', 'member': self.member,
                          'request_id': request_id, 'token': token}
                if hasattr(self, 'outcome'):
                    packet['outcome'] = dict(self.outcome) if isinstance(self.outcome, dict) else {}
                self._release_or_defer(packet)


def group_provider_gate(settings, *, should_pause=None):
    """Return a gate only for locally grouped standalone containers."""
    url = os.environ.get("WAKE_GROUP_COORDINATOR_URL", "")
    # The gateway indexes configured members by their public route hostname;
    # WAKE_GROUP_INSTANCE is an internal peer-discovery alias instead.
    member = os.environ.get("WAKE_PUBLIC_HOSTNAME", "").lower()
    if (not url or not member) and should_pause is None and os.environ.get("WAKE_INSTALLATION_WORKER") != "1":
        return None
    return GroupProviderGate(url if member else '', member,
                             timeout_seconds=settings.get("timeout_seconds", 60),
                             should_pause=should_pause)
