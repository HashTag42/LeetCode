# LeetCode challenge: 2. Add Two Numbers
# <https://leetcode.com/problems/add-two-numbers/description/>

from typing import List, Optional
import unittest


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


class addTwoNumbers_tests(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_addTwoNumbers_1(self):
        self.assertEqual(self.sol.addTwoNumbers(l1=[2, 4, 3], l2=[5, 6, 4]), [7, 0, 8])

    def test_addTwoNumbers_2(self):
        self.assertEqual(self.sol.addTwoNumbers(l1=[0], l2=[0]), [0])

    def test_addTwoNumbers_3(self):
        self.assertEqual(self.sol.addTwoNumbers(l1=[9, 9, 9, 9, 9, 9, 9], l2=[9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1])

    def test_addTwoNumbers_4(self):
        self.assertEqual(self.sol.addTwoNumbers(l1=[0, 1], l2=[0, 1, 2]), [0, 2, 2])

    def test_addTwoNumbers_5(self):
        self.assertEqual(self.sol.addTwoNumbers(l1=[], l2=[0, 1]), [0, 1])

    def test_addTwoNumbers_6(self):
        self.assertEqual(self.sol.addTwoNumbers(l1=[9, 9], l2=[1]), [0, 0, 1])


class list_to_int_tests(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_list_to_int(self):
        self.assertEqual(self.sol.list_to_int([1, 2, 3]), 321)

    def test_list_to_int_one_item(self):
        self.assertEqual(self.sol.list_to_int([0]), 0)


class int_to_list_tests(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_int_to_list_1(self):
        self.assertEqual(self.sol.int_to_list(0), [0])

    def test_int_to_list_2(self):
        self.assertEqual(self.sol.int_to_list(321), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
