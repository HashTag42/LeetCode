/*
LeetCode problem 217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
*/

namespace LeetCode.ContainsDuplicate;

public class Solution
{
    public bool ContainsDuplicate(int[] nums)
    {
        var seen = new HashSet<int>();
        foreach (var item in nums)
        {
            if (!seen.Add(item))
                return true;
        }
        return false;
    }
}