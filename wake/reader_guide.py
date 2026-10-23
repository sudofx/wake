"""Publication-time passage index over already filtered public records only."""
import re
from .reader_context import article_descriptor

MAX_GUIDE_BYTES = 96 * 1024
MAX_PASSAGES = 180
MAX_LINKED = 24
STOP = frozenset('the a an and or of to in on at for is are was were be been this that it its with from as by we our they their not can could would should what how why when where which does do about'.split())


def terms(text):
    return sorted(set(re.findall(r'[a-z0-9]{3,}', text.lower())) - STOP)


def build_guide(post, state, head):
    """No provider, authority reads or new facts: preserve literal source excerpts."""
    import json
    sources, passages, omitted = [], [], []
    guide = {'schema': 1, 'head': head, 'article': article_descriptor(post, head),
             'sources': sources, 'passages': passages, 'omitted': omitted}
    def size():
        return len(json.dumps(guide, ensure_ascii=False, separators=(',', ':')).encode())
    def add(collection, item):
        if collection == 'evidence':
            from .research_projection import _evidence_class
            quality = _evidence_class(item)
            if quality in ('receipt', 'metadata', 'discovery', 'background', 'unreadable'):
                omitted.append({'collection': collection, 'id': item['id'], 'reason': quality + '; not readable source evidence'})
                return
            try:
                payload = json.loads(item.get('content', ''))
            except (ValueError, TypeError):
                payload = None
            if isinstance(payload, dict):
                item = {**item, 'title': payload.get('title') or payload.get('url') or item.get('source') or item['id'],
                        'content': payload.get('excerpt', '')}
        sid = 'S' + str(len(sources) + 1)
        route = {'posts': 'blog.html#blog/', 'notebooks': 'index.html#projects/notebook:',
                 'projects': 'index.html#projects/', 'evidence': 'index.html#evidence/'}[collection]
        from urllib.parse import quote
        sources.append({'id': sid, 'collection': collection, 'record_id': item['id'],
                        'label': str(item.get('title') or item.get('question') or item['id'])[:240],
                        'url': route + quote(item['id'], safe=''), 'head': head})
        if size() > MAX_GUIDE_BYTES - 2048:
            sources.pop()
            return
        # Field order makes a concise editorial summary available without inventing one.
        fields = ('lede', 'body') if collection == 'posts' else ('question', 'summary', 'content', 'body', 'findings', 'limitations', 'uncertainties')
        seen = set()
        source_passages = 0
        for field in fields:
            value = item.get(field)
            if not isinstance(value, str):
                continue
            for paragraph in re.split(r'\n\s*\n', value):
                paragraph = paragraph.strip()
                if not paragraph or paragraph in seen:
                    continue
                seen.add(paragraph)
                # Bounded literal excerpts; offsets and lengths expose clipping.
                for start in range(0, min(len(paragraph), 6000), 1000):
                    text = paragraph[start:start + 1000]
                    row = {'source': sid, 'field': field, 'text': text,
                           'offset': start, 'excerpted': len(paragraph) > 1000,
                           'terms': terms(text)}
                    if source_passages >= (32 if collection == 'posts' else 12):
                        omitted.append({'collection': collection, 'id': item['id'], 'reason': 'source passage budget'})
                        return
                    passages.append(row)
                    source_passages += 1
                    if len(passages) > MAX_PASSAGES or size() > MAX_GUIDE_BYTES - 2048:
                        passages.pop()
                        omitted.append({'collection': collection, 'id': item['id'], 'reason': 'passage budget'})
                        return
    add('posts', post)
    links = []
    for collection, identifiers in (('notebooks', post.get('notebooks', [])),
                                     ('evidence', post.get('evidence', [])),
                                     ('projects', [post.get('project')])):
        for identifier in identifiers:
            if isinstance(identifier, str) and identifier and (collection, identifier) not in links:
                links.append((collection, identifier))
    # Shared Bob articles name node notebooks through editorial references rather
    # than post.notebooks. Resolve only IDs in the already public unified state.
    from urllib.parse import urlsplit, unquote
    for group in post.get('editorial_references', []) or []:
        for reference in group if isinstance(group, list) else []:
            if not isinstance(reference, dict):
                continue
            member = reference.get('member', '')
            if member not in {f'{parent + child}.wake' for parent in (100, 200, 300) for child in range(4)}:
                continue
            notebook = reference.get('notebook_id')
            if isinstance(notebook, str):
                key = ('notebooks', member + '::' + notebook)
                if key not in links:
                    links.append(key)
            for source in reference.get('sources', []) or []:
                if not isinstance(source, dict):
                    continue
                parsed = urlsplit(str(source.get('record_url', '')))
                fragment = unquote(parsed.fragment)
                if parsed.scheme or parsed.netloc or parsed.query or parsed.path not in (f'/nodes/{member}/index.html', f'/nodes/{member}/evidence.html') or not fragment.startswith('evidence/'):
                    continue
                key = ('evidence', member + '::' + fragment[len('evidence/'):])
                if key not in links:
                    links.append(key)
    for collection, identifier in links[:MAX_LINKED]:
        item = state.get(collection, {}).get(identifier)
        if item:
            add(collection, item)
        else:
            omitted.append({'collection': collection, 'id': identifier, 'reason': 'not publicly available'})
    if len(links) > MAX_LINKED:
        omitted.append({'reason': 'linked source budget', 'count': len(links) - MAX_LINKED})
    # Source metadata is bounded too. Never publish a malformed partial JSON packet.
    if size() > MAX_GUIDE_BYTES:
        raise ValueError('Reader guide metadata exceeds budget')
    return guide


def refresh_public_reader(site):
    """Refresh derived reader assets from the exact captured public archive only."""
    import json
    from pathlib import Path
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
    previous = (site / 'ask-bob.js').read_text() if (site / 'ask-bob.js').exists() else None
    current = (assets / 'ask-bob.js').read_text()
    for page in site.glob('*.html'):
        text = page.read_text()
        if previous and previous in text:
            page.write_text(text.replace(previous, current))
    for name in ('ask-bob.js', 'ask-bob.css', 'ask-bob-guide.js', 'ask-bob-browser.js'):
        (site / name).write_bytes((assets / name).read_bytes())
    for post in data['state'].get('posts', {}).values():
        guide = build_guide(post, data['state'], data['head'])
        path = site / record_path('guides', post['id'])
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(guide, ensure_ascii=False, separators=(',', ':')))
