"""Unified reader-facing website, derived entirely from dated node snapshots."""
from pathlib import Path
import re

from .report import export, atomic_write, _deployment_site


def export_unified_site(projection, target):
    target = Path(target)
    export(None, target, projection=projection, standalone=True, browser_only=True)
    assets = Path(__file__).parent / 'assets'
    dashboard = (assets / 'installation.html').read_text()
    content = re.search(r'<main[^>]*>(.*?)<noscript>', dashboard, re.S).group(1)
    content = re.sub(r'<footer.*?</footer>', '<p id="installation-provenance" class="installation-caption"></p>', content, flags=re.S)
    content = content.replace('<h1 id="installation-name">WAKE✳︎ Console</h1>', '<h2 id="installation-name">Installation overview</h2>')
    content = content.replace('Inspect the installation, then open a node’s full Console to follow its record.',
        'A combined view of recorded work. Select a node to inspect its contribution.')
    # Keep the normal Console and its ordered workspace intact. Installation
    # observations precede it as one optional expandable section.
    content = content.replace('<section class="panel installation-panel"', '<details class="installation-extra"><summary>Node comparison</summary><section class="panel installation-panel"', 1)
    content = content.replace('<div class="installation-columns">', '</details><details class="installation-extra"><summary>Group activity and things to watch</summary><div class="installation-columns">', 1)
    content += '</details>'
    console = (target / 'console.html').read_text()
    console = console.replace('class="research-page"', 'class="research-page installation-page unified-console"')
    console = console.replace('<main id="main" tabindex="-1">', '<main id="main" tabindex="-1"><section class="installation-overview">' + content + '</section>', 1)
    atomic_write(target / 'console.html', console)
    _deployment_site(target, standalone=True, installation={'unified': True, 'instance_name': 'WAKE✳︎'})
    return {'path': str(target / 'index.html'), 'head': projection['head']}
