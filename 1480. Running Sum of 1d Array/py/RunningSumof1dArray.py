# LeetCode challenge: 1480. Running Sum of 1d Array
# <https://leetcode.com/problems/running-sum-of-1d-array/description/>

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        _runningSum = 0
        _runningSumList = []
        for n in nums:
            _runningSum += n
            _runningSumList.append(_runningSum)
        return _runningSumList
