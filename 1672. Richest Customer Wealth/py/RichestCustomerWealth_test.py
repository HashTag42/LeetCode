import unittest
from RichestCustomerWealth import Solution


class Solution_maximumWealth_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_Case1(self):
        self.assertEqual(self.solution.maximumWealth([[1, 2, 3], [3, 2, 1]]), 6)

    def test_Case2(self):
        self.assertEqual(self.solution.maximumWealth([[1, 5], [7, 3], [3, 5]]), 10)

    def test_Case3(self):
        self.assertEqual(self.solution.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]), 17)
