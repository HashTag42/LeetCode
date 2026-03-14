using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.MergeSortedArray;

public class MergeSortedArrayTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<int[], int, int[], int, int[]> TestCases
    {
        get
        {
            var data = new TheoryData<int[], int, int[], int, int[]>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var nums1 = row[0] is JsonElement digitElement
                ? digitElement.EnumerateArray().Select(e => e.GetInt32()).ToArray()
                : null;
                var m = ((JsonElement)row[1]).GetInt32();
                var nums2 = row[2] is JsonElement nums2Element
                ? nums2Element.EnumerateArray().Select(e => e.GetInt32()).ToArray()
                : null;
                var n = ((JsonElement)row[3]).GetInt32();
                var expected = row[4] is JsonElement expectedElement
                ? expectedElement.EnumerateArray().Select(e => e.GetInt32()).ToArray()
                : null;
                data.Add(nums1!, m, nums2!, n, expected!);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestMergeSortedArray(int[] nums1, int m, int[] num2, int n, int[] expected)
    {
        Assert.Equal(expected, new Solution().MergeSortedArray(nums1, m, num2, n));
    }
}