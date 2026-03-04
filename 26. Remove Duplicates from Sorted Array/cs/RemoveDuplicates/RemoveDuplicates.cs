// LeetCode problem: 26. Remove Duplicates from Sorted Array
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

namespace LeetCode.RemoveDuplicates;

public class Solution
{
    public int RemoveDuplicates(int[] nums)
    {
        if (nums.Length == 0)
        {
            return 0;
        }

        int insertIndex = 1;
        for (int i = 1; i < nums.Length; i++)
        {
            if (nums[i - 1] != nums[i])
            {
                nums[insertIndex] = nums[i];
                insertIndex += 1;
            }
        }

        return insertIndex;
    }
}