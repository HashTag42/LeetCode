using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.ReverseList;

public class ReverseListTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<int[], int[]> TestCases
    {
        get
        {
            var data = new TheoryData<int[], int[]>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var nodes = ((JsonElement)row[0]).EnumerateArray().Select(e => e.GetInt32()).ToArray();
                var expected = ((JsonElement)row[1]).EnumerateArray().Select(e => e.GetInt32()).ToArray();
                data.Add(nodes, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestReverseList(int[] nodes, int[] expected)
    {
        var inHead = ToLinkedList(nodes);
        var outHead = new Solution().ReverseList(inHead);
        Assert.Equal(expected, ToArray(outHead));
    }

    private static ListNode? ToLinkedList(int[] values)
    {
        if (values.Length == 0)
            return null;

        var head = new ListNode(values[0]);
        var current = head;
        for (int i = 1; i < values.Length; i++)
        {
            current.next = new ListNode(values[i]);
            current = current.next;
        }
        return head;
    }

    private static int[] ToArray(ListNode? head)
    {
        var values = new List<int>();
        var current = head;
        while (current != null)
        {
            values.Add(current.val);
            current = current.next;
        }
        return values.ToArray();
    }
}