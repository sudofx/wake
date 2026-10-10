"""Best-effort provider-call coordination for local wake_runner groups."""

from contextlib import contextmanager
import json
import os
import sys
import time
from urllib.request import ProxyHandler, Request, build_opener
import uuid


class GroupProviderGate:
    """Ask the local group router for a fair provider-call slot; fail open."""

    def __init__(self, url, member, *, timeout_seconds=60):
        self.url = url
        self.member = member
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
        with self.opener.open(request, timeout=10) as response:
            return json.loads(response.read(4096))

    def _acquire(self, request_id, model):
        deadline = time.monotonic() + self.wait_seconds
        while time.monotonic() < deadline:
            packet = self._request({
                "action": "acquire", "member": self.member,
                "request_id": request_id, "model": model,
                "lease_seconds": self.lease_seconds,
            })
            if packet.get("status") == "granted" and isinstance(packet.get("token"), str):
                return packet["token"]
            if packet.get("status") != "queued":
                raise ValueError("group coordinator returned an unknown status")
            time.sleep(min(1.0, max(0.1, float(packet.get("retry_after", 1.0)))))
        raise TimeoutError("local group provider slot was not available in time")

    @contextmanager
    def request(self, model):
        request_id = uuid.uuid4().hex
        token = None
        try:
            token = self._acquire(request_id, model)
        except Exception as exc:
            print(
                f"WAKE group call coordination unavailable; continuing independently ({type(exc).__name__}).",
                file=sys.stderr,
                flush=True,
            )
        try:
            yield
        finally:
            if token:
                try:
                    self._request({
                        "action": "release", "member": self.member,
                        "request_id": request_id, "token": token,
                    })
                except Exception as exc:
                    print(
                        f"WAKE group call slot release unavailable; it will expire automatically ({type(exc).__name__}).",
                        file=sys.stderr,
                        flush=True,
                    )


def group_provider_gate(settings):
    """Return a gate only for locally grouped standalone containers."""
    url = os.environ.get("WAKE_GROUP_COORDINATOR_URL", "")
    member = os.environ.get("WAKE_GROUP_INSTANCE", "")
    if not url or not member:
        return None
    return GroupProviderGate(url, member, timeout_seconds=settings.get("timeout_seconds", 60))
