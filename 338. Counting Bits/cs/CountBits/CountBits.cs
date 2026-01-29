/*
LeetCode problem 338. Counting Bits
https://leetcode.com/problems/counting-bits/description/

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's
in the binary representation of i.

Example 1:
    Input: n = 2
    Output: [0,1,1]
    Explanation:
        0 --> 0
        1 --> 1
        2 --> 10

Example 2:
    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
        3 --> 11
        4 --> 100
        5 --> 101
*/
namespace LeetCode.CountBits;

public class CountBits
{
    // Complexity:
    //      Time: O(n log n)
    //      Space: O(n)
    public static int[] Solve(int n)
    {
        int[] result = new int[n + 1];
        for (int i = 0; i < n + 1; i++)
        {
            string binary = Convert.ToString(i, 2);
            int count = 0;
            foreach (char ch in binary)
            {
                if (ch == '1')
                {
                    count++;
                }
            }
            result[i] = count;
        }
        return result;
    }
}