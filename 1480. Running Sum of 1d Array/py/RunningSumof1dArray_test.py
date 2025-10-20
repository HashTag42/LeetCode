import unittest
from RunningSumof1dArray import Solution


class runningSum_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.runningSum([1, 2, 3, 4]), [1, 3, 6, 10])

    def test_2(self):
        self.assertEqual(self.solution.runningSum([1, 1, 1, 1, 1]), [1, 2, 3, 4, 5])

    def test_3(self):
        self.assertEqual(self.solution.runningSum([3, 1, 2, 10, 1]), [3, 4, 6, 16, 17])
