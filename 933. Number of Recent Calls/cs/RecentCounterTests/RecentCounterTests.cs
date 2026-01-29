using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.RecentCounter;

public class RecentCounterTests
{
    public static TheoryData<int[], int[]> TestCases
    {
        get
        {
            var data = new TheoryData<int[], int[]>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var inputs = ((JsonElement)row[0]).EnumerateArray()
                    .Select(e => e.GetInt32())
                    .ToArray();
                var expected = ((JsonElement)row[1]).EnumerateArray()
                    .Select(e => e.GetInt32())
                    .ToArray();
                data.Add(inputs, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestRecentCounter(int[] inputs, int[] expected)
    {
        var counter = new RecentCounter();
        List<int> result = [];
        foreach (var t in inputs)
        {
            result.Add(counter.Ping(t));
        }

        Assert.Equal(expected, result);
    }
}