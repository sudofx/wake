"""Operator corrections to scientific interpretation; never rewrite research history."""
from .governance import require, text

FUNDING_CORRECTION = '10.1371/annotation/b5283cc5-5a93-4c96-abc4-c5112266fabe'


def background_reason(url, payload=None):
    from urllib.parse import urlsplit
    host = (urlsplit(url).hostname or '').lower()
    if host == 'dictionary.cambridge.org':
        return 'A dictionary defines words; it does not establish a scientific mechanism or measured result.'
    if FUNDING_CORRECTION in url.lower():
        return 'This notice corrects funding information; it contains no new scientific methods or results.'
    return None


def weak_notebook_reviews(state):
    """Only deterministic known defects; absence of a flag is not scientific approval."""
    reviews = []
    for notebook in state.get('notebooks', {}).values():
        issues = []
        for eid in notebook.get('evidence', []):
            evidence = state['evidence'][eid]
            reason = background_reason(evidence.get('source', ''))
            if reason:
                issues.append({'evidence': eid, 'reason': reason})
        if issues:
            reviews.append({'actor': 'operator', 'notebook': notebook['id'],
                            'revision': notebook['revision'], 'issues': issues,
                            'assessment': 'needs-source-review',
                            'correction': 'The cited background material does not support the scientific conclusions. '
                            'Treat the mechanism, bound or heredity interpretation as an unverified hypothesis until '
                            'a claim-by-claim review identifies substantive supporting passages. Other cited papers '
                            'have not been invalidated by this correction. Original findings are preserved below.'})
    return reviews


def apply_review(state, payload, event):
    require(payload.get('actor') == 'operator', 'Scientific corrections are operator-owned')
    notebook = state.get('notebooks', {}).get(payload.get('notebook'))
    require(notebook is not None, 'Correction needs an existing notebook')
    require(payload.get('revision') == notebook['revision'], 'Correction must name the current revision')
    require(payload.get('assessment') == 'needs-source-review', 'Unknown scientific assessment')
    text(payload.get('correction'), 'correction', 2400)
    require(isinstance(payload.get('issues'), list) and 0 < len(payload['issues']) <= 12, 'Correction needs bounded source issues')
    for issue in payload['issues']:
        require(issue.get('evidence') in notebook['evidence'], 'Correction source must be cited by this notebook')
        text(issue.get('reason'), 'source issue', 1000)
    reviews = state.setdefault('research_reviews', {})
    key = f"{notebook['id']}@{notebook['revision']}"
    require(key not in reviews, 'This notebook revision already has a correction')
    reviews[key] = {**payload, 'time': event['time'], 'event_seq': event['seq']}


def notebook_review(state, notebook):
    return state.get('research_reviews', {}).get(f"{notebook['id']}@{notebook.get('revision', 0)}")
