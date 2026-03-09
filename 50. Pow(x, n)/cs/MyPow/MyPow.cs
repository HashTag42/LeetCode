// LeetCode problem: 50. Pow(x, n)
// https://leetcode.com/problems/powx-n/description/

namespace LeetCode.MyPow;

public class Solution
{
    public static double MyPow(double x, int n)
    {
        if (n == 0)
            return 1;
        long absN = Math.Abs((long)n);
        if (n < 0)
        {
            x = 1.0 / x;
            n = -n;
        }
        double result = 1.0;
        while (absN != 0)
        {
            if (absN % 2 == 1)
                result *= x;
            x *= x;
            absN /= 2;
        }
        return result;
    }
}