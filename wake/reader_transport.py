"""Bounded reader bootstrap and disposable, same-generation detail pages.

The complete exported snapshot remains an archive. Reading a homepage must never
transfer the accumulated evidence and provider history merely to show one story.
"""
from copy import deepcopy
import json
from pathlib import Path

MAX_BOOTSTRAP_BYTES = 256 * 1024
PAGE_SIZE = 24
COLLECTIONS = ('posts', 'projects', 'notebooks', 'evidence', 'invocations',
               'beliefs', 'commitments', 'acquisition', 'research_reviews')


def record_path(collection, identifier):
    # Hex path segments are injective, portable, and cannot escape the export.
    encoded = str(identifier).encode().hex()
    return 'reader-records/' + collection + '/' + '/'.join(
        encoded[i:i + 64] for i in range(0, len(encoded), 64)) + '.json'


def _json(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def export_reader_transport(data, target):
    """Write views only; callers pass an already public-filtered browser packet."""
    from .reader_context import article_descriptor
    target = Path(target)
    state = data['state']
    counts = {key: len(state.get(key, {})) for key in COLLECTIONS}
    counts.update(journal=len(state.get('journal', [])), events=len(data.get('events', [])))

    def ordered(collection):
        rows = list(state.get(collection, {}).values())
        def stamp(item):
            invocation = state.get('invocations', {}).get(item.get('updated_by') or item.get('created_by'), {})
            return (str(item.get('published_at') or item.get('finished') or item.get('time')
                        or invocation.get('finished') or invocation.get('time') or ''),
                    item.get('updated_version', item.get('created_version', 0)), str(item.get('id', '')))
        return sorted(rows, key=stamp)

    def write(relative, value):
        path = target / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(_json(value), encoding='utf-8')

    def related(item):
        result = {}
        for name, ids in (
                ('evidence', item.get('evidence', [])),
                ('notebooks', item.get('notebooks', [])),
                ('projects', [item.get('project')]),
                ('invocations', [item.get(k) for k in ('created_by', 'updated_by', 'resolved_by')])):
            result[name] = {identifier: state.get(name, {})[identifier] for identifier in ids
                            if isinstance(identifier, str) and identifier in state.get(name, {})}
        return result

    for collection in COLLECTIONS:
        rows = ordered(collection)
        for item in rows:
            if not item.get('id'):
                continue
            write(record_path(collection, item['id']), {'head': data['head'],
                'collection': collection, 'item': item, 'related': related(item),
                **({'article': article_descriptor(item, data['head'])} if collection == 'posts' else {}),
                'events': [event for event in data.get('events', [])
                           if event.get('payload', {}).get('id') == item['id']]})
    for row in state.get('journal', []):
        identifier = row.get('invocation')
        write(record_path('journal', 'cycle:' + str(row['cycle'])), {
            'head': data['head'], 'collection': 'journal', 'item': row,
            'related': {'invocations': {identifier: state['invocations'][identifier]}
                        if identifier in state.get('invocations', {}) else {}},
            'events': [event for event in data.get('events', [])
                       if event.get('payload', {}).get('id') == identifier]})
    for collection, rows in (
            *((key, ordered(key)) for key in COLLECTIONS),
            ('journal', state.get('journal', [])), ('events', data.get('events', []))):
        rows = list(reversed(rows))
        for offset in range(0, len(rows), PAGE_SIZE):
            batch = rows[offset:offset + PAGE_SIZE]
            links = {}
            if collection == 'journal':
                links['invocations'] = {row['invocation']: state['invocations'][row['invocation']]
                                        for row in batch if row['invocation'] in state.get('invocations', {})}
            write(f'reader-records/pages/{collection}/{offset // PAGE_SIZE}.json',
                  {'head': data['head'], 'collection': collection,
                   'rows': batch, 'related': links,
                   'next': offset // PAGE_SIZE + 1 if offset + PAGE_SIZE < len(rows) else None})

    # Bootstrap cost is fixed by a byte budget, including unusually long prose.
    # Exact bodies live in the detail shards; prose is never silently truncated.
    def bootstrap(limit):
        view = {key: deepcopy(value) for key, value in data.items()
                if key not in ('state', 'events', 'application_observability', 'research')}
        small = {key: deepcopy(state[key]) for key in
                 ('version', 'charter', 'pet_name', 'objective', 'topic_colors', 'focus', 'pending')
                 if key in state}
        small['research_topics'] = deepcopy(state.get('research_topics', [])[:32])
        for collection in COLLECTIONS:
            all_rows = ordered(collection)
            rows = all_rows[-limit:] if limit else []
            if collection == 'commitments':
                required = [row for row in all_rows if row.get('status') == 'open']
                rows = list({row['id']: row for row in [*rows, *required]}.values())
            small[collection] = {}
            for item in rows:
                if not item.get('id'):
                    continue
                if collection == 'invocations':
                    item = {key: value for key, value in item.items() if key in
                            ('id', 'time', 'finished', 'status', 'reason', 'provider', 'model', 'phase', 'origin')}
                elif collection == 'evidence':
                    item = {key: value for key, value in item.items() if key in
                            ('id', 'time', 'source', 'actor', 'origin')}
                small[collection][item['id']] = deepcopy(item)
                if collection == 'posts':
                    small[collection][item['id']]['_reader_article'] = article_descriptor(item, data['head'])
        small['journal'] = deepcopy(state.get('journal', [])[-limit:])
        for row in small['journal']:
            identifier = row.get('invocation')
            item = state.get('invocations', {}).get(identifier)
            if item:
                small['invocations'][identifier] = {key: value for key, value in item.items() if key in
                    ('id', 'time', 'finished', 'status', 'provider', 'model', 'origin')}
        small['attention'] = {'counters': {}, 'deferred': {}}
        small['representations'] = {}
        view.update(state=small, events=[], reader_transport={'schema': 1,
            'counts': counts, 'page_size': PAGE_SIZE, 'scope': 'Recent overview; open a record or load older entries for details.'})
        return view

    for limit in (16, 12, 8, 4, 2, 1, 0):
        view = bootstrap(limit)
        encoded = _json(view)
        if len(encoded.encode()) <= MAX_BOOTSTRAP_BYTES:
            write('reader-data.json', view)
            return view
    raise ValueError('Reader metadata exceeds the bounded bootstrap')
