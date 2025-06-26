# LeetCode challenge: 1342. Number of Steps to Reduce a Number to Zero: <https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/>

import unittest

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while (num > 0):
            isNumEven = True if num % 2 == 0 else False
            if isNumEven:
                num /= 2
            else:
                num -= 1
            steps += 1
        return steps

class Solution_numberOfSteps_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_Case1(self):
        self.assertEqual(self.solution.numberOfSteps(14), 6)
    def test_Case2(self):
        self.assertEqual(self.solution.numberOfSteps(8), 4)
    def test_Case3(self):
        self.assertEqual(self.solution.numberOfSteps(123), 12)

if __name__ == "__main__":
    unittest.main()
