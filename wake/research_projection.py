"""Bounded Research✳︎ presentation. Never consumed by runtime or governance.

All graph edges come from provenance.build_map. Source readiness describes
retrieval depth, not claim support, scientific correctness, or publication.
"""
from collections import Counter
from copy import deepcopy
from datetime import datetime, timedelta, timezone
import json
from urllib.parse import urlsplit

from .evidence_quality import evidence_quality
from .provenance import build_map
from .research import effective_evidence_role, effective_host_tier, source_observation_readable

MAX_ACTIVITY = 48
MAX_GRAPH_NODES = 240
MAX_RECORDS = 80


def _text(value, limit=360):
    return str(value or '')[:limit]


def _payload(item):
    try:
        value = json.loads(item.get('content', ''))
        return value if isinstance(value, dict) else {}
    except (ValueError, TypeError):
        return {}


def _evidence_class(item):
    if str(item.get('source', '')).startswith('runtime:'):
        return 'receipt'
    payload = _payload(item)
    if not payload:
        return 'unclassified'
    role = effective_evidence_role(item.get('source', ''), payload)
    if role in ('discovery', 'metadata'):
        return role
    if effective_host_tier(item.get('source', ''), payload) == 'verification-metadata':
        return 'metadata'
    if not payload.get('excerpt') or not source_observation_readable(payload):
        return 'unreadable'
    return 'source'


def build_research_projection(state, events, head, *, generated=None, metrics=None,
                              operation=None, source=None, graph=None, matrix_progress=None, matrix_reported=False):
    """Project an already verified snapshot; no database reads or writes."""
    generated = generated or datetime.now(timezone.utc).isoformat()
    metrics = metrics or {}
    invocations = sorted(state.get('invocations', {}).values(), key=lambda x: x.get('time', ''))
    completed = [x for x in invocations if x.get('status') in ('accepted', 'rejected', 'deferred', 'failed')]
    outcomes = dict(Counter(x['status'] for x in completed))
    records = {}
    fields = ('id', 'title', 'question', 'next_step', 'summary', 'findings', 'limitations',
              'next_questions', 'statement', 'task', 'status', 'domain', 'project', 'reason',
              'revision', 'confidence', 'due_cycle', 'updated_version', 'created_version',
              'updated_by', 'created_by', 'resolved_by')
    totals = {}
    for collection in ('projects', 'notebooks', 'beliefs', 'commitments', 'research'):
        items = sorted(state.get(collection, {}).values(),
                       key=lambda x: (x.get('status') == 'active', x.get('updated_version', x.get('created_version', 0))), reverse=True)
        totals[collection] = len(items)
        records[collection] = [{**{k: (_text(x[k], 700) if isinstance(x[k], str) else deepcopy(x[k]))
                                   for k in fields if k in x},
                                'evidence': list(x.get('evidence', []))[:24]}
                               for x in items[:MAX_RECORDS]]
    evidence = state.get('evidence', {})
    classes = {key: _evidence_class(item) for key, item in evidence.items()}
    counts = dict(Counter(classes.values()))
    hosts = Counter(urlsplit(x.get('source', '')).hostname for x in evidence.values()
                    if urlsplit(x.get('source', '')).scheme in ('http', 'https'))
    source_works = {
        str(_payload(item).get('source_identity') or 'url:' + item.get('source', '')).strip().lower()
        for key, item in evidence.items() if classes[key] == 'source'
    }
    recent_evidence = sorted(evidence.values(), key=lambda x: x.get('time', ''), reverse=True)
    recent_evidence = [x for x in recent_evidence if classes.get(x['id']) != 'receipt'][:12]
    activity = []
    for item in reversed(completed[-MAX_ACTIVITY:]):
        attempts = item.get('provider_attempts', [])
        activity.append({'id': item['id'], 'time': item.get('finished') or item.get('time'),
                         'status': item['status'], 'reason': _text(item.get('reason'), 500),
                         'model': item.get('successful_model') or item.get('model'),
                         'provider': item.get('provider'),
                         'requests': item.get('provider_requests_sent'),
                         'attempts': len(attempts) if 'provider_attempts' in item else None})
    # Hour bins use all durable invocation timestamps, not the 400-event tail.
    bins = {}
    for item in completed:
        try:
            stamp = datetime.fromisoformat(item.get('finished') or item['time']).astimezone(timezone.utc)
        except (ValueError, KeyError):
            continue
        key = stamp.replace(minute=0, second=0, microsecond=0).isoformat()
        bins.setdefault(key, Counter())[item['status']] += 1
    series = []
    if bins:
        end = datetime.fromisoformat(max(bins))
        start = max(datetime.fromisoformat(min(bins)), end - timedelta(hours=23))
        while start <= end:
            key = start.isoformat()
            series.append({'time': key, **dict(bins.get(key, {}))})
            start += timedelta(hours=1)
    graph = graph or build_map(state, events, head, replay_history=False)
    # Current research objects first, then explicitly linked evidence. History,
    # editorial and runtime receipts remain in the existing full map.
    candidates = [n for n in graph['nodes'] if n['kind'] in ('project', 'notebook', 'belief', 'commitment', 'research')
                  and n.get('detail', {}).get('as_of_cycle') == state['version']]
    research_ids = {n['id'] for n in candidates}
    preferred = {e['target'] for e in graph['edges'] if e['relation'] == 'evidence'
                 and e['source'] in research_ids}
    candidates += [n for n in graph['nodes'] if n['kind'] == 'evidence' and n['id'] in preferred]
    overview_total = len(candidates)
    candidates = candidates[:MAX_GRAPH_NODES]
    ids = {n['id'] for n in candidates}
    nodes = []
    for n in candidates:
        detail = n.get('detail', {})
        item = {k: deepcopy(detail[k]) for k in fields if k in detail}
        if n['kind'] == 'evidence':
            eid = detail.get('id') or n['id'].removeprefix('evidence:')
            item.update(source=detail.get('source'), evidence_class=classes.get(eid, 'unclassified'))
            origin = detail.get('peer_origin')
            if isinstance(origin, dict):
                item['peer_origin'] = {
                    key: deepcopy(origin[key])
                    for key in ('instance_id', 'application_head', 'record_version',
                                'evidence_id', 'evidence_version', 'content_sha256')
                    if key in origin
                }
            payload = _payload(evidence.get(eid, {}))
            if payload.get('topic_domain'):
                item['domain'] = payload['topic_domain']
        item = {k: _text(v, 700) if isinstance(v, str) else v for k, v in item.items()}
        nodes.append({'id': n['id'], 'kind': n['kind'], 'title': _text(n.get('title'), 160), 'detail': item})
    latest = completed[-1] if completed else {}
    traces = _wake_traces(invocations, events, state)
    matrix = _matrix_projection(matrix_progress, matrix_reported)
    pending_id = state.get('pending')
    pending = state.get('invocations', {}).get(pending_id, {})
    probe = (pending.get('continuity_probe_shadow') or {}).get('context', {})
    recorded_activity = {'source': 'published-record', 'active': False,
                         'invocation_id': pending_id,
                         'coordinate_id': probe.get('campaign', {}).get('coordinate_id'),
                         'recorded_at': generated}
    accepted = [i for i in completed if i['status'] == 'accepted']
    actions = metrics.get('accepted_actions', {})
    return {
        'projection_schema': 1, 'projection_kind': 'disposable-research-view', 'authoritative': False,
        'recorded_activity': recorded_activity,
        'head': head, 'version': state['version'], 'generated': generated, 'source': deepcopy(source or {}),
        'topics': [{'id': t['id'], 'label': t.get('label', t['id'])} for t in state.get('research_topics', [])],
        'status': {'accepted_cycles': state['version'], 'latest': activity[0] if activity else None,
                   'last_accepted': {'id': accepted[-1]['id'], 'time': accepted[-1].get('finished') or accepted[-1].get('time')} if accepted else None,
                   'active_projects': sum(x.get('status') == 'active' for x in state.get('projects', {}).values()),
                   'open_commitments': sum(x.get('status') == 'open' for x in state.get('commitments', {}).values()),
                   'pending': bool(state.get('pending')), 'next_eligible': (operation or {}).get('wake_status', {}).get('next_eligible'),
                   'attention_topic': state.get('attention', {}).get('attention', {}).get('topic'),
                   'regime': deepcopy(state.get('experimental', {}).get('controls', {}).get('time_dilation', {}))},
        'records': records, 'record_totals': totals,
        'evidence_quality': evidence_quality(state),
        'frontier': {'acquisition': [{k: deepcopy(x[k]) for k in ('project', 'capability_blocked', 'stage', 'last_outcome', 'consecutive_no_progress') if k in x}
                                    | {'project': key} for key, x in state.get('acquisition', {}).items()],
                     'deferred_topics': list(state.get('attention', {}).get('deferred', {}))},
        'evidence': {'total': len(evidence), 'by_class': counts, 'source_works': len(source_works),
                     'classification_complete': not counts.get('unclassified'),
                     'classification': 'Retrieval depth; source-ready does not establish claim support or publication eligibility.',
                     'hosts': [{'host': k, 'count': v} for k, v in hosts.most_common(6) if k],
                     'recent': [{'id': x['id'], 'source': x.get('source'), 'time': x.get('time'), 'class': classes[x['id']]} for x in recent_evidence]},
        'metrics': {'completed': len(completed), 'outcomes': outcomes,
                    'research_actions': {k: v for k, v in actions.get('by_type', {}).items() if k != 'blog'},
                    'editorial_actions': actions.get('by_type', {}).get('blog', 0),
                    'by_topic': deepcopy(actions.get('by_topic', {})),
                    'rejection_reasons': sorted(({'reason': k, 'count': v} for k, v in metrics.get('rejection_reasons', {}).items()), key=lambda x: -x['count'])[:6],
                    'hourly': series, 'history_start': completed[0].get('time') if completed else None,
                    'history_end': latest.get('finished') or latest.get('time'),
                    'provider_requests': sum(x.get('provider_requests_sent', 0) for x in invocations),
                    'provider_requests_complete': all('provider_requests_sent' in x for x in invocations),
                    'storage': deepcopy(metrics.get('storage', {}))},
        'activity': activity, 'activity_total': len(completed),
        'wakes': traces, 'matrix': matrix,
        'graph': {'nodes': nodes, 'edges': [deepcopy(e) for e in graph['edges'] if e['source'] in ids and e['target'] in ids],
                  'scope': 'Current research objects and their cited evidence. Positions are layout only.',
                  'total_nodes': len(graph['nodes']), 'limit': MAX_GRAPH_NODES,
                  'overview_total': overview_total,
                  'truncated': overview_total > MAX_GRAPH_NODES},
    }


def _matrix_projection(progress, reported):
    """Coordinates use the frozen native grammar, never inferred research clusters."""
    from .matrix import MATRIX, MATRIX_KEY
    if progress is not None and (progress.get('matrix') != MATRIX_KEY or progress.get('definition_digest') != MATRIX.definition_digest):
        raise ValueError('Research matrix definition does not match continuity@1')
    axes = [{'key': a.key, 'label': a.label, 'values': [{'key': v.key, 'label': v.label, 'description': v.description} for v in a.values]} for a in MATRIX.axes]
    indices = [{v.key: i for i, v in enumerate(a.values)} for a in MATRIX.axes]
    results = (progress or {}).get('results', {})
    cells = [{'id': c.coordinate_id, 'ordinal': c.ordinal, 'position': [indices[i][key] for i, key in enumerate(c.value_keys)],
              'status': results.get(c.coordinate_id, {}).get('status', 'not_recorded'),
              'score': results.get(c.coordinate_id, {}).get('score'),
              'invocation_id': results.get(c.coordinate_id, {}).get('invocation_id'),
              'research_status': results.get(c.coordinate_id, {}).get('research_status'),
              'failed_checks': [k for k, v in results.get(c.coordinate_id, {}).get('checks', {}).items() if v is False],
              'diagnostics': deepcopy(results.get(c.coordinate_id, {}).get('diagnostics', {}))}
             for c in MATRIX.coordinates()]
    scores = [cell['score'] for cell in cells if cell['status'] == 'completed' and isinstance(cell['score'], (int, float))]
    return {'id': MATRIX_KEY, 'definition_digest': MATRIX.definition_digest, 'axes': axes,
            'cells': cells, 'reported': reported, 'enabled': bool(progress) if reported else None,
            'completed': (progress or {}).get('completed_count', 0) if reported else None,
            'next_coordinate': (progress or {}).get('next_coordinate_id'),
            'failure_counts': deepcopy((progress or {}).get('failure_counts', {})),
            'passed': (progress or {}).get('passed_count', 0) if reported else None,
            'mean_score': round(sum(scores) / len(scores), 4) if scores else None,
            'score_count': len(scores)}


def _wake_traces(invocations, events, state):
    """Observed wake lifecycle, with explicit gaps when the event tail omits a phase."""
    traces = []
    for invocation in reversed(invocations[-MAX_RECORDS:]):
        identifier = invocation['id']
        matching = [e for e in events if e.get('payload', {}).get('id') == identifier
                    or e.get('payload', {}).get('invocation') == identifier]
        start = next((e for e in matching if e['kind'] == 'invocation_started'), None)
        terminal = next((e for e in reversed(matching) if e['kind'] in ('accepted', 'rejected', 'failed', 'deferred', 'recovered', 'research_planned')), None)
        request = (start or {}).get('payload', {}).get('request', {})
        context = request.get('context', {})
        proposal = (terminal or {}).get('payload', {}).get('proposal', {})
        raw_response = (terminal or {}).get('payload', {}).get('raw_response')
        if not proposal and isinstance(raw_response, str):
            try:
                decoded = json.loads(raw_response)
                proposal = decoded if isinstance(decoded, dict) else {}
            except (ValueError, TypeError):
                pass
        actions = proposal.get('actions', [])
        actions = [a for a in actions if isinstance(a, dict)] if isinstance(actions, list) else []
        traces.append({
            'id': identifier, 'time': invocation.get('time'), 'finished': invocation.get('finished'),
            'status': invocation.get('status'), 'reason': _text(invocation.get('reason'), 1000),
            'base_version': invocation.get('base_version', (start or {}).get('payload', {}).get('base_version')), 'request_hash': invocation.get('request_hash'),
            'context': {'available': bool(start), 'receipt': context.get('receipt'),
                        'fields': list(context), 'system': request.get('system', ''), 'request': deepcopy(request),
                        'objective': _text(context.get('objective'), 700),
                        'characters': len(json.dumps(context, ensure_ascii=False)) if start else None},
            'topic': invocation.get('attention', {}).get('selected_topic') or context.get('attention', {}).get('selected_topic'),
            'context_delivery': deepcopy(invocation.get('context_delivery') or (start or {}).get('payload', {}).get('context_delivery') or {}),
            'provider': invocation.get('provider'), 'model': invocation.get('successful_model') or invocation.get('model'),
            'attempts': [{k: deepcopy(a[k]) for k in ('model', 'result', 'elapsed_ms', 'http_status', 'request_payload_bytes', 'usage') if k in a}
                         for a in invocation.get('provider_attempts', [])],
            'response': raw_response if isinstance(raw_response, str) else json.dumps(raw_response, ensure_ascii=False) if raw_response is not None else None,
            'proposal': {'title': _text(proposal.get('title')), 'summary': _text(proposal.get('summary'), 1000),
                         'actions': [{'type': a.get('type'), 'id': a.get('id'), 'project': a.get('project'), 'title': _text(a.get('title'))} for a in actions]},
            'receipt': {'available': bool(terminal), 'seq': (terminal or {}).get('seq'),
                        'hash': (terminal or {}).get('hash'), 'result_hash': (terminal or {}).get('payload', {}).get('result_hash')},
            'events': [{'kind': e['kind'], 'time': e['time'], 'seq': e['seq'], 'hash': e['hash'],
                        'reason': _text(e.get('payload', {}).get('reason'), 500)} for e in matching][-16:],
        })
    return traces
