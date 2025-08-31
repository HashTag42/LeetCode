# LeetCode challenge: 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


class Solution_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.strStr("sadbutsad", "sad"), 0)

    def test_failure(self):
        self.assertEqual(self.solution.strStr("leetcode", "leeto"), -1)


if __name__ == "__main__":
    unittest.main()
