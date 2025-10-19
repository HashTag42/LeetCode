import unittest
from climbStairs import Solution


class Solution_climbStairs_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.climbStairs(1), 1)

    def test_case_2(self):
        self.assertEqual(self.solution.climbStairs(2), 2)

    def test_case_3(self):
        self.assertEqual(self.solution.climbStairs(3), 3)

    def test_case_5(self):
        self.assertEqual(self.solution.climbStairs(5), 8)
