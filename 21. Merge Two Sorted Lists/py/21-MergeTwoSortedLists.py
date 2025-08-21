# LeetCode challenge: 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/

import unittest
from typing import Optional


################################################################################
# Definition for singly-linked list.
################################################################################
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


################################################################################
# SOLUTION
################################################################################
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list2.extend(list1)
        list2.sort()
        return list2


################################################################################
# UNIT TESTS
################################################################################
class Solution_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_mergeTwoLists_example_11(self):
        self.assertEqual(self.solution.mergeTwoLists([0], [0]), [0, 0])

    def test_mergeTwoLists_example_12(self):
        self.assertEqual(self.solution.mergeTwoLists([0], [1]), [0, 1])

    def test_mergeTwoLists_example_13(self):
        self.assertEqual(self.solution.mergeTwoLists([1], [0]), [0, 1])

    def test_mergeTwoLists_example_14(self):
        self.assertEqual(self.solution.mergeTwoLists([0], [1, 2]), [0, 1, 2])

    def test_mergeTwoLists_example_15(self):
        self.assertEqual(self.solution.mergeTwoLists([1], [0, 2]), [0, 1, 2])

    def test_mergeTwoLists_example_16(self):
        self.assertEqual(self.solution.mergeTwoLists([2], [0, 1]), [0, 1, 2])

    def test_mergeTwoLists_example_17(self):
        self.assertEqual(self.solution.mergeTwoLists([1, 2], [0]), [0, 1, 2])

    def test_mergeTwoLists_example_18(self):
        self.assertEqual(self.solution.mergeTwoLists([0, 2], [1]), [0, 1, 2])

    def test_mergeTwoLists_example_19(self):
        self.assertEqual(self.solution.mergeTwoLists([0, 1], [2]), [0, 1, 2])

    def test_mergeTwoLists_example_1(self):
        self.assertEqual(self.solution.mergeTwoLists([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4])

    def test_mergeTwoLists_example_2(self):
        self.assertEqual(self.solution.mergeTwoLists([], []), [])

    def test_mergeTwoLists_example_3(self):
        self.assertEqual(self.solution.mergeTwoLists([], [0]), [0])


################################################################################
# MAIN
################################################################################
if __name__ == "__main__":
    unittest.main()
