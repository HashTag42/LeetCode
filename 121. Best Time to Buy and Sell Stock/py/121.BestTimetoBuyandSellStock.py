# LeetCode challenge: 121. Best Time to Buy and Sell Stock: <https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/>

################################################################################
from typing import List
from math import inf
import unittest
################################################################################

################################################################################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price  =  inf
        max_price  = -inf
        cur_profit = -inf
        max_profit = -inf
        for i in range(len(prices)):
            price = prices[i]
            if price < min_price:
                min_price = price
                max_price = -inf
            if price > max_price:
                max_price = price
                cur_profit = max_price - min_price
                max_profit = max(cur_profit, max_profit)
        return max_profit
################################################################################

################################################################################
class maxProfit_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test01(self):
        self.assertEqual(self.solution.maxProfit([0]), 0)
    def test02(self):
        self.assertEqual(self.solution.maxProfit([0,0]), 0)
    def test03(self):
        self.assertEqual(self.solution.maxProfit([0,1]), 1)
    def test04(self):
        self.assertEqual(self.solution.maxProfit([1,0]), 0)
    def test05(self):
        self.assertEqual(self.solution.maxProfit([0,1,2]), 2)
    def test06(self):
        self.assertEqual(self.solution.maxProfit([0,2,1]), 2)
    def test07(self):
        self.assertEqual(self.solution.maxProfit([7,1,5,3,6,4]), 5)
    def test08(self):
        self.assertEqual(self.solution.maxProfit([7,6,4,3,1]), 0)
    def test09(self):
        self.assertEqual(self.solution.maxProfit([0,2,1,4]), 4)
    def test10(self):
        self.assertEqual(self.solution.maxProfit([0,1,2,3,4,5]), 5)
    def test11(self):
        self.assertEqual(self.solution.maxProfit([2,4,1,4]), 3)
    def test12(self):
        self.assertEqual(self.solution.maxProfit([2,4,1]), 2)
    def test13(self):
        self.assertEqual(self.solution.maxProfit([2,5,1,3]), 3)
    def test14(self):
        self.assertEqual(self.solution.maxProfit([3,2,6,5,0,3]), 4)
    def tearDown(self):
        pass
################################################################################

################################################################################
if __name__ == "__main__":
    unittest.main()
################################################################################

