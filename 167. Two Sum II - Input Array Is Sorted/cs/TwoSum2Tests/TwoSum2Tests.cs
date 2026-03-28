using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.TwoSum2;

public class TwoSum2Tests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<int[], int, int[]> TestCases
    {
        get
        {
            var data = new TheoryData<int[], int, int[]>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var numbers = ((JsonElement)row[0]).EnumerateArray().Select(e => e.GetInt32()).ToArray();
                var target = ((JsonElement)row[1]).GetInt32();
                var expected = ((JsonElement)row[2]).EnumerateArray().Select(e => e.GetInt32()).ToArray();
                data.Add(numbers, target, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestTwoSum2(int[] numbers, int target, int[] expected)
    {
        Assert.Equal(expected, new Solution().TwoSum2(numbers, target));
    }

    [Fact]
    public void TwoSum2_NoSolution_ThrowsInvalidOperationException()
    {
        Assert.Throws<InvalidOperationException>(() => new Solution().TwoSum2([1, 2], 100));
    }
}