from BinaryTreeLevelOrderTraversal import Solution, TreeNode


def test__Solution__levelOrder__case0():
    solution = Solution()
    root = None
    assert solution.levelOrder(root) == []


def test__Solution__levelOrder__case1():
    solution = Solution()
    root = TreeNode()
    assert solution.levelOrder(root) == [[0]]


def test__Solution__levelOrder__case2():
    solution = Solution()
    root = TreeNode(1)
    assert solution.levelOrder(root) == [[1]]


def test__Solution__levelOrder__case3():
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert solution.levelOrder(root) == [[3], [9, 20], [15, 7]]
