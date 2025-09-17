# LeetCode challenge: 50. Pow(x, n)
# <https://leetcode.com/problems/powx-n/description/>

import unittest


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Time Complexity: O(N)
        if n > 0:
            expo = x
            for _ in range(1, n):
                expo *= x
        elif n == 0:
            expo = 1
        else:   # n < 0
            expo = 1 / x
            for _ in range(1, abs(n)):
                expo /= x
        return expo


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

    def test_myPow_5(self):
        self.assertAlmostEqual(self.solution.myPow(0.00001, 2147483647), 0)


if __name__ == "__main__":
    unittest.main()
