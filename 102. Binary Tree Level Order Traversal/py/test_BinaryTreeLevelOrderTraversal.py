import json
import os
from collections import deque
from typing import Optional

import pytest

from BinaryTreeLevelOrderTraversal import Solution, TreeNode


def build_tree(values: Optional[list]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
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
    return root


def load_cases():
    path = os.path.join(os.path.dirname(__file__), "..", "test_cases.json")
    with open(path) as f:
        return json.load(f)


CASES = load_cases()


@pytest.mark.parametrize("case", CASES)
def test__Solution__levelOrder(case):
    root = build_tree(case[0])
    assert Solution().levelOrder(root) == case[1]
