import unittest
from AddTwoIntegers import Solution


class sum_tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1(self):
        self.assertEqual(self.solution.mySum(12, 5), 17)

    def test2(self):
        self.assertEqual(self.solution.mySum(-10, 4), -6)
