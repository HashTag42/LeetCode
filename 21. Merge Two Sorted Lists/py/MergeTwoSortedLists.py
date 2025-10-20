# LeetCode challenge: 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/

from typing import Optional


################################################################################
# Definition for singly-linked list.
################################################################################
class ListNode:
    pass


################################################################################
# SOLUTION
################################################################################
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list2.extend(list1)
        list2.sort()
        return list2
