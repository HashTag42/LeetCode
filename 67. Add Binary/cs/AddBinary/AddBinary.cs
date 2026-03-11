/*
 * LeetCode problem 67. Add Binary
 * https://leetcode.com/problems/add-binary/description/
 *
 * Given two binary strings a and b, return their sum as a binary string.
 */

namespace LeetCode.AddBinary;

public class Solution
{
    public string AddBinary(string a, string b)
    {
        var result = new System.Text.StringBuilder();
        int i = a.Length - 1, j = b.Length - 1, carry = 0;

        /* Traverse both strings from right to left, summing bits and carry */
        while (i >= 0 || j >= 0 || carry > 0)
        {
            int sum = carry;
            if (i >= 0) sum += a[i--] - '0';
            if (j >= 0) sum += b[j--] - '0';
            carry = sum / 2;
            result.Insert(0, sum % 2);
        }

        return result.ToString();
    }
}