using System.Text.Json;
using System.Text.Json.Nodes;
using Shared;
using Xunit;

namespace LeetCode.AddTwoNumbers;

public class AddTwoNumbersTests
{
    public static TheoryData<int[]?, int[]?, int[]?> TestCases
    {
        get
        {
            var data = new TheoryData<int[]?, int[]?, int[]?>();
            var rows = TestDataLoader.LoadNestedArrayData("addTwoNumbers_tests.json");
            foreach (var row in rows)
            {
                var list1 = row[0] is JsonElement list1El
                    ? list1El.EnumerateArray().Select(e => e.GetInt32()).ToArray()
                    : null;
                var list2 = row[1] is JsonElement list2El
                    ? list2El.EnumerateArray().Select(e => e.GetInt32()).ToArray()
                    : null;
                var expected = row[2] is JsonElement expectedEl
                    ? expectedEl.EnumerateArray().Select(e => e.GetInt32()).ToArray()
                    : null;
                data.Add(list1, list2, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestAddTwoNumbers(int[]? list1, int[]? list2, int[]? expected)
    {
        Assert.Equal(expected, Solution.AddTwoNumbers(list1, list2));
    }
}