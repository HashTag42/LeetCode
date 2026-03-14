# LeetCode problem: 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/description/


class Solution:
    def mergeSortedArray(self, nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]
        nums1.sort()
        return nums1
