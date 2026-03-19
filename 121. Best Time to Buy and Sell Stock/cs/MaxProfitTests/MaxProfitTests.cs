using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.MaxProfit;

public class MaxProfitTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<int[], int> TestCases
    {
        get
        {
            var data = new TheoryData<int[], int>();
            var rows = TestDataLoader.LoadNestedArrayData("testcase_data.json");
            foreach (var row in rows)
            {
                var prices = ((JsonElement)row[0]).EnumerateArray().Select(e => e.GetInt32()).ToArray();
                var expected = ((JsonElement)row[1]).GetInt32();
                data.Add(prices, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestMaxProfit(int[] prices, int expected)
    {
        Assert.Equal(expected, new Solution().MaxProfit(prices));
    }
}