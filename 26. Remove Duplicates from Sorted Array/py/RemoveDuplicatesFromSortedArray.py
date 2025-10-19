# LeetCode challenge: 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> List[int]:
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
            # Found unique element
            if nums[i - 1] != nums[i]:
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i]
                # Incrementing insertIndex count by 1
                insertIndex = insertIndex + 1
        return insertIndex
