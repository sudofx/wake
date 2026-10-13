"""Forward scientific support contract, separate from immutable historical acceptance."""
from .research import source_material_text

POLICY_VERSION = 3


def render_findings(claims):
    return '\n\n'.join(c['statement'] + ' ' + ' '.join('[' + s['evidence'] + ']' for s in c['support']) for c in claims)


def validate_claims(action, state):
    from .governance import require, text, keys, _evidence_payload
    from .research_reviews import background_reason
    claims = action.get('claims')
    require(isinstance(claims, list) and 0 < len(claims) <= 8, 'Notebook needs one to eight traceable claims')
    for claim in claims:
        version = state.get('research_quality_policy', 1)
        keys(claim, 'statement support' + (' certainty result' if version >= 2 else '') + (' review' if version >= 3 else ''), 'Claim')
        if version >= 2:
            require(claim['certainty'] in ('paper-supported', 'hypothesis', 'analogy', 'tested'), 'Unknown claim certainty')
            if claim['certainty'] == 'tested':
                result = state.get('reproductions', {}).get(claim['result'])
                require(result is not None and result.get('status') == 'measured', 'Tested claims require an operator-recorded measured reproduction')
                require(claim['statement'] == result.get('claim'), 'Tested wording must match the measured result scope')
            else:
                require(claim['result'] == '', 'Only tested claims can reference a measured result')
        text(claim['statement'], 'claim statement', 1800)
        if version >= 3:
            review = claim['review']
            keys(review, 'counterevidence alternative would_change_mind', 'Critical review')
            require(isinstance(review['counterevidence'], list) and len(review['counterevidence']) <= 4, 'Counterevidence must be bounded')
            for eid in review['counterevidence']:
                require(eid in action['evidence'], 'Counterevidence must be a collected cited source')
            for field in ('alternative', 'would_change_mind'):
                text(review[field], field, 1800)
                require(len(review[field].strip()) >= 40, 'Critical review needs a substantive alternative and disconfirmation condition')
        support = claim['support']
        require(isinstance(support, list) and 0 < len(support) <= 4, 'Claim needs bounded source support')
        for item in support:
            keys(item, 'evidence passage explanation', 'Claim support')
            require(item['evidence'] in action['evidence'], 'Claim source must be cited by notebook')
            evidence = state['evidence'][item['evidence']]
            require(not background_reason(evidence.get('source', '')), 'Background definitions and funding notices cannot establish scientific claims')
            text(item['passage'], 'support passage', 1800)
            text(item['explanation'], 'support explanation', 1800)
            material = source_material_text(_evidence_payload(evidence))
            normalize = lambda value: ' '.join(value.split())
            require(len(item['passage'].strip()) >= 40 and normalize(item['passage']) in normalize(material),
                    'Supporting passage must be a substantive exact excerpt of the collected source')
    require(action['findings'] == render_findings(claims), 'Findings must match the enumerated supported claims exactly')


def claim_schema(version=POLICY_VERSION, measured_results=()):
    string = {'type': 'string'}
    support = {'type': 'object', 'additionalProperties': False,
               'required': ['evidence', 'passage', 'explanation'],
               'properties': {k: string for k in ('evidence', 'passage', 'explanation')}}
    properties = {'statement': string, 'support': {'type': 'array', 'minItems': 1, 'maxItems': 4, 'items': support}}
    required = ['statement', 'support']
    if version >= 2:
        measured_ids = [item['id'] for item in measured_results if item.get('status') == 'measured']
        properties.update(certainty={'type': 'string', 'enum': ['paper-supported', 'hypothesis', 'analogy'] + (['tested'] if measured_ids else [])},
                          result={'type': 'string', 'enum': [''] + measured_ids,
                                  'description': 'Use the empty string for paper-supported, hypothesis, or analogy. Only tested may name a supplied measured reproduction ID; never put prose here.'})
        required += ['certainty', 'result']
    if version >= 3:
        properties['review'] = {'type': 'object', 'additionalProperties': False,
                               'required': ['counterevidence', 'alternative', 'would_change_mind'],
                               'properties': {'counterevidence': {'type': 'array', 'maxItems': 4, 'items': string},
                                              'alternative': string, 'would_change_mind': string}}
        required.append('review')
    return {'type': 'array', 'minItems': 1, 'maxItems': 8,
            'items': {'type': 'object', 'additionalProperties': False,
                      'required': required,
                      'properties': properties}}


def support_provenance(action, state):
    from .governance import _source_identity
    result = []
    for claim in action.get('claims', []):
        evidence = [state['evidence'][s['evidence']] for s in claim['support']]
        works = sorted({_source_identity(e) for e in evidence})
        result.append({'statement': claim['statement'], 'source_works': works,
                       'distinct_works': len(works), 'peer_imported': any(e.get('peer_origin') for e in evidence),
                       'independent_confirmation': 'not-established',
                       'review': claim.get('review')})
    return result
