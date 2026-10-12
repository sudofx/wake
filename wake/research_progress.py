"""Derived research outputs, never a truth score or accepted-cycle authority."""
import hashlib
import json
from .governance import _source_identity, _evidence_payload
from .research import effective_evidence_role, source_material_text, source_observation_readable


def research_progress(state):
    works = set()
    passages = set()
    reviewed = 0
    certainty = {}
    for evidence in state.get('evidence', {}).values():
        payload = _evidence_payload(evidence)
        if (evidence.get('actor') == 'collector' and evidence.get('scope') == 'collected'
                and effective_evidence_role(evidence.get('source', ''), payload) == 'source'
                and source_observation_readable(payload)):
            works.add(_source_identity(evidence))
    for notebook in state.get('notebooks', {}).values():
        for claim in notebook.get('claims', []):
            certainty[claim.get('certainty', 'unclassified')] = certainty.get(claim.get('certainty', 'unclassified'), 0)+1
            reviewed += bool(claim.get('review'))
            for support in claim.get('support', []):
                evidence = state.get('evidence', {}).get(support.get('evidence'))
                if not evidence:
                    continue
                passage = ' '.join(support.get('passage', '').split()).casefold()
                if passage and passage in ' '.join(source_material_text(_evidence_payload(evidence)).split()).casefold():
                    # Rewording a finding or importing a mirror cannot add a support unit.
                    passages.add((_source_identity(evidence), passage))
    return {'basis': 'research-output@1', 'distinct_source_works': len(works),
            'distinct_supporting_passages': len(passages), 'claims_with_critical_review': reviewed,
            'claim_labels': certainty, 'operator_source_corrections': len(state.get('research_reviews', {})),
            'measured_reproductions': len(state.get('reproductions', {})),
            'historical_unclassified_notebooks': sum(not n.get('claims') for n in state.get('notebooks', {}).values()),
            'activity': {'accepted_cycles': state['version'], 'notebooks': len(state.get('notebooks', {})),
                         'notebook_revisions': sum(n.get('revision', 0) for n in state.get('notebooks', {}).values())},
            'interpretation': 'Evidence, traceability, critical review and measured outputs are shown separately. '
            'Cycles and revisions measure activity. Passage matching is not semantic proof; '
            'understanding, novelty and independent confirmation are not automatically scored.'}
