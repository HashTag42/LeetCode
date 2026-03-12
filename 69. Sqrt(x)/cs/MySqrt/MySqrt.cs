// LeetCode problem: 69. Sqrt(x)
// https://leetcode.com/problems/sqrtx/

namespace LeetCode.MySqrt;

public class Solution
{
    public int MySqrt(int x)
    {
        int lo = 0, hi = x;
        while (lo <= hi)
        {
            int mid = lo + (hi - lo) / 2;
            long sq = (long)mid * mid;
            if (sq == x)
                return mid;
            else if (sq < x)
                lo = mid + 1;
            else
                hi = mid - 1;
        }
        return hi;
    }
}