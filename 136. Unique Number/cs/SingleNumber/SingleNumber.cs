/*
Leet Code problem 136. Unique Number
https://leetcode.com/problems/single-number/
*/

namespace LeetCode.SingleNumber;

public class Solution
{
    public int SingleNumber(int[] nums)
    {
        int result = 0;
        foreach (var n in nums)
            result ^= n;
        return result;
    }
}
