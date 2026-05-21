using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.MoveZeroes;

public class MoveZeroesTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<int[], int[]> TestCases
    {
        get
        {
            var data = new TheoryData<int[], int[]>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var nums = ((JsonElement)row[0]).EnumerateArray().Select(e => e.GetInt32()).ToArray();
                var expected = ((JsonElement)row[1]).EnumerateArray().Select(e => e.GetInt32()).ToArray();
                data.Add(nums, expected);
            }

            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestMovingZeroes(int[] nums, int[] expected)
    {
        new Solution().MoveZeroes(nums);
        Assert.Equal(expected, nums);
    }
}