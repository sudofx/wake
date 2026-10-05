"""Select WAKE's authoritative durable store.

Production entry points use WAKE SQLite. The legacy WAKE Store is opened only
as a verified migration source, then removed after wake has archived and
verified the complete historical prefix. Offline experiment fixtures may still
instantiate the legacy Store directly; that path is deliberately not selected
here.
"""

from pathlib import Path
import sqlite3
from contextlib import closing

from .errors import IntegrityError
from .record_store import RecordStore
from .kernel.record import Record, APPLICATION_ID, SCHEMA_VERSION


def verify_existing_record(path):
    """Check existing format read-only before the record can run migrations."""
    path = Path(path).resolve()
    with closing(sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)) as database:
        identity = database.execute("PRAGMA application_id").fetchone()[0]
        version = database.execute("PRAGMA user_version").fetchone()[0]
        if identity != APPLICATION_ID or not 1 <= version <= SCHEMA_VERSION:
            raise IntegrityError("Unrecognized WAKE authority format")
    revision, state = Record(path).full_replay()
    if "app:wake" not in state:
        raise IntegrityError("Verified record contains no WAKE application authority")
    return revision, state


def adopt_record_filename(data_directory):
    """Verify and atomically adopt an existing V1 record without changing bytes.

    Older checkpoints used a different filename. Discover the single record by
    its format, never by a product name. Ambiguous authority fails closed.
    """
    directory = Path(data_directory)
    destination = directory / "wake.sqlite"
    candidates = [path for path in directory.glob("*.sqlite") if path != destination]
    if candidates and (destination.exists() or len(candidates) != 1):
        raise IntegrityError("Ambiguous WAKE authority; refusing to select a database")
    if candidates:
        source = candidates[0]
        # SQLite and the complete hash-linked receipt chain must verify before
        # a filename changes. No events, hashes, provenance, or headers change.
        verify_existing_record(source)
        source.replace(destination)
    return destination


def open_authoritative_store(data_directory, *, allow_initialize=False):
    """Open existing authority, or explicitly initialize a brand-new record.

    Missing authority is not equivalent to an empty project. Production and
    recovery callers therefore fail closed when neither database exists.
    Only deliberate bootstrap paths may set allow_initialize=True; that path
    initializes the WAKE record directly without an intermediate legacy store.
    """
    data_directory = Path(data_directory)
    wake_path = adopt_record_filename(data_directory)
    legacy_path = data_directory / "wake.sqlite3"

    if wake_path.exists():
        return RecordStore(data_directory)

    if not legacy_path.exists():
        if not allow_initialize:
            raise IntegrityError(
                "No authoritative WAKE database exists; refusing to initialize implicitly"
            )
        # A brand-new WAKE begins directly in wake. Do not create a temporary
        # legacy wake.sqlite3 merely to import an empty state.
        return RecordStore(data_directory, initialize_empty=True)

    # Keep the legacy engine entirely off the normal operational import path.
    # It is loaded only when an actual pre-migration database exists.
    from .store import Store

    legacy = Store(data_directory)
    migrated = None
    try:
        migrated = RecordStore.migrate_legacy(data_directory, legacy)
    finally:
        legacy.close()

    # RecordStore's constructor verifies and archives the complete legacy chain
    # before returning. Reclaim migration-only free pages only after that complete
    # verification succeeds, while the legacy database still exists as fallback
    # evidence if compaction itself fails.
    migrated.record.compact()

    # Only after verified migration and verified compaction succeed is the
    # duplicate legacy database removed, leaving one authoritative operational
    # database on disk.
    if legacy_path.exists():
        legacy_path.unlink()
    return migrated
