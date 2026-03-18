// LeetCode problem: 118. Pascal's Triangle
// https://leetcode.com/problems/pascals-triangle/description/

namespace LeetCode.PascalTriangle;

public class Solution
{
    public IList<IList<int>> Generate(int numRows)
    {
        // LeetCode constraint: 1 <= NumRows <= 30
        IList<IList<int>> tree = [[1]];
        for (int i = 1; i < numRows; i++)
        {
            var row = new List<int> { 1 };
            for (int j = 1; j < i; j++)
                row.Add(tree[i - 1][j - 1] + tree[i - 1][j]);
            row.Add(1);
            tree.Add(row);
        }
        return tree;
    }
}