/*
LeetCode problem 283. Move Zeroes
https://leetcode.com/problems/move-zeroes/description
*/

namespace LeetCode.MoveZeroes;

public class Solution
{
    public void MoveZeroes(int[] nums)
    {
        /*
        Do not return anything, modify nums in-place instead.
        Time complexity: O(n)
        Space complexity: O(1)
        */
        int numsCount = nums.Length;
        int insertIndex = 0;
        for (int n = 0; n < numsCount; n++)
        {
            if (nums[n] != 0)
            {
                nums[insertIndex] = nums[n];
                insertIndex++;
            }
        }
        for (int z = insertIndex; z < numsCount; z++)
        {
            nums[z] = 0;
        }
    }
}