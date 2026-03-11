using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.AddBinary;

public class AddBinaryTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

    public static TheoryData<string?, string?, string?> TestCases
    {
        get
        {
            var data = new TheoryData<string?, string?, string?>();
            var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
            foreach (var row in rows)
            {
                var a = ((JsonElement)row[0]).GetString();
                var b = ((JsonElement)row[1]).GetString();
                var expected = ((JsonElement)row[2]).GetString();
                data.Add(a, b, expected);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestAddBinary(string? a, string? b, string? expected)
    {
        Assert.Equal(expected, new Solution().AddBinary(a!, b!));
    }
}