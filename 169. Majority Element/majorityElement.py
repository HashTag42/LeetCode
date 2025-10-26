'''
LeetCode problem 169. Majority Element
https://leetcode.com/problems/majority-element/description/
'''
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Returns the element that appears more in an array (list)
        Implementation using a HashMap (dictionary)
        Time complexity = O(n)
        Space complexity = O(n)
        """
        counts = {}
        max_count = 0
        max_num = 0
        for n in nums:
            if n in counts:
                counts[n] += 1
                if max_count < counts[n]:
                    max_count = counts[n]
                    max_num = n
            else:
                counts[n] = 1
                if max_count < counts[n]:
                    max_count = counts[n]
                    max_num = n
        return max_num
