"""Reproduce bounded A/B/C input measurements without a provider call."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import tempfile

from .reader_transport import export_reader_transport


def fixture(site):
    """Synthetic publications and conversation; these are not WAKE research."""
    old = {'id': 'fixture-old', 'title': 'Synthetic baseline',
           'body': 'The fixture measured ten completed tasks. This is a synthetic test, not a scientific finding.',
           'evidence': [], 'notebooks': [], 'created_version': 1, 'status': 'superseded',
           'superseded_by': 'fixture-current'}
    current = {'id': 'fixture-current', 'title': 'Synthetic correction',
               'body': 'The fixture corrected the completed-task count from ten to twelve. The count does not establish a cause or energy savings.',
               'evidence': ['fixture-source'], 'notebooks': [], 'created_version': 2,
               'status': 'published', 'supersedes': old['id']}
    source = {'id': 'fixture-source', 'source': 'https://example.org/synthetic-fixture',
              'content': {'text': 'Synthetic fixture correction: twelve tasks, previously ten; cause unknown.'}}
    export_reader_transport({'head': 'fixture-head', 'state': {
        'version': 2, 'posts': {old['id']: old, current['id']: current},
        'evidence': {source['id']: source}}, 'events': []}, site)
    history = []
    for index in range(8):
        history.append({'id': f'fixture-turn-{index}', 'article_id': current['id'],
                        'question': 'Please explain the count and its uncertainty again.',
                        'answer': ('The count is a synthetic observation. A count does not show its cause. '
                                   'No measured energy comparison is available. ') * 12})
    history.append({'id': 'fixture-turn-latest', 'article_id': current['id'],
                    'question': 'What changed in the completed-task count?',
                    'answer': 'The corrected synthetic count is twelve, previously ten. Its cause remains unknown.',
                    'self_report': 'unsure'})
    return {'article_id': current['id'], 'question': 'What does that correction imply?',
            'history': history, 'previous_article': {'id': old['id'], 'exposure': {'opened': True}}}


def compare(site, request):
    from .reader_context import prepare_context
    rows = []
    for condition in ('A', 'B', 'C'):
        prepared = prepare_context(site, {**request, 'condition': condition})
        exact = (prepared['system'] + prepared['prompt']).encode()
        rows.append({'condition': condition, 'metrics': prepared['metrics'],
                     'exact_input_bytes': len(exact),
                     'exact_input_sha256': hashlib.sha256(exact).hexdigest(),
                     'missing_count': len(prepared['missing']),
                     'warning_count': len(prepared['warnings'])})
    return {'experiment': 'reader-context-inputs-v1', 'conditions': rows,
            'provider_calls': 0, 'output_bytes': None, 'provider_tokens': None,
            'response_latency_ms': None, 'energy_savings': None,
            'quality_assessment': 'Not measured by this input-only experiment; use the documented blinded response review.'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, help='Pinned completed public export')
    parser.add_argument('--request', type=Path, help='Private bounded JSON question/history; never printed')
    args = parser.parse_args(argv)
    if bool(args.site) != bool(args.request):
        parser.error('--site and --request must be supplied together')
    if args.site:
        with args.request.open('rb') as stream:
            raw = stream.read(65537)
        if len(raw) > 65536:
            parser.error('Private experiment request exceeds 64 KiB')
        request = json.loads(raw)
        if not isinstance(request, dict):
            parser.error('Private experiment request must be an object')
        result = compare(args.site.resolve(strict=True), request)
    else:
        with tempfile.TemporaryDirectory(prefix='wake-reader-experiment-') as directory:
            site = Path(directory)
            result = compare(site, fixture(site))
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
