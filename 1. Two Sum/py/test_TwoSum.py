import unittest
from TwoSum import Solution


class twoSum_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test2(self):
        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [1, 2])

    def test3(self):
        self.assertEqual(self.solution.twoSum([3, 3], 6), [0, 1])
