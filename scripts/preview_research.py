#!/usr/bin/env python3
"""Read-only Research preview: static assets plus current public wake-live views.

No database is opened, workflow dispatched, or branch changed. The public
projection is disposable presentation; missing source classification stays unknown.
"""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import threading
import time
from urllib.request import urlopen

from wake.research_projection import build_research_projection


class PublicResearch:
    def __init__(self, directory):
        self.value = json.loads((directory / 'research-data.json').read_text())
        self.checked = 0
        self.lock = threading.Lock()

    def read(self):
        with self.lock:
            if time.monotonic() - self.checked >= 30:
                self.checked = time.monotonic()
                try:
                    with urlopen('https://raw.githubusercontent.com/sudofx/wake/wake-live/live.json', timeout=12) as response:
                        live = json.load(response)
                    if live.get('head') != self.value['head']:
                        candidate = live.get('research') or build_research_projection(
                            live['state'], live.get('events', []), live['head'],
                            generated=live.get('generated'), metrics=live.get('metrics'),
                            operation=live.get('operation'), source=live.get('source'))
                        if candidate['head'] != live['head'] or candidate['version'] != live['state']['version']:
                            raise ValueError('Public research projection does not match its snapshot')
                        self.value = candidate
                    self.value.pop('preview_transport_error', None)
                except Exception:
                    self.value['preview_transport_error'] = True
            return json.dumps(self.value, ensure_ascii=False, separators=(',', ':')).encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, default=Path('site'))
    parser.add_argument('--port', type=int, default=8947)
    args = parser.parse_args()
    # This is a hosted-data mirror, not a preview of a local installation.
    identity = args.directory / 'deployment.json'
    if not identity.exists() or json.loads(identity.read_text()).get('mode') != 'hosted':
        parser.error('Requires a hosted export; serve standalone exports with a plain static server instead')
    source = PublicResearch(args.directory)

    class Handler(SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path.split('?', 1)[0] == '/research-data.json':
                content = source.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.send_header('Cache-Control', 'no-store')
                self.send_header('Content-Length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
            else:
                super().do_GET()

    server = ThreadingHTTPServer(('127.0.0.1', args.port), partial(Handler, directory=str(args.directory)))
    print(f'Read-only Research preview: http://127.0.0.1:{args.port}/console.html', flush=True)
    server.serve_forever()


if __name__ == '__main__':
    main()
