import unittest
from plusOne import Solution


class Solution_plusOne_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_Case_1(self):
        self.assertEqual(self.solution.plusOne([1, 2, 3]), [1, 2, 4])

    def test_Case_2(self):
        self.assertEqual(self.solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_Case_3(self):
        self.assertEqual(self.solution.plusOne([9]), [1, 0])
