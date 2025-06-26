# LeetCode challenge: 2236. Root Equals Sum of Children <https://leetcode.com/problems/root-equals-sum-of-children/description/>

import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkTree(self, root: TreeNode) -> bool:
        if root.val == root.left.val + root.right.val:
            return True
        else:
            return False

class checkTree_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_if_true(self):
        _root = TreeNode(10)
        _root.left = TreeNode(4)
        _root.right = TreeNode(6)
        self.assertEqual(self.solution.checkTree(_root), True)
    def test_if_false(self):
        _root = TreeNode(5)
        _root.left = TreeNode(3)
        _root.right = TreeNode(1)
        self.assertEqual(self.solution.checkTree(_root), False)

if __name__ == "__main__":
    unittest.main()
