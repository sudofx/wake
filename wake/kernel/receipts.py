"""Versioned attribution for new receipts; historical attribution stays untouched."""
from datetime import datetime, timezone

SCHEMA = 'wake-receipt@1'
FIELDS = ('who', 'what', 'where', 'why', 'how', 'when')


def receipt_provenance(provenance, *, what, where, why, how):
    """Bind caller attribution and observed execution facts, never permissions."""
    data = dict(provenance or {})
    data.update(receipt_schema=SCHEMA,
                who=data.get('actor') or 'Caller identity not supplied',
                what=what, where=where or 'Execution location not supplied',
                why=why or data.get('purpose') or 'Reason not supplied',
                how=how + (f"; source: {data['source']}" if data.get('source') else ''),
                when=datetime.now(timezone.utc).isoformat())
    return data
