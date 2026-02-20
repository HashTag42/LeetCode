using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.IsPalindrome;

public class IsPalindromTests
{
    public static TheoryData<int, bool> TestCases
    {
        get
        {
            var data = new TheoryData<int, bool>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var x = ((JsonElement)row[0]).GetInt32();
                var expected = bool.Parse(((JsonElement)row[1]).GetString()!);
                data.Add(x, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestIsPalindrome(int x, bool expected)
    {
        Assert.Equal(expected, new Solution().IsPalindrome(x));
    }
}
