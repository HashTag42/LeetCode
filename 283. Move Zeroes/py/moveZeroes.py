'''
LeetCode problem 283. Move Zeroes
https://leetcode.com/problems/move-zeroes/description
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        nums_count = len(nums)
        insert_index = 0
        for n in range(nums_count):
            if nums[n] != 0:
                nums[insert_index] = nums[n]
                insert_index += 1
        for z in range(insert_index, nums_count):
            nums[z] = 0
