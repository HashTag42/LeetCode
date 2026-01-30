using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.MinCostClimbingStairs;

public class MinCostClimbingStairsTests
{
    public static TheoryData<int[], int> TestCases
    {
        get
        {
            var data = new TheoryData<int[], int>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var costs = ((JsonElement)row[0]).EnumerateArray()
                    .Select(e => e.GetInt32())
                    .ToArray();
                var expected = ((JsonElement)row[1]).GetInt32();
                data.Add(costs, expected);
            }

            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestMinCostClimbingStairs(int[] costs, int expected)
    {
        Assert.Equal(expected, MinCostClimbingStairs.Calculate(costs));
    }
}