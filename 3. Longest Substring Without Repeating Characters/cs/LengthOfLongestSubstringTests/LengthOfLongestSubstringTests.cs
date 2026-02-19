using System.Text.Json;
using System.Text.Json.Nodes;
using Shared;
using Xunit;

namespace LeetCode.LengthOfLongestSubstring;

public class LengthOfLongestSubstringTests
{
    public static TheoryData<string, int> TestCases
    {
        get
        {
            var data = new TheoryData<string, int>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var s = (JsonElement)row[0];
                var expected = ((JsonElement)row[1]).GetInt32();
                data.Add(s, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestLengthOfLongestSubstring(string s, int expected)
    {
        Assert.Equal(expected, Solution.LengthOfLongestSubstring(s));
    }
}