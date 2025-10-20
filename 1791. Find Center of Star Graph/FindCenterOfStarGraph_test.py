import unittest
from FindCenterOfStarGraph import Solution


class Solution_findCenter_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findCenter_Case_1(self):
        self.assertEqual(self.solution.findCenter([[1, 2], [2, 3], [4, 2]]), 2)

    def test_findCenter_Case_2(self):
        self.assertEqual(self.solution.findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]), 1)

    def test_findCenter_Case_3(self):
        self.assertEqual(self.solution.findCenter([]), None)

    def test_findCenter_Case_4(self):
        self.assertEqual(self.solution.findCenter(None), None)

    def test_findCenter_Case_5(self):
        self.assertEqual(self.solution.findCenter([[1, 2], [1, 3], [1, 4], [5, 1]]), 1)
