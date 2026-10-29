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
    from .reader_presentation import remove_retired_reader
    manifest = json.loads((site / 'installation.json').read_text())
    if (manifest.get('live') is not False or not manifest.get('hosted_execution')
            or not manifest.get('installation_id') or len(manifest.get('record_heads', {})) != 12):
        raise ValueError('Hosted status requires an identified twelve-node hosted snapshot')
    remove_retired_reader(site)
    config = {'repository': repository, 'workflow': 'research-worker.yml', 'branch': 'master'}
    assets = Path(__file__).parent / 'assets'
    shell = (assets / 'index.html').read_text()
    light = re.search(r'<a\b[^>]*class="actions-light"[^>]*>.*?</a>', shell, re.S).group(0)
    roots = set()
    bindings = {}
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
        if 'scientific-research.html' not in page:
            page = page.replace('>Research</a>', '>Research</a><a href="'+prefix+'scientific-research.html">Experiments</a>')
        root = (path.parent / prefix).resolve()
        if not root.is_relative_to(site):
            raise ValueError('Navigation assets must remain inside the public artifact')
        roots.add(root)
        def binding(match):
            deployment = json.loads(match.group(1))
            deployment['hosted_status'] = config
            deployment.pop('hosted_activity', None)
            deployment.pop('ask_bob', None)
            bindings.setdefault(root, deployment)
            return ('window.WAKE_DEPLOYMENT=' + json.dumps(deployment)
                    + ";document.documentElement.dataset.wakeHostedStatus='true';")
        from .report import _masthead_navigation
        page = _masthead_navigation(page)
        # Existing exported Console pages keep their generated data bindings.
        # Add the current correction entry without replacing their HTML shell.
        if path.name == 'console.html' and 'class="self-correction-console-link"' not in page:
            entry = f'<a class="self-correction-console-link" href="{prefix}self-correction/">Self-correction →</a>'
            page = page.replace('<button id="reset-console-layout"', entry + '<button id="reset-console-layout"', 1)
        page = page.replace("document.documentElement.dataset.wakeHostedStatus='true';", '')
        page, count = re.subn(r'window\.WAKE_DEPLOYMENT=(\{[^<]*?\});', binding, page)
        if count != 1:
            raise ValueError('Hosted page must have one generated deployment binding')
        page = re.sub(r'<a\b[^>]*class="[^"]*actions-light[^"]*"[^>]*>.*?</a>', '', page, flags=re.S)
        page = page.replace('class="header-tools">', 'class="header-tools">' + light, 1)
        page = re.sub(r'((?:nav\.js|masthead\.css)\?v=)[^"<]+', r'\g<1>20261027-quota-picker', page)
        page = re.sub(r'(href="(?:\.\./)*theme\.css)(?:\?[^"]*)?"',
                      lambda match: match.group(1)+'?v='+revision[:12]+'"', page)
        page = re.sub(r'<script src="[^\"]*hosted-status\.js[^\"]*"[^>]*></script>', '', page)
        page = page.replace('</head>', f'<script src="{prefix}hosted-status.js?v=20261028-aggregate-status" defer></script></head>', 1)
        page = re.sub(r'((?:runtime-activity\.js|installation-console\.js|process-field\.js|research\.js)\?v=)[^"<]+', r'\g<1>20261020-hosted-activity', page)
        page = re.sub(r'((?:research\.js|research\.css)\?v=)[^"<]+', r'\g<1>20261021-fit-history', page)
        page = re.sub(r'(installation-console\.js\?v=)[^"<]+', r'\g<1>20261020-masthead-menu', page)
        path.write_text(page)
    if not roots:
        raise ValueError('No generated hosted pages found')
    for root in roots:
        for name in ('theme.css', 'nav.js', 'masthead.css', 'hosted-status.js', 'runtime-activity.js', 'installation-console.js', 'process-field.js', 'research.js', 'research.css'):
            shutil.copyfile(assets / name, root / name)
        deployment_path = root / 'deployment.json'
        if deployment_path.exists():
            deployment = json.loads(deployment_path.read_text())
            deployment['hosted_status'] = config
            deployment.pop('hosted_activity', None)
            deployment.pop('ask_bob', None)
            deployment_path.write_text(json.dumps(deployment))
    # Personal colonies stay browser-local; Bob’s dedicated shared checkpoint is a separate read-only presentation.
    farm_assets=('ant-farm.css','ant-colony.js','ant-drawing.js','ant-farm.js','bob-ant-farm.js',
                 'ant-experiment.css','ant-experiment.js')
    for root in roots:
        for name in farm_assets:
            shutil.copyfile(assets/name,root/name)
        (root/'backgrounds').mkdir(exist_ok=True)
        for name in ('ant-soil-v1.png','ant-body-v1.png','ant-sand-v2.png','ant-room-day-v1.webp','ant-room-night-v1.webp'):
            shutil.copyfile(assets/'backgrounds'/name,root/'backgrounds'/name)
        deployment=json.loads((root/'deployment.json').read_text()) if (root/'deployment.json').exists() else {'schema':1,'mode':'hosted','snapshot_only':True}
        deployment.pop('hosted_activity', None)
        deployment.pop('ask_bob', None)
        farm=(assets/'ant-farm.html').read_text().replace('<head>', '<head><script>window.WAKE_DEPLOYMENT='+json.dumps(deployment)+';</script>',1)
        (root/'ant-farm.html').write_text(farm)
        experiment=(assets/'ant-experiment.html').read_text().replace('<head>', '<head><script>window.WAKE_DEPLOYMENT='+json.dumps({**deployment, 'presentation_revision': revision})+';</script>',1)
        (root/'ant-experiment.html').write_text(experiment)
    from .reader_presentation import refresh_public_reader
    for root in roots:
        refresh_public_reader(root)
        # Deliver the reader independently of runtime adoption. Reuse the
        # exporter binding so captured installation identity and operator links
        # survive; presentation refresh must not generate scientific results.
        from .report import _deployment_site
        deployment_path = root/'deployment.json'
        deployment = json.loads(deployment_path.read_text()) if deployment_path.exists() else bindings[root]
        page = root/'scientific-research.html'
        page.write_bytes((assets/page.name).read_bytes())
        (root/'scientific-research.js').write_bytes((assets/'scientific-research.js').read_bytes())
        _deployment_site(root, standalone=deployment.get('mode')=='standalone',
                         installation={**deployment, 'presentation_revision': revision},
                         pages=[page, root/'ant-farm.html', root/'ant-experiment.html'])
        # The refreshed audit reader is created after the captured-page pass.
        # Give it the same hosted observer instead of silently losing its light.
        audit = page.read_text().replace('class="header-tools">', 'class="header-tools">' + light, 1)
        audit = audit.replace('</head>', '<script>document.documentElement.dataset.wakeHostedStatus="true";</script>'
                              '<script src="hosted-status.js" defer></script></head>', 1)
        page.write_text(audit)
    # The served interface and public data have separate delivery lifecycles.
    # Bind only hosted exports; ordinary/local readers never discover GitHub.
    data_assets=('public-data.js','map.js','map3d.js','flat-view.js','console-tools.js')
    for root in roots:
        for name in data_assets:
            shutil.copyfile(assets/name,root/name)
        public_data={'repository':repository,'branch':'wake-public',
                     'installation_id':manifest['installation_id'],
                     'prefix':root.relative_to(site).as_posix().strip('.')}
        if public_data['prefix']:
            public_data['prefix']+='/'
        deployment_path=root/'deployment.json'
        deployment=json.loads(deployment_path.read_text()) if deployment_path.exists() else {'schema':1,'mode':'hosted','snapshot_only':True}
        deployment['public_data']=public_data
        deployment_path.write_text(json.dumps(deployment))
        for page_path in root.rglob('*.html'):
            relative=page_path.relative_to(root)
            if 'inspect' in relative.parts or 'nodes' in relative.parts or 'self-correction' in relative.parts or page_path.name=='ant-experiment.html':
                continue
            page=page_path.read_text()
            if 'window.WAKE_DEPLOYMENT=' in page:
                def data_binding(match):
                    bound=json.loads(match.group(1));bound['public_data']=public_data
                    return 'window.WAKE_DEPLOYMENT='+json.dumps(bound)+';'
                page=re.sub(r'window\.WAKE_DEPLOYMENT=(\{[^<]*?\});',data_binding,page)
            else:
                continue
            feed_base='https://raw.githubusercontent.com/'+repository+'/wake-public/'+public_data['prefix']
            page=re.sub(r'href="(?:\.\./)*(blog|journal)\.xml"',
                        lambda match:'href="'+feed_base+match.group(1)+'.xml"',page)
            # Load synchronously before any inline data consumer starts.
            page=re.sub(r'<script src="[^\"]*public-data\.js[^\"]*"[^>]*></script>','',page)
            prefix='../'*len(relative.parts[:-1])
            page=re.sub(r'(window\.WAKE_DEPLOYMENT=\{[^<]*?\};[^<]*</script>)',
                        lambda match:match.group(1)+f'<script src="{prefix}public-data.js?v={revision[:12]}"></script>',page,count=1)
            # Browser caches must not retain an older status/aggregation contract
            # after a presentation release, especially across Safari navigation.
            page=re.sub(r'((?:nav\.js|masthead\.css|installation-console\.js|hosted-status\.js|scientific-research\.js|reader-data\.js))(?:\?v=[^"<]+)?"',
                        lambda match:match.group(1)+'?v='+revision[:12]+'"',page)
            page_path.write_text(page)
    shutil.copytree(assets / 'self-correction', site / 'self-correction', dirs_exist_ok=True)
    # This independent reader has no generated masthead binding. Give it only
    # the identified root snapshot transport, never operator/runtime controls.
    correction = site / 'self-correction/index.html'
    correction_binding = {'schema': 1, 'snapshot_only': True,
                          'public_data': {'repository': repository, 'branch': 'wake-public',
                                          'installation_id': manifest['installation_id'], 'prefix': ''}}
    encoded_binding = json.dumps(correction_binding).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    page = correction.read_text().replace('<head>', '<head><script>window.WAKE_DEPLOYMENT='
            + encoded_binding + ';</script><script src="../public-data.js?v='
            + revision[:12] + '"></script>', 1)
    page = re.sub(r'((?:self-correction\.js|self-correction\.css))(?:\?v=[^"<]+)?"',
                  lambda match: match.group(1) + '?v=' + revision[:12] + '"', page)
    correction.write_text(page)
    manifest['presentation'] = {'source_revision': revision, 'hosted_status': config,
                                'data_transport':'github-pinned@1'}
    encoded = json.dumps(manifest, sort_keys=True)
    for path in [site / 'installation.json', *site.glob('nodes/*/installation.json')]:
        path.write_text(encoded)
    return manifest
