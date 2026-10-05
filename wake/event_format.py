"""Stable WAKE event-format primitives shared by legacy replay and sudofx-backed runtime.

These functions define byte/identity semantics, not storage authority. Keep their
output stable so historical WAKE event hashes remain replayable across the authority transition.
"""

from datetime import datetime, timezone
import hashlib
import json

ZERO = "0" * 64


def canonical(value):
    """Return the exact canonical JSON encoding used by WAKE event identities."""
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    )


def digest(value):
    """Hash one canonical WAKE value without implying storage authority."""
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def now():
    """Return the historical WAKE UTC timestamp format."""
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")
