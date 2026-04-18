using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.ContainsNearbyDuplicate;

public class ContainsNearbyDuplicateTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<int[], int, bool> TestCases
    {
        get
        {
            var data = new TheoryData<int[], int, bool>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var nums = ((JsonElement)row[0]).EnumerateArray().Select(e => e.GetInt32()).ToArray();
                var k = ((JsonElement)row[1]).GetInt32();
                var expected = ((JsonElement)row[2]).GetBoolean();
                data.Add(nums, k, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestContainsNearbyDuplicate(int[] nums, int k, bool expected)
    {
        Assert.Equal(expected, new Solution().ContainsNearbyDuplicate(nums, k));
    }
}