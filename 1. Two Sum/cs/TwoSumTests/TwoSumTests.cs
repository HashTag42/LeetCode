using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.TwoSum;

public class TwoSumTests
{
    public static TheoryData<int[]?, int, int[]?> TestCases
    {
        get
        {
            var data = new TheoryData<int[]?, int, int[]?>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var nums = row[0] is JsonElement numsEl
                    ? numsEl.EnumerateArray().Select(e => e.GetInt32()).ToArray()
                    : null;
                var target = ((JsonElement)row[1]).GetInt32();
                var expected = row[2] is JsonElement expectedEl
                    ? expectedEl.EnumerateArray().Select(e => e.GetInt32()).ToArray()
                    : null;
                data.Add(nums, target, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestTwoSum(int[]? nums, int target, int[]? expected)
    {
        Assert.Equal(expected, Solution.TwoSum(nums, target));
    }
}