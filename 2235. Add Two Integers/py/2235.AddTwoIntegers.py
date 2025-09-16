# LeetCode challenge: 2235. Add Two Integers: <https://leetcode.com/problems/add-two-integers/description/>

import unittest


class Solution:
    def mySum(self, num1: int, num2: int) -> int:
        return num1 + num2


class sum_tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1(self):
        self.assertEqual(self.solution.mySum(12, 5), 17)

    def test2(self):
        self.assertEqual(self.solution.mySum(-10, 4), -6)


if __name__ == "__main__":
    unittest.main()
