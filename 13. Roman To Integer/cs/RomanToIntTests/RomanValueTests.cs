using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.RomanToInt;

public class RomanValueTests
{
    public static TheoryData<string, int> TestCases
    {
        get
        {
            var data = new TheoryData<string, int>();
            var rows = TestDataLoader.LoadNestedArrayData("roman_value_test_cases.json");
            foreach (var row in rows)
            {
                var s = ((JsonElement)row[0]).GetString()!;
                var expected = ((JsonElement)row[1]).GetInt32();
                data.Add(s, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestRomanValue(string s, int expected)
    {
        Assert.Equal(expected, Solution.RomanValue(s));
    }
}