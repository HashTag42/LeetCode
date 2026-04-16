using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.ContainsDuplicate;

public class ContainsDuplicateTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<int[], bool> TestCases
    {
        get
        {
            var data = new TheoryData<int[], bool>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var nums = ((JsonElement)row[0]).EnumerateArray().Select(e => e.GetInt32()).ToArray();
                var expected = ((JsonElement)row[1]).GetBoolean();
                data.Add(nums, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestContainsDuplicate(int[] nums, bool expected)
    {
        Assert.Equal(expected, new Solution().ContainsDuplicate(nums));
    }
}