import json
import pathlib
import pytest
from collections import deque
from inorderTraversal import TreeNode, Solution

root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test_cases.json"

with open(test_cases_path) as f:
    test_cases = json.load(f)


def build_tree(values: list) -> TreeNode | None:
    if not values:
        return None
    root_node = TreeNode(values[0])
    queue = deque([root_node])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root_node


@pytest.mark.parametrize("tree_values, expected", test_cases)
def test_inorderTraversal(tree_values, expected):
    sol = Solution()
    tree = build_tree(tree_values) if tree_values is not None else None
    assert sol.inorderTraversal(tree) == expected
