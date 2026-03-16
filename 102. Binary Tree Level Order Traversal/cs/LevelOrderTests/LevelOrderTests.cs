using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.LevelOrder;

public class LevelOrderTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    private static readonly List<object[]> TestCases =
        TestDataLoader.LoadNestedArrayData("test_cases.json");

    public static IEnumerable<object[]> GetTestCases() => TestCases;

    private static TreeNode? BuildTree(JsonElement element)
    {
        if (element.ValueKind is JsonValueKind.Null or JsonValueKind.Undefined)
            return null;

        var values = element.EnumerateArray().ToList();
        if (values.Count == 0)
            return null;

        var rootNode = new TreeNode(values[0].GetInt32());
        var queue = new Queue<TreeNode>();
        queue.Enqueue(rootNode);
        int i = 1;

        while (queue.Count > 0 && i < values.Count)
        {
            var node = queue.Dequeue();

            if (i < values.Count && values[i].ValueKind != JsonValueKind.Null)
            {
                node.left = new TreeNode(values[i].GetInt32());
                queue.Enqueue(node.left);
            }
            i++;

            if (i < values.Count && values[i].ValueKind != JsonValueKind.Null)
            {
                node.right = new TreeNode(values[i].GetInt32());
                queue.Enqueue(node.right);
            }
            i++;
        }

        return rootNode;
    }

    [Theory]
    [MemberData(nameof(GetTestCases))]
    public void Test_LevelOrder(JsonElement treeValues, JsonElement expected)
    {
        var tree = BuildTree(treeValues);
        var expectedList = expected.EnumerateArray()
            .Select(level => level.EnumerateArray().Select(e => e.GetInt32()).ToList())
            .ToList();

        var result = new Solution().LevelOrder(tree);

        Assert.Equal(expectedList, result);
    }
}
