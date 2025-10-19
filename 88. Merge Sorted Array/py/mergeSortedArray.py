# LeetCode challenge: 88. Merge Sorted Array <https://leetcode.com/problems/merge-sorted-array/description/>

from typing import List


class Solution:
    def mergeSortedArray(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m+n):
            nums1[i] = nums2[i-m]
        nums1.sort()
