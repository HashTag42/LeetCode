'''
Leet Code problem 136. Unique Number
https://leetcode.com/problems/single-number/
'''
from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        uniques = [item for item, count in counter.items() if count == 1]
        return uniques[0]
