"""Offline transport evidence for incomplete provider answers."""
import json
import io
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import Request
from urllib.error import HTTPError
from unittest.mock import patch

from wake.kernel.generation import GeminiGenerationProvider, GenerationRequest, request_gemini_json, _safe_error_payload
from wake.kernel.providers import ProviderError


class GenerationFailureTests(unittest.TestCase):
    def test_content_length_response_bytes_do_not_extend_body_deadline(self):
        self.check_slow_response(200)

    def test_error_response_bytes_do_not_extend_body_deadline(self):
        self.check_slow_response(429)

    def test_ordinary_chunked_json_remains_supported(self):
        payload = b'{"candidates":[]}'
        class ChunkedResponse(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_GET(self):
                self.send_response(200)
                self.send_header("Transfer-Encoding", "chunked")
                self.end_headers()
                try:
                    for offset in range(0, len(payload), 4):
                        chunk = payload[offset:offset + 4]
                        self.wfile.write(f'{len(chunk):x}\r\n'.encode() + chunk + b'\r\n')
                        self.wfile.flush()
                    self.wfile.write(b"0\r\n\r\n")
                    self.wfile.flush()
                except (BrokenPipeError, ConnectionResetError):
                    pass

        server = HTTPServer(("127.0.0.1", 0), ChunkedResponse)
        worker = threading.Thread(target=server.handle_request, daemon=True)
        worker.start()
        try:
            result, status = request_gemini_json(
                Request(f"http://127.0.0.1:{server.server_port}/"), timeout=1)
            self.assertEqual((result, status), ({'candidates': []}, 200))
        finally:
            worker.join(timeout=1)
            server.server_close()

    def check_slow_response(self, status):
        payload = json.dumps({"candidates": [], "padding": "x" * 100}).encode()

        class SlowResponse(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_GET(self):
                self.send_response(status)
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                try:
                    for value in payload:
                        self.wfile.write(bytes([value]))
                        self.wfile.flush()
                        time.sleep(.02)
                except (BrokenPipeError, ConnectionResetError):
                    pass

        server = HTTPServer(("127.0.0.1", 0), SlowResponse)
        worker = threading.Thread(target=server.handle_request, daemon=True)
        worker.start()
        started = time.monotonic()
        try:
            request = Request(f"http://127.0.0.1:{server.server_port}/")
            if status == 200:
                with self.assertRaises(TimeoutError):
                    request_gemini_json(request, timeout=.15)
            else:
                with self.assertRaises(HTTPError) as caught:
                    request_gemini_json(request, timeout=.15)
                self.assertEqual(_safe_error_payload(caught.exception, deadline=started + .15), {})
                self.assertTrue(caught.exception.closed)
            # The old single read would accept the entire multi-second drip.
            self.assertLess(time.monotonic() - started, 1.0)
        finally:
            worker.join(timeout=1)
            server.server_close()

    def test_http_success_without_complete_answer_keeps_bounded_failure_evidence(self):
        partial = "private incomplete response"
        for candidates, finish_reason in (
            ([], None),
            ([None], None),
            ([{"content": {"parts": {}}}], None),
            ([{"content": {"parts": [{"text": {}}]}}], None),
            ([{"finishReason": "MAX_TOKENS", "content": {"parts": [{"text": partial}]}}], "MAX_TOKENS"),
            ([{"finishReason": "STOP", "content": {"parts": [{"thought": True, "text": partial}]}}], "STOP"),
            ([{"finishReason": []}], None),
        ):
            with self.subTest(finish_reason=finish_reason):
                payload = {
                    "candidates": candidates,
                    "modelVersion": "fixture-version",
                    "usageMetadata": {"totalTokenCount": 42, "untrusted": partial},
                }
                with patch("wake.kernel.generation.request_gemini_json", return_value=(payload, 200)) as send:
                    with self.assertRaises(ProviderError) as caught:
                        GeminiGenerationProvider("fixture-key").generate(
                            GenerationRequest(model="fixture-model", prompt="bounded fixture")
                        )
                send.assert_called_once()
                details = caught.exception.details
                self.assertEqual(details["category"], "invalid_response")
                self.assertEqual(details["http_status"], 200)
                self.assertEqual(details["model"], "fixture-model")
                self.assertEqual(details["model_version"], "fixture-version")
                self.assertEqual(details["finish_reason"], finish_reason)
                self.assertEqual(details["usage"], {"totalTokenCount": 42})
                self.assertNotIn(partial, json.dumps(details))
                self.assertNotIn("fixture-key", json.dumps(details))

    def test_non_object_transport_json_is_classified_without_retaining_payload(self):
        for value in ([], None, "private invalid body"):
            with self.subTest(shape=type(value).__name__):
                response = io.BytesIO(json.dumps(value).encode())
                response.status = 200
                with patch("urllib.request.urlopen", return_value=response):
                    with self.assertRaises(ProviderError) as caught:
                        GeminiGenerationProvider("fixture-key").generate(
                            GenerationRequest(model="fixture", prompt="bounded fixture")
                        )
                self.assertEqual(caught.exception.details["category"], "invalid_response")
                self.assertNotIn("private invalid body", json.dumps(caught.exception.details))

    def test_malformed_metadata_cannot_expand_incomplete_answer_diagnostics(self):
        payload = {
            "candidates": [{"finishReason": "X" * 5000}],
            "modelVersion": "Y" * 5000,
            "usageMetadata": {"totalTokenCount": "Z" * 5000, "thoughtsTokenCount": -1},
        }
        with patch("wake.kernel.generation.request_gemini_json", return_value=(payload, 200)):
            with self.assertRaises(ProviderError) as caught:
                GeminiGenerationProvider("fixture-key").generate(
                    GenerationRequest(model="fixture", prompt="bounded fixture")
                )
        self.assertEqual(len(caught.exception.details["finish_reason"]), 100)
        self.assertEqual(len(caught.exception.details["model_version"]), 200)
        self.assertEqual(caught.exception.details["usage"], {})

    def test_incomplete_answer_metadata_redacts_the_key_before_truncation(self):
        secret = "fixture-sensitive-key"
        payload = {
            "candidates": [{"finishReason": "X" * 90 + secret}],
            "modelVersion": "Y" * 190 + secret,
        }
        with patch("wake.kernel.generation.request_gemini_json", return_value=(payload, 200)):
            with self.assertRaises(ProviderError) as caught:
                GeminiGenerationProvider(secret).generate(
                    GenerationRequest(model="fixture", prompt="bounded fixture"))
        details = caught.exception.details
        self.assertEqual(details["finish_reason"], "X" * 90 + "[redacted]")
        self.assertEqual(details["model_version"], "Y" * 190 + "[redacted]")
        self.assertNotIn(secret, json.dumps(details))
        self.assertNotIn(secret[:10], json.dumps(details))


if __name__ == "__main__":
    unittest.main()
