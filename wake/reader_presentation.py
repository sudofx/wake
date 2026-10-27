"""Refresh generated reading pages from current presentation source."""
import json
import re
from pathlib import Path


def retired_reader_asset(path):
    """Identify derived assets removed from already captured public snapshots."""
    return (path.name == 'help.js'
            or path.name.startswith(('ask-bob', 'bob-chat', 'bob-markdown'))
            or ('reader-records' in path.parts and 'guides' in path.parts))


def remove_retired_reader(site):
    """Retire removed reader UI without changing research/inspection bytes."""
    site = Path(site)
    marker = '/* Private browser conversation views; never research authority or exported state. */'
    app = '/* Render exported research records and reader navigation; browser interactions never mutate authority. */'
    for path in site.rglob('*'):
        if not path.is_file() or 'inspect' in path.relative_to(site).parts:
            continue
        if retired_reader_asset(path):
            path.unlink()
        elif path.suffix == '.html':
            text = path.read_text()
            start = text.find(marker)
            if start >= 0:
                end = text.find(app, start)
                if end < 0:
                    end = text.find('</script>', start)
                if end < 0:
                    raise ValueError('Incomplete retired reader script')
                text = text[:start] + text[end:]
            text = re.sub(r'<(?:script|link)\b[^>]*(?:ask-bob|bob-chat|bob-markdown)[^>]*>(?:</script>)?', '', text)
            # Older exports inline this retired feature, including on node pages.
            text = re.sub(r'<script\b[^>]*>\s*/\*\s*\*?\s*WAKE✳︎ plain-language help\..*?</script>', '', text, flags=re.S)
            text = re.sub(r'<script\b[^>]*src="[^"]*\bhelp\.js(?:\?[^"]*)?"[^>]*>\s*</script>', '', text)
            text = re.sub(r'<button\b[^>]*\bdata-help="[^"]*"[^>]*>.*?</button>', '', text, flags=re.S)
            text = re.sub(r'<div\b[^>]*\bid="help-layer"[^>]*>.*?</section>\s*</div>', '', text, flags=re.S)
            path.write_text(text)

def refresh_public_reader(site):
    """Refresh derived reader assets from the exact captured public archive only."""
    from .reader_transport import record_path
    site = Path(site)
    archive = site / 'wake-data.json'
    if not archive.exists():
        return
    data = json.loads(archive.read_text())
    overview = json.loads((site / 'reader-data.json').read_text())
    if data['head'] != overview['head']:
        raise ValueError('Reader refresh requires one captured snapshot')
    assets = Path(__file__).parent / 'assets'
    previous_pet = (site / 'pet.js').read_text() if (site / 'pet.js').exists() else None
    for page in site.glob('*.html'):
        text = page.read_text()
        if previous_pet and previous_pet in text:
            text=text.replace(previous_pet, (assets / 'pet.js').read_text())
        pet_marker='/* Homepage reading experience'
        pet_start=text.find(pet_marker)
        if pet_start>=0:
            pet_end=text.find('</script>',pet_start)
            if pet_end<0:raise ValueError('Reader page has an incomplete research presentation script')
            text=text[:pet_start]+(assets/'pet.js').read_text()+text[pet_end:]
        marker='/* Render exported research records and reader navigation; browser interactions never mutate authority. */'
        start=text.find(marker)
        if start>=0:
            end=text.find('</script>',start)
            if end<0:raise ValueError('Reader page has an incomplete application script')
            text=text[:start]+(assets/'app.js').read_text()+text[end:]
        # Captured public HTML can predate automatic list loading.
        text=re.sub(r'<button\b[^>]*\bid="(more|history-more)"[^>]*>.*?</button>',
                    lambda match: '<p id="'+match.group(1)+'" class="more" role="status" hidden>Scroll for more</p>', text, flags=re.S)
        text=re.sub(r'(src="reader-data\.js)(?:\?[^"]*)?(")',r'\1?v=20261027-autoload\2',text)
        page.write_text(text)
    for name in ('style.css','console-light.css','reader-theme.css',
                 'evaluation-view.js','reader-data.js','app.js','pet.js',
                 'bob-ant-farm.js','ant-colony.js','site-theme.js'):
        (site/name).write_bytes((assets/name).read_bytes())
    # Invocation IDs keep journal detail identity distinct across nodes that share a cycle number.
    for row in data['state'].get('journal', []):
        identifier = row.get('invocation')
        if not identifier:
            continue
        path = site / record_path('journal', identifier)
        path.parent.mkdir(parents=True, exist_ok=True)
        related = {'invocations': {identifier: data['state']['invocations'][identifier]}} if identifier in data['state'].get('invocations', {}) else {}
        path.write_text(json.dumps({'head': data['head'], 'collection': 'journal', 'item': row, 'related': related}, ensure_ascii=False, separators=(',', ':')))
