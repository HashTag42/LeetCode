using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.IsPalindrome;

public class IsPalindromeTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<string, bool> TestCases
    {
        get
        {
            var data = new TheoryData<string, bool>();
            var rows = TestDataLoader.LoadNestedArrayData("testcase_data.json");
            foreach (var row in rows)
            {
                var s = ((JsonElement)row[0]).GetString();
                var expected = ((JsonElement)row[1]).GetBoolean();
                data.Add(s!, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestIsPalindrome1(string s, bool expected)
    {
        Assert.Equal(expected, new Solution().IsPalindrome1(s));
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestIsPalindrome2(string s, bool expected)
    {
        Assert.Equal(expected, new Solution().IsPalindrome2(s));
    }
}