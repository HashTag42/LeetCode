'''
LeetCode problem 35. Search Insert Position
https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Uses a Binary Search.
        Time complexity: O(log n)
        Space complexity: O(1)
        """
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid  # Found
            elif nums[mid] < target:
                low = mid + 1  # Search right half
            else:
                high = mid - 1  # Search left half

        return low  # Not found
