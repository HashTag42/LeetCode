using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.StrStr;

public class StrStrTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<String?, String?, int> TestCases
    {
        get
        {
            var data = new TheoryData<String?, String?, int>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var haystack = ((JsonElement)row[0]).GetString();
                var needle =  ((JsonElement)row[1]).GetString();
                var expected = ((JsonElement)row[2]).GetInt32();
                data.Add(haystack, needle, expected);
            }
            return data;
        }
    }

    [Theory(DisplayName = "StrStr with varied inputs")]
    [MemberData(nameof(TestCases))]
    public void TestStrStr(String? haystack, String? needle, int expected)
    {
        Assert.Equal(expected, Solution.StrStr(haystack!, needle!));
    }
}