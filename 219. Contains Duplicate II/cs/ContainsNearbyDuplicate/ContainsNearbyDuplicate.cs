/*
LeetCode problem 219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/
*/

namespace LeetCode.ContainsNearbyDuplicate;

public class Solution
{
    public bool ContainsNearbyDuplicate(int[] nums, int k)
    {
        var seen = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++)
        {
            int num = nums[i];
            if (seen.TryGetValue(num, out int prevIndex) && i - prevIndex <= k)
                return true;
            seen[num] = i;
        }
        return false;
    }
}