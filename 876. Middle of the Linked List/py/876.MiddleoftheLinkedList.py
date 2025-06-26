# LeetCode problem: 876. Middle of the Linked List: <https://leetcode.com/problems/middle-of-the-linked-list/description/>

# Solution provided by DeepSeek

import unittest
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Two pointer approach
    # Time Complexity = O(N)
    # Space Complexity = O(1)
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Helper function
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

class Solution_middleNode_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1(self):
        # Odd length list
        head = create_linked_list([1, 2, 3, 4, 5])
        middle = self.solution.middleNode(head)
        self.assertEqual(middle.val, 3)  # Check value
        self.assertEqual(middle.next.val, 4)  # Verify it's the correct node
        
    def test2(self):
        # Even length list (should return second middle)
        head = create_linked_list([1, 2, 3, 4, 5, 6])
        middle = self.solution.middleNode(head)
        self.assertEqual(middle.val, 4)  # Check value
        self.assertEqual(middle.next.val, 5)  # Verify it's the correct node

    def test3(self):
        # Single node list
        head = create_linked_list([1])
        middle = self.solution.middleNode(head)
        self.assertEqual(middle.val, 1)  # Check value
        self.assertIsNone(middle.next)  # Verify it's the correct node

if __name__ == "__main__":
    unittest.main()