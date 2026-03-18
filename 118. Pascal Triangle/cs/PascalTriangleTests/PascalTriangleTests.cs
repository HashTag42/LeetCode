using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.PascalTriangle;

public class GenerateTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    private static readonly List<object[]> TestCases =
        TestDataLoader.LoadNestedArrayData("test_cases.json");

    public static IEnumerable<object[]> GetTestCases() => TestCases;

    [Theory]
    [MemberData(nameof(GetTestCases))]
    public void Generate(JsonElement numRows, JsonElement expected)
    {
        var expectedList = expected.EnumerateArray()
            .Select(row => (IList<int>)row.EnumerateArray().Select(v => v.GetInt32()).ToList())
            .ToList<IList<int>>();

        var result = new Solution().Generate(numRows.GetInt32());

        Assert.Equal(expectedList, result);
    }
}


