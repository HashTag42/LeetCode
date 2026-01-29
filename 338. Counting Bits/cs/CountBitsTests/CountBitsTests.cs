using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.CountBits;

public class CountBitsTests
{
    public static TheoryData<int, int[]> TestCases
    {
        get
        {
            var data = new TheoryData<int, int[]>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var n = ((JsonElement)row[0]).GetInt32();
                var expected = ((JsonElement)row[1]).EnumerateArray()
                    .Select(e => e.GetInt32())
                    .ToArray();
                data.Add(n, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestCountBits(int n, int[] expected)
    {
        Assert.Equal(expected, CountBits.Solve(n));
    }
}
