# LeetCode challenge: 1. Two Sum: <https://leetcode.com/problems/two-sum/description/>

from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class twoSum_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test2(self):
        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [1, 2])

    def test3(self):
        self.assertEqual(self.solution.twoSum([3, 3], 6), [0, 1])


if __name__ == "__main__":
    unittest.main()
