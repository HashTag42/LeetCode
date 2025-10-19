import unittest
from FindIndexFirstOcurrenceString import Solution


class Solution_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.strStr("sadbutsad", "sad"), 0)

    def test_failure(self):
        self.assertEqual(self.solution.strStr("leetcode", "leeto"), -1)
