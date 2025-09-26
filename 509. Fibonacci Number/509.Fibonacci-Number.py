# LeetCode problem 509. Fibonacci Number
# <https://leetcode.com/problems/fibonacci-number/>

import unittest


class Solution:
    def fib(self, n: int) -> int:
        if n < 0:
            raise ValueError("Number must be a positive integer")
        elif n == 0:
            return 0
        elif n <= 2:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                c = a + b
                a = b
                b = c
            return c


class Solution_fib_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_fib_0(self):
        self.assertEqual(self.solution.fib(0), 0)

    def test_fib_1(self):
        self.assertEqual(self.solution.fib(1), 1)

    def test_fib_2(self):
        self.assertEqual(self.solution.fib(2), 1)

    def test_fib_3(self):
        self.assertEqual(self.solution.fib(3), 2)

    def test_fib_4(self):
        self.assertEqual(self.solution.fib(4), 3)

    def test_fib_5(self):
        self.assertEqual(self.solution.fib(5), 5)

    def test_fib_10(self):
        self.assertEqual(self.solution.fib(10), 55)


if __name__ == "__main__":
    unittest.main()
