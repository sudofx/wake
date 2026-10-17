"""Disposable mirror delivery state; reads only completed exported generations."""
from pathlib import Path
import json
import math
import os
import time

from .event_format import digest

DEFAULT_INTERVAL_SECONDS = 30 * 60


def interval_seconds():
    value = float(os.environ.get('WAKE_MIRROR_INTERVAL_SECONDS', DEFAULT_INTERVAL_SECONDS))
    if not math.isfinite(value) or value < 60:
        raise ValueError('WAKE_MIRROR_INTERVAL_SECONDS must be at least 60')
    return value


def heads_digest(record_heads):
    # Include missing members explicitly. Versions and generation timestamps are
    # presentation metadata; the immutable head identifies the captured record.
    from .installation_cli import NODE_IDS
    return digest({node: record_heads.get(node, {}).get('head') for node in NODE_IDS})


def exported_identity(root):
    from .installation_cli import NODE_IDS
    heads = {}
    for node in NODE_IDS:
        try:
            head = (Path(root) / 'nodes' / node / 'site/current/head.txt').read_text().strip()
            if len(head) == 64 and all(c in '0123456789abcdef' for c in head):
                heads[node] = {'head': head}
        except OSError:
            pass
    # The leader exports the accepted article independently of follower export
    # availability. Reading this public packet never grants editorial authority.
    try:
        publication = json.loads((Path(root) / 'nodes/100.wake/site/current/group/bob-publication.json').read_text())
        article = digest(publication) if publication else None
    except (OSError, ValueError):
        article = None
    return {'export_digest': heads_digest(heads), 'publication_digest': article,
            'available_exports': len(heads)}


def delivery_due(status, identity, now=None):
    now = time.time() if now is None else now
    if not status.get('enabled') or status.get('retry_at', 0) > now or not identity['available_exports']:
        return False
    changed = identity['export_digest'] != status.get('published_export_digest')
    article = identity.get('publication_digest')
    immediate = article and article != status.get('published_digest')
    return bool(changed and (immediate or now >= status.get('next_capture_at', 0)))


def acknowledge(status, manifest, now=None):
    from datetime import datetime, timezone
    now = time.time() if now is None else now
    status.update(status='published', published_export_digest=manifest['export_digest'],
                  published_digest=manifest.get('publication_digest'), retry_at=0,
                  published_at=datetime.fromtimestamp(now, timezone.utc).isoformat(),
                  next_capture_at=now + status.get('interval_seconds', interval_seconds()))
    for key in ('error', 'queued_digest', 'queued_export_digest'):
        status.pop(key, None)
    return status


def mirror_status(root):
    root = Path(root)
    path = root / 'public-mirror.json'
    status = json.loads(path.read_text()) if path.exists() else {'enabled': False}
    receipt = root / 'public-mirror-host.json'
    if status.get('delivery') == 'host' and receipt.exists():
        # Host receipts cannot enable delivery, replace configuration, or turn a
        # disabled mirror back on. They report only the completed upload/retry.
        try:
            host = json.loads(receipt.read_text())
            if not isinstance(host, dict):
                raise ValueError('Invalid host delivery receipt')
        except (OSError, ValueError):
            host = {}
            status['host_receipt_error'] = 'unreadable'
        for key in ('published_export_digest', 'published_digest', 'published_at',
                    'next_capture_at', 'retry_at', 'error', 'status'):
            if key in host:
                status[key] = host[key]
    if not status.get('enabled'):
        status['status'] = 'disabled'
    return status
