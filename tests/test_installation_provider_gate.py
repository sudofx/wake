"""Mandatory provider slots never fail open or stall an eligible fallback."""
import os
import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from unittest.mock import patch
from urllib.error import HTTPError

from wake.group_coordinator import GroupProviderGate, group_provider_gate
from wake.installation_gate import InstallationCallCoordinator, InstallationSlotUnavailable
from wake.providers import ProviderCallPaused


class InstallationProviderGateTests(unittest.TestCase):
    def setUp(self):
        # Unit fixtures control recovery explicitly; do not leave retry threads
        # making real HTTP requests after a mocked transport has been restored.
        retry = patch('wake.group_coordinator._releases.add')
        self.defer_release = retry.start()
        self.addCleanup(retry.stop)

    def test_unconfirmed_grant_lost_on_every_reply_can_be_cancelled(self):
        coordinator = InstallationCallCoordinator()
        gate = GroupProviderGate('http://controller', '100.wake')
        tokens, packets = [], []
        def reply(packet):
            packets.append(packet)
            key = ('wake', packet['member'], packet['request_id'])
            if packet['action'] == 'cancel':
                coordinator.cancel_request(key)
                return {'status': 'cancelled'}
            result = coordinator.acquire(key, packet['model'], confirmation_required=True)
            tokens.append((key, result['token']))
            raise OSError('Every reservation response lost')
        with patch.dict(os.environ, {'WAKE_INSTALLATION_WORKER': '1'}), \
             patch.object(gate, '_request', side_effect=reply), patch('wake.group_coordinator.time.sleep'):
            with self.assertRaises(ProviderCallPaused):
                with gate.request('gemini'):
                    self.fail('Unconfirmed reservation authorized an effect')
        self.assertEqual([p['action'] for p in packets], ['acquire'] * 3 + ['cancel'])
        self.assertIsNone(coordinator.status()['active'])
        self.assertFalse(coordinator.confirm(*tokens[0]))
        self.assertEqual(coordinator.acquire(('wake', '101.wake', 'next'), 'gemini')['status'], 'granted')

    def test_only_unconfirmed_reservations_expire_and_stale_confirmation_fails(self):
        now = [0.0]
        coordinator = InstallationCallCoordinator(clock=lambda: now[0])
        first = ('wake', '100.wake', 'first')
        grant = coordinator.acquire(first, 'gemini', confirmation_required=True)
        now[0] = 31
        second = ('wake', '101.wake', 'second')
        replacement = coordinator.acquire(second, 'gemini', confirmation_required=True)
        self.assertEqual(replacement['status'], 'granted')
        self.assertFalse(coordinator.confirm(first, grant['token']))
        self.assertTrue(coordinator.confirm(second, replacement['token']))
        now[0] = 1_000_000
        self.assertFalse(coordinator.cancel_request(second))
        self.assertEqual(coordinator.acquire(('wake', '102.wake', 'third'), 'gemini')['status'], 'queued')
        self.assertTrue(coordinator.status()['active']['confirmed'])

    def test_confirmation_retries_and_pending_release_never_repeat_provider_effect(self):
        from wake.group_coordinator import _ReleaseRetrier
        coordinator = InstallationCallCoordinator()
        gate = GroupProviderGate('http://controller', '100.wake')
        effects, packets = [], []
        lost_confirm, offline_release = [True], [True]
        def reply(packet):
            packets.append(dict(packet))
            key = ('wake', packet['member'], packet['request_id'])
            if packet['action'] == 'acquire':
                return coordinator.acquire(key, packet['model'], confirmation_required=True)
            if packet['action'] == 'confirm':
                result = {'status': 'confirmed' if coordinator.confirm(key, packet['token']) else 'expired'}
                if lost_confirm[0]:
                    lost_confirm[0] = False
                    raise OSError('First confirmation response lost')
                return result
            if offline_release[0]:
                raise OSError('Release temporarily unreachable')
            return {'status': 'released' if coordinator.release(key, packet['token'], packet.get('outcome')) else 'expired'}
        with patch.object(gate, '_request', side_effect=reply), patch('wake.group_coordinator.time.sleep'), \
             patch('wake.group_coordinator.sys.stderr'):
            with gate.request('gemini'):
                self.assertTrue(coordinator.status()['active']['confirmed'])
                effects.append('one effect')
                gate.outcome = {'result': 'rate_limited', 'http_status': 429, 'retry_after_seconds': 60}
            self.assertIsNotNone(coordinator.status()['active'])
            self.defer_release.assert_called_once()
            retrier = _ReleaseRetrier()
            with patch('wake.group_coordinator.threading.Thread'):
                retrier.add(*self.defer_release.call_args.args)
            retrier.retry()
            self.assertTrue(retrier.pending)
            offline_release[0] = False
            retrier.retry()
            self.assertFalse(retrier.pending)
        self.assertEqual(effects, ['one effect'])
        self.assertEqual([p['action'] for p in packets].count('confirm'), 2)
        self.assertIsNone(coordinator.status()['active'])
        self.assertEqual(coordinator.acquire(('wake', '101.wake', 'next'), 'gemini')['reason'], 'rate_limited')

    def test_lost_confirmation_exhaustion_releases_known_token_without_effect(self):
        coordinator = InstallationCallCoordinator()
        gate = GroupProviderGate('http://controller', '100.wake')
        def reply(packet):
            key = ('wake', packet['member'], packet['request_id'])
            if packet['action'] == 'acquire':
                return coordinator.acquire(key, packet['model'], confirmation_required=True)
            if packet['action'] == 'confirm':
                coordinator.confirm(key, packet['token'])
                raise OSError('Confirmation reply lost')
            if packet['action'] == 'release':
                return {'status': 'released' if coordinator.release(key, packet['token']) else 'expired'}
            return {'status': 'cancelled', 'removed': coordinator.cancel_request(key)}
        with patch.dict(os.environ, {'WAKE_INSTALLATION_WORKER': '1'}), \
             patch.object(gate, '_request', side_effect=reply), patch('wake.group_coordinator.time.sleep'):
            with self.assertRaises(ProviderCallPaused):
                with gate.request('gemini'):
                    self.fail('Unknown confirmation authorized an effect')
        self.assertIsNone(coordinator.status()['active'])
        self.defer_release.assert_not_called()

    def test_real_installation_endpoint_confirms_before_effect_and_persists_release(self):
        from http.server import ThreadingHTTPServer
        from types import SimpleNamespace
        from wake.installation import InstallationHTTP
        coordinator = InstallationCallCoordinator()
        persisted = []
        controller = SimpleNamespace(token='fixture-token', mode='running', editorial_nonce=None,
            coordinator=coordinator, slot_condition=threading.Condition(),
            persist_schedule=lambda packet=None: persisted.append(packet))
        server = ThreadingHTTPServer(('127.0.0.1', 0), InstallationHTTP)
        server.controller = controller
        thread = threading.Thread(target=server.serve_forever, kwargs={'poll_interval': .01}, daemon=True)
        thread.start()
        gate = GroupProviderGate(f'http://127.0.0.1:{server.server_port}/group/coordinator', '100.wake')
        try:
            with patch.dict(os.environ, {'WAKE_INSTALLATION_TOKEN': 'fixture-token', 'WAKE_INSTALLATION_WORKER': '1'}):
                with gate.request('fixture'):
                    self.assertTrue(coordinator.status()['active']['confirmed'])
                    self.assertEqual(len(persisted), 1)
                    gate.outcome = {'result': 'rate_limited', 'http_status': 429}
            self.assertIsNone(coordinator.status()['active'])
            self.assertTrue(persisted[-1]['models']['fixture']['retry_at'])
            controller.mode = 'stopped'
            controller.editorial_nonce = 'operator-editorial'
            gate.editorial_nonce = 'operator-editorial'
            with patch.dict(os.environ, {'WAKE_INSTALLATION_TOKEN': 'fixture-token', 'WAKE_INSTALLATION_WORKER': '1'}):
                with gate.request('editorial-fixture'):
                    self.assertTrue(coordinator.status()['active']['confirmed'])
                gate.editorial_nonce = 'wrong-command'
                with self.assertRaises(ProviderCallPaused):
                    with gate.request('editorial-fixture'):
                        self.fail('Wrong editorial command authorized a provider effect')
            self.assertIsNone(coordinator.status()['active'])
        finally:
            server.shutdown()
            thread.join(timeout=1)
            server.server_close()

    def test_research_requires_running_mode(self):
        from wake.installation import provider_admitted
        for mode in ('paused', 'stopped'):
            self.assertFalse(provider_admitted(mode, '100.wake', {}))
            self.assertFalse(provider_admitted(mode, '101.wake', {}))
        self.assertTrue(provider_admitted('running', '101.wake', {}))

    def test_shared_limit_returns_immediately_and_cancels_queue(self):
        for reason in ("daily_quota", "rate_limited", "access_blocked"):
            gate = GroupProviderGate("http://controller", "100.wake")
            packets = []
            def reply(packet):
                packets.append(packet)
                return {"status": "queued", "reason": reason, "retry_after": 300}
            with patch.dict(os.environ, {"WAKE_INSTALLATION_WORKER": "1"}), patch.object(gate, "_request", side_effect=reply), patch("wake.group_coordinator.time.sleep") as sleep:
                with self.assertRaises(InstallationSlotUnavailable) as raised:
                    with gate.request("gemini"):
                        self.fail("Unavailable model obtained a provider slot")
                self.assertEqual(raised.exception.outcome["provider_call_made"], False)
                self.assertEqual(raised.exception.retry_after_seconds, 300)
                self.assertEqual([packet["action"] for packet in packets], ["acquire", "cancel"])
                sleep.assert_not_called()

    def test_busy_longpoll_response_does_not_add_a_second_of_delay(self):
        gate = GroupProviderGate("http://controller", "100.wake")
        replies = [{"status": "queued", "reason": "busy", "retry_after": 1},
                   {"status": "granted", "token": "slot"}]
        with patch.dict(os.environ, {"WAKE_INSTALLATION_WORKER": "1"}), patch.object(gate, "_request", side_effect=replies), patch("wake.group_coordinator.time.sleep") as sleep:
            self.assertEqual(gate._acquire("a" * 32, "gemini"), "slot")
            sleep.assert_called_once_with(.05)

    def test_controller_failure_and_missing_url_never_send_provider_call(self):
        with patch.dict(os.environ, {"WAKE_INSTALLATION_WORKER": "1"}):
            for url in ("http://controller", ""):
                gate = GroupProviderGate(url, "100.wake")
                with patch.object(gate, "_request", side_effect=OSError("offline")):
                    with self.assertRaises(ProviderCallPaused):
                        with gate.request("gemini"):
                            self.fail("Controller bypassed")

    def test_installation_factory_without_controller_still_fails_closed(self):
        with patch.dict(os.environ, {"WAKE_INSTALLATION_WORKER": "1",
                                    "WAKE_GROUP_COORDINATOR_URL": "",
                                    "WAKE_PUBLIC_HOSTNAME": ""}):
            gate = group_provider_gate({})
            self.assertIsNotNone(gate)
            with self.assertRaises(ProviderCallPaused):
                with gate.request("gemini"):
                    self.fail("Missing installation configuration bypassed controller")

    def test_release_sends_only_current_request_outcome(self):
        gate = GroupProviderGate("http://controller", "100.wake")
        releases = []
        def reply(packet):
            if packet["action"] == "acquire":
                return {"status": "granted", "token": "slot"}
            releases.append(packet)
            return {"status": "released"}
        with patch.object(gate, "_request", side_effect=reply):
            with gate.request("first"):
                gate.outcome = {"result": "success"}
            with gate.request("second"):
                pass
        self.assertEqual(releases[0]["outcome"], {"result": "success"})
        self.assertEqual(releases[1]["outcome"], {})

    def test_restore_retains_limits_but_never_restores_grant(self):
        clock = lambda: 1791932400.0
        coordinator = InstallationCallCoordinator(clock=clock)
        key = ("wake", "100.wake", "request")
        grant = coordinator.acquire(key, "daily", 1)
        coordinator.release(key, grant["token"], {"result": "daily_quota"})
        grant = coordinator.acquire(key, "access", 1)
        coordinator.release(key, grant["token"], {"http_status": 403})
        coordinator.acquire(key, "active", 1)
        saved = coordinator.dump_state()
        self.assertNotIn("token", str(saved))
        restored = InstallationCallCoordinator(clock=clock)
        restored.restore_state(saved)
        self.assertIsNone(restored.status()["active"])
        self.assertEqual(restored.acquire(key, "daily", 1)["reason"], "daily_quota")
        self.assertTrue(restored.cancel_request(key))
        self.assertEqual(restored.acquire(key, "access", 1)["reason"], "access_blocked")

    def test_cancel_queued_request_cannot_cancel_active_holder(self):
        coordinator = InstallationCallCoordinator()
        key = ("wake", "100.wake", "request")
        coordinator.acquire(key, "gemini", 1)
        self.assertFalse(coordinator.cancel_request(key))
        self.assertIsNotNone(coordinator.status()["active"])

    def test_restore_refuses_live_queue_and_invalid_deadlines(self):
        coordinator = InstallationCallCoordinator()
        for value in (float("nan"), float("inf"), -1, "later"):
            with self.assertRaises(ValueError):
                coordinator.restore_state({"version": 1, "models": {"gemini": {"probe_at": value}}})
        coordinator.acquire(("wake", "100.wake", "request"), "gemini", 1)
        with self.assertRaises(RuntimeError):
            coordinator.restore_state({"version": 1, "models": {}})

    def test_lost_grant_and_release_responses_reuse_identity_without_overlap(self):
        coordinator = InstallationCallCoordinator()
        gate = GroupProviderGate('http://controller', '100.wake')
        packets, effects = [], []
        lost = {'acquire', 'release'}
        def reply(packet):
            packets.append(dict(packet))
            key = ('wake', packet['member'], packet['request_id'])
            if packet['action'] == 'acquire':
                result = coordinator.acquire(key, packet['model'])
            else:
                released = coordinator.release(key, packet['token'], packet.get('outcome'))
                result = {'status': 'released' if released else 'expired'}
            if packet['action'] in lost:
                lost.remove(packet['action'])
                raise OSError('Response lost after controller applied request')
            return result
        with patch.dict(os.environ, {'WAKE_INSTALLATION_WORKER': '1'}), \
             patch.object(gate, '_request', side_effect=reply), \
             patch('wake.group_coordinator.time.sleep'):
            with gate.request('gemini'):
                effects.append('provider effect')
                self.assertEqual(coordinator.acquire(('wake', '101.wake', 'other'), 'gemini')['status'], 'queued')
                gate.outcome = {'result': 'success'}
        self.assertEqual(effects, ['provider effect'])
        self.assertEqual([packet['action'] for packet in packets], ['acquire', 'acquire', 'release', 'release'])
        self.assertEqual(packets[0], packets[1])
        self.assertEqual(packets[2], packets[3])
        self.assertIsNone(coordinator.status()['active'])
        self.assertEqual(coordinator.acquire(('wake', '101.wake', 'other'), 'gemini')['status'], 'granted')

    def test_ambiguous_acquire_exhaustion_retains_grant_and_never_calls_provider(self):
        coordinator = InstallationCallCoordinator()
        gate = GroupProviderGate('http://controller', '100.wake')
        packets = []
        def reply(packet):
            packets.append(dict(packet))
            key = ('wake', packet['member'], packet['request_id'])
            if packet['action'] == 'cancel':
                return {'status': 'cancelled', 'removed': coordinator.cancel_request(key)}
            coordinator.acquire(key, packet['model'])
            raise OSError('Controller response unavailable')
        with patch.dict(os.environ, {'WAKE_INSTALLATION_WORKER': '1'}), \
             patch.object(gate, '_request', side_effect=reply), \
             patch('wake.group_coordinator.time.sleep'):
            with self.assertRaises(ProviderCallPaused):
                with gate.request('gemini'):
                    self.fail('Ambiguous grant permitted provider effect')
        self.assertEqual([packet['action'] for packet in packets], ['acquire'] * 3 + ['cancel'])
        self.assertEqual(packets[0], packets[1])
        self.assertEqual(packets[1], packets[2])
        self.assertIsNotNone(coordinator.status()['active'])
        self.assertEqual(coordinator.acquire(('wake', '101.wake', 'next'), 'gemini')['status'], 'queued')

    def test_release_exhaustion_retains_grant_without_repeating_provider_effect(self):
        coordinator = InstallationCallCoordinator()
        gate = GroupProviderGate('http://controller', '100.wake')
        packets, effects = [], []
        def reply(packet):
            packets.append(dict(packet))
            if packet['action'] == 'release':
                raise OSError('Release never reached controller')
            return coordinator.acquire(('wake', packet['member'], packet['request_id']), packet['model'])
        with patch.dict(os.environ, {'WAKE_INSTALLATION_WORKER': '1'}), \
             patch.object(gate, '_request', side_effect=reply), \
             patch('wake.group_coordinator.time.sleep'), \
             patch('wake.group_coordinator.sys.stderr'):
            with gate.request('gemini'):
                effects.append('provider effect')
        self.assertEqual(effects, ['provider effect'])
        self.assertEqual([packet['action'] for packet in packets], ['acquire'] + ['release'] * 3)
        self.assertEqual(packets[1], packets[2])
        self.assertEqual(packets[2], packets[3])
        self.assertIsNotNone(coordinator.status()['active'])

    def test_controller_http_rejection_is_not_retried(self):
        gate = GroupProviderGate('http://controller', '100.wake')
        error = HTTPError('http://controller', 409, 'Stopped', {}, None)
        self.addCleanup(error.close)
        with patch.object(gate, '_request', side_effect=error) as request, \
             patch('wake.group_coordinator.time.sleep') as sleep:
            with self.assertRaises(HTTPError):
                gate._request_reliably({'action': 'acquire'})
        request.assert_called_once()
        sleep.assert_not_called()

    def test_semantically_invalid_controller_packet_is_not_retried(self):
        gate = GroupProviderGate('http://controller', '100.wake')
        packets = []
        def reply(packet):
            packets.append(packet)
            return {'status': 'unknown'}
        with patch.dict(os.environ, {'WAKE_INSTALLATION_WORKER': '1'}), \
             patch.object(gate, '_request', side_effect=reply), \
             patch('wake.group_coordinator.time.sleep') as sleep:
            with self.assertRaises(ProviderCallPaused):
                with gate.request('gemini'):
                    self.fail('Invalid controller packet allowed provider effect')
        self.assertEqual([packet['action'] for packet in packets], ['acquire', 'cancel'])
        sleep.assert_not_called()

    def test_pause_after_ambiguous_acquire_releases_recovered_grant(self):
        coordinator = InstallationCallCoordinator()
        gate = GroupProviderGate('http://controller', '100.wake', should_pause=lambda: paused[0])
        paused, packets = [False], []
        def reply(packet):
            packets.append(dict(packet))
            key = ('wake', packet['member'], packet['request_id'])
            if packet['action'] == 'release':
                return {'status': 'released' if coordinator.release(key, packet['token']) else 'expired'}
            result = coordinator.acquire(key, packet['model'])
            if len(packets) == 1:
                paused[0] = True
                raise OSError('Pause arrives while grant response is lost')
            return result
        with patch.dict(os.environ, {'WAKE_INSTALLATION_WORKER': '1'}), \
             patch.object(gate, '_request', side_effect=reply), \
             patch('wake.group_coordinator.time.sleep'):
            with self.assertRaises(ProviderCallPaused):
                with gate.request('gemini'):
                    self.fail('Operator pause ignored')
        self.assertEqual([packet['action'] for packet in packets], ['acquire', 'acquire', 'release'])
        self.assertIsNone(coordinator.status()['active'])

    def test_truncated_controller_responses_recover_or_exhaust_with_same_identity(self):
        for failure in ('json', 'unicode', 'chunked'):
            for exhausted in (False, True):
                for phase in ('acquire', 'release'):
                    with self.subTest(failure=failure, exhausted=exhausted, phase=phase):
                        self.check_truncated_controller_response(failure, exhausted, phase)

    def check_truncated_controller_response(self, failure, exhausted, phase):
        coordinator = InstallationCallCoordinator()
        packets, effects = [], []

        class ControllerResponse(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_POST(self):
                packet = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
                packets.append(packet)
                key = ('wake', packet['member'], packet['request_id'])
                failed = packet['action'] == phase and (exhausted or sum(p['action'] == phase for p in packets) == 1)
                if packet['action'] == 'acquire':
                    result = coordinator.acquire(key, packet['model'])
                elif packet['action'] == 'release':
                    # Exhausted release delivery leaves the grant held; an
                    # applied release with a lost reply is safe to repeat.
                    released = False if exhausted and failed else coordinator.release(key, packet['token'])
                    result = {'status': 'released' if released else 'expired'}
                else:
                    result = {'status': 'cancelled', 'removed': coordinator.cancel_request(key)}
                self.send_response(200)
                if failed and failure == 'chunked':
                    self.send_header('Transfer-Encoding', 'chunked')
                    self.end_headers()
                    self.wfile.write(b'10\r\n{')
                else:
                    body = (b'{' if failure == 'json' else b'\xff') if failed else json.dumps(result).encode()
                    self.send_header('Content-Length', str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
                self.close_connection = True

        server = HTTPServer(('127.0.0.1', 0), ControllerResponse)
        worker = threading.Thread(target=server.serve_forever, kwargs={'poll_interval': .01}, daemon=True)
        worker.start()
        gate = GroupProviderGate(f'http://127.0.0.1:{server.server_port}', '100.wake')
        try:
            with patch.dict(os.environ, {'WAKE_INSTALLATION_WORKER': '1'}), \
                 patch('wake.group_coordinator.time.sleep'), \
                 patch('wake.group_coordinator.sys.stderr'):
                if exhausted and phase == 'acquire':
                    with self.assertRaises(ProviderCallPaused):
                        with gate.request('gemini'):
                            self.fail('Truncated grant allowed provider effect')
                else:
                    with gate.request('gemini'):
                        effects.append('provider effect')
                        self.assertEqual(coordinator.acquire(('wake', '101.wake', 'other'), 'gemini')['status'], 'queued')
        finally:
            server.shutdown()
            worker.join(timeout=1)
            server.server_close()
        acquires = [packet for packet in packets if packet['action'] == 'acquire']
        self.assertEqual(len(acquires), (3 if exhausted else 2) if phase == 'acquire' else 1)
        self.assertTrue(all(packet == acquires[0] for packet in acquires))
        retries = [packet for packet in packets if packet['action'] == phase]
        self.assertTrue(all(packet == retries[0] for packet in retries))
        self.assertEqual(effects, [] if exhausted and phase == 'acquire' else ['provider effect'])
        expected = (['acquire'] * 3 + ['cancel'] if exhausted else ['acquire', 'acquire', 'release']) if phase == 'acquire' else ['acquire'] + ['release'] * (3 if exhausted else 2)
        self.assertEqual([packet['action'] for packet in packets], expected)
        self.assertEqual(coordinator.status()['active'] is not None, exhausted)


if __name__ == "__main__":
    unittest.main()
