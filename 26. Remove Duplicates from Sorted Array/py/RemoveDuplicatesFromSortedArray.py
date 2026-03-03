# LeetCode challenge: 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        insertIndex = 1
        for i in range(1, len(nums)):
            # Found unique element
            if nums[i - 1] != nums[i]:
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i]
                # Incrementing insertIndex count by 1
                insertIndex += 1
        return insertIndex
