import pytest
from BinaryTreeLevelOrderTraversal import Solution


cases = [
    ([], []),
    # ([1], [[1]]),
    # ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
]


@pytest.mark.parametrize("tree,expected", cases)
def test__Solution__levelOrder(tree, expected):
    solution = Solution()
    assert expected == solution.levelOrder(tree)
