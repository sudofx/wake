"""Bind a read-only Actions light to an already generated hosted public site."""
import json
from pathlib import Path
import re
import shutil


def bind_hosted_status(site, repository, revision):
    """Change presentation only; keep research, capture provenance and hashed packets.

    This also supports refreshing a published snapshot without opening native
    authority or waiting for another research batch. Callers must publish against
    the exact public parent they captured, so newer exports cannot be rolled back.
    """
    site = Path(site).resolve()
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository):
        raise ValueError('Expected a GitHub repository')
    if not re.fullmatch(r'[0-9a-f]{40}', revision):
        raise ValueError('Expected a complete presentation source revision')
    manifest = json.loads((site / 'installation.json').read_text())
    if (manifest.get('live') is not False or not manifest.get('hosted_execution')
            or not manifest.get('installation_id') or len(manifest.get('record_heads', {})) != 12):
        raise ValueError('Hosted status requires an identified twelve-node hosted snapshot')
    config = {'repository': repository, 'workflow': 'hosted-research.yml', 'branch': 'master'}
    from .hosted_activity import ACTIVITY_ORIGIN
    activity = {'url': ACTIVITY_ORIGIN + '/activity.json', 'installation_id': manifest['installation_id']}
    assets = Path(__file__).parent / 'assets'
    shell = (assets / 'index.html').read_text()
    light = re.search(r'<a\b[^>]*class="actions-light"[^>]*>.*?</a>', shell, re.S).group(0)
    roots = set()
    for path in site.rglob('*.html'):
        if 'inspect' in path.relative_to(site).parts:
            continue  # Reviewed packet bytes and hashes are immutable.
        page = path.read_text()
        if 'class="header-tools"' not in page:
            continue
        # Reader exports can inline navigation. The shared stylesheet still
        # identifies their own asset root without replacing their page identity.
        stylesheet = re.search(r'<link[^>]*href="((?:\.\./)*)masthead\.css[^\"]*"[^>]*>', page)
        if not stylesheet:
            raise ValueError('Hosted page is missing its generated masthead binding')
        prefix = stylesheet.group(1)
        root = (path.parent / prefix).resolve()
        if not root.is_relative_to(site):
            raise ValueError('Navigation assets must remain inside the public artifact')
        roots.add(root)
        def binding(match):
            deployment = json.loads(match.group(1))
            deployment['hosted_status'] = config
            deployment['hosted_activity'] = activity
            return ('window.WAKE_DEPLOYMENT=' + json.dumps(deployment)
                    + ";document.documentElement.dataset.wakeHostedStatus='true';")
        page = page.replace("document.documentElement.dataset.wakeHostedStatus='true';", '')
        page, count = re.subn(r'window\.WAKE_DEPLOYMENT=(\{[^<]*?\});', binding, page)
        if count != 1:
            raise ValueError('Hosted page must have one generated deployment binding')
        page = re.sub(r'<a\b[^>]*class="[^"]*actions-light[^"]*"[^>]*>.*?</a>', '', page, flags=re.S)
        page = page.replace('class="header-tools">', 'class="header-tools">' + light, 1)
        page = re.sub(r'((?:nav\.js|masthead\.css)\?v=)[^"<]+', r'\g<1>20261020-hosted-status', page)
        page = re.sub(r'<script src="[^\"]*hosted-status\.js[^\"]*"[^>]*></script>', '', page)
        page = page.replace('</head>', f'<script src="{prefix}hosted-status.js?v=20261020-hosted-recovery" defer></script></head>', 1)
        page = re.sub(r'((?:runtime-activity\.js|installation-console\.js|process-field\.js|research\.js)\?v=)[^"<]+', r'\g<1>20261020-hosted-activity', page)
        path.write_text(page)
    if not roots:
        raise ValueError('No generated hosted pages found')
    for root in roots:
        for name in ('nav.js', 'masthead.css', 'hosted-status.js', 'runtime-activity.js', 'installation-console.js', 'process-field.js', 'research.js'):
            shutil.copyfile(assets / name, root / name)
        deployment_path = root / 'deployment.json'
        if deployment_path.exists():
            deployment = json.loads(deployment_path.read_text())
            deployment['hosted_status'] = config
            deployment['hosted_activity'] = activity
            deployment_path.write_text(json.dumps(deployment))
    manifest['presentation'] = {'source_revision': revision, 'hosted_status': config, 'hosted_activity': activity}
    encoded = json.dumps(manifest, sort_keys=True)
    for path in [site / 'installation.json', *site.glob('nodes/*/installation.json')]:
        path.write_text(encoded)
    return manifest
