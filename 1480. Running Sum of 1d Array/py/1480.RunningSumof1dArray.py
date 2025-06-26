# LeetCode challenge: 1480. Running Sum of 1d Array: <https://leetcode.com/problems/running-sum-of-1d-array/description/>

import unittest
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        _runningSum = 0
        _runningSumList = []
        for n in nums:
            _runningSum += n
            _runningSumList.append(_runningSum)
        return _runningSumList

class runningSum_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_1(self):
        self.assertEqual(self.solution.runningSum([1,2,3,4]), [1,3,6,10])
    def test_2(self):
        self.assertEqual(self.solution.runningSum([1,1,1,1,1]), [1,2,3,4,5])
    def test_3(self):
        self.assertEqual(self.solution.runningSum([3,1,2,10,1]), [3,4,6,16,17])

if __name__ == "__main__":
    unittest.main()

