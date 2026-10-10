import threading
import unittest
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from scripts.wake_group_proxy import GroupProxy


class _MemberHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"member response"
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *_args):
        pass


class GroupProxyTests(unittest.TestCase):
    def setUp(self):
        self.member = ThreadingHTTPServer(("127.0.0.1", 0), _MemberHandler)
        self.member_thread = threading.Thread(target=self.member.serve_forever, daemon=True)
        self.member_thread.start()

        self.proxy = ThreadingHTTPServer(("127.0.0.1", 0), GroupProxy)
        self.proxy.routes = {
            f"{member:03d}.wake.local": {
                "target": "127.0.0.1",
                "subnet": "127.0.0.0/8",
                "gateway": "",
                "host_ip": "0.0.0.0",
                "host_port": str(8080 + member),
            }
            for member in range(1, 4)
        }
        self.proxy.groups = {
            "wake.local": {
                "members": ["001.wake.local", "002.wake.local", "003.wake.local"],
                "subnet": "127.0.0.0/8",
                "gateway": "",
            }
        }
        self.proxy_thread = threading.Thread(target=self.proxy.serve_forever, daemon=True)
        self.proxy_thread.start()

    def tearDown(self):
        self.proxy.shutdown()
        self.proxy.server_close()
        self.proxy_thread.join(timeout=2)
        self.member.shutdown()
        self.member.server_close()
        self.member_thread.join(timeout=2)

    def request(self, host, path="/"):
        request = Request(
            f"http://127.0.0.1:{self.proxy.server_port}{path}",
            headers={"Host": host},
        )
        return urlopen(request, timeout=2)

    def test_group_hostname_serves_proxy_directory(self):
        with self.request("wake.local") as response:
            body = response.read().decode("utf-8")
        self.assertIn("WAKE group wake.local", body)
        for member in ("001", "002", "003"):
            self.assertIn(f"http://{member}.wake.local/", body)

    def test_lan_ip_serves_group_directory_with_direct_member_urls(self):
        with self.request("192.0.2.10") as response:
            body = response.read().decode("utf-8")
        for member in range(1, 4):
            self.assertIn(f"http://192.0.2.10:{8080 + member}/console.html", body)

    def test_numbered_hostname_forwards_to_member(self):
        with patch(
            "scripts.wake_group_proxy.HTTPConnection",
            side_effect=lambda _target, _port, timeout: HTTPConnection(
                "127.0.0.1", self.member.server_port, timeout=timeout
            ),
        ):
            with self.request("001.wake.local") as response:
                self.assertEqual(response.read(), b"member response")

    def test_unknown_hostname_is_rejected(self):
        with self.assertRaises(HTTPError) as error:
            self.request("wake.local-001")
        self.assertEqual(error.exception.code, 404)
        error.exception.close()


if __name__ == "__main__":
    unittest.main()
