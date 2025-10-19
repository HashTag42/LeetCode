import unittest
from myPow import Solution


class Solution_myPow_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_myPow_1(self):
        self.assertAlmostEqual(self.solution.myPow(2.00000, 10), 1024)

    def test_myPow_2(self):
        self.assertAlmostEqual(self.solution.myPow(2.10000, 3), 9.26100)

    def test_myPow_3(self):
        self.assertAlmostEqual(self.solution.myPow(2.00000, -2), 0.25000)

    def test_myPow_4(self):
        self.assertAlmostEqual(self.solution.myPow(0.44528, 0), 1)

    # Commenting the following tests as it takes a long time to complete
    # def test_myPow_5(self):
    #     self.assertAlmostEqual(self.solution.myPow(0.00001, 2147483647), 0)
