"""Ephemeral inspection telemetry. Never replay it or use it as authority.

Only stages and public invocation/matrix identifiers leave the process. Sampling
acknowledges a live server; it does not imply an accepted research transition.
"""
from datetime import datetime, timezone
import threading
import uuid

STAGES = frozenset({'idle', 'record', 'context', 'collecting', 'provider',
                    'governance', 'continuity', 'receipt'})


class RuntimeActivity:
    def __init__(self):
        self.runtime_id = uuid.uuid4().hex
        self._lock = threading.Lock()
        self.update(stage='idle')

    def update(self, *, stage, invocation_id=None, coordinate_id=None):
        if stage not in STAGES:
            raise ValueError('Unknown activity stage')
        with self._lock:
            self._activity = {
                'stage': stage, 'active': stage != 'idle',
                'invocation_id': invocation_id, 'coordinate_id': coordinate_id,
                'started_at': datetime.now(timezone.utc).isoformat(),
            }

    def snapshot(self):
        with self._lock:
            return {'activity_schema': 1, 'runtime_id': self.runtime_id,
                    'capabilities': {'live_activity': True},
                    'observed_at': datetime.now(timezone.utc).isoformat(),
                    'activity': dict(self._activity)}
