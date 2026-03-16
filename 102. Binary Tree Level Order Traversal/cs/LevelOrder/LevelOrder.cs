// LeetCode problem #102 Binary Tree Level Order Traversal
// https://leetcode.com/problems/binary-tree-level-order-traversal/description/

// Definition for a binary tree node.
public class TreeNode
{
    public int val;
    public TreeNode? left;
    public TreeNode? right;
    public TreeNode(int val=0, TreeNode? left=null, TreeNode? right=null)
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution
{
    public IList<IList<int>> LevelOrder(TreeNode? root)
    {
        var levels = new List<IList<int>>();
        if (root == null)
            return levels;

        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);

        while (queue.Count > 0)
        {
            var level = new List<int>();
            int size = queue.Count;
            for (int i = 0; i < size; i++)
            {
                var node = queue.Dequeue();
                level.Add(node.val);
                if (node.left != null)  queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }
            levels.Add(level);
        }

        return levels;
    }
}
