import unittest

from group_access import group_access_allowed, normalize_group_ids


class GroupAccessTests(unittest.TestCase):
    def test_normalizes_multiple_group_id_formats(self):
        self.assertEqual(
            normalize_group_ids(["123", 456, " 789 ", "", "invalid"]),
            {"123", "456", "789"},
        )

    def test_disabled_mode_allows_group(self):
        self.assertTrue(group_access_allowed("disabled", "123", ["999"], []))

    def test_whitelist_only_allows_listed_group(self):
        self.assertTrue(group_access_allowed("whitelist", "123", ["123"], []))
        self.assertFalse(group_access_allowed("whitelist", "999", ["123"], []))

    def test_blacklist_denies_listed_group(self):
        self.assertFalse(group_access_allowed("blacklist", "123", [], ["123"]))
        self.assertTrue(group_access_allowed("blacklist", "999", [], ["123"]))


if __name__ == "__main__":
    unittest.main()
