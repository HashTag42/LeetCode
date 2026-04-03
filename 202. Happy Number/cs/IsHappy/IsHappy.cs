/*
LeetCode problem 202. Happy Number
https://leetcode.com/problems/happy-number/description/
*/

namespace LeetCode.IsHappy;

public class Solution
{
    public bool IsHappy(int n)
    {
        var results = new HashSet<int>();
        while (true)
        {
            n = n.ToString().Sum(c => (c - '0') * (c - '0'));
            if (n == 1)
                return true;
            if (results.Contains(n))
                return false;
            results.Add(n);
        }
    }
}