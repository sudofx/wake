"""Select WAKE's authoritative durable store.

Production entry points use sudofx SQLite. The legacy WAKE Store is opened only
as a verified migration source, then removed after sudofx has archived and
verified the complete historical prefix. Offline experiment fixtures may still
instantiate the legacy Store directly; that path is deliberately not selected
here.
"""

from pathlib import Path

from .errors import IntegrityError
from .sudofx_store import SudofxStore


def open_authoritative_store(data_directory, *, allow_initialize=False):
    """Open existing authority, or explicitly initialize a brand-new record.

    Missing authority is not equivalent to an empty project. Production and
    recovery callers therefore fail closed when neither database exists.
    Only deliberate bootstrap paths may set allow_initialize=True; that path
    creates the legacy-compatible empty source solely long enough to pass
    through the same verified migration boundary into sudofx.
    """
    data_directory = Path(data_directory)
    sudofx_path = data_directory / "sudofx.sqlite"
    legacy_path = data_directory / "wake.sqlite3"

    if sudofx_path.exists():
        return SudofxStore(data_directory)

    if not legacy_path.exists():
        if not allow_initialize:
            raise IntegrityError(
                "No authoritative WAKE database exists; refusing to initialize implicitly"
            )
        # A brand-new WAKE begins directly in sudofx. Do not create a temporary
        # legacy wake.sqlite3 merely to import an empty state.
        return SudofxStore(data_directory, initialize_empty=True)

    # Keep the legacy engine entirely off the normal operational import path.
    # It is loaded only when an actual pre-migration database exists.
    from .store import Store

    legacy = Store(data_directory)
    migrated = None
    try:
        migrated = SudofxStore.migrate_legacy(data_directory, legacy)
    finally:
        legacy.close()

    # SudofxStore's constructor verifies and archives the complete legacy chain
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
