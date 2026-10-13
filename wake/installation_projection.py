"""Disposable installation-wide views of independent governed node snapshots.

Nothing in this module opens a record or feeds aggregation back into governance.
A fingerprint identifies the supplied snapshots, not an authoritative event head.
"""
from copy import deepcopy
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
        heads[node] = deepcopy(origin)
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
    research['matrix'] = _matrix_projection(None, False)
    research['matrix']['scope'] = 'Select an individual node to inspect its recorded matrix results.'
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
