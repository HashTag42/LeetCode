using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.PlusOne;

public class PlusOneTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<int[]?, int[]?> TestCases
    {
        get
        {
            var data = new TheoryData<int[]?, int[]?>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var digits = row[0] is JsonElement digitElement
                ? digitElement.EnumerateArray().Select(e => e.GetInt32()).ToArray()
                : null;
                var expected = row[1] is JsonElement expectedElement
                ? expectedElement.EnumerateArray().Select(e => e.GetInt32()).ToArray()
                : null;
                data.Add(digits, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestPlusOne(int[]? digits, int[]? expected)
    {
        Assert.Equal(expected, new Solution().PlusOne(digits!));
    }
}