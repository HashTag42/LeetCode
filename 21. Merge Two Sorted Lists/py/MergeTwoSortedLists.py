# LeetCode challenge: 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/

from typing import Optional
from LinkedList import LinkedList


class ListNode:
    # def __init__(self, val=0, next=None):
    #     self.val = val
    #     self.next = next
    pass


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == [] or list1 is None:
            return list2
        if list2 == [] or list2 is None:
            return list1

        ll1, ll2, llm = LinkedList(list1), LinkedList(list2), LinkedList()

        p1, p2 = ll1.head, ll2.head
        while p1 and p2:
            if p1.data <= p2.data:
                llm.append(p1.data)
                ll1.delete(p1.data)
                p1 = p1.next
            else:
                llm.append(p2.data)
                ll2.delete(p2.data)
                p2 = p2.next

        if p1:
            llm.append_from_list(ll1.to_list())
        if p2:
            llm.append_from_list(ll2.to_list())

        print(f"llm = {llm}")
        return llm.to_list()
