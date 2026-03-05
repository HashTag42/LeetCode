# LeetCode Problem: 27. Remove Element
# <https://leetcode.com/problems/remove-element/description/>


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        while True:
            if index >= len(nums):
                break
            if nums[index] == val:
                del nums[index]
            else:
                index += 1
        k = len(nums) - nums.count(val)
        return k
