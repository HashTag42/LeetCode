using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.ValidParentheses;

public class ValidParenthesesTests
{
    public static TheoryData<string, bool> TestCases
    {
        get
        {
            var data = new TheoryData<string, bool>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var s = ((JsonElement)row[0]).GetString()!;
                var expected = ((JsonElement)row[1]).GetBoolean();
                data.Add(s, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestIsValid(string s, bool expected)
    {
        Assert.Equal(expected, new Solution().IsValid(s));
    }
}
