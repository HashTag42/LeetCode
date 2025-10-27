'''
LeetCode problem 217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
'''
from typing import List
from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return max(Counter(nums).values()) > 1
