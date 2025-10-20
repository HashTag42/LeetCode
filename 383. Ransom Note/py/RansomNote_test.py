import unittest
from RansomNote import Solution


class Solution_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_Case1(self):
        self.assertEqual(self.solution.canConstruct("a", "b"), False)

    def test_Case2(self):
        self.assertEqual(self.solution.canConstruct("aa", "ab"), False)

    def test_Case3(self):
        self.assertEqual(self.solution.canConstruct("aa", "aab"), True)
