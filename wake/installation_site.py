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


def export_unified_history(generations, snapshots, target):
    """Merge complete exported streams without reading any authority database.

    Keep file handles open across rendering: a retired generation's files may be
    unlinked by its owner while these handles continue reading the captured bytes.
    The sort index contains only dates and offsets, not growing provider payloads.
    """
    from contextlib import ExitStack
    import json
    from .installation_projection import _COLLECTIONS, _remap, _prefix
    from .installation_cli import _public_projection
    target = Path(target)
    index, streams, known = [], {}, {}
    with ExitStack() as stack:
        for node, packet in snapshots.items():
            streams[node] = stack.enter_context((Path(generations[node]) / 'events.jsonl').open('rb'))
            state = packet['state']
            known[node] = {str(key) for collection in _COLLECTIONS for key in state.get(collection, {})}
            known[node].update(str(t['id']) for t in state.get('research_topics', []) if t.get('id'))
        for node, stream in streams.items():
            while True:
                offset = stream.tell()
                line = stream.readline()
                if not line:
                    break
                if not line.strip():
                    continue
                event = json.loads(line)
                index.append((str(event.get('time', '')), node, event.get('seq', 0), offset))
        with (target / 'events.jsonl').open('w') as output:
            for _, node, _, offset in sorted(index):
                streams[node].seek(offset)
                event = _public_projection(json.loads(streams[node].readline()))
                packet = snapshots[node]
                mapped = {**event, 'payload': _remap(event.get('payload', {}), node, known[node]),
                    'origin': {'node': node, 'head': packet['head'], 'version': packet['state']['version']},
                    'original_event': event, 'projection_only': True,
                    'projection_id': _prefix(node, event.get('hash') or event.get('seq'))}
                output.write(json.dumps(mapped, ensure_ascii=False, separators=(',', ':')) + '\n')
    overview = json.loads((target / 'wake-data.json').read_text())
    overview['event_history'] = {'displayed': len(overview.get('events', [])),
                                 'total': len(index), 'complete_url': 'events.jsonl'}
    atomic_write(target / 'wake-data.json', json.dumps(overview, ensure_ascii=False, separators=(',', ':')))
    return len(index)
