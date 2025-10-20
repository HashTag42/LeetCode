# LeetCode challenge: 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/

from typing import Optional


################################################################################
# Definition for singly-linked list.
################################################################################
class ListNode:
    # def __init__(self, val=0, next=None):
    #     self.val = val
    #     self.next = next
    pass


################################################################################
# SOLUTION
################################################################################
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == [] or list1 is None:
            return list2
        if list2 == [] or list2 is None:
            return list1
        list2.extend(list1)
        list2.sort()
        return list2
