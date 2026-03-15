// LeetCode problem 94. Binary Tree Inorder Traversal
// https://leetcode.com/problems/binary-tree-inorder-traversal/?submissionId=1782814471

namespace LeetCode.InorderTraversal;

public class TreeNode(int val = 0, TreeNode? left = null, TreeNode? right = null)
{
    public int val = val;
    public TreeNode? left = left;
    public TreeNode? right = right;
}

public class Solution
{
    public IList<int> InorderTraversal(TreeNode? root)
    {
        var result = new List<int>();
        var stack = new Stack<TreeNode>();
        var current = root;
        while (current != null || stack.Count > 0)
        {
            while (current != null)
            {
                stack.Push(current);
                current = current.left;
            }
            current = stack.Pop();
            result.Add(current.val);
            current = current.right;
        }
        return result;
    }
}
