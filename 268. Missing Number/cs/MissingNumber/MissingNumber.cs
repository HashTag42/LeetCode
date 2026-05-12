/*
LeetCode problem 268. Missing Number
https://leetcode.com/problems/missing-number/
*/

namespace LeetCode.MissingNumber;

public class Solution
{
    public int MissingNumber1(int[] nums)
    {
        /*
        Brute force approach
        Time complexity = O(n^2)
        Space complexity = O(1)
        */
        // LeetCode guarantees nums is a valid list with at least one element
        for (int i = 0; i < nums.Length; i++)
        {
            if (!nums.Contains(i))
                return i;
        }

        return nums.Length;
    }

    public int MissingNumber2(int[] nums)
    {
        /*
        Optimal approach
        Time complexity = O(n) to obtain sumOfElements
        Space complexity = O(1)
        */
        // LeetCode guarantees nums is a valid list with at least one element
        int n = nums.Length;
        int sumOfElements = nums.Sum();
        int actualSum = (n * (n + 1)) / 2;
        return actualSum - sumOfElements;
    }
}