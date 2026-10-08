# =============================================================================
# LEGACY STORE — compatibility/migration semantics for the pre-wake WAKE record.
# Live operational authority is now wake SQLite. This module remains necessary
# to verify/import historical wake.sqlite3 records and to support explicit
# compatibility fixtures. It must not become a second live authority path.
# =============================================================================

"""Legacy WAKE SQLite replay used for migration evidence and compatibility fixtures."""

from contextlib import contextmanager
from copy import deepcopy
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import sqlite3
from time import perf_counter

from .event_format import ZERO, canonical, digest, now
from .domain_events import _normalize_legacy_attention_state, empty, reduce_event
from .errors import IntegrityError
from .governance import Rejected, require, transition


# ---------------------------------------------------------------------------


# STEP: empty


#


# This step exists as an explicit seam so its behavior can be


# inspected, tested, and replaced without giving a model hidden authority.


# Inputs should already belong to the layer named above; outputs remain data


# until the next boundary validates or records them. Callers may rely on this contract.


# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------


# OBJECT: Store


#


# This object groups state/behavior exists as an explicit seam so its behavior can be


# inspected, tested, and replaced without giving a model hidden authority.


# Inputs should already belong to the layer named above; outputs remain data


# until the next boundary validates or records them. Callers may rely on this contract.


# ---------------------------------------------------------------------------


class Store:
    # ---------------------------------------------------------------------------
    # STEP: __init__
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.
    # ---------------------------------------------------------------------------
    def __init__(self, directory):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.path = self.directory / "wake.sqlite3"
        self.db = sqlite3.connect(self.path, timeout=10)
        self.db.execute("PRAGMA synchronous=FULL")
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS events (
                seq INTEGER PRIMARY KEY, time TEXT NOT NULL, kind TEXT NOT NULL,
                payload TEXT NOT NULL, prev_hash TEXT NOT NULL, hash TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS snapshot (id INTEGER PRIMARY KEY CHECK(id=1),
                head TEXT NOT NULL, state TEXT NOT NULL);
        """)
        # A fresh Store still proves history by replaying from genesis. After that
        # proof succeeds, repeated reads/appends in the same process may reuse the
        # exact derived projection while the SQLite connection fingerprint remains
        # unchanged. Any observed database mutation invalidates the cache and falls
        # back to full replay. The cache is an optimization, never a second authority.
        self._trusted = None
        self._performance = {
            "full_replays": 0,
            "cached_loads": 0,
            "append_cache_hits": 0,
            "append_cache_misses": 0,
            "replay_ms": 0.0,
            "cached_copy_ms": 0.0,
        }

    # ---------------------------------------------------------------------------
    # STEP: close
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def close(self):
        self.db.close()

    @contextmanager
    # ---------------------------------------------------------------------------
    # STEP: lock
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------
    def lock(self):
        with (self.directory / "writer.lock").open("a") as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise Rejected("Another wake owns this state directory; no call was made") from None
            try:
                yield
            finally:
                fcntl.flock(lock, fcntl.LOCK_UN)

    # ---------------------------------------------------------------------------
    # STEP: events
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def events(self):
        return [{"seq": row[0], "time": row[1], "kind": row[2], "payload": json.loads(row[3]),
                 "prev_hash": row[4], "hash": row[5]}
                for row in self.db.execute("SELECT * FROM events ORDER BY seq")]

    def event_counts_since(self, seq, kinds):
        """Count a bounded event suffix without materializing the full history."""
        rows = self.db.execute(
            "SELECT kind, COUNT(*) FROM events WHERE seq > ? GROUP BY kind",
            (seq,),
        ).fetchall()
        counts = dict(rows)
        return {
            "total": sum(counts.values()),
            "kinds": {kind: counts.get(kind, 0) for kind in kinds},
        }

    def tail_events(self, kinds, limit):
        """Return the newest matching events in chronological order."""
        if not kinds or limit <= 0:
            return []
        placeholders = ",".join("?" for _ in kinds)
        rows = self.db.execute(
            f"SELECT seq,time,kind,payload,prev_hash,hash FROM events "
            f"WHERE kind IN ({placeholders}) ORDER BY seq DESC LIMIT ?",
            (*kinds, limit),
        ).fetchall()
        return [
            {"seq": row[0], "time": row[1], "kind": row[2], "payload": json.loads(row[3]),
             "prev_hash": row[4], "hash": row[5]}
            for row in reversed(rows)
        ]

    def _data_version(self):
        return self.db.execute("PRAGMA data_version").fetchone()[0]

    def _remember(self, state, head, seq):
        # Preserve Python insertion order in the hot projection. Canonical JSON is
        # useful for hashing/snapshot comparison, but sort_keys=True would destroy
        # the record's deterministic recency ordering if used as the cache format.
        self._trusted = {
            "seq": seq,
            "head": head,
            "state": deepcopy(state),
            "encoded": canonical(state),
            "total_changes": self.db.total_changes,
            "data_version": self._data_version(),
        }

    def _cached_base(self):
        """Return the already-proved projection only while SQLite is unchanged."""
        trusted = self._trusted
        if not trusted:
            return None
        if self.db.total_changes != trusted["total_changes"] or self._data_version() != trusted["data_version"]:
            self._trusted = None
            return None
        tail = self.db.execute("SELECT seq, hash FROM events ORDER BY seq DESC LIMIT 1").fetchone()
        seq, head = (tail if tail else (0, ZERO))
        if seq != trusted["seq"] or head != trusted["head"]:
            self._trusted = None
            return None
        snapshot = self.db.execute("SELECT head, state FROM snapshot WHERE id=1").fetchone()
        if snapshot is not None and snapshot != (trusted["head"], trusted["encoded"]):
            self._trusted = None
            return None
        if seq and snapshot is None:
            self._trusted = None
            return None
        started = perf_counter()
        state = deepcopy(trusted["state"])
        self._performance["cached_copy_ms"] += (perf_counter() - started) * 1000
        return state, head

    def head(self):
        cached = self._cached_base()
        if cached is not None:
            return cached[1]
        return self.replay()[1]

    def projection(self):
        """Return current verified state/head, reusing the trusted hot snapshot when possible."""
        cached = self._cached_base()
        if cached is not None:
            return cached
        return self.replay()

    def tail_events_all(self, limit):
        """Return the newest bounded event suffix in chronological order."""
        if limit <= 0:
            return []
        rows = self.db.execute(
            "SELECT seq,time,kind,payload,prev_hash,hash FROM events ORDER BY seq DESC LIMIT ?",
            (limit,),
        ).fetchall()
        return [
            {"seq": row[0], "time": row[1], "kind": row[2], "payload": json.loads(row[3]),
             "prev_hash": row[4], "hash": row[5]}
            for row in reversed(rows)
        ]

    def performance_snapshot(self):
        return {
            "authority": "legacy-wake",
            **{key: (round(value, 3) if isinstance(value, float) else value)
               for key, value in self._performance.items()},
            "event_count": self.db.execute("SELECT COUNT(*) FROM events").fetchone()[0],
            "trusted_projection_active": self._trusted is not None,
        }

    # ---------------------------------------------------------------------------
    # STEP: replay
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def replay_record(self):
        """Verify history once and return the reconstructed state, head, and verified events."""
        started = perf_counter()
        state, head = empty(), ZERO
        try:
            events = self.events()
            for expected, event in enumerate(events, 1):
                body = {k: v for k, v in event.items() if k != "hash"}
                if event["seq"] != expected or event["prev_hash"] != head or digest(body) != event["hash"]:
                    raise IntegrityError(f"Event {expected}: broken hash chain; restore a known-good backup")
                # Reconstruct historical decisions under replay-compatible policy.
                # New acceptance-time editorial rules must not invalidate old accepted events.
                state = reduce_event(state, event, historical=True)
                head = event["hash"]
        except (ValueError, KeyError, TypeError, sqlite3.DatabaseError) as exc:
            self._trusted = None
            raise IntegrityError(f"Invalid history: {exc}") from exc
        self._performance["full_replays"] += 1
        self._performance["replay_ms"] += (perf_counter() - started) * 1000
        self._remember(state, head, len(events))
        return state, head, events

    def replay(self):
        state, head, _ = self.replay_record()
        return state, head

    # ---------------------------------------------------------------------------
    # STEP: load
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def load(self, repair=False):
        # Reads remain authoritative reconstruction points. The hot cache is used
        # only by append/head operations after a successful replay, so callers that
        # explicitly load state keep the original full-history verification contract.
        state, head = self.replay()
        encoded = canonical(state)
        row = self.db.execute("SELECT head, state FROM snapshot WHERE id=1").fetchone()
        normalized_row = row
        if row is not None:
            try:
                normalized_row = (row[0], canonical(_normalize_legacy_attention_state(json.loads(row[1]))))
            except (TypeError, ValueError):
                normalized_row = row
        if normalized_row != (head, encoded):
            if not repair:
                raise IntegrityError("Projection differs from valid history; run `python -m wake recover`")
            with self.db:
                self.db.execute("INSERT OR REPLACE INTO snapshot VALUES(1,?,?)", (head, encoded))
            self._remember(state, head, self.db.execute("SELECT COUNT(*) FROM events").fetchone()[0])
        elif row != normalized_row:
            with self.db:
                self.db.execute("INSERT OR REPLACE INTO snapshot VALUES(1,?,?)", (head, encoded))
            self._remember(state, head, self.db.execute("SELECT COUNT(*) FROM events").fetchone()[0])
        return state

    # ---------------------------------------------------------------------------
    # STEP: reset
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def reset(self):
        """Irreversibly clear durable history and rebuild the empty projection."""
        self._trusted = None
        with self.db:
            self.db.execute("DELETE FROM events")
            self.db.execute("DELETE FROM snapshot")
        # Rewrite the SQLite file so deleted records are not left in free pages.
        self.db.execute("VACUUM")
        (self.directory / "experiment.json").unlink(missing_ok=True)
        return self.load(repair=True)

    # ---------------------------------------------------------------------------
    # STEP: append
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def append(self, kind, payload, crash=False):
        cached = self._cached_base()
        if cached is None:
            self._performance["append_cache_misses"] += 1
            state, head = self.replay()
        else:
            self._performance["append_cache_hits"] += 1
            state, head = cached
        seq = (self._trusted["seq"] if self._trusted else
               self.db.execute("SELECT COUNT(*) FROM events").fetchone()[0]) + 1
        event = {"seq": seq, "time": now(), "kind": kind, "payload": payload, "prev_hash": head}
        event["hash"] = digest(event)
        state = reduce_event(state, event)
        encoded = canonical(state)
        with self.db:
            self.db.execute("INSERT INTO events VALUES(?,?,?,?,?,?)",
                            (seq, event["time"], kind, canonical(payload), head, event["hash"]))
            if crash:
                os._exit(86)  # Deliberate experiment: process dies before transaction commit.
            self.db.execute("INSERT OR REPLACE INTO snapshot VALUES(1,?,?)", (event["hash"], encoded))
        self._remember(state, event["hash"], seq)
        return state

    # ---------------------------------------------------------------------------
    # STEP: backup
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def backup(self, destination):
        path = Path(destination)
        path.parent.mkdir(parents=True, exist_ok=True)
        require(not path.exists(), "Backup destination already exists")
        with sqlite3.connect(path) as target:
            self.db.backup(target)
        return path
