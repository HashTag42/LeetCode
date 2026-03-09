using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.MyPow;

public class MyPowTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<double, int, double> TestCases
    {
        get
        {
            var data = new TheoryData<double, int, double>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var x = ((JsonElement)row[0]).GetDouble();
                var n = ((JsonElement)row[1]).GetInt32();
                var expected = ((JsonElement)row[2]).GetDouble();
                data.Add(x, n, expected);
            }
            return data;
        }
    }

    [Theory(DisplayName = "MyPow with varied inputs")]
    [MemberData(nameof(TestCases))]
    public void TestMyPow(double x, int n, double expected)
    {
        Assert.Equal(expected, Solution.MyPow(x, n), 5);
    }
}