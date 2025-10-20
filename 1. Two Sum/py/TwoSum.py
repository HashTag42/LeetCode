# LeetCode challenge: 1. Two Sum: <https://leetcode.com/problems/two-sum/description/>

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums == [] or nums is None:
            length = 0
        else:
            length = len(nums)
        for i in range(length):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
