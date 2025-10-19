import unittest
from RemoveDuplicatesFromSortedArray import Solution


class Solution_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.removeDuplicates([1, 1, 2]), 2)

    def test_case_2(self):
        self.assertEqual(self.solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
