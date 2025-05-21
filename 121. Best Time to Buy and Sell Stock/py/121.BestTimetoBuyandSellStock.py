# LeetCode challenge: 121. Best Time to Buy and Sell Stock: <https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/>

from typing import List
import unittest

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                maxp = max(maxp, prices[j] - prices[i])
        return maxp

class maxProfit_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test1(self):
        self.assertEqual(self.solution.maxProfit([7,1,5,3,6,4]), 5)
    def test2(self):
        self.assertEqual(self.solution.maxProfit([7,6,4,3,1]), 0)

if __name__ == "__main__":
    unittest.main()

