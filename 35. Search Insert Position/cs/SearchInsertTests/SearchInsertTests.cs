using System.ComponentModel;
using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.SearchInsert;

public class SearchInsertTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<int[]?, int, int> TestCases
    {
        get
        {
            var data = new TheoryData<int[]?, int, int>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var nums = row[0] is JsonElement listElement
                    ? listElement.EnumerateArray().Select(e => e.GetInt32()).ToArray()
                    : null;
                var target = ((JsonElement)row[1]).GetInt32();
                var expected = ((JsonElement)row[2]).GetInt32();
                data.Add(nums, target, expected);
            }
            return data;
        }
    }

    [Theory(DisplayName = "SearchInsert with varied inputs")]
    [MemberData(nameof(TestCases))]
    public void TestSearchInsert(int[]? nums, int target, int expected)
    {
        Assert.Equal(expected, new Solution().SearchInsert(nums!, target));
    }
}