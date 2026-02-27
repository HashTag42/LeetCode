import unittest
from MergeTwoSortedLists import Solution, ListNode


def list_to_linked_list(lst):
    """Convert a Python list to a linked list."""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Convert a linked list back to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


class mergeTwoLists_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_mergeTwoLists_example_1(self):
        list1 = list_to_linked_list([1, 2, 4])
        list2 = list_to_linked_list([1, 3, 4])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 1, 2, 3, 4, 4])

    def test_mergeTwoLists_example_2(self):
        result = self.solution.mergeTwoLists(None, None)
        self.assertIsNone(result)

    def test_mergeTwoLists_example_3(self):
        list2 = list_to_linked_list([0])
        result = self.solution.mergeTwoLists(None, list2)
        self.assertEqual(linked_list_to_list(result), [0])

    def test_mergeTwoLists_example_4(self):
        list1 = list_to_linked_list([0])
        result = self.solution.mergeTwoLists(list1, None)
        self.assertEqual(linked_list_to_list(result), [0])

    def test_mergeTwoLists_example_5(self):
        result = self.solution.mergeTwoLists(None, None)
        self.assertIsNone(result)

    def test_mergeTwoLists_example_6(self):
        list2 = list_to_linked_list([1])
        result = self.solution.mergeTwoLists(None, list2)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_mergeTwoLists_example_7(self):
        list1 = list_to_linked_list([1])
        result = self.solution.mergeTwoLists(list1, None)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_mergeTwoLists_example_11(self):
        list1 = list_to_linked_list([0])
        list2 = list_to_linked_list([0])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [0, 0])

    def test_mergeTwoLists_example_12(self):
        list1 = list_to_linked_list([0])
        list2 = list_to_linked_list([1])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [0, 1])

    def test_mergeTwoLists_example_13(self):
        list1 = list_to_linked_list([1])
        list2 = list_to_linked_list([0])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [0, 1])

    def test_mergeTwoLists_example_14(self):
        list1 = list_to_linked_list([0])
        list2 = list_to_linked_list([1, 2])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [0, 1, 2])

    def test_mergeTwoLists_example_15(self):
        list1 = list_to_linked_list([1])
        list2 = list_to_linked_list([0, 2])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [0, 1, 2])

    def test_mergeTwoLists_example_16(self):
        list1 = list_to_linked_list([2])
        list2 = list_to_linked_list([0, 1])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [0, 1, 2])

    def test_mergeTwoLists_example_17(self):
        list1 = list_to_linked_list([1, 2])
        list2 = list_to_linked_list([0])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [0, 1, 2])

    def test_mergeTwoLists_example_18(self):
        list1 = list_to_linked_list([0, 2])
        list2 = list_to_linked_list([1])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [0, 1, 2])

    def test_mergeTwoLists_example_19(self):
        list1 = list_to_linked_list([0, 1])
        list2 = list_to_linked_list([2])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [0, 1, 2])
