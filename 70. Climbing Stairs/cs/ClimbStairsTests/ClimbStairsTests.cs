using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.ClimbStairs;

public class ClimbStairsTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<int, int> TestCases
    {
        get
        {
            var data = new TheoryData<int, int>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var n = ((JsonElement)row[0]).GetInt32();
                var expected = ((JsonElement)row[1]).GetInt32();
                data.Add(n, expected);
            }
            return data;
        }
    }

    [Theory(DisplayName = "ClimbStairs with varied inputs")]
    [MemberData(nameof(TestCases))]
    public void TestClimbStairs(int n, int expected)
    {
        Assert.Equal(expected, new Solution().ClimbStairs(n));
    }
}