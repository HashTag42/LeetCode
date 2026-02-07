using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.LengthOfLastWord;

public class LengthOfLastWordTests
{
    public static TheoryData<string, int> TestCases
    {
        get
        {
            var data = new TheoryData<string, int>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                data.Add(((JsonElement)row[0]).GetString()!, ((JsonElement)row[1]).GetInt32());
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestLengthOfLastWord(string s, int expected)
    {
        Assert.Equal(expected, Solution.LengthOfLastWord(s));
    }
}