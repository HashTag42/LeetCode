# LeetCode Problem: 27. Remove Element
# <https://leetcode.com/problems/remove-element/description/>

import unittest
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        while True:
            if index >= len(nums):
                break
            if nums[index] == val:
                del nums[index]
            else:
                index += 1
        k = len(nums) - nums.count(val)
        return k, nums[0:k]


class Solution_removeElement_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_Example_1(self):
        self.assertEqual(self.solution.removeElement([3, 2, 2, 3], 3), (2, [2, 2]))

    def test_Example_2(self):
        self.assertEqual(self.solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2), (5, [0, 1, 3, 0, 4]))

    def test_Example_3(self):
        self.assertEqual(self.solution.removeElement([2, 2, 3], 2), (1, [3]))


if __name__ == "__main__":
    unittest.main()
