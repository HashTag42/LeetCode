// LeetCode challenge: 1. Two Sum: <https://leetcode.com/problems/two-sum/description/>

namespace LeetCode.TwoSum;

public class Solution
{
    public static int[]? TwoSum(int[]? nums, int target)
    {
        if (nums == null || nums.Length < 2)
            return null;
        for (int i = 0; i < nums.Length; i++)
            for (int j = i + 1; j < nums.Length; j++)
                if (nums[i] + nums[j] == target)
                    return [i, j];
        return null;
    }
}