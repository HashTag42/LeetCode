using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.SearchBST;

public class SearchBSTTests
{
    public static TheoryData<int[], int, int[]> TestCases
    {
        get
        {
            var data = new TheoryData<int[], int, int[]>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var root = ExtractIntArray((JsonElement)row[0]);
                var val = ((JsonElement)row[1]).GetInt32();
                var expected = ExtractIntArray((JsonElement)row[2]);
                data.Add(root, val, expected);
            }
            return data;
        }
    }

    private static int[] ExtractIntArray(JsonElement element)
    {
        var list = new List<int>();
        foreach (var item in element.EnumerateArray())
        {
            list.Add(item.GetInt32());
        }
        return [.. list];
    }

    private static TreeNode? ListToTree(int[] vals)
    {
        if (vals.Length == 0) return null;
        var root = new TreeNode(vals[0]);
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        int i = 1;
        while (queue.Count > 0 && i < vals.Length)
        {
            var node = queue.Dequeue();
            if (i < vals.Length)
            {
                node.left = new TreeNode(vals[i]);
                queue.Enqueue(node.left);
            }
            i++;
            if (i < vals.Length)
            {
                node.right = new TreeNode(vals[i]);
                queue.Enqueue(node.right);
            }
            i++;
        }
        return root;
    }

    private static int[] TreeToList(TreeNode? root)
    {
        if (root == null) return [];
        var result = new List<int?>();
        var queue = new Queue<TreeNode?>();
        queue.Enqueue(root);
        while (queue.Count > 0)
        {
            var node = queue.Dequeue();
            if (node != null)
            {
                result.Add(node.val);
                queue.Enqueue(node.left);
                queue.Enqueue(node.right);
            }
            else
            {
                result.Add(null);
            }
        }
        while (result.Count > 0 && result[^1] == null)
        {
            result.RemoveAt(result.Count - 1);
        }
        return result.Select(v => v!.Value).ToArray();
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestSearchBST(int[] root, int val, int[] expected)
    {
        var sol = new Solution();
        var tree = ListToTree(root);
        var result = sol.SearchBST(tree!, val);
        Assert.Equal(expected, TreeToList(result));
    }
}
