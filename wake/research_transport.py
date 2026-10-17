"""Disposable, same-origin Console transport derived from the full export.

The overview retains recorded counts and bounded chart samples. Provider input,
output and event details travel only when a reader opens a wake. Neither file is
an authority source; research-data.json remains the complete exported projection.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path


CONTEXT_GROUPS = {
    'objectives': ('objective', 'mission'),
    'constraints': ('bounded_context',),
    'frontier': ('projects', 'research', 'working_notebook'),
    'results': ('notebooks', 'beliefs', 'evidence', 'project_evidence'),
}
MAX_OVERVIEW_BYTES = 2 * 1024 * 1024
MAX_WAKE_SUMMARIES = 24
MAX_ACTIVITY = 48


def _json(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def export_research_transport(research, target):
    """Write an overview and immutable, content-addressed selected-wake details.

    Preserve missing phases as missing. An exported detail is not a promise that
    its start/terminal events survived the bounded event tail.
    """
    from .report import atomic_write

    target = Path(target)
    overview = {key: deepcopy(value) for key, value in research.items() if key != 'wakes'}
    overview['transport'] = {'schema': 1, 'kind': 'research-overview',
                             'complete_projection': 'research-data.json',
                             'wake_trace_count': len(research.get('wakes', [])),
                             'overview_budget_bytes': MAX_OVERVIEW_BYTES}
    overview['activity'] = overview.get('activity', [])[:MAX_ACTIVITY]
    quality = overview.get('evidence_quality')
    if quality:
        quality['reused_works_count'] = len(quality.get('reused_works', []))
        for key in ('reused_works', 'notebooks', 'uncited_readable_source_ids'):
            quality.pop(key, None)
    for rows in overview.get('records', {}).values():
        for row in rows:
            for key in ('claims', 'support_provenance'):
                row.pop(key, None)
    for node in overview.get('graph', {}).get('nodes', []):
        for key in ('claims', 'support_provenance'):
            node.get('detail', {}).pop(key, None)
    projects = {row['id'] for row in overview.get('records', {}).get('projects', [])}
    frontier = overview.get('frontier', {})
    frontier['acquisition'] = [row for row in frontier.get('acquisition', []) if row.get('project') in projects]
    frontier.pop('deferred_topics', None)
    # The cube displays all scores and each selected cell's diagnostics. Nested
    # contributions display only the node and outcome, not duplicate diagnostics.
    for cell in overview.get('matrix', {}).get('cells', []):
        for contribution in cell.get('contributions', []):
            contribution.pop('diagnostics', None)
    overview['wakes'] = []
    overview['chart_wakes'] = []
    for wake in research.get('wakes', []):
        # Installation attribution names the current export head and therefore
        # changes between snapshots. Keep it in the overview, so unchanged wake
        # transcripts retain the same immutable path as later research arrives.
        detail = _json({'schema': 1, 'wake': {key: value for key, value in wake.items() if key != 'origin'}})
        filename = f'research-details/{hashlib.sha256(detail.encode()).hexdigest()}.json'
        atomic_write(target / filename, detail)
        row = {key: deepcopy(value) for key, value in wake.items()
               if key not in ('context', 'response', 'events', 'context_delivery', 'receipt')}
        context = wake.get('context') or {}
        row['context'] = {key: deepcopy(context[key]) for key in ('available', 'characters') if key in context}
        row['receipt'] = {key: deepcopy(wake.get('receipt', {})[key]) for key in ('available', 'seq') if key in wake.get('receipt', {})}
        row['context_delivery'] = {key: deepcopy(wake.get('context_delivery', {})[key])
                                   for key in ('delivered_request_chars', 'rich_context_chars', 'request_compression_ratio')
                                   if key in wake.get('context_delivery', {})}
        delivered = (context.get('request') or {}).get('context')
        if isinstance(delivered, dict):
            # Match the existing chart's serialized-character definition exactly.
            row['context_allocation'] = {
                name: sum(len(_json(delivered[key]).encode('utf-16-le')) // 2
                          for key in keys if key in delivered)
                for name, keys in CONTEXT_GROUPS.items()
            }
        row['detail_url'] = filename
        if len(overview['wakes']) < MAX_WAKE_SUMMARIES:
            overview['wakes'].append(row)
        chart = {key: deepcopy(row[key]) for key in
                 ('id', 'time', 'finished', 'status', 'topic', 'origin', 'request_hash',
                  'detail_url', 'context_delivery', 'context_allocation') if key in row}
        chart['attempts'] = [{key: deepcopy(attempt[key]) for key in ('result', 'elapsed_ms', 'usage') if key in attempt}
                             for attempt in wake.get('attempts', [])]
        overview['chart_wakes'].append(chart)
    # Current graph/record lists are an overview, not full-history metrics. Reduce
    # those lists if unusually large summaries exhaust the transport budget;
    # never clip counters, chart measurements or cube scores to meet the budget.
    overview['transport']['wake_summary_count'] = len(overview['wakes'])
    while len(_json(overview).encode()) > MAX_OVERVIEW_BYTES:
        graph = overview.get('graph', {})
        nodes = graph.get('nodes', [])
        records = overview.get('records', {})
        if len(nodes) > 24 or any(len(rows) > 8 for rows in records.values()):
            graph['nodes'] = nodes[:max(24, len(nodes) // 2)]
            graph['truncated'] = True
            ids = {node['id'] for node in graph.get('nodes', [])}
            graph['edges'] = [edge for edge in graph.get('edges', []) if edge['source'] in ids and edge['target'] in ids]
            for collection, rows in records.items():
                records[collection] = rows[:max(8, len(rows) // 2)]
            overview['transport']['record_overview_limited'] = True
        else:
            raise ValueError('Console metrics and cube exceed the overview transport budget')
    atomic_write(target / 'research-overview.json', _json(overview))
    return overview
