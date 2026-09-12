import unittest

from authorization import authorized_read, vulnerable_read


class AuthorizationTests(unittest.TestCase):
    def setUp(self):
        self.records = {1: {"owner_id": "alice", "title": "Private"}}

    def test_owner_can_read(self):
        self.assertEqual(authorized_read(self.records, "alice", 1)["title"], "Private")

    def test_other_actor_is_denied(self):
        with self.assertRaises(PermissionError):
            authorized_read(self.records, "bob", 1)

    def test_reference_exposes_the_original_defect(self):
        self.assertEqual(vulnerable_read(self.records, "bob", 1)["title"], "Private")


if __name__ == "__main__":
    unittest.main()
