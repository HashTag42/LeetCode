// LeetCode problem 70. Climbing Stairs
// https://leetcode.com/problems/climbing-stairs/description/

namespace LeetCode.ClimbStairs;

public class Solution
{
    public int ClimbStairs(int n)
    {
        return Fibonacci(n);
    }

    private static int Fibonacci(int n)
    {
        // LeetCode guarantees that n >= 1
        if (n == 1)
            return 1;
        if (n == 2)
            return 2;

        int a = 1, b = 2;
        for (int i = 3; i <= n; i++)
            (a, b) = (b, a + b);

        return b;
    }
}