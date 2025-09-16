# LeetCode challenge: 88. Merge Sorted Array <https://leetcode.com/problems/merge-sorted-array/description/>

from typing import List
import unittest


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m+n):
            nums1[i] = nums2[i-m]
        nums1.sort()


class merge_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        self.solution.merge(nums1, m=3, nums2=[2, 5, 6], n=3)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test2(self):
        nums1 = [1]
        self.solution.merge(nums1, m=1, nums2=[], n=0)
        self.assertEqual(nums1, [1])

    def test3(self):
        nums1 = [0]
        self.solution.merge(nums1, m=0, nums2=[1], n=1)
        self.assertEqual(nums1, [1])

    def test4(self):
        nums1 = [1, 2, 4, 5, 6, 0]
        self.solution.merge(nums1, m=5, nums2=[3], n=1)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
