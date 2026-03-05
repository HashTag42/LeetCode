# LeetCode Problem: 27. Remove Element
# <https://leetcode.com/problems/remove-element/description/>


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        while index < len(nums):
            if nums[index] == val:
                del nums[index]
            else:
                index += 1
        return len(nums)
