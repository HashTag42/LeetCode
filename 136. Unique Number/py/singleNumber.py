'''
Leet Code problem 136. Unique Number
https://leetcode.com/problems/single-number/
'''


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result
