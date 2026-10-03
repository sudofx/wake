import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from wake.authority import open_authoritative_store
from wake.store import IntegrityError, Store


class AuthorityCutoverTests(unittest.TestCase):
    def test_missing_authority_fails_closed_unless_initialization_is_explicit(self):
        """Missing database files must never be interpreted as an empty recovered project."""
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            with self.assertRaisesRegex(IntegrityError, "refusing to initialize implicitly"):
                open_authoritative_store(root)

            with patch("wake.store.Store", side_effect=AssertionError("legacy Store must not be opened")):
                initialized = open_authoritative_store(root, allow_initialize=True)
            try:
                self.assertTrue((root / "sudofx.sqlite").exists())
                self.assertFalse((root / "wake.sqlite3").exists())
                envelope = initialized._envelope()
                self.assertEqual(envelope["migration"]["source"], "sudofx-native")
                self.assertEqual(envelope["migration"]["legacy_event_count"], 0)
                self.assertTrue(envelope["migration"]["archive_complete"])
            finally:
                initialized.close()

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
