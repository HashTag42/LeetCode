import unittest
from RootEqualsSumofChildren import Solution, TreeNode


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
