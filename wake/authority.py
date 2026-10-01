"""Select WAKE's authoritative durable store.

Production entry points use sudofx SQLite. The legacy WAKE Store is opened only
as a verified migration source, then removed after sudofx has archived and
verified the complete historical prefix. Offline experiment fixtures may still
instantiate the legacy Store directly; that path is deliberately not selected
here.
"""

from pathlib import Path

from .store import Store
from .sudofx_store import SudofxStore


def open_authoritative_store(data_directory):
    """Open sudofx authority and perform a one-time verified legacy migration."""
    data_directory = Path(data_directory)
    sudofx_path = data_directory / "sudofx.sqlite"
    legacy_path = data_directory / "wake.sqlite3"

    if sudofx_path.exists():
        return SudofxStore(data_directory)

    legacy = Store(data_directory)
    migrated = None
    try:
        migrated = SudofxStore(data_directory, legacy_store=legacy)
    finally:
        legacy.close()

    # SudofxStore's constructor verifies and archives the complete legacy chain
    # before returning. Only after that succeeds is the duplicate database
    # removed, leaving one authoritative operational database on disk.
    if legacy_path.exists():
        legacy_path.unlink()
    return migrated
