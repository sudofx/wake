"""Detached signed witnesses and trusted replay seeds; never a second authority.

Trust comes from an independently retained public key and checkpoint. A suffix
replay verifies new events, not the old prefix; full verification checks both.
"""
from copy import deepcopy
from functools import wraps
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

from .errors import IntegrityError
from .kernel.record import apply_operation, IntegrityError as RecordIntegrityError
from .kernel.applications import application_state
from .application import WAKE_APPLICATION
from .kernel.storage import GENESIS_HASH, canonical_json, hash_event

FORMAT = 'wake-checkpoint@1'


def _bytes(value):
    return canonical_json(value).encode()


def _digest(value):
    return hashlib.sha256(_bytes(value)).hexdigest()


def _openssl(arguments):
    try:
        subprocess.run(['openssl', *arguments], check=True, capture_output=True)
    except (OSError, subprocess.CalledProcessError) as error:
        raise IntegrityError('Checkpoint signature operation failed (requires OpenSSL Ed25519)') from error


def _chain_anchor(connection, table):
    row = connection.execute(f'SELECT sequence, event_hash FROM {table} ORDER BY sequence DESC LIMIT 1').fetchone()
    return {'sequence': row['sequence'], 'head': row['event_hash']} if row else {'sequence': 0, 'head': GENESIS_HASH}


def _record_errors(function):
    @wraps(function)
    def guarded(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except RecordIntegrityError as error:
            raise IntegrityError(str(error)) from error
    return guarded


@_record_errors
def create_checkpoint(record, destination, private_key):
    """Fully verify all journals in one read transaction, then sign exact bytes.

    Destination must be new. Keys are operator-owned; never copied into artifacts.
    """
    target = Path(destination)
    if target.exists():
        raise FileExistsError('Checkpoint destination already exists')
    with record.connect() as connection:
        connection.execute('BEGIN')
        revision, state, sequence, head = record._full_replay(connection)
        record._verified_invocation_history(connection)
        record._verified_application_access_history(connection)
        state = _compact_state(state)
        value = {
            'format': FORMAT, 'revision': revision, 'sequence': sequence,
            'head': head, 'state_digest': _digest(state), 'state': state,
            'journals': {name: _chain_anchor(connection, name) for name in
                         ('invocation_events', 'application_access_events')},
        }
    # Build off to the side. An incomplete artifact can never replace a witness.
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=target.parent) as temporary:
        root = Path(temporary) / 'checkpoint'
        root.mkdir()
        snapshot = root / 'checkpoint.json'
        snapshot.write_bytes(_bytes(value))
        _openssl(['pkeyutl', '-sign', '-rawin', '-inkey', str(private_key),
                  '-in', str(snapshot), '-out', str(root / 'checkpoint.sig')])
        target.mkdir()  # Exclusive reservation prevents replacing a concurrent witness.
        snapshot.rename(target / 'checkpoint.json')
        (root / 'checkpoint.sig').rename(target / 'checkpoint.sig')
    return {key: value[key] for key in ('format', 'revision', 'sequence', 'head', 'state_digest')}


def read_checkpoint(directory, public_key):
    """Verify with an explicitly supplied trusted key, never an artifact's key."""
    root = Path(directory)
    snapshot = root / 'checkpoint.json'
    # Verify and parse the same captured bytes even if the source changes.
    raw = snapshot.read_bytes()
    signature = (root / 'checkpoint.sig').read_bytes()
    with tempfile.TemporaryDirectory() as temporary:
        captured = Path(temporary)
        (captured / 'payload').write_bytes(raw)
        (captured / 'signature').write_bytes(signature)
        _openssl(['pkeyutl', '-verify', '-rawin', '-pubin', '-inkey', str(public_key),
                  '-in', str(captured / 'payload'), '-sigfile', str(captured / 'signature')])
    try:
        value = json.loads(raw)
        if (value['format'] != FORMAT or type(value['sequence']) is not int
                or type(value['revision']) is not int or value['sequence'] < 0
                or value['revision'] < 0 or value['revision'] > value['sequence']
                or set(value['journals']) != {'invocation_events', 'application_access_events'}
                or not isinstance(value['state'], dict)
                or value['state_digest'] != _digest(value['state'])):
            raise ValueError('invalid snapshot')
        if raw != _bytes(value):
            raise ValueError('noncanonical snapshot')
        for anchor in value['journals'].values():
            if (set(anchor) != {'sequence', 'head'} or type(anchor['sequence']) is not int
                    or anchor['sequence'] < 0 or not _valid_hash(anchor['head'])):
                raise ValueError('invalid journal anchor')
        if not _valid_hash(value['head']):
            raise ValueError('invalid semantic head')
        return value
    except (ValueError, KeyError, TypeError, AttributeError) as error:
        raise IntegrityError('Invalid signed checkpoint schema or state digest') from error


def _boundary(connection, table, anchor):
    if anchor['sequence'] == 0:
        if anchor['head'] != GENESIS_HASH:
            raise IntegrityError('Invalid genesis checkpoint')
        return
    row = connection.execute(f'SELECT event_hash FROM {table} WHERE sequence=?', (anchor['sequence'],)).fetchone()
    if row is None or row['event_hash'] != anchor['head']:
        raise IntegrityError(f'{table} does not match independently retained checkpoint (rewrite or truncation)')


@_record_errors
def replay_checkpoint(record, directory, public_key, *, full=False):
    """Replay only the verified suffix from a signed seed, or audit from genesis.

    Full mode also verifies provider/access journals and checks the seed against
    a genesis reconstruction. Fast mode attests semantic state only. It cannot
    detect modifications inside the trusted prefix; use full audit for that.
    No database bytes or history are changed.
    """
    seed = read_checkpoint(directory, public_key)
    with record.connect() as connection:
        connection.execute('BEGIN')
        _boundary(connection, 'events', {'sequence': seed['sequence'], 'head': seed['head']})
        for table, anchor in seed['journals'].items():
            if table not in ('invocation_events', 'application_access_events'):
                raise IntegrityError('Unknown checkpoint journal')
            _boundary(connection, table, anchor)
        state = deepcopy(seed['state'])
        revision, head, sequence = seed['revision'], seed['head'], seed['sequence']
        if full:
            # Reconstruct the prefix without trusting the projection or signer.
            prefix_state, prefix_revision, prefix_head = {}, 0, GENESIS_HASH
            prefix_revision_sequence = 0
            for row in connection.execute('SELECT * FROM events WHERE sequence<=? ORDER BY sequence', (sequence,)):
                event = record._event_from_row(row)
                if event['sequence'] != prefix_revision_sequence + 1:
                    raise IntegrityError('Checkpoint prefix sequence gap')
                prefix_revision_sequence = event['sequence']
                prefix_revision, prefix_head = _apply_event(event, prefix_state, prefix_revision, prefix_head, compact=False)
            if prefix_revision != revision or prefix_head != head or _digest(_compact_state(prefix_state)) != seed['state_digest']:
                raise IntegrityError('Checkpoint state differs from verified history')
            record._verified_invocation_history(connection)
            record._verified_application_access_history(connection)
        verified = 0
        for row in connection.execute('SELECT * FROM events WHERE sequence>? ORDER BY sequence', (sequence,)):
            event = record._event_from_row(row)
            if event['sequence'] != sequence + 1:
                raise IntegrityError('Checkpoint suffix sequence gap')
            revision, head = _apply_event(event, state, revision, head)
            sequence = event['sequence']
            verified += 1
    return revision, state, {'sequence': sequence, 'head': head, 'suffix_events_verified': verified,
                             'verification': 'full-history' if full else 'signed-prefix-and-semantic-suffix'}


def _apply_event(event, state, revision, previous, *, compact=True):
    material = {key: event[key] for key in
                ('receipt_id', 'proposal_id', 'status', 'revision_before', 'revision_after', 'reasons')}
    material['payload'] = event['proposal']
    if event['provenance'] is not None:
        material['provenance'] = event['provenance']
    if (event['previous_hash'] != previous or hash_event(previous, material) != event['event_hash']
            or event['revision_before'] != revision or event['status'] not in ('accepted', 'rejected')):
        raise IntegrityError(f"Checkpoint event verification failed at {event['sequence']}")
    if event['status'] == 'accepted':
        for operation in event['proposal']['operations']:
            if compact:
                _apply_seed_operation(state, operation)
            else:
                apply_operation(state, operation)
        revision += 1
    if event['revision_after'] != revision:
        raise IntegrityError('Checkpoint revision discontinuity')
    return revision, event['event_hash']


def _compact_state(state):
    """Materialize the owned application once; history stays in the database."""
    result = deepcopy(state)
    for key, envelope in list(result.items()):
        if isinstance(envelope, dict) and envelope.get("storage") == "event_log":
            if envelope.get("application_id") != WAKE_APPLICATION.application_id:
                raise IntegrityError("No registered checkpoint reducer for this application")
            result[key] = {
                "application_id": envelope["application_id"],
                "application_version": envelope["application_version"],
                "storage": "event_log", "projection_state": application_state(WAKE_APPLICATION, envelope),
            }
    return result


def _apply_seed_operation(state, operation):
    """Apply a suffix to the signed application projection and verify result digest.

    This application-owned replay optimization never changes kernel event bytes
    or installs a new storage authority. Unknown applications fail closed.
    """
    if operation.get("action") != "apply_application" or operation["value"].get("storage") != "event_log":
        apply_operation(state, operation)
        return
    value = operation["value"]
    if value["application_id"] != WAKE_APPLICATION.application_id or value["application_version"] != WAKE_APPLICATION.version:
        raise IntegrityError("Unsupported application checkpoint version")
    key = 'app:' + value["application_id"]
    envelope = state.get(key)
    current = application_state(WAKE_APPLICATION, envelope)
    action = WAKE_APPLICATION.action(value["action"])
    if action is None:
        raise IntegrityError("Unknown application action in checkpoint suffix")
    decision = (action.replay or action.evaluate)(current, value.get("input"))
    if not decision.accepted or _digest(decision.next_state) != value["result_digest"]:
        raise IntegrityError("Checkpoint application suffix replay drift")
    state[key] = {"application_id": value["application_id"],
                  "application_version": value["application_version"],
                  "storage": "event_log", "projection_state": decision.next_state}


def _valid_hash(value):
    return isinstance(value, str) and len(value) == 64 and all(c in '0123456789abcdef' for c in value)
