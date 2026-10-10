import io
import json
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from scripts.wake_group_proxy import GroupProxy


class _Response:
    status = 200

    def __init__(self, packet):
        self.packet = packet

    def read(self, limit):
        return json.dumps(self.packet).encode()


class _Connection:
    def __init__(self, host, port, timeout):
        if host == "offline":
            raise OSError("offline peer")
        self.host = host

    def request(self, *args, **kwargs):
        pass

    def getresponse(self):
        return _Response({
            "schema": 1, "group_id": "wake.local", "instance_id": "wake.local-002",
            "application_head": "a" * 64,
            "posts": [{"id": "post-002", "created_by": "wake-002"}],
            "invocations": {"wake-002": {"id": "wake-002"}},
            "evidence": {},
        })

    def close(self):
        pass


class GroupProxyTests(unittest.TestCase):
    def test_zero_ordinal_hostname_serves_its_group_directory(self):
        proxy = GroupProxy.__new__(GroupProxy)
        group = {"members": ["001.wake.local", "002.wake.local"],
                 "subnet": "172.24.0.0/16", "gateway": "172.24.0.1"}
        proxy.server = SimpleNamespace(routes={}, groups={"wake.local": group})
        proxy.headers = {"Host": "000.wake.local"}
        proxy.path = "/"
        proxy.client_address = ("127.0.0.1", 12345)
        proxy.command = "GET"
        served = []
        errors = []
        proxy._serve_group_directory = lambda host, value: served.append((host, value))
        proxy.send_error = lambda *args: errors.append(args)
        proxy._forward()
        self.assertEqual(served, [("000.wake.local", group)])
        self.assertEqual(errors, [])

    def test_host_and_lan_clients_are_allowed_but_other_group_members_are_not(self):
        proxy = GroupProxy.__new__(GroupProxy)
        proxy.server = SimpleNamespace(groups={
            "wake.local": {"subnet": "172.24.0.0/16"},
            "other.local": {"subnet": "172.25.0.0/16"},
        })
        route = {"subnet": "172.24.0.0/16", "gateway": "172.24.0.1"}
        for address, expected in (("127.0.0.1", True), ("192.168.65.1", True),
                                  ("192.168.1.42", True), ("172.24.0.8", True),
                                  ("172.25.0.8", False), ("8.8.8.8", False)):
            with self.subTest(address=address):
                proxy.client_address = (address, 12345)
                self.assertEqual(proxy._allowed(route), expected)

    def test_group_bob_skips_unreachable_peer_and_serves_the_reachable_member(self):
        proxy = GroupProxy.__new__(GroupProxy)
        proxy.server = SimpleNamespace(
            groups={"wake.local": {"members": ["001.wake.local", "002.wake.local"]}},
            routes={
                "001.wake.local": {"target": "offline", "group_id": "wake.local"},
                "002.wake.local": {"target": "online", "group_id": "wake.local"},
            },
        )
        proxy.command = "GET"
        proxy.wfile = io.BytesIO()
        statuses = []
        proxy.send_response = lambda status, *args: statuses.append(status)
        proxy.send_header = lambda *args: None
        proxy.end_headers = lambda: None
        with patch("scripts.wake_group_proxy.HTTPConnection", _Connection):
            proxy._serve_group_bob("wake.local")
        self.assertEqual(statuses, [200])
        body = json.loads(proxy.wfile.getvalue())
        self.assertEqual(body["members"], ["wake.local-002"])
        self.assertEqual([post["id"] for post in body["posts"]], ["post-002"])


if __name__ == "__main__":
    unittest.main()
