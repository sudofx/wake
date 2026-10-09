"""Transparent source concentration/reuse diagnostics, never truth scores."""
from collections import Counter
from urllib.parse import urlsplit
from .governance import _source_identity, _claim_tokens, _evidence_payload
from .research import (source_material_text, source_observation_readable,
                       effective_evidence_role, effective_host_tier)


def evidence_quality(state):
    sources = {key: item for key, item in state.get('evidence', {}).items()
               if item.get('actor') == 'collector' and item.get('scope') == 'collected'}
    works = Counter(_source_identity(item) for item in sources.values())
    hosts = Counter(urlsplit(item.get('source', '')).hostname or 'local' for item in sources.values())
    roles = Counter(effective_evidence_role(item.get('source', ''), _evidence_payload(item))
                    for item in sources.values())
    readable = {key: item for key, item in sources.items()
                if effective_evidence_role(item.get('source', ''), _evidence_payload(item)) == 'source'
                and effective_host_tier(item.get('source', ''), _evidence_payload(item)) != 'verification-metadata'
                and source_observation_readable(_evidence_payload(item))}
    readable_works = {_source_identity(item) for item in readable.values()}
    use = Counter()
    notebooks = []
    for notebook in state.get('notebooks', {}).values():
        cited = [sources[key] for key in notebook.get('evidence', []) if key in sources]
        identities = {_source_identity(item) for item in cited}
        use.update(identities)
        claim = _claim_tokens(notebook.get('findings', ''))
        mismatches = [item['id'] for item in cited if len(claim & _claim_tokens(' '.join((
            str(_evidence_payload(item).get('title', '')), str(_evidence_payload(item).get('abstract', '')),
            source_material_text(_evidence_payload(item)))))) < 2]
        notebooks.append({'id': notebook['id'], 'distinct_works': len(identities),
                          'citation_count': len(cited), 'possible_mismatch_ids': mismatches,
                          'unreadable_source_ids': [item['id'] for item in cited
                              if not source_observation_readable(_evidence_payload(item))]})
    return {'schema_version': 1, 'collected_observations': len(sources), 'distinct_works': len(works),
            'observations_by_role': dict(sorted(roles.items())),
            'readable_source_observations': len(readable),
            'readable_distinct_works': len(readable_works),
            'cited_readable_distinct_works': len(readable_works & set(use)),
            'uncited_readable_distinct_works': len(readable_works - set(use)),
            'mirror_or_repeat_observations': len(sources) - len(works), 'distinct_hosts': len(hosts),
            'largest_host_share': round(max(hosts.values(), default=0) / max(1, len(sources)), 4),
            'reused_works': [{'work': work, 'notebook_count': count} for work, count in sorted(use.items()) if count > 1],
            'cited_distinct_works': len(use),
            'uncited_readable_source_ids': [key for key, item in sorted(readable.items())
                if _source_identity(item) not in use][-20:],
            'notebooks': notebooks,
            'boundary': 'Lexical mismatch and concentration diagnostics do not establish entailment, independence, truth, or novelty.'}
