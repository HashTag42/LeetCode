# LeetCode challenge: 1672. Richest Customer Wealth
# <https://leetcode.com/problems/richest-customer-wealth/description/>

import unittest
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


class Solution_maximumWealth_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_Case1(self):
        self.assertEqual(self.solution.maximumWealth([[1, 2, 3], [3, 2, 1]]), 6)

    def test_Case2(self):
        self.assertEqual(self.solution.maximumWealth([[1, 5], [7, 3], [3, 5]]), 10)

    def test_Case3(self):
        self.assertEqual(self.solution.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]), 17)


if __name__ == "__main__":
    unittest.main()
