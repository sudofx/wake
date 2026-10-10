import hashlib
import json
import unittest
from unittest.mock import patch

from wake.group_peers import (
    _validated_peer, collect_group_peer_research, group_bob_snapshot,
    import_group_peer_evidence,
)


class _Store:
    def __init__(self):
        self.state = {"charter": {"id": "charter"}, "evidence": {}}
        self.appended = []

    def load(self):
        return self.state

    def append(self, event_type, payload):
        self.appended.append((event_type, payload))
        self.state["evidence"][payload["id"]] = payload


class _Engine:
    def __init__(self):
        self.store = _Store()


class _BobStore:
    def replay(self):
        state = {
            "version": 5,
            "posts": {
                "post-a": {"id": "post-a", "created_by": "wake-a", "status": "published",
                           "created_version": 4, "evidence": ["evidence-a"]},
                "draft": {"id": "draft", "created_by": "wake-b", "status": "draft",
                          "created_version": 5, "evidence": []},
            },
            "invocations": {"wake-a": {"id": "wake-a", "time": "2026-10-10T12:00:00Z"}},
            "evidence": {"evidence-a": {"id": "evidence-a", "source": "https://example.edu"}},
        }
        return state, "a" * 64


class _PeerResponse:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def read(self, _limit):
        return json.dumps({
            "schema": 2, "group_id": "wake.local", "instance_id": "wake.local-002",
            "application_head": "a" * 64, "version": 3, "evidence": [],
            "notes": [{"id": "note", "revision": 1, "title": "Finding"}],
        }).encode()


class _PeerOpener:
    def open(self, request, timeout):
        if "wake.local-001" in request.full_url:
            raise OSError("peer offline")
        return _PeerResponse()


class GroupPeerTests(unittest.TestCase):
    def setUp(self):
        self.url = "https://example.edu/paper"
        self.content = json.dumps({"url": self.url, "text": "A readable source observation."})
        self.content_hash = hashlib.sha256(self.content.encode("utf-8")).hexdigest()
        self.peer = {
            "schema": 2,
            "group_id": "wake.local",
            "instance_id": "002-wake.local",
            "application_head": "a" * 64,
            "version": 12,
            "notes": [],
            "evidence": [{
                "id": "source-123",
                "source": self.url,
                "content": self.content,
                "content_sha256": self.content_hash,
                "version": 7,
            }],
        }

    def test_peer_packet_requires_matching_content_hash_and_valid_source(self):
        with patch("wake.group_peers._source_payload", return_value={"url": self.url}):
            accepted = _validated_peer(self.peer, "wake.local", "002-wake.local")
            self.assertEqual(accepted["evidence"][0]["id"], "source-123")

            altered = {**self.peer, "evidence": [{**self.peer["evidence"][0], "content": "changed"}]}
            self.assertEqual(_validated_peer(altered, "wake.local", "002-wake.local")["evidence"], [])

    def test_import_appends_attributed_source_once_to_local_record(self):
        engine = _Engine()
        with patch.dict("os.environ", {"WAKE_GROUP_ID": "wake.local"}), \
                patch("wake.group_peers._source_payload", return_value={"url": self.url}):
            first = import_group_peer_evidence(engine, [{
                "instance_id": "002-wake.local",
                "application_head": "a" * 64,
                "version": 12,
                "evidence": self.peer["evidence"],
            }])
            second = import_group_peer_evidence(engine, [{
                "instance_id": "002-wake.local",
                "application_head": "a" * 64,
                "version": 12,
                "evidence": self.peer["evidence"],
            }])

        self.assertEqual(len(first), 1)
        self.assertEqual(second, [])
        self.assertEqual(len(engine.store.appended), 1)
        event_type, stored = engine.store.appended[0]
        self.assertEqual(event_type, "observation")
        self.assertEqual(stored["peer_origin"]["instance_id"], "002-wake.local")
        self.assertEqual(stored["peer_origin"]["evidence_id"], "source-123")
        self.assertEqual(stored["source"], self.url)

    def test_group_bob_snapshot_exports_published_posts_and_receipts_only(self):
        packet = group_bob_snapshot(type("Engine", (), {"store": _BobStore()})(),
                                    "wake.local", "wake.local-001")
        self.assertEqual(packet["group_id"], "wake.local")
        self.assertEqual(packet["instance_id"], "wake.local-001")
        self.assertEqual([post["id"] for post in packet["posts"]], ["post-a"])
        self.assertIn("wake-a", packet["invocations"])
        self.assertIn("evidence-a", packet["evidence"])

    def test_unreachable_peer_does_not_prevent_collecting_from_another_member(self):
        with patch.dict("os.environ", {
            "WAKE_GROUP_ID": "wake.local",
            "WAKE_GROUP_INSTANCE": "wake.local-003",
            "WAKE_GROUP_PEERS": "wake.local-001,wake.local-002",
        }, clear=True), patch("wake.group_peers.build_opener", return_value=_PeerOpener()):
            peers = collect_group_peer_research()
        self.assertEqual([peer["instance_id"] for peer in peers], ["wake.local-002"])
        self.assertEqual(peers[0]["notes"][0]["id"], "note")


if __name__ == "__main__":
    unittest.main()
