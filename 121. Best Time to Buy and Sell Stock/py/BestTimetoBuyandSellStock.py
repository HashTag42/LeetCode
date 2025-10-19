# LeetCode challenge: 121. Best Time to Buy and Sell Stock
# <https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/>

from typing import List
from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = inf
        max_price = -inf
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
