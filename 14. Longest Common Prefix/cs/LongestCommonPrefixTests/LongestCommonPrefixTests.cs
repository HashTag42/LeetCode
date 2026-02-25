using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.LongestCommonPrefix;

public class LongestCommonPrefixTests
{
    public static TheoryData<string[], string> TestCases
    {
        get
        {
            var data = new TheoryData<string[], string>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var strs = TestDataLoader.ExtractStringArray((JsonElement)row[0]);
                var expected = ((JsonElement)row[1]).GetString() ?? string.Empty;
                data.Add(strs, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestLongestCommonPrefix(string[] strs, string expected)
    {
        var solution = new Solution();
        Assert.Equal(expected, solution.LongestCommonPrefix(strs));
    }
}