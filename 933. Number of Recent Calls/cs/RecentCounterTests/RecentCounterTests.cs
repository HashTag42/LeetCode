using Xunit;

namespace LeetCode.RecentCounter;

public class RecentCounterTests
{
    [Fact]
    public void TestRecentCounter()
    {
        List<int> inputs = [1, 100, 3001, 3002];
        List<int> expected = [1, 2, 3, 3];

        var counter = new RecentCounter();
        List<int> result = [];
        foreach (var t in inputs)
        {
            result.Add(counter.Ping(t));
        }

        Assert.Equal(expected, result);
    }
}