"""Private worker RPC for bounded explanations of completed public exports.

Only the existing worker opens its record. The bridge transports transient JSON;
it cannot open authority, change controls, or select models or credentials.
"""
import argparse
from dataclasses import asdict
import hashlib
import json
import os
from pathlib import Path
import re
import socket
import socketserver
import sys
import threading
import time
from urllib.parse import quote

from .application import APPLICATION_ID
from .group_coordinator import group_provider_gate
from .kernel.generation import GeminiGenerationProvider, GenerationRequest
from .kernel.models import Context, SubmissionProvenance
from .kernel.runtime import InvocationLifecycle
from .kernel.providers import ProviderQuotaError, ProviderTemporaryError
from .kernel.storage import ApplicationAccessError
from .installation_gate import InstallationSlotUnavailable
from .providers import ProviderCallPaused
from .reader_context import prepare_context

MAX_REQUEST_BYTES = 96 * 1024
MAX_REPLY_BYTES = 64 * 1024
MAX_ATTEMPTS = 24
ANSWER_SCHEMA = {
    'type': 'object', 'properties': {
        'answer': {'type': 'string'},
        'citations': {'type': 'array', 'items': {'type': 'string'}},
    }, 'required': ['answer', 'citations'], 'additionalProperties': False,
}


def socket_path(data):
    # Docker Desktop bind mounts cannot carry Unix-domain sockets.
    identity = hashlib.sha256(str(Path(data).resolve()).encode()).hexdigest()[:16]
    return Path('/tmp') / ('wake-reader-' + identity + '.sock')


def _encode(packet):
    return json.dumps(packet, ensure_ascii=False, separators=(',', ':'), allow_nan=False).encode()


def validate_answer(raw, context):
    if not isinstance(raw, str) or len(raw.encode()) > 24_000:
        raise ValueError('Invalid reader answer')
    packet = json.loads(raw)
    if not isinstance(packet, dict) or set(packet) != {'answer', 'citations'}:
        raise ValueError('Invalid reader answer')
    answer, cited = packet['answer'], packet['citations']
    sources = {item['id']: item for item in context['sources']}
    if (not isinstance(answer, str) or not answer.strip() or len(answer) > 6000
            or not isinstance(cited, list) or not 1 <= len(cited) <= len(sources)
            or any(not isinstance(item, str) or item not in sources for item in cited)
            or len(set(cited)) != len(cited)
            or any(item not in cited for item in re.findall(r'\[(S\d+)\]', answer))):
        raise ValueError('Invalid reader answer citations')
    selected = []
    for identifier in cited:
        source = dict(sources[identifier])
        route = {'posts': 'blog/', 'evidence': 'evidence/',
                 'projects': 'projects/', 'notebooks': 'projects/notebook:'}.get(source.get('collection'))
        if route and isinstance(source.get('record_id'), str):
            source['url'] = 'index.html#' + route + quote(source['record_id'], safe='')
        selected.append(source)
    return answer, selected


class ReaderQuestions:
    def __init__(self, engine, settings, site, should_pause):
        self.engine, self.settings, self.site = engine, settings, Path(site)
        self.should_pause = should_pause
        self.attempts = 0
        self.busy = threading.Lock()

    def answer(self, request):
        if not self.busy.acquire(blocking=False):
            return {'ok': False, 'error': 'busy'}
        try:
            if self.should_pause():
                return {'ok': False, 'error': 'paused'}
            if self.attempts >= MAX_ATTEMPTS:
                return {'ok': False, 'error': 'session_limit'}
            try:
                with self.engine.store.lock():
                    return self._answer_locked(request)
            except Exception:
                # Never echo exception strings containing question/provider text.
                return {'ok': False, 'error': 'busy_or_unavailable'}
        finally:
            self.busy.release()

    def _answer_locked(self, request):
        access = self.engine.store.kernel.application_access_state()
        if not access.enabled:
            return {'ok': False, 'error': 'access_blocked'}
        try:
            # Pin the completed generation once. Retirement during bounded reads
            # fails closed or is reported missing by the public-context owner.
            prepared = prepare_context((self.site / 'current').resolve(strict=True), request)
        except (ValueError, OSError, TypeError, KeyError):
            return {'ok': False, 'error': 'invalid_or_unavailable_article'}
        if self.should_pause():
            return {'ok': False, 'error': 'paused'}
        key = os.environ.get('GEMINI_API_KEY')
        if not key:
            return {'ok': False, 'error': 'provider_unavailable'}
        gate = group_provider_gate(self.settings, should_pause=self.should_pause)
        if gate is None or not gate.url:
            return {'ok': False, 'error': 'coordinator_unavailable'}
        gate.wait_seconds = min(gate.wait_seconds, 10)
        generation = GenerationRequest(
            model=self.settings['model'], system=prepared['system'],
            prompt=prepared['prompt'],
            response_schema=ANSWER_SCHEMA, max_output_tokens=1800, tools=(),
        )
        # Exact private context is fingerprinted, never copied to the journal.
        context = Context(revision=self.engine.store.kernel.context().revision,
                          state={'generation_request': asdict(generation)}, recent_receipts=())
        lifecycle = InvocationLifecycle.begin(
            self.engine.store.record, context,
            provenance=SubmissionProvenance('model', 'google-gemini', generation.model,
                                           purpose='Explain completed public exports for a local reader'),
            context_scope={'kind': 'application', 'application_id': APPLICATION_ID, 'purpose': 'reader'},
        )
        self.attempts += 1

        def effect():
            with gate.request(generation.model):
                try:
                    # Queue waiting cannot outlive a revoked application latch.
                    self.engine.store.kernel.require_application_access(access.generation)
                    response = GeminiGenerationProvider(key, timeout_seconds=60).generate(generation)
                except Exception as error:
                    details = getattr(error, 'details', {})
                    gate.outcome = dict(details) if isinstance(details, dict) else {}
                    gate.outcome['result'] = ('daily_quota' if any('PerDay' in value for value in gate.outcome.get('quota_ids', []))
                                              else 'rate_limited' if gate.outcome.get('http_status') == 429 else 'failed')
                    raise
                gate.outcome = {'result': 'success'}
                return response
        try:
            started = time.monotonic()
            response = lifecycle.invoke(effect,
                effect_barrier=lambda: self.engine.store.kernel.require_application_access(access.generation),
                classify_error=lambda error:
                None if isinstance(error, ProviderCallPaused) else
                'effect_barrier_failure' if isinstance(error, ApplicationAccessError) else
                'quota_exhausted' if isinstance(error, ProviderQuotaError) else
                'temporary_failure' if isinstance(error, (ProviderTemporaryError, InstallationSlotUnavailable)) else
                'provider_failure')
        except Exception:
            return {'ok': False, 'error': 'provider_deferred_or_failed'}
        proposal_id = 'reader-answer-' + lifecycle.invocation_id
        lifecycle.proposal_received(proposal_id)
        try:
            answer, sources = validate_answer(response.text, prepared)
        except (ValueError, TypeError, KeyError):
            lifecycle.fail(proposal_id=proposal_id, detail='invalid_reader_answer')
            return {'ok': False, 'error': 'invalid_provider_answer'}
        # This stage records output validation only: no semantic application
        # action, research receipt, or provider answer is submitted or persisted.
        lifecycle.governed(proposal_id, None, 'reader_answer_validated')
        lifecycle.complete(proposal_id=proposal_id, detail='reader_answer_ready')
        usage = response.metadata.get('usage', {})
        usage = {field: value for field, value in usage.items()
                 if field in ('promptTokenCount', 'candidatesTokenCount', 'totalTokenCount', 'thoughtsTokenCount')
                 and type(value) is int and value >= 0} if isinstance(usage, dict) else {}
        metrics = {**prepared['metrics'], 'latency_ms': round((time.monotonic() - started) * 1000),
                   'output_bytes': len(response.text.encode()), 'provider_tokens': usage}
        return {'ok': True, 'answer': answer, 'sources': sources, 'citations': sources,
                'article': prepared['article'], 'metrics': metrics,
                'warnings': prepared['warnings'], 'missing': prepared['missing'],
                'condition': request.get('condition', 'C')}


class ReaderService:
    def __init__(self, data, questions):
        self.path = socket_path(data)
        self._active = threading.Event()
        active = self._active
        if self.path.exists():
            self.path.unlink()
        class Handler(socketserver.StreamRequestHandler):
            def handle(self):
                active.set()
                try:
                    self.connection.settimeout(5)
                    raw = self.rfile.readline(MAX_REQUEST_BYTES + 1)
                    if len(raw) > MAX_REQUEST_BYTES or not raw.endswith(b'\n'):
                        raise ValueError('Invalid packet')
                    packet = json.loads(raw)
                    reply = questions.answer(packet)
                    body = _encode(reply)
                    if len(body) + 1 > MAX_REPLY_BYTES:
                        body = _encode({'ok': False, 'error': 'response_limit'})
                    self.wfile.write(body + b'\n')
                except Exception:
                    try:
                        self.wfile.write(b'{"ok":false,"error":"unavailable"}\n')
                    except OSError:
                        pass
                finally:
                    active.clear()
        self.server = socketserver.UnixStreamServer(str(self.path), Handler)
        os.chmod(self.path, 0o600)
        self.thread = threading.Thread(target=self.server.serve_forever, kwargs={'poll_interval': .1})
        self.thread.start()

    @property
    def active(self):
        return self._active.is_set()

    def close(self):
        # shutdown waits for the active synchronous handler, then join before
        # closing the owning record. Disconnect never releases a provider grant.
        self.server.shutdown()
        self.thread.join()
        self.server.server_close()
        self.path.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['bridge'])
    parser.add_argument('--data', required=True)
    args = parser.parse_args()
    try:
        raw = sys.stdin.buffer.read(MAX_REQUEST_BYTES + 1)
        if len(raw) > MAX_REQUEST_BYTES:
            raise ValueError('Invalid packet')
        packet = json.loads(raw)
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
            client.settimeout(95)
            client.connect(str(socket_path(args.data)))
            client.sendall(_encode(packet) + b'\n')
            with client.makefile('rb') as stream:
                reply = stream.readline(MAX_REPLY_BYTES + 1)
            if len(reply) > MAX_REPLY_BYTES:
                raise ValueError('Invalid response')
            result = json.loads(reply)
    except Exception:
        result = {'ok': False, 'error': 'reader_worker_unavailable'}
    print(_encode(result).decode())


if __name__ == '__main__':
    main()
