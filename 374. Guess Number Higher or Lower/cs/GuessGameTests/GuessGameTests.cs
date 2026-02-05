using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.GuessGame;

public class GuessGameTests
{
    public static TheoryData<int, int> TestCases
    {
        get
        {
            var data = new TheoryData<int, int>();
            var rows = TestDataLoader.LoadArrayData<int>("test_cases.json");
            foreach (var row in rows)
            {
                data.Add((int)row[0], (int)row[1]);
            }
            return data;
        }
    }

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestGuessGame(int num, int pick)
    {
        GuessGame gg = new(pick);
        var result = gg.GuessNumber(num);
        Assert.Equal(pick, result);
    }
}