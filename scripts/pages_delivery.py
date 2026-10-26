#!/usr/bin/env python3
"""Skip redundant interface deployments; public data has its own commit stream."""
import json
import os
import re
import subprocess
import urllib.request


def presentation_path(path):
    return (path.startswith('wake/assets/') or path in {
        'wake/report.py', 'wake/reader_guide.py', 'wake/hosted_presentation.py',
        'wake/installation_cli.py', 'scripts/prepare_pages.py', 'scripts/pages_bundle.py',
        '.github/workflows/publish-pages.yml'})


def needs_delivery(current, revision, comparison=None):
    presentation = current.get('presentation', {})
    if presentation.get('data_transport') != 'github-pinned@1':
        return True
    previous = presentation.get('source_revision', '')
    if not re.fullmatch('[a-f0-9]{40}', previous):
        return True
    if previous == revision:
        return False
    if not comparison or comparison.get('status') != 'ahead':
        return True
    files = comparison.get('files')
    # GitHub limits comparison file lists to 300; truncation must not hide UI changes.
    if not isinstance(files, list) or len(files) >= 300:
        return True
    return any(presentation_path(row.get('filename', '')) or
               presentation_path(row.get('previous_filename', '')) for row in files)


def gh(path):
    return json.loads(subprocess.check_output(['gh', 'api', path], text=True))


def main():
    repository = os.environ['GITHUB_REPOSITORY']
    revision = os.environ['PRESENTATION_REVISION']
    deliver = True
    try:
        page = gh(f'repos/{repository}/pages')
        url = page['html_url'].rstrip('/') + '/installation.json'
        request = urllib.request.Request(url, headers={'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(request, timeout=10) as response:
            raw = response.read(524289)
        if len(raw) > 524288:
            raise ValueError('Published installation metadata exceeds limit')
        current = json.loads(raw)
        previous = current.get('presentation', {}).get('source_revision', '')
        comparison = None
        if re.fullmatch('[a-f0-9]{40}', previous) and previous != revision:
            comparison = gh(f'repos/{repository}/compare/{previous}...{revision}')
        deliver = needs_delivery(current, revision, comparison)
    except (KeyError, ValueError, OSError, subprocess.CalledProcessError):
        # A missing/unreadable site is a reason to repair delivery, not skip it.
        pass
    with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
        if os.environ.get('PAGES_FORCE') == 'true':
            deliver = True
        output.write('needed=' + str(deliver).lower() + '\n')
    print('Website interface deployment needed.' if deliver else
          'Website interface already current; public data updates independently.')


if __name__ == '__main__':
    main()
