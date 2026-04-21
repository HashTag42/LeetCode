/*
LeetCode problem 231. Power of Two
https://leetcode.com/problems/power-of-two/
*/

namespace LeetCode.IsPowerOfTwo;

public class Solution
{
    public bool IsPowerOfTwo(int n)
    {
        return (n > 0 && (n & (n - 1)) == 0);
    }
}