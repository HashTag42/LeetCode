import unittest
from MiddleoftheLinkedList import Solution, create_linked_list


class Solution_middleNode_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_odd_length_list(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        middle = self.solution.middleNode(head)
        self.assertEqual(middle.val, 3)  # Check value
        self.assertEqual(middle.next.val, 4)  # Verify it's the correct node

    def test_even_length_list(self):
        # Even length list (should return second middle)
        head = create_linked_list([1, 2, 3, 4, 5, 6])
        middle = self.solution.middleNode(head)
        self.assertEqual(middle.val, 4)  # Check value
        self.assertEqual(middle.next.val, 5)  # Verify it's the correct node

    def test_single_node_list(self):
        head = create_linked_list([1])
        middle = self.solution.middleNode(head)
        self.assertEqual(middle.val, 1)  # Check value
        self.assertIsNone(middle.next)  # Verify it's the correct node

    def test_empty_list(self):
        head = create_linked_list([])
        middle = self.solution.middleNode(head)
        self.assertEqual(middle, None)  # Check value

    def test_no_list(self):
        head = create_linked_list(None)
        middle = self.solution.middleNode(head)
        self.assertEqual(middle, None)  # Check value
