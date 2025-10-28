from reverseList import Solution
from LinkedList import LinkedList
import pytest


cases = [
    ([], []),
    ([1, 2], [2, 1]),
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
]


@pytest.mark.parametrize("nodes, expected", cases)
def test__reverseList(nodes, expected):
    solution = Solution()

    ll_in = LinkedList(nodes)
    out_head = solution.reverseList(ll_in.head)

    out_list = list()
    current = out_head
    while current:
        out_list.append(current.data)
        current = current.next

    assert out_list == expected
