# LeetCode problem 94. Binary Tree Inorder Traversal
# <https://leetcode.com/problems/binary-tree-inorder-traversal/?submissionId=1782814471>

import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root is not None:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)


class Solution_inorderTraversal_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_inorderTraversal_TestCase_1(self):
        bt = TreeNode(1)
        bt.right = TreeNode(2)
        bt.right.left = TreeNode(3)
        self.assertEqual(self.solution.inorderTraversal(bt), [1, 3, 2])

    def test_inorderTraversal_TestCase_2(self):
        bt = TreeNode(1)
        bt.left = TreeNode(2)
        bt.left.left = TreeNode(4)
        bt.left.right = TreeNode(5)
        bt.left.right.left = TreeNode(6)
        bt.left.right.right = TreeNode(7)
        bt.right = TreeNode(3)
        bt.right.right = TreeNode(8)
        bt.right.right.left = TreeNode(9)
        actual = self.solution.inorderTraversal(bt)
        expected = [4, 2, 6, 5, 7, 1, 3, 9, 8]
        self.assertEqual(actual, expected)

    def test_inorderTraversal_TestCase_3(self):
        self.assertEqual(self.solution.inorderTraversal(None), [])

    def test_inorderTraversal_TestCase_4(self):
        bt = TreeNode(1)
        self.assertEqual(self.solution.inorderTraversal(bt), [1])


if __name__ == "__main__":
    unittest.main()
