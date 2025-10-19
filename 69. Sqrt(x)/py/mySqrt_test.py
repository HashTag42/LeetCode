import unittest
from mySqrt import Solution


class Solution_mySqrt_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.mySqrt(4), 2)

    def test_2(self):
        self.assertEqual(self.solution.mySqrt(8), 2)

    def test_3(self):
        self.assertEqual(self.solution.mySqrt(2147395599), 46339)
