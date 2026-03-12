using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.MySqrt;

public class MySqrtTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<int, int> TestCases
    {
        get
        {
            var data = new TheoryData<int, int>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var x = ((JsonElement)row[0]).GetInt32();
                var expected = ((JsonElement)row[1]).GetInt32();
                data.Add(x, expected);
            }
            return data;
        }
    }

    [Theory(DisplayName = "MySqrt with varied inputs")]
    [MemberData(nameof(TestCases))]
    public void TestMySqrt(int x, int expected)
    {
        Assert.Equal(expected, new Solution().MySqrt(x));
    }
}