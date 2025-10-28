'''
LeetCode problem 349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/
'''
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()
        for n in nums1:
            if n in nums2 and n not in result:
                result.append(n)
        return result
