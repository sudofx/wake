"""Disposable installation-wide views of independent governed node snapshots.

Nothing in this module opens a record or feeds aggregation back into governance.
A fingerprint identifies the supplied snapshots, not an authoritative event head.
"""
from copy import deepcopy
from datetime import datetime, timezone
from math import isfinite
from hashlib import sha256
import json

from .domain_events import empty
from .history import merge_history_metrics
from .research_projection import build_research_projection, _matrix_projection

_COLLECTIONS = ('projects', 'notebooks', 'beliefs', 'evidence', 'commitments',
                'invocations', 'research', 'posts', 'acquisition', 'representations',
                'research_reviews', 'reproductions')
_REFS = {'id', 'project', 'invocation', 'invocation_id', 'created_by', 'updated_by',
         'resolved_by', 'supersedes', 'superseded_by', 'domain', 'topic', 'selected_topic',
         'attention_topic', 'pending', 'evidence_id', 'notebook', 'belief', 'commitment'}
_REF_LISTS = {'evidence', 'notebooks', 'projects', 'beliefs', 'commitments', 'deferred_topics'}
_OPAQUE = {'content', 'raw_response', 'response', 'request', 'group_publication',
           'peer_origin', 'origin', 'original_event', 'context_delivery'}


def _prefix(node, value):
    return f'{node}::{value}' if value else value


def _remap(value, node, known, field=None):
    """Rewrite explicit local links only; prose and immutable receipt bytes stay exact."""
    if field in _OPAQUE:
        return deepcopy(value)
    if isinstance(value, dict):
        return {key: _remap(item, node, known, key) for key, item in value.items()}
    if isinstance(value, list):
        return [_remap(item, node, known, field) for item in value]
    if isinstance(value, str) and (field in _REFS or field in _REF_LISTS) and value in known:
        return _prefix(node, value)
    return deepcopy(value)



def _canonical_topic_refs(value, aliases, field=None):
    """Collapse display topic links without rewriting source receipts or prompts."""
    if field in _OPAQUE:
        return deepcopy(value)
    if isinstance(value, dict):
        return {key: _canonical_topic_refs(item, aliases, key) for key, item in value.items()}
    if isinstance(value, list):
        return [_canonical_topic_refs(item, aliases, field) for item in value]
    if isinstance(value, str) and field in {
            'domain', 'topic', 'selected_topic', 'attention_topic', 'deferred_topics'}:
        return aliases.get(value, value)
    return deepcopy(value)



def _unified_matrix(node_snapshots, node_research):
    """Select recorded coordinate results; never average node scores into a trial."""
    matrix = _matrix_projection(None, False)
    canonical = {cell['id']: cell for cell in matrix['cells']}
    reported_nodes, enabled_nodes = [], []
    contributions = {}
    for node, packet in node_snapshots.items():
        view = node_research.get(node, {}).get('matrix', {})
        if not view.get('reported'):
            continue
        if (view.get('id') != matrix['id'] or
                view.get('definition_digest') != matrix['definition_digest'] or
                view.get('axes') != matrix['axes']):
            raise ValueError(f'Continuity matrix grammar does not match node {node}')
        reported_nodes.append(node)
        if view.get('enabled'):
            enabled_nodes.append(node)
        state = packet['state']
        for cell in view.get('cells', []):
            if cell.get('id') not in canonical or cell.get('position') != canonical[cell['id']]['position']:
                raise ValueError(f'Continuity matrix coordinate does not match node {node}')
            if cell.get('status') == 'not_recorded':
                continue
            if cell.get('status') not in ('completed', 'failed', 'deferred'):
                raise ValueError(f'Continuity matrix result status does not match node {node}')
            score = cell.get('score')
            if score is not None and (isinstance(score, bool) or not isinstance(score, (int, float))
                                      or not isfinite(score) or not 0 <= score <= 1):
                raise ValueError(f'Continuity matrix score does not match node {node}')
            invocation_id = cell.get('invocation_id')
            invocation = state.get('invocations', {}).get(invocation_id, {})
            recorded_at = invocation.get('finished') or invocation.get('time')
            try:
                stamp = datetime.fromisoformat(recorded_at)
                stamp = stamp.replace(tzinfo=timezone.utc) if stamp.tzinfo is None else stamp
                order = stamp.timestamp()
            except (ValueError, TypeError):
                order = float('-inf')
            result = {**deepcopy(cell), 'invocation_id': _prefix(node, invocation_id),
                      'recorded_at': recorded_at,
                      'origin': {'node': node, 'head': packet.get('head'),
                                 'version': state.get('version', 0), 'invocation_id': invocation_id}}
            contributions.setdefault(cell['id'], []).append((order, node, result))
    for identifier, entries in contributions.items():
        entries.sort(key=lambda entry: (entry[0], entry[1]), reverse=True)
        cell = canonical[identifier]
        cell.update(deepcopy(entries[0][2]))
        cell['contributions'] = [deepcopy(entry[2]) for entry in entries]
        cell['contribution_count'] = len(entries)
        cell['selection_time_available'] = entries[0][0] != float('-inf')
    completed = [cell for cell in matrix['cells'] if cell['status'] == 'completed']
    graded = [cell for cell in completed if not cell.get('response_error')]
    valid_scores = [cell['score'] for cell in graded if isinstance(cell.get('score'), (int, float))]
    raw_scores = [cell['score'] for cell in completed if isinstance(cell.get('score'), (int, float))]
    passed_known = [cell for cell in graded if isinstance(cell.get('passed'), bool)]
    failed_checks = {}
    lens_coverage = {value['key']: 0 for value in matrix['axes'][0]['values']}
    for cell in completed:
        lens_coverage[matrix['axes'][0]['values'][cell['position'][0]]['key']] += 1
        if not cell.get('response_error'):
            for check in cell.get('failed_checks', []):
                failed_checks[check] = failed_checks.get(check, 0) + 1
    all_results = [entry[2] for entries in contributions.values() for entry in entries]
    matrix.update(
        reported=bool(reported_nodes), enabled=bool(enabled_nodes) if reported_nodes else None,
        completed=len(completed) if reported_nodes else None,
        passed=sum(cell['passed'] for cell in passed_known) if len(passed_known) == len(graded) and reported_nodes else None,
        passed_known_cells=len(passed_known), graded_count=len(graded),
        graded_failed_count=sum(bool(cell.get('failed_checks')) or cell.get('passed') is False for cell in graded),
        invalid_response_count=len(completed) - len(graded), failure_counts=failed_checks,
        lens_coverage=lens_coverage, next_coordinate=None,
        mean_score=round(sum(valid_scores) / len(valid_scores), 4) if valid_scores else None,
        historical_mean_score=round(sum(raw_scores) / len(raw_scores), 4) if raw_scores else None,
        score_count=len(valid_scores),
        aggregation='latest-recorded-node-result-per-coordinate',
        scope='Each cell displays the latest recorded node result by invocation time; ties use node ID. All current node contributions remain attributed. Counts describe distinct displayed cells, not independent confirmations.',
        mean_scope='Mean of valid displayed coordinate scores; node scores are never averaged to create a cell result.',
        reported_nodes=reported_nodes, enabled_nodes=enabled_nodes,
        contribution_counts={
            'recorded': len(all_results), 'completed': sum(r['status'] == 'completed' for r in all_results),
            'failed': sum(r['status'] == 'failed' for r in all_results),
            'deferred': sum(r['status'] == 'deferred' for r in all_results),
            'nodes': len({r['origin']['node'] for r in all_results}),
            'coordinates': len(contributions)},
        history_scope='Current exported result from each node for each coordinate; earlier overwritten trials are not reconstructed.')
    return matrix


def build_unified_projection(node_snapshots, node_research, installation_id):
    """Combine public exports without synthesizing accepted research or shared authority.

    IDs in the disposable view are node-qualified. Original IDs and source heads
    accompany each record. Shared Bob publications appear once, retaining their
    original provider and group provenance; node initialization posts stay local.
    """
    available = {str(node): packet for node, packet in sorted(node_snapshots.items())
                 if isinstance(packet, dict) and isinstance(packet.get('state'), dict)}
    leader = next(iter(available), None)
    state = deepcopy(available[leader]['state']) if leader else empty()
    for collection in _COLLECTIONS:
        state[collection] = {}
    state['journal'] = []
    state['research_topics'] = []
    state['pending'] = None
    state['version'] = 0
    state['attention'] = {'counters': {}, 'deferred': {}}
    heads, events, metrics, origins, publications = {}, [], {}, {}, {}
    pending_nodes = []
    post_aliases = {}
    topic_aliases, topic_groups = {}, {}
    for node, packet in available.items():
        local = packet['state']
        origin = {'node': node, 'head': packet.get('head'), 'version': local.get('version', 0)}
        origins[node] = origin
        heads[node] = {**deepcopy(origin), 'snapshot_digest': sha256(json.dumps(
            {'record': packet, 'research': node_research.get(node)}, sort_keys=True,
            separators=(',', ':')).encode()).hexdigest()}
        heads[node]['generated'] = packet.get('generated')
        known = {str(key) for collection in _COLLECTIONS for key in local.get(collection, {})}
        known.update(str(topic['id']) for topic in local.get('research_topics', []) if topic.get('id'))
        for collection in _COLLECTIONS:
            for identifier, item in local.get(collection, {}).items():
                if collection == 'posts':
                    publication = item.get('group_publication')
                    if not isinstance(publication, dict):
                        continue
                    # Exact body/provenance equality is necessary for deduplication.
                    key = json.dumps({'publication': publication,
                                      'title': item.get('title'), 'body': item.get('body'),
                                      'summary': item.get('summary'), 'lede': item.get('lede'),
                                      'lens': item.get('lens')}, sort_keys=True)
                    if key in publications:
                        post_aliases[_prefix(node, identifier)] = publications[key]
                        state['posts'][publications[key]]['origins'].append(deepcopy(origin))
                        continue
                    publications[key] = _prefix(node, identifier)
                    post_aliases[_prefix(node, identifier)] = publications[key]
                mapped = _remap(item, node, known)
                mapped['id'] = _prefix(node, identifier)
                mapped['origin'] = {**deepcopy(origin), 'id': identifier}
                if collection == 'posts':
                    mapped['origins'] = [deepcopy(origin)]
                state[collection][_prefix(node, identifier)] = mapped
        for item in local.get('journal', []):
            state['journal'].append({**_remap(item, node, known), 'origin': deepcopy(origin)})
        for topic in local.get('research_topics', []):
            semantic = json.dumps({key: topic.get(key) for key in (
                'id', 'label', 'seed_question', 'kind', 'repository', 'enabled')}, sort_keys=True)
            qualified = _prefix(node, topic['id'])
            topic_origin = {**deepcopy(origin), 'id': topic['id']}
            if semantic in topic_groups:
                unified_topic = topic_groups[semantic]
                unified_topic['origins'].append(topic_origin)
            else:
                unified_topic = {**_remap(topic, node, known),
                                 'origin': deepcopy(topic_origin), 'origins': [topic_origin]}
                topic_groups[semantic] = unified_topic
                state['research_topics'].append(unified_topic)
            topic_aliases[qualified] = unified_topic['id']
        if local.get('pending'):
            pending_nodes.append({'node': node, 'invocation': _prefix(node, local['pending'])})
        state['version'] += int(local.get('version', 0))
        for event in packet.get('events', []):
            # The history viewer can inspect the exact source receipt. These are
            # not a replayable installation chain and must never be reduced.
            events.append({**deepcopy(event),
                           'payload': _remap(event.get('payload', {}), node, known),
                           'origin': deepcopy(origin), 'original_event': deepcopy(event),
                           'projection_only': True,
                           'projection_id': _prefix(node, event.get('hash') or event.get('seq'))})
        node_metrics = deepcopy(packet.get('metrics', {}))
        by_topic = node_metrics.get('accepted_actions', {}).get('by_topic')
        if isinstance(by_topic, dict):
            node_metrics['accepted_actions']['by_topic'] = {
                _prefix(node, key): value for key, value in by_topic.items()}
        metrics = merge_history_metrics(metrics, node_metrics)
        metrics.setdefault('storage', {})
        for key, amount in packet.get('metrics', {}).get('storage', {}).items():
            if isinstance(amount, (int, float)):
                metrics['storage'][key] = metrics['storage'].get(key, 0) + amount
    for post in state['posts'].values():
        for field in ('supersedes', 'superseded_by'):
            if post.get(field) in post_aliases:
                post[field] = post_aliases[post[field]]
            elif post.get(field) and post[field] not in state['posts']:
                # Node-only introductory articles are absent from this view.
                post.pop(field)
    state = _canonical_topic_refs(state, topic_aliases)
    events = _canonical_topic_refs(events, topic_aliases)
    topic_metrics = {}
    for key, counts in metrics.get('accepted_actions', {}).get('by_topic', {}).items():
        target = topic_metrics.setdefault(topic_aliases.get(key, key), {'total': 0, 'by_type': {}})
        target['total'] += counts.get('total', 0)
        for kind, count in counts.get('by_type', {}).items():
            target['by_type'][kind] = target['by_type'].get(kind, 0) + count
    metrics.setdefault('accepted_actions', {})['by_topic'] = topic_metrics
    state['pending'] = pending_nodes[0]['invocation'] if pending_nodes else None
    state['pending_nodes'] = pending_nodes
    state['journal'].sort(key=lambda row: (str(row.get('time', '')), str(row['origin']['node']), row.get('cycle', 0)))
    events.sort(key=lambda event: (str(event.get('time', '')), event['origin']['node'], event.get('seq', 0)))
    head = 'snapshot:' + sha256(json.dumps(heads, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    generated = max((str(p.get('generated') or '') for p in available.values()), default='') or None
    source = {'installation': 'unified', 'installation_id': installation_id,
              'authority': 'Derived view of governed node records; not an authoritative record',
              'node_heads': heads, 'head': head, 'head_kind': 'snapshot-fingerprint',
              'version_meaning': 'Sum of accepted node cycles; not one record version',
              'available_nodes': list(available),
              'unavailable_nodes': sorted(set(map(str, node_snapshots)) - set(available))}
    research = build_research_projection(state, [], head, generated=generated,
                                        metrics=metrics, source=source)
    # Preserve source projections' recorded traces and graph identities. A node
    # cycle coordinate must not become a fictitious shared experiment result.
    for collection in ('activity', 'wakes'):
        research[collection] = []
    research['graph']['nodes'] = []
    research['graph']['edges'] = []
    for node, packet in available.items():
        local = packet['state']
        known = {str(key) for collection in _COLLECTIONS for key in local.get(collection, {})}
        known.update(str(t['id']) for t in local.get('research_topics', []) if t.get('id'))
        view = node_research.get(node) or build_research_projection(local, [], packet.get('head'), generated=packet.get('generated'))
        if view.get('head') != packet.get('head') or view.get('version') != local.get('version', 0):
            raise ValueError(f'Research projection does not match node {node}')
        for collection in ('activity', 'wakes'):
            research[collection].extend({**_remap(item, node, known), 'origin': deepcopy(origins[node])}
                                        for item in view.get(collection, []))
        graph = view.get('graph', {})
        graph_ids = {item['id'] for item in graph.get('nodes', [])}
        for item in graph.get('nodes', []):
            mapped = _remap(item, node, known)
            mapped['id'] = _prefix(node, item['id'])
            mapped['origin'] = deepcopy(origins[node])
            research['graph']['nodes'].append(mapped)
        for edge in graph.get('edges', []):
            if edge.get('source') in graph_ids and edge.get('target') in graph_ids:
                research['graph']['edges'].append({**deepcopy(edge),
                    'source': _prefix(node, edge['source']), 'target': _prefix(node, edge['target']),
                    'origin': deepcopy(origins[node])})
    for collection in ('activity', 'wakes'):
        research[collection].sort(key=lambda item: str(item.get('finished') or item.get('time') or ''), reverse=True)
    for collection, rows in research['records'].items():
        for item in rows:
            item['origin'] = deepcopy(state[collection].get(item['id'], {}).get('origin', {}))
    for item in research['evidence']['recent']:
        item['origin'] = deepcopy(state['evidence'].get(item['id'], {}).get('origin', {}))
    research['matrix'] = _unified_matrix(available, node_research)
    research['status']['accepted_cycles_meaning'] = source['version_meaning']
    research['status']['pending_nodes'] = deepcopy(pending_nodes)
    research['status']['attention_topic'] = None
    regimes = [packet['state'].get('experimental', {}).get('controls', {}).get('time_dilation', {})
               for packet in available.values()]
    research['status']['regime'] = deepcopy(regimes[0]) if regimes and all(r == regimes[0] for r in regimes) else {}
    research['status']['regime_scope'] = 'shared node setting' if regimes and all(r == regimes[0] for r in regimes) else 'mixed or unavailable; select a node'
    research['recorded_activity']['source'] = 'published-node-records'
    research['graph'].update(total_nodes=len(research['graph']['nodes']),
                             overview_total=len(research['graph']['nodes']),
                             scope='Union of attributed node research views; no inferred cross-node evidence links.')
    research = _canonical_topic_refs(research, topic_aliases)
    topic_origins = {topic['id']: topic['origins'] for topic in state['research_topics']}
    for topic in research['topics']:
        topic['origins'] = deepcopy(topic_origins[topic['id']])
    research['progress']['interpretation'] += ' Aggregated records may repeat the same work; counts do not establish independent confirmation.'
    return {'projection_schema': 1, 'projection_kind': 'disposable-live-view', 'authoritative': False,
            'source': source, 'state': state, 'events': events, 'head': head,
            'generated': research['generated'], 'metrics': metrics, 'research': research,
            'timezone': 'America/Los_Angeles', 'experiment': None, 'operation': None,
            'wake_status': {'status': 'unified-view', 'pending_nodes': pending_nodes}}
