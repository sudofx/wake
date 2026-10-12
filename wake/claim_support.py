"""Forward scientific support contract, separate from immutable historical acceptance."""
from .research import source_material_text

POLICY_VERSION = 1


def render_findings(claims):
    return '\n\n'.join(c['statement'] + ' ' + ' '.join('[' + s['evidence'] + ']' for s in c['support']) for c in claims)


def validate_claims(action, state):
    from .governance import require, text, keys, _evidence_payload
    from .research_reviews import background_reason
    claims = action.get('claims')
    require(isinstance(claims, list) and 0 < len(claims) <= 8, 'Notebook needs one to eight traceable claims')
    for claim in claims:
        keys(claim, 'statement support', 'Claim')
        text(claim['statement'], 'claim statement', 1800)
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


def claim_schema(version=POLICY_VERSION):
    string = {'type': 'string'}
    support = {'type': 'object', 'additionalProperties': False,
               'required': ['evidence', 'passage', 'explanation'],
               'properties': {k: string for k in ('evidence', 'passage', 'explanation')}}
    return {'type': 'array', 'minItems': 1, 'maxItems': 8,
            'items': {'type': 'object', 'additionalProperties': False,
                      'required': ['statement', 'support'],
                      'properties': {'statement': string, 'support': {'type': 'array', 'minItems': 1, 'maxItems': 4, 'items': support}}}}
