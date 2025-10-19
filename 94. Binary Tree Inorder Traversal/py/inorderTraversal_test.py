import unittest
from inorderTraversal import TreeNode, Solution


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
