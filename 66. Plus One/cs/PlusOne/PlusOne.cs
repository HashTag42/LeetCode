// LeetCode problem: 66. Plus One
// https://leetcode.com/problems/plus-one/

namespace LeetCode.PlusOne;

public class Solution
{
    public int[] PlusOne(int[] digits)
    {
        for (int i = digits.Length - 1; i >= 0; i--)
        {
            if (digits[i] < 9)
            {
                digits[i] += 1;
                return digits;
            }
            digits[i] = 0;
        }
        return [1, ..digits];
    }
}