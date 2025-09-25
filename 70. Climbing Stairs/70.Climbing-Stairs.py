# LeetCode problem 70. Climbing Stairs
# <https://leetcode.com/problems/climbing-stairs/description/>

import unittest


class Solution:
    def climbStairs(self, n: int) -> int:
        return self.fibonacci(n)

    def fibonacci(self, n: int) -> int:
        if n <= 0:
            raise ValueError()
        elif n == 1:
            return 1
        else:
            a = 1
            b = 2
        for _ in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return b


class Solution_climbStairs_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.climbStairs(1), 1)

    def test_case_2(self):
        self.assertEqual(self.solution.climbStairs(2), 2)

    def test_case_3(self):
        self.assertEqual(self.solution.climbStairs(3), 3)

    def test_case_5(self):
        self.assertEqual(self.solution.climbStairs(5), 8)


if __name__ == "__main__":
    unittest.main()
