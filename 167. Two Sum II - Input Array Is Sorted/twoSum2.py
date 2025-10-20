'''
    LeetCode problem 167. Two Sum II - Input Array Is Sorted
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''

from typing import List


class Solution:
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if numbers == [] or numbers is None:
            length = 0
        else:
            length = len(numbers)
        found_values = dict()
        for i in range(length):
            if numbers[i] not in found_values:
                found_values[numbers[i]] = i
            wanted = target - numbers[i]
            if wanted in found_values and i != found_values[wanted]:
                return [found_values[wanted] + 1, i + 1]
