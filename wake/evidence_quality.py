"""Transparent source concentration/reuse diagnostics, never truth scores."""
from collections import Counter
from urllib.parse import urlsplit
from .governance import _source_identity, _claim_tokens, _evidence_payload


def evidence_quality(state):
    sources = {key: item for key, item in state.get('evidence', {}).items()
               if item.get('actor') == 'collector' and item.get('scope') == 'collected'}
    works = Counter(_source_identity(item) for item in sources.values())
    hosts = Counter(urlsplit(item.get('source', '')).hostname or 'local' for item in sources.values())
    use = Counter()
    notebooks = []
    for notebook in state.get('notebooks', {}).values():
        cited = [sources[key] for key in notebook.get('evidence', []) if key in sources]
        identities = {_source_identity(item) for item in cited}
        use.update(identities)
        claim = _claim_tokens(notebook.get('findings', ''))
        mismatches = [item['id'] for item in cited if len(claim & _claim_tokens(' '.join(
            str(_evidence_payload(item).get(key, '')) for key in ('title', 'abstract', 'excerpt')))) < 2]
        notebooks.append({'id': notebook['id'], 'distinct_works': len(identities),
                          'citation_count': len(cited), 'possible_mismatch_ids': mismatches})
    return {'schema_version': 1, 'collected_observations': len(sources), 'distinct_works': len(works),
            'mirror_or_repeat_observations': len(sources) - len(works), 'distinct_hosts': len(hosts),
            'largest_host_share': round(max(hosts.values(), default=0) / max(1, len(sources)), 4),
            'reused_works': [{'work': work, 'notebook_count': count} for work, count in sorted(use.items()) if count > 1],
            'notebooks': notebooks,
            'boundary': 'Lexical mismatch and concentration diagnostics do not establish entailment, independence, truth, or novelty.'}
