'''
Leet Code problem 136. Unique Number
https://leetcode.com/problems/single-number/
'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result
