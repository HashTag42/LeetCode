import json
import pathlib
import pytest
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
    if head is None:
        return None
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test_cases.json"
with open(test_cases_path) as f:
    test_cases = json.load(f)


@pytest.mark.parametrize('list1, list2, expected', test_cases)
def test_MergeTwoSortedLists(list1, list2, expected):
    l1 = list_to_linked_list(list1)
    l2 = list_to_linked_list(list2)
    result = Solution().mergeTwoLists(l1, l2)
    assert linked_list_to_list(result) == expected
