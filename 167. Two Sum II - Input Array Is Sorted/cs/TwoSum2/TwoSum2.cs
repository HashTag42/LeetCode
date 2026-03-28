/*
    LeetCode problem 167. Two Sum II - Input Array Is Sorted
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
*/

namespace LeetCode.TwoSum2;

public class Solution()
{
    public int[] TwoSum2(int[] numbers, int target)
    {
        int left = 0, right = numbers.Length - 1;
        while (left < right)
        {
            int s = numbers[left] + numbers[right];
            if (s == target)
                return [left + 1, right + 1];
            else if (s < target)
                left += 1;
            else
                right -= 1;
        }
        throw new InvalidOperationException("No solution found.");
    }
}