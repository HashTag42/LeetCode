using System.Reflection;
using System.Text.Json;
using System.Text.RegularExpressions;

namespace Shared;

public static class TestDataLoader
{
    public static List<T[]> LoadArrayData<T>(string fileName)
    {
        var assemblyDir = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location)!;
        var jsonPath = Path.Combine(assemblyDir, fileName);
        var json = File.ReadAllText(jsonPath);

        // Strip comments if JSON5 file
        if (fileName.EndsWith(".json5", StringComparison.OrdinalIgnoreCase))
        {
            json = StripJson5Comments(json);
        }

        return JsonSerializer.Deserialize<List<T[]>>(json)!;
    }

    public static List<object[]> LoadNestedArrayData(string fileName)
    {
        var assemblyDir = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location)!;
        var jsonPath = Path.Combine(assemblyDir, fileName);
        var json = File.ReadAllText(jsonPath);

        // Strip comments if JSON5 file
        if (fileName.EndsWith(".json5", StringComparison.OrdinalIgnoreCase))
        {
            json = StripJson5Comments(json);
        }

        return JsonSerializer.Deserialize<List<object[]>>(json)!;
    }

    public static string[] ExtractStringArray(JsonElement element)
    {
        var list = new List<string>();
        foreach (var item in element.EnumerateArray())
        {
            list.Add(item.GetString()!);
        }
        return [.. list];
    }

    private static string StripJson5Comments(string json)
    {
        // Remove single-line comments (//)
        json = Regex.Replace(json, @"//.*?(\r?\n|$)", "$1");

        // Remove trailing commas before closing brackets/braces
        json = Regex.Replace(json, @",(\s*[}\]])", "$1");

        return json;
    }
}