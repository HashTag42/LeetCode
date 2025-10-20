# LeetCode challenge: 1672. Richest Customer Wealth
# <https://leetcode.com/problems/richest-customer-wealth/description/>

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for customer in accounts:
            customerWealth = 0
            for money in customer:
                customerWealth += money
            if customerWealth > maxWealth:
                maxWealth = customerWealth
        return maxWealth
