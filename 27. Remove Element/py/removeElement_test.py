import unittest
from removeElement import Solution


class Solution_removeElement_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_Example_1(self):
        self.assertEqual(self.solution.removeElement([3, 2, 2, 3], 3), (2, [2, 2]))

    def test_Example_2(self):
        self.assertEqual(self.solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2), (5, [0, 1, 3, 0, 4]))

    def test_Example_3(self):
        self.assertEqual(self.solution.removeElement([2, 2, 3], 2), (1, [3]))
