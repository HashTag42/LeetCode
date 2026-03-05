// LeetCode Problem: 27. Remove Element
// https://leetcode.com/problems/remove-element/description/

namespace LeetCode.RemoveElement;

public class Solution
{
    public int RemoveElement(int[] nums, int val)
    {
        int index = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] != val)
                nums[index++] = nums[i];
        }
        return index;
    }
}