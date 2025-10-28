from reverseList import Solution, ListNode
import pytest


cases = [
    ([], []),
    ([1, 2], [2, 1]),
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
]


@pytest.mark.parametrize("nodes, expected", cases)
def test__reverseList(nodes, expected):
    # Convert input list to a linked list
    in_head = ListNode(None)
    current = in_head
    for i in range(len(nodes)):
        current.val = nodes[i]
        if i < len(nodes) - 1:
            current.next = ListNode()
            current = current.next

    in_head = None if in_head.val is None else in_head
    out_head = Solution().reverseList(in_head)

    # Conver resulting linked list to a list
    out_list = list()
    current = out_head
    while current:
        out_list.append(current.val)
        current = current.next

    assert out_list == expected
