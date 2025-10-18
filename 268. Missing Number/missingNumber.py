'''
LeetCode problem 268. Missing Number
https://leetcode.com/problems/missing-number/
'''

from typing import List


class Solution:
    def missingNumber1(self, nums: List[int]) -> int:
        """
            Time complexity = O(n^2)
            Storage complexity = O(1)
        """
        n = len(nums) + 1
        for i in range(0, n):
            if i not in nums:
                return i

    def missingNumber2(self, nums: List[int]) -> int:
        """
            Time complexity = O(n) to obtain sum_of_elements
            Storage complexity = O(1)
        """
        n = len(nums)
        sum_of_elements = sum(nums)
        actual_sum = (n * (n + 1)) / 2
        return int(actual_sum - sum_of_elements)
