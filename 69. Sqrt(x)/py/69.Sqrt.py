# Leet Code challenge: 69. Sqrt(x)
# <https://leetcode.com/problems/sqrtx/>

import unittest


class Solution:
    def mySqrt(self, x: int) -> int:
        previous, current = 0, 0
        while True:
            previous = current
            current += 1
            sum = current * current
            if sum > x:
                return previous


class Solution_mySqrt_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.mySqrt(4), 2)

    def test_2(self):
        self.assertEqual(self.solution.mySqrt(8), 2)

    def test_3(self):
        self.assertEqual(self.solution.mySqrt(2147395599), 46339)


if __name__ == "__main__":
    unittest.main()
