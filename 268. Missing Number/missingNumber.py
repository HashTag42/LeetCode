'''
LeetCode problem 268. Missing Number
https://leetcode.com/problems/missing-number/
'''

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        for i in range(0, n):
            if i not in nums:
                return i
