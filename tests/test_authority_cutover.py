import tempfile
import unittest
from pathlib import Path

from wake.authority import open_authoritative_store
from wake.store import Store


class AuthorityCutoverTests(unittest.TestCase):
    def test_verified_legacy_migration_leaves_one_operational_database(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            legacy = Store(root)
            try:
                legacy.append("initialized", {
                    "objective": "Preserve one authoritative database.",
                    "governance": 1,
                })
                before = legacy.load()
            finally:
                legacy.close()

            self.assertTrue((root / "wake.sqlite3").exists())
            self.assertFalse((root / "sudofx.sqlite").exists())

            migrated = open_authoritative_store(root)
            try:
                self.assertEqual(migrated.load(), before)
                self.assertTrue((root / "sudofx.sqlite").exists())
                self.assertFalse((root / "wake.sqlite3").exists())
            finally:
                migrated.close()

            reopened = open_authoritative_store(root)
            try:
                self.assertEqual(reopened.load(), before)
                self.assertFalse((root / "wake.sqlite3").exists())
            finally:
                reopened.close()


if __name__ == "__main__":
    unittest.main()
