using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.IsAnagram;

public class IsAnagramTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<string, string, bool> TestCases
    {
        get
        {
            var data = new TheoryData<string, string, bool>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var s = ((JsonElement)row[0]).GetString()!;
                var t = ((JsonElement)row[1]).GetString()!;
                var expected = ((JsonElement)row[2]).GetBoolean();
                data.Add(s, t, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestIsAnagram(string s, string t, bool expected)
    {
        Assert.Equal(expected, new Solution().IsAnagram(s, t));
    }
}