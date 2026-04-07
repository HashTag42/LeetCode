import json
import pathlib
import pytest
from reverseList import Solution, ListNode

root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test_cases.json"
with open(test_cases_path) as file:
    test_cases = json.load(file)


@pytest.mark.parametrize("nodes, expected", test_cases)
def test__reverseList(nodes, expected):
    # Convert input list to a linked list
    in_head = None
    if nodes:
        in_head = ListNode(nodes[0])
        current = in_head
        for i in range(1, len(nodes)):
            current.next = ListNode(nodes[i])
            current = current.next
    out_head = Solution().reverseList(in_head)

    # Conver resulting linked list to a list
    out_list = list()
    current = out_head
    while current:
        out_list.append(current.val)
        current = current.next

    assert out_list == expected
