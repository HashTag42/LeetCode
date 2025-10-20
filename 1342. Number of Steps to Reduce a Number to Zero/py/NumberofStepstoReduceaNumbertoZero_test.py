import unittest
from NumberofStepstoReduceaNumbertoZero import Solution


class Solution_numberOfSteps_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_Case1(self):
        self.assertEqual(self.solution.numberOfSteps(14), 6)

    def test_Case2(self):
        self.assertEqual(self.solution.numberOfSteps(8), 4)

    def test_Case3(self):
        self.assertEqual(self.solution.numberOfSteps(123), 12)
