/*
LeetCode problem 169. Majority Element
https://leetcode.com/problems/majority-element/description/
*/

namespace LeetCode.MajorityElement;

public class Solution
{
    public int MajorityElement(int[] nums)
    {
        int candidate = nums[0], count = 0;
        foreach (var n in nums)
        {
            if (count == 0)
                candidate = n;
            count += n == candidate ? 1 : -1;
        }
        return candidate;
    }
}