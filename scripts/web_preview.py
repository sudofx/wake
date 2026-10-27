#!/usr/bin/env python3
"""Preview the website from disposable fixture data; reload after source edits."""
import argparse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import subprocess
import shutil
import sys
import tempfile
import threading
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
RELOAD = b'''<script>/* Local preview only. */
let previewVersion;
setInterval(async()=>{try{const r=await fetch('/__preview',{cache:'no-store'}),s=await r.json();
if(previewVersion&&previewVersion!==s.version)location.reload();previewVersion=s.version;
}catch{}},250);</script>'''


def build(destination):
    from wake.domain_events import empty
    from wake.report import export
    state = empty()
    state.update(projects={}, notebooks={}, research={})
    state['posts'] = {'preview-story': {
        'id': 'preview-story', 'title': 'Local preview fixture',
        'lede': 'Disposable sample content for editing the website.',
        'body': 'This is fixture data, not a research result.\n\nSummary\n\nEdit source files and this page reloads.',
        'status': 'published', 'created_version': 0, 'created_by': 'preview',
        'notebooks': [], 'evidence': []}}
    export(destination=destination, projection={'state': state, 'head': '0'*64,
           'events': [], 'generated': '2026-10-26T00:00:00Z'}, browser_only=True,
           standalone=False)
    (Path(destination)/'evaluation.json').write_text(json.dumps({
        'schema': 'wake-evaluation@1', 'result_id': 'local-preview',
        'title': 'Local evaluation fixture', 'generated_at': '2026-10-26T00:00:00Z',
        'summary': 'Sample report for editing the evaluation view.',
        'metrics': [{'name': 'Fixture cases', 'value': 1}],
        'limitations': ['Fixture only; no model behavior or intelligence was measured.']}))


def fingerprint():
    return tuple((str(p), p.stat().st_mtime_ns, p.stat().st_size)
                 for p in sorted((ROOT/'wake').rglob('*'))
                 if p.is_file() and '__pycache__' not in p.parts
                 and (p.suffix == '.py' or 'assets' in p.parts))


class Preview(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, address, directory):
        self.workspace = Path(directory)
        self.current = None
        self.version = 0
        self.error = None
        self.closed = threading.Event()
        super().__init__(address, Handler)
        self.rebuild()
        self.watcher = threading.Thread(target=self.watch, daemon=True)
        self.watcher.start()

    def rebuild(self):
        start = time.monotonic()
        version = self.version + 1
        target = self.workspace/str(version)
        result = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                                 '--build', str(target)], cwd=ROOT,
                                capture_output=True, text=True)
        if result.returncode:
            self.error = result.stderr[-4000:]
            print(self.error, file=sys.stderr, flush=True)
            return False
        self.current, self.version, self.error = target, version, None
        for old in self.workspace.iterdir():
            if old.is_dir() and old.name.isdecimal() and int(old.name)<version-1:
                shutil.rmtree(old)
        print(json.dumps({'preview_version': version,
                          'build_ms': round((time.monotonic()-start)*1000)}), flush=True)
        return True

    def watch(self):
        previous = fingerprint()
        while not self.closed.wait(.1):
            current = fingerprint()
            if current != previous:
                previous = current
                self.rebuild()

    def server_close(self):
        self.closed.set()
        if hasattr(self, 'watcher'):
            self.watcher.join(timeout=5)
        super().server_close()


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='.', **kwargs)

    def log_message(self, *_):
        pass

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def do_GET(self):
        if self.path.split('?')[0] == '/__preview':
            body = json.dumps({'version': self.server.version,
                               'error': self.server.error}).encode()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if self.server.current is None:
            self.send_error(503, 'Fix the source error shown in the terminal')
            return
        self.directory = str(self.server.current)
        super().do_GET()

    def send_head(self):
        path = Path(self.translate_path(self.path))
        if path.is_dir():
            path = path/'index.html'
        if path.suffix == '.html' and path.is_file():
            import io
            body = path.read_bytes().replace(b'</body>', RELOAD.replace(b'let previewVersion;', f'let previewVersion={self.server.version};'.encode())+b'</body>')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            return io.BytesIO(body)
        return super().send_head()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8081)
    parser.add_argument('--build', type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.build:
        build(args.build)
        return
    with tempfile.TemporaryDirectory(prefix='wake-web-preview-') as directory:
        with Preview((args.host, args.port), directory) as server:
            print(f'Local fixture preview: http://{args.host}:{server.server_port}/', flush=True)
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                pass


if __name__ == '__main__':
    main()
