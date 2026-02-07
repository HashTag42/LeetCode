# LeetCode challenge: 1. Two Sum: <https://leetcode.com/problems/two-sum/description/>

from typing import List, Optional


class Solution:
    def twoSum(self, nums: Optional[List[int]], target: int) -> Optional[List[int]]:
        if nums is None or len(nums) < 2:
            return None
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
