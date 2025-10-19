# LeetCode challenge: 2. Add Two Numbers
# <https://leetcode.com/problems/add-two-numbers/description/>

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.int_to_list(self.list_to_int(l1) + self.list_to_int(l2))

    def list_to_int(self, l1: Optional[ListNode]) -> List:
        number = 0
        for n in range(len(l1)):
            number += l1[n] * (10 ** n)
        return number

    def int_to_list(self, num: int) -> List:
        s_num = str(num)
        len_s = len(s_num)
        li = []
        for i in range(len_s):
            li.append(int(s_num[len_s - i - 1]))
        return li
