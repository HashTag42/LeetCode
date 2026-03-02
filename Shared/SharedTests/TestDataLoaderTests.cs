using System.Text.Json;
using Shared;
using Xunit;

namespace SharedTests;

public class TestDataLoaderTests
{
    [Fact]
    public void LoadArrayData_Json_ReturnsData()
    {
        var result = TestDataLoader.LoadArrayData<string>("test_data.json");

        Assert.Equal(2, result.Count);
        Assert.Equal(["hello", "world"], result[0]);
        Assert.Equal(["foo", "bar"], result[1]);
    }

    [Fact]
    public void LoadArrayData_Json5_StripsCommentsAndTrailingCommas()
    {
        var result = TestDataLoader.LoadArrayData<string>("test_data.json5");

        Assert.Equal(2, result.Count);
        Assert.Equal(["hello", "world"], result[0]);
        Assert.Equal(["foo", "bar"], result[1]);
    }

    [Fact]
    public void LoadNestedArrayData_Json5_StripsCommentsAndTrailingCommas()
    {
        var result = TestDataLoader.LoadNestedArrayData("test_data.json5");

        Assert.Equal(2, result.Count);
    }

    [Fact]
    public void ExtractStringArray_ReturnsStrings()
    {
        var json = JsonDocument.Parse("[\"hello\", \"world\"]");
        var result = TestDataLoader.ExtractStringArray(json.RootElement);

        Assert.Equal(["hello", "world"], result);
    }
}
