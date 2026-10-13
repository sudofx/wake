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
            "schema": 1, "group_id": "wake", "instance_id": "wake-002",
            "application_head": "a" * 64,
            "posts": [{"id": "post-002", "created_by": "wake-002"}],
            "invocations": {"wake-002": {"id": "wake-002"}},
            "evidence": {},
        })

    def close(self):
        pass


class GroupProxyTests(unittest.TestCase):
    def test_member_card_opens_console_on_the_correct_hostname_or_lan_port(self):
        proxy = GroupProxy.__new__(GroupProxy)
        proxy.server = SimpleNamespace(routes={"101.wake": {}})
        with patch.object(proxy, "_member_runtime", return_value=("paused", "Paused")):
            for origin in ("http://101.wake", "http://192.168.1.74:54321"):
                card = proxy._member_button("101.wake", origin + "/console.html")
                self.assertIn('href="' + origin + '/console.html"', card)
                self.assertEqual(card.count('<a '), 1)
                self.assertTrue(card.startswith('<a '))
                self.assertNotIn("<svg", card)

    def test_gateway_directory_explains_each_status_light_color(self):
        proxy = GroupProxy.__new__(GroupProxy)
        proxy.command = "GET"
        proxy.wfile = io.BytesIO()
        proxy.send_response = lambda *args: None
        proxy.send_header = lambda *args: None
        proxy.end_headers = lambda: None

        proxy._serve_directory("wake", [])
        html = proxy.wfile.getvalue().decode()

        for color, state, meaning in (
            ("Red", "blocked", "Operator or agent action required"),
            ("Yellow", "waiting", "Waiting, paused, or stopped"),
            ("Green", "running", "Research running"),
            ("Blue", "idle", "Research idle"),
            ("Purple", "standby", "Provider quota reported; retrying on schedule"),
        ):
            with self.subTest(color=color):
                self.assertIn(f'data-state="{state}"', html)
                self.assertIn(f"{color} · {meaning}", html)
        colors = [html.index(f'{color} ·') for color in ("Red", "Yellow", "Green", "Blue", "Purple")]
        self.assertEqual(colors, sorted(colors))

    def test_missing_member_status_is_yellow_and_rechecked_not_red(self):
        proxy = GroupProxy.__new__(GroupProxy)
        proxy.server = SimpleNamespace(routes={"101.wake": {"target": "offline"}})
        with patch("scripts.wake_group_proxy.HTTPConnection", side_effect=OSError("offline")):
            state, label = proxy._member_runtime("101.wake")
        self.assertEqual(state, "waiting")
        self.assertIn("checking again automatically", label)

    def test_blocked_without_operator_action_is_yellow(self):
        class RuntimeResponse:
            status = 200
            def read(self, limit):
                return json.dumps({"mode": "standalone", "state": "blocked",
                                   "reason": "unknown temporary condition"}).encode()

        class RuntimeConnection:
            def __init__(self, *args, **kwargs): pass
            def request(self, *args, **kwargs): pass
            def getresponse(self): return RuntimeResponse()
            def close(self): pass

        proxy = GroupProxy.__new__(GroupProxy)
        proxy.server = SimpleNamespace(routes={"101.wake": {"target": "online"}})
        with patch("scripts.wake_group_proxy.HTTPConnection", RuntimeConnection):
            state, label = proxy._member_runtime("101.wake")
        self.assertEqual(state, "waiting")
        self.assertIn("no operator action", label)

    def test_blocked_light_explains_the_required_operator_action(self):
        class RuntimeResponse:
            status = 200

            def read(self, limit):
                return json.dumps({
                    "mode": "standalone", "state": "blocked",
                    "reason": "Invalid provider configuration",
                    "action": "Check the API key and restart",
                }).encode()

        class RuntimeConnection:
            def __init__(self, *args, **kwargs):
                pass

            def request(self, *args, **kwargs):
                pass

            def getresponse(self):
                return RuntimeResponse()

            def close(self):
                pass

        proxy = GroupProxy.__new__(GroupProxy)
        proxy.server = SimpleNamespace(routes={"101.wake": {"target": "101.wake"}})
        with patch("scripts.wake_group_proxy.HTTPConnection", RuntimeConnection):
            state, label = proxy._member_runtime("101.wake")
        self.assertEqual(state, "blocked")
        self.assertIn("Operator or agent action required", label)
        self.assertIn("Invalid provider configuration", label)
        self.assertIn("Check the API key and restart", label)

    def test_zero_ordinal_hostname_serves_its_group_directory(self):
        proxy = GroupProxy.__new__(GroupProxy)
        group = {"members": ["101.wake", "102.wake"],
                 "subnet": "172.24.0.0/16", "gateway": "172.24.0.1"}
        proxy.server = SimpleNamespace(routes={}, groups={"wake": group})
        proxy.headers = {"Host": "000.wake"}
        proxy.path = "/"
        proxy.client_address = ("127.0.0.1", 12345)
        proxy.command = "GET"
        served = []
        errors = []
        proxy._serve_group_directory = lambda host, value: served.append((host, value))
        proxy.send_error = lambda *args: errors.append(args)
        proxy._forward()
        self.assertEqual(served, [("000.wake", group)])
        self.assertEqual(errors, [])

    def test_group_directory_displays_parent_and_child_ordinals(self):
        proxy = GroupProxy.__new__(GroupProxy)
        parent = "100.wake"
        child = "101.wake"
        proxy.server = SimpleNamespace(routes={
            parent: {"role": "parent"},
            child: {"role": "child"},
        })
        proxy._member_runtime = lambda member: ("idle", "Research idle")

        html = proxy._group_panel(
            "wake",
            {"parents": [parent], "children": {parent: [child]}},
            lambda member: f"http://{member}/",
            "Open a member on this local network in a new tab.",
        )

        self.assertIn("<span>100</span>", html)
        self.assertIn("<span>101</span>", html)
        self.assertIn('aria-label="Parent node 100.wake"', html)

    def test_host_and_lan_clients_are_allowed_but_other_group_members_are_not(self):
        proxy = GroupProxy.__new__(GroupProxy)
        proxy.server = SimpleNamespace(groups={
            "wake": {"subnet": "172.24.0.0/16"},
            "other": {"subnet": "172.25.0.0/16"},
        })
        route = {"subnet": "172.24.0.0/16", "gateway": "172.24.0.1"}
        for address, expected in (("127.0.0.1", True), ("192.168.65.1", True),
                                  ("192.168.1.42", True), ("172.24.0.8", True),
                                  ("172.25.0.8", False), ("8.8.8.8", False)):
            with self.subTest(address=address):
                proxy.client_address = (address, 12345)
                self.assertEqual(proxy._allowed(route), expected)

    def test_group_directory_allows_localhost_without_a_group_subnet_field(self):
        proxy = GroupProxy.__new__(GroupProxy)
        proxy.server = SimpleNamespace(groups={"wake": {"networks": ["wake-group-wake"]}})
        proxy.client_address = ("127.0.0.1", 12345)
        self.assertTrue(proxy._allowed(proxy.server.groups["wake"]))

    def test_group_directory_accepts_each_member_network_but_rejects_other_group(self):
        proxy=GroupProxy.__new__(GroupProxy)
        group={'members':['100.wake','101.wake','201.wake','301.wake']}
        proxy.server=SimpleNamespace(groups={'wake':group},routes={
            name:{'subnet':f'172.{ordinal}.0.0/16'}
            for name,ordinal in [('100.wake',20),('101.wake',21),('201.wake',22),('301.wake',23),('100.other',24)]})
        for ordinal in range(20,25):
            proxy.client_address=(f'172.{ordinal}.0.8',12345)
            self.assertEqual(proxy._allowed(group),ordinal<24)
        proxy.client_address=('172.21.0.8',12345)
        self.assertFalse(proxy._allowed(proxy.server.routes['100.other']))

    def test_parent_coordinator_accepts_own_cell_interface_only(self):
        proxy=GroupProxy.__new__(GroupProxy)
        parent={'subnet':'172.20.0.0/16','role':'parent','group_id':'wake'}
        proxy.server=SimpleNamespace(routes={'100.wake':parent,
            '101.wake':{'subnet':'172.21.0.0/16','parent':'100.wake','group_id':'wake'},
            '201.wake':{'subnet':'172.22.0.0/16','parent':'200.wake','group_id':'wake'},
            '101.other':{'subnet':'172.24.0.0/16','parent':'100.wake','group_id':'other'}})
        for ordinal in (20,21,22,24):
            proxy.client_address=(f'172.{ordinal}.0.8',12345)
            self.assertEqual(proxy._coordinator_allowed('100.wake',parent),ordinal in (20,21))

    def test_member_count_is_attributed_accepted_progress_not_attempts(self):
        proxy = GroupProxy.__new__(GroupProxy)
        proxy.server = SimpleNamespace(routes={'201.wake': {'target': '201.wake', 'group_id': 'wake'}})
        packet = {'schema': 1, 'group_id': 'wake', 'member': '201.wake',
                  'head': 'a' * 64, 'version': 21, 'attempts': [1, 2, 3]}
        connection = _Connection('201.wake', 8080, 0.7)
        connection.getresponse = lambda: _Response(packet)
        with patch('scripts.wake_group_proxy.HTTPConnection', return_value=connection):
            self.assertEqual(proxy._member_count('201.wake'), 21)
            for field, invalid in [('version', True), ('version', -1), ('member', '202.wake')]:
                changed = {**packet, field: invalid}
                connection.getresponse = lambda: _Response(changed)
                self.assertIsNone(proxy._member_count('201.wake'))
        proxy._member_status = lambda member: {'state': 'running', 'label': 'Research running', 'accepted_wakes': 21}
        html = proxy._member_button('201.wake', 'http://201.wake/console.html')
        self.assertLess(html.index('<span>201</span>'), html.index(' | 21</span>'))
        self.assertLess(html.index(' | 21</span>'), html.index('member-status-light'))

    def test_gateway_status_endpoint_returns_each_members_current_state(self):
        proxy = GroupProxy.__new__(GroupProxy)
        proxy.server = SimpleNamespace(
            groups={"wake": {"members": ["101.wake", "102.wake"]}},
            routes={},
        )
        proxy.headers = {"Host": "000.wake"}
        proxy.path = "/group/status.json"
        proxy.client_address = ("127.0.0.1", 12345)
        proxy.command = "GET"
        proxy.wfile = io.BytesIO()
        proxy.send_response = lambda *args: None
        proxy.send_header = lambda *args: None
        proxy.end_headers = lambda: None
        proxy._member_runtime = lambda member: (
            ("standby", "Research paused until midnight Pacific time")
            if member == "101.wake" else ("blocked", "Research blocked")
        )

        proxy._forward()

        payload = json.loads(proxy.wfile.getvalue())
        self.assertEqual(payload["states"]["101.wake"]["state"], "standby")
        self.assertEqual(payload["states"]["102.wake"]["state"], "blocked")

    def test_group_bob_skips_unreachable_peer_and_serves_the_reachable_member(self):
        proxy = GroupProxy.__new__(GroupProxy)
        proxy.server = SimpleNamespace(
            groups={"wake": {"members": ["101.wake", "102.wake"]}},
            routes={
                "101.wake": {"target": "offline", "group_id": "wake"},
                "102.wake": {"target": "online", "group_id": "wake", "instance": "wake-002"},
            },
        )
        proxy.command = "GET"
        proxy.wfile = io.BytesIO()
        statuses = []
        proxy.send_response = lambda status, *args: statuses.append(status)
        proxy.send_header = lambda *args: None
        proxy.end_headers = lambda: None
        with patch("scripts.wake_group_proxy.HTTPConnection", _Connection):
            proxy._serve_group_bob("wake")
        self.assertEqual(statuses, [200])
        body = json.loads(proxy.wfile.getvalue())
        self.assertEqual(body["members"], ["wake-002"])
        self.assertEqual([post["id"] for post in body["posts"]], ["post-002"])

    def test_editorial_manifest_requires_parent_and_child(self):
        proxy = GroupProxy.__new__(GroupProxy)
        group = {'members':['100.wake','101.wake']}
        proxy.server = SimpleNamespace(groups={'wake':group}, routes={
            '100.wake':{'target':'100.wake','group_id':'wake','role':'parent'},
            '101.wake':{'target':'101.wake','group_id':'wake','role':'child'}})
        proxy.command='GET'; proxy.path='/group/bob-inputs.json'; proxy.wfile=io.BytesIO()
        statuses=[]; proxy.send_response=lambda status,*args:statuses.append(status)
        proxy.send_header=lambda *args:None; proxy.end_headers=lambda:None
        class Connection:
            def __init__(self,host,*args,**kwargs): self.host=host
            def request(self,*args,**kwargs): pass
            def getresponse(self): return _Response({'schema':1,'group_id':'wake','member':self.host})
            def close(self): pass
        with patch('scripts.wake_group_proxy.HTTPConnection',Connection): proxy._serve_group_editorial(group)
        packet=json.loads(proxy.wfile.getvalue())
        self.assertEqual(statuses,[200]); self.assertEqual(packet['leader'],'100.wake')
        self.assertEqual([i['member'] for i in packet['inputs']],['100.wake','101.wake'])
        proxy.wfile=io.BytesIO(); statuses.clear()
        class MissingChild(Connection):
            def __init__(self,host,*args,**kwargs):
                if host=='101.wake': raise OSError('offline child')
                super().__init__(host)
        with patch('scripts.wake_group_proxy.HTTPConnection',MissingChild): proxy._serve_group_editorial(group)
        self.assertEqual(statuses,[503])
        self.assertNotIn('inputs',json.loads(proxy.wfile.getvalue()))


if __name__ == "__main__":
    unittest.main()
