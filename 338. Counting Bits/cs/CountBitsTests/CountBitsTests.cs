using Xunit;

namespace LeetCode.CountBits;

public class CountBitsTests
{
    public static TheoryData<int, int[]> TestCases => new()
    {
        { 2, [0, 1, 1] },
        { 5, [0, 1, 1, 2, 1, 2] },
    };

    [Theory]
    [MemberData(nameof(TestCases))]
    public void TestCountBits(int n, int[] expected)
    {
        Assert.Equal(expected, CountBits.Solve(n));
    }
}
