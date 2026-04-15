'''
LeetCode problem 217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
'''
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
