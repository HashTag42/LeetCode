# LeetCode challenge: 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        '''
        Time Complexity: O(n + m) where n and m are the lengths of the lists
        Space Complexity: O(1) - only using pointers, no extra data structures
        '''
        # Create a dummy node to simplify logic
        dummy = ListNode(0)
        current = dummy

        # Merge by comparing nodes and attaching the smaller one
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach remaining nodes
        current.next = list1 if list1 else list2

        return dummy.next
