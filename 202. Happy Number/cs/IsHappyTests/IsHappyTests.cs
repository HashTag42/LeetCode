using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.IsHappy;

public class IsHappyTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<int, bool> TestCases
    {
        get
        {
            var data = new TheoryData<int, bool>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var n = ((JsonElement)row[0]).GetInt32();
                var expected = ((JsonElement)row[1]).GetBoolean();
                data.Add(n, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestIsHappy(int n, bool expected)
    {
        Assert.Equal(expected, new Solution().IsHappy(n));
    }
}