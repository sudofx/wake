"""Opt-in loopback reader prototype over completed installation exports.

This host process owns no research records or provider credentials. Requests cross
the container boundary over stdin, then the existing owning worker's private IPC.
"""
from __future__ import annotations

import argparse
from functools import partial
from http.server import ThreadingHTTPServer
import json
from pathlib import Path
import secrets
import subprocess
import threading
import time
from urllib.parse import unquote, urlsplit

from .report import PublicSnapshotHandler

MAX_REQUEST = 64 * 1024
MAX_RESPONSE = 64 * 1024
PUBLIC_SUFFIXES = {'.html', '.css', '.js', '.json', '.jsonl', '.xml', '.svg',
                   '.png', '.webp', '.jpg', '.jpeg', '.ico', '.woff', '.woff2'}


def completed_site(root, node=None):
    """Translate only this installation's container-absolute generation link.

    Docker writes /data/... symlinks into the host bind mount. Never follow an
    arbitrary link outside the installation, even when previewing on the host.
    """
    root = Path(root).resolve()
    site = root / 'nodes' / node / 'site' if node else root / 'site'
    current = site / 'current'
    if current.is_symlink():
        target = current.readlink()
        if target.is_absolute() and target.is_relative_to('/data'):
            target = root / target.relative_to('/data')
        elif not target.is_absolute():
            target = site / target
    else:
        target = current
    target = target.resolve(strict=True)
    if not target.is_relative_to(site.resolve()) or not target.is_dir():
        raise ValueError('Completed export link escapes its installation site')
    return target


def verify_container(container, root):
    """Fail before serving if the selected container does not own this installation."""
    def inspect(template):
        result = subprocess.run(['docker', 'inspect', '--format', template, container],
                                capture_output=True, text=True, timeout=10, check=True)
        return result.stdout.strip()
    if inspect('{{index .Config.Labels "com.sudofx.wake.installation"}}') != 'true':
        raise ValueError('Select a managed WAKE installation container')
    if inspect('{{.State.Running}}') != 'true':
        raise ValueError('The selected installation container is not running')
    mounts = json.loads(inspect('{{json .Mounts}}'))
    sources = {item['Destination']: Path(item['Source']).resolve() for item in mounts
               if item.get('Type') == 'bind'}
    if sources.get('/data') != Path(root).resolve():
        raise ValueError('Container /data does not match the selected installation directory')
    if sources.get('/workspace') != Path(__file__).resolve().parents[1]:
        raise ValueError('Container /workspace does not match this source checkout')


class ReaderPreview(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, root, *, port=8766, container='wake', bridge=None):
        self.root = Path(root).resolve()
        identity = json.loads((self.root / 'installation-id.json').read_text())
        self.installation_id = identity['id']
        if not (completed_site(self.root) / 'reader-data.json').is_file():
            raise ValueError('A completed installation reader export is required')
        self.token = secrets.token_urlsafe(32)
        self.busy = threading.Lock()
        self.attempts = 0
        self.next_request = 0.0
        self.container = container
        self.bridge = bridge or self.container_bridge
        super().__init__(('127.0.0.1', port), partial(ReaderPreviewHandler,
                                                   directory=str(self.root / 'site/current')))
        self.origin = f'http://127.0.0.1:{self.server_port}'

    def container_bridge(self, packet):
        result = subprocess.run(
            ['docker', 'exec', '-i', '-e', 'PYTHONPATH=/workspace', self.container,
             'python', '-m', 'wake.reader_questions', 'bridge',
             '--data', '/data/nodes/100.wake/record'],
            input=json.dumps(packet, ensure_ascii=False).encode(),
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=100)
        # Provider errors and visitor text must never leak through subprocess logs.
        if result.returncode or len(result.stdout) > MAX_RESPONSE:
            raise ValueError('The local reader worker is unavailable; check local installation readiness')
        return json.loads(result.stdout)


class ReaderPreviewHandler(PublicSnapshotHandler):
    def log_message(self, *_):
        pass  # No URLs, visitor questions, responses or history in access logs.

    def end_headers(self):
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def authorized_host(self):
        return self.headers.get('Host') == self.server.origin.removeprefix('http://')

    def json_response(self, status, packet):
        body = json.dumps(packet, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'no-referrer')
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if not self.authorized_host():
            self.send_error(403)
            return
        route = unquote(urlsplit(self.path).path)
        if route == '/ask-bob/capabilities':
            self.json_response(200, {'enabled': True, 'token': self.server.token,
                                    'installation_id': self.server.installation_id,
                                    'max_attempts': 24, 'local_only': True})
            return
        super().do_GET()

    def do_HEAD(self):
        if not self.authorized_host():
            self.send_error(403)
            return
        super().do_HEAD()

    def translate_path(self, path):
        route = unquote(urlsplit(path).path)
        parts = route.strip('/').split('/') if route.strip('/') else ['index.html']
        denied = str(self.server.root / '.unavailable')
        if any(part.startswith('.') or '\\' in part for part in parts):
            return denied
        node = None
        if parts[0] == 'nodes':
            from .installation import NODE_IDS
            if len(parts) < 3 or parts[1] not in NODE_IDS:
                return denied
            node, parts = parts[1], parts[2:]
        try:
            base = completed_site(self.server.root, node)
        except (OSError, RuntimeError, ValueError):
            return denied
        candidate = base.joinpath(*parts)
        try:
            resolved = candidate.resolve(strict=True)
        except (OSError, RuntimeError):
            return denied
        from .inspection import PUBLIC_FILES as INSPECTION_FILES
        inspection_text = len(parts) == 2 and parts[0] == 'inspect' and parts[1] in INSPECTION_FILES
        if (not resolved.is_relative_to(base) or not resolved.is_file()
                or (resolved.suffix.lower() not in PUBLIC_SUFFIXES and not inspection_text)):
            return denied
        return str(resolved)

    def do_POST(self):
        server = self.server
        if (not self.authorized_host() or self.headers.get('Origin') != server.origin
                or not secrets.compare_digest(self.headers.get('X-Wake-Reader-Token', ''), server.token)):
            self.json_response(403, {'error': 'Open the local reader preview to ask a question'})
            return
        if self.path != '/ask-bob':
            self.json_response(404, {'error': 'Unknown reader endpoint'})
            return
        try:
            length = int(self.headers.get('Content-Length', '0'))
        except ValueError:
            length = 0
        if (not 0 < length <= MAX_REQUEST or self.headers.get('Transfer-Encoding')
                or self.headers.get_content_type() != 'application/json'):
            self.json_response(413, {'error': 'Use a bounded JSON question request'})
            return
        self.connection.settimeout(5)
        try:
            packet = json.loads(self.rfile.read(length))
            if not isinstance(packet, dict):
                raise ValueError()
        except (ValueError, OSError, RecursionError):
            self.json_response(400, {'error': 'Invalid question request'})
            return
        if not server.busy.acquire(blocking=False):
            self.json_response(429, {'error': 'A reader question is already in progress'})
            return
        try:
            if server.attempts >= 24 or time.monotonic() < server.next_request:
                self.json_response(429, {'error': 'Reader preview limit reached; wait before trying again'})
                return
            server.attempts += 1
            server.next_request = time.monotonic() + 5
            try:
                result = server.bridge(packet)
                if not isinstance(result, dict) or len(json.dumps(result).encode()) > MAX_RESPONSE:
                    raise ValueError('Invalid worker response')
            except (ValueError, OSError, subprocess.SubprocessError):
                self.json_response(503, {'error': 'The local reader worker is unavailable; no answer was confirmed'})
                return
            self.json_response(200, result)
        finally:
            server.busy.release()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=Path('data/installation'))
    parser.add_argument('--container', default='wake')
    parser.add_argument('--port', type=int, default=8766)
    args = parser.parse_args(argv)
    verify_container(args.container, args.data)
    with ReaderPreview(args.data, port=args.port, container=args.container) as server:
        print(f'Local Ask Bob preview: {server.origin}/blog.html (24 attempts per preview process)', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()
