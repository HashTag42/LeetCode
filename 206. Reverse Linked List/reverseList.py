'''
LeetCode Problem 206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        nodes = list()
        current = head
        while current:
            nodes.append(current.val)
            current = current.next
        nodes.reverse()

        new_head = ListNode()
        current = new_head
        for i in range(len(nodes)):
            current.val = nodes[i]
            if i < len(nodes) - 1:
                current.next = ListNode()
                current = current.next
        return new_head
