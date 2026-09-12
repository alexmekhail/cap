"""Acceptance checks: run with python3 -m unittest -v."""
import sqlite3
import unittest

from seed import seed_users


class SeedTests(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(":memory:")
        self.addCleanup(self.db.close)

    def test_requested_users_exist(self):
        seed_users(self.db, 100)
        self.assertEqual(self.db.execute("SELECT COUNT(*) FROM users").fetchone()[0], 100)

    def test_emails_are_distinct(self):
        seed_users(self.db, 20)
        rows = self.db.execute("SELECT email FROM users").fetchall()
        self.assertEqual(len({row[0] for row in rows}), 20)

    def test_reseeding_is_idempotent(self):
        seed_users(self.db, 20)
        seed_users(self.db, 20)
        self.assertEqual(self.db.execute("SELECT COUNT(*) FROM users").fetchone()[0], 20)

    def test_negative_count_is_rejected_without_writes(self):
        with self.assertRaises(ValueError):
            seed_users(self.db, -1)
        tables = self.db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        self.assertEqual(tables, [])


if __name__ == "__main__":
    unittest.main()
