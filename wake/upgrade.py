"""Audit disposable copies before replacing a running installation's source."""
from contextlib import closing
from pathlib import Path
import argparse
import sqlite3
import tempfile

from .installation_cli import NODE_IDS
from .record_store import RecordStore
from .audit import verify_events
from .hosted import verify_recovery


def check_upgrade(root):
    """Read the original records; run migrations and semantic replay only on copies."""
    root = Path(root)
    records = {node: root / 'nodes' / node / 'record' / 'wake.sqlite' for node in NODE_IDS}
    present = {node: path for node, path in records.items() if path.exists()}
    if present and len(present) != len(records):
        raise ValueError('Incomplete installation; inspect missing records before upgrading')
    with tempfile.TemporaryDirectory(prefix='wake-upgrade-check-') as temporary:
        for node, source in present.items():
            directory = Path(temporary) / node
            directory.mkdir()
            with closing(sqlite3.connect(source.resolve().as_uri() + '?mode=ro', uri=True)) as original:
                with closing(sqlite3.connect(directory / 'wake.sqlite')) as copy:
                    original.backup(copy)
            store = RecordStore(directory)
            try:
                # Reject unsupported domain history before the more expensive
                # native-journal check. Replaying the generic application log
                # again would duplicate this domain proof at quadratic cost.
                state, _ = verify_events(store.events(), store.head())
                if state != store.load():
                    raise ValueError('Record projection differs from independent replay')
                verify_recovery(directory / 'wake.sqlite')
            finally:
                store.close()
    return len(present)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', required=True, type=Path)
    args = parser.parse_args()
    try:
        count = check_upgrade(args.data)
    except Exception as error:
        # Errors may carry historical payloads; disclose only the failure class.
        parser.exit(1, f'Upgrade check failed ({type(error).__name__}); existing container and records were not changed.\n')
    print(f'Upgrade check passed for {count} existing records; originals were read only.')


if __name__ == '__main__':
    main()
