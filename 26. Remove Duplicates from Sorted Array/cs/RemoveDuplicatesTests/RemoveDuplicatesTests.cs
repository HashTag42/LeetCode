using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.RemoveDuplicates;

public class RemoveDuplicatesTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<int[]?, int> TestCases
    {
        get
        {
            var data = new TheoryData<int[]?, int>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var list = row[0] is JsonElement listEl
                    ? listEl.EnumerateArray().Select(e => e.GetInt32()).ToArray()
                    : null;
                var expected = ((JsonElement)row[1]).GetInt32();
                data.Add(list, expected);
            }
            return data;
        }
    }

    [Theory(DisplayName = "RemoveDuplicates with varied inputs")]
    [MemberData(nameof(TestCases))]
    public void TestRemoveDuplicates(int[]? list, int expected)
    {
        if (list is null)
            return;

        var solution = new Solution();
        Assert.Equal(expected, solution.RemoveDuplicates(list));
    }
}